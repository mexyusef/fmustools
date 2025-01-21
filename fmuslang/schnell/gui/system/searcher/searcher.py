import json
import os
import re
import sys
import pyperclip
from pyqtkeybind import keybinder
from functools import partial
from dotenv import load_dotenv

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *

# print('debug 001')
envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
load_dotenv(envfile)
ULIBPY_BASEDIR = os.environ['ULIBPY_BASEDIR']
SIDOARJODIR = os.environ['ULIBPY_ROOTDIR']
sys.path.extend([SIDOARJODIR, ULIBPY_BASEDIR])

from startup import startup # sidoarjodir
# from constants import sidoarjodir
# ULIBPY_BASEDIR = schnelldir
# SIDOARJODIR = sidoarjodir
MAX_ITEM = 7
MAX_LIST_LENGTH = 1000
MAX_VISIBLE_ITEMS = 12

import ctypes
myappid = 'fulgent.de.fmus.tools.0.0.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# print('debug 002')

ICON_FILEPATH = os.path.join(SIDOARJODIR, 'schnell/gui/system/searcher/logo.png')
if not os.path.isfile(ICON_FILEPATH):
  ICON_FILEPATH = os.path.join(ULIBPY_BASEDIR, 'gui/system/searcher/logo.png')


def parse_query(text):
  """
  cmd, arg = parse_query(text)

  harus bisa handle \py, dst...
  """
  if not text.startswith('\\'):
    return None, text
  m = re.search(r'\\(\S*)( (.*)){0,1}', text)
  return m.group(1), m.group(2)[1:] if not m.group(2) is None else None


# print('debug 003')
# ini termasuk initialize programming_data
startup()
# print('debug 004')
# ini kita pindah ke startup
# # utk redis subscribe
# # belum tau apa ini bisa berhasil atau tidak...
# try_pubsub_connect()

from schnell.gui.system.searcher.common import get_icon, about_qt
from schnell.gui.system.searcher.worker import Worker
from schnell.gui.system.searcher.make_redis import RedisWorker
from schnell.gui.system.searcher.make_redis_help import (
  get_cached_pubsub,
  clear_db_7, clear_db_8, clear_db_9,
  clearload,
  # try_pubsub_connect,
  # get_connection,
  redis_publish
)

from schnell.gui.system.searcher.make_py import PythonWorker
from schnell.gui.system.searcher.make_pydir import PyDirWorker
from schnell.gui.system.searcher.make_word import WordWorker
from schnell.gui.system.searcher.make_repl import REPLWorker
from schnell.gui.system.searcher.menu_runner import running
from schnell.gui.system.searcher.note import YellowNote
from schnell.gui.system.searcher.cmder import Cmder
from schnell.gui.system.searcher.windowshelper import to_top, set_topmost

from schnell.gui.system.searcher.edit_menu import edit_menu, sidoarjo_menu
from schnell.gui.system.searcher.widgets.clock import CornerWidget
from schnell.app.autoutils import klik, click
from schnell.app.gptutils import create_chatbot
from schnell.app.dirutils import joiner
# from schnell.app.envutils import env_get
from schnell.gui.system.searcher.searcher_constants import searcher_stylesheet

# print('debug 005')

class RedisSubscriber(QThread):

  incoming_data = pyqtSignal(object)

  def __init__(self, channel='replservice_response', redis_config_key='sub', *args, **kwargs):
    """
    https://stackoverflow.com/questions/7871526/is-non-blocking-redis-pubsub-possible
    """
    super(RedisSubscriber, self).__init__(*args, **kwargs)
    self.channel = channel
    # # print('pubsub #1')
    # self.r = get_connection(redis_config_key)
    # # print('pubsub #2')
    # try:
    #   self.pubsub = self.r.pubsub()
    #   # print('pubsub #3')
    # except Exception as err:
    #   print(err)
    self.pubsub = get_cached_pubsub(conn=redis_config_key, db=0)

    self.pubsub.subscribe(self.channel)
    # print('pubsub #4')

  def run(self):
    """
    https://stackoverflow.com/questions/7871526/is-non-blocking-redis-pubsub-possible
    .get_message() over .listen()
    """
    try:
      # print('pubsub #5')
      for message in self.pubsub.listen():

        if message.get('type') == 'message':
          msgdata = message.get('data')

          # print(f'[searcher][RedisSubscriber] message = {message}, data = {msgdata}, jenis = {type(msgdata)}\n')

          try:
            data = json.loads(msgdata)
          except:
            data = msgdata

          # print(f'[searcher][RedisSubscriber] data = {data}, jenis = {type(data)}\n')

          if isinstance(data, (bytes, bytearray, str)):
            if not isinstance(data, str):
              data = data.decode('utf8')
            if data in ['quit', 'bye', 'exit', 'q', 'x']:
              return  # perlukah keluar?
            else:
              # tampilkan di self.note, dg emit signal
              self.incoming_data.emit(data)
          elif isinstance(data, (dict, list)):
            # jk awalnya dict, handler jadikan json.dumps, di sini kita loads, jadi dict lagi
            # maka jadikan lagi string...
            data = json.dumps(data, indent=4)
            self.incoming_data.emit(data)

    except Exception as err:
      print(err)


class CenterListView(QListView):
  """Always scroll to center."""

  def __init__(self, parent=None):
    super(CenterListView, self).__init__(parent)
    self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
    self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    # self.setAttribute(Qt.WA_TranslucentBackground, True)
    # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
    # self.setRootIsDecorated(False)
    # self.setHeaderHidden(True)
    # self.setVerticalScrollBar(Bar())
    self.setUniformItemSizes(True)

  def scrollTo(self, index, _):
    """Always scroll to center."""
    super(CenterListView, self).scrollTo(
        index, QAbstractItemView.PositionAtCenter)


