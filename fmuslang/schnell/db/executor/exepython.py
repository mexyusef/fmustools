from schnell.app.dirutils import (
	tempdir, 
	under_tempdir, 
  save_file_under_tempdir,
	timestamp,
)
from schnell.app.fileutils import (
  file_write,
)
from schnell.app.printutils import (
  indah3,
)
from schnell.app.utils import (
  perintah, perintahsp_simple,
	PBPASTE,PBCOPY,LANGUAGES,
)


def exepython(filepath=None, complete_program=None):
  if filepath is None:
    filepath = save_file_under_tempdir(f'delete_{timestamp()}.py')
    if complete_program is None:      
      command = f"{PBPASTE} > {filepath} && python {filepath} && rm -f {filepath}"
    else:
      file_write(filepath, complete_program)
      command = f"python {filepath} && rm -f {filepath}"
  else:
    command = f"python {filepath}"

  indah3(f'exepython = {command}', warna='red')

  perintah(command)
  return 'OK'
