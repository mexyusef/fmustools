from PyQt5 import QtCore, QtGui, QtWidgets


note_stylesheet = """
#frame_buttom{
    background-color: rgb(255, 247, 209);    
}
QTextBrowser{
    border: none;
    font: 16pt "Consolas";
    background-color: rgb(255, 247, 209);
    border-radius: 15px;
    line-height: 2.5em;
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

        self.verticalLayout = QtWidgets.QVBoxLayout(Note)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame_outer = QtWidgets.QFrame(Note)
        self.frame_outer.setStyleSheet("")
        self.frame_outer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_outer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_outer.setObjectName("frame_outer")

        self.layout_editor = QtWidgets.QVBoxLayout(self.frame_outer)
        self.layout_editor.setContentsMargins(0, 0, 0, 0)
        self.layout_editor.setSpacing(0)
        self.layout_editor.setObjectName("layout_editor")

        self.textBrowser = QtWidgets.QTextBrowser(self.frame_outer)

        font = QtGui.QFont()
        font.setFamily("MingLiU-ExtB")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("")

        # biar bisa select+copy, matikan
        # self.textBrowser.setReadOnly(True)

        # https://stackoverflow.com/questions/54875284/scrollbar-to-always-show-the-bottom-of-a-qtextbrowser-streamed-text
        # self.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser.setObjectName("textBrowser")

        self.layout_editor.addWidget(self.textBrowser)

        # self.frame_buttom = QtWidgets.QFrame(self.frame_outer)
        # self.frame_buttom.setMinimumSize(QtCore.QSize(0, 48))
        # # self.frame_buttom.setStyleSheet("\n""")
        # self.frame_buttom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_buttom.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_buttom.setObjectName("frame_buttom")

        # # self.horizontalLayout_3.addWidget(self.frame_grip, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        # self.layout_editor.addWidget(self.frame_buttom)
        self.verticalLayout.addWidget(self.frame_outer)

        self.retranslateUi(Note)
        QtCore.QMetaObject.connectSlotsByName(Note)

    def retranslateUi(self, Note):
        _translate = QtCore.QCoreApplication.translate
        Note.setWindowTitle(_translate("Note", "Form"))
        self.textBrowser.setHtml(_translate("Note", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MingLiU-ExtB\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser.setPlaceholderText(_translate("Note", "output goes here..."))

    def setText(self, text, is_markdown=False):
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


# import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dummy = QtWidgets.QWidget()
    ui = YellowNote()
    ui.setupUi(dummy)
    # ui = YellowNote(dummy)
    dummy.show()
    sys.exit(app.exec_())
