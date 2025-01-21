import json, re, traceback, os, sys
import time
from pprint import pprint
import redis

# if __name__ in ['myredis', '__main__']:
# 	import os, sys

# 	curdir = os.path.dirname(__file__)
# 	schnelldir = os.path.join(curdir, os.pardir)
# 	sidoarjodir = os.path.join(schnelldir, os.pardir)
# 	sys.path.extend([sidoarjodir, schnelldir])
# 	from dotenv import load_dotenv
# 	load_dotenv(os.path.join(schnelldir, '.env'))
# print('mr1')
if __name__ in ["myredis", "__main__"]:
    dbdir = os.path.dirname(__file__)
    schnelldir = os.path.join(dbdir, os.pardir)
    sidoarjodir = os.path.join(schnelldir, os.pardir)
    sys.path.extend([sidoarjodir, schnelldir])
    from dotenv import load_dotenv

    load_dotenv(os.path.join(schnelldir, ".env"))
# print('mr2')
from schnell.app.appconfig import programming_data
from schnell.app.datetimeutils import lama_operasi
from schnell.app.dirutils import (
    # ayah, joiner, here, exists_in_dir_bypattern,
    isdir,
    isfile,
    walk_fullpath,
)
from schnell.app.fileutils import (
    get_daftar,
    get_definition_by_key_permissive_start,
    get_definition_by_key_permissive_start_with_lineno,
    file_write,
)
from schnell.app.osutils import is_linux_path_on_windows_and_convert
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
from schnell.app.richutils import print_markdown, print_copy_markdown
from schnell.db.mapper import map_input

# print('mr3')
from schnell.db.replservice import ReplService, repl_service

# print('mr3a')
from schnell.db.redis_config import redis_config

# print('mr3b')
from schnell.db.myredis_common import (
    all_redis_keys,
    docker_start_redis,
    get_connection,
    load_bylangs,
    redis_connect,
    redis_get_daftar,
    redis_keys_recurse,
    redis_publish,
    redis_value_recurse,
    try_redis_connect,
)

# print('mr3c')
from schnell.creator.repl_help import bahasa_entry

# print('mr3d')
from .redis_repl_from_vscode import redis_repl_from_vscode

# print('mr3e')
from .redis_repl_search_service import redis_repl_search_service

# print('mr4')

# algorithm = {
# 	'1': search_algo1,
# 	'2': search_algo2,
# 	'3': search_algo3,
# }

SubKey = "Sub"
PubKey = "Pub"


# search_algorithm_index = programming_data['j']['schnell']['app']['configuration']['ULIBPY_SEARCH_ALGO']
# pengurutan = lambda tempres, keylist: algorithm[search_algorithm_index](tempres, keylist)

# utk ULIBPY_REDISKEY_SHORTVIEW
SNIPPETSDIR = programming_data["j"]["schnell"]["app"]["configuration"][
    "ULIBPY_SNIPPETS"
]
# SNIPPETSDIR = env_get('ULIBPY_SNIPPETS')
BYLANGSDIR = programming_data["j"]["schnell"]["app"]["configuration"][
    "ULIBPY_BYLANGSDIR"
]
ULIBPY_DAFTARZ_BYLINE_AFTER = programming_data["j"]["schnell"]["app"]["configuration"][
    "ULIBPY_DAFTARZ_BYLINE_AFTER"
]
ULIBPY_USE_MARKDOWN_PRINTER = programming_data["j"]["schnell"]["app"]["configuration"][
    "ULIBPY_USE_MARKDOWN_PRINTER"
]
ULIBPY_REDIS_ONE_IS_VIEWING = programming_data["j"]["schnell"]["app"]["configuration"][
    "ULIBPY_REDIS_ONE_IS_VIEWING"
]
# BYLANGSDIR = env_get('ULIBPY_BYLANGSDIR')
wiekesym = programming_data["j"]["schnell"]["app"]["configuration"][
    "ULIBPY_WIEKES_TEMPLATE_PREFIX"
]
# wiekesym = env_get('ULIBPY_WIEKES_TEMPLATE_PREFIX')

