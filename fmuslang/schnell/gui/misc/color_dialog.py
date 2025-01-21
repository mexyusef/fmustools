
import sys
from PyQt5.QtCore import Qt, QSize, QTimer, pyqtSlot
from PyQt5.QtWidgets import (
    QApplication,    
    QColorDialog,
    QDialog,
    QGraphicsDropShadowEffect,      
    QGridLayout,
    QPushButton,
    QSpacerItem,
    QSizePolicy, 
    QVBoxLayout,
    QWidget,

    qApp,
)


def main():
    app = QApplication(sys.argv)
    w = QColorDialog()
    # w.exec_()
    color = w.getColor()
    if color.isValid():
        print(f"""[{color}]
            name: {color.name()}
            R {color.red()} G {color.green()} B {color.blue()}            
            RGB {color.rgb()} RGBA {color.rgba()} torgb as QColor: {color.toRgb()}
            A {color.alpha()} H {color.hue()} L {color.lightness()} S {color.saturation()}            
            """)
        # w.accept()
        # print('mau keluar')
        # qApp.quit()
        # app.quit()
        # print('keluar')
    # sys.exit(0)
    w.raise_()
    w.exec_()
    # QTimer.singleShot(200, app.quit)
    # sys.exit(app.exec_())
    app.exec_()
    # QTimer.singleShot(200, app.quit)
    # sys.exit(app.exec_())

if __name__ == '__main__':
    main()
