import os
from fmuslib import joinhere, files_filter, file_lines, basename
from fpcommon import read_json
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text, HTML

ls_high = "ls -a --color=always --format=across -c -l"
ls_wide = "ls -a --color=always --format=horizontal"
ls_choose = ls_wide


vscode_exec = [
    "C:\\Users\\usef\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "C:\\portapps\\VSCode-win32-x64-1.92.1\\code.exe"
    "C:\\portapps\\vscode-portable\\vscode-portable.exe",
]

config_app = {
    "vscode": vscode_exec[0],
    "thread": False,
    # "multicolumn": True,
    "multicolumn": False,
    "ls_style": ls_wide,  # multicolumn bareng dg ls-wide, column dg ls-high
    "readme_after_cd": True,
    "check_all_drives_space": True,

    "show_bottom_toolbar": True,

    "show_textarea": True,
    'show_textarea_editor': True,
    # "show_textarea_editor": False,  # mending pake del-a utk editor baru
    "show_editor_toolbar": True,
    # 'show_textarea_editor': False,
    "text_area_height": 5,
    # 'text_area_style': "bg:ansibrightyellow",
    # 'text_area_style': "bg:ansiblue ansibrightyellow",
    "text_area_style": "ansibrightyellow",
    # 'text_area_editor_style': 'reverse',
    # 'text_area_editor_style': 'bg:ansibrightblack',
    "text_area_editor_style": "ansibrightgreen",
    # 'text_area_lexer': 'markdown',
    "text_area_lexer": "bash",
    # 'text_area_lexer': 'fish',
    # 'text_area_lexer': 'psh',
    # 'text_area_lexer': 'exe',
    # 'text_area_lexer': 'python',
    # 'text_area_lexer': 'html',
    "text_area_focused": False,
    "text_area_editor_focused": False,
    "enable_page_navigation_bindings": False,
    "text_area_editor_lexer": "fish",
 
    "temporary_prompt_validate": True,
    "temporary_prompt_current_fmusfile": None,
    "temporary_prompt_logged_dict": None,
    "temporary_prompt_last_barisentry": None,
 
    # ini harusnya lebih kecil jk ada external drives
    "max_panjang_path": 50,  # kita sesuaikan dengan ukuran window
    "max_panjang_line": 100,

    "openai_model": "gpt-3.5-turbo",
    "openai_temperature": 0,
    "openai_key": None,

    "llm:llm"   : "gemini",
    "llm:model" : "random",
    "llm:temp"  : 0.0,  # utk coding=0, utk project ideas=0.3, utk novel=0.8, utk non-fiction=0.5
 
    "last_cohere_file": None,
    "last_gemini_file": None,
    "last_groq_file": None,
    "last_openai_file": None,

    "emojis": ["🧭", "🔴", "🌙", "👉", "🦢", "🐦", "🌄", "🌐", "⚡", "✍️", "👨‍"],
    "emoji_index": 0,
    "fmuscode": [
        "__INPUT__,f(t=,@line=1,2,3|i+|data)",
        "__INPUT__,f(t=,@line>(lit)|i+|data)",
        "__INPUT__,f(t=,@line~(rgx)|i+|data)",
        "__INPUT__,f(t=,@btw>(sta)(end)|i+|data)",
        "__INPUT__,f(t=,@btw~(sta)(end)|i+|data)",
    ],
    "fmuscode_index": 0,

    "capture_and_copy_screenshot_folder": r"C:\Users\usef\Desktop\Screenshots\llms-vscode",

    "server:fastapi": {
        "host": "0.0.0.0",
        # "host": "127.0.0.1",
        "port": 8100,
    },
    "server:flask": {
        "host": "0.0.0.0",
        # "host": "127.0.0.1",
        "port": 8200,
    },
    "quick-projects": {
        "status": 0,  # 0 = stop, 1 = start
        "current-filename": None,
        "input-from-user": None,
    },
}