shortens = {
    "$": SNIPPETSDIR,
    "@": BYLANGSDIR,
}
shorten_keys = list(shortens.keys())
# there are no duplicate values
# https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
replacens = dict(zip(shortens.values(), shortens.keys()))
key_delimiter = ":"


def redis_keys(r, cari=None, sort=True):
    if cari is None:
        kuncis = r.keys("*")
    else:
        kuncis = r.keys(f"*{cari}*")

    kuncis = [item.decode("utf8") for item in kuncis]

    if sort:
        return sorted(kuncis)

    return kuncis


def redis_deletes(r, cari, recurse=False, confirm=True):
    """
    https://stackoverflow.com/questions/21975228/redis-python-how-to-delete-all-keys-according-to-a-specific-pattern-in-python

    for key in x: cache.delete(key)

    Using redis-python package you can do that such way: cache.delete(*keys)
    """
    if recurse:
        kuncis = redis_keys_recurse(r, cari)
    else:
        kuncis = redis_keys(r, cari)

    if kuncis:
        if confirm:
            try:
                pprint(kuncis)
            except:
                """[BlockingIOError: [Errno 11] write could not complete without blocking]
                File "/home/usef/work/sidoarjo/schnell/db/myredis.py", line 122, in redis_deletes
                        pprint(kuncis)
                File "/home/usef/.local/lib/python3.9/site-packages/rich/pretty.py", line 925, in pprint
                        _console.print(
                File "/home/usef/.local/lib/python3.9/site-packages/rich/console.py", line 1683, in print
                        self._buffer.extend(new_segments)
                File "/home/usef/.local/lib/python3.9/site-packages/rich/console.py", line 838, in __exit__
                        self._exit_buffer()
                File "/home/usef/.local/lib/python3.9/site-packages/rich/console.py", line 796, in _exit_buffer
                        self._check_buffer()
                File "/home/usef/.local/lib/python3.9/site-packages/rich/console.py", line 2005, in _check_buffer
                        self.file.write(text)
                """
                pprint(kuncis)
            indah4(
                f"""[myredis][redis_deletes] Sure to delete ({len(kuncis)} items) ? """,
                newline=False,
            )
            yesno = input(" ")
            if yesno.lower() == "y":
                r.delete(*kuncis)
        else:
            r.delete(*kuncis)


def redis_value(r, key, key_delimiter_=key_delimiter, get_from_db=False, REPL=None):
    """
    selalu kembalikan list

    ternyata masih get dari filepath, bukan dari redis
    """
    full_key = redis_keys(r, key)
    if not full_key:
        return None
    full_key = full_key[0]
    # di sini full_key adlh b'', hrs konversi dulu ke str
    if isinstance(full_key, (bytes, bytearray)):
        full_key = full_key.decode("utf8")
    filepath, baris_cari = full_key.split(key_delimiter_, 1)

    if get_from_db:
        superkey = f"{filepath}:{baris_cari}"
        result = r.get(superkey)
        if REPL:
            REPL.last_file = filepath
        return result

    elif isfile(filepath):
        if env_int("ULIBPY_FMUS_DEBUG") > 1:
            print(f"redis_value {filepath}:{baris_cari}")
        # return get_definition_by_key_permissive_start(filepath, baris_cari)
        result, lineno = get_definition_by_key_permissive_start_with_lineno(
            filepath, baris_cari
        )
        if REPL:
            REPL.last_file = filepath
            REPL.last_lineno = lineno
        return result

    return None


def redis_clear_db(r, all_db=False):
    if all_db:
        r.flushall()
        return 1

    r.flushdb()
    return 1


def redis_remove(r, cari, recurse=False):
    redis_deletes(r, cari, recurse)


def redis_add_channel(channel, r=None, default_set_name="active_channels"):
    if not r:
        r = get_connection("sub")
    r.sadd(default_set_name, channel)
    print("redis_add_channel ok")


def redis_rem_channel(channel, r=None, default_set_name="active_channels"):
    if not r:
        r = get_connection("sub")
    r.srem(default_set_name, channel)
    print("redis_rem_channel ok")


def redis_list_channel(r=None, default_set_name="active_channels"):
    if not r:
        r = get_connection("sub")
    return r.smembers(default_set_name)


