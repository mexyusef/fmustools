import os
from schnell.app.fileutils import file_append, file_write, not_binary, file_content
from schnell.vendor.survey import survey


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


FOLLOW_REPOS = [
    r'C:\portfolio\ciledug-repo\next.js',
    r'C:\portfolio\ciledug-repo\react',
    r'C:\portfolio\ciledug-repo\budibase',
    r'C:\portfolio\ciledug-repo\baserow',
]


def file_browser(start_path='.', INITIAL_OPTIONS=[
    '.. (Up one level)',
    '+ Create file or directory',
    'Goto',
    *FOLLOW_REPOS,
    'Quit'
]):
    # mengirim repl di sini useless
    # krn ternyata repl gak merespon aktivitas survey

    current_path = os.path.abspath(start_path)
    while True:
        # List directories and files in the current path
        items = sorted(os.listdir(current_path))
        options = INITIAL_OPTIONS
        options += [
            f'📁 {item}' if os.path.isdir(os.path.join(current_path, item)) else f'📄 {item}'
            for item in items
        ]

        # Ask the user to select an item
        index = survey.routines.select(f'Select a file or directory in {current_path}: ',
            options=options,
            focus_mark='👉 ',
            # callback=lambda x,y:print(f'x={x}, y={y}'),
            # callback=lambda x,y:tulis_data(x,y),
            # callback=lambda item:pilihan_sekarang(repl, item),
            # validate=lambda x:print('validasi:', x),
            # validate=lambda x:validasi(x), # ini hasil akhir, bukan waktu select
            # delegate=lambda x:delegasi(x), # ini hasil akhir, bukan waktu select
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
        elif selection in FOLLOW_REPOS:
            print('[file_browser] pilihan:', selection)
            return selection
        else:
            selected_item = selection[2:]  # Remove the emoji
            selected_path = os.path.join(current_path, selected_item)
            if os.path.isdir(selected_path):
                current_path = selected_path
            else:
                return selected_path


def survey_print(tulisan, warna_tulisan='cyan'):
    warna = survey.colors.basic
    cetak = survey.printers.text
    cetak(warna(warna_tulisan), tulisan)


def test_file_browser():
    selected_file = file_browser()
    # print("Selected file:", selected_file)
    survey_print(f"Selected file: {selected_file}.")


if __name__ == '__main__':
    test_file_browser()
