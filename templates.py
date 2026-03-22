from utils import refine_goal

def linkedin_template(user_input):
    return f"""
Act as an expert content strategist.

Create a high-quality LinkedIn post (150–300 words) based on the following idea:

User Input:
{user_input}

Goal:
{refine_goal(user_input)}

Instructions:
- Start with a strong and attention-grabbing hook
- Maintain a relatable and professional tone
- Expand the idea with meaningful insights or real-life relevance
- Ensure the content is suitable for a broad audience
- Keep the structure clear and engaging
- End with a thought-provoking question or call-to-action

Output Format:
- Well-structured paragraphs
- Clear flow of ideas
"""

def resume_template(user_input):
    return f"""
Act as an expert resume writer.

Transform the following input into a strong, ATS-friendly resume bullet point:

User Input:
{user_input}

Goal:
{refine_goal(user_input)}

Instructions:
- Use strong action verbs (e.g., Developed, Implemented, Designed)
- Highlight key skills and technologies
- Add measurable impact if possible
- Keep it concise and results-oriented
- Ensure clarity and professionalism

Output Format:
- 1–2 impactful bullet points
"""


def ppt_template(user_input):
    return f"""
Act as a presentation expert.

Create a structured PPT outline based on:

User Input:
{user_input}

Instructions:
- Divide content into clear slides
- Keep points concise and easy to understand
- Include headings and bullet points
- Ensure logical flow of content

Output Format:
- Slide-wise structure
"""

def email_template(user_input):
    return f"""
Act as a professional email writer.

Write a clear and effective email based on:

User Input:
{user_input}

Instructions:
- Use a professional tone
- Keep it concise and polite
- Clearly state purpose
- Include proper opening and closing

Output Format:
- Subject line
- Email body
"""

def coding_template(user_input):
    return f"""
Act as a software engineer.

Provide a clear and structured coding solution for:

User Input:
{user_input}

Instructions:
- Explain approach step-by-step
- Provide clean and readable code
- Add comments where necessary
- Optimize for efficiency

Output Format:
- Explanation + Code
"""

def explanation_template(user_input):
    return f"""
Act as an expert educator.

Explain the following topic clearly:

User Input:
{user_input}

Instructions:
- Use simple language
- Break down concepts step-by-step
- Include examples if needed
- Keep it easy to understand

Output Format:
- Structured explanation
"""

def webapp_template(user_input):
    return f"""
Act as a full-stack developer.

Design a complete web application based on the following requirement:

User Input:
{user_input}

Instructions:
- Clearly define the problem and solution
- Suggest frontend and backend technologies
- Describe key features and functionalities
- Outline system architecture (frontend, backend, database)
- Include API structure if applicable
- Suggest possible improvements or future enhancements

Output Format:
- Project overview
- Features list
- Tech stack
- Architecture explanation
"""
