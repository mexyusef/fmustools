from schnell.app.printutils import indah4
from schnell.app.stringutils import splitstrip, joinsplitlines, joinsplitstrip
from schnell.app.dirutils import (
    file_under_tempdir,
    under_tempdir,
    joiner,
    basename, dirname,
    is_file_not_dir,
    is_filename_not_filepath,
    is_dir_not_file)
from schnell.app.fileutils import file_write
from schnell.app.fileutils import get_definition_by_key_permissive_start
from schnell.app.fmusutils import run_fmus_for_content
from schnell.app.utils import platform
import schnell.app.ipynbutils as NB
from prompt_toolkit.shortcuts import confirm


__TEMPLATE_IMPORTS = """
import numpy as np
import cv2 as cv
import random
"""

__TEMPLATE_CV_FINAL = """
cv.waitKey(0)
cv.destroyAllWindows()
"""

__TEMPLATE_VARS = """
width = 900
height = 600
n_trees = 30
ground_level = height-100
green, light_green, brown = (40,185,40), (25,220,0), (30,65,155)
img = np.zeros((__H__, __W__, 3), dtype=np.uint8)
"""

__TEMPLATE_BG_2RECTS = """
cv.rectangle(img, (width,0), (0, ground_level), (255,225,95), -1)
cv.rectangle(img, (width, ground_level), (0, height), green, -1)
"""

__TEMPLATE_TEXT = """
font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
cv.putText(img, "__TULISAN__", (120,490), font, 1.5, (255,255,255), 2)
"""

__TEMPLATE_SUN = """
cv.circle(img, (200,150), 60, (0,255,255), -1)
cv.circle(img, (200,150), 75, (220,255,255), 10)
"""

__TEMPLATE_TREE1 = """
# *** TREE 1 ***
# tree stem
cv.line(img, (710, 500), (710, 420), (30,65,155), 15)
# tree leafs
triangle2 = np.array([[640,460],[780,460], [710,200]], dtype=np.int32)
cv.fillPoly(img, [triangle2], (75,180,70))
"""

__TEMPLATE_TREE2 = """
# *** TREE 2 ***
# tree stem
cv.line(img, (600, 500), (600, 420), (30,65,155), 25)
# tree leafs
triangle = np.array([[500,440],[700,440], [600,75]], dtype=np.int32)
cv.fillPoly(img, [triangle], (75,200,70))
"""

plotly_play = """
import pandas as pd
import numpy as np
import plotly.express as px
xdata = np.random.random(50)
ydata = np.random.random(50)
fig = px.scatter(x=xdata, y=ydata)
fig.show()
europedata2007 = px.data.gapminder().query('year==2007').query('continent=="Europe"')
print(europedata2007)
fig2 = px.scatter(europedata2007, x='lifeExp', y='gdpPercap', size='pop', color='lifeExp')
fig3 = px.scatter(europedata2007, x='lifeExp', y='gdpPercap', size='pop', color='lifeExp', hover_name='country')
fig3.show()
europedata = px.data.gapminder().query('continent=="Europe"')
print(europedata)
fig4 = px.line(europedata, x='year', y='lifeExp', color='country')
fig4.show()
px.line(europedata, x='year', y='pop', color='country')
austriadata = px.data.gapminder().query('country=="Austria"')
fig5 = px.bar(austriadata, x='year', y='pop', color='lifeExp')
fig5.show()

px.bar(austriadata, x='year', y='pop', color='gdpPercap')
px.bar(austriadata, x='year', y='gdpPercap', color='gdpPercap', color_continuous_scale='ice')
px.bar(austriadata, x='year', y='gdpPercap', color='gdpPercap', color_continuous_scale='bluered')
px.bar(austriadata, x='year', y='gdpPercap', color='gdpPercap', color_continuous_scale='bluered_r')

fig6 = px.pie(europedata, values='pop', names='country', title='Distribusi populasi eropa')
fig6.show()
"""

