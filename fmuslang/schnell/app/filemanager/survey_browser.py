import os
import survey  # pip install --user survey


def create_only_directory(current_path, name, is_directory=False):
    full_path = os.path.join(current_path, name)
    if is_directory:
        os.makedirs(full_path, exist_ok=True)
    else:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        open(full_path, 'a').close()
    return full_path

def create_file_or_directory(current_path, name):
    if '/' in name:
        # Create a directory and file
        dir_name, file_name = name.rsplit('/', 1)
        dir_path = os.path.join(current_path, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, file_name)
    else:
        # Create a file in the current directory
        file_path = os.path.join(current_path, name)
    
    # Create the file if it does not exist
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass
    return file_path

def file_browser_old(start_path='.'):
    current_path = os.path.abspath(start_path)
    while True:
        # List directories and files in the current path
        items = sorted(os.listdir(current_path))
        options = ['.. (Up one level)', '+ Create file or directory']
        options += [f'📁 {item}' if os.path.isdir(os.path.join(current_path, item)) else f'📄 {item}' for item in items]

        # Ask the user to select an item
        index = survey.routines.select(f'Select a file or directory in {current_path}: ',
                                       options=options,
                                       focus_mark='> ',
                                       evade_color=survey.colors.basic('yellow'))

        # Handle selection
        selection = options[index]
        if selection == '.. (Up one level)':
            current_path = os.path.dirname(current_path)
        elif selection == '+ Create file or directory':
            name = survey.routines.input('Enter the name of the file or directory (use / for nested directories): ')
            created_path = create_file_or_directory(current_path, name)
            print(f'Created: {created_path}')
        else:
            selected_item = selection[2:]  # Remove the emoji
            selected_path = os.path.join(current_path, selected_item)
            if os.path.isdir(selected_path):
                current_path = selected_path
            else:
                return selected_path

def file_browser(start_path='.'):
    current_path = os.path.abspath(start_path)
    while True:
        # List directories and files in the current path
        items = sorted(os.listdir(current_path))
        # options = ['.. (Up one level)', '+ Create file or directory', 'Goto', 'Quit']
        options = ['.. (Up one level)', 'Quit', '+ Create file or directory', 'Goto']
        options += [f'📁 {item}' if os.path.isdir(os.path.join(current_path, item)) else f'📄 {item}' for item in items]

        # Ask the user to select an item
        index = survey.routines.select(f'Select a file or directory in {current_path}: ',
                                       options=options,
                                       focus_mark='👉 ',
                                       evade_color=survey.colors.basic('yellow'))

        # Handle selection
        selection = options[index]
        if selection == '.. (Up one level)':
            current_path = os.path.dirname(current_path)
        elif selection == '+ Create file or directory':
            name = survey.routines.input('Enter the name of the file or directory (use / for nested directories): ')
            created_path = create_file_or_directory(current_path, name)
            print(f'Created: {created_path}')
        elif selection == 'Goto':
            path = survey.routines.input('Enter the path to go to: ')
            # full_path = os.path.join(current_path, path)
            # Check if the path is absolute or relative
            if os.path.isabs(path):
                full_path = path
            else:
                full_path = os.path.join(current_path, path)
            if os.path.exists(full_path):
                if os.path.isdir(full_path):
                    current_path = full_path
                else:
                    current_path = os.path.dirname(full_path)
                    # If possible, select the filename in the list
                    filename = os.path.basename(full_path)
                    if filename in items:
                        index = items.index(filename)
                        # Select the file in the listbox (if using a GUI)
            else:
                print("Warning: Path does not exist.")
        elif selection == 'Quit':
            return None
        else:
            selected_item = selection[2:]  # Remove the emoji
            selected_path = os.path.join(current_path, selected_item)
            if os.path.isdir(selected_path):
                current_path = selected_path
            else:
                return selected_path

def folder_browser(start_path='.'):
    current_path = os.path.abspath(start_path)
    while True:
        # List only directories in the current path
        items = sorted([item for item in os.listdir(current_path) if os.path.isdir(os.path.join(current_path, item))])
        options = ['.. (Up one level)', 'Select this folder', 'Quit', '+ Create directory', 'Goto']
        options += [f'📁 {item}' for item in items]

        # Ask the user to select an item
        index = survey.routines.select(f'Select a directory in {current_path}: ',
                                       options=options,
                                       focus_mark='👉 ',
                                       evade_color=survey.colors.basic('yellow'))

        # Handle selection
        selection = options[index]
        if selection == '.. (Up one level)':
            current_path = os.path.dirname(current_path)
        elif selection == 'Select this folder':
            return current_path
        elif selection == '+ Create directory':
            name = survey.routines.input('Enter the name of the directory (use / for nested directories): ')
            created_path = create_only_directory(current_path, name, is_directory=True)
            print(f'Created: {created_path}')
        elif selection == 'Goto':
            path = survey.routines.input('Enter the path to go to: ')
            full_path = os.path.join(current_path, path) if not os.path.isabs(path) else path
            if os.path.isdir(full_path):
                current_path = full_path
            else:
                print("Warning: Path does not exist or is not a directory.")
        elif selection == 'Quit':
            return None
        else:
            selected_item = selection[2:].strip()  # Remove the emoji
            current_path = os.path.join(current_path, selected_item)


def survey_print(tulisan, warna_tulisan='cyan'):
    warna = survey.colors.basic
    cetak = survey.printers.text
    cetak(warna(warna_tulisan), tulisan)

def test_file_browser():
    selected_file = file_browser()
    # print("Selected file:", selected_file)
    survey_print(f"Selected file: {selected_file}.")


# color = survey.colors.basic('cyan')
# colored = survey.utils.paint(color, 'I am blue!') 
# survey.printers.text(colored) # "I am blue", but cyan
if __name__ == '__main__':
    test_file_browser()