def default_subscribe_callback(*args):
    print(*args)


skip_publish_channels = ["android", "test", "guest"]


def redis_subscribe(channel, r=None, message_callback=default_subscribe_callback):
    """
    mengenai data yg datang ke kanal:
    redis_conn = redis.Redis(charset="utf-8", decode_responses=True)

    We can only publish messages of type string, bytes or float,
    but when the subscriber gets a message from the channel,
    it comes as a dictionary object:
    {
     "type": "message",
                    There are six types:
                            subscribe, unsubscribe, psubscribe, punsubscribe, message, pmessage.
                    We are only interested in the message type for this tutorial.
     "pattern": None,
     "channel": b"broadcast",
     "data": b"hello"
    }
    """
    if not r:
        r = get_connection("sub")

    try:
        pubsub = r.pubsub()
    except Exception as err:
        print('[myredis] "pubsub = r.pubsub()" => redis belum jalan:', err)
        print("[myredis] redis_config:", redis_config)
        try_redis_connect()
        time.sleep(1.0)
        r = get_connection("sub")
        pubsub = r.pubsub()
        print("[myredis][redis_subscribe]", r)

    pubsub.subscribe(channel)

    try:
        for message in pubsub.listen():
            print(
                f"""[db.myredis][redis_subscribe] jenis pesan: [{message['type']}] kanal [{message['channel']}]"""
            )
            kanal_redis = message["channel"].decode("utf8")
            if kanal_redis in skip_publish_channels:
                print(
                    f"""kanal_redis [{kanal_redis}] in skip_publish_channels [{skip_publish_channels}]
				type = {message['type']}
				data = {message['data']}
				"""
                )
                continue

            if message.get("type") == "message":
                # message punya type dan data, data bisa string atau dict
                data = json.loads(message.get("data"))

                print(
                    "*" * 20
                    + f"[db.myredis][redis_subscribe] kanal = [{channel}] menerima data berjenis [{type(data)}]:"
                )
                # data: selamat deh
                pp(data)
                # message: {'type': 'message', 'pattern': None, 'channel': b'notif', 'data': b'"selamat deh"'}
                # print('message:', message)
                print("*" * 20)

                if isinstance(data, (bytes, bytearray, str)):
                    # keluar dg
                    # /Pub <nama kanal>|quit
                    # {'type': 'message', 'pattern': None, 'channel': b'command', 'data': b'"hello baby"'}
                    if not isinstance(data, str):
                        data = data.decode("utf8")
                    print(
                        f"""[db.myredis] terima Pub data berjenis bytes/bytearray/str:\n\n{data}"""
                    )
                    if data in ["quit", "bye", "exit", "q", "x"]:
                        return
                    else:
                        # UPD 9 Jul 2022, handle dg replservice
                        # tapi utk mengirim respond, client jg hrs mendengar dari kanal kedua
                        # server mendengar di kanal: namakanal_request
                        # 	mengirim ke kanal: namakanal_response
                        # client mendengar di kanal: namakanal_response
                        # 	mengirim ke kanal: namakanal_request

                        # hasil, meta = repl_service.process(content, meta_input=metacontent)
                        # data = {
                        # 	'content': hasil,
                        # 	'meta': meta,
                        # 	'original': metacontent,
                        # }
                        # redis_publish(data, redis_config['from_server'])
                        # request_kanal = redis_config['request_kanal'] == channel
                        response_kanal = redis_config["response_kanal"]
                        # answer = f"We acknowledge your request: {data}."
                        answer, _ = repl_service.process(data)
                        indah4(answer)
                        redis_publish(answer, response_kanal)

                else:  # dict message utk pesan dari vscode
                    # kirim jawaban
                    # redis_publish(f'SERVER TELAH PROSES {data}!', redis_config['from_server'])
                    try:
                        redis_repl_from_vscode(data)
                    except Exception as err:
                        indah4(
                            f"[db.myredis] Gagal: [{err}]\nwaktu minta jawaban dari repl service.",
                            warna="red",
                        )
                        indah4(traceback.format_exc(), warna="magenta")
                        # kirim error ke client
                        data = {
                            # TypeError: Object of type UnexpectedCharacters is not JSON serializable
                            "content": str(err),
                            "original": data,
                        }
                        redis_publish(data, redis_config["from_server"])

                if message_callback:
                    message_callback(data, message)

            else:
                print("""redis_subscribe: unknown type, message:""", message)

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    except EOFError:
        print("EOFError")
    except Exception as err:
        print("Exception:", err)
        print(traceback.format_exc())


