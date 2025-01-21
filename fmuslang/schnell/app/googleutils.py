# google docs, sheets, app-scripts, etc
from constants import GOOGLESEARCH, YOUTUBESEARCH
from startup import buka_internet
import urllib.parse


def cari_google(query, history=None):
    # query = self.text()
    print(f'[cari_google] query [{query}]')
    if history is not None and query not in history:
        history.append(query)
    # self.set_input_completer()
    # __TEXTPLACEHOLDER__ = query.replace(' ', '+')
    __TEXTPLACEHOLDER__ = urllib.parse.quote(query)
    alamat = GOOGLESEARCH.replace('__TEXTPLACEHOLDER__', __TEXTPLACEHOLDER__)
    buka_internet(alamat)


def cari_youtube(query, history=None):
    """
    https://www.youtube.com/results?search_query=react+diagram
    """
    print(f'[cari_youtube] query [{query}]')
    if history is not None and query not in history:
        history.append(query)
    __TEXTPLACEHOLDER__ = urllib.parse.quote(query)
    alamat = YOUTUBESEARCH.replace('__TEXTPLACEHOLDER__', __TEXTPLACEHOLDER__)
    buka_internet(alamat)
