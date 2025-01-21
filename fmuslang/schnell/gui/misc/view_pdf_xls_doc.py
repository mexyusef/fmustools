#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017年4月6日
@author: Irony
@site: https://pyqt.site , https://github.com/PyQt5
@email: 892768447@qq.com
@file: ViewOffice
@description: 
"""

from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox


class AxWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(AxWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        layout = QVBoxLayout(self)
        self.axWidget = QAxWidget(self)
        layout.addWidget(self.axWidget)
        layout.addWidget(QPushButton('select excel,word,pdf files', self, clicked=self.onOpenFile))

    def onOpenFile(self):
        path, _ = QFileDialog.getOpenFileName(
            self, 'Please select file', '', 'pdf(*.pdf);;word(*.docx *.doc);;excel(*.xlsx *.xls)')
        if not path:
            return
        if _.find('*.doc'):
            return self.openOffice(path, 'Word.Application')
        if _.find('*.xls'):
            return self.openOffice(path, 'Excel.Application')
        if _.find('*.pdf'):
            return self.openPdf(path)

    def openOffice(self, path, app):
        self.axWidget.clear()
        if not self.axWidget.setControl(app):
            return QMessageBox.critical(self, 'Error', 'Not installed  %s' % app)
        self.axWidget.dynamicCall(
            'SetVisible (bool Visible)', 'false')  # 不显示窗体
        self.axWidget.setProperty('DisplayAlerts', False)
        self.axWidget.setControl(path)

    def openPdf(self, path):
        self.axWidget.clear()
        if not self.axWidget.setControl('Adobe PDF Reader'):
            return QMessageBox.critical(self, 'Error', 'Not installed Adobe PDF Reader')
        self.axWidget.dynamicCall('LoadFile(const QString&)', path)

    def closeEvent(self, event):
        self.axWidget.close()
        self.axWidget.clear()
        self.layout().removeWidget(self.axWidget)
        del self.axWidget
        super(AxWidget, self).closeEvent(event)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = AxWidget()
    w.show()
    sys.exit(app.exec_())
