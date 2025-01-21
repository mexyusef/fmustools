from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

note_stylesheet = """
#frame_buttom{
    background-color: rgb(255, 247, 209);
    
}
QTextBrowser{
    border: none;
    font: 14pt "Consolas";
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

class YellowNote(object):

    # def __init__(self, parent):
    #     super().__init__(parent)
    #     self.setupUi(parent)

    def setupUi(self, Note, stylesheet=note_stylesheet):
        Note.setObjectName("Note")
        # Note.resize(396, 400)
        Note.setStyleSheet(stylesheet)

        self.verticalLayout = QVBoxLayout(Note)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame_outer = QFrame(Note)
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
        font.setFamily("MingLiU-ExtB")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setReadOnly(False)
        # https://stackoverflow.com/questions/54875284/scrollbar-to-always-show-the-bottom-of-a-qtextbrowser-streamed-text
        # self.setLineWrapMode(QTextEdit.NoWrap)
        self.textBrowser.setObjectName("textBrowser")

        self.layout_editor.addWidget(self.textBrowser)

        # self.frame_buttom = QFrame(self.frame_outer)
        # self.frame_buttom.setMinimumSize(QSize(0, 48))
        # # self.frame_buttom.setStyleSheet("\n""")
        # self.frame_buttom.setFrameShape(QFrame.StyledPanel)
        # self.frame_buttom.setFrameShadow(QFrame.Raised)
        # self.frame_buttom.setObjectName("frame_buttom")

        # # self.horizontalLayout_3.addWidget(self.frame_grip, 0, Qt.AlignRight|Qt.AlignBottom)
        # self.layout_editor.addWidget(self.frame_buttom)
        self.verticalLayout.addWidget(self.frame_outer)

        self.retranslateUi(Note)
        QMetaObject.connectSlotsByName(Note)

    def retranslateUi(self, Note):
        _translate = QCoreApplication.translate
        Note.setWindowTitle(_translate("Note", "Form"))
        self.textBrowser.setHtml(_translate("Note", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MingLiU-ExtB\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser.setPlaceholderText(_translate("Note", "output goes here..."))

    def setText(self, text):
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

    def show_and_print(self, text):
        # print('my note, setting text:', text)
        self.setText(text)
        if not self.textBrowser.isVisible():
            self.textBrowser.show()


class StickyNote(QWidget):
    def __init__(self, parent=None, *args, **kwargs):        
        super(StickyNote, self).__init__(parent, *args, **kwargs)
        ui = YellowNote()
        ui.setupUi(self)

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     dummy = QWidget()
#     ui = YellowNote()
#     ui.setupUi(dummy)
#     # ui = YellowNote(dummy)
#     dummy.show()
#     sys.exit(app.exec_())
