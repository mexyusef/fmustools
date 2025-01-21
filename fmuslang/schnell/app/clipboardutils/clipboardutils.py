from rich.console import Console
from rich.prompt import Prompt
import pyperclip

console = Console()

def copy_to_clipboard(text):
    pyperclip.copy(text)
    console.print(f"Copied to clipboard: [bold]{text}[/bold]", style="green")

def main():
    text = Prompt.ask("Enter text to copy")
    copy_to_clipboard(text)

if __name__ == "__main__":
    main()