NAMAPROYEK = "commands-history"
file_ini = os.path.realpath(__file__)
disini = os.path.dirname(file_ini)  # schnell/app
data_dir = os.path.join(disini, "data")
data_dir = os.path.abspath(data_dir)
filename = f"{NAMAPROYEK}.hist"
file_location_history = os.path.join(data_dir, filename)
file_location_last_file = os.path.join(data_dir, "last.txt")
daftar_config_files = os.path.join(disini, "config_files.txt")
daftar_config_files_content = [
    item
    for item in file_lines(daftar_config_files)
    if item.strip() and not item.strip().startswith("#")
]
ciledug_files = os.path.join(disini, "ciledug.txt")
ciledug_files_content = [
    item
    for item in file_lines(ciledug_files)
    if item.strip() and not item.strip().startswith("#")
]

cirebon_files = os.path.join(disini, "cirebon.txt")
cirebon_files_content = file_lines(cirebon_files)
cirebon_files_content_cleanup = [
    [e.strip() for e in item.split("|")][0]
    for item in cirebon_files_content
    if item.strip() and not item.strip().startswith("#")
]
# peroleh github user/owner name dari cirebon base folder
cirebon_files_mapping = {
    item.split("|")[0]: (
        # item.split('|')[1] adlh github user/owner name
        [e.strip() for e in item.split("|")][1]
        if "|" in item
        else basename(item)
    )
    for item in cirebon_files_content
    if item.strip() and not item.strip().startswith("#")
}

fmuscontent_config = r"C:\work\ciledug\ciledug\fmuscontent\data.json"
fmusperintah_dir = os.path.dirname(__file__)
json_configs_dir = joinhere(__file__, "configs")
daftar_json_configs_files = files_filter(json_configs_dir, extension=[".json"])


prompt_style = Style.from_dict(
    {
        "progress-bar": "bg:#000000 #ffffff",
        "progress-bar.used": "bg:#00FFFF #ffffff",
        # menu completion
        # "completion-menu.completion": "bg:#1ad1ff #ffffff",
        "completion-menu.completion": "bg:#1ad1ff ansiblue",
        # "completion-menu.completion": "bg:#00eeaa ansiblue",
        # "completion-menu.completion": "bg:#00eeaa #eeeeee",  # terlalu sama dg fmus* lain
        # "completion-menu.completion": "bg:#00aaee #eeeeee",  # terlalu sama dg fmus* lain
        # "completion-menu.completion": "bg:#5533ff #eeeeee",
        # pilihan pada menu completion
        # "completion-menu.completion.current": "bg:#00aaaa #000000",
        "completion-menu.completion.current": "bg:#00ff00 #ffffff bold italic",
        # 'completion-menu.completion.current': 'bg:#00ff00 #ffffff bold italic underline',
        "scrollbar.background": "bg:#88aaaa",
        "scrollbar.button": "bg:#222222",
        "username": "#884444 italic",
        "at": "#00aa00",
        # utk panah
        # "colon": "#00aa00 bg:#aaee11",
        # "colon": "#00aa00 bg:#ffffff",
        "colon": "#00aa00",
        "pound": "#00aa00",
        # "host": "#000088 bg:#aaaaff",
        # "host": "#00FFFF bg:#00BFFF",
        "host": "#00FFFF bg:#0000FF",
        # "host": "#000088 bg:#9955ee",
        # "host": "#000088 bg:#3366ff",
        "path": "#884444 underline",
        # Make a selection reverse/underlined.
        # (Use Control-Space to select.)
        "selected-text": "reverse underline",
    }
)

prompt_style_temporary = Style.from_dict(
    {
        # menu completion
        # "completion-menu.completion": "bg:#0000ee #ffffff",
        # "completion-menu.completion": "bg:#0000ee #ff1111",
        "completion-menu.completion": "bg:#1ad1ff ansiblue",
        # pilihan pada menu completion
        # 'completion-menu.completion.current': 'bg:#00ff00 #ffffff bold italic',
        # 'completion-menu.completion.current': 'bg:#00ff00 #ff0000 bold italic',
        "completion-menu.completion.current": "bg:#00ff00 #ffffff bold italic",
        "scrollbar.background": "bg:#88aaaa",
        "scrollbar.button": "bg:#222222",
        "username": "#884444 italic",
        "at": "#00aa00",
        "colon": "#00aa00",
        "pound": "#00aa00",
        "host": "#000088 bg:#bbbbff",
        "path": "#884444 underline",
        "selected-text": "reverse underline",
    }
)

