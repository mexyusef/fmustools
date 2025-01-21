import re, requests
from bs4 import BeautifulSoup
import bs4


def get_data_medium(code = 'programming'):
    # original_so_url = 'https://dev.to/'
    # so_url = original_so_url

    base_url = 'https://medium.com'
    so_url = 'https://medium.com/tag/programming'
    if code:
        so_url = f'https://medium.com/tag/{code}'

    # print(so_url)
    results = [
        {
            'title': 'homepage',
            'summary': '', 'postname': '', 'postdate': '', 'readingtime': '',
            'url': 'https://medium.com',
        },
        {
            'title': 'programming',
            'summary': '', 'postname': '', 'postdate': '', 'readingtime': '',
            'url': 'https://medium.com/tag/programming',
        },
        {
            'title': 'javascript',
            'summary': '', 'postname': '', 'postdate': '', 'readingtime': '',
            'url': 'https://medium.com/tag/javascript',
        },
        {
            'title': 'python',
            'summary': '', 'postname': '', 'postdate': '', 'readingtime': '',
            'url': 'https://medium.com/tag/python',
        },
        {
            'title': 'data science',
            'summary': '', 'postname': '', 'postdate': '', 'readingtime': '',
            'url': 'https://medium.com/tag/data-science',
        },
        {
            'title': 'machine learning',
            'summary': '', 'postname': '', 'postdate': '', 'readingtime': '',
            'url': 'https://medium.com/tag/machine-learning',
        },
        {
            'title': 'AI',
            'summary': '', 'postname': '', 'postdate': '', 'readingtime': '',
            'url': 'https://medium.com/tag/artificial-intelligence',
        },
        {
            'title': 'software engineering',
            'summary': '', 'postname': '', 'postdate': '', 'readingtime': '',
            'url': 'https://medium.com/tag/software-engineering',
        },
    ]
    isi = requests.get(so_url).content
    soup = BeautifulSoup(isi, 'html.parser')
    blocks = soup.findAll('article', class_='meteredContent')
    for idx, block in enumerate(blocks,1):
        first_a_is_author = block.find('a', class_='au av aw ax ay az ba bb bc bd be bf bg bh bi').text.strip()
        #au av aw ax ay az ba bb bc bd be bf bg bh bi
        #kz l
        kzl_berisi_judul_dan_link = block.find('div', class_='kz l')
        link = ''
        if kzl_berisi_judul_dan_link:
            link = kzl_berisi_judul_dan_link.find('a', class_='au av aw ax ay az ba bb bc bd be bf bg bh bi').attrs['href']            
        link = base_url + link
        judul = kzl_berisi_judul_dan_link.find('h2', class_='bn gi ll lm ln lo gm lp lq lr ls gq lt lu lv lw gu lx ly lz ma gy mb mc md me hc fm hd he hg hh gg').text.strip()
        # postdate = block.find('p', class_='bn b bo bp co').text.strip()
        # waktu = block.find('div', class_='ao o').text.strip()
        waktos = block.find('div', class_='l fv')
        waktos2 = waktos.find('p', class_='bn b bo bp co').text.strip()
        meta = block.find('div', class_='mi mj mk ml mm l')
        if meta:
            meta = meta.text.strip()
        else:
            meta = ''
        preview = block.find('p', class_='mf b dn do fm mg hd he mh hg hh jy gg')
        if preview:
            preview = preview.text.strip()
        else:
            preview = ''
    #     print(f"{idx}. {first_a_is_author} at [{waktos2} | {postdate} | {waktu}], {judul}, {link}, {preview}, meta => {meta}")
        # print(f"{idx}. {first_a_is_author} at [{waktos2}], {judul}, {link}, {preview}, meta => {meta}")
        item = {
            'title': judul,
            'summary': preview,
            'postname': first_a_is_author,
            'postdate': waktos2,
            'readingtime': meta,
            'url': link,
        }
        results.append(item)
    return results

