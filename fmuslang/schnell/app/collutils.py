def replace_key(kamus, source):
  for k,v in kamus.items():
    source = source.replace(k, v)

  return source


def sort_lines(lines):
  return '\n'.join(sorted(lines.splitlines()))


def merge_dicts_of_lists(dict1, dict2):
  """
  # 1
  dict1 = {}
  dict2 = {
    'express': [1,2,3]
  }
  ==
  dict1 = { 'express': [1,2,3] }

  #2
  dict1 = { 'express': [1,2,3] }
  dict2 = {
    'express': [4,5,6]
  }
  ==
  dict1 = {
    'express': [1,2,3,4,5,6]
  }
  """
  for k,v in dict2.items():
    if not k in dict1:
      dict1[k] = v
    else:
      dict1[k].extend(v)
  return dict1  

# https://programminghistorian.org/en/lessons/counting-frequencies
# Given a list of words, return a dictionary of
# word-frequency pairs.

def wordListToFreqDict(wordlist):
  wordfreq = [wordlist.count(p) for p in wordlist]
  return dict(list(zip(wordlist,wordfreq)))

# Sort a dictionary of word-frequency pairs in
# order of descending frequency.

def sortFreqDict(freqdict):
  aux = [(freqdict[key], key) for key in freqdict]
  aux.sort()
  aux.reverse()
  return aux


def balik(the_list):
  """
  >>> a = [1,2,3,4]
  >>> a[::-1]
  [4, 3, 2, 1]
  """
  return the_list[::-1]


def balik_list_of_pairs(the_list):
  """
  >>> a = [(1,'satu'),(2,'dua')]
  >>> a
  [(1, 'satu'), (2, 'dua')]
  >>> b = [item[::-1] for item in a]
  >>> b
  [('satu', 1), ('dua', 2)]
  >>> a
  [(1, 'satu'), (2, 'dua')]
  """
  return [item[::-1] for item in the_list]

