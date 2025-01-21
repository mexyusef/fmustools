

def resize_screen_ratio(object, screenw, screenh, posx_ratio=1/2, w_ratio=1/6, h_ratio=0, delta_y=60):
    """
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w1, screenw, screenh, 1/4, 1/5)
    resize_screen_ratio(w2, screenw, screenh, 3/4, 1/5)
    atau:
    from schnell.app.guiutils import wh, pindah
    screenw, screenh = wh()
    pindah(w, screenw, screenh, 1/2, 1/2) # 1/2 layar horizontal, 1/2 lebar & tinggi

    object hrs punya method resize dan move.
    posx_ratio = 1/2 = ditengah2 layar, 1/3 di 1/3 layar horizontal, dst.
    """
    if h_ratio <= 0:
        h_ratio = w_ratio
    lebar, tinggi = int(screenw*w_ratio),int(screenh*h_ratio)
    object.resize(lebar, tinggi)
    posx = int((screenw-lebar)*posx_ratio)    
    posy = int((screenh - tinggi)/2) - delta_y
    object.move(posx, posy)


def pindah(object, screenw, screenh, posx_ratio=1/2, w_ratio=1/6, h_ratio=0, delta_y=60):
    return resize_screen_ratio(object=object, screenw=screenw, screenh=screenh, posx_ratio=posx_ratio, w_ratio=w_ratio, h_ratio=h_ratio, delta_y=delta_y)


def screenwh():
    from PyQt5.QtWidgets import QDesktopWidget
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    return screenw, screenh


def wh():
    return screenwh()


def kanan_of(master, slave, posx_ratio=1/2, w_ratio=1/6, h_ratio=0, delta_y=60):
    """
    taro slave di kanan dari master
    """
    sw, sh = screenwh()
    pass


def bawah_of(master, slave, posx_ratio=1/2, w_ratio=1/6, h_ratio=0, delta_y=60):
    """
    taro slave di bawah dari master
    """
    sw, sh = screenwh()
    pass


def set_theme(app):
    from PyQt5.QtGui import QPalette, QColor
    from PyQt5.QtCore import Qt
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)


def get_icon(icon_name):
    """
    self.style().standardIcon(QStyle.SP_ComputerIcon)
    QApplication.style().standardIcon(QStyle.SP_MediaPlay)
    """
    from PyQt5.QtWidgets import QStyle, QApplication
    # return QApplication.style().standardIcon(QStyle.SP_MediaPlay)
    return QApplication.style().standardIcon(getattr(QStyle, icon_name))
