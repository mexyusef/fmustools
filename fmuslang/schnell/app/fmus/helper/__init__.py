from .constants import InsertReplace
from schnell.app.stringutils import sanitize_chars
from schnell.app.dirutils import bongkar


def decode_filename(filename):
    """
    from schnell.app.fmus.helper import decode_filename
    from .helper import decode_filename
    namafile = decode_filename(namafile)

	src,d(/mk)
		__AT__core,d(/mk)
        menjadi
        @core,d(/mk)

    # kita kasih __AT__ utk @ krn bentrok dg pesan-instruksi

    digunakan di processor:514
        elif tree.data == 'filename':
    """
    # return filename.replace('__AT__', '@').replace('__AT', '@')
    first = sanitize_chars(filename)
    # jangan lupa utk "bongkar"
    second = bongkar(first)
    return second

