import re, requests
from bs4 import BeautifulSoup
import bs4


def get_data_stackoverflow(prefix_url = 'https://stackoverflow.com', code = 'python 1'):
    """
    qt.so 2
    qt.so python 5
    qt.so rust
    """
    default_parser = 'html.parser'
    so_url = f'{prefix_url}/questions__TAG__?tab=newest&pagesize=50__PAGE__'
    # tag_tpl = '/tagged/python'
    # page_tpl = '&page=5'
    m = re.match(r'([A-Za-z]+)?\s*(\d+)?', code).groups()
    # (None, '9')
    # ('rust ', '9')
    # ('rust', None)
    if m[0] or m[1]:
        if m[0]:
            so_url = so_url.replace('__TAG__', '/tagged/'+m[0])
        else:
            so_url = so_url.replace('__TAG__', '')
        if m[1]:
            so_url = so_url.replace('__PAGE__', '&page='+m[1])
        else:
            so_url = so_url.replace('__PAGE__', '')
    else:
        so_url = so_url.replace('__TAG__', '')
        so_url = so_url.replace('__PAGE__', '')

    isi = requests.get(so_url).content
    soup = BeautifulSoup(isi, default_parser)
    doctype, html = [item for item in list(soup.children) if type(item) is not bs4.element.NavigableString]
    head, body = [item for item in list(html.children) if type(item) is not bs4.element.NavigableString]

    # question_links = body.findAll('a', class_='s-link')
    # question_links = [item for item in question_links if item.attrs['href'].startswith('/questions/')]
    # satu = [item.text for item in question_links]
    # dua = [prefix_url+item.attrs['href'] for item in question_links]
    # return [{'title': a, 'url': b} for (a,b) in zip(satu,dua)]
    results = []
    blocks = body.findAll('div', class_='s-post-summary')
    for block in blocks:
        stat_links = block.findAll('div', class_='s-post-summary--stats')[0]
        question_links = block.findAll('div', class_='s-post-summary--content')[0]
        stat = stat_links.findAll('div', class_='s-post-summary--stats-item')[1]
        stat = stat.find('span')
        answers = stat.text
        q_link = question_links.find('a')
        text = q_link.text
        url = prefix_url+q_link.attrs['href']
        d_sum = question_links.findAll('div', class_='s-post-summary--content-excerpt')[0]
        summary = d_sum.text.strip()
        tags = question_links.findAll('div', class_='s-post-summary--meta-tags')[0]
        tags_ref = tags.findAll('a')
        tags = ', '.join([a.text for a in tags_ref])

        item = {
            'title': text,
            'url': url,
            'summary': summary,
            'answers': answers,
            'tags': tags,
        }
        results.append(item)
    return results

