import datetime, keyboard, os, pyperclip, re, time


def generate_filename(filename='clipboard', extension='exs', suffix=None):
    timestamp = re.sub(r'[^a-zA-Z0-9]', '_', str(datetime.datetime.now()))

    final_filename = f'{filename}_{timestamp}.{extension}'

    if suffix:
        final_filename = f'{final_filename}{suffix}'
        

    return final_filename

def copy_clipboard_to_file(clipboard_content, suffix=None, force_filename=None):
    
    if force_filename:
        filename = force_filename
    else:
        filename = generate_filename(suffix=suffix)

    with open(filename, 'w') as file:
        file.write(clipboard_content)

    return filename


def elixir_watcher():
    pyperclip.copy('')
    print("Listening to clipboard. Press 'q' to quit.")
    while True:
        clipboard_content = pyperclip.paste()
        if clipboard_content:
            filename = copy_clipboard_to_file(clipboard_content)
            os.system(f'elixir {filename}')
            print('----- END -----')
            pyperclip.copy('')
            time.sleep(1.0)

        if keyboard.is_pressed('q'):
            print("Exiting the loop.")
            break
