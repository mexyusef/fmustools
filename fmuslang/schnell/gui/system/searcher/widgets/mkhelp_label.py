import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QClipboard
import pyperclip


class ClickableLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)

    def mousePressEvent(self, event):
        # QApplication.clipboard().setText(self.text())
        pyperclip.copy(self.text())
        print("Text copied to clipboard:", self.text())