# ini kita split agar masing statement dlm cell sendiri
sns_play = """
# https://www.youtube.com/watch?v=ooqXQ37XHMM
import seaborn as sns
sns.get_dataset_names()
iris = sns.load_dataset('iris')
planets = sns.load_dataset('planets')
tips = sns.load_dataset('tips')
titanic = sns.load_dataset('titanic')
tips
sns.scatterplot(x='tip', y='total_bill', data=tips)
sns.scatterplot(x='tip', y='total_bill', data=tips, hue='day', size='size')
sns.scatterplot(x='tip', y='total_bill', data=tips, hue='day', size='size', palette='YlGnBu')
sns.histplot(tips['tip'], kde=True, bins=5)
sns.histplot(tips['tip'], kde=True, bins=15)
sns.histplot(tips['tip'], bins=15)
sns.histplot(tips['tip'], kde=True, bins=30)
sns.displot(tips['tip'], kde=True, bins=15)
sns.barplot(x='sex', y='tip', data=tips, palette='YlGnBu')
sns.boxplot(x='day', y='tip', data=tips, hue='sex', palette='YlGnBu')
sns.boxplot(x='day', y='total_bill', data=tips, hue='sex', palette='YlGnBu')
sns.stripplot(x='day', y='tip', data=tips, hue='sex', palette='YlGnBu', dodge=True)
sns.jointplot(x='tip', y='total_bill', data=tips)
sns.jointplot(x='tip', y='total_bill', data=tips, kind='reg')
sns.jointplot(x='tip', y='total_bill', data=tips, kind='kde')
sns.jointplot(x='tip', y='total_bill', data=tips, kind='kde', shade=True)
sns.jointplot(x='tip', y='total_bill', data=tips, kind='kde', shade=True, cmap='YlGnBu')
sns.jointplot(x='tip', y='total_bill', data=tips, kind='hex', cmap='YlGnBu')
titanic
sns.pairplot(titanic.select_dtypes(['number']), hue='pclass')
titanic.corr()
sns.heatmap(titanic.corr(), annot=True, cmap='YlGnBu')
sns.heatmap(titanic.corr(), annot=True, cmap='coolwarm')
sns.heatmap(titanic.corr(), annot=True, cmap='icefire')
iris
sns.clustermap(iris.drop('species', axis=1))
"""

# np_bg = "img = np.zeros((__H__, __W__, 3), dtype=np.uint8)"
content_map = {
    'P': __TEMPLATE_IMPORTS,
    '.': __TEMPLATE_CV_FINAL,
    '#': "cv.imshow(__TITLE__, img)",
    # 'bg': np_bg,
    '2r': __TEMPLATE_BG_2RECTS,
    't': __TEMPLATE_TEXT,
    'sun': __TEMPLATE_SUN,
    'tree1': __TEMPLATE_TREE1,
    'tree2': __TEMPLATE_TREE2,
    'V': __TEMPLATE_VARS,
    'PV': __TEMPLATE_IMPORTS + __TEMPLATE_VARS + '\n',
    '##': '\n\n' + "cv.imshow('__TITLE__', img)" + '\n' + __TEMPLATE_CV_FINAL,
    # ini perlu di add per cell
    # 'sns1': joinsplitlines(sns_play, '\n\n'),
    'sns1': '\n'.join([item.strip() for item in sns_play.splitlines() if item.strip()]),
    'plot1': '\n'.join([item.strip() for item in plotly_play.splitlines() if item.strip()]),
    # 'scolor': "green, light_green, brown = (40,185,40), (25,220,0), (30,65,155)",
}


__TEMPLATE_NOTEBOOK_FMUS = """
__LOCATION__,d
    #$* code .
    $* jupyter-notebook --port 9201
"""

temploc = '__DOLLAR__temp'
if platform() in ['win32', 'windows', 'desktop']:
    temploc = '__PRC__TEMP__PRC__'