class SearchSuggestion(QWidget):

  activated = pyqtSignal(QModelIndex)

  def __init__(self, parent, screenw, screenh):

    QObject.__init__(self, parent)
    self.screenw, self.screenh = screenw, screenh
    self.editor = parent
    self.popup = None
    self.viewer = QWidget()
    self.viewer.setAttribute(Qt.WA_TranslucentBackground, True)
    self.viewer.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
    self.note = YellowNote()
    self.note.setupUi(self.viewer)
    pw = self.editor.width()
    ph = self.editor.height()
    # sama dengan lokasi popup
    # self.viewer.move(self.editor.mapToGlobal(QPoint(0, ph)))
    self.viewer.hide()

    self.list_popup = CenterListView()
    # self.list_popup.setStyleSheet('border-radius: 10px;')
    self.set_popup(self.list_popup)
    self.content = None

  def set_popup(self, popup):
    if self.popup:
      self.popup.removeEventFilter(self)

    self.popup = popup
    popup.setWindowFlags(Qt.Popup)
    popup.setFocusPolicy(Qt.NoFocus)

    # popup.setFocusProxy(self.editor)
    # gagal semua...
    # popup.setStyleSheet('border-radius: 10px;')
    # self.popup.setStyleSheet('border-radius: 10px;')

    popup.setMouseTracking(True)
    popup.installEventFilter(self)
    popup.clicked.connect(self.activated)
    # self.activated.connect(popup.hide)
    # coba tutup popup+viewer
    # self.activated.connect(self.hide_popup)
    self.activated.connect(self.hide_popup_show_viewer)

  def hide_popup(self):
    self.popup.hide()
    # self.from_popup_to_viewer(True, self.popup.width(), self.popup.height())

  def hide_popup_show_viewer(self):
    """
    model selected (activated signal)
    """
    self.popup.hide()
    # self.from_popup_to_viewer(True)
    self.from_popup_to_viewer(True, self.popup.width(), self.popup.height())

  def _resize_popup(self):
    """
    ukuran dan posisi diseting di sini
    """
    h = sum([
            self.popup.sizeHintForRow(0) * min(MAX_ITEM, self.row_count),
            self.popup.contentsMargins().top(),
            self.popup.contentsMargins().bottom()
            ])
    self.popup.resize(self.editor.width(), h)
    # self.popup._adjust_popup_height()
    #hsb = self.popup.horizontalScrollBar()
    # if hsb and hsb.isVisible():
    #h += hsb.sizeHint().height()
    jarak_vertikal = 10
    self.popup.move(self.editor.mapToGlobal(
        QPoint(0, self.editor.height()+jarak_vertikal)))
    # buat viewer di kanan
    # self.from_popup_to_viewer(True, self.editor.width(), self.editor.height(), h)
    # jk popup muncul, viewer mati
    self.from_popup_to_viewer(False)

  def from_popup_to_viewer(self, show=True, popup_width=0, popup_height=0, extra_tinggi=300, jarak_vertikal=10):
    if popup_width and popup_height:
      # self.viewer.resize(popup_width, popup_height+extra_tinggi)
      # di kanan dari popup
      # self.viewer.move(self.editor.mapToGlobal(QPoint(pw, ph)))

      # self.viewer.resize(popup_width, popup_height*3)
      # self.viewer.move(self.editor.mapToGlobal(QPoint(0, self.editor.height()+jarak_vertikal)))
      # _, y = self.editor.mapToGlobal(QPoint(0, self.editor.height()+jarak_vertikal))

      # update, kita ambil saja pos y...
      # resize_screen_ratio(object, screenw, screenh,
      # posx_ratio=1/2, posy_ratio=1/2, w_ratio=1/6, h_ratio=0, delta = 60):
      # resize_screen_ratio(self.completer.viewer, self.screenw, self.screenh,
      # posx_ratio=1/2, posy_ratio=3/4, w_ratio=0.8, h_ratio=0.5)
      resize_screen_ratio(self.viewer, self.screenw, self.screenh,
                          posx_ratio=1/2, posy_ratio=3/4, w_ratio=0.8, h_ratio=0.5)
    if show:
      self.viewer.show()
    else:
      self.viewer.hide()

  def completionModel(self):
    return self.model

  def done(self, index):
    if index.isValid():
      self.activated.emit(index)

  def eventFilter(self, o, e):
    # if e.type() == QEvent.MouseButtonPress:
      # self.popup.hide()
      # self.editor.setFocus()
      # return True

    if o == self.popup:
      if not self.popup.underMouse() and e.type() in (
              QEvent.MouseButtonPress,
              # QEvent.MouseButtonRelease,
              # QEvent.MouseButtonDblClick,
              # QEvent.MouseMove
      ):
        self.popup.hide()
        # self.editor.setFocus()
        #QApplication.sendEvent(self.editor, e)
        return False
      elif e.type() == QEvent.KeyPress:
        key = e.key()
        if e.key() == Qt.Key_Tab or e.key() == Qt.Key_J and e.modifiers() & Qt.ControlModifier:
          ne = QKeyEvent(
              QEvent.KeyPress,
              Qt.Key_Down,
              e.modifiers(),
              ''
          )
          QApplication.sendEvent(o, ne)
          return True
        elif e.key() == Qt.Key_Tab or e.key() == Qt.Key_K and e.modifiers() & Qt.ControlModifier:
          ne = QKeyEvent(
              QEvent.KeyPress,
              Qt.Key_Up,
              e.modifiers(),
              e.text(),
              e.isAutoRepeat(),
              e.count()
          )
          QApplication.sendEvent(o, ne)
          return True
        elif e.key() == Qt.Key_Up and self.attop:
          ne = QKeyEvent(
              QEvent.KeyPress,
              Qt.Key_End,
              Qt.ControlModifier
          )
          QApplication.sendEvent(o, ne)
          return True
        elif e.key() == Qt.Key_Down and self.atbottom:
          ne = QKeyEvent(
              QEvent.KeyPress,
              Qt.Key_Home,
              Qt.ControlModifier
          )
          QApplication.sendEvent(o, ne)
          return True
        elif key in (Qt.Key_Enter, Qt.Key_Return):
          self.done(self.popup.currentIndex())
          return True
        # elif e.key() == Qt.Key_Down:
        #     # gagal: dapatkan current index yg benar (selalu kurang)
        #     # print('down:', self.popup.currentIndex().row())
        #     # ne = QKeyEvent(
        #     #     QEvent.KeyPress,
        #     #     Qt.Key_Down,
        #     #     # e.modifiers(),
        #     #     Qt.ControlModifier,
        #     # )
        #     # QApplication.sendEvent(o, ne)
        #     # return True
        #     # text = f"choose: {self.popup.currentIndex().row()}"
        #     text = self.popup.currentIndex().data()
        #     self.note.setText(text)
        #     return False
        # elif e.key() == Qt.Key_Up:
        #     # text = f"choose: {self.popup.currentIndex().row()}"
        #     text = self.popup.currentIndex().data()
        #     # self.popup.mo
        #     self.note.setText(text)
        #     return False
        # elif key in (Qt.Key_Escape, ):
          # self.editor.setFocus()
          # self.popup.hide()
          # return True
        # elif key in (
          # Qt.Key_Home,
          # Qt.Key_End,
        # ):
          #QApplication.sendEvent(self.editor, e)
          # return True
        # elif key in (
          # Qt.Key_Up,
          # Qt.Key_Down,
          # Qt.Key_Home,
          # Qt.Key_End,
          # Qt.Key_PageUp,
          # Qt.Key_PageDown
          # ):
          # pass
        else:
          # self.editor.setFocus()
          # self.editor.event(e)
          # TODO: why HOME and END not processed by editor?
          QApplication.sendEvent(self.editor, e)
          # self.popup.hide()

    return self.super.eventFilter(o, e)

  @property
  def atbottom(self):
    p = self.popup
    return p.currentIndex().row() + 1 == p.model().rowCount(QModelIndex())

  @property
  def attop(self):
    return self.popup.currentIndex().row() == 0

  @property
  def popuped(self):
    return self.popup.isVisible()

  @property
  def super(self):
    return super(QWidget, self)

  @property
  def model(self):
    return self.popup.model() if self.popup else None

  @model.setter
  def model(self, value):
    self.popup.setModel(value)

  def reset(self):
    """Reset model and hide popup."""
    self.model = QStringListModel()
    self.hide_popup()

  def select_first_item(self):
    first_index = self.popup.model().index(0, 0)
    self.popup.selectionModel().setCurrentIndex(
        first_index,
        QItemSelectionModel.Select | QItemSelectionModel.Rows
    )
    self.popup.scrollTo(first_index, QAbstractItemView.PositionAtCenter)

  @property
  def row_count(self):
    return self.model.rowCount(QModelIndex())

  @property
  def empty(self):
    return self.row_count == 0

  def complete(self, content):
    if content is None:
      # logging.debug('Content should not be None...')
      content = []

    # cache content
    self.content = content

    # make model
    if isinstance(content, QAbstractItemModel):
      model = content
    else:
      model = QStringListModel()
      model.setStringList([str(c) for c in content])

    self.model = model

    if self.empty:
      # no suggestion, hide
      self.hide_popup()
    else:
      # self.popup.setFocus()
      self._resize_popup()
      self.select_first_item()
      self.popup.show()
      # self._continues_update()

  def _update_popup(self):
    model = self.model
    self.model = None
    self.model = model

  def _continues_update(self):
    if self.popuped:
      self._update_popup()
      QTimer.singleShot(1000, self._continues_update)


