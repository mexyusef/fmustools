import os, random, string, sys, subprocess, json, functools
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *
# from PyQt5.Qsci.QsciScintilla import *


envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
from dotenv import load_dotenv
load_dotenv(envfile)
schnelldir = os.environ['ULIBPY_BASEDIR']
sidoarjodir = os.environ['ULIBPY_ROOTDIR']
sys.path.extend([sidoarjodir, schnelldir])

if __name__ == '__main__':
    from mylexers import LANGUAGES, LEXERS
    from common import get_icon, autocompletions, bahasa_filepaths
else:
    from schnell.gui.system.searcher.widgets.mylexers import LANGUAGES, LEXERS
    from schnell.gui.system.searcher.widgets.common import get_icon, autocompletions, bahasa_filepaths

from schnell.app.fileutils import (
    content_length, file_length, line_number_expression, get_daftar,
    get_definition_double_entry_aware,
    file_write,
    file_content,
    get_extension,
)
from schnell.app.dirutils import (
    joiner,
    files_filter,
    get_cwd,
    tempdir,
    timestamp,
)
from schnell.app.fmusutils import run_fmus_for_content_in_thread
from schnell.app.redisutils import savedconn, redis_publish


CREATOR_CHANNEL_REQUEST = 'service_creator_request'
CREATOR_CHANNEL_RESPONSE = 'service_creator_response'


class RedisSubscriber(QThread):

  incomingData = pyqtSignal(object)

  def __init__(self, channel=CREATOR_CHANNEL_RESPONSE, *args, **kwargs):
    """
    utk nama kanal, lihat system/searcher/menu_runner.py
    https://stackoverflow.com/questions/7871526/is-non-blocking-redis-pubsub-possible
    """
    super(RedisSubscriber, self).__init__(*args, **kwargs)
    self.channel = channel
    # print('pubsub #1')
    # self.r = get_connection('sub')
    self.r = savedconn(0)
    try:
      self.pubsub = self.r.pubsub()
      # print('pubsub #3')
    except Exception as err:
      print(err)
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
        # print('[searcher][thread run] message:', message, '\n')
        if message.get('type') == 'message':
          data = json.loads(message.get('data'))
          if isinstance(data, (bytes, bytearray, str)):
            if not isinstance(data, str):
              data = data.decode('utf8')
            if data in ['quit', 'bye', 'exit', 'q', 'x']:
              return  # perlukah keluar?
            else:
              # tampilkan di self.note, dg emit signal
              self.incomingData.emit(data)
    except Exception as err:
      print(err)


class HelperEditor(QsciScintilla):
    # more https://riverbankcomputing.com/pipermail/pyqt/2009-July/023783.html
    def __init__(self, content=None):
        super().__init__()
        self.setStyleSheet('background-color: lemonchiffon;')
        # global background
        self.SendScintilla(QsciScintilla.SCI_STYLESETBACK, QsciScintilla.STYLE_DEFAULT, QColor('#F0E68C'));
        # utk background tulisan
        self.setPaper(QColor('#F0E68C'))
        self.setFont(QFont('Terminal', 16))
        self.setMarginType(1, QsciScintilla.NumberMargin)
        self.setMarginWidth(0, 35)
        self.setMarginLineNumbers(0, True)
        # self.setMarginsBackgroundColor(QColor("gainsboro"))
        self.setMarginWidth(1, 0)
        self.setMarginWidth(2, 14) # folded area
        if content:
            self.setText(content)


