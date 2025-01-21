from schnell.app.dirutils import isfile
from schnell.app.mediautils import lihat_gambar
from schnell.app.printutils import indah3, indah4
from schnell.app.utils import env_expand
from .ocr import capture_to_text
from .config import autolib_config

# set_credentials()

def auto_process(code, service_mode=False):
  """
  jk digunakan dlm service_mode
  return result, meta
  """

  # if autolib_config['creds'] is None:
  #   set_credentials()
  #   indah3(f'Credentials set to ' + get_credentials(), warna='red')
  # else:
  #   indah3('Ready to auto', warna='white')

  if code == 'ocr':
    '''
    dari vscode
    *@ocr
    '''
    text, output = capture_to_text()
    if service_mode:
      return text, output
    indah4('='*40 + ' ' + output, warna='green')
    indah3(text, warna='white')
    # trycopy(text)
    indah4('='*40, warna='green')

  elif code .startswith('s:'):
    '''
    dari vscode
    *@s:filepath
    '''
    filepath = code.removeprefix('s:').strip()
    filepath = env_expand(filepath, bongkarin=True)
    if isfile(filepath):
      lihat_gambar(filepath)

  else:
    indah4(f'command [{code}] not recognized', warna='red')

  return None, None