puncs_map = {
    "-": "io_stdin",
    "+": "io_stdout",
    "=": "main",
}

internal_commands = [
    "cls",
    "diary",
    "img",
    "l",
    "lang",
    "oss",
    "own",
    "pypkg",
    "sh",
    "ulib",
    # 'wmc',
    # ':', '!', '#', '\\', '?',
    # 'H', 'help'
] + [item for item in puncs_map.keys()]

keluar = ["x", "q", "exit", "quit", "bye"]

snippets_dir = r"C:\Users\usef\work\sidoarjo\perintah\fmusfiles\snippets"
config_file = joinhere(__file__, "data.json")
help_file = joinhere(__file__, "HELP.md")

original_cd_list = [
    "C:\\Users\\usef\\work\\sidoarjo",
    "C:\\work\\ciledug",
    "C:\\work\\ciledug\\ciledug",
    "C:\\work\\ciledug\\ciledug\\fmusperintah",
    r"C:\work\ciledug\ciledug\fmusperintah\images",
    "C:\\work\\ciledug\\ciledug\\fmusperintah\\vendor\\ojol",
    "C:\\work\\ciledug\\fmusmania",
    "C:\\work\\ciledug\\github",
    "c:\\hapus",
    "c:\\portfolio",
    "c:\\tmp",
    "c:\\work\\kenza",
    "c:\\work\\kenza\\zpt",
    "c:\\work\\jupe",
    "C:\\Users\\usef\\Desktop",
    "C:\\Users\\usef\\Downloads",
    "C:\\Users\\usef\\Pictures",
]


dir_stack = original_cd_list

# data.json
original_dict_to_json = read_json(config_file)
original_dict_keys = {}

vscode = '"C:\\Users\\usef\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
background = "&"
cursor = "C:\\Users\\usef\\AppData\\Local\\Programs\\cursor\\Cursor.exe"
vim = '"C:\\Program Files\\Neovim\\bin\\nvim.exe"'
bunny = "wsl /home/usef/.bun/bin/bun"
bunx = "wsl /home/usef/.bun/bin/bunx"
render = "wsl /home/usef/.deno/bin/deno task run"
fzf = "C:\\ProgramData\\chocolatey\\lib\\fzf\\tools\\fzf.exe"
micronaut = "c:\\bin\\micronaut-cli-3.9.4\\bin\\mn.bat"
fmusreader = "python C:\\Users\\usef\\work\\sidoarjo\\schnell\\gui\\fmusreader.py"
fmusmk = "python C:\\Users\\usef\\work\\sidoarjo\\schnell\\gui\\system\\searcher\\widgets\\mkhelp.py"
unixsort = "c:\\work\\usr\\local\\wbin\\sort"
codewriter = '"C:\\Program Files\\WindowsApps\\ActiproSoftwareLLC.562882FEEB491_4.2.42.0_x64__24pqs290vpjk0\\codewriter.exe"'
plaintext = "c:\\work\\kenza\\zpt\\Snow-Plaintext\\bin\\plaintext.exe"
devpad = "c:\\work\\kenza\\zpt\\DevPad\\DevPad\\bin\\Release\\DevPad.exe"
# notepad = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2310.13.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
notedown = "C:\\work\\kenza\\zpt\\Notedown\\Notedown.Windows\\bin\\Release\\Notedown.Windows.exe"
# fmuspad = r"C:\work\kenza\zpt\fmuspad\Tester\bin\Debug\Tester.exe"
fmuspad = r"C:\work\kenza\zpt\fmuspad\Tester\bin\Release\Tester.exe"
pager = r"C:\work\ciledug\ciledug\fmusperintah\handlers\pager\pager.exe"