class CreatorEditor(QsciScintilla):

    save_file = pyqtSignal(bool)
    line_numbers_request = pyqtSignal(tuple)
    replrequest = pyqtSignal(tuple)
    fmusrequest = pyqtSignal(str, int, int, int, int)

    def __init__(self, parent=None, *args, **kwargs):
        super(CreatorEditor, self).__init__(parent, *args, **kwargs)
        self.margin = 24
        self.init()
        self.linesChanged.connect(self.onLinesChanged)
        # self.setStyleSheet('background-color: #FFEBCD;')
        self.SendScintilla(QsciScintilla.SCI_STYLESETBACK, QsciScintilla.STYLE_DEFAULT, QColor('#FFEBCD'))
        self.setPaper(QColor('#FFEBCD'))
        # self.setEolMode(QsciScintilla.EolWindows)
        self.setEolMode(QsciScintilla.EolUnix)
        # self.setEolVisibility(True)
        # self.setFont(QFont('Terminal', 16))

    def keyPressEvent(self, event):
        """
        https://www.programcreek.com/python/example/101683/PyQt5.QtCore.Qt.Key_Backspace
        https://stackoverflow.com/questions/6647970/how-can-i-capture-qkeysequence-from-qkeyevent-depending-on-current-keyboard-layo
        https://www.programcreek.com/python/example/101657/PyQt5.QtCore.Qt.Key_Up
        property var keys: ({
        0x01000000: "Escape",
        0x01000001: "Tab", 0x01000002: "Backtab", 0x01000003: "Backspace", 0x01000004: "Return", 0x01000005: "Enter", 0x01000006: "Insert", 0x01000007: "Delete", 0x01000008: "Pause", 0x01000009: "Print", 0x0100000a: "SysReq", 0x0100000b: "Clear", 0x01000010: "Home", 0x01000011: "End", 0x01000012: "Left", 0x01000013: "Up", 0x01000014: "Right", 0x01000015: "Down", 0x01000016: "PageUp", 0x01000017: "PageDown", 0x01000020: "Shift", 0x01000021: "Control", 0x01000022: "Meta", 0x01000023: "Alt", 0x01001103: "AltGr", 0x01000024: "CapsLock", 0x01000025: "NumLock", 0x01000026: "ScrollLock", 0x01000030: "F1", 0x01000031: "F2", 0x01000032: "F3", 0x01000033: "F4", 0x01000034: "F5", 0x01000035: "F6", 0x01000036: "F7", 0x01000037: "F8", 0x01000038: "F9", 0x01000039: "F10", 0x0100003a: "F11", 0x0100003b: "F12", 0x0100003c: "F13", 0x0100003d: "F14", 0x0100003e: "F15", 0x0100003f: "F16", 0x01000040: "F17", 0x01000041: "F18", 0x01000042: "F19", 0x01000043: "F20", 0x01000044: "F21", 0x01000045: "F22", 0x01000046: "F23", 0x01000047: "F24", 0x01000048: "F25", 0x01000049: "F26", 0x0100004a: "F27", 0x0100004b: "F28", 0x0100004c: "F29", 0x0100004d: "F30", 0x0100004e: "F31", 0x0100004f: "F32", 0x01000050: "F33", 0x01000051: "F34", 0x01000052: "F35", 0x01000053: "Super_L", 0x01000054: "Super_R", 0x01000055: "Menu", 0x01000056: "Hyper_L", 0x01000057: "Hyper_R", 0x01000058: "Help", 0x01000059: "Direction_L", 0x01000060: "Direction_R", 0x20: "Space", 0x21: "Exclam", 0x22: "QuoteDbl", 0x23: "NumberSign", 0x24: "Dollar", 0x25: "Percent", 0x26: "Ampersand", 0x27: "Apostrophe", 0x28: "ParenLeft", 0x29: "ParenRight", 0x2a: "Asterisk", 0x2b: "Plus", 0x2c: "Comma", 0x2d: "Minus", 0x2e: "Period", 0x2f: "Slash", 0x30: "0", 0x31: "1", 0x32: "2", 0x33: "3", 0x34: "4", 0x35: "5", 0x36: "6", 0x37: "7", 0x38: "8", 0x39: "9", 0x3a: "Colon", 
        0x3b: "Semicolon",
        0x3c: "Less", 0x3d: "Equal", 0x3e: "Greater", 0x3f: "Question", 0x40: "At", 0x41: "A", 0x42: "B", 0x43: "C", 0x44: "D", 0x45: "E", 0x46: "F", 0x47: "G", 0x48: "H", 0x49: "I", 0x4a: "J", 0x4b: "K", 0x4c: "L", 0x4d: "M", 0x4e: "N", 0x4f: "O", 0x50: "P", 0x51: "Q", 0x52: "R", 0x53: "S", 0x54: "T", 0x55: "U", 0x56: "V", 0x57: "W", 0x58: "X", 0x59: "Y", 0x5a: "Z", 0x5b: "BracketLeft", 0x5c: "Backslash", 0x5d: "BracketRight", 0x5e: "AsciiCircum", 0x5f: "Underscore", 0x60: "QuoteLeft", 0x7b: "BraceLeft", 0x7c: "Bar", 0x7d: "BraceRight", 0x7e: "AsciiTilde", 0x0a0: "nobreakspace", 0x0a1: "exclamdown", 0x0a2: "cent", 0x0a3: "sterling", 0x0a4: "currency", 0x0a5: "yen", 0x0a6: "brokenbar", 0x0a7: "section", 0x0a8: "diaeresis", 0x0a9: "copyright", 0x0aa: "ordfeminine", 0x0ab: "guillemotleft", 0x0ac: "notsign", 0x0ad: "hyphen", 0x0ae: "registered", 0x0af: "macron", 0x0b0: "degree", 0x0b1: "plusminus", 0x0b2: "twosuperior", 0x0b3: "threesuperior", 0x0b4: "acute", 0x0b5: "mu", 0x0b6: "paragraph", 0x0b7: "periodcentered", 0x0b8: "cedilla", 0x0b9: "onesuperior", 0x0ba: "masculine", 0x0bb: "guillemotright", 0x0bc: "onequarter", 0x0bd: "onehalf", 0x0be: "threequarters", 0x0bf: "questiondown", 0x0c0: "Agrave", 0x0c1: "Aacute", 0x0c2: "Acircumflex", 0x0c3: "Atilde", 0x0c4: "Adiaeresis", 0x0c5: "Aring", 0x0c6: "AE", 0x0c7: "Ccedilla", 0x0c8: "Egrave", 0x0c9: "Eacute", 0x0ca: "Ecircumflex", 0x0cb: "Ediaeresis", 0x0cc: "Igrave", 0x0cd: "Iacute", 0x0ce: "Icircumflex", 0x0cf: "Idiaeresis", 0x0d0: "ETH", 0x0d1: "Ntilde", 0x0d2: "Ograve", 0x0d3: "Oacute", 0x0d4: "Ocircumflex", 0x0d5: "Otilde", 0x0d6: "Odiaeresis", 0x0d7: "multiply", 0x0d8: "Ooblique", 0x0d9: "Ugrave", 0x0da: "Uacute", 0x0db: "Ucircumflex", 0x0dc: "Udiaeresis", 0x0dd: "Yacute", 0x0de: "THORN", 0x0df: "ssharp", 0x0f7: "division", 0x0ff: "ydiaeresis", 0x01001120: "Multi_key", 0x01001137: "Codeinput", 0x0100113c: "SingleCandidate", 0x0100113d: "MultipleCandidate", 0x0100113e: "PreviousCandidate", 0x0100117e: "Mode_switch", 0x01001121: "Kanji", 0x01001122: "Muhenkan", 0x01001123: "Henkan", 0x01001124: "Romaji", 0x01001125: "Hiragana", 0x01001126: "Katakana", 0x01001127: "Hiragana_Katakana", 0x01001128: "Zenkaku", 0x01001129: "Hankaku", 0x0100112a: "Zenkaku_Hankaku", 0x0100112b: "Touroku", 0x0100112c: "Massyo", 0x0100112d: "Kana_Lock", 0x0100112e: "Kana_Shift", 0x0100112f: "Eisu_Shift", 0x01001130: "Eisu_toggle", 0x01001131: "Hangul", 0x01001132: "Hangul_Start", 0x01001133: "Hangul_End", 0x01001134: "Hangul_Hanja", 0x01001135: "Hangul_Jamo", 0x01001136: "Hangul_Romaja", 0x01001138: "Hangul_Jeonja", 0x01001139: "Hangul_Banja", 0x0100113a: "Hangul_PreHanja", 0x0100113b: "Hangul_PostHanja", 0x0100113f: "Hangul_Special", 0x01001250: "Dead_Grave", 0x01001251: "Dead_Acute", 0x01001252: "Dead_Circumflex", 0x01001253: "Dead_Tilde", 0x01001254: "Dead_Macron", 0x01001255: "Dead_Breve", 0x01001256: "Dead_Abovedot", 0x01001257: "Dead_Diaeresis", 0x01001258: "Dead_Abovering", 0x01001259: "Dead_Doubleacute", 0x0100125a: "Dead_Caron", 0x0100125b: "Dead_Cedilla", 0x0100125c: "Dead_Ogonek", 0x0100125d: "Dead_Iota", 0x0100125e: "Dead_Voiced_Sound", 0x0100125f: "Dead_Semivoiced_Sound", 0x01001260: "Dead_Belowdot", 0x01001261: "Dead_Hook", 0x01001262: "Dead_Horn", 0x01001263: "Dead_Stroke", 0x01001264: "Dead_Abovecomma", 0x01001265: "Dead_Abovereversedcomma", 0x01001266: "Dead_Doublegrave", 0x01001267: "Dead_Belowring", 0x01001268: "Dead_Belowmacron", 0x01001269: "Dead_Belowcircumflex", 0x0100126a: "Dead_Belowtilde", 0x0100126b: "Dead_Belowbreve", 0x0100126c: "Dead_Belowdiaeresis", 0x0100126d: "Dead_Invertedbreve", 0x0100126e: "Dead_Belowcomma", 0x0100126f: "Dead_Currency", 0x01001280: "Dead_a", 0x01001281: "Dead_A", 0x01001282: "Dead_e", 0x01001283: "Dead_E", 0x01001284: "Dead_i", 0x01001285: "Dead_I", 0x01001286: "Dead_o", 0x01001287: "Dead_O", 0x01001288: "Dead_u", 0x01001289: "Dead_U", 0x0100128a: "Dead_Small_Schwa", 0x0100128b: "Dead_Capital_Schwa", 0x0100128c: "Dead_Greek", 0x01001290: "Dead_Lowline", 0x01001291: "Dead_Aboveverticalline", 0x01001292: "Dead_Belowverticalline", 0x01001293: "Dead_Longsolidusoverlay", 0x01000061: "Back", 0x01000062: "Forward", 0x01000063: "Stop", 0x01000064: "Refresh", 0x01000070: "VolumeDown", 0x01000071: "VolumeMute", 0x01000072: "VolumeUp", 0x01000073: "BassBoost", 0x01000074: "BassUp", 0x01000075: "BassDown", 0x01000076: "TrebleUp", 0x01000077: "TrebleDown", 0x01000080: "MediaPlay", 0x01000081: "MediaStop", 0x01000082: "MediaPrevious", 0x01000083: "MediaNext", 0x01000084: "MediaRecord", 0x1000085: "MediaPause", 0x1000086: "MediaTogglePlayPause", 0x01000090: "HomePage", 0x01000091: "Favorites", 0x01000092: "Search", 0x01000093: "Standby", 0x01000094: "OpenUrl", 0x010000a0: "LaunchMail", 0x010000a1: "LaunchMedia", 0x010000a2: "Launch0", 0x010000a3: "Launch1", 0x010000a4: "Launch2", 0x010000a5: "Launch3", 0x010000a6: "Launch4", 0x010000a7: "Launch5", 0x010000a8: "Launch6", 0x010000a9: "Launch7", 0x010000aa: "Launch8", 0x010000ab: "Launch9", 0x010000ac: "LaunchA", 0x010000ad: "LaunchB", 0x010000ae: "LaunchC", 0x010000af: "LaunchD", 0x010000b0: "LaunchE", 0x010000b1: "LaunchF", 0x0100010e: "LaunchG", 0x0100010f: "LaunchH", 0x010000b2: "MonBrightnessUp", 0x010000b3: "MonBrightnessDown", 0x010000b4: "KeyboardLightOnOff", 0x010000b5: "KeyboardBrightnessUp", 0x010000b6: "KeyboardBrightnessDown", 0x010000b7: "PowerOff", 0x010000b8: "WakeUp", 0x010000b9: "Eject", 0x010000ba: "ScreenSaver", 0x010000bb: "WWW", 0x010000bc: "Memo", 0x010000bd: "LightBulb", 0x010000be: "Shop", 0x010000bf: "History", 0x010000c0: "AddFavorite", 0x010000c1: "HotLinks", 0x010000c2: "BrightnessAdjust", 0x010000c3: "Finance", 0x010000c4: "Community", 
        0x010000c5: "AudioRewind", 0x010000c6: "BackForward", 0x010000c7: "ApplicationLeft", 0x010000c8: "ApplicationRight", 0x010000c9: "Book", 0x010000ca: "CD", 0x010000cb: "Calculator", 0x010000cc: "ToDoList", 0x010000cd: "ClearGrab", 0x010000ce: "Close", 0x010000cf: "Copy", 0x010000d0: "Cut", 0x010000d1: "Display", 0x010000d2: "DOS", 0x010000d3: "Documents", 0x010000d4: "Excel", 0x010000d5: "Explorer", 0x010000d6: "Game", 0x010000d7: "Go", 0x010000d8: "iTouch", 0x010000d9: "LogOff", 0x010000da: "Market", 0x010000db: "Meeting", 0x010000dc: "MenuKB", 0x010000dd: "MenuPB", 0x010000de: "MySites", 0x010000df: "News", 0x010000e0: "OfficeHome", 0x010000e1: "Option", 0x010000e2: "Paste", 0x010000e3: "Phone", 0x010000e4: "Calendar", 0x010000e5: "Reply", 0x010000e6: "Reload", 
        0x010000e7: "RotateWindows", 0x010000e8: "RotationPB", 0x010000e9: "RotationKB", 0x010000ea: "Save", 0x010000eb: "Send", 0x010000ec: "Spell", 0x010000ed: "SplitScreen", 0x010000ee: "Support", 0x010000ef: "TaskPane", 0x010000f0: "Terminal", 0x010000f1: "Tools", 0x010000f2: "Travel", 0x010000f3: "Video", 0x010000f4: "Word", 0x010000f5: "Xfer", 0x010000f6: "ZoomIn", 0x010000f7: "ZoomOut", 0x010000f8: "Away", 0x010000f9: "Messenger", 0x010000fa: "WebCam", 0x010000fb: "MailForward", 0x010000fc: "Pictures", 0x010000fd: "Music", 0x010000fe: "Battery", 0x010000ff: "Bluetooth", 0x01000100: "WLAN", 0x01000101: "UWB", 0x01000102: "AudioForward", 0x01000103: "AudioRepeat", 0x01000104: "AudioRandomPlay", 0x01000105: "Subtitle", 0x01000106: "AudioCycleTrack", 0x01000107: "Time", 0x01000108: "Hibernate", 0x01000109: "View", 0x0100010a: "TopMenu", 0x0100010b: "PowerDown", 0x0100010c: "Suspend", 0x0100010d: "ContrastAdjust", 0x01000110: "TouchpadToggle", 0x01000111: "TouchpadOn", 0x01000112: "TouchpadOff", 0x01000113: "MicMute", 0x01000114: "Red", 0x01000115: "Green", 0x01000116: "Yellow", 0x01000117: "Blue", 0x01000118: "ChannelUp", 0x01000119: "ChannelDown", 0x0100011a: "Guide", 0x0100011b: "Info", 0x0100011c: "Settings", 0x0100011d: "MicVolumeUp", 0x0100011e: "MicVolumeDown", 0x01000120: "New", 0x01000121: "Open", 0x01000122: "Find", 0x01000123: "Undo", 0x01000124: "Redo", 0x0100ffff: "MediaLast", 0x01ffffff: "unknown", 0x01100004: "Call", 0x01100020: "Camera", 0x01100021: "CameraFocus", 0x01100000: "Context1", 0x01100001: "Context2", 0x01100002: "Context3", 0x01100003: "Context4", 0x01100006: "Flip", 0x01100005: "Hangup", 0x01010002: "No", 0x01010000: "Select", 0x01010001: "Yes", 0x01100007: "ToggleCallHangup", 0x01100008: "VoiceDial", 0x01100009: "LastNumberRedial", 0x01020003: "Execute", 0x01020002: "Printer", 0x01020005: "Play", 0x01020004: "Sleep", 0x01020006: "Zoom", 0x0102000a: "Exit", 0x01020001: "Cancel"
        })
        """
        super().keyPressEvent(event)
        key = event.key()
        key_modifiers = QApplication.keyboardModifiers()
        if (key == Qt.Key_K and key_modifiers == Qt.ControlModifier):
        # if (key == Qt.Key_Semicolon and key_modifiers == Qt.ControlModifier):
            self.process_word()
        elif (key == Qt.Key_M and key_modifiers == Qt.ControlModifier):
            self.process_fmus()

    def onLinesChanged(self):
        self.setMarginWidth(0, self.fontMetrics().width(str(self.lines())) + self.margin)

    def set_lexer(self, lex):
        self.setLexer(lex(self))

    def init(self):
        self.setUtf8(True)
        # lexer bikin background tulisan beda warna...
        # lexer = QsciLexerMarkdown(self)
        # lexer = QsciLexerPython(self)
        # self.setLexer(lexer)
        font = self.font() or QFont()
        font.setFamily("Consolas")
        font.setFixedPitch(True)
        font.setPointSize(13)
        self.setFont(font)
        self.setMarginsFont(font)
        self.fontmetrics = QFontMetrics(font)
        # lexer.setFont(font)

        self.setAutoCompletionCaseSensitivity(False)  # ignore case
        self.setAutoCompletionSource(QsciScintilla.AcsAll)
        # self.setAutoCompletionSource(QsciScintilla.AcsAPIs)
        self.setAutoCompletionThreshold(1)  # One character pops up completion
        # Sets whether the characters to the right of the autocompletion
        # will be overwritten when an autocompletion is selected.
        self.setAutoCompletionReplaceWord(True)
        # Select the behaviour of autocompletions when there is only a single
        # entry in the autocompletion list. The selection below sets that
        # when the autocompletion window will always be displayed.
        self.setAutoCompletionUseSingle(QsciScintilla.AcusNever)

        self.setAutoIndent(True)  # auto indent
        self.setBackspaceUnindents(True)
        self.setBraceMatching(self.StrictBraceMatch)
        self.setIndentationGuides(True)
        self.setIndentationsUseTabs(False)
        self.setIndentationWidth(4)
        self.setTabIndents(True)
        self.setTabWidth(4)
        self.setWhitespaceSize(1)
        self.setWhitespaceVisibility(self.WsVisible)
        # self.setWhitespaceForegroundColor(Qt.gray)
        self.setWrapIndentMode(self.WrapIndentFixed)
        self.setWrapMode(self.WrapWord)

        # fold
        # https://docs.huihoo.com/pyqt/QScintilla2/classQsciScintilla.html
        self.setFolding(self.BoxedTreeFoldStyle, 2)
        # self.setFoldMarginColors(QColor("#676A6C"), QColor("#676A6D"))

        self.setMarginWidth(0, self.fontmetrics.width(str(self.lines())) + self.margin)
        self.setMarginLineNumbers(0, True)
        # self.setMarginsBackgroundColor(QColor("gainsboro"))
        self.setMarginWidth(1, 0)
        self.setMarginWidth(2, 14) # folded area

        # Bind autocompletion hotkey Alt+/
        completeKey = QShortcut(QKeySequence(Qt.ALT + Qt.Key_Slash), self)
        completeKey.setContext(Qt.WidgetShortcut)
        completeKey.activated.connect(self.autoCompleteFromAll)

        # my_lexer = QsciLexerCPP()
        # api = QsciAPIs(my_lexer)
        # for ac in autocompletions['all']:
        #     print('autocomplete:', ac)
        #     api.add(ac)
        # api.prepare()
        # my_lexer.setAPIs(api)
        # self.setLexer(my_lexer)

        QShortcut(QKeySequence("Ctrl+S"), self, activated=lambda: self.save_file.emit(True))

    def get_selections(self):
        # Get the selection and store them in a list
        selections = []
        for i in range(self.SendScintilla(self.SCI_GETSELECTIONS)):
            selection = (
                self.SendScintilla(self.SCI_GETSELECTIONNSTART, i),
                self.SendScintilla(self.SCI_GETSELECTIONNEND, i)
            )
            # Add selection to list
            from_line, from_index = self.lineIndexFromPosition(selection[0])
            to_line, to_index = self.lineIndexFromPosition(selection[1])
            # selections.append((from_line, to_line))
            selections.append((from_line, from_index, to_line, to_index))

            # https://docs.huihoo.com/pyqt/QScintilla2/functions_w.html
            # self.wordAtLineIndex(from_line, from_index)
            # self.wordAtLineIndex(from_line, 0) # dari awal baris

        selections.sort()
        # Return selection list
        return selections

    def get_first_selection_only(self):
        selections = self.get_selections()
        if selections == None:
            return None
        return selections[0]  # nilai (x,y) dimana kita hanya pake x = from_line, krn y pasti sama dg x utk no-selection

    def process_word(self):
        """
        TODO:
        sementara kita hanya proses dari awal baris ke akhir baris
        perlu juga bisa multiple line dari fromline ke toline
        krn agar bisa run fmus
        jadi hrs terima fromline dan toline selain fromindex dan toindex
        jadi mestinya bisa:
        barismulai, kolommulai, barisakhir, kolomakhir = self.get_first_selection_only()
        """
        baris, kolom, _, _ = self.get_first_selection_only()
        bariskata = self.wordAtLineIndex(baris, kolom)  # kata under cursor gak berguna krn skip puncs
        start = self.positionFromLineIndex(baris, 0)  # dari awal baris
        end = self.positionFromLineIndex(baris, kolom)  # sampai cursor di baris yg sama
        bariskalimat = self.text(start, end)
        # print(f"""[process_word] baris start {start}, end {end}, baris (ini yg kita ambil) {baris}, kolom {kolom}
        # we should be processing [{bariskata}] dan baris kalimat [{bariskalimat}]
        # """)
        inputset = set(bariskalimat)
        checkset = set([chr(n) for n in list(range(ord('0'),ord('9')+1))] + [',', '-'])
        if inputset.issubset(checkset):
            maxbaris = 100
            # numbres = line_number_expression(maxbaris, bariskalimat, line_startat_one=True, inclusive_end=True)
            numbres = line_number_expression(maxbaris, bariskalimat)
            # print(f'line_number_expression found in {bariskalimat} => {numbres}')
            self.line_numbers_request.emit((numbres, baris))
        else:
            # print('repling:', bariskalimat)
            self.replrequest.emit((bariskalimat, baris))

    def process_fmus(self):
        """
        """
        barismulai, kolommulai, barisakhir, kolomakhir = self.get_first_selection_only()
        start = self.positionFromLineIndex(barismulai, kolommulai)
        end = self.positionFromLineIndex(barisakhir, kolomakhir)
        bariskalimat = self.text(start, end)
        self.fmusrequest.emit(bariskalimat, barismulai, kolommulai, barisakhir, kolomakhir)


