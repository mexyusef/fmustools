from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os


def edit_menu(editor_menu, get_icon, ULIBPY_BASEDIR, SIDOARJODIR):
    editor_menu.addAction(get_icon(), 'Edit geura/readme',
                               lambda: os.system(f'code {SIDOARJODIR}/database/geura/README.md'))
    editor_menu.addAction(get_icon(), 'Edit ageh/django.mk',
                               lambda: os.system(f'code {SIDOARJODIR}/database/ageh/django.mk'))
    editor_menu.addAction(get_icon(), 'Open geura (epmus)',
                               lambda: os.system(f'code {SIDOARJODIR}/database/geura/'))
    editor_menu.addAction(get_icon(), 'Open ageh (smus)',
                               lambda: os.system(f'code {SIDOARJODIR}/database/ageh/'))
    editor_menu.addAction(get_icon(), 'Open refcards/epmus+smus',
                               lambda: os.system(f'code {SIDOARJODIR}/database/refcards/'))
    editor_menu.addAction(get_icon(), 'Edit guilang.py',
                               lambda: os.system(f'code {ULIBPY_BASEDIR}/app/quick/languages/guilang.py'))


def sidoarjo_menu(self, get_icon, ULIBPY_BASEDIR, SIDOARJODIR):
    self.sidomuncul = QMenu('Sidoarjo', self)
    self.sidomuncul.setIcon(get_icon())
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo', lambda: os.system(
        f'code {SIDOARJODIR}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/codes', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "codes")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/coords', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "coords")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/coords/fullstack', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "coords/fullstack")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/coords/fullstack/__init__.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "coords/fullstack/__init__.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/data', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/data/github', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data/github")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/data/gui', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data/gui")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/data/gui/README.md⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data/gui/README.md")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/data/gui/PyQt/README.md⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data/gui/PyQt/README.md")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/database', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "database")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/database/ageh', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "database/ageh")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/database/geura', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "database/geura")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/database/refcards', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "database/refcards")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/database/refcards/pyqt5.mk⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "database/refcards/pyqt5.mk")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/database/zhelps', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "database/zhelps")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/schnell', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/schnell/app', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/wmc.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/wmc.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/quick/blitz/__init__.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/quick/blitz/__init__.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/quick/dahsyater.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/quick/dahsyater.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/schnell/app/transpiler', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/transpiler")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/transpiler/frontend/fullstack.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/transpiler/frontend/fullstack.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/transpiler/frontend/fslang/django/__init__.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/transpiler/frontend/fslang/django/__init__.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/transpiler/frontend/fslang/node_antd/__init__.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/transpiler/frontend/fslang/node_antd/__init__.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/schnell/gui', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/schnell/gui/system', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/schnell/gui/system/help', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/help")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/gui/system/help/helper.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/help/helper.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/gui/system/launcher/mmm.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/launcher/mmm.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/schnell/gui/system/searcher', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/searcher")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/gui/system/searcher/searcher.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/searcher/searcher.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open C:/src/', lambda: os.system(
        f'code C:/src/'))
    self.sidomuncul.addAction(get_icon(), 'Open C:/src/flet-flutter/', lambda: os.system(
        f'code C:/src/flet-flutter/'))
    self.sidomuncul.addAction(get_icon(), 'Open C:/verwijderen/', lambda: os.system(
        f'code C:/verwijderen/'))
    return self.sidomuncul
