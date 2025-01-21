import json, re
from schnell.db.mapper import map_input
from schnell.db.myredis_common import (
    get_connection,
    try_redis_connect,
    redis_connect,
    redis_publish,
    docker_start_redis,
    load_bylangs,
    redis_keys_recurse,
    redis_value_recurse,
    redis_get_daftar,
    shortens,
    shorten_keys,
)
from schnell.db.redis_config import redis_config
from schnell.db.replservice import ReplService, repl_service
from schnell.app.printutils import (
    print_list_warna,
    indah0,
    indah3,
    indah4,
    pp,
)
from schnell.app.utils import (
    env_get,
    env_int,
    replace_wiekes,
    get_suffix_angka,
    platform,
)


key_delimiter = ":"


def redis_repl_search_service(code, REPL=None):
    wiekes = None
    if env_int("ULIBPY_FMUS_DEBUG") > 1:
        print("redis_repl_search_service:", code)
    result = ""
    metaresult = {}

    if redis_config["r"] is None:
        try:
            # try_redis_connect()
            redis_config["r"] = redis_connect(db=7)
            redis_config["r"].ping()
            redis_config["pub"] = redis_connect(db=0)
            redis_config["sub"] = redis_connect(db=0)
            # result += 'config: ' + str(redis_config)
        except Exception as err:
            import time

            print("[db.redis_repl_search_service] gagal koneksi redis:", err)
            # result += 'gagal koneksi redis: ' + str(err)
            docker_start_redis()
            time.sleep(0.5)
            # try_redis_connect()
            redis_config["r"] = redis_connect(db=7)
            redis_config["r"].ping()
            redis_config["pub"] = redis_connect(db=0)
            redis_config["sub"] = redis_connect(db=0)
            indah4(
                "[db.redis_repl_search_service] reconnecting to redis r0, pub, sub after docker start...",
                warna="yellow",
            )

    ####################################
    # cek wiekes
    if "\\" in code:
        # code, wiekes = code.split('\\')
        # code, wiekes = (lambda x, *y: (x, y))(*code.split('\\'))
        # code, wiekes = code.split(None, maxsplit=1)
        # https://stackoverflow.com/questions/3513947/pythonic-way-to-split-a-list-into-first-and-rest
        split_by_backslash = code.split("\\")
        # bisa saja ini ls c:\....sehingga harusnya kode = ls, sisanya filepath
        # di sini split_by_backslash hasilkan: [ls "C:", "Users", "user", "Desktop", "file.txt"]
        # di bawah ini hasilkan: ls "C", ("Users", "user", "Desktop", "file.txt")
        # /p)$ dir "C:\\Program Files\\Java\\jdk-11.0.13"
        # hasilkan:
        # found code: p)$ dir "C:
        # found wiekes: ('', 'Program Files', '', 'Java', '', 'jdk-11.0.13"')
        # ini bukan wiekes
        if not split_by_backslash[0].lower().endswith("c:"):
            code, wiekes = (lambda x, *y: (x, y))(*split_by_backslash)
            print("[redis_repl_search_service][found backslash] found code:", code)
            print("[redis_repl_search_service][found backslash] found wiekes:", wiekes)
    ####################################

    if code == ".conn" or code == ".C":
        redis_config["r"] = redis_connect()
        redis_config["pub"] = redis_connect(db=0)
        redis_config["sub"] = redis_connect(db=0)
        result += "db connected..."

    elif code == ".load" or code == ".L":
        load_bylangs(redis_config["r"])
        result += "loaded..."

    # elif code == '.CLR':
    # 	redis_clear_db(redis_config['r'])
    # 	result += 'clear language db...please reload with .L'

    elif code.endswith("@"):
        code = code.removesuffix("@")
        if code:
            a = redis_value_recurse(redis_config["r"], code, REPL=REPL)
            # indah3(a)
            if a:
                result += a
                metaresult.update({"code": code})

    elif code.endswith("#"):
        code = code.removesuffix("#")
        if code:
            code = map_input(code)
            print("[db.redis_repl_search_service] mapped input:", code)
            a = redis_value_recurse(redis_config["r"], code, print_keys=True, REPL=REPL)
            if a:
                # print_list_warna(redis_keys_recurse(redis_config['r'], code))
                pipa = " | "
                nl = "\n"
                entries_mulai_newline = env_int("ULIBPY_DAFTARZ_BYLINE_AFTER", 5)
                pipa_or_newline = (
                    lambda entries: pipa
                    if len(entries) <= entries_mulai_newline
                    else nl
                )
                daftarz_sorted = redis_get_daftar(redis_config["r"], code)
                # print(f'daftarz_sorted {code}:', daftarz_sorted)
                toc = nl.join(daftarz_sorted)
                metaresult.update({"toc": toc})
                indah3(toc, warna="magenta")
                #################
                if wiekes:
                    a = replace_wiekes(a, wiekes)
                #################
                # indah3(a)
                result += a

    else:
        if code:
            is_choosing = None
            is_angka = get_suffix_angka(code)
            pipa_angka = get_suffix_angka(code, pipa="|")
            slash_angka = get_suffix_angka(code, pipa="/")
            if is_angka and (
                pipa_angka == "|" + is_angka or slash_angka == "/" + is_angka
            ):
                if env_int("ULIBPY_FMUS_DEBUG") > 1:
                    print(
                        f"[db.redis_repl_search_service] is_choosing: {is_choosing}, is_angka {is_angka} utk pipa_angka: {pipa_angka}."
                    )
                is_choosing = int(is_angka)
                if env_int("ULIBPY_FMUS_DEBUG") > 1:
                    print(f"[db.redis_repl_search_service] is_choosing: {is_choosing}.")
                if pipa_angka == "|" + is_angka:
                    code = code.removesuffix(pipa_angka)
                else:
                    code = code.removesuffix(slash_angka)

            a = redis_keys_recurse(redis_config["r"], code, sort=True, mapper=True)
            print_list_warna(a, extra_warna={5: "white"})
            metaresult.update({"keys": a})

            # indah4(f"""[redis_repl_search_service] debugging variables
            # is_choosing = {is_choosing}
            # a / the_list = {a}
            # """, warna='cyan')

            # is_choosing bisa None, 0, dst.
            if (is_choosing is not None) and (0 <= is_choosing <= len(a)):
                #################### START ADD: agar sama dg myredis.py
                if env_int("ULIBPY_FMUS_DEBUG") > 1:
                    print(f"[myredis] #1 is_choosing: {is_choosing} utk a: {a[:10]}...")
                filepath = a[is_choosing]
                if env_int("ULIBPY_FMUS_DEBUG") > 1:
                    print(
                        f"[myredis] #2 is_choosing: {is_choosing} utk a: =hasilkan=> {filepath}"
                    )
                # filepath_filepart, filepath_barispart = filepath.split(':', 1)
                if re.match(r"^[cde]:", filepath.lower()):
                    if ".mk" in filepath:
                        _file, filepath_barispart = filepath.split(".mk:", 1)
                        filepath_filepart = _file + ".mk"
                    elif ".fmus" in filepath:
                        _file, filepath_barispart = filepath.split(".fmus:", 1)
                        filepath_filepart = _file + ".fmus"
                else:
                    filepath_filepart, filepath_barispart = filepath.split(":", 1)

                if filepath.startswith(shorten_keys[0]) or filepath.startswith(
                    shorten_keys[1]
                ):
                    filepath = shortens[filepath[0]] + filepath[1:]
                #################### END ADD

                if env_int("ULIBPY_FMUS_DEBUG") > 1:
                    print(
                        f"[db.redis_repl_search_service] is_choosing: {is_choosing} utk a: {a[:10]}..."
                    )

                b = redis_value_recurse(
                    redis_config["r"],
                    filepath,
                    print_keys=True,
                    is_fullkey=True,
                    REPL=REPL,
                )
                # b = redis_value_recurse(redis_config['r'], a[is_choosing], print_keys=True, is_fullkey=True, REPL=REPL)

                if b:
                    last_file = filepath_filepart
                    for k, v in shortens.items():
                        last_file = last_file.replace(k, v)
                    metaresult.update({"last_file": last_file})
                    # metaresult.update({'last_file': filepath_filepart})
                    result += b
            elif len(a) == 1 and env_int("ULIBPY_REDIS_ONE_IS_VIEWING", 1):
                """
                jika ada satu hasil dari redis_keys_recurse = satu file
                maka print isinya
                """
                #################### START ADD: agar sama dg myredis.py
                filepath = a[0]
                # 0. /docker.rb.mk:EP:ESF exec shell form / CMD string vs list, exec form vs shell form
                # c:/something:baris harus dihandle di sini, krn klo gak, hasilkan c, /something:baris
                # dan filepath c akan selalu gagal
                if re.match(r"^[cde]:", filepath.lower()):
                    if ".mk" in filepath:
                        _file, filepath_barispart = filepath.split(".mk:", 1)
                        filepath_filepart = _file + ".mk"
                    elif ".fmus" in filepath:
                        _file, filepath_barispart = filepath.split(".fmus:", 1)
                        filepath_filepart = _file + ".fmus"
                else:
                    filepath_filepart, filepath_barispart = filepath.split(":", 1)
                # if not isfile(filepath_filepart):
                # 	if not filepath.startswith(BYLANGSDIR):
                # 		filepath = BYLANGSDIR + filepath
                if filepath.startswith(shorten_keys[0]) or filepath.startswith(
                    shorten_keys[1]
                ):
                    filepath = shortens[filepath[0]] + filepath[1:]

                # ini skrg dah gak perlu lagi
                # if filepath_filepart.lower().startswith('c:'):
                # 	from app.stringutils import split_by_pos
                # 	# : pertama = C: of filepath
                # 	# : kedua baru filepath:baris_cari
                # 	pecah = split_by_pos(filepath_filepart, key_delimiter, 2)
                # 	# print('pecah', pecah)
                # 	filepath, baris_cari = pecah

                b = redis_value_recurse(
                    redis_config["r"],
                    filepath,
                    print_keys=True,
                    is_fullkey=True,
                    REPL=REPL,
                )
                #################### END ADD
                # b = redis_value_recurse(redis_config['r'], a[0], print_keys=True, is_fullkey=True, REPL=REPL)
                if b:
                    #################
                    if wiekes:
                        b = replace_wiekes(b, wiekes)
                    #################
                    last_file = filepath_filepart
                    for k, v in shortens.items():
                        last_file = last_file.replace(k, v)
                    metaresult.update({"last_file": last_file})
                    result += b
            else:
                formatted = [f"{i}. {item}" for i, item in enumerate(a)]
                result += "\n".join(formatted)

    return result, metaresult
