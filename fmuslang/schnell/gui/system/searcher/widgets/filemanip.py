
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# panggil langsung fungsi...
import os, sys
envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
from dotenv import load_dotenv
load_dotenv(envfile)
schnelldir = os.environ['ULIBPY_BASEDIR']
sidoarjodir = os.environ['ULIBPY_ROOTDIR']
sys.path.extend([sidoarjodir, schnelldir])

from schnell.app.quick.fileops import fileops
# fileops(request, root_tree=None, item=None, self_run_configuration_replacer=None)
# rencana...provide menu...
from schnell.app.fileutils import (
	against_regex,
    append_file_by_linenumber,
    comment_file,
    comment_file_by_linenumber,	
    comment_file_by_prefix,
    create_if_empty_file,
	dedent_file,
    dedent_file_by_pattern,
    file_content,
    get_definition_by_key_permissive_start,
    indent_file,
    indent_file_by_pattern,
    insert_after,
    insert_after_then_tabify,
    insert_at,
	insert_before,    
    insert_before_then_tabify,
    join_lines,
    join_lines_by_prefix,
    remove_lines_by_no,
    remove_lines_by_prefix,
    remove_prefix_by_regex,
    remove_prefix_by_lineno_and_regex,
    replace_between,
    replace_file_content,
    replace_from,
    replace_line_by_no,
    replace_string_in_file,
    replace_until,
    sort_lines,
    space_to_tab_start,
    tab_to_space_start,
    uncomment_file,
)


