import re, requests
from bs4 import BeautifulSoup
import bs4


def get_data_devto(code = 'python 1'):
    original_so_url = 'https://dev.to/'
    so_url = original_so_url
    if code:
        if ' ' in code:
            tag, page = code.split()
            so_url = f'https://dev.to/t/{tag}/page/{page}'
        elif code.isdigit():
            so_url = f'https://dev.to/page/{code}'
        else:
            so_url = f'https://dev.to/t/{code}'

    # print(so_url)
    results = []
    isi = requests.get(so_url).content
    soup = BeautifulSoup(isi, 'html.parser')
    blocks = soup.findAll('div', class_='crayons-story__body')
    for idx, block in enumerate(blocks,1):
        author = block.find('a', class_='crayons-story__secondary').text.strip()
        postdate = block.find('a', class_='crayons-story__tertiary').text.strip()
        tags = block.find('div', class_='crayons-story__tags').text.strip().replace('\n', ', ')
        judul_link = block.find('div', class_='crayons-story__indention')
        a_link = judul_link.find('a')
        judul = a_link.text.strip()
        link = a_link.attrs['href']
        link = original_so_url.removesuffix('/') + link if not link.startswith(original_so_url) else link
        find_comments = block.find('div', class_='crayons-story__details')
        reaction_comment = find_comments.findAll('a')
        if len(reaction_comment) == 2:
            reaction = reaction_comment [0].text.strip().removeprefix('Reactions').strip()
            comment = reaction_comment [1].text.strip().removeprefix('Comments').strip()
        else:
            comment = reaction_comment [0].text.strip().removeprefix('Comments').strip()
        find_readingtime = block.find('div', class_='crayons-story__save').find('small').text.strip()
        # print(f'{idx}. {author}, {postdate}, [{tags}], {judul}, {link}, reaksi = [{reaction}], komentar = [{comment}], readingtime = [{find_readingtime}]')
        item = {
            'title': judul,
            'summary': f"{comment}, {reaction}, [{tags}]",
            'postname': author,
            'postdate': postdate,
            'readingtime': find_readingtime,
            'url': link,
            'commenturl': link + '#comments',
        }
        results.append(item)
    return results

