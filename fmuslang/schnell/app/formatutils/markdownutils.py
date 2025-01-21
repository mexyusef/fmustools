from schnell.vendor.rich.console import Console
from schnell.vendor.rich.markdown import Markdown
from schnell.app.fileutils import file_content


# C:\Users\usef\work\sidoarjo\schnell\vendor\rich\markdown.py
def print_markdown_content(markdown_body):
    markdown = Markdown(markdown_body, justify="full")
    console = Console()
    console.print(markdown)


def print_markdown_file(markdown_filepath):
    markdown_body = file_content(markdown_filepath)
    print_markdown_content(markdown_body)


# https://github.com/matthewwithanm/python-markdownify
# pip install --user markdownify
from markdownify import markdownify as md
def html_to_markdown(html_content):
    return md(html_content)


def htmlfile_to_markdown(html_filepath):
    return html_to_markdown(file_content(html_filepath))
