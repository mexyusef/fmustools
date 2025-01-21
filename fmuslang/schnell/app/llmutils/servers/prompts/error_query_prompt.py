error_query_prompt = """
I need you to generate solutions based on the following error description. The description can range from very vague to detailed. Regardless of the level of detail, the solutions should be practical, easy to follow, and aim to resolve the issue quickly.

Here are some guidelines to follow:

Make reasonable assumptions about the framework or library being used based on the error message.
Provide solutions in a bullet-point format for easy implementation.
Include any necessary commands, code snippets, or configuration changes in the solutions.
Offer additional explanations or context at the end, if needed.

Generate a list of solutions based on the provided error description, ensuring they are clear and actionable. Provide any additional explanations or context after the solutions.
******************************
Let's start!

Error Description:

__USER_PROMPT__
"""
