import subprocess
import os



def run_command_in_folder(folder_path, command):
    subprocess.run(command, shell=True, cwd=folder_path)


def count_suffix(pendek, panjang, suffix='/'):
    if panjang.startswith(pendek):
        count = panjang[len(pendek):].count(suffix)
        return count
    else:
        return 0
