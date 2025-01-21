from app.dirutils import (
	tempdir, 
	under_tempdir,
  save_file_under_tempdir,
	timestamp,
)
from app.printutils import (
  indah3,
)
from app.utils import (
  perintah, perintahsp_simple,
	PBPASTE,PBCOPY,LANGUAGES,
)


def exego(filepath=None):
  """
  ingat:
  go run *.go
  ???
  jk ada file selain main.go
  """
  if filepath is None:
    filepath = save_file_under_tempdir(f'delete_{timestamp()}.go')
    command = f"{PBPASTE} > {filepath} && go run {filepath} && rm -f {filepath}"    
  else:
    command = f"go run {filepath}"

  indah3(f'exego = {command}', warna='red')

  perintah(command)
  return 'OK'
