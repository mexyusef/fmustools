def search_algo1(tempres, keylist):
    result = sorted(
        tempres,
        key=lambda item: len(  # utamakan nama file .mk sama dg salah satu item cari
            [
                elem
                for elem in keylist
                if elem == item.split(":")[0].split("/")[-1].removesuffix(".mk")
            ]
        )
        +  # utamakan salah satu item cari sama dengan nama baris_cari (split(:)[1])
        # yg sengaja kita sediakan agar dia ter searched
        len([elem for elem in keylist if elem == item.split(":")[1]])
        + len(  # utamakan nama file .mk dimulai dg salah satu item cari
            [
                elem
                for elem in keylist
                if item.split(":")[0]
                .split("/")[-1]
                .removesuffix(".mk")
                .startswith(elem)
            ]
        )
        + len(  # utamakan semua item cari ada di filepath
            [elem for elem in keylist if elem in item.split(":")[0]]
        )
        + len(  # utamakan nama folder berisi file .mk sama dg salah satu item cari
            [
                elem
                for elem in keylist
                if elem == item.split(":")[0].split("/")[-2].removesuffix(".mk")
            ]
        ),
        reverse=True,
    )

    return result


def search_algo2(tempres, keylist):
    return sorted(tempres)


def search_algo3(tempres, keylist):
    r"""
    /QTreeWid
    repl run() err: string index out of range
    Traceback (most recent call last):
    File "C:\Users\usef\work\sidoarjo\schnell\creator\repl.py", line 301, in run
            self.process(text)
    File "C:\Users\usef\work\sidoarjo\schnell\creator\repl.py", line 395, in process
            redis_repl(code, self)
    File "C:\Users\usef\work\sidoarjo\schnell\db\myredis.py", line 963, in redis_repl
            a = redis_keys_recurse(redis_config['r'], code, mapper=True)
    File "C:\Users\usef\work\sidoarjo\schnell\db\myredis.py", line 195, in redis_keys_recurse
            tempres = search_algo3(tempres, keylist)
    File "C:\Users\usef\work\sidoarjo\schnell\db\search.py", line 24, in search_algo3
            return sorted(tempres, key=lambda item:item.split(':', 1)[0].count('/')*100 + ord(item.split(':', 1)[0][1]))
    File "C:\Users\usef\work\sidoarjo\schnell\db\search.py", line 24, in <lambda>
            return sorted(tempres, key=lambda item:item.split(':', 1)[0].count('/')*100 + ord(item.split(':', 1)[0][1]))
    IndexError: string index out of range

    di sini ada \\ tapi gak ada /
    121. C:\Users\usef\work\sidoarjo\database\refcards\pyqt5_references.mk:QTreeWidget

    walau ini berhasil, tapi gagal "baca"
    /QTreeWid/0 <- gak berhasil baca...
    """
    try:
        return sorted(
            tempres,
            key=lambda item: item.split(":", 1)[0].count("/") * 100
            + ord(item.split(":", 1)[0][1]),
        )
    except:
        return sorted(tempres)
