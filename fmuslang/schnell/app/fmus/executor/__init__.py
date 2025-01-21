import subprocess as sp


def handle_bash(code):
  """
  sementara baru bisa handle bash
  """
  return sp.Popen(code, shell=True, stdout=sp.PIPE).stdout.read().decode('utf-8').strip()


def handle_py(code):
  """
  agak membingungkan gimana proses python
  """
  pass
