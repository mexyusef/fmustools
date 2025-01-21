# oprek notebook file, terutama dipake utk data science
# https://nbformat.readthedocs.io/en/latest/api.html
# https://github.com/jupyter/nbformat
# pip install nbformat
# pip install ipynbname
import os
import nbformat
from nbformat import v4 as nbf


def sample0(filename='generated.ipynb'):

    nb = nbf.new_notebook()

    cells = [
        nbf.new_code_cell(f"""print("Doing the thing: {i}")""")
        for i in range(10)
    ]

    cells.append('''
    get_ipython().run_cell_magic(u'HTML', u'', u'<font color=blue>heffffo</font>')
    ''')

    nb.cells.extend(cells)

    with open(filename, 'w', encoding='utf8') as f:
        nbformat.write(nb, f)


def sample1(filename='generated_notebook.ipynb', content='print("ayo dong masuk, ini programmatically oprek gitu loh")'):    
    filepath =  os.path.join(os.path.abspath(''), filename)
    print(filepath)
    thenotebook = nbformat.read(filepath, as_version=4)
    nb_newcell(thenotebook, content)
    with open(filepath, 'w', encoding='utf8') as f:
        nbformat.write(thenotebook, f)


def nb_newcells(nb, contents):
    cells = [nbf.new_code_cell(content) for content in contents]
    nb.cells.extend(cells)


def nb_newcell(nb, content):
    cell = nbf.new_code_cell(content)
    nb.cells.append(cell)


def nb_new(cells=[]):
    nb = nbf.new_notebook()
    if cells:
        nb.cells.extend(cells)
    return nb


def nb_open(filepath):
    nb = nbformat.read(filepath, as_version=4)
    return nb


def nb_write(filepath, notebook):
    with open(filepath, 'w', encoding='utf8') as fd:
        nbformat.write(notebook, fd)


def nb_save(filepath, notebook):
    nb_write(filepath, notebook)

