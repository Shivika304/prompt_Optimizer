from utils import detect_type
from templates import (
    linkedin_template,
    resume_template,
    ppt_template,
    email_template,
    coding_template,
    explanation_template,
    webapp_template
)

def enhance_prompt(user_input):
    category = detect_type(user_input)

    if category == "linkedin":
        return linkedin_template(user_input)
    elif category == "resume":
        return resume_template(user_input)
    elif category == "ppt":
        return ppt_template(user_input)
    elif category == "email":
        return email_template(user_input)
    elif category == "coding":
        return coding_template(user_input)
    elif category == "explanation":
        return explanation_template(user_input)
    elif category == "webapp":
        return webapp_template(user_input)
    else:
        return "Sorry, could not understand the request."

if __name__ == "__main__":
    user_input = input("Enter your requirement: ")

    result = enhance_prompt(user_input)

    print("\nOptimized Prompt:\n")
    print(result)