class AnimationShadowEffect(QGraphicsDropShadowEffect):

  def __init__(self, color, *args, **kwargs):
    super(AnimationShadowEffect, self).__init__(*args, **kwargs)
    self.setColor(color)
    # self.setOffset(0, 0)
    self.setOffset(5, 5)
    self.setBlurRadius(25)
    self._radius = 0
    self.animation = QPropertyAnimation(self)
    self.animation.setTargetObject(self)
    self.animation.setDuration(2000)
    self.animation.setLoopCount(-1)
    self.animation.setPropertyName(b'radius')
    self.animation.setKeyValueAt(0, 1)
    self.animation.setKeyValueAt(0.5, 30)
    self.animation.setKeyValueAt(1, 1)

  def start(self):
    self.animation.start()

  def stop(self, r=0):
    self.animation.stop()
    self.radius = r

  @pyqtProperty(int)
  def radius(self):
    return self._radius

  @radius.setter
  def radius(self, r):
    self._radius = r
    self.setBlurRadius(r)


class SearchInput(QLineEdit):

  def __init__(self, enter=lambda: None, parent=None):
    super(SearchInput, self).__init__(parent)
    self.enter = enter

  @property
  def super(self):
    return super(SearchInput, self)

  def keyPressEvent(self, e):
    # {
      # Qt.Key_Escape: lambda: self.setText(''),
      #Qt.Key_Return: self.enter
    # }.get(e.key(), lambda: None)()
    #super(SearchInput, self).keyPressEvent(e)

    if e.key() == Qt.Key_Escape:
      if self.text():
        self.setText('')
        e.accept()
      else:
        e.ignore()
    elif e.key() == Qt.Key_Return:
      self.enter()
    else:
      super(SearchInput, self).keyPressEvent(e)


def resize_screen_ratio(object, screenw, screenh, posx_ratio=1/2, posy_ratio=1/2, w_ratio=1/6, h_ratio=0, delta=60):
  """
  screen_geometry = PyQt5.QtWidgets.QDesktopWidget().screenGeometry(-1)
  screenw, screenh = screen_geometry.width(), screen_geometry.height()
  resize_screen_ratio(w1, screenw, screenh, 1/4, 1/5)
  resize_screen_ratio(w2, screenw, screenh, 3/4, 1/5)

  object hrs punya method resize dan move.
  """
  if h_ratio <= 0:
    h_ratio = w_ratio
  if posy_ratio <= 0:
    posy_ratio = posx_ratio
  lebar, tinggi = int(screenw*w_ratio), int(screenh*h_ratio)
  object.resize(lebar, tinggi)
  posx = int((screenw-lebar)*posx_ratio)
  posy = int((screenh-tinggi)*posy_ratio) - delta
  object.move(posx, posy)


class WinEventFilter(QAbstractNativeEventFilter):

  def __init__(self, keybinder):
    self.keybinder = keybinder
    super().__init__()

  def nativeEventFilter(self, eventType, message):
    ret = self.keybinder.handler(eventType, message)
    return ret, 0