def notebook(code, item, filename = 'notebook.py', notebookfile = 'notebook.ipynb', __PROJECTNAME__ = 'notebook', default_location=None):
    """
    contoh content:
    P/V/2r/#/.
    PV/2r/##

    PV/2r/t=selamat datang pujaanku/tree1/tree2/##

    gambar utama di 2r
    """
    nb = NB.nb_new()
    cells = []

    if not '|' in code:
        new_ipynb_name_or_workdir = item.workdir
        location = item.workdir
        contents = code
    else:
        # new_ipynb_name_or_workdir skrg digunakan sbg judul
        contents, new_ipynb_name_or_workdir = splitstrip(code, '|')
        # notebookfile = new_ipynb_name_or_workdir # sementara gak pake __PWD etc
        if is_filename_not_filepath(new_ipynb_name_or_workdir): # os.path.basename(filepath) == filepath, file tapi bukan dir, filename.ipynb
            # jk hanya berikan namafile
            # harusnya bisa gunakan item.workdir
            notebookfile = new_ipynb_name_or_workdir
            # location = f'{default_location}/__PROJECTNAME__' # harus bongkar dulu...juga PRC jadikan % dulu
            location = default_location  # /nb)import os,sys|filename.ipynb => maka tulis di item.workdir = '.'
        else: # /path/to/file
            notebookfile = basename(new_ipynb_name_or_workdir)
            location = dirname(new_ipynb_name_or_workdir)
            # expand location di sini...
    # TODO:
    # expand location...
    # new_ipynb_name_or_workdir: cek abs atau rel, jk abs, maka filepath gak usah lagi under tempdir
    # jk rel maka under temptidr tapi notebookfile disesuaikan dgnya.

    kembali = ''
    # content bisa dari fmus/mk
    if '.fmus=' in contents or '.mk=' in contents:
        fmus_filepath, barisentry = [item.strip() for item in contents.split('=', 1)]
        content = get_definition_by_key_permissive_start(fmus_filepath, barisentry)
        # utk ipynb, bikin cell utk tiap baris
        for baris in content.splitlines():
            cells.append(baris)
        # utk main.py, masukkan semua diteguk
        kembali = content
    else:
        for content in splitstrip(contents, '/'):
            # t=whatever...
            indexer = content
            if indexer in content_map and indexer in ['sns1', 'plot1']:
                # map(lambda line: cells.append(line), content_map.get(indexer, indexer).splitlines())
                for baris in content_map.get(indexer, indexer).splitlines():
                    cells.append(baris)
                    kembali += baris + '\n'
                    # print('cells adlh', cells)
                continue
            tulisan = ''
            if content.startswith('t='):
                # if '=' in content:
                indexer, tulisan = splitstrip(content, '=')
                content = content_map.get(indexer, indexer)
                if tulisan:
                    content = content.replace('__TULISAN__', tulisan)
            else:
                content = content_map.get(indexer, indexer)

            content = content.replace('__TITLE__', new_ipynb_name_or_workdir).replace('__W__', 'width').replace('__H__', 'height')
            cells.append(content)
            kembali += content + '\n' # utk main.py, perlu \n antar statement


    # indah4(f'''[app.quick.notebook]
    # notebookfile = {notebookfile}
    # location = {location}
    # cells utk notebook = {kembali}
    # ''', warna='cyan')

    NB.nb_newcells(nb, cells)

    if kembali:
        indah4(kembali, warna='white')

        # projdir = under_tempdir(__PROJECTNAME__)
        projdir = location
        # tulis main.py
        filepath = joiner(projdir, filename)
        file_write(filepath, kembali)
        # tulis main.ipynb
        notebookfilepath = joiner(projdir, notebookfile)
        NB.nb_save(notebookfilepath, nb)

        # indah4(f'''[app.quick.notebook]
        # notebookfilepath = {notebookfilepath}
        # projdir = {projdir}
        # filepath = {filepath}
        # ''', warna='magenta')

        # jalankan jupyter
        # fmuscontent = __TEMPLATE_NOTEBOOK_FMUS.replace('__LOCATION__', location)
        # fmuscontent = fmuscontent.replace('__FILENAME__', filename).replace('__PROJECTNAME__', __PROJECTNAME__)
        # run_fmus_for_content(fmuscontent)
        jalankan = confirm(f'jalankan "/ketik)jupyter-notebook --port 9201"? ')
        if jalankan:
            run_fmus_for_content(f'/ketik)jupyter-notebook --port 9201', dirpath=location)
