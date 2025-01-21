from curses.ascii import isdigit
import re, requests
from bs4 import BeautifulSoup
import bs4


def get_data_logrocket(code = 'react 1'):
    so_url = 'https://blog.logrocket.com/'
    if code:
        if ' ' in code:
            tag, page = code.split()
            so_url = f'https://blog.logrocket.com/tag/{tag}/page/{page}/'
        elif code.isdigit():
            so_url = f'https://blog.logrocket.com/page/{code}/'
        else:
            so_url = f'https://blog.logrocket.com/tag/{code}/'

    # print(so_url)
    results = []
    isi = requests.get(so_url).content
    soup = BeautifulSoup(isi, 'html.parser')
    blocks = soup.findAll('div', class_='card-block')
    for idx, block in enumerate(blocks,1):
        judul = block.findAll('h2', class_='card-title') [0]
        link = judul.find('a').attrs['href']
        preview = block.findAll('span', class_='card-text') [0]
        if not isinstance(preview, str):
            preview = preview.text
        metafooter_ = block.findAll('div', class_='metafooter') [0]
        postname = metafooter_.find('span', 'post-name').text
        postdate = metafooter_.find('span', 'post-date').text
        readingtime = metafooter_.find('span', 'readingtime').text
        # print(f'{idx}.', judul.text, link, '|', preview.text, f"({postname}, {postdate}, {readingtime})", '\n')
        item = {
            'title': judul.text if not isinstance(judul, str) else judul,
            'summary': preview,
            'postname': postname,
            'postdate': postdate,
            'readingtime': readingtime,
            'url': link,
        }
        results.append(item)
    return results


# # so_url = 'https://blog.logrocket.com/page/4/'
# so_url = 'https://blog.logrocket.com/tag/nextjs/page/1/'
# # so_url = f'{prefix_url}/questions__TAG__?tab=newest&pagesize=50__PAGE__'
# # so_url = f'{prefix_url}/tag/__TAG__/page/__PAGE__/'
# isi = requests.get(so_url).content
# soup = BeautifulSoup(isi, 'html.parser')
# # blocks = soup.findAll('div', class_='col-md-7')
# blocks = soup.findAll('div', class_='card-block')
# for idx, block in enumerate(blocks,1):
#     judul = block.findAll('h2', class_='card-title') [0]
#     link = judul.find('a').attrs['href']
#     preview = block.findAll('span', class_='card-text') [0].text
    
#     metafooter_ = block.findAll('div', class_='metafooter') [0]
#     postname = metafooter_.find('span', 'post-name').text
#     postdate = metafooter_.find('span', 'post-date').text
#     readingtime = metafooter_.find('span', 'readingtime').text
    
    
#     print(f'{idx}.', judul.text, link, '|', preview.text, f"({postname}, {postdate}, {readingtime})", '\n')

# get_data_logrocket()
