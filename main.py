from prompt_Optimizer.predict import generate_prompt

if __name__ == "__main__":
    user_input = input("Enter your requirement: ")
    tone = input("Enter tone (professional/casual/motivational): ")
    length = input("Enter length (short/medium/long): ")

    print("\n--- AI Generated Prompt ---\n")
    result = generate_prompt(user_input)
    print(result)