# https://lokalise.com/blog/how-to-translate-languages-in-python-with-google-translate-and-deepl-plus-more/
# https://stackabuse.com/text-translation-with-google-translate-api-in-python/
# pip install googletrans
# https://github.com/ssut/py-googletrans
# https://py-googletrans.readthedocs.io/en/latest/
# pip install googletrans-py
# https://github.com/geekpradd/PyDictionary
# pip install PyDictionary
# https://github.com/nit-in/py-dictionary
# pip install Py-Dictionary

from googletrans import Translator

from pydictionary import Dictionary
# dict = Dictionary("fix")
# meanings_list = dict.meanings()
# synonyms_list = dict.synonyms()
# antonyms_list = dict.antonyms()
def kamus(text, separator='*'*10):
    jawaban = Dictionary(text)
    result = separator + ' meanings\n'
    meanings_list = jawaban.meanings()
    result += '\n'.join(meanings_list)
    result += '\n' + separator + ' synonyms\n'
    synonyms_list = jawaban.synonyms()
    result += '\n'.join(synonyms_list)
    result += '\n' + separator + ' antonyms\n'
    antonyms_list = jawaban.antonyms()
    result += '\n'.join(antonyms_list)
    return result

# gagal install
# from PyDictionary import PyDictionary
# dictionary=PyDictionary()

# >>> translator = Translator()
# >>> translator.translate('안녕하세요.')
# # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
# >>> translator.translate('안녕하세요.', dest='ja')
# # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
# >>> translator.translate('veritas lux mea', src='la')
# # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>

# >>> translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
# >>> for translation in translations:
# ...    print(translation.origin, ' -> ', translation.text)
# # The quick brown fox  ->  빠른 갈색 여우
# # jumps over  ->  이상 점프
# # the lazy dog  ->  게으른 개
translator = Translator()


#   File "C:\Users\usef\work\sidoarjo\schnell\app\translatorutils.py", line 63, in coded_translate
#     translation = translator.translate(content, src=src, dest=dest)
#                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\googletrans\client.py", line 184, in translate
#     data = self._translate(text, dest, src, kwargs)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\googletrans\client.py", line 80, in _translate
#     token = self.token_acquirer.do(text)
#             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\googletrans\gtoken.py", line 194, in do
#     self._update()
#   File "C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\googletrans\gtoken.py", line 62, in _update
#     code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'NoneType' object has no attribute 'group'

def translate(content, src='en', dest='id'):
    translation = translator.translate(content, src=src, dest=dest)
    return translation.text

def coded_translate(content):
    """
    en,id/text
    """
    langs, content = content.split('/', 1)
    src, dest = langs.split(',')
    try:
        translation = translator.translate(content, src=src, dest=dest)
        return translation.text
    except Exception as err:
        return 'Error: ' + str(err)

