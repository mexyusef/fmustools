import requests
from schnell.app.printutils import indah, indah0, indah3, indah4


# elif oper .startswith ('url_file'):
def url_file(oper, item, self_debug):
  source = oper.split('=') [1]

  self_debug('get image file dari', source)
  response = requests.get(source)
  if (response.content):
    with open(item.workdir, 'wb') as fd:
      fd.write(response.content)

  indah0(f"[url_file] File {source} sudah ditulis ke {item.workdir}...", warna='green', layar='black')
  # input(f"")

  # data = ''
  # binary_mode = '' if not hasattr(item, 'binary_mode') else 'b'
  # with open(source, 'r'+binary_mode) as fd:
  #   data = fd.read()
  # if data:
  #   with open(item.workdir, 'w'+binary_mode) as fd:
  #     fd.write(data)
  # debug(os.listdir(os.path.dirname(item.workdir))) # workdir adlh file
