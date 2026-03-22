from utils import detect_type
from templates import linkedin_template, resume_template, general_template

def enhance_prompt(user_input):
    category = detect_type(user_input)

    if category == "linkedin":
        return linkedin_template(user_input)
    elif category == "resume":
        return resume_template(user_input)
    else:
        return general_template(user_input)


if __name__ == "__main__":
    user_input = input("Enter your requirement: ")
    result = enhance_prompt(user_input)

    print("\nOptimized Prompt:\n")
    print(result)