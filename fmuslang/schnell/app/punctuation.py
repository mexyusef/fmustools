
# [
#     '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
#     '{', '[', '}', ']', '\\', '|', "'", '"', ';', ':', '<', '>', ',', '.', '/', '?',
# ]
"""
Cara kerja:
Puncture = Punctuation()
Puncture.set_handler('!', lambda lakukan: os.system(f'cd {Contiki.cwd()} && ' + lakukan))

Puncture.set_handler('/', lambda cari: system_grep(Contiki.cwd(), cari))
Puncture.set_handler('\\', lambda cari: curdir_grep(Contiki.cwd(), cari))

jk bisa cuma: # saja atau #argumen
Puncture.set_handler('@', twitter)
Puncture.set_handler('#', lambda namafile=None: edit_last_file(namafile))
Puncture.set_handler('$', lambda filepath=None: handle_ocr(filepath))  
Puncture.set_handler('^', lambda code=None: process_symbol(code))

if code and code[0] in Puncture.handled_punctuations():
  Puncture.execute(code)

"""
DEFAULT_PUNCTUATIONS = { 
  '~' : None,
  '`' : None,
  '!' : None,
  '@' : None,
  '#' : None,
  '$' : None,
  '%' : None,
  '^' : None,
  '&' : None,
  '*' : None,
  '(' : None,
  ')' : None,
  '-' : None,
  '_' : None,
  '+' : None,
  '=' : None,
  '{' : None, 
  '[' : None,
  '}' : None, 
  ']' : None,
  '\\' : None,
  '|' : None,
  "'" : None,

  # " spt |, tapi jk | hanya bisa | dan |50, " bisa " dan "50 dan "50 kata1 kata2 kata3
  # contoh "1000 sucor
  '"' : None,

  ';' : None,
  ':' : None,
  '<' : None,
  '>' : None,
  ',' : None,
  '.' : None,
  '/' : None,
  '?' : None,
}

class Punctuation():
  def __init__(self, *args, **kwargs):
    # self.Herstory = None
    # if 'history' in kwargs:
    #   self.Herstory = kwargs['history']
    self.PUNCTUATIONS_DICTS = DEFAULT_PUNCTUATIONS
    self.PUNCTUATIONS = list(self.PUNCTUATIONS_DICTS.keys())

    # misal Punctuation(1), Punctuation(1,2,3), Punctuation(24,42) dst
    if args:      
      # print('Punctuation args')
      for item in args:
        # print('Punctuation args', item)
        if isinstance(item, int):          
          self.PUNCTUATIONS += [str(item)]
          self.PUNCTUATIONS_DICTS.update({ str(item): None, })
    if kwargs:
      for k,v in kwargs.items():
        if k in self.PUNCTUATIONS:
          self.PUNCTUATIONS_DICTS[k] = v

  def handler(self, punc):
    if punc in self.PUNCTUATIONS and self.PUNCTUATIONS_DICTS[punc]:
      return self.PUNCTUATIONS_DICTS[punc]

  def set_handler(self, punc, handler):
    if punc in self.PUNCTUATIONS:
      self.PUNCTUATIONS_DICTS[punc] = handler

  def handled_punctuations(self):
    return [punc for punc in self.PUNCTUATIONS if self.PUNCTUATIONS_DICTS[punc]]

  # def set_history(self, history):
  #   self.Herstory = history

  def execute(self, code):
    """
    ada kasus begini:
    @
    @case
    @data
    @case dan @data jadi dihandle oleh @
    """
    punc = code[0]
    arg = None
    # print(f"executor for: {punc}.")    
    if len(code) > 1:
      arg = code[1:].strip()
    if self.PUNCTUATIONS_DICTS[punc]:
      if arg:
        self.PUNCTUATIONS_DICTS[punc] (arg)
      else:
        self.PUNCTUATIONS_DICTS[punc] ()
