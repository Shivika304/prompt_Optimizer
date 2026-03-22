from prompt_Optimizer.utils import refine_goal

def linkedin_template(user_input, tone, length):
    return f"""
Act as an expert content strategist.

Create a LinkedIn post based on the following:

Topic:
{user_input}

Tone:
{tone}

Length:
{length}

Goal:
{refine_goal(user_input)}

Guidelines:
- Start with an engaging hook
- Maintain a natural and relatable flow
- Add meaningful insights or perspective
- Keep it clear and impactful
- End with a thought-provoking question or CTA
"""

def resume_template(user_input, tone, length):
    return f"""
Act as an expert resume writer.

Improve the following into a strong resume bullet point:

Input:
{user_input}

Tone:
Professional

Length:
Concise

Goal:
{refine_goal(user_input)}

Guidelines:
- Use strong action verbs
- Highlight impact and results
- Mention relevant skills or tools
- Keep it clear and ATS-friendly
"""


def ppt_template(user_input, tone, length):
    return f"""
Act as a presentation expert.

Create a structured PPT outline for:

Topic:
{user_input}

Tone:
{tone}

Length:
{length}

Goal:
{refine_goal(user_input)}

Guidelines:
- Divide content into slides
- Use short and clear bullet points
- Maintain logical flow
- Include headings and key points
"""


def email_template(user_input, tone, length):
    return f"""
Act as a professional email writer.

Write an email based on:

Purpose:
{user_input}

Tone:
{tone}

Length:
{length}

Goal:
{refine_goal(user_input)}

Guidelines:
- Start with a proper greeting
- Clearly state purpose
- Keep it polite and concise
- End with a professional closing
"""



def coding_template(user_input, tone, length):
    return f"""
Act as a software engineer.

Provide a solution for:

Problem:
{user_input}

Tone:
Clear and technical

Length:
{length}

Goal:
{refine_goal(user_input)}

Guidelines:
- Explain approach step-by-step
- Write clean and readable code
- Add comments where needed
- Focus on efficiency and clarity
"""


def explanation_template(user_input, tone, length):
    return f"""
Act as an expert educator.

Explain the following topic:

Topic:
{user_input}

Tone:
{tone}

Length:
{length}

Goal:
{refine_goal(user_input)}

Guidelines:
- Use simple language
- Break down concepts step-by-step
- Provide examples if needed
- Keep it easy to understand
"""

def webapp_template(user_input, tone, length):
    return f"""
Act as a full-stack developer.

Design a web application based on:

Requirement:
{user_input}

Tone:
{tone}

Length:
{length}

Goal:
{refine_goal(user_input)}

Guidelines:
- Define problem and solution
- List key features
- Suggest tech stack (frontend, backend, database)
- Describe system architecture
- Include possible improvements
"""
