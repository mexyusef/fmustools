from schnell.app.dirutils import tempdir
from schnell.app.notifutils import notify
from schnell.app.quick import handle_publish_to_redis
from schnell.app.utils import env_int
from schnell.db.replservice import repl_service
from database.langnew import programming_languages, starts_with_programming_language
from .processor import process
from .generator import generate


handled_by_replservice = [
  '/',
  '`',
  # ',<', # csslang dari editor
  'f12',
]


def replify_check_language(text, workdir, language_to_choose='py'):
  """
  filename.scala,f(cg[scala]=__FILE__=baris_entry)
  isi = replify(konten, item.workdir, language_to_choose=programming_languages)
  """
  # print('[creator.repl_language.replify][replify]:', text)
  if env_int('ULIBPY_FMUS_DEBUG')>1:
    print('[creator.repl_language.replify][replify]:', text)
  # update 10 dec 22
  if any([item for item in handled_by_replservice if text.startswith(item)]):
    answer, _ = repl_service.process(text)
    return answer
  
  prefixlang, language = starts_with_programming_language(text)
  if prefixlang:
    language_to_choose = language
    text = text.removeprefix(language + '/').strip()

  pohon = process(text, current_workdir=workdir, langchoice=language_to_choose)
  hasil = generate(pohon, language_to_choose)
  return hasil


def replify(text, workdir, language_to_choose='py'):
  """
  filename.scala,f(cg[scala]=__FILE__=baris_entry)
  isi = replify(konten, item.workdir, language_to_choose=programming_languages)
  """
  # print('[creator.repl_language.replify][replify]:', text)
  if env_int('ULIBPY_FMUS_DEBUG')>1:
    print('[creator.repl_language.replify][replify]:', text)
  # update 10 dec 22
  if any([item for item in handled_by_replservice if text.startswith(item)]):
    answer, _ = repl_service.process(text)
    return answer

  pohon = process(text, current_workdir=workdir, langchoice=language_to_choose)
  hasil = generate(pohon, language_to_choose)
  return hasil


def quick_replify(request, lang='py', workdir=tempdir()):
  """
  memanggil replify di atas
    + handle_publish_to_redis
    + notify
  """
  # lang = 'py'
  # jk /R)py/ tapi bukan /R)/... yg minta cari
  if env_int('ULIBPY_FMUS_DEBUG')>1:
    print(f"""[creator.repl_language.replify][quick_replify]
    request = {request}
    dir = {workdir}
    """)
  if '/' in request and not request.startswith('/'):
    _lang, _request = request.split('/')
    if _lang in programming_languages:
      lang = _lang
      request = _request
  hasil = replify(request, workdir, lang)
  handle_publish_to_redis(hasil)
  title = request
  body = f'Running [{request[:80]}]'
  notify(title, body, duration=3)
