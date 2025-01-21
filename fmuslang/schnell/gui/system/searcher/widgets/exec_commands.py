import subprocess


def exec_code_sidoarjo(env_location="ULIBPY_ROOTDIR"):
    from schnell.app.utils import env_get
    subprocess.run(f'code {env_get(env_location)}'.split(), shell=True)


def exec_notepad(plusplus=False):    
    if plusplus:
        subprocess.run([r'C:\Program Files"\Notepad++\notepad++.exe'], shell=True)
    else:
        subprocess.run(r'C:\Windows\system32\notepad.exe'.split(), shell=True)
