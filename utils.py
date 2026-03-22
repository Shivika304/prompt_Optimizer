from fuzzywuzzy import fuzz

def detect_type(text):
    text = text.lower()
    words = text.split()

    for word in words:
        if fuzz.ratio(word, "linkedin") > 80:
            return "linkedin"
        if fuzz.ratio(word, "resume") > 80 or fuzz.ratio(word, "cv") > 80:
            return "resume"
        if fuzz.ratio(word, "ppt") > 80 or fuzz.ratio(word, "presentation") > 80:
            return "ppt"
        if fuzz.ratio(word, "email") > 80 or fuzz.ratio(word, "mail") > 80:
            return "email"
        if fuzz.ratio(word, "code") > 80 or fuzz.ratio(word, "program") > 80:
            return "coding"
        if fuzz.ratio(word, "web") > 80 or fuzz.ratio(word, "website") > 80 or fuzz.ratio(word, "app") > 80:
            return "webapp"
        if fuzz.ratio(word, "explain") > 80:
            return "explanation"

    return "unknown"

def refine_goal(text):
    text = text.lower()

    # Action-based detection
    if any(word in text for word in ["encourage", "motivate", "inspire"]):
        return f"Encourage and inspire the audience regarding: {text}"

    elif any(word in text for word in ["explain", "understand", "learn"]):
        return f"Provide a clear and simple explanation about: {text}"

    elif any(word in text for word in ["guide", "how", "steps", "build"]):
        return f"Provide step-by-step guidance for: {text}"

    elif any(word in text for word in ["create", "design", "develop"]):
        return f"Design or create a structured solution for: {text}"

    elif any(word in text for word in ["resume", "cv"]):
        return f"Present the information in a professional resume format based on: {text}"

    elif any(word in text for word in ["post", "linkedin"]):
        return f"Generate an engaging and high-quality LinkedIn post about: {text}"

    else:
        return f"Provide a clear, structured, and valuable response for: {text}"