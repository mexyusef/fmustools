# app.httputils
import requests
from lxml import html
from lxml import etree


def req_content(alamat):
  return requests.get(alamat).content
rq = req_content

def doc_from_string(content):
  return html.fromstring(content)
docs = doc_from_string

def doc_from_url(alamat):
  return doc_from_string(req_content(alamat))
docu = doc_from_url

def xp_from_doc(doc, pattern):
  """
  kembalian selalu list
  """
  return doc.xpath(pattern)

xpd = xp_from_doc

def css_from_doc(doc, pattern):
  """
  kembalian selalu list
  """
  return doc.cssselect(pattern)
cssd = css_from_doc

class FakeResult:  
  def __init__(self, text):
    self.text = text

def xp_first(doc, pattern):
  result = FakeResult
  try:
    result = doc.xpath(pattern) [0]
  except Exception as err:
    errmsg = f'err doc.xpath {pattern}: {err}'
    print(errmsg)
    result.text = errmsg
    return result

  return result

xp1 = xp_first

def xp_first_text(doc, pattern):
  return doc.xpath(pattern) [0].text

xp1txt = xp_first_text

def css_first(doc, pattern):
  return doc.cssselect(pattern) [0]
css1 = css_first

def css_first_text(doc, pattern):
  return doc.cssselect(pattern) [0].text
css1txt = css_first_text

def doc_elem_byid(doc, id):
  """
  kembalikan list
  doc di sini adlh root element
  jadi bisa element div, dll, gak perlu hrs html.fromstring
  """
  return doc.get_element_by_id(id)


def doc_elem_bycls(doc, cls):
  """
  kembalikan list
  """
  return doc.find_class(cls)
