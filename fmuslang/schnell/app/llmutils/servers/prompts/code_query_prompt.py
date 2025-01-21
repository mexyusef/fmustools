code_query_prompt = """
I need you to generate code based on the following specification. The specification can range from very vague to very detailed. Regardless of the level of detail, the code you generate should follow common best practices and design patterns. It should be self-sufficient and ready for use, allowing for easy modification without extensive additional coding.

Here are some guidelines to follow:

- Do not give any explanation except in the comments.
- Use functional components and React hooks.
- Ensure the code is modular and easy to read.
- Include comments where necessary to explain key parts of the code.
- If data fetching is required, use fetch or a similar method.
- Use common design patterns and best practices.
- Assume common dependencies are already setup.

Example vague user specifications are in quote below, followed by expected output:

- "React Dashboard"
the generated code should include typical components and features like hooks, data fetching, a table or list, charts, and cards.
- "Node Express API user authentication"
the generated code should be a functional backend server in node express with initialization and listen parts and endpoints that allow user authentication such as login, logout, forgot password, and token mechanism. Since no authentication framework is specified, use the most poular one, in this case, the JWT authentication framework.

- "Python, scrape data from <website url>"
the generated code should be a website scraper to scrape information from <website url>. Since no librar is mentioned, use the most popular python web scraping library, which is beautifulsoup.

- "Typescript array"
In this case, user specifically mention the language "typescript" without framework or library, therefore, focus only on the language: create an array in typescript. Since no type is given, assume it's a string which is more popular than other data types.

Generate code based on the provided specification, ensuring it is functional and adheres to the best practices mentioned above.

The user is assumed to know and understand the code you generate.
DO NOT give any explanation, all you need to generate is code and only code.
******************************
Let's start!

Specification:

__USER_PROMPT__
"""