def write_ip_file_for_extension():
    """
    ini dari dalam wsl
    """
    if platform() != "wsl":
        return
    # filepath = '/mnt/c/Users/user/ip'
    # filepath = env_get('ULIBPY_WHERE_TO_WRITE_WSL_IP_ADDR')
    filepath = programming_data["j"]["schnell"]["app"]["configuration"][
        "ULIBPY_WHERE_TO_WRITE_WSL_IP_ADDR"
    ]
    import socket, fcntl, struct

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    alamat = socket.inet_ntoa(
        fcntl.ioctl(
            s.fileno(), 0x8915, struct.pack("256s", "eth0"[:15].encode("utf-8"))
        )[20:24]
    )
    file_write(filepath, alamat)
    indah4(
        f"[myredis] Selesai menulis ip '{alamat}' ke file '{filepath}'", warna="green"
    )


def handlePubsub(code, channel_msg_delimiter="|"):
    """
    listen:
    /S
    /S channel_name
    /Sub
    /Sub channel_name
    fungsi pendengar ada di: redis_subscribe

    send:
    /Pub channel_name|hello, world!
    /Pub channel_name|hello baby
    /Pub channel_name|x utk hentikan /S

    g "//Pub mycnannel|hello"
    pub channelname|message

    [myredis] Pub command
            code = command|hello baby
            channel = command
            message = hello baby
    """
    if code.startswith(SubKey) or code == "S" or code.startswith("S "):
        # channel = code.removeprefix('sub' if code.startswith('sub') else 'S').strip()
        # tulis file ip utk digunakan oleh terminal/js/vscode-ext/extension.ts

        # write_ip_file_for_extension() # disable, 24/4/2022

        if code.startswith(SubKey):
            channel = code.removeprefix(SubKey)
        elif code.startswith("S "):
            channel = code.removeprefix("S ")
        else:
            channel = ""
        channel = (
            channel.strip()
        )  # penting nih agar bisa /Sub <namakanal> tanpa harus /Sub<nama kanal>

        channel_name = channel if channel else redis_config["from_client"]

        # if channel:
        # 	redis_subscribe(channel)
        # else:
        # redis_subscribe(redis_config['from_client'])
        # if not channel:
        # 	channel_name = redis_config['from_client']

        # redis_client.srem('active_channels', channel_name)
        redis_add_channel(channel_name)
        indah4(f"Sub active channels [{redis_list_channel()}]", warna="magenta")
        redis_subscribe(channel_name)

    elif code.startswith(PubKey):
        code = code.removeprefix(PubKey).strip()
        if code and code.count(channel_msg_delimiter) == 1:
            channel, message = [
                item.strip() for item in code.split(channel_msg_delimiter)
            ]
            print(
                f"""[myredis] Pub command
			code = {code}
			channel = {channel}
			message = {message}
			"""
            )
            if channel and message:
                redis_publish(message, channel)
            elif message:
                redis_publish(message, redis_config["from_server"])


