for_app_qinputdialog_stylesheet = """
QDialog {
    background-color: black;
}

QInputDialog {
    background-color: red;
}
"""

qinputdialog_content_stylesheet = """
QLabel{
    font-size:20px;
    font-weight:bold;
    font-family:Arial;
}
QLineEdit{
    font-size:20px;
    font-weight:bold;
    font-family:Arial;
    background-color: linen;
}
QPushButton{
    font-size:20px;
    font-weight:bold;
    font-family:Arial;
    border-style:solid;
    border-color:black;
    border-width:2px; 
}
"""

def input_handler_for_pushbutton(judul='Masukkan', isi='Masukkan data'):
    input_dialog = QInputDialog(None)
    input_dialog.setInputMode(QInputDialog.TextInput)
    input_dialog.setWindowTitle(judul)
    input_dialog.setLabelText(isi)
    input_dialog.setStyleSheet(qinputdialog_content_stylesheet)
    ok = input_dialog.exec_()
    if (ok):
        text = input_dialog.textValue()
        return text
    else:
        return None
