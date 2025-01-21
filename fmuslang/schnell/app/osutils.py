from .utils import is_windows


def linux_to_windows(linux_path, prefixer='\\\\wsl.localhost\\Ubuntu20.04LTS'):
    """
    /home/usef/work/sidoarjo/database/by-langs/medium/titles.mk
    wsl.localhost
        Ubuntu20.04LTS
            home
                usef
                    work
                        sidoarjo
                            database
                                by-langs
                                    medium
                                        titles.mk
    """
    slash_to_backslash = linux_path.replace('/', '\\')
    result = prefixer + slash_to_backslash
    print(result)
    return result


def is_linux_path_on_windows(filepath):
    """
    /home/usef...
    sedangkan kita pake windows.
    """
    if not is_windows():
        return False

    if not filepath.startswith('/'):
        return False

    if filepath.startswith('/home'):
        return True

    return True


def is_linux_path_on_windows_and_convert(filepath):
    """
    gabung 2 fungsi utk menyederhanakan code
    is_linux_path_on_windows
    linux_to_windows
    """
    islinux = is_linux_path_on_windows(filepath)
    if not islinux:
        return False, None
    
    windowsify_linux_path = linux_to_windows(filepath)
    return islinux, windowsify_linux_path
