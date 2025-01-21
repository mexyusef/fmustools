import os
from InquirerPy import inquirer
from InquirerPy.separator import Separator

def file_browser(start_path='.'):
    current_path = os.path.abspath(start_path)
    while True:
        # List directories and files in the current path
        items = [f for f in os.listdir(current_path) if not f.startswith('.')]
        items.sort(key=lambda x: (os.path.isfile(os.path.join(current_path, x)), x.lower()))
        choices = [Separator('Directories:')] if any(os.path.isdir(os.path.join(current_path, f)) for f in items) else []
        
        # Add directories and files to choices
        for item in items:
            full_path = os.path.join(current_path, item)
            if os.path.isdir(full_path):
                choices.append({'name': f'[Dir]  {item}', 'value': full_path})
            else:
                choices.append({'name': f'[File] {item}', 'value': full_path})
        
        # Add option to go up one directory
        choices.insert(0, {'name': '[..] Go up one directory', 'value': '..'})

        # Add option to quit the file browser
        choices.insert(0, {'name': '[Quit] Exit file browser', 'value': 'QUIT'})

        # Ask the user to select an item
        selected = inquirer.select(
            message=f'Select a file or directory in {current_path}:',
            choices=choices,
            default='..',
            qmark='>',
            pointer='>'
        ).execute()

        # If the user chooses to quit, return None
        if selected == 'QUIT':
            return None

        # If the selected item is a directory, change the current path
        if selected == '..':
            new_path = os.path.dirname(current_path)
            # Check if the new path is different from the current path
            if new_path != current_path:
                current_path = new_path
        elif os.path.isdir(selected):
            current_path = selected
        else:
            # A file is selected, return its path
            return selected

# def test_file_browser2():
#     selected_file = file_browser()
#     if selected_file:
#         absolute_path = os.path.abspath(selected_file)
#         print("Selected file absolute path:", absolute_path)
#     else:
#         print("No file selected or file browser exited.")

# def file_browser_absolute(start_path='.'):
#     selected_file = file_browser(start_path=start_path)
#     if selected_file:
#         selected_file = os.path.abspath(selected_file)
#     return selected_file

# sayangnya https://github.com/kazhala/InquirerPy
# gak dukung emoji
def file_browser_emoji(start_path='.'):
    current_path = os.path.abspath(start_path)
    while True:
        # List directories and files in the current path
        items = [f for f in os.listdir(current_path) if not f.startswith('.')]
        items.sort(key=lambda x: (os.path.isfile(os.path.join(current_path, x)), x.lower()))
        choices = [Separator('Directories:')] if any(os.path.isdir(os.path.join(current_path, f)) for f in items) else []
        
        # Add directories and files to choices
        for item in items:
            full_path = os.path.join(current_path, item)
            if os.path.isdir(full_path):
                choices.append({'name': f'📁 {item}', 'value': full_path})
            else:
                choices.append({'name': f'📄 {item}', 'value': full_path})
        
        # Add option to go up one directory
        choices.insert(0, {'name': '⬆️ [..] Go up one directory', 'value': '..'})

        # Add option to quit the file browser
        choices.insert(0, {'name': '❌ [Quit] Exit file browser', 'value': 'QUIT'})

        # Ask the user to select an item
        selected = inquirer.select(
            message=f'Select a file or directory in {current_path}:',
            choices=choices,
            default='..',
            qmark='>',
            pointer='>'
        ).execute()

        # If the user chooses to quit, return None
        if selected == 'QUIT':
            return None

        # If the selected item is a directory, change the current path
        if selected == '..':
            new_path = os.path.dirname(current_path)
            # Check if the new path is different from the current path
            if new_path != current_path:
                current_path = new_path
        elif os.path.isdir(selected):
            current_path = selected
        else:
            # A file is selected, return its path
            return selected

def test_file_browser_emoji():
    selected_file = file_browser()
    print("Selected file:", selected_file)

# https://github.com/kazhala/InquirerPy

def inquire_text(message="What's your name:"):
    response = inquirer.text(message=message).execute()
    return response

# setara:
# jalankan = rich.prompt.Confirm.ask(prompt=f"Jalankan kode di atas di {os.getcwd()}?", default=True)
def inquire_yn(message="Confirm?"):
    confirm = inquirer.confirm(message=message).execute()
    return confirm


# pip install --user pick
from pick import pick

import sys


#reflect#schnell.app.filemanager.tui_browser/restore_terminal
def init_ctypes():

    import ctypes
    from ctypes import wintypes

    # Windows API constants
    ENABLE_QUICK_EDIT_MODE = 0x0040
    ENABLE_EXTENDED_FLAGS = 0x0080
    STD_INPUT_HANDLE = -10

    # Get the standard input handle
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    std_input_handle = kernel32.GetStdHandle(STD_INPUT_HANDLE)

    # Get the current console mode
    original_mode = wintypes.DWORD()
    kernel32.GetConsoleMode(std_input_handle, ctypes.byref(original_mode))

def restore_terminal():
    init_ctypes()
    # Restore the original console mode
    kernel32.SetConsoleMode(std_input_handle, original_mode)

#reflect#schnell.app.filemanager.tui_browser/reset_terminal
def reset_terminal():
    # Reset the terminal to normal mode
    sys.stdout.write('\033[?1049l')  # Exit alternate screen buffer
    sys.stdout.write('\033[?25h')    # Show cursor
    sys.stdout.flush()

def file_browser_pick(start_path='.'):
    current_path = os.path.abspath(start_path)
    while True:
        # List directories and files in the current path
        items = [f for f in os.listdir(current_path) if not f.startswith('.')]
        items.sort(key=lambda x: (os.path.isfile(os.path.join(current_path, x)), x.lower()))
        choices = [(f'📁 {item}', os.path.join(current_path, item)) for item in items if os.path.isdir(os.path.join(current_path, item))]
        choices += [(f'📄 {item}', os.path.join(current_path, item)) for item in items if not os.path.isdir(os.path.join(current_path, item))]

        # Add option to go up one directory
        if current_path != start_path:
            choices.insert(0, ('⬆️ [..] Go up one directory', '..'))

        # Add option to quit the file browser
        choices.insert(0, ('❌ [Quit] Exit file browser', 'QUIT'))

        # Ask the user to select an item
        title = f'Select a file or directory in {current_path}:'
        selected, index = pick([choice[0] for choice in choices], title, indicator='>')

        reset_terminal()

        # If the user chooses to quit, return None
        if choices[index][1] == 'QUIT':
            return None

        # If the selected item is a directory, change the current path
        if choices[index][1] == '..':
            current_path = os.path.dirname(current_path)
        elif os.path.isdir(choices[index][1]):
            current_path = choices[index][1]
        else:
            # A file is selected, return its path
            return choices[index][1]

def test_file_browser_pick():
    selected_file = file_browser()
    print("Selected file:", selected_file)

def input_text(prompt):
    return input(prompt)

def input_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid float.")

def input_boolean(prompt):
    while True:
        response = input(f"{prompt} (y/n): ").lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def test_input_pick():
    text = input_text("Enter some text: ")
    print("You entered:", text)

    integer = input_integer("Enter an integer: ")
    print("You entered:", integer)

    floating_point = input_float("Enter a float: ")
    print("You entered:", floating_point)

    confirmation = input_boolean("Confirm? ")
    print("You confirmed:", confirmation)
