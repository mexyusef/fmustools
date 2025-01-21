# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

"""
self.internal_logger = QWidget()
self.internal_logger.setAttribute(Qt.WA_TranslucentBackground, True)
self.internal_logger.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
self.note = YellowNote()
stylesheet = "QTextBrowser{border: none; font: 14pt "Consolas"; background-color: #5aff5a; border-radius: 10px;}"
self.note.setupUi(self.internal_logger, stylesheet)
"""

note_stylesheet = """
#frame_buttom{
    background-color: rgb(255, 247, 209);
    
}
QTextBrowser{
    border: none;
    font: 12pt "Verdana";
    background-color: rgb(255, 247, 209);
    border-radius: 10px;
}
#frame_title{
    background-color: rgb(255, 242, 171);
}
#frame{
    border: none;
    border-radius: 10px;
}
QPushButton{
    border:none;
}
QPushButton:hover, QPushButton:checked{
    background: rgb(237, 230, 194);
}
"""

initial_html = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
<head>
<meta name="qrichtext" content="1" />
<style type="text/css">
p, li { white-space: pre-wrap; }
</style>
</head>
<body style=" font-family:'MingLiU-ExtB'; font-size:14pt; font-weight:400; font-style:normal;">
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<br />
</p>
</body>
</html>"""


import os, sys
envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
from dotenv import load_dotenv
load_dotenv(envfile)
schnelldir = os.environ['ULIBPY_BASEDIR']
sidoarjodir = os.environ['ULIBPY_ROOTDIR']
sys.path.extend([sidoarjodir, schnelldir])

from schnell.app.quick.dahsyater import provider_to_location
provider_to_location_keys = sorted(list(provider_to_location.keys()) [::-1])
dahsyater_project_list = '\n'.join(provider_to_location_keys)


class NoteBrowser(QWidget):

    def __init__(self, content=None, parent=None):
        super().__init__(parent)
        if content:
            self.content = content
        else:
            # content default ambil dari dahsyater code
            contents = []
            for project in provider_to_location_keys:
                fungsi = provider_to_location[project]
                lengkap = f"{fungsi.__module__}.{fungsi.__name__}"
                contents.append(f"{project}\n\t{lengkap}\n\n")
            self.content = '\n'.join(contents)

        self.setupUi()

    def setupUi(self):
        self.setObjectName("NoteBrowser")
        # self.resize(396, 400)
        self.setStyleSheet(note_stylesheet)

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame_outer = QFrame(self)
        self.frame_outer.setStyleSheet("")
        self.frame_outer.setFrameShape(QFrame.NoFrame)
        self.frame_outer.setFrameShadow(QFrame.Raised)
        self.frame_outer.setObjectName("frame_outer")

        self.layout_editor = QVBoxLayout(self.frame_outer)
        self.layout_editor.setContentsMargins(0, 0, 0, 0)
        self.layout_editor.setSpacing(0)
        self.layout_editor.setObjectName("layout_editor")

        self.textBrowser = QTextBrowser(self.frame_outer)

        font = QFont()
        # font.setFamily("MingLiU-ExtB")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setReadOnly(True)
        # https://stackoverflow.com/questions/54875284/scrollbar-to-always-show-the-bottom-of-a-qtextbrowser-streamed-text
        # self.setLineWrapMode(QTextEdit.NoWrap)
        self.textBrowser.setObjectName("textBrowser")

        self.layout_editor.addWidget(self.textBrowser)

        # self.frame_buttom = QFrame(self.frame_outer)
        # self.frame_buttom.setMinimumSize(QtCore.QSize(0, 48))
        # # self.frame_buttom.setStyleSheet("\n""")
        # self.frame_buttom.setFrameShape(QFrame.StyledPanel)
        # self.frame_buttom.setFrameShadow(QFrame.Raised)
        # self.frame_buttom.setObjectName("frame_buttom")

        # # self.horizontalLayout_3.addWidget(self.frame_grip, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        # self.layout_editor.addWidget(self.frame_buttom)
        self.verticalLayout.addWidget(self.frame_outer)
        self.setWindowTitle("Form")
        self.textBrowser.setHtml(initial_html)
        # self.textBrowser.setPlaceholderText(palsu_contents)
        self.textBrowser.setText(self.content)
        # self.retranslateUi(self)
        # QtCore.QMetaObject.connectSlotsByName(self)

    # def retranslateUi(self, self):
    #     _translate = QtCore.QCoreApplication.translate
    #     self.setWindowTitle(_translate("Note", "Form"))
    #     self.textBrowser.setHtml(_translate("Note", initial_html))
    #     self.textBrowser.setPlaceholderText(_translate("Note", "output goes here..."))

    def setText(self, text, is_markdown):
        if is_markdown:
            self.textBrowser.setMarkdown(text)
        else:
            self.textBrowser.setText(text)

    def appendText(self, text):
        """
        https://stackoverflow.com/questions/54875284/scrollbar-to-always-show-the-bottom-of-a-qtextbrowser-streamed-text
        """
        # horScrollBar = self.textBrowser.horizontalScrollBar()
        # verScrollBar = self.textBrowser.verticalScrollBar()
        # scrollIsAtEnd = verScrollBar.maximum() - verScrollBar.value() <= 10
        self.textBrowser.append(text)
        # if scrollIsAtEnd:
        #     verScrollBar.setValue(verScrollBar.maximum()) # Scrolls to the bottom
        #     horScrollBar.setValue(0) # scroll to the left

    def show_and_print(self, text, is_markdown=True):
        # print('my note, setting text:', text)
        self.setText(text, is_markdown=is_markdown)
        if not self.textBrowser.isVisible():
            self.textBrowser.show()

# def main():
#     app = QApplication([])
#     # set_theme(app)
#     ex = NoteBrowser()
#     ex.show()
#     # ex.setStyleSheet(background_image_stylesheet)
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()