class SearchMainWindow(QDialog):

  def _teardown_plugins(self):
    for p in self.plugins.values():
      if hasattr(p, 'teardown'):
        p.teardown()

  def _setup_plugins(self):
    for p in self.plugins.values():
      if hasattr(p, 'setup'):
        p.setup()

  def act(self):
    if self.cmd in ['x', 'q', 'exit']:
      self._teardown_plugins()
      # if hasattr(self, 'client'):
      #     self.client.stop()
      QApplication.quit()
    elif self.cmd == 'hello':
      print('hello, world!')
    elif self.cmd == 'load':
      r'''
      \load
      \load dirpath => masuk args...
      '''
      # from make_redis_help import clearload
      clearload()
      print('clearload/Db8 END...')
    elif self.cmd == 'pyload':
      r'''
      \pyload
      '''
      from make_py_help import pyload
      pyload()
      print('pyload/Db9 END...')
    elif self.cmd == 'clear7':
      clear_db_7()
      print('clear_db_7 END...')
    elif self.cmd == 'clear8':
      clear_db_8()
      print('clear_db_8 END...')
    elif self.cmd == 'clear9':
      clear_db_9()
      print('clear_db_9 END...')
    if self.cmd in self.plugins:
      print(f"""act()
			cmd = {self.cmd}
			query = {self.arg}
			""")
      if self.cmd == self.repl_worker.name:
        self.plugins[self.cmd].act(self.arg)
      else:
        self.plugins[self.cmd].act()
    else:
      # jk selc.cmd = \scala, \elixir, \clj dst...
      print('forcing switching language')
      self.repl_worker.act(f"\\{self.cmd}")

  def _install_plugins(self, plugins):
    self.plugins = {p.name: p for p in plugins}
    # yg pertama jadi default, jk gak specify cmd
    self.default_plugin = plugins[0] if self.plugins else None
    self._setup_plugins()

  def _try_query(self, text):
    """Avoid line editor frozen when key continues pressed."""
    QTimer.singleShot(0, lambda: self.query(text))

  def hide_window(self):
    # self.search_input.setText('')
    # self.completer.popup().hide()
    #self.setWindowState(self.windowState() | Qt.WindowMinimized)
    # print('[launcher][hide_window] hiding windows')
    self.hide()

  def select(self, index):
    cmd = self.cmd
    # text = self.completer.completionModel().data(index, Qt.DisplayRole)
    # self.hide_window() # ternyata ini sebabnya hide...susah mau diakses setelah itu
    assert self.completer.content
    if cmd in self.plugins:
      # if hasattr('select')
      content = self.plugins[cmd].select(
          content=self.completer.content, index=index)
      # bisa juga kita tampilkan: filepath, baris entry...gak hanya content hasil
      pyperclip.copy(str(content))
      # if hasattr('note')
      self.completer.note.setText(content)

  def _reset_popup(self):
    self.completer.reset()

  def _try_popup(self, content):
    # don't show popup if search box is hidden
    # print(f"_try_popup v=[{self.isVisible()}] dg content.data [{content}]")
    if self.isVisible():
      QTimer.singleShot(0, lambda: self.popup(content))

  def popup(self, content):
    with QMutexLocker(self.mutex):
      self.completer.complete(content)

  def query(self, text):
    cmd, arg = parse_query(text)
    # print(f'query, cmd = [{cmd}], arg = [{arg}]')
    self.arg = arg  # utk dipake di arg
    self.cmd = self.default_plugin.name if (
        (cmd is None) and (self.default_plugin)) else cmd
    if arg is None:
      self._reset_popup()
    else:
      plugin = None
      if cmd is None:
        if not self.default_plugin is None:
          plugin = self.default_plugin
      else:
        if cmd in self.plugins:
          plugin = self.plugins[cmd]
      if plugin:
        plugin.worker.clear()
        plugin.lit(
            arg,
            upper_bound=MAX_LIST_LENGTH,
            finished=self._try_popup
        )

  def __init__(self, screenw, screenh, *args, **kwargs):
    super(SearchMainWindow, self).__init__(*args, **kwargs)
    self.screenw = screenw
    self.screenh = screenh

    # print('mainwindow 001')
    self.init_logger()  # sblm menu
    # print('mainwindow 002')
    self.init_cmder()  # sblm menu
    # print('mainwindow 003')
    self.init_clocker()  # sblm menu
    # print('mainwindow 004')
    self.init()
    # print('mainwindow 005')
    self.init_thread()
    # print('mainwindow 006')
    self.init_server()
    # print('mainwindow 007')
    # markdown utk browser
    self.markdown_mode = False
    self.toggle_markdown_action.setIcon(self.stop_icon if self.markdown_mode else self.start_icon)

    # err...belum semua terinit
    # self.toggle_visibility() # main hide saja, jarang dipake, ctrl+a
    # print('mainwindow 008')

  def toggle_markdown_action_visibility(self):
    if self.markdown_mode:
      self.toggle_markdown_action.setIcon(self.start_icon)
      self.markdown_mode = False
    else:
      self.toggle_markdown_action.setIcon(self.stop_icon)
      self.markdown_mode = True

  def init_server(self):
    self.gptchat = None
    # command: ff, kanal ulang dan ulang/fromserver
    self.server_start_handler()
    # search: /something, kanal replservice_request dan replservice_response
    self.searchserver_start_handler()
    # utk creator, kanal service_creator_request dan service_creator_response
    self.service_creator_handler()

  def init_cmder(self):
    self.internal_cmder = Cmder()
    # self.internal_cmder.setAttribute(Qt.WA_TranslucentBackground, True)
    # self.internal_cmder.setWindowFlags(
    #     self.windowFlags() | Qt.FramelessWindowHint)
    # self.note = YellowNote()
    # stylesheet = """QTextBrowser{border: none; font: 14pt "Consolas"; background-color: #5aff5a; border-radius: 10px;}"""
    # self.note.setupUi(self.internal_cmder, stylesheet)
    resize_screen_ratio(self.internal_cmder, self.screenw, self.screenh,
                        posx_ratio=0.01, posy_ratio=0.95, w_ratio=0.8, h_ratio=0.25)
    self.internal_cmder.hide()

  def init_clocker(self):
    # print('clock 001')
    self.internal_clocker = CornerWidget()
    # print('clock 002')
    self.internal_clocker.setCmderToggler(self.toggle_cmder_action_visibility)
    # print('clock 003')
    self.internal_clocker.setRedisPublisher(redis_publish)
    # print('clock 004')
    self.internal_clocker.hide() # skrg lebih sering pake ini..., ctrl+shift+k
    # print('clock 005')
    self.internal_clocker.filemanager.show() # ctrl+shift+j
    # print('clock 006')

  def init_logger(self):
    self.internal_logger = QWidget()
    self.internal_logger.setAttribute(Qt.WA_TranslucentBackground, True)
    self.internal_logger.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
    self.note = YellowNote()
    stylesheet = """QTextBrowser{border: none; font: 14pt "Consolas"; background-color: #5aff5a; border-radius: 10px;}"""
    self.note.setupUi(self.internal_logger, stylesheet)
    resize_screen_ratio(self.internal_logger, self.screenw, self.screenh,
                        posx_ratio=0.01, posy_ratio=0.95, w_ratio=0.8, h_ratio=0.25)
    self.internal_logger.hide()

  def init_thread(self):
    # RedisSubscriber
    self.subscriber = RedisSubscriber()
    self.subscriber.incoming_data.connect(self.incomingData)
    self.subscriber.start()

    self.quick_subscriber = RedisSubscriber('quicklang_channel', 'quicklang_redisconfig')
    self.quick_subscriber.incoming_data.connect(self.incomingData)
    self.quick_subscriber.start()

    # image shower
    from schnell.app.redisquiutils import redis_subscribe_image
    # redis_subscribe_image(callback=lambda filepath: self.internal_clocker.filemanager.show_image(filepath))
    # redis_subscribe_image()

  def incomingData(self, data):
    # print('[searcher incomingData]', str(data))
    text = str(data)
    self.completer.note.show_and_print(text, self.markdown_mode)
    pyperclip.copy(text)
    resize_screen_ratio(self.completer.viewer, self.screenw, self.screenh,
                        posx_ratio=1/2, posy_ratio=0.9, w_ratio=1, h_ratio=0.7)
    self.completer.viewer.show()
    hwnd = self.completer.viewer.winId()
    to_top(hwnd)
    set_topmost(hwnd)

  def init(self):

    lay = QVBoxLayout()
    # spacing of search box
    lay.setSpacing(0)
    # lay.setMargin(0)

    self.search_input = SearchInput(self.act, self)
    # aniButton = AnimationShadowEffect(Qt.blue, self.search_input)
    aniButton = AnimationShadowEffect(Qt.yellow, self.search_input)
    # aniButton = AnimationShadowEffect(Qt.red, self.search_input)
    self.search_input.setGraphicsEffect(aniButton)
    aniButton.start()
    self.search_input.textChanged.connect(self._try_query)

    self.completer = SearchSuggestion(
        self.search_input, self.screenw, self.screenh)

    # completer/suggestion/popup diaktivasi jk user select item (tekan Enter) pada model/list
    # dan jika model/list tdk kosong
    # self.search_input.setCompleter(self.completer)
    self.completer.activated[QModelIndex].connect(self.select)

    lay.addWidget(self.search_input)
    self.setLayout(lay)
    # plugins = []
    worker = Worker()

    self.repl_worker = REPLWorker(worker)
    plugins = [
        # Go(worker=worker, client=client),
        # Run(worker=worker, client=client),
        self.repl_worker,  # \, = default
        RedisWorker(worker),  # \R = default
        PythonWorker(worker),  # \P
        PyDirWorker(worker),  # \dir
        WordWorker(worker),  # \W
    ]
    self._install_plugins(plugins)

    # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup | Qt.WindowStaysOnTopHint)
    self.setWindowTitle('launcher')
    self.mutex = QMutex()
    self.jobs = []

    self.setAttribute(Qt.WA_TranslucentBackground, True)
    self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

    self.tray_icon = QSystemTrayIcon(self)
    # self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
    self.tray_icon.setIcon(QIcon(QPixmap(ICON_FILEPATH)))
    self.setTrayMenu()
    self.trayMessage('App is running', 'App is running here in the tray')
    # self.tray_icon.hide(), jk window visible: hide tray, jk window hidden: show tray
    self.toggle_tray()

  def exit_not_close(self):
    # QApplication.quit() # ini salah/gagal, jadi restart
    QApplication.instance().quit()

  def chatgpt_handler(self):
    """
    chatgpt create/start, stop/exit
    """
    if self.chatgpt_action.data() == 1:
      # create new obj
      # self.gptchat.reset_chat()
      self.gptchat.refresh_session()
      #             self.fm.setGptChat
      #                               <- self.parent.gptchat
      # searcher -> clock.py -> fm.py -> mkhelp.py -> editor_fmus.py
      # owner                   owner
      #                         (....property....)
      self.chatgpt_action.setIcon(self.start_icon)
      self.chatgpt_action.setChecked(False)  # tidak jalan
      self.chatgpt_action.setData(0)
    else:
      # obj exit
      # self.gptchat.reset_chat()
      # self.gptchat.refresh_session()
      self.gptchat = create_chatbot()
      self.internal_clocker.setGptChat(self.gptchat)

      self.chatgpt_action.setIcon(self.stop_icon)
      self.chatgpt_action.setChecked(True)  # lagi jalan
      self.chatgpt_action.setData(1)

  def server_start_handler(self):
    """
    command server
    """
    # if self.server_action.isChecked():
    if self.server_action.data() == 1:
      # print('self.server_action.isChecked()...stopping now/unchecking...')
      running('stop')
      self.server_action.setIcon(self.start_icon)
      self.server_action.setChecked(False)  # tidak jalan
      self.server_action.setData(0)
    else:
      # print('self.server_action IS NOT CHECKED (in stopped mode), starting/checking')
      # set icon ke berbeda
      running('S', self.print_to_logger)
      self.server_action.setIcon(self.stop_icon)
      self.server_action.setChecked(True)  # lagi jalan
      self.server_action.setData(1)

  # def server_stop_handler(self):
  #   running('stop')
  #   self.server_stop.setIcon(self.start_icon)
  #   self.server_action.setIcon(self.start_icon)

  def searchserver_start_handler(self):
    """
    search server
    """
    # if self.searchserver_action.isChecked():
    if self.searchserver_action.data() == 1:
      running('server_search_stop')
      self.searchserver_action.setIcon(self.start_icon)
      self.searchserver_action.setChecked(False)  # tidak jalan
      self.searchserver_action.setData(0)
    else:
      # set icon ke berbeda
      running('server_search_start', self.print_to_logger)
      self.searchserver_action.setIcon(self.stop_icon)
      self.searchserver_action.setChecked(True)  # lagi jalan
      self.searchserver_action.setData(1)

  def service_creator_handler(self):
    """
    group server = ulang + replservice_request
    """
    # if self.searchserver_action.isChecked():
    if self.servicecreator_action.data() == 1:
      running('redis_for_creator_stop')
      self.servicecreator_action.setIcon(self.start_icon)
      self.servicecreator_action.setChecked(False)  # tidak jalan
      self.servicecreator_action.setData(0)
    else:
      # set icon ke berbeda
      running('redis_for_creator_start', self.print_to_logger)
      self.servicecreator_action.setIcon(self.stop_icon)
      self.servicecreator_action.setChecked(True)  # lagi jalan
      self.servicecreator_action.setData(1)

  def toggle_clocker_action_visibility(self):
    if self.internal_clocker.isVisible():
      self.toggle_clocker_action.setIcon(self.start_icon)
      self.internal_clocker.hide()
    else:
      self.toggle_clocker_action.setIcon(self.stop_icon)
      self.internal_clocker.show()
      # focus masuk tapi mouse ada di tempat lain
      self.internal_clocker.inputter.setFocus()

      # klik(0.3)
      x,y = self.internal_clocker.inputter.pos()
      click(x+2,y+2)

  def toggle_filemanager_visibility(self):
    if self.internal_clocker.filemanager.isVisible():
      # self.toggle_clocker_action.setIcon(self.start_icon)
      self.internal_clocker.filemanager.hide()
    else:
      # self.toggle_clocker_action.setIcon(self.stop_icon)
      self.internal_clocker.filemanager.show()
      to_top(self.internal_clocker.filemanager.winId())

  def toggle_cmder_action_visibility(self):
    if self.internal_cmder.isVisible():
      self.toggle_cmder_action.setIcon(self.start_icon)
      self.internal_cmder.hide()
    else:
      self.toggle_cmder_action.setIcon(self.stop_icon)
      self.internal_cmder.show()

  def toggle_logger_action_visibility(self):
    if self.internal_logger.isVisible():
      self.toggle_logger_action.setIcon(self.start_icon)
      self.internal_logger.hide()
    else:
      self.toggle_logger_action.setIcon(self.stop_icon)
      self.internal_logger.show()

  def print_to_logger(self, text):
    self.note.appendText(text)

  def setTrayMenu(self):
    # gunakan SP_MediaPlay dan SP_MediaStop utk server start/stop
    # play jk belum start, stop jk sedang listen
    self.start_icon = QApplication.style().standardIcon(QStyle.SP_MediaPlay)
    self.stop_icon = QApplication.style().standardIcon(QStyle.SP_MediaStop)
    exit_icon = QApplication.style().standardIcon(QStyle.SP_BrowserStop)

    show_action = QAction(get_icon(), "Menu Show", self)
    quit_action = QAction(exit_icon, "Menu Exit", self)
    hide_action = QAction(get_icon(), "Menu Hide", self)

    show_action.triggered.connect(self.show)
    hide_action.triggered.connect(self.hide)
    quit_action.triggered.connect(QApplication.instance().quit)

    self.tray_menu = QMenu()

    # chatgpt_action
    self.chatgpt_action = QAction(
        self.start_icon, "ChatGPT'", self)
    # self.tray_menu.addAction(get_icon(), 'server start', lambda: running('S'))
    # self.chatgpt_action.setShortcut('Ctrl+S')
    self.chatgpt_action.setCheckable(True)
    # https://stackoverflow.com/questions/70104570/qaction-ischecked-seems-to-report-inverted-value
    self.chatgpt_action.setChecked(True)
    self.chatgpt_action.setData(0)
    self.chatgpt_action.triggered.connect(self.chatgpt_handler)
    self.tray_menu.addAction(self.chatgpt_action)

    self.server_action = QAction(
        self.start_icon, "Server Command 'replservice_request'", self)
    # self.tray_menu.addAction(get_icon(), 'server start', lambda: running('S'))
    self.server_action.setShortcut('Ctrl+S')
    self.server_action.setCheckable(True)
    # https://stackoverflow.com/questions/70104570/qaction-ischecked-seems-to-report-inverted-value
    # inverted???
    self.server_action.setChecked(True)
    self.server_action.setData(0)
    self.server_action.triggered.connect(self.server_start_handler)
    # icon, text, slot, shortcut
    self.tray_menu.addAction(self.server_action)

    self.searchserver_action = QAction(
        self.start_icon, "Server Search 'ulang'", self)
    self.searchserver_action.setShortcut('Ctrl+Z')
    self.searchserver_action.setCheckable(True)
    self.searchserver_action.setChecked(True)
    self.searchserver_action.setData(0)
    self.searchserver_action.triggered.connect(self.searchserver_start_handler)
    # icon, text, slot, shortcut
    self.tray_menu.addAction(self.searchserver_action)

    self.servicecreator_action = QAction(
        self.start_icon, "Server ulang+replservice_request", self)
    self.servicecreator_action.setShortcut('Ctrl+S')
    self.servicecreator_action.setCheckable(True)
    # self.server_action.setChecked(True)
    self.servicecreator_action.setData(0)
    self.servicecreator_action.triggered.connect(self.service_creator_handler)
    # icon, text, slot, shortcut
    self.tray_menu.addAction(self.servicecreator_action)

    self.tray_menu.addAction(get_icon(), 'MMM', lambda: running('m'))
    self.tray_menu.addAction(get_icon(), 'Helper', lambda: running('h'))
    self.tray_menu.addAction(get_icon(), 'GH Repo', lambda: running('ghrepo'))
    self.tray_menu.addAction(get_icon(), 'GH Gist', lambda: running('ghgist'))
    self.tray_menu.addAction(get_icon(), 'GH Issue',
                             lambda: running('ghissue'))
    self.tray_menu.addAction(get_icon(), 'GH PR', lambda: running('ghpull'))

    # # self.tray_menu.addAction(get_icon(), 'Server stop', lambda: running('stop'))
    # self.server_stop = QAction(self.start_icon, "Server stop", self)
    # self.server_stop.triggered.connect(self.server_stop_handler)
    # self.tray_menu.addAction(self.server_stop)

    self.editor_menu = QMenu('Edit', self.tray_menu)
    self.editor_menu.setIcon(get_icon())
    # github repoall, gistall, issue, pullrequest
    self.editor_menu.addAction(get_icon(), 'Edit searcher.py (me)', lambda: os.system(
        f'code {ULIBPY_BASEDIR}/gui/system/searcher/searcher.py'))
    self.editor_menu.addAction(get_icon(), 'Edit kbrepl.mk', lambda: os.system(
        f'code {ULIBPY_BASEDIR}/gui/system/help/kbrepl.mk'))
    self.editor_menu.addAction(get_icon(), 'Edit pyqt5.mk', lambda: os.system(
        f'code {SIDOARJODIR}/database/refcards/pyqt5.mk'))
    self.editor_menu.addAction(get_icon(), 'Edit lalang.py', lambda: os.system(
        f'code {ULIBPY_BASEDIR}/app/transpiler/lalang.py'))
    self.editor_menu.addAction(get_icon(), 'Edit csvlang.py', lambda: os.system(
        f'code {ULIBPY_BASEDIR}/app/transpiler/mycsv/main.py'))
    self.editor_menu.addAction(get_icon(), 'Edit fullstack.py', lambda: os.system(
        f'code {ULIBPY_BASEDIR}/app/transpiler/frontend/fullstack.py'))
    self.editor_menu.addAction(get_icon(), 'Edit mmm.py', lambda: os.system(
        f'code {ULIBPY_BASEDIR}/gui/system/launcher/mmm.py'))
    self.editor_menu.addAction(get_icon(), 'Edit gh repo.py', lambda: os.system(
        f'code {ULIBPY_BASEDIR}/gui/system/launcher/helper/repoall.py'))
    edit_menu(self.editor_menu, get_icon, ULIBPY_BASEDIR, SIDOARJODIR)
    self.editor_menu.addAction(get_icon(
    ), 'Edit GUI/readme', lambda: os.system(f'code {SIDOARJODIR}/data/gui/README.md'))
    self.editor_menu.addAction(get_icon(
    ), 'Edit GH/readme', lambda: os.system(f'code {SIDOARJODIR}/data/github/README.md'))

    self.editor_menu.addAction(
        get_icon(), 'Open schnell', lambda: os.system(f'code {SIDOARJODIR}/schnell/'))
    self.editor_menu.addAction(get_icon(), 'Open sidoarjo', lambda: os.system(
        f'code {SIDOARJODIR}/'), 'Ctrl+O')
    # self.editor_menu.addAction(
    #     get_icon(), 'Open fmusify', lambda: os.system(f'code C:/work/fmusify'))
    self.editor_menu.addAction(get_icon(), 'Open GH', lambda: os.system(
        f'code {SIDOARJODIR}/data/github/'))
    # self.editor_menu.addAction(
    #     get_icon(), 'Open GH/go', lambda: os.system(f'code {godir}/'))
    # self.editor_menu.addAction(
    #     get_icon(), 'Sublime GH/go', lambda: os.system(f"subl {godir}/"))
    self.editor_menu.addAction(get_icon(), 'Open rockit mex', lambda: os.system(
        f'code C:/work/upw/rockit/mex'))
    self.editor_menu.addAction(
        get_icon(), 'Open django play', lambda: os.system(f'code C:/work/upw/_create'))
    self.editor_menu.addAction(
        get_icon(), 'Open resto', lambda: os.system(f'code C:/work/upw/menu/resto'))
    # cmd.exe /c start "judul window baru" /D c:\\work
    self.editor_menu.addAction(
        get_icon(), 'CMD resto', lambda: os.system('cmd.exe /c start "RESTO" /D c:\\work\\upw\\menu\\resto'))
    self.editor_menu.addAction(
        get_icon(), 'CMD flaskfaker', lambda: os.system('cmd.exe /c start "FLASKFAKER" /D c:\\work\\flaskfaker'))
    self.editor_menu.addAction(
        get_icon(), 'CMD ulang', lambda: os.system('cmd.exe /c start "ULANG" /D c:\\work\\ulang'))
    self.editor_menu.addAction(
        get_icon(), 'q editor', lambda: running('qedit'))
    self.editor_menu.addAction(
        get_icon(), 'tk editor', lambda: running('tkedit'))
    self.editor_menu.addAction(get_icon(), 'Edit tkeditor', lambda: os.system(
        f'code {ULIBPY_BASEDIR}/gui/system/editor/tkeditor.py'))
    self.tray_menu.addMenu(self.editor_menu)
    self.tray_menu.addMenu(sidoarjo_menu(self, get_icon, ULIBPY_BASEDIR, SIDOARJODIR))

    # self.tray_menu.addAction(get_icon(), 'CMD /k', lambda: os.system('cmd /k start')) # err, ini quit app
    self.tray_menu.addAction(
        get_icon(), 'CMD /c', lambda: os.system('cmd /c start'))

    fake_menu = QMenu('Cake menu', self.tray_menu)
    fake_menu.setIcon(get_icon())
    for i in range(5):
      fake_menu.addAction(get_icon(), f'Cake {i}', partial(
          print, f"Hello numero #{i}"))
    self.tray_menu.addMenu(fake_menu)

    self.tray_menu.addAction(show_action)

    self.tray_menu.addAction(get_icon(), 'About', about_qt)

    self.toggle_logger_action = QAction(self.start_icon, "Logger", self)
    self.toggle_logger_action.setShortcut('Ctrl+L')
    self.toggle_logger_action.triggered.connect(
        self.toggle_logger_action_visibility)
    self.tray_menu.addAction(self.toggle_logger_action)

    self.toggle_cmder_action = QAction(self.start_icon, "Cmder", self)
    self.toggle_cmder_action.triggered.connect(
        self.toggle_cmder_action_visibility)
    self.tray_menu.addAction(self.toggle_cmder_action)

    self.toggle_clocker_action = QAction(self.start_icon, "Clock", self)
    self.toggle_clocker_action.triggered.connect(
        self.toggle_clocker_action_visibility)
    self.tray_menu.addAction(self.toggle_clocker_action)

    self.toggle_markdown_action = QAction(self.start_icon, "Markdown", self)
    self.toggle_markdown_action.triggered.connect(
        self.toggle_markdown_action_visibility)
    self.tray_menu.addAction(self.toggle_markdown_action)    

    self.tray_menu.addAction(quit_action)
    self.tray_menu.setWindowFlags(self.tray_menu.windowFlags(
    ) | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
    self.tray_icon.setContextMenu(self.tray_menu)

  def trayMessage(self, judul, isi, lama=3000):
    self.tray_icon.showMessage(judul, isi, QSystemTrayIcon.Information, lama)

  def doShakeMenu(self, target):
    if hasattr(target, '_shake_animation'):
      return
    animation = QPropertyAnimation(target, b'pos', target)
    target._shake_animation = animation
    animation.finished.connect(lambda: delattr(target, '_shake_animation'))
    pos = target.pos()
    x, y = pos.x(), pos.y()

    animation.setDuration(200)
    animation.setLoopCount(2)
    animation.setKeyValueAt(0, QPoint(x, y))
    animation.setKeyValueAt(0.09, QPoint(x + 2, y - 2))
    animation.setKeyValueAt(0.18, QPoint(x + 4, y - 4))
    animation.setKeyValueAt(0.27, QPoint(x + 2, y - 6))
    animation.setKeyValueAt(0.36, QPoint(x + 0, y - 8))
    animation.setKeyValueAt(0.45, QPoint(x - 2, y - 10))
    animation.setKeyValueAt(0.54, QPoint(x - 4, y - 8))
    animation.setKeyValueAt(0.63, QPoint(x - 6, y - 6))
    animation.setKeyValueAt(0.72, QPoint(x - 8, y - 4))
    animation.setKeyValueAt(0.81, QPoint(x - 6, y - 2))
    animation.setKeyValueAt(0.90, QPoint(x - 4, y - 0))
    animation.setKeyValueAt(0.99, QPoint(x - 2, y + 2))
    animation.setEndValue(QPoint(x, y))
    animation.start(animation.DeleteWhenStopped)

  def shakeMenu(self):
    """
    gak bisa utk context menu
    pos = target.pos()
    AttributeError: 'QSystemTrayIcon' object has no attribute 'pos'
    """
    print('shaking menu...')
    self.doShakeMenu(self.tray_icon)

  def closeEvent(self, event):
    # if self.check_box.isChecked():
    event.ignore()
    # self.hide()
    self.toggle_visibility()
    self.trayMessage('App is running', 'App is running here in the tray')

  def toggle_visibility(self):
    if self.isVisible():
      self.hide()
      self.completer.viewer.hide()  # sticky note suka ketinggalan...
      # self.completer.note.hide()  # sticky note suka ketinggalan...note itu obj, bukan widget
      self.tray_icon.show()
    else:
      # to_top(self.winId())
      set_topmost(self.winId())
      self.show()
      self.tray_icon.hide()

  def toggle_tray(self):
    if self.isVisible():
      self.tray_icon.hide()
    else:
      self.tray_icon.show()

  # def winId(self):
  #     """
  #     https://stackoverflow.com/questions/39734913/how-to-get-hwnd-for-qdialog-in-windows-10
  #     Set the Qt::WA_NativeWindow attribute on widgets: The widget itself and all of its ancestors will become native (unless Qt::WA_DontCreateNativeAncestors is set).
  #     """
  #     return self.window().winId()

  def setApplicationIcon(self, filepath):
    # window.setWindowIcon(QIcon('web.png')
    self.setWindowIcon(QIcon(filepath))


def main():

  # print('debug 006')

  app = QApplication([])
  app.setStyleSheet(searcher_stylesheet)

  screen_geometry = QDesktopWidget().screenGeometry(-1)
  screenw, screenh = screen_geometry.width(), screen_geometry.height()

  # print('debug 006b')

  window = SearchMainWindow(screenw, screenh)

  # print('debug 007')

  resize_screen_ratio(window, screenw, screenh,
                      posy_ratio=0.15, w_ratio=1/2, h_ratio=1/20)

  # print('debug 008')

  keybinder.init()

  # print('debug 009')

  def callback_show():
    # print("showing")
    window.show()

  def callback_toggle():
    # print("toggle visibility")
    window.toggle_visibility()

  def callback_hide():
    # print("hiding")
    window.hide()

  def exit_app():
    # print('quitting')
    # window.close()
    window.exit_not_close()  # err

  def show_menu():
    # print('tunjukkan menu...')
    # window.tray_icon.contextMenu().show()
    menu = window.tray_icon.contextMenu()
    if menu.isVisible():
      menu.close()
    else:
      # menu.exec(QtCore.QPoint(0,0))
      posx = int(screenw * 0.9)
      posy = int(screenh * 0.8)
      menu.exec(QtCore.QPoint(posx, posy))
      # QTimer.singleShot(100, lambda:window.shakeMenu())

  def unregister():
    keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+A")
    print("unregister and register previous binding")
    keybinder.register_hotkey(window.winId(), "Shift+Ctrl+A", callback_toggle)

  def view_helper():
    running('h')

  def view_mmm():
    running('m')

  def run_u():
    from schnell.app.threadutils import startme
    startme(os.system, 'U is running', pyperclip.paste()[:80]+'...', ['u'])

  def run_u2():
    # from schnell.app.threadutils import startme
    from schnell.app.fmusutils import run_fmus_for_content_in_thread_notify
    # startme(os.system, 'U is running', pyperclip.paste()[:80]+'...', ['u'])
    content = pyperclip.paste()
    run_fmus_for_content_in_thread_notify(content, os.getcwd(), title='U2 is running', body=content[:80]+'...')

  def run_y():
    """
    apa nih, ctrl+shift+y utk replify???
    """
    from schnell.creator.repl_language.replify import quick_replify
    quick_replify(pyperclip.paste())

  def run_ocr():
    running('ocr')

  def run_ocr_local():
    from schnell.app.ocrutils import ocr_screenshot
    ocr_screenshot()

  def run_ocr_google():
    running('ocr_google')

  def toggle_clock():
    window.toggle_clocker_action_visibility()

  def screenshot_clipboard():
    from schnell.app.ocrutils import clipboard_screenshot, clipboard_screenshot2, clipboard_screenshot3
    clipboard_screenshot3()

  def toggle_filemanager():
    window.toggle_filemanager_visibility()

  # print('debug 0010')

  # keybinder.register_hotkey(window.winId(), "Print Screen", callback_show)
  keybinder.register_hotkey(window.winId(), "Shift+Ctrl+A", callback_toggle)
  keybinder.register_hotkey(window.winId(), "Shift+Ctrl+Alt+E", exit_app)
  # keybinder.register_hotkey(window.winId(), "Shift+Ctrl+F", unregister)
  keybinder.register_hotkey(window.winId(), "Shift+Ctrl+Alt+G", show_menu)
  # keybinder.register_hotkey(window.winId(), "Shift+Ctrl+H", view_helper)
  keybinder.register_hotkey(window.winId(), "Shift+Ctrl+Alt+J", toggle_filemanager)
  keybinder.register_hotkey(window.winId(), "Shift+Ctrl+Alt+K", toggle_clock)
  keybinder.register_hotkey(window.winId(), "Shift+Ctrl+L", screenshot_clipboard) # capture -> clipboard
  # keybinder.register_hotkey(window.winId(), "Shift+Ctrl+M", view_mmm)
  keybinder.register_hotkey(window.winId(), "Shift+Ctrl+O", run_ocr_local) # capture -> text (ocr)
  # keybinder.register_hotkey(window.winId(), "Shift+Ctrl+U", run_u)
  keybinder.register_hotkey(window.winId(), "Shift+Ctrl+U", run_u2) # run fmuslang
  keybinder.register_hotkey(window.winId(), "Shift+Ctrl+Alt+Y", run_y) # run replify

  win_event_filter = WinEventFilter(keybinder)
  event_dispatcher = QAbstractEventDispatcher.instance()
  event_dispatcher.installNativeEventFilter(win_event_filter)

  # print('debug 011')

  # https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
  # setApplicationIcon(window)
  window.setApplicationIcon(joiner(SIDOARJODIR, 'fmus-us.png'))
  window.show()
  # ini window searcher, jd gak showmax
  # window.showMaximized()
  callback_toggle()
  # sys.exit(app.exec_())
  app.exec_()

  # print('debug 012')

  keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+Alt+Y")
  keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+U")
  keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+O")
  # keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+M")
  keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+L")
  keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+Alt+K")
  keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+Alt+J")
  # keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+H")
  keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+Alt+G")
  keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+Alt+E")
  keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+A")
  # keybinder.unregister_hotkey(window.winId(), "Print Screen")


if __name__ == '__main__':
  main()
