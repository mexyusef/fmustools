from textwrap import dedent

online_test_prompt = dedent("""
    The following image contain a coding, data science, or machine learning problem where you might be requested to either
    - fill the blanks
    or
    - select the correct answer(s) from multiple choice question
    according to the instruction given in the image.

    You have 3 task, each task should be separated by delimiter "*******" in a new line.

    First, please give me your description of the content of the image.
    Second, rewrite the text content of the image as closely matched as possible.
    Last, you try to give solution the problem described in the image.
""")
# Please rewrite the content of the image, to make sure that what you are seeing is correct, and any assumption(s) made are correct, so i can verify that the solution you provided is correct

twitter_lowercase_prompt = dedent("""
""")

twitter_prompt = dedent("""
""")

project_skeleton_prompt = dedent("""
""")

fmus_skeleton_prompt = dedent("""
""")

# ada berbagai jenis hafalan
hafalan_prompt = dedent("""
""")