class CreatorWidget(QWidget):

    def __init__(self, filepath=None, language=None, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.dirpath = get_cwd()
        self.filepath = filepath

        if not self.filepath:
            if self.property('filepath'):
                self.filepath = self.property('filepath')
                self.dirpath = self.property('dirpath')
            elif self.property('dirpath'):
                self.dirpath = self.property('dirpath')
        
        self.status_button = QPushButton('Status')
        self.creator = CreatorEditor() # dipanggil di setup 
        # self.set_autocompletion('all')

        if filepath and not language:
            self.set_language_by_filepath(filepath)
        elif not language:
            # self.setter_for_language('py')
            self.change_language_and_tabs('py')

        if self.filepath:
            self.dirpath = os.path.dirname(self.filepath)
            # perlu set editor?
            self.creator.setText(file_content(self.filepath))

        self.initUI()
        self.init_thread()
        self.creator.setFocus()

    def set_filepath_dirpath(self, filepath=None, dirpath=None):
        # print(f"set_filepath_dirpath, filepath {filepath}, dirpath {dirpath}.")
        if filepath:
            self.filepath = filepath
            self.set_language_by_filepath(filepath)
            # jk ada file baru maka load di editor, knp kadang gak terload jk pindah2 file?
            self.openFileOnStart(self.filepath)
        if dirpath:
            self.dirpath = dirpath
            if not filepath:
                self.filepath = None
                # jangan lupa kosongkan editor krn bisa jadi sebelumnya buka file, skrg buka folder
                self.creator.setText('')
                self.filepath_label.setText('Saved') # default di awal
        elif filepath:
            # jk set file tapi tdk set dir, maka set dirpath ke dir dari file
            # terkadang ini jadi reassign self.dirpath, jk misal kasus bikin file quick
            self.dirpath = os.path.dirname(self.filepath)

    def run_by_language(self, language='py'):
        if language == 'py':
            self.run_python()
        elif language == 'go':
            self.run_python('go', ['run'])
        elif language == 'java':
            self.run_java()
        elif language == 'js':
            self.run_python('node')
        elif language == 'pl':
            self.run_python('perl')
        elif language == 'php':
            self.run_python('php')
        elif language == 'rb':
            self.run_python('ruby')
        elif language == 'scala':
            only_basename = os.path.basename(self.filepath)
            without_ext = os.path.splitext(only_basename)[0]  # scalac jk dg path: Exception in thread "main" java.lang.IllegalArgumentException: name
            self.run_python(r'C:\bin\scala\bin\scalac.bat')
            self.run_python(r'C:\bin\scala\bin\scala.bat', ['-nc'], filepath=without_ext)
        elif language == 'ts':
            self.run_python('deno', ['run'])
        else:
            print(f'dont know how to run [{language}]')

    def run_current_filepath_by_language(self):
        if not self.filepath:
            print(f'self.filepath not set')
            return
        language = get_extension(self.filepath)
        if language:
            self.run_by_language(language)

    def run_kotlin(self):
        unset_filepath = False  # apa self.filepath belum terset? berarti perlu temp name
        if not self.filepath:
            self.filepath = os.path.join(tempdir(), 'hapus_' + timestamp())
            file_write(self.filepath, self.creator.text())
            unset_filepath = True
        filename_ext = os.path.basename(self.filepath)
        filename, ext = os.path.splitext(filename_ext)
        result = subprocess.run(f'kotlinc {filename_ext} -include-runtime -d {filename}.jar'.split(), capture_output=True, text=True)
        self.stdout.appendPlainText(result.stdout)
        self.stderr.appendPlainText(result.stderr)
        result = subprocess.run(f'java -jar {filename}.jar'.split(), capture_output=True, text=True)
        self.stdout.appendPlainText(result.stdout)
        self.stderr.appendPlainText(result.stderr)
        if unset_filepath:
            self.filepath = ''  # spy bisa ganti content

    def run_java(self):
        unset_filepath = False  # apa self.filepath belum terset? berarti perlu temp name
        if not self.filepath:
            self.filepath = os.path.join(tempdir(), 'hapus_' + timestamp())
            file_write(self.filepath, self.creator.text())
            unset_filepath = True
        filename_ext = os.path.basename(self.filepath)
        filename, ext = os.path.splitext(filename_ext)
        result = subprocess.run(f'javac {self.filepath}'.split(), capture_output=True, text=True)
        self.stdout.appendPlainText(result.stdout)
        self.stderr.appendPlainText(result.stderr)
        result = subprocess.run(f'java {filename}'.split(), capture_output=True, text=True)
        self.stdout.appendPlainText(result.stdout)
        self.stderr.appendPlainText(result.stderr)
        if unset_filepath:
            self.filepath = ''  # spy bisa ganti content

    def run_python(self, main_command='python', additional_args_before_filepath = [], filepath=None):
        if not filepath:
            # bisa override nama file (misal tanpa extension)
            filepath = self.filepath
        filepath = os.path.normpath(filepath)
        commands = [main_command] + additional_args_before_filepath + [filepath]
        unset_filepath = False  # apa self.filepath belum terset? misal dari modify editor tapi belum save, berarti perlu temp name
        if not self.filepath:
            self.filepath = os.path.join(tempdir(), 'hapus_' + timestamp())
            file_write(self.filepath, self.creator.text())
            unset_filepath = True
        try:
            result = subprocess.run(commands, capture_output=True, text=True)
            self.stdout.appendPlainText(result.stdout)
            self.stderr.appendPlainText(result.stderr)
            self.stdout_stderr_widget.setVisible(True)
        except Exception as err:
            print(f"""[run_python] => {err}
            cwd = {os.getcwd()}
            self.filepath = {self.filepath}
            commands = {commands}
            """)
        if unset_filepath:
            self.filepath = ''  # spy bisa ganti content

    def set_autocompletion(self, language):
        if not language in autocompletions:
            return
        if not hasattr(self, 'creator'):  # di awal belum ada self.creator
            return
        my_lexer = QsciLexerCPP()
        api = QsciAPIs(my_lexer)
        # Set the editor's lexer
        self.creator.setLexer(my_lexer)
        # Register an image that will be displayed with an autocompletion
        # autocompletion_image = QPixmap("marker_image.png")
        # self.creator.registerImage(1, autocompletion_image)
        # Create a list of autocompletions
        # autocompletions = [
        #     "test_autocompletion",
        #     "autocompletion_with_image?1",
        #     "another_autocompletion",
        #     "subtract?1(int arg_1, float arg_2) Subtract function",
        #     "entry_that_will_be_removed_later"
        # ]
        # Add the functions to the api
        print(f"daftar completions {autocompletions[language]} utk bahasa {language}.")
        for ac in autocompletions[language]:
            api.add(ac)
        api.prepare()

    def setter_for_language(self, language):
        """
        gunakan ini utk set language dan label pada button
        """
        self.language = language
        self.status_button.setText(self.language)
        # coba set completion di sini, gunakan lexer satu python saja
        # autocompletions
        # self.set_autocompletion(language)

    def set_language_by_filepath(self, filepath):
        ext = get_extension(filepath)
        # print(f"[set_language_by_filepath] filepath = {filepath} => ext {ext}.")
        if ext in LANGUAGES:
            # self.setter_for_language(ext)
            self.change_language_and_tabs(ext)
        # else:
        #     print(f"[creator][set_language_by_filepath] language '{ext}' tidak ada dalam  daftar <rootdir>/providers/languages/*: {LANGUAGES}.")

    def set_language_by_current_filepath(self):
        self.set_language_by_filepath(self.filepath)

    def set_language(self, language):
        if language in LANGUAGES:
            # self.setter_for_language(language)
            self.change_language_and_tabs(language)

    # lexer_menu.addAction(label, functools.partial(self.set_lexer_and_language, (label, lexerobj)))
    # lexer_menu.addAction(label, functools.partial(self.creator.set_lexer, lexerobj))
    def set_lexer_and_language(self, tuple_label_lexer):
        lang, lexerobj = tuple_label_lexer
        self.creator.set_lexer(lexerobj)
        self.setter_for_language(lang)

    def change_language_and_tabs(self, language):
        self.setter_for_language(language)
        self.tabs = []
        self.tabwidgets = []
        if self.language in bahasa_filepaths:
            self.tabs = get_daftar(bahasa_filepaths[self.language])
        else:
            print(f"{self.language} tidak ada dalam daftar: {bahasa_filepaths} [gui.system.searcher.widgets.common.py:bahasa_filepaths].")

        # self.helper_tab = QTabWidget(self)
        # self.helper_tab.setTabPosition(QTabWidget.East)
        # bersihkan tab utk tulis ulang
        if not hasattr(self, 'helper_tab'): # di awal __init__ wkt akses change_language_and_tabs, belum ada self.helper_tab
            return

        for i in range(self.helper_tab.count()):
            self.helper_tab.removeTab(i)

        for baris_entry in self.tabs:
            content = get_definition_double_entry_aware(bahasa_filepaths[self.language], baris_entry)
            helper = HelperEditor(content)
            # nama bs panjang, max 25 chars
            self.helper_tab.addTab(helper, baris_entry[:25])
            self.tabwidgets.append(helper)

    def openFile(self, path=None):
        if not path:
            path, _ = QFileDialog.getOpenFileName(self, "Open File", self.dirpath, "Python Files (*.py);; all Files (*)")
        if path:
            self.openFileOnStart(path)

    def openFileOnStart(self, path=None):
        try:
            content = file_content(path)
            self.creator.setText(content)
            self.filepath = path
            self.filepath_label.setText(self.filepath)
        except Exception as err:
            print(err)

    def ganti_tabspace(self):
        curr = self.tabspace_control.currentIndex()
        if curr == 0:
            self.creator.setIndentationsUseTabs(True)
            self.creator.setTabWidth(8)
        elif curr == 1:
            self.creator.setIndentationsUseTabs(False)
            self.creator.setTabWidth(2)
        elif curr == 2:
            self.creator.setIndentationsUseTabs(False)
            self.creator.setTabWidth(4)

    def screensize(self):
        screen_geometry = QDesktopWidget().screenGeometry(-1)
        self.screenw = screen_geometry.width()
        self.screenh = screen_geometry.height()

    def create_edit_file_quick(self):
        filename = self.quickedit_menu_control.text().strip()
        # dirpath dari control.property('dirpath')
        # dirpath = self.quickedit_menu_control.property('dirpath')
        # if filename and dirpath:
        #     filepath = os.path.join(dirpath, filename)
        #     print('quick create file:', filepath)
        #     self.showedit = ShowEditWindow(filepath, title=filepath, initial_text='')
        #     self.showedit.show()
        if self.dirpath:
            # self.filepath = os.path.join(self.dirpath, filename)
            # self.openFileOnStart(self.filepath)
            self.set_filepath_dirpath(filepath=os.path.join(self.dirpath, filename))

    def initUI(self):
        self.screensize()
        self.main_layout = QVBoxLayout()

        # https://doc.qt.io/qt-6/qkeysequence.html
        self.openAct = QAction("&Open", self, shortcut=QKeySequence.Open, statusTip="open file", triggered=self.openFile)
        self.openAct.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogOpenButton))

        self.saveAsAct = QAction("Save &as", self, shortcut=QKeySequence('Ctrl+G'), statusTip="save as", triggered=self.save_as)
        self.saveAsAct.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogSaveButton))

        toolbar = QHBoxLayout()

        self.filepath_label = QLabel(self.filepath if self.filepath else 'Saved') # QPushButton("Saved")        
        self.prev = QAction('prev')
        self.prev.setShortcut(QKeySequence('Ctrl+P'))
        self.next = QAction('next')
        self.next.setShortcut(QKeySequence('Ctrl+N'))
        self.helper_button_action = QAction('helper')
        self.helper_button_action.setCheckable(True)
        self.helper_button_action.setShortcut(QKeySequence('Ctrl+H'))
        self.status_button_action = QAction('status')
        self.status_button_action.setCheckable(True)
        self.status_button_action.setShortcut(QKeySequence('Ctrl+I'))
        status_menu = QMenu('Status', self.status_button)
        self.action_run_python = QAction('Run Python')
        self.action_run_python.triggered.connect(self.run_python)
        self.action_run_python.setShortcut(QKeySequence("Ctrl+R"))

        # 11 sep 2022, tambah menu quick create file
        self.quickedit_menu = QMenu('Quick create file', self)
        self.quickedit_menu_control = QLineEdit(self.quickedit_menu)
        self.quickedit_menu_control.setFont(QFont("Verdana", 16))
        self.quickedit_menu_control.setStyleSheet('background-color: oldlace; height: 32px;')
        self.quickedit_menu_action = QWidgetAction(self.quickedit_menu)
        self.quickedit_menu_action.setDefaultWidget(self.quickedit_menu_control)
        self.quickedit_menu.addAction(self.quickedit_menu_action)
        self.quickedit_menu_control.returnPressed.connect(self.create_edit_file_quick)


        status_menu.addAction(self.openAct)
        status_menu.addAction(self.saveAsAct)
        status_menu.addAction(self.action_run_python)
        status_menu.addAction('Run by language', self.run_current_filepath_by_language)
        status_menu.addAction('Set language/helper by current file', self.set_language_by_current_filepath)
        status_menu.addMenu(self.quickedit_menu)
        status_menu.addAction(self.prev)
        status_menu.addAction(self.next)
        status_menu.addAction(self.helper_button_action)
        status_menu.addAction(self.status_button_action)
        self.tabspace_control = QComboBox(status_menu)
        self.tabspace_control.addItems(['tab', 'space 2', 'space 4'])
        self.tabspace_control.currentIndexChanged.connect(self.ganti_tabspace)
        tabspace_action = QWidgetAction(status_menu)
        tabspace_action.setDefaultWidget(self.tabspace_control)
        status_menu.addAction(tabspace_action)
        self.status_button.setMenu(status_menu)

        self.lexer_button = QPushButton('lexers', self)
        lexer_menu = QMenu(self.lexer_button)
        for label, lexerobj in sorted(LEXERS.items()):
            # lexer_menu.addAction(label, functools.partial(self.creator.set_lexer, lexerobj))
            lexer_menu.addAction(label, functools.partial(self.set_lexer_and_language, (label, lexerobj)))
        self.lexer_button.setMenu(lexer_menu)

        # add buttons to layout
        toolbar.addWidget(self.status_button)
        toolbar.addWidget(self.filepath_label)
        toolbar.addWidget(self.lexer_button)
        toolbar.addStretch(1)
        toolbar_widget = QWidget()
        toolbar_widget.setLayout(toolbar)
        toolbar_widget.setStyleSheet('background-color: blanchedalmond;')
        # toolbar_widget.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        # toolbar_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # toolbar_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        # toolbar_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        # toolbar_widget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        # toolbar_widget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        toolbar_widget.setFixedHeight(48)
        splitter_atas_tengah_bawah = QSplitter(Qt.Vertical)

        # editor utama dan status group dalam 1 splitter...default status akan hide

        self.stdout_stderr_widget = QGroupBox('Status')
        stdout_layout = QHBoxLayout(self.stdout_stderr_widget)
        # self.stdout = QTextBrowser()
        self.stdout = QPlainTextEdit()
        self.stdout.setStyleSheet('background-color: darkseagreen; font-size: 14px; font-family: MonoLisa, Terminal, Inconsolatas, Noto Sans, Open Sans;')
        # self.stderr = QTextBrowser()
        self.stderr = QPlainTextEdit()
        self.stderr.setStyleSheet('background-color: lightcoral; font-size: 14px; font-family: MonoLisa, Terminal, Inconsolatas, Noto Sans, Open Sans;')
        stdout_layout.addWidget(self.stdout)
        stdout_layout.addWidget(self.stderr)
        # self.stdout_stderr_widget.hide()
        editor_status_splitter = QSplitter(Qt.Vertical)
        editor_status_splitter.addWidget(self.creator)
        editor_status_splitter.addWidget(self.stdout_stderr_widget)

        self.helper_tab = QTabWidget(self)
        self.helper_tab.setTabPosition(QTabWidget.East)
        splitter_atas_tengah_bawah.addWidget(self.helper_tab)
        splitter_atas_tengah_bawah.addWidget(toolbar_widget)
        # splitter_atas_tengah_bawah.addWidget(self.creator)
        splitter_atas_tengah_bawah.addWidget(editor_status_splitter)
        self.main_layout.addWidget(splitter_atas_tengah_bawah)
        splitter_atas_tengah_bawah.handle(1).setStyleSheet('background-color: darkgoldenrod; border: 3px solid darksalmon;')
        splitter_atas_tengah_bawah.handle(2).setStyleSheet('background-color: darkgoldenrod; border: 3px solid darksalmon;')

        # self.footer = QLabel(self.information)
        self.footer = QLabel('__________________________________________________________________________________________________________________________________________________________________________')
        self.footer.setStyleSheet('font-family: Consolas;')
        self.main_layout.addWidget(self.footer)

        slider = QSlider(Qt.Vertical)
        slider.setFixedHeight(self.screenh - 60)
        wrapper = QHBoxLayout()
        wrapper.addLayout(self.main_layout)
        wrapper.addWidget(slider)
        # self.setLayout(self.main_layout)
        self.setLayout(wrapper)

        # signals
        self.creator.textChanged.connect(lambda: self.unsaving_creator())
        # self.creator.textChanged.connect(lambda: self.filepath_label.setText('*Unsaved'))
        self.creator.save_file.connect(lambda: self.saving_creator())
        # self.prev.clicked.connect(self.previous_tab)
        self.prev.triggered.connect(self.previous_tab)
        # self.next.clicked.connect(self.next_tab)
        self.next.triggered.connect(self.next_tab)
        self.helper_button_action.toggled.connect(self.helper_tab.setVisible)
        self.status_button_action.toggled.connect(self.stdout_stderr_widget.setVisible)
        # self.helper_button_action.setChecked(False)
        # self.status_button_action.setChecked(False)
        self.helper_tab.setVisible(False)
        self.stdout_stderr_widget.setVisible(False)
        self.creator.line_numbers_request.connect(self.handle_request_copy_line_numbers)
        self.creator.replrequest.connect(self.handle_replrequest)  # ctrl k
        self.creator.fmusrequest.connect(self.handle_fmusrequest)  # ctrl m

        self.creator_repl_line = None

        QShortcut(QKeySequence("Ctrl+2"), self, activated=lambda: self.helper_tab.currentWidget().setFocus())
        QShortcut(QKeySequence("Ctrl+1"), self, activated=lambda: self.creator.setFocus())

    def unsaving_creator(self):
        # print("unsaving")
        label = '*' + (self.filepath if self.filepath else 'Unsaved')
        self.filepath_label.setText(label)

    def saving_creator(self):
        content = self.creator.text()
        if self.filepath:
            # di line yg termodify selalu hasilkan extra newline            
            file_write(self.filepath, content)
        else:
            self.filepath, ok = QFileDialog.getSaveFileName(self, 'Save File', directory=self.dirpath)
            if ok:
                file_write(self.filepath, content)
        label = self.filepath if self.filepath else 'Saved'
        self.filepath_label.setText(label)

    def save_as(self):
        content = self.creator.text()
        # self.filepath, ok = QFileDialog.getSaveFileName(self, 'Save File as', self.filepath, directory=self.dirpath)
        # reassign self.filepath
        self.filepath, ok = QFileDialog.getSaveFileName(self, 'Save File as', self.filepath)
        if ok:
            file_write(self.filepath, content)
        label = self.filepath if self.filepath else 'Saved'
        self.filepath_label.setText(label)

    def previous_tab(self):
        cur = self.helper_tab.currentIndex()
        self.helper_tab.setCurrentIndex((cur - 1) % self.helper_tab.count())

    def next_tab(self):
        cur = self.helper_tab.currentIndex()
        self.helper_tab.setCurrentIndex((cur + 1) % self.helper_tab.count())

    def init_thread(self):
        self.subscriber = RedisSubscriber()
        self.subscriber.incomingData.connect(self.incomingData)
        self.subscriber.start()

    def incomingData(self, data):
        # print('[creator incomingData]', str(data), 'apa ada line?', self.creator_repl_line)
        pengganti = str(data)
        if self.creator_repl_line is not None:
            self.select_baris(self.creator_repl_line)
            self.creator.replaceSelectedText(pengganti)

    def handle_fmusrequest(self, content, baris, kolom, baris2, kolom2):
        if not content.endswith('\n'):
            content += '\n'
        run_fmus_for_content_in_thread(content, dirpath=self.dirpath)

    def handle_replrequest(self, tuple_isibaris_currentline):
        isibaris, self.creator_repl_line = tuple_isibaris_currentline
        # currentline dipake utk replace content dari self.creator stlh dapat jawaban dari redis server
        redis_publish(isibaris, savedconn(0), channel=CREATOR_CHANNEL_REQUEST)

    def handle_request_copy_line_numbers(self, tuple_daftar_baris_currentline):
        """
        simple grammar utk line number expression
        1-3
        1-3,7,9-10
        5-~
        """
        daftar_baris, currentline = tuple_daftar_baris_currentline
        # current_content = self.helper_tab.currentWidget().text()
        current_helper = self.helper_tab.currentWidget()
        total = current_helper.lines()
        # print('terima request daftar baris', daftar_baris, 'sedangkan content lines berjumlah:', total)
        terima = []
        for baris in daftar_baris:
            if baris < total:
                ambil = current_helper.text(baris)
                print(f"[{ambil}]")
                terima.append(ambil)
        # replace baris currentline
        pengganti = ''.join(terima)
        self.select_baris(currentline)
        self.creator.replaceSelectedText(pengganti)

    def select_baris(self, currentline):
        last_line = currentline
        if last_line == self.creator.lines() - 1: # baris terakhir di editor
            to_index = len(self.creator.text(currentline))
        else:
            to_index = len(self.creator.text(currentline))-1
        # Set the selection from the beginning of the cursor line
        # to the end of the last selection line
        self.creator.setSelection(currentline, 0, currentline, to_index)


background_image_stylesheet = '''
CreatorWidget {
    border-image: url("bg.jpg");
    background-repeat: no-repeat; 
    background-position: center;
}
'''


def main():
    app = QApplication([])
    wnd = CreatorWidget()
    wnd.setStyleSheet(background_image_stylesheet)
    wnd.show()
    wnd.resize(800, 600)
    wnd.setWindowTitle('judul2an')
    QShortcut(QKeySequence("Ctrl+Q"), wnd, activated=lambda: qApp.quit())
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
