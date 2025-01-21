import re
import pyperclip
from tkinter import Tk, simpledialog
from schnell.app.inpututils.survey_input import input_survey_select, input_survey_text


def get_url_from_clipboard(use_survey=True):
    text = pyperclip.paste()
    if not text:
        return None, text
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    if len(urls) > 1:
        if use_survey:
            print('urls:', urls)
            url = input_survey_select("Multiple URLs found. Please enter the number of the URL you want to use:", urls)
            return url, text
        else:
            root = Tk()
            root.withdraw()  # Hide the main window
            url = simpledialog.askstring(
                "URL Selection", 
                "Multiple URLs found. Please enter the number of the URL you want to use:\n" 
                    + "\n".join(
                        [f"{i+1}. {url}"
                            for i, url in enumerate(urls)]
                        )
                )
            if url and url.isdigit() and 1 <= int(url) <= len(urls):
                return urls[int(url) - 1], text
    elif len(urls) == 1:
        return urls[0], text
    return None, text


def get_copy_url_from_clipboard(use_survey=True):
    url, _ = get_url_from_clipboard(use_survey=use_survey)
    if url:
        pyperclip.copy(url)
    return url


def print_get_url_from_clipboard():
    url, text = get_url_from_clipboard()
    if url:
        print("Found:", url)
    else:
        print(f"Nothing in {text}")


def print_copy_get_url_from_clipboard():
    url, text = get_url_from_clipboard()
    if url:
        pyperclip.copy(url)
        print("Found and copied:", url)
    else:
        print(f"Nothing in {text}")


def replace_variable_in_file_spaces(filepath, variable_name, value):
    with open(filepath, 'r') as file:
        content = file.read()
    content = re.sub(f"{variable_name} = .+", f"{variable_name} = '{value}'", content)
    with open(filepath, 'w') as file:
        file.write(content)


def replace_variable_in_file(filepath, variable_name, value):
    with open(filepath, 'r') as file:
        content = file.read()
    # Updated regex to handle spaces around the equals sign
    content = re.sub(f"{variable_name} *= *.*", f"{variable_name} = '{value}'", content)
    with open(filepath, 'w') as file:
        file.write(content)


def test_clipboardurl(filename='processor.py', key='UPLOAD_URL', value=None):
    if not value:
        url, _ = get_url_from_clipboard()
    else:
        url = value

    print(f"""test_clipboardurl
    filename    = "{filename}"
    key         = "{key}"
    value       = "{value}"
    url       = "{url}"
    """)

    if url:
        replace_variable_in_file(filename, key, url)
    else:
        print("No urls")


def prompt_clipboardurl():
    filename = input_survey_text("filename: ")
    key = input_survey_text("key to replace: ")
    value = input_survey_text("value: ")
    if not value:
        url, _ = get_url_from_clipboard()
    else:
        url = value

    print(f"""test_clipboardurl
    filename    = "{filename}"
    key         = "{key}"
    value       = "{value}"
    url         = "{url}"
    """)

    if url:
        replace_variable_in_file(filename, key, url)
    else:
        print("No urls")
