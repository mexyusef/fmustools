import sys
from schnell.app.dirutils import (
    ayah,
    isfile,
    isdir,
)
from schnell.app.printutils import indah4
from schnell.app.utils import (
    perintah_shell,
    env_get,
    platform,
    wslify,
)


def declarative(text, meta_input):
    """
    #<decl codes>...
    konversi prefix utk kode deklaratif yg bs dihandle oleh
    creator.declarative.handler
    """
    preprocessed_program = text
    print("[db.replservice_helper] servicing declarative program:", text)
    preprocessed_program = "DF" + preprocessed_program
    return preprocessed_program


def launch_terminal(basedir):
    operos = platform()
    if operos == "windows":
        # terminal = env_get('ULIBPY_EXPLORER').replace('__BASEDIR__', basedir)
        # terminal = f'wt.exe -d "{basedir}"'
        terminal = env_get("ULIBPY_EXPLORER").replace("__BASEDIR__", basedir)
    elif operos == "wsl":
        # terminal = f'wt.exe -d "{wslify(basedir)}"'
        # terminal = f'wt.exe -d "{wslify(basedir, rewindows=True)}"'
        terminal = env_get("ULIBPY_EXPLORER").replace("__BASEDIR__", basedir)
    else:
        terminal = f"qterminal -w {basedir} 2>/dev/null &"
    print("launch_terminal, operating system:", operos)
    return terminal


def launch_explorer(basedir):
    exp = env_get("ULIBPY_EXPLORER")
    terminal = f"{exp} {basedir}"
    return terminal


def explorer_handler(text, meta_input):
    """
    ceritanya:
    listener adlh linux
    filepath adlh linux
    mau buka filepath di windows
    """
    # text sementara gak diproses
    # if sys.platform == 'win32':
    if meta_input:
        docinfo = meta_input["metaDocument"]
        filepath = docinfo["filename"]
        if isfile(filepath):
            folder = ayah(filepath, 1)
            folder = wslify(folder)
            terminal = launch_explorer(folder)
            indah4(
                f"Filepath from meta = {filepath}.\nTerminal = {terminal}", warna="cyan"
            )
            perintah_shell(terminal)
        else:
            terminal = launch_explorer("~")
            indah4(
                f"Filepath from default = {filepath}.\nTerminal = {terminal}",
                warna="cyan",
            )
            perintah_shell(terminal)


def term_handler(text, meta_input):
    if text.startswith("term "):
        folder_or_file = text.split()[1:]
        folder_or_file = " ".join(folder_or_file)
        if isfile(folder_or_file):
            folder = ayah(folder_or_file, 1)
            terminal = launch_terminal(folder)
            indah4(
                f"Filepath from isfile = {folder_or_file}.\nTerminal = {terminal}",
                warna="cyan",
            )
            perintah_shell(terminal)
        elif isdir(folder_or_file):
            folder = folder_or_file
            terminal = launch_terminal(folder)
            indah4(
                f"Filepath from isdir = {folder_or_file}.\nTerminal = {terminal}",
                warna="cyan",
            )
            perintah_shell(terminal)

    elif meta_input:
        docinfo = meta_input["metaDocument"]
        filepath = docinfo["filename"]
        if isfile(filepath):
            folder = ayah(filepath, 1)
            terminal = launch_terminal(folder)
            indah4(
                f"Filepath from meta = {filepath}.\nTerminal = {terminal}", warna="cyan"
            )
            perintah_shell(terminal)
        else:
            terminal = launch_terminal("~")
            indah4(
                f"Filepath from default = {filepath}.\nTerminal = {terminal}",
                warna="cyan",
            )
            perintah_shell(terminal)
