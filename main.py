from prompt_Optimizer.utils import detect_type
from prompt_Optimizer.templates import (
    linkedin_template,
    resume_template,
    ppt_template,
    email_template,
    coding_template,
    explanation_template,
    webapp_template
)

def enhance_prompt(user_input, tone, length):
    category = detect_type(user_input)

    if category == "linkedin":
        return linkedin_template(user_input, tone, length)
    elif category == "resume":
        return resume_template(user_input, tone, length)
    elif category == "ppt":
        return ppt_template(user_input, tone, length)
    elif category == "email":
        return email_template(user_input, tone, length)
    elif category == "coding":
        return coding_template(user_input, tone, length)
    elif category == "explanation":
        return explanation_template(user_input, tone, length)
    elif category == "webapp":
        return webapp_template(user_input, tone, length)
    else:
        return "Sorry, could not understand the request."

if __name__ == "__main__":
    user_input = input("Enter your requirement: ")
    tone = input("Enter tone (professional/casual/motivational): ")
    length = input("Enter length (short/medium/long): ")

    result = enhance_prompt(user_input, tone, length)

    print("\nOptimized Prompt:\n")
    print(result)