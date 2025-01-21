import re
import webbrowser


chrome_invoke = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
firefox_invoke = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
firefox_profile_invoke = '"C:\\Program Files\\Mozilla Firefox\\firefox.exe -no-remote -P"'
webbrowser.register('ff', None, webbrowser.BackgroundBrowser(firefox_invoke))
webbrowser.register('ffp', None, webbrowser.BackgroundBrowser(firefox_profile_invoke))


def launcher(code):
    """
    l)alamat

    f, c, o = firefox, chrome, opera
    l)f/alamat
        firefox new tab
    l)f+/alamat
        firefox new window
    l)c/alamat
        chrome
    l)o/alamat
        opera
    """
    if not code.startswith('http') and '/' not in code:  # not http:// or https:// dan tdk c/something
        if 'localhost' in code or '127.0.0.1' in code:
            code = 'http:' + code
        else:
            code = 'https:' + code

    if not re.match(r'^(f\+?|c|o).*', code):
        webbrowser.open_new_tab(code)
    # elif ' ' in code:
    #     from schnell.app.utils import PROGRAMS
    #     from schnell.app.stringutils import splitspace
    #     import os
    #     # l ff
    #     cmd, args = splitspace(code)
    #     if args in PROGRAMS:
    #         os.system(PROGRAMS[args])
    else:
        request, alamat = code.split('/', 1)
        if request.startswith('f'):
            request = request.removeprefix('f')
            if request.startswith('++'):
                webbrowser.get('ffp').open_new(alamat)
                print('ffp')
            elif request.startswith('+'):
                webbrowser.get('ff').open_new(alamat)
            else:
                webbrowser.get('ff').open_new_tab(alamat)

        elif request.startswith('c'):
            webbrowser.get(chrome_invoke).open(alamat)

        elif request.startswith('o'):
            pass
