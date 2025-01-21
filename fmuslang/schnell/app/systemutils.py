import os, shutil, subprocess, sys, threading
# from typing import List
import configparser
from schnell.app.appconfig import programming_data


# firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# noteplusplus_path = r"C:\Program Files\Notepad++\notepad++.exe"


def transeditor(args):
    editor_trans = programming_data['j']["editors"]['TRANS']
    if isinstance(args, str):
        args = [args]
    elif isinstance(args, int):
        args = [str(args)]

    subprocess.run([editor_trans] + args, shell=True)


def noteplusplus(args):
    noteplusplus_path = programming_data['j']["editors"]['N++']
    if isinstance(args, str):
        args = [args]
    elif isinstance(args, int):
        args = [str(args)]

    # program_args = [r'"C:\Program Files"\Notepad++\notepad++.exe'] + args
    # print('noteplusplus:', program_args)
    subprocess.run([noteplusplus_path] + args, shell=True)
    # subprocess.run(program_args, shell=True)


def firefox_profiles():
    # from .fileutils import file_content
    appdata_dir = os.getenv('APPDATA')
    # Construct the path to the profiles.ini file
    profiles_ini_path = os.path.join(appdata_dir, 'Mozilla', 'Firefox', 'profiles.ini')
    # print(profiles_ini_path)
    # content = file_content(profiles_ini_path)
    config = configparser.ConfigParser()
    config.read(profiles_ini_path)
    # Retrieve all values of the 'Name' key from all sections
    name_values = []
    for section in config.sections():
        if 'Name' in config[section]:
            name_value = config[section]['Name']
            name_values.append(name_value)

    # # Print all values of the 'Name' key
    # for name_value in name_values:
    #     print(name_value)
    return name_values


def open_url_with_firefox(url, profile_name = 'default-release'):
    """
    open_url_with_firefox('https://www.example.com')
    => ['C:\\Program Files\\Mozilla Firefox\\firefox.exe', '--new-tab', '--no-remote', '--profile', 'ktg', 'www.detik.com']
    apakah ini benar atau '--profile', 'ktg' harus digabung?
    C:\\Program Files\\Mozilla Firefox\\firefox.exe --new-tab --no-remote --profile ktg www.detik.com
    """
    firefox_path = programming_data['j']["browsers"]['programs']['firefox']['exe']
    # command = [firefox_path, '--new-tab', '--no-remote', '--profile', profile_name, url]
    command = [firefox_path, '--new-tab', '--no-remote', '-P', profile_name, url]
    print(f'open_url_with_firefox=[{command}]')
    subprocess.Popen(command)


def sub_detach(command):
    # kembalian adlh process obj, yg bisa process.wait() spt <thread>.join()
    return subprocess.Popen(command, shell=True)


def sub_async(command):
    # kembalian adlh result obj, yg bisa result.returncode dimana 0 = success, otherwise = failed
    return subprocess.run(command, shell=True)


def execute_command(command):
    """
    stdout, stderr = execute_command("grep -R -i sometext somefolder")
    if stderr is not None:
        print(f"Error: {stderr}")
    else:
        print(stdout)
    """
    print(f"execute_command => {command}.")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # stdout = result.stdout.decode('utf-8').strip()
    try:
        stdout = result.stdout.decode('utf-8').strip()
    except UnicodeDecodeError:
        stdout = result.stdout.decode('utf-8', errors='replace').strip()
    stderr = result.stderr.decode('utf-8').strip() if result.returncode else None
    return stdout, stderr


def execute_in_thread(command):
    threading.Thread(target=lambda: subprocess.run(command)).start()


def execute_command2(command, working_dir=None):
    """
    bisa exec command dlm workingdir
    stdout, stderr = execute_command("grep -R -i sometext somefolder", working_dir="/path/to/working/directory")
    """
    kwargs = {
        "stdout": subprocess.PIPE,
        "stderr": subprocess.PIPE,
        "shell": True,
    }
    if working_dir:
        kwargs["cwd"] = working_dir
    print(f"execute_command2 => {command}, args={kwargs}.")
    result = subprocess.run(command, **kwargs)
    stdout = result.stdout.decode('utf-8').strip()
    stderr = result.stderr.decode('utf-8').strip() if result.returncode else None
    return stdout, stderr