statement_delimiter = ";;;"
potong_kiri = "<|"
potong_kanan = "|>"
more_potong_kiri = "🔴"
ganti_space = "🌙"
# 🔸 Orange Diamond
# 🔻 Red Triangle Pointed Down
# 🔺 Red Triangle Pointed Up
# 🔹 Small Blue Diamond
# 🔷 Large Blue Diamond
# 🔶 Large Orange Diamond
ganti_spaces = [ganti_space, "🔸", "🔹"]
lambang_continuation = "👉"
ganti_url = "🌐"
ganti_run = "⚡"
ganti_ketik = "✍️"
ganti_ketik2 = "👨‍💻"

# using_thread = True
using_thread = False

config_keys = read_json(joinhere(__file__, "keys.json"))
# print(config_keys)
delimiter_for_metadict = "||"

# konsep keren dimana kita bisa set variables
# !!50 pengen exec history number 50
# contoh: utk dg gampang masukkan hasil output, filepath, dst
# terminal_variables = {}

# utk %cari
search_result_to_commands = []
current_files_in_cwd = []


def remove_current_files_from_dict(dictionary):
    for item in current_files_in_cwd:
        dictionary.pop(item, None)


def add_current_files_to_dict(dictionary, daftar_files):
    dictionary.update({item: None for item in daftar_files})


import pyperclip
import datetime
import re


def generate_filename(filename="clipboard", extension="ts", suffix=None):
    # Generate a timestamp with no punctuation, separated by underscores
    timestamp = re.sub(r"[^a-zA-Z0-9]", "_", str(datetime.datetime.now()))

    # Combine the elements to create the final filename
    final_filename = f"{filename}_{timestamp}.{extension}"

    # # Add the suffix if specified
    # dari misalnya index.ts => index.tsx
    if suffix:
        final_filename = f"{final_filename}{suffix}"

    # print(f"generate_filename, extension=[{extension}], suffix=[{suffix}]")

    return final_filename


def copy_clipboard_to_file(suffix=None, force_filename=None):
    # print(f"copy_clipboard_to_file, suffix=[{suffix}]")
    # Get clipboard content using pyperclip
    clipboard_content = pyperclip.paste()
    if force_filename:
        filename = force_filename
    else:
        # Generate a filename using the previously defined function
        filename = generate_filename(suffix=suffix)

    # Write clipboard content to the file
    with open(filename, "w") as file:
        file.write(clipboard_content)

    # print(f'Clipboard content copied to {filename}')
    return filename


def test_warna(fg="#ff0066", bg=None, pesan="hello, world"):
    # https://python-prompt-toolkit.readthedocs.io/en/master/pages/printing_text.html
    print_formatted_text(
        HTML(f"<warna>{pesan}</warna>!"),
        style=Style.from_dict({"warna": f"bg:{'#'+bg+' ' if bg else ''}#{fg}"}),
    )


# 29 mar 2024, kita tambah keyword utk folders
# FP_CONFIG_DIR=C:\work\ciledug\ciledug\fmusperintah\configs
# FP_ROOT_DIR=C:\work\ciledug\ciledug\fmusperintah\configs
def potongify(text):
    # 5-12-23 tambah "space coder", bisa taro space di json
    # 🧭 hanya utk peek di text_area
    # 👉 utk lambang: hey ada lagi setelah ini
    # text = text.replace(ganti_space, " ").replace("🧭", "").replace("👉", "")
    text = text.replace("🧭", "").replace("👉", "") \
            .replace('FP_CONFIG_DIR', r"C:\work\ciledug\ciledug\fmusperintah\configs") \
                .replace('FP_ROOT_DIR', r"C:\work\ciledug\ciledug\fmusperintah")
    for char in ganti_spaces:
        text = text.replace(char, " ")
    while potong_kiri in text or more_potong_kiri in text or potong_kanan in text:
        # jangan lupa utk strip, karena "gen" dan " gen" jadi berbeda, " gen" malah panggilan wmcgen

        if more_potong_kiri in text:
            _, text = [item.strip() for item in text.split(more_potong_kiri, 1)]

        if potong_kiri in text:
            _, text = [item.strip() for item in text.split(potong_kiri, 1)]

        if potong_kanan in text:
            text, _ = [item.strip() for item in text.split(potong_kanan, 1)]
            # kita biarkan text turun ke bawah

    return text
