from fuzzywuzzy import fuzz

def detect_type(text):
    text = text.lower()
    words = text.split()

    for word in words:
        if fuzz.ratio(word, "linkedin") > 80:
            return "linkedin"
        elif fuzz.ratio(word, "resume") > 80:
            return "resume"

    return "general"