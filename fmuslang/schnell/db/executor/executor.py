# new executor berbasis app.executor
from schnell.app.utils import trypaste

from .exego import exego
from .exejava import exejava
from .exepython import exepython

class FileExecutor():

  def __init__(self):
	  pass

  def exec(self, language, filepath=None, complete_program=None):
    result = 'OK'
    if language == 'python' or language == 'py':
      result = exepython(filepath, complete_program)
    elif language == 'go':
      result = exego(filepath)
    elif language == 'java':
      result = exejava(filepath)
    elif language == 'rust':
      result = 'Not implemented yet'

    return result

file_executor = FileExecutor()
