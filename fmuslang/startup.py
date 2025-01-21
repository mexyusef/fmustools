import sys
from pathlib import Path
from pprint import pprint
import webbrowser

current_file_path = Path(__file__).resolve()
rootdir = current_file_path.parent
sys.path.append(rootdir)

from schnell.app.appconfig import programming_data
from schnell.app.iniutils import read_ini
from schnell.app.jsonutils import read_json
from schnell.app.yamlutils import read_yaml
from schnell.gui.system.searcher.make_redis_help import try_pubsub_connect


declang_file = rootdir / "declang.json"
env_file = rootdir / "schnell" / ".env"
config_json = rootdir / "config.json"
config_ini = rootdir / "config.ini"
config_yaml = rootdir / "config.yaml"
config_txt = rootdir / "config.txt"
config_quick = rootdir / "config_quick.json"
config_perintah = rootdir / "config_perintah.json"


CACHE = {}


def GET(filepath):
    if not filepath in CACHE:
        if filepath == config_json:
            CACHE[filepath] = read_json(config_json)
        elif filepath == declang_file:
            CACHE[filepath] = read_json(declang_file)
        elif filepath == config_yaml:
            CACHE[filepath] = read_yaml(config_yaml)
        elif filepath == config_ini:
            CACHE[filepath] = read_ini(config_ini)
        elif filepath == config_quick:
            CACHE[filepath] = read_json(config_quick)
        elif filepath == config_perintah:
            CACHE[filepath] = read_json(config_perintah)
        else:
            from schnell.app.fileutils import file_content

            CACHE[filepath] = file_content(filepath)
    return CACHE[filepath]


def read_txt_config():
    # with open(config_txt, 'r', encoding='utf8') as file_handle:
    # 	content = file_handle.readlines()
    # 	for idx, line in enumerate(content,1):
    # 		# replace \\n ke \n
    # 		baris = line.strip().replace('\\n', '\n').replace('\\t', '\t')
    # 		if baris:
    # 			programming_data[str(idx)] = baris
    config_txt_content = GET(config_txt)
    for idx, line in enumerate(config_txt_content.splitlines(), 1):
        # replace \\n ke \n
        baris = line.strip().replace("\\n", "\n").replace("\\t", "\t")
        if baris:
            programming_data[str(idx)] = baris


def initialize_programming_data(invalidate=[]):
    for invalid in invalidate:
        print("invalidating:", invalid)
        if invalid == "config.json":
            del CACHE[config_json]
        elif invalid == "config_quick.json":
            del CACHE[config_json]
        elif invalid == "config_perintah.json":
            del CACHE[config_perintah]
    read_txt_config()
    programming_data["j"] = GET(config_json)  # read_json(config_json)
    programming_data["y"] = GET(config_yaml)  # read_yaml(config_yaml)
    programming_data["i"] = GET(config_ini)  # read_ini(config_ini)
    # programming_data['d'] = GET(declang_file)
    config_quick_json_content = GET(config_quick)
    programming_data.update(config_quick_json_content)
    config_perintah_json_content = GET(config_perintah)
    programming_data.update(config_perintah_json_content)


def reload_config(filepath):
    """
    config_quick.json =>
    """
    if filepath in ["config.json", "config_quick.json", "config_perintah.json"]:
        print("Reloading configuration", filepath)
        if filepath in CACHE:
            del CACHE[filepath]
        if filepath == "config.json":
            programming_data["j"] = GET(config_json)
        elif filepath == config_perintah:
            programming_data.update(GET(config_perintah))
        else:
            programming_data.update(GET(config_quick))
            # print('GET(config_quick)', GET(config_quick))


def init_environment():
    pass


def database_init():
    # sementara gak dipake krn cuma 1 baris
    try_pubsub_connect()


BROWSERS = {
    # "firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
    # "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    # "msedge": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    # "opera": "C:\\Users\\usef\\AppData\\Local\\Programs\\Opera\\opera.exe",
}


def browsers_init():
    # programming_data['j']["browsers"]["programs"]["firefox"]["exe"]
    # programming_data['j']["browsers"]["default"]
    # programming_data['j']["browsers"]["default_method"]
    for browserkunci, browsernilai in programming_data["j"]["browsers"][
        "programs"
    ].items():
        BROWSERS[browserkunci] = browsernilai["exe"]
    for browser_name, browser_path in BROWSERS.items():
        webbrowser.register(
            browser_name, None, webbrowser.BackgroundBrowser(browser_path)
        )
    # pprint(BROWSERS)


def buka(alamat):
    # from schnell.app.appconfig import programming_data
    # pprint(programming_data['j']["browsers"])
    try:
        # programming_data['j']["browsers"]["programs"]["firefox"]["exe"]
        if programming_data["j"]["browsers"]["default"]:
            browser_choice = programming_data["j"]["browsers"]["default"]
            # browser_path = programming_data['j']["browsers"]["programs"][browser_choice]["exe"]
            # print('[startup:buka] browser_choice:', browser_choice)
            if programming_data["j"]["browsers"]["default_method"]:
                if programming_data["j"]["browsers"]["default_method"] == "window":
                    webbrowser.get(browser_choice).open(alamat)
                else:
                    webbrowser.get(browser_choice).open_tab(alamat)
            else:
                webbrowser.get(browser_choice).open(alamat)
        else:
            webbrowser.open(alamat)
    except Exception:
        webbrowser.open(alamat)


buka_internet = buka


def startup():
    """
    from startup import startup
    startup()
    """
    initialize_programming_data()
    try_pubsub_connect()
    browsers_init()