def redis_repl(code, REPL):
    """
    dipanggil dg /<perintah> dari kbrepl.
    """
    wiekes = None

    if env_int("ULIBPY_FMUS_DEBUG") > 1:
        print("[myredis] redis_repl:", code)

    if redis_config["r"] is None:
        try:
            redis_config["r"] = redis_connect()
            # https://stackoverflow.com/questions/12857604/python-how-to-check-if-redis-server-is-available
            redis_config["r"].ping()
            redis_config["pub"] = redis_connect(db=0)
            redis_config["sub"] = redis_connect(db=0)
            if env_int("ULIBPY_FMUS_DEBUG") > 1:
                print("[myredis] config:", redis_config)
        except Exception as err:
            print("[myredis] gagal koneksi redis:", err)
            docker_start_redis()

    ####################################
    # cek wiekes
    if "\\" in code:
        # code, wiekes = code.split('\\')
        # code, wiekes = (lambda x, *y: (x, y))(*code.split('\\'))
        # code, wiekes = code.split(None, maxsplit=1)
        # https://stackoverflow.com/questions/3513947/pythonic-way-to-split-a-list-into-first-and-rest
        code, wiekes = (lambda x, *y: (x, y))(*code.split("\\"))
        print("[myredis] found code:", code)
        print("[myredis] found wiekes:", wiekes)

    ####################################

    if code == ".conn" or code == ".C":
        redis_config["r"] = redis_connect()
        redis_config["pub"] = redis_connect(db=0)
        redis_config["sub"] = redis_connect(db=0)

    elif code == ".load" or code == ".L":
        load_bylangs(redis_config["r"])
        print("[myredis] loaded...")

    elif code == ".CLR":
        redis_clear_db(redis_config["r"])
        print("[myredis] clear language db...please reload with .L")

    elif code.startswith(".clearload") or code == ".reboot" or code == ".restart":
        if code in [".reboot", ".restart"]:
            code = ""
        else:
            code = code.removeprefix(".clearload").strip()
        if code:
            if isdir(code):
                newpath = isdir(code)

                def lakukan():
                    redis_deletes(redis_config["r"], f"{newpath}*", confirm=False)
                    load_bylangs(
                        redis_config["r"], with_snippets=False, langsdir=newpath
                    )

                print(
                    f"[{lama_operasi(lakukan)} detik] [myredis] clear + load {newpath}..."
                )
            else:
                print(f"[myredis] {code} is not dir")
        else:

            def lakukan():
                redis_clear_db(redis_config["r"])
                load_bylangs(redis_config["r"], with_snippets=False)

            print(f"[{lama_operasi(lakukan)} detik] [myredis] clear + load...")

    elif code.startswith(".loadfile"):
        filepath = code.removeprefix(".loadfile").strip()
        if filepath and isfile(filepath):
            from .myredis_common import load_mkfile_to_redis

            load_mkfile_to_redis(redis_config["r"], filepath)

    elif code.startswith(".D"):
        """
        D *_ng*
        krn recurse, cukup D _ng ?
        """
        code = code.removeprefix(".D").strip()
        print("[myredis] want delete:", code)
        new_code = isdir(code)  # bongkar, kembalikan false atau bongkared path
        if new_code:  # hanya jk (bongkared) path
            redis_deletes(redis_config["r"], new_code, recurse=True)
        else:
            redis_deletes(redis_config["r"], code, recurse=True)

    elif code.startswith(".K "):
        # g "//.K grid"
        code = code.removeprefix(".K ")
        new_code = isdir(code)
        # print(f"code {code}, newcode {new_code}")
        if new_code:
            a = redis_keys(redis_config["r"], new_code)
        else:
            a = redis_keys(redis_config["r"], code)
        print_list_warna(a)

    elif code.startswith(".K2 "):
        # g "//.K2 grid layout"
        code = code.removeprefix(".K2 ")
        if code:
            a = redis_keys_recurse(redis_config["r"], code, sort=True)
            print_list_warna(a)

    elif code.startswith(".K3 "):
        code = code.removeprefix(".K3 ")
        if code:
            a = redis_keys_recurse(redis_config["r"], code, sort=True, mapper=True)
            print_list_warna(a)

    elif code.startswith(".V "):
        code = code.removeprefix(".V ").replace(" ", "*")
        if code:
            a = redis_value(redis_config["r"], code)
            indah3(a)

    elif code.startswith(".V2 "):
        code = code.removeprefix(".V2 ")
        if code:
            a = redis_value_recurse(redis_config["r"], code)
            indah3(a)

    elif code.startswith("@") or code.endswith("@"):
        if code.endswith("@"):
            code = code.removesuffix("@")
        else:
            code = code.removeprefix("@")

        if code:
            a = redis_value_recurse(redis_config["r"], code, REPL=REPL)
            indah3(a)

    elif code.startswith(".V3 "):
        code = code.removeprefix(".V3 ")
        if code:
            a = redis_value_recurse(redis_config["r"], code, mapper=True)
            indah3(a)

    elif (
        code.startswith(SubKey)
        or code == "S"
        or code.startswith("S ")
        or code.startswith(PubKey)
    ):
        """
        TODO: cek apa jadi makan searching value yg lain
        TODO: ubah sub, pub, dll dg kode yg aman, searching /substringBefore jadi kemakan
        contoh:
        /^subscribe
        /^publish
        /sub terlalu panjang
        mending /S :)
        """
        indah4(
            f"handling pubsub subscribe krn startswith: /Sub atau /Pub atau /S<space> atau ==S",
            warna="yellow",
        )
        handlePubsub(code)

    elif code in ["activechannels", "active", "active_channels"]:
        indah4(f"Sub active channels [{redis_list_channel()}]", warna="magenta")

    elif code.startswith("#") or code.endswith("#"):
        """
        ini cara brilian biar bisa
        lihat key dulu
        jk ok
        kasih sufix # utk lihat value
        """
        if code.endswith("#"):
            code = code.removesuffix("#")
        else:
            code = code.removeprefix("#")
        if code:
            code = map_input(code)
            print("mapped input:", code)
            a = redis_value_recurse(redis_config["r"], code, print_keys=True, REPL=REPL)
            if a:
                # print_list_warna(redis_keys_recurse(redis_config['r'], code))
                pipa = " | "
                nl = "\n"
                entries_mulai_newline = ULIBPY_DAFTARZ_BYLINE_AFTER  # env_int('ULIBPY_DAFTARZ_BYLINE_AFTER')
                pipa_or_newline = (
                    lambda entries: pipa
                    if len(entries) <= entries_mulai_newline
                    else nl
                )
                daftarz_sorted = redis_get_daftar(redis_config["r"], code)
                # print(f'daftarz_sorted {code}:', daftarz_sorted)
                indah3(nl.join(daftarz_sorted), warna="magenta")
                #################
                if wiekes:
                    a = replace_wiekes(a, wiekes)
                #################
                indah3(a)

    elif code.startswith("repl:"):
        """
        apa nih?
        menggunakan replservice spt di vscode, hanya saja via terminal
        """
        code = code.removeprefix("repl:").strip()
        repl_service.process(code)

    else:
        # default setara r.keys
        if code:
            # /something
            # /something|0
            # /something|1
            if env_int("ULIBPY_FMUS_DEBUG") > 1:
                print("[myredis] redis_repl, lanjut proses:", code)
            # UPDATE: berikan bahasa_entry

            baris_entry = bahasa_entry(code)
            if baris_entry:
                indah4(baris_entry, warna="white")

            is_choosing = None
            is_angka = get_suffix_angka(code)
            pipa_angka = get_suffix_angka(code, pipa="|")
            slash_angka = get_suffix_angka(code, pipa="/")
            # if env_int('ULIBPY_FMUS_DEBUG')>1:
            # 	print(f'pipa_angka: {pipa_angka} == |+is_angka: {is_angka}?')
            if is_angka and (
                pipa_angka == "|" + is_angka or slash_angka == "/" + is_angka
            ):
                if env_int("ULIBPY_FMUS_DEBUG") > 1:
                    print(
                        f"[myredis] is_choosing: {is_choosing}, is_angka {is_angka} utk pipa_angka: {pipa_angka}."
                    )
                is_choosing = int(is_angka)
                if env_int("ULIBPY_FMUS_DEBUG") > 1:
                    print(f"[myredis] is_choosing: {is_choosing}.")
                if pipa_angka == "|" + is_angka:
                    code = code.removesuffix(pipa_angka)
                else:
                    code = code.removesuffix(slash_angka)

            a = redis_keys_recurse(
                redis_config["r"], code, mapper=True
            )  # print daftar isi
            print_list_warna(a, extra_warna={10: "white"})  # tadinya 5:'red'

            if (is_choosing is not None) and (0 <= is_choosing <= len(a)):
                """
                choosing dg
                text/angka
                text|angka
                """
                if env_int("ULIBPY_FMUS_DEBUG") > 1:
                    print(f"[myredis] #1 is_choosing: {is_choosing} utk a: {a[:10]}...")
                filepath = a[is_choosing]
                if env_int("ULIBPY_FMUS_DEBUG") > 1:
                    print(
                        f"[myredis] #2 is_choosing: {is_choosing} utk a: =hasilkan=> {filepath}"
                    )
                filepath_filepart, filepath_barispart = filepath.split(":", 1)
                # if not isfile(filepath_filepart):
                # 	if not filepath.startswith(BYLANGSDIR):
                # 		filepath = BYLANGSDIR + filepath
                if filepath.startswith(shorten_keys[0]) or filepath.startswith(
                    shorten_keys[1]
                ):
                    filepath = shortens[filepath[0]] + filepath[1:]
                if env_int("ULIBPY_FMUS_DEBUG") > 1:
                    print(f"[myredis] #3 is_choosing: {is_choosing} => {filepath}")
                b = redis_value_recurse(
                    redis_config["r"],
                    filepath,
                    print_keys=True,
                    is_fullkey=True,
                    REPL=REPL,
                )
                if b:
                    #################
                    # if wiekes:
                    # 	b = replace_wiekes(b, wiekes)
                    #################
                    # indah3('-'*10 + ' ' + filepath_barispart, warna='red')
                    indah4(
                        "-" * 10 + " " + filepath_filepart + " | " + filepath_barispart,
                        warna="red",
                    )
                    if (
                        ULIBPY_USE_MARKDOWN_PRINTER
                    ):  # env_int('ULIBPY_USE_MARKDOWN_PRINTER'):
                        print_copy_markdown(b)
                    else:
                        indah3(b)
                # if env_int('ULIBPY_FMUS_DEBUG')>1 and not b:
                # 	indah4(f"""
                # 	{filepath}
                # 	print_keys=True
                # 	is_fullkey=True
                # 	REPL=REPL
                # 	""", warna='magenta', layar='green')

            elif (
                len(a) == 1 and ULIBPY_REDIS_ONE_IS_VIEWING
            ):  # env_int('ULIBPY_REDIS_ONE_IS_VIEWING'):
                # jika ada satu hasil dari redis_keys_recurse = satu file
                # maka print isinya

                filepath = a[0]
                # 0. /docker.rb.mk:EP:ESF exec shell form / CMD string vs list, exec form vs shell form
                filepath_filepart, filepath_barispart = filepath.split(":", 1)
                # if not isfile(filepath_filepart):
                # 	if not filepath.startswith(BYLANGSDIR):
                # 		filepath = BYLANGSDIR + filepath
                if filepath.startswith(shorten_keys[0]) or filepath.startswith(
                    shorten_keys[1]
                ):
                    filepath = shortens[filepath[0]] + filepath[1:]

                # if not isfile(filepath):
                # 	if not filepath.startswith(BYLANGSDIR):
                # 		filepath = BYLANGSDIR + filepath
                if filepath_filepart.lower().startswith("c:"):
                    from schnell.app.stringutils import split_by_pos

                    # : pertama = C: of filepath
                    # : kedua baru filepath:baris_cari
                    pecah = split_by_pos(filepath_filepart, key_delimiter, 2)
                    # print('pecah', pecah)
                    filepath, baris_cari = pecah
                b = redis_value_recurse(
                    redis_config["r"],
                    filepath,
                    print_keys=True,
                    is_fullkey=True,
                    REPL=REPL,
                )
                if b:
                    #################
                    if wiekes:
                        b = replace_wiekes(b, wiekes)
                    #################
                    # indah3('-'*10 + ' ' + filepath_barispart, warna='red')
                    indah4(
                        "-" * 10 + " " + filepath_filepart + " | " + filepath_barispart,
                        warna="red",
                    )
                    if ULIBPY_USE_MARKDOWN_PRINTER:
                        print_copy_markdown(b)
                    else:
                        indah3(b)

            # else:
            # 	print(f'[{code}] not found, len(a)={len(a)}')


def main():
    # listen ke 'replservice_request'
    channel = redis_config["request_kanal"]
    # r = redis_connect()
    try_redis_connect()
    redis_subscribe(channel, redis_config["r"])


if __name__ == "__main__":
    main()

#
