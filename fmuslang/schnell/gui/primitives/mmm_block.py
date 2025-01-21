from PyQt5.QtWidgets import (
    qApp,
    
    QApplication,
    QCheckBox,
	QDesktopWidget,
	QDialog,
	QFormLayout,	
    QGraphicsDropShadowEffect,
    QGridLayout,
	QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
	QListWidgetItem,
	QMainWindow,
	QMessageBox,
	QMenu,
    QPushButton,
    QScrollArea,
	QShortcut,
	QTextEdit,
	QToolTip,
	QVBoxLayout,
    QWidget,
)


default_stylesheet = """
background-color:skyblue;
"""

class BlockWidget(QWidget):


    def __init__(self, parent=None, angka_mulai=1, style_sheet=default_stylesheet, effect=None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.angka_mulai = angka_mulai
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents) # scrollAreaWidgetContents ber-layout = grid
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        if not effect:
            self.setGraphicsEffect(effect)

        rows = 20
        cols = 5
        for i in range(rows):
            for j in range(cols):
                btn = QPushButton(f"{self.angka_mulai}")
                self.angka_mulai += 1
                btn.setStyleSheet(style_sheet)
                # btn.resize(20,10) # gak pengaruh
                # btn.clicked.connect(self.button_clicked)
                self.gridLayout.addWidget(btn, i, j)

        lay = QVBoxLayout()
        lay.addWidget(self.scrollArea)
        self.setLayout(lay)
        self.setMinimumWidth(500)
