import re

# print('vs1')
from schnell.app.fileutils import get_definition_by_key_permissive_start_with_lineno
from schnell.app.stringutils import tabify_content
from schnell.db.redis_config import redis_config
from schnell.db.redis_repl_search_service import redis_repl_search_service

# print('vs2')
from schnell.db.myredis_common import (
    get_connection,
    try_redis_connect,
    redis_connect,
    redis_publish,
    key_delimiter,
    shortens,
)
from schnell.db.replservice import ReplService, repl_service

# print('vs3')
from schnell.app.transpiler.lalang import process_language_wrapper as lalang

# print('vs4')
from schnell.db.llms import quick_invoke

# print('vs5')


def redis_repl_from_vscode(data):
    """
    mem-publish reply dari server ke client/vscode, prefix menentukan channel mana yg menerima reply.

    hanldePubSub
            redis_subscribe
                    message: string
                            handle internally di redis_subscribe
                    message: data
                            handle di redis_repl_from_vscode
            redis_publish

    ping => pong
    fs etc => ...
    """
    # redis_publish(f'SERVER TELAH PROSES {data}!', redis_config['from_server'])
    # data = json.loads(data)
    content = data["content"]
    metacontent = data["meta"]
    content_original = content
    content = content.lstrip()  # biar bisa ketik dari dalam indented block
    indentor = content_original.replace(content, "")
    # print('[db.myredis][redis_repl_from_vscode] content:', content)
    # print('meta:', metacontent)
    print(
        f"""[db.myredis][redis_repl_from_vscode]
	content = {content}
	metacontent = {metacontent}
	"""
    )

    # content: @/devops/selenium.mk:find/get html element by xpath and css
    # UPD: 25-05-2022, expand @ atau $ di awal ke real path
    if content.startswith("@/") or content.startswith("$/"):
        kunci = "@" if content.startswith("@/") else "$"
        content = re.sub(f"^{kunci}", shortens[kunci], content)
        # agar redis_repl_search_service (via content.startswith(/)) dengan 1 entry = melihat isi entry
        # content = '/' + content
        print(
            f"""[db.myredis][redis_repl_from_vscode] recontent @/$ to and get content from [{content}]"""
        )
        filepath, baris_cari = content.split(key_delimiter, 1)
        result, lineno = get_definition_by_key_permissive_start_with_lineno(
            filepath, baris_cari
        )
        data = {
            "content": result,
            "meta": {
                "lineno": lineno,
                "filepath": filepath,
                "baris_entry": baris_cari,
                "original": content,
            },
            "original": metacontent,
        }
        redis_publish(data, redis_config["mapper_service"])

    elif content.startswith("/"):
        # spt repl_service, dg ctrl ; atau ctrl '
        code = content.removeprefix("/").strip()
        hasil, meta = redis_repl_search_service(code)
        data = {
            "content": hasil,
            "meta": meta,
            "original": metacontent,
        }
        print(f"""[redis_repl_search_service] hasil = [{hasil}]""")
        redis_publish(data, redis_config["search_service"])

    elif content.startswith("fastmapper:"):
        # ctrl+n dari vscode

        code = content.removeprefix("fastmapper:").strip()
        hasil, meta = repl_service.fastmapper(code, meta_input=metacontent)
        data = {
            "content": hasil,
            "meta": meta,
            "original": metacontent,
        }
        redis_publish(data, redis_config["mapper_service"])

    elif content.startswith(","):
        # lalang
        # lstrip() dulu krn kadang
        # space space ,<code>

        # content = content.lstrip()
        code = content.removeprefix(",").strip()
        hasil = lalang(code)
        if len(indentor):
            hasil = tabify_content(hasil, indentor)
        data = {
            "content": hasil,
            # 'meta': meta,
            "original": metacontent,
        }
        redis_publish(data, redis_config["from_server"])

    elif content.startswith("llm-query:"):
        # llms request
        llm_query = content.removeprefix(",").strip()
        result = quick_invoke(llm_query)
        data = {
            "content": result,
            # 'meta': meta,
            "original": metacontent,
        }
        redis_publish(data, redis_config["from_server"])

    else:
        # ff, fs, fl, dll bisa jalan
        hasil, meta = repl_service.process(content, meta_input=metacontent)
        data = {
            "content": hasil,
            "meta": meta,
            "original": metacontent,
        }
        redis_publish(data, redis_config["from_server"])
