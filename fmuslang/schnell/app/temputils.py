import os
import tempfile
import urllib.request
# from PIL import Image
import shutil


def empty_temp(temp_dir = tempfile.gettempdir()):
    # Get the path of the temporary directory
    print('[temputils.empty_temp] emptying', temp_dir)
    # Iterate over the files and directories in the temporary directory
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        try:
            if os.path.isfile(file_path):
                # Remove the file
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                # Remove the directory and its contents
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


def file_write(data, suffix=".gif", delete=False):
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=delete) as temp_file:
        temp_file.write(data)

    return temp_file.name


def temp_file_write(data, suffix=".gif", delete=False):
    if isinstance(data, str):
        data = data.encode()
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=delete) as temp_file:
        temp_file.write(data)

    return temp_file.name