def grep_text(sometext, somefolder=".", case_sensitive=False, limit_chars=1024, files=None):
    """
    stdout, stderr = grep_text("sometext", "somefolder")
    if stderr is not None:
        print(f"Error: {stderr}")
    else:
        print(stdout)
    """
    sensitive = "" if case_sensitive else "-i"
    include_files = f"--include='*.{files}'" if files else '' # err, ini gak jalan.
    command = f'grep -r {sensitive} -n -s -H -I {include_files} "{sometext}" {somefolder} | cut -c1-{limit_chars}' # charater 1-1024
    print(f"grep_text {command}.")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout = result.stdout.decode('utf-8').strip()
    stderr = result.stderr.decode('utf-8').strip() if result.returncode else None
    return stdout, stderr


def find_files(sometext, somefolder=".", case_sensitive=False):
    """
    stdout, stderr = find_files("*rails*", "C:\\")
    if stderr is not None:
        print(f"Error: {stderr}")
    else:
        print(stdout)
    """
    sensitive = "-name" if case_sensitive else "-iname"
    command = f'C:\\work\\usr\\local\\wbin\\find.exe {somefolder} {sensitive} "*{sometext}*"'
    print(f"find_files {command}.")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout = result.stdout.decode('utf-8').strip()
    stderr = result.stderr.decode('utf-8').strip() if result.returncode else None
    return stdout, stderr


def execute_command_in_dir(command, dirpath, command_is_string=False):
    # if command_is_string:
    #     command = command.split()
    if isinstance(command, (str)):
        command = command.split()
    return subprocess.run(command, shell=True, cwd=dirpath)


def execute_command_in_dir_in_thread(command, dirpath):
    x = threading.Thread(target=execute_command_in_dir, args=(command, dirpath))
    x.start()


def execute_file_in_dir_from_file(filepath):
    """
    kita gunakan utk execute batch file.
    masalahnya: stlh selesai console langsung tutup
    """
    filename = os.path.basename(filepath)
    dirpath = os.path.dirname(filepath)
    os.chdir(dirpath)
    os.startfile(filename)


def execute_file_in_dir(dirpath, filename):
    """
    kita gunakan utk execute batch file.
    masalahnya: stlh selesai console langsung tutup
    """
    os.chdir(dirpath)
    os.startfile(filename)


def execute_file_in_dir_with_system(dirpath, filename):
    """
    kita gunakan utk execute batch file.
    masalahnya: gak hasilkan console baru
    """
    os.chdir(dirpath)
    os.system(filename)


def os_system(cmd):
    os.system(cmd)


def run_code_file(file_path):
    """
    Executes a code file using its file path as an argument.
    """
    from .fileutils import touch_file
    touch_file(file_path)
    print(f'run_code_file: "{file_path}"')
    # if not os.path.exists(file_path):
    #     with open(file_path, 'w') as f:
    #         pass
    os.system(f'code "{file_path}"')
    # try:
    #     if sys.platform == 'win32':
    #         print(f'Opening file "{file_path}"')
    #         subprocess.run(['code', f'"{file_path}"'], check=True)
    #     else:
    #         subprocess.run(['code', file_path], check=True)
    # except subprocess.CalledProcessError as e:
    #     print(f"Error: {e}")


def find_command_location(command):
    # Get the paths from the environment variable
    paths = os.environ['PATH'].split(os.pathsep)

    # Search for the command in each path
    for path in paths:
        full_path = os.path.join(path, command)
        # Check if the command exists in the current path
        if os.path.exists(full_path):
            return full_path

    # If the command is not found in any path
    return None


def test_find_command_location():
    command_name = 'mvn'
    command_location = find_command_location(command_name)

    if command_location:
        print(f"The location of '{command_name}' is: {command_location}")
    else:
        print(f"'{command_name}' not found in the PATH.")
