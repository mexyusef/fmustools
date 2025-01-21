def create_entries(code):
    """
    a=
    b=
    values_from_clipboard dari creator.declarative.handler akan handle empty vals
    """
    daftar = list(code)
    hasil = [f"{key}=" for key in daftar]
    return "\n".join(hasil)


def provide_for_clipboard(code):
    """
    a-z
    abcdef
    a-z,bcdsdg
    """
    if "," in code:
        parts = code.split(",")
        texts = []
        for p in parts:
            if "-" in p:
                q = p.split("-")
                text = [chr(i) for i in range(ord(q[0]), ord(q[1]))]
                texts.append(text)
            else:
                texts.append(p)
        res = create_entries(texts)
    elif "-" in code:
        p = code.split("-")
        text = [chr(i) for i in range(ord(p[0]), ord(p[1]))]
        res = create_entries(text)
    else:
        res = create_entries(code)

    return res
