import os, re
from schnell.app.printutils import print_enumerate, indah4
from schnell.app.writers.file_handler import (
    ambil_acak,
    get_words_in_file,
    get_all_words_in_existing_files,
    get_definition_byword,
    get_words_from_number,
    get_words_from_zau,
    is_zau,
    number_filepath,
    search_word,
    terdeteksi,
    word_to_zaunumber,
    word_filepath,
    zau_filepath,
    zau_all_filepaths,
)
from schnell.app.writers.actor_handler import actor_name
from schnell.app.utils import perintah, platform, linuxpath_to_wslpath


EDITOR = "vscode"


def edit_zau_digit_word(word):
    if isinstance(word, int) or word.isdigit():
        filepath = number_filepath(word)
        # jk belum ada buat dulu
        perintah(f"touch {filepath}")
    elif is_zau(word):
        filepath = zau_filepath(word)
    else:
        filepath = word_filepath(word)

    # print(f'word_filepath utk {word} {filepath}')
    if platform() == "wsl":
        filepath = linuxpath_to_wslpath(filepath)
        # print(f'wslify word_filepath utk {word} {filepath}')
    kode = f"{EDITOR} {filepath}"
    indah4(f"[db.writer_service] {filepath}", warna="yellow")
    perintah(kode)


def process_writer(code, print_result=False, as_list=False):
    """
    load
    123
    /cari
    /*cari-case-sensitive
    /10/cari				10 before, 10 after
    /10*/cari
    /3,0/cari				3 before, 0 after
    #define-word
    *edit-word
    $1			get one randomly
    $1*			get one randomly + definition
    neo
    vert, tion
    """

    current_number = -1
    kembalian = ""

    if code == "load" or code == "reload":
        # print('exec load #1')
        words = get_all_words_in_existing_files(reload=True)
        kembalian = len(words)

    elif code.isdigit():
        # print('exec code isdigit #2')
        words = get_words_from_number(code)
        kembalian = words
        if not words:
            filepath_to_process = number_filepath(code)
            kembalian = f"{filepath_to_process} gak ditemukan"
            # kita kasih kesempatan utk mengbuatnya
            os.system(f"{EDITOR} {filepath_to_process}")

        current_number = code

    elif code.startswith("/"):
        """
        search
        /cari
        /*cari-case
        /10/cari
        /10*/cari-case
        /3,0/cari
                                                                                                        case sensitive			case insensitive
        limitchar context
        limitchar context
        normal: non sensitive, no horiz context
        """
        # print('exec starts with / #3')
        # search_word(pattern, case_sensitive=False, horizontal_context_limit=0)
        if code.startswith("/*"):
            # %/*cari-case-sensitive
            pattern = code.removeprefix("/*").strip()
            kembalian, err = search_word(pattern, case_sensitive=True)
        elif re.match(r"^/(\d+)/(.*)", code):
            # %/10/cari			grep limit: grep  -I -ro -P ".{0,10}naik.{0,10}" ..
            m = re.match(r"^/(\d+)/(.*)", code)
            context = int(m.group(1))
            pattern = m.group(2)
            kembalian, err = search_word(
                pattern, case_sensitive=False, horizontal_context_limit=context
            )
        elif re.match(r"^/(\d+)\*/(.*)", code):
            # %/10*/cari-case		grep limit: grep  -I -ro -P ".{0,10}naik.{0,10}" ..
            m = re.match(r"^/(\d+)\*/(.*)", code)
            context = int(m.group(1))
            pattern = m.group(2)
            kembalian, err = search_word(
                pattern, case_sensitive=True, horizontal_context_limit=context
            )
        elif re.match(r"^/(\d+),(\d+)/(.*)", code):
            # %/3,0/cari			before=3 lines, after=0 lines
            m = re.match(r"^/(\d+),(\d+)/(.*)", code)
            before = int(m.group(1))
            after = int(m.group(2))
            pattern = m.group(3)
            kembalian, err = search_word(
                pattern, case_sensitive=True, before=before, after=after
            )
        else:
            # %/cari
            pattern = code.removeprefix("/").strip()
            kembalian, err = search_word(pattern)

        if not kembalian and err:
            kembalian = err

    elif code.startswith("#"):  # define word
        # %#word 		define
        # print('exec startswith # #4')
        kembalian = get_definition_byword(code.removeprefix("#"))

    elif code.startswith("*"):  # edit file containing word
        # %*word		edit file
        word = code.removeprefix("*")
        if is_zau(word):
            filepath = zau_filepath(word)
        elif word.isdigit():
            filepath = number_filepath(word)
            # jk belum ada buat dulu
            perintah(f"touch {filepath}")
        else:
            filepath = word_filepath(word)

        # print(f'word_filepath utk {word} {filepath}')
        if platform() == "wsl":
            filepath = linuxpath_to_wslpath(filepath)
            # print(f'wslify word_filepath utk {word} {filepath}')
        kode = f"{EDITOR} {filepath}"
        indah4(f"[db.writer_service] {filepath}", warna="yellow")
        perintah(kode)
        # print(f'exec {kode}')
        kembalian = "OK"

    elif code.startswith("$"):  # choose random word
        # %$1 -> without definition, just the word
        # %$1* -> diakhiri star, minta definisi
        # print('exec startswith $ #5')
        code = code.removeprefix("$")
        ask_definition = False
        if code.endswith("*"):
            code = code.removesuffix("*")
            ask_definition = True
        if not code:
            kembalian = ambil_acak(1)
        elif code.isdigit():
            kembalian = ambil_acak(code)

        if ask_definition and kembalian:
            pemisah_kata_arti = "\n" + "=" * 80 + "\n"
            pemisah_antar_arti = "\n" + "-" * 80 + "\n"
            definisi = []
            for kata in kembalian.splitlines():
                definisi.append(get_definition_byword(kata))

            # print('[db.writer_service] definisi:', definisi)
            kembalian += pemisah_kata_arti + pemisah_antar_arti.join(definisi)

    elif is_zau(code):
        """
        ngasih spt neo, dio, dll
        keluarkan semua kata2 yg masuk class zau tsb
        """
        # print('exec is_zau #6')
        kembalian = get_words_from_zau(code)
        if len(kembalian) == 1:
            word = kembalian[0]
            current_number = word_to_zaunumber(word)

    else:
        kembalian = terdeteksi(code)
        print_enumerate(kembalian)
        # jk kembalian hanya ada 1 member, berarti itu kata terdekat,
        # atau yg mungkin dinginkan
        if len(kembalian) == 1:
            word = kembalian[0]
            kembalian = get_definition_byword(word)
            current_number = word_to_zaunumber(word)
        elif code in kembalian:
            # jk ada 1 yg match:
            # decided -> [decided], decidedly, undecided
            pemisah_kata_arti = "\n" + "=" * 80 + "\n"
            mulai_arti = "\n" + "-" * 40 + f" {code}" + "\n"
            definisi = get_definition_byword(code)
            kembalian.append(pemisah_kata_arti + mulai_arti + definisi)
        # print(f"""process_writer
        # code = {code}
        # word = {word}
        # kembalian = {kembalian}
        # current_number = {current_number}
        # """)

    # kembalian_as_list = kembalian
    if as_list:
        return kembalian

    if isinstance(kembalian, list):
        kembalian = "\n".join(kembalian)

    elif isinstance(kembalian, int):
        kembalian = str(kembalian)

    if int(current_number) > 0:
        actor = actor_name(current_number)
        kembalian = f"{actor}\n" + kembalian

    if print_result:
        indah4(kembalian, warna="yellow", layar="blue")

    return kembalian
