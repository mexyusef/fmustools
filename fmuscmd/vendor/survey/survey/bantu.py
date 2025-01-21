def append_to_file(file_path, content):
    with open(file_path, 'a', encoding='utf8') as file:
        file.write(content)
