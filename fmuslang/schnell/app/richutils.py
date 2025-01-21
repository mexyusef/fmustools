from rich.console import Console
from rich.markdown import Markdown
from .utils import try_copy


console = Console()


def print_markdown(markdown_text):
    """
    https://rich.readthedocs.io/en/stable/markdown.html
    """
    console.print(markdown_text)


def print_copy_markdown(markdown_text):
    """
    https://rich.readthedocs.io/en/stable/markdown.html
    """
    console.print(markdown_text)
    try_copy(markdown_text)