def filemanip(filePath, parent, prefix_menu=None, prefix_action=None):
    filemanip_menu = QMenu('File manipulation', parent)

    if prefix_menu:
        filemanip_menu.addMenu(prefix_menu)
    if prefix_action:
        filemanip_menu.addAction(prefix_action)

    # replace string in file
    # replace_string_menu = QMenu('Replace string in file')
    replace_string_in_file_widget = QWidget(filemanip_menu)
    replace_string_in_file_widget_layout = QHBoxLayout(replace_string_in_file_widget)
    # old_string = QLineEdit(replace_string_in_file_widget)
    old_string = QLineEdit()
    # new_string = QLineEdit(replace_string_in_file_widget)
    new_string = QLineEdit()
    # replace_string_button = QPushButton('Replace string', replace_string_in_file_widget)
    replace_string_button = QPushButton('Replace string')
    # QWidget::setTabOrder: 'first' and 'second' must be in the same window
    # replace_string_in_file_widget.setTabOrder(old_string, new_string)
    # replace_string_in_file_widget.setTabOrder(new_string, replace_string_button)
    replace_string_in_file_widget.setFocusProxy(old_string)
    replace_string_in_file_widget_layout.addWidget(QLabel('Old string:'))
    replace_string_in_file_widget_layout.addWidget(old_string)
    replace_string_in_file_widget_layout.addWidget(QLabel('New string:'))
    replace_string_in_file_widget_layout.addWidget(new_string)
    replace_string_in_file_widget_layout.addWidget(replace_string_button)
    def callback_for_replace_string_in_file():
        oldstring = old_string.text().strip()
        newstring = new_string.text().strip()
        if oldstring and newstring and filePath:
            status = replace_string_in_file(filePath, oldstring, newstring)
            print(f'berhasil ganti "{oldstring}" menjadi "{newstring}" di {filePath}. status = {status}')
            # parent.hide() # coba menu context tutup
            filemanip_menu.hide() # biar bisa akses menu lainnya (peek dsb)
    replace_string_button.clicked.connect(callback_for_replace_string_in_file)
    replace_string_action = QWidgetAction(filemanip_menu)
    replace_string_action.setDefaultWidget(replace_string_in_file_widget)
    filemanip_menu.addAction(replace_string_action)
    # replace_string_menu.addAction(replace_string_action)
    # filemanip_menu.addMenu(replace_string_menu)

    filemanip_menu.addSeparator()

    # replace line in file by lineno
    # replace_line_menu = QMenu('Replace line in file')
    replace_line_in_file_widget = QWidget(filemanip_menu)
    replace_line_in_file_widget_layout = QHBoxLayout(replace_line_in_file_widget)
    replace_line_line_no = QSpinBox()
    replace_line_line_no.setRange(1,1000) # sementara max file line no 1000 dulu
    replace_line_line_no.setValue(1)
    replace_line_content = QLineEdit()
    replace_line_button = QPushButton('Replace line')
    replace_line_in_file_widget_layout.addWidget(QLabel('Line no:'))
    replace_line_in_file_widget_layout.addWidget(replace_line_line_no)
    replace_line_in_file_widget_layout.addWidget(QLabel('New content:'))
    replace_line_in_file_widget_layout.addWidget(replace_line_content)
    replace_line_in_file_widget_layout.addWidget(replace_line_button)
    def callback_for_replace_line_in_file():
        lineno = replace_line_line_no.value() - 1 # dikurang 1
        linecontent = replace_line_content.text() # .strip()
        if lineno and linecontent and filePath:
            replace_line_by_no(filePath, lineno, linecontent)
            print(f'berhasil ganti baris "{lineno}" dengan "{linecontent}" di {filePath}.')
            # parent.hide() # coba menu context tutup
            filemanip_menu.hide() # biar bisa akses menu lainnya (peek dsb)
    replace_line_button.clicked.connect(callback_for_replace_line_in_file)
    replace_line_action = QWidgetAction(filemanip_menu)
    replace_line_action.setDefaultWidget(replace_line_in_file_widget)
    filemanip_menu.addAction(replace_line_action)
    # replace_line_menu.addAction(replace_line_action)
    # filemanip_menu.addMenu(replace_line_menu)

    filemanip_menu.addSeparator()

    # urut baris
    # sort_lines_menu = QMenu('Sort lines in file')
    sort_lines_in_file_widget = QWidget(filemanip_menu)
    sort_lines_in_file_widget_layout = QHBoxLayout(sort_lines_in_file_widget)
    line_start = QSpinBox()
    line_start.setRange(1,1000) # sementara max file line no 1000 dulu
    line_start.setValue(1)
    line_end = QSpinBox()
    line_end.setRange(1,1000) # sementara max file line no 1000 dulu
    line_end.setValue(1)
    sort_line_button = QPushButton('Sort lines')
    sort_lines_in_file_widget_layout.addWidget(QLabel('Line no:'))
    sort_lines_in_file_widget_layout.addWidget(line_start)
    sort_lines_in_file_widget_layout.addWidget(QLabel('New content:'))
    sort_lines_in_file_widget_layout.addWidget(line_end)
    sort_lines_in_file_widget_layout.addWidget(sort_line_button)
    def callback_for_sort_lines_in_file():
        line_start_no = line_start.value() - 1 # dikurang 1
        line_end_no = line_end.value() - 1
        if line_start_no and line_end_no and (line_start_no<line_end_no) and filePath:
            sort_lines(filePath, line_start_no, line_end_no)
            print(f'berhasil urut baris "{line_start_no}" sampai "{line_end_no}" di {filePath}.')
            # parent.hide() # coba menu context tutup
            filemanip_menu.hide() # biar bisa akses menu lainnya (peek dsb)
    sort_line_button.clicked.connect(callback_for_sort_lines_in_file)
    sort_lines_action = QWidgetAction(filemanip_menu)
    sort_lines_action.setDefaultWidget(sort_lines_in_file_widget)
    filemanip_menu.addAction(sort_lines_action)
    # sort_lines_menu.addAction(sort_lines_action)
    # filemanip_menu.addMenu(sort_lines_menu)

    filemanip_menu.addSeparator()

    # tab to space, bisa pilih 2 atau 4
    # tab2space_menu = QMenu('Tab to space file')
    tab2space_in_file_widget = QWidget(filemanip_menu)
    tab2space_in_file_widget_layout = QHBoxLayout(tab2space_in_file_widget)
    number_of_space = QComboBox(filemanip_menu)
    number_of_space.addItems(['2','4'])
    tab2space_button = QPushButton('Tab to space')
    tab2space_in_file_widget_layout.addWidget(QLabel('No of space:'))
    tab2space_in_file_widget_layout.addWidget(number_of_space)
    tab2space_in_file_widget_layout.addWidget(tab2space_button)
    def callback_for_tab2space_in_file():
        jumlah_tab = int(number_of_space.currentText())
        if jumlah_tab and filePath:
            tab_to_space_start(filePath, jumlah_tab)
            print(f'tab to "{jumlah_tab}" spaces di {filePath}.')
            # parent.hide() # coba menu context tutup
            filemanip_menu.hide() # biar bisa akses menu lainnya (peek dsb)
    tab2space_button.clicked.connect(callback_for_tab2space_in_file)
    tab2space_action = QWidgetAction(filemanip_menu)
    tab2space_action.setDefaultWidget(tab2space_in_file_widget)
    filemanip_menu.addAction(tab2space_action)
    # tab2space_menu.addAction(tab2space_action)
    # filemanip_menu.addMenu(tab2space_menu)

    filemanip_menu.addSeparator()

    # space to tab
    # space2tab_menu = QMenu('Space to tab file')
    space2tab_in_file_widget = QWidget(filemanip_menu)
    space2tab_in_file_widget_layout = QHBoxLayout(space2tab_in_file_widget)
    number_of_space2 = QComboBox(filemanip_menu)
    number_of_space2.addItems(['2','4'])
    space2tab_button = QPushButton('Space to tab')
    space2tab_in_file_widget_layout.addWidget(QLabel('No of space:'))
    space2tab_in_file_widget_layout.addWidget(number_of_space2)
    space2tab_in_file_widget_layout.addWidget(space2tab_button)
    def callback_for_space2tab_in_file():
        jumlah_tab = int(number_of_space2.currentText())
        if jumlah_tab and filePath:
            space_to_tab_start(filePath, jumlah_tab)
            print(f'space"{jumlah_tab}" to tab di {filePath}.')
            # parent.hide() # coba menu context tutup
            filemanip_menu.hide() # biar bisa akses menu lainnya (peek dsb)
    space2tab_button.clicked.connect(callback_for_space2tab_in_file)
    space2tab_action = QWidgetAction(filemanip_menu)
    space2tab_action.setDefaultWidget(space2tab_in_file_widget)
    filemanip_menu.addAction(space2tab_action)
    # space2tab_menu.addAction(space2tab_action)
    # filemanip_menu.addMenu(space2tab_menu)

    filemanip_menu.addSeparator()

    # insert at
    # insert_at_menu = QMenu('Insert at line in# file')
    insert_at_in_file_widget = QWidget(filemanip_menu)
    insert_at_in_file_widget_layout = QHBoxLayout(insert_at_in_file_widget)
    insert_at_line = QSpinBox()
    insert_at_line.setRange(1,1000) # sementara max file line no 1000 dulu
    insert_at_line.setValue(1)
    insert_at_content = QPlainTextEdit()
    # insert_at_content.setMaximumBlockCount(3)
    insert_at_content.setFixedHeight(48)
    insert_at_button = QPushButton('Insert at')
    insert_at_in_file_widget_layout.addWidget(QLabel('Line no:'))
    insert_at_in_file_widget_layout.addWidget(insert_at_line)
    insert_at_in_file_widget_layout.addWidget(QLabel('Content to insert:'))
    insert_at_in_file_widget_layout.addWidget(insert_at_content)
    insert_at_in_file_widget_layout.addWidget(insert_at_button)
    def callback_for_insert_at_in_file():
        lineno = insert_at_line.value() - 1
        content = insert_at_content.toPlainText() # + '\n'  # force add newline
        if content and filePath:
            insert_at(filePath, lineno, content)
            print(f'insert [{content}] at {lineno} in {filePath}.')
            # parent.hide() # coba menu context tutup
            filemanip_menu.hide() # biar bisa akses menu lainnya (peek dsb)
    insert_at_button.clicked.connect(callback_for_insert_at_in_file)
    insert_at_action = QWidgetAction(filemanip_menu)
    insert_at_action.setDefaultWidget(insert_at_in_file_widget)
    filemanip_menu.addAction(insert_at_action)
    # insert_at_menu.addAction(insert_at_action)
    # filemanip_menu.addMenu(insert_at_menu)

    filemanip_menu.addSeparator()

    # insert after
    insert_after_in_file_widget = QWidget(filemanip_menu)
    insert_after_in_file_widget_layout = QHBoxLayout(insert_after_in_file_widget)
    pola_cari_edit = QLineEdit()
    insert_after_content = QPlainTextEdit()
    # insert_after_content.setMaximumBlockCount(3)
    insert_after_content.setFixedHeight(48)
    insert_after_button = QPushButton('Insert after')
    insert_after_in_file_widget_layout.addWidget(QLabel('Pattern to search:'))
    insert_after_in_file_widget_layout.addWidget(pola_cari_edit)
    insert_after_in_file_widget_layout.addWidget(QLabel('Content to insert:'))
    insert_after_in_file_widget_layout.addWidget(insert_after_content)
    insert_after_in_file_widget_layout.addWidget(insert_after_button)
    def callback_for_insert_after_in_file():
        pola_cari = pola_cari_edit.text()  #.strip()
        content = insert_after_content.toPlainText() + '\n' # .strip()
        if content and filePath:
            insert_after(filePath, pola_cari, content)
            print(f'insert [{content}] at {pola_cari} in {filePath}.')
            # parent.hide() # coba menu context tutup
            filemanip_menu.hide() # biar bisa akses menu lainnya (peek dsb)
    insert_after_button.clicked.connect(callback_for_insert_after_in_file)
    insert_after_action = QWidgetAction(filemanip_menu)
    insert_after_action.setDefaultWidget(insert_after_in_file_widget)
    filemanip_menu.addAction(insert_after_action)

    filemanip_menu.addSeparator()

    # insert before
    insert_before_in_file_widget = QWidget(filemanip_menu)
    insert_before_in_file_widget_layout = QHBoxLayout(insert_before_in_file_widget)
    pola_cari_edit2 = QLineEdit()
    insert_before_content = QPlainTextEdit()
    # insert_before_content.setMaximumBlockCount(3)
    insert_before_content.setFixedHeight(48)
    insert_before_button = QPushButton('Insert before')
    insert_before_in_file_widget_layout.addWidget(QLabel('Pattern to search:'))
    insert_before_in_file_widget_layout.addWidget(pola_cari_edit2)
    insert_before_in_file_widget_layout.addWidget(QLabel('Content to insert:'))
    insert_before_in_file_widget_layout.addWidget(insert_before_content)
    insert_before_in_file_widget_layout.addWidget(insert_before_button)
    def callback_for_insert_before_in_file():
        pola_cari = pola_cari_edit2.text()  #.strip()
        content = insert_before_content.toPlainText() + '\n' # .replace('\\\\n', '\\n')  # .strip()
        if content and filePath:
            insert_before(filePath, pola_cari, content)
            print(f'insert [{content}] at {pola_cari} in {filePath}.')
            # parent.hide() # coba menu context tutup
            filemanip_menu.hide() # biar bisa akses menu lainnya (peek dsb)
    insert_before_button.clicked.connect(callback_for_insert_before_in_file)
    insert_before_action = QWidgetAction(filemanip_menu)
    insert_before_action.setDefaultWidget(insert_before_in_file_widget)
    filemanip_menu.addAction(insert_before_action)

    filemanip_menu.addSeparator()

    # indent file
    indent_file_file_widget = QWidget(filemanip_menu)
    indent_file_file_widget_layout = QHBoxLayout(indent_file_file_widget)
    space_or_tab = QComboBox(filemanip_menu)
    space_or_tab.addItems(['tab', '2','4'])
    indent_line_expression = QLineEdit()
    number_of_tab = QSpinBox()
    number_of_tab.setRange(1,1000) # sementara max file line no 1000 dulu
    number_of_tab.setValue(1)
    indent_file_button = QPushButton('Indent')
    indent_file_file_widget_layout.addWidget(QLabel('Tab/space:'))
    indent_file_file_widget_layout.addWidget(space_or_tab)
    indent_file_file_widget_layout.addWidget(QLabel('# tab:'))
    indent_file_file_widget_layout.addWidget(number_of_tab)
    indent_file_file_widget_layout.addWidget(QLabel('Line expr:'))
    indent_file_file_widget_layout.addWidget(indent_line_expression)
    indent_file_file_widget_layout.addWidget(indent_file_button)
    def callback_for_indent_file_file():
        num_tab = number_of_tab.value()
        space_or_tab_value = space_or_tab.currentText()
        use_tab = space_or_tab_value != 'tab'
        space_size = -1
        line_expression = indent_line_expression.text()
        if not use_tab:
            space_size = 2 if space_or_tab_value=='2' else 4
        if line_expression and filePath:
            indent_file(filePath, line_expression, use_tab=use_tab, num_tab=num_tab, space_size=space_size)
            print(f'indent_file {filePath}, space_size {space_size} use_tab {use_tab} num_tab {num_tab}')
            # parent.hide() # coba menu context tutup
            filemanip_menu.hide() # biar bisa akses menu lainnya (peek dsb)
    indent_file_button.clicked.connect(callback_for_indent_file_file)
    indent_file_action = QWidgetAction(filemanip_menu)
    indent_file_action.setDefaultWidget(indent_file_file_widget)
    filemanip_menu.addAction(indent_file_action)

    filemanip_menu.addSeparator()

    # dedent file
    dedent_file_file_widget = QWidget(filemanip_menu)
    dedent_file_file_widget_layout = QHBoxLayout(dedent_file_file_widget)
    space_or_tab2 = QComboBox(filemanip_menu)
    space_or_tab2.addItems(['tab', '2','4'])
    dedent_line_expression = QLineEdit()
    number_of_tab2 = QSpinBox()
    number_of_tab2.setRange(1,1000) # sementara max file line no 1000 dulu
    number_of_tab2.setValue(1)
    dedent_file_button = QPushButton('Dedent')
    dedent_file_file_widget_layout.addWidget(QLabel('Tab/space:'))
    dedent_file_file_widget_layout.addWidget(space_or_tab2)
    dedent_file_file_widget_layout.addWidget(QLabel('# tab:'))
    dedent_file_file_widget_layout.addWidget(number_of_tab2)
    dedent_file_file_widget_layout.addWidget(QLabel('Line expr:'))
    dedent_file_file_widget_layout.addWidget(dedent_line_expression)
    dedent_file_file_widget_layout.addWidget(dedent_file_button)
    def callback_for_dedent_file_file():
        num_tab = number_of_tab2.value()
        space_or_tab_value = space_or_tab2.currentText()
        use_tab = space_or_tab_value != 'tab'
        space_size = -1
        line_expression = dedent_line_expression.text()
        if not use_tab:
            space_size = 2 if space_or_tab_value=='2' else 4
        if line_expression and filePath:
            dedent_file(filePath, line_expression, use_tab=use_tab, num_tab=num_tab, space_size=space_size)
            print(f'dedent_file {filePath}, space_size {space_size} use_tab {use_tab} num_tab {num_tab}')
            # parent.hide() # coba menu context tutup
            filemanip_menu.hide() # biar bisa akses menu lainnya (peek dsb)
    dedent_file_button.clicked.connect(callback_for_dedent_file_file)
    dedent_file_action = QWidgetAction(filemanip_menu)
    dedent_file_action.setDefaultWidget(dedent_file_file_widget)
    filemanip_menu.addAction(dedent_file_action)

    filemanip_menu.addSeparator()

    # comment file
    comment_line_in_file_widget = QWidget(filemanip_menu)
    comment_line_in_file_widget_layout = QHBoxLayout(comment_line_in_file_widget)
    comment_line_starts = QLineEdit()
    comment_characters = QLineEdit()
    comment_characters.setText('#')
    comment_characters.setFixedWidth(40)
    comment_skip_whitespaces = QCheckBox()
    # comment_line_button = QPushButton('Replace string', comment_line_in_file_widget)
    comment_line_button = QPushButton('Comment lines')
    comment_line_in_file_widget.setFocusProxy(comment_line_starts)
    comment_line_in_file_widget_layout.addWidget(QLabel('Line startswith:'))
    comment_line_in_file_widget_layout.addWidget(comment_line_starts)
    comment_line_in_file_widget_layout.addWidget(QLabel('Comment characters:'))
    comment_line_in_file_widget_layout.addWidget(comment_characters)
    comment_line_in_file_widget_layout.addWidget(QLabel('Skip whitespaces:'))
    comment_line_in_file_widget_layout.addWidget(comment_skip_whitespaces)
    comment_line_in_file_widget_layout.addWidget(comment_line_button)
    def callback_for_comment_line_in_file():
        prefix_text = comment_line_starts.text()
        comment = comment_characters.text()
        if comment_line_starts and filePath:            
            if comment_skip_whitespaces.isChecked():
                comment_file_by_prefix(filePath, prefix_text, comment, re_prefixer='^\s+')
            else:
                comment_file_by_prefix(filePath, prefix_text, comment)
            # print(f'berhasil ganti "{oldstring}" menjadi "{newstring}" di {filePath}. status = {status}')
            # parent.hide() # coba menu context tutup
            filemanip_menu.hide() # biar bisa akses menu lainnya (peek dsb)
    comment_line_button.clicked.connect(callback_for_comment_line_in_file)
    comment_line_action = QWidgetAction(filemanip_menu)
    comment_line_action.setDefaultWidget(comment_line_in_file_widget)
    filemanip_menu.addAction(comment_line_action)

    filemanip_menu.addSeparator()

    # uncomment
    uncomment_line_in_file_widget = QWidget(filemanip_menu)
    uncomment_line_in_file_widget_layout = QHBoxLayout(uncomment_line_in_file_widget)
    uncomment_line_starts = QLineEdit()
    comment_characters = QLineEdit()
    comment_characters.setText('#')
    comment_characters.setFixedWidth(40)
    how_many_lines = QSpinBox()
    how_many_lines.setRange(1,100)
    how_many_lines.setValue(1)
    # uncomment_line_button = QPushButton('Replace string', uncomment_line_in_file_widget)
    uncomment_line_button = QPushButton('Comment lines')
    uncomment_line_in_file_widget.setFocusProxy(uncomment_line_starts)
    uncomment_line_in_file_widget_layout.addWidget(QLabel('Line startswith:'))
    uncomment_line_in_file_widget_layout.addWidget(uncomment_line_starts)
    uncomment_line_in_file_widget_layout.addWidget(QLabel('Comment characters:'))
    uncomment_line_in_file_widget_layout.addWidget(comment_characters)
    uncomment_line_in_file_widget_layout.addWidget(QLabel('How many to uncomment:'))
    uncomment_line_in_file_widget_layout.addWidget(how_many_lines)
    uncomment_line_in_file_widget_layout.addWidget(uncomment_line_button)
    def callback_for_uncomment_line_in_file():
        prefix_text = uncomment_line_starts.text()
        comment = comment_characters.text()
        if uncomment_line_starts and filePath:            
            uncomment_file(filePath, baris_cari=prefix_text, comment=comment, how_many_lines=how_many_lines.value())
            # print(f'berhasil ganti "{oldstring}" menjadi "{newstring}" di {filePath}. status = {status}')
            # parent.hide() # coba menu context tutup
            filemanip_menu.hide() # biar bisa akses menu lainnya (peek dsb)
    uncomment_line_button.clicked.connect(callback_for_uncomment_line_in_file)
    uncomment_line_action = QWidgetAction(filemanip_menu)
    uncomment_line_action.setDefaultWidget(uncomment_line_in_file_widget)
    filemanip_menu.addAction(uncomment_line_action)


    # filemanip_menu.addSeparator()

    # filemanip_menu.addSeparator()

    # filemanip_menu.addSeparator()

    return filemanip_menu
