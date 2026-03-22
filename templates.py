def linkedin_template(user_input):
    return f"""
Write a LinkedIn post (150-200 words)

Tone:
- Relatable
- Professional
- Engaging

Instructions:
- Make it suitable for a broad audience
- Add a strong hook at the beginning
- Keep it concise and impactful

Topic:
{user_input}
"""


def resume_template(user_input):
    return f"""
Create a professional resume bullet point based on the following:

Task:
{user_input}

Instructions:
- Use action verbs (e.g., Developed, Implemented, Designed)
- Keep it concise and impactful
- Highlight skills and outcomes
- Make it ATS-friendly
- Add measurable results if possible

Output format:
- Bullet point (1–2 lines)
"""


def general_template(user_input):
    return f"""
Provide a clear, structured, and high-quality response for the following:

Task:
{user_input}

Instructions:
- Use simple and easy-to-understand language
- Organize content into sections or bullet points
- Be concise but informative
- Include examples if helpful
- Ensure clarity and readability
"""