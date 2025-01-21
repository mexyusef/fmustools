import colorsys, sys

from PyQt5.QtCore import * # QDir, QPoint, QRect, QSize, Qt
from PyQt5.QtGui import * # QImage, QImageWriter, QPainter, QPen, qRgb
from PyQt5.QtWidgets import * # (QAction, QApplication, QColorDialog, QFileDialog, QInputDialog, QMainWindow, QMenu, QMessageBox, QWidget)
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtPrintSupport import QPrintDialog, QPrinter

# from PyQt5.QtCore import Qt, pyqtSignal


# https://github.com/nlfmt/pyqt-colorpicker-widget

class Ui_ColorPicker(object):
    def setupUi(self, ColorPicker):
        ColorPicker.setObjectName("ColorPicker")
        ColorPicker.resize(360, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ColorPicker.sizePolicy().hasHeightForWidth())
        ColorPicker.setSizePolicy(sizePolicy)
        ColorPicker.setMinimumSize(QtCore.QSize(0, 0))
        ColorPicker.setMaximumSize(QtCore.QSize(360, 200))
        ColorPicker.setStyleSheet("QWidget{\n"
"    background-color: none;\n"
"}\n"
"QFrame{\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"/*  LINE EDIT */\n"
"QLineEdit{\n"
"    color: rgb(221, 221, 221);\n"
"    background-color: #303030;\n"
"    border: 2px solid #303030;\n"
"    border-radius: 5px;\n"
"    selection-color: rgb(16, 16, 16);\n"
"    selection-background-color: rgb(221, 51, 34);\n"
"    font-family: Segoe UI;\n"
"    font-size: 11pt;\n"
"}\n"
"QLineEdit::focus{\n"
"    border-color: #aaaaaa;\n"
"}\n"
"")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(ColorPicker)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.color_view = QtWidgets.QFrame(ColorPicker)
        self.color_view.setMinimumSize(QtCore.QSize(200, 200))
        self.color_view.setMaximumSize(QtCore.QSize(5000, 5000))
        self.color_view.setStyleSheet("/* ALL CHANGES HERE WILL BE OVERWRITTEN */;\n"
"background-color: qlineargradient(x1:1, x2:0, stop:0 hsl(0%,100%,50%), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        self.color_view.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.color_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.color_view.setObjectName("color_view")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.color_view)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.black_overlay = QtWidgets.QFrame(self.color_view)
        self.black_overlay.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 255));\n"
"border-radius: 4px;\n"
"\n"
"")
        self.black_overlay.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.black_overlay.setFrameShadow(QtWidgets.QFrame.Raised)
        self.black_overlay.setObjectName("black_overlay")
        self.selector = QtWidgets.QFrame(self.black_overlay)
        self.selector.setGeometry(QtCore.QRect(-6, 194, 12, 12))
        self.selector.setMinimumSize(QtCore.QSize(12, 12))
        self.selector.setMaximumSize(QtCore.QSize(12, 12))
        self.selector.setStyleSheet("background-color:none;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.selector.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.selector.setFrameShadow(QtWidgets.QFrame.Raised)
        self.selector.setObjectName("selector")
        self.black_ring = QtWidgets.QLabel(self.selector)
        self.black_ring.setGeometry(QtCore.QRect(1, 1, 10, 10))
        self.black_ring.setMinimumSize(QtCore.QSize(10, 10))
        self.black_ring.setMaximumSize(QtCore.QSize(10, 10))
        self.black_ring.setBaseSize(QtCore.QSize(10, 10))
        self.black_ring.setStyleSheet("background-color: none;\n"
"border: 1px solid black;\n"
"border-radius: 5px;")
        self.black_ring.setText("")
        self.black_ring.setObjectName("black_ring")
        self.verticalLayout_2.addWidget(self.black_overlay)
        self.horizontalLayout_2.addWidget(self.color_view)
        self.hue_frame = QtWidgets.QFrame(ColorPicker)
        self.hue_frame.setMinimumSize(QtCore.QSize(30, 0))
        self.hue_frame.setStyleSheet("QLabel{\n"
"    border-radius: 5px;\n"
"}")
        self.hue_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hue_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hue_frame.setObjectName("hue_frame")
        self.hue_bg = QtWidgets.QFrame(self.hue_frame)
        self.hue_bg.setGeometry(QtCore.QRect(10, 0, 20, 200))
        self.hue_bg.setMinimumSize(QtCore.QSize(20, 200))
        self.hue_bg.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"border-radius: 5px;")
        self.hue_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hue_bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hue_bg.setObjectName("hue_bg")
        self.hue_selector = QtWidgets.QLabel(self.hue_frame)
        self.hue_selector.setGeometry(QtCore.QRect(7, 185, 26, 15))
        self.hue_selector.setMinimumSize(QtCore.QSize(26, 0))
        self.hue_selector.setStyleSheet("background-color: #222;\n"
"")
        self.hue_selector.setText("")
        self.hue_selector.setObjectName("hue_selector")
        self.hue = QtWidgets.QFrame(self.hue_frame)
        self.hue.setGeometry(QtCore.QRect(7, 0, 26, 200))
        self.hue.setMinimumSize(QtCore.QSize(20, 200))
        self.hue.setStyleSheet("")
        self.hue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hue.setObjectName("hue")
        self.horizontalLayout_2.addWidget(self.hue_frame)
        self.editfields = QtWidgets.QFrame(ColorPicker)
        self.editfields.setMinimumSize(QtCore.QSize(120, 200))
        self.editfields.setMaximumSize(QtCore.QSize(120, 200))
        self.editfields.setStyleSheet("QLabel{\n"
"    font-family: Segoe UI;\n"
"font-weight: bold;\n"
"    font-size: 11pt;\n"
"    color: #aaaaaa;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.editfields.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.editfields.setFrameShadow(QtWidgets.QFrame.Raised)
        self.editfields.setObjectName("editfields")
        self.formLayout = QtWidgets.QFormLayout(self.editfields)
        self.formLayout.setContentsMargins(5, 10, 15, 3)
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.color_vis = QtWidgets.QLabel(self.editfields)
        self.color_vis.setMinimumSize(QtCore.QSize(0, 50))
        self.color_vis.setMaximumSize(QtCore.QSize(16777215, 50))
        self.color_vis.setStyleSheet("/* ALL CHANGES HERE WILL BE OVERWRITTEN */;\n"
"background-color: #000;\n"
"")
        self.color_vis.setText("")
        self.color_vis.setObjectName("color_vis")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.color_vis)
        self.lbl_red = QtWidgets.QLabel(self.editfields)
        self.lbl_red.setObjectName("lbl_red")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_red)
        self.red = QtWidgets.QLineEdit(self.editfields)
        self.red.setAlignment(QtCore.Qt.AlignCenter)
        self.red.setClearButtonEnabled(False)
        self.red.setObjectName("red")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.red)
        self.lbl_green = QtWidgets.QLabel(self.editfields)
        self.lbl_green.setObjectName("lbl_green")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_green)
        self.green = QtWidgets.QLineEdit(self.editfields)
        self.green.setAlignment(QtCore.Qt.AlignCenter)
        self.green.setObjectName("green")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.green)
        self.lbl_blue = QtWidgets.QLabel(self.editfields)
        self.lbl_blue.setObjectName("lbl_blue")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_blue)
        self.blue = QtWidgets.QLineEdit(self.editfields)
        self.blue.setAlignment(QtCore.Qt.AlignCenter)
        self.blue.setObjectName("blue")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.blue)
        self.lbl_hex = QtWidgets.QLabel(self.editfields)
        self.lbl_hex.setStyleSheet("font-size: 14pt;")
        self.lbl_hex.setObjectName("lbl_hex")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_hex)
        self.hex = QtWidgets.QLineEdit(self.editfields)
        self.hex.setAlignment(QtCore.Qt.AlignCenter)
        self.hex.setObjectName("hex")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.hex)
        self.horizontalLayout_2.addWidget(self.editfields)
        self.lbl_red.setBuddy(self.red)
        self.lbl_green.setBuddy(self.green)
        self.lbl_blue.setBuddy(self.blue)
        self.lbl_hex.setBuddy(self.blue)

        self.retranslateUi(ColorPicker)
        QtCore.QMetaObject.connectSlotsByName(ColorPicker)
        ColorPicker.setTabOrder(self.red, self.green)
        ColorPicker.setTabOrder(self.green, self.blue)

    def retranslateUi(self, ColorPicker):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_red.setText(_translate("ColorPicker", "R"))
        self.red.setText(_translate("ColorPicker", "255"))
        self.lbl_green.setText(_translate("ColorPicker", "G"))
        self.green.setText(_translate("ColorPicker", "255"))
        self.lbl_blue.setText(_translate("ColorPicker", "B"))
        self.blue.setText(_translate("ColorPicker", "255"))
        self.lbl_hex.setText(_translate("ColorPicker", "#"))
        self.hex.setText(_translate("ColorPicker", "ffffff"))

class ColorPicker(QWidget):

    colorChanged = pyqtSignal()

    def __init__(self, *args, **kwargs):

        # Extract Initial Color out of kwargs
        rgb = kwargs.pop("rgb", None)
        hsv = kwargs.pop("hsv", None)
        hex = kwargs.pop("hex", None)

        super(ColorPicker, self).__init__(*args, **kwargs)

        # Call UI Builder function
        self.ui = Ui_ColorPicker()
        self.ui.setupUi(self)

        # Connect update functions
        self.ui.hue.mouseMoveEvent = self.moveHueSelector
        self.ui.hue.mousePressEvent = self.moveHueSelector
        self.ui.red.textEdited.connect(self.rgbChanged)
        self.ui.green.textEdited.connect(self.rgbChanged)
        self.ui.blue.textEdited.connect(self.rgbChanged)
        self.ui.hex.textEdited.connect(self.hexChanged)

        # Connect selector moving function
        self.ui.black_overlay.mouseMoveEvent = self.moveSVSelector
        self.ui.black_overlay.mousePressEvent = self.moveSVSelector

        if rgb:
            self.setRGB(rgb)
        elif hsv:
            self.setHSV(hsv)
        elif hex:
            self.setHex(hex)
        else:
            self.setRGB((0,0,0))


    ## Main Functions ##
    def getHSV(self, hrange=100, svrange=100):
        h,s,v = self.color
        return (h*(hrange/100.0), s*(svrange/100.0), v*(svrange/100.0))

    def getRGB(self, range=255):
        r,g,b = self.i(self.ui.red.text()), self.i(self.ui.green.text()), self.i(self.ui.blue.text())
        return (r*(range/255.0),g*(range/255.0),b*(range/255.0))

    def getHex(self, ht=False):
        rgb = (self.i(self.ui.red.text()), self.i(self.ui.green.text()), self.i(self.ui.blue.text()))
        if ht: return "#" + self.rgb2hex(rgb)
        else: return self.rgb2hex(rgb)


    ## Update Functions ##
    def hsvChanged(self):
        h,s,v = (100 - self.ui.hue_selector.y() / 1.85, (self.ui.selector.x() + 6) / 2.0, (194 - self.ui.selector.y()) / 2.0)
        r,g,b = self.hsv2rgb(h,s,v)
        self.color = (h,s,v)
        self._setRGB((r,g,b))
        self._setHex(self.hsv2hex(self.color))
        self.ui.color_vis.setStyleSheet(f"background-color: rgb({r},{g},{b})")
        self.ui.color_view.setStyleSheet(f"border-radius: 5px;background-color: qlineargradient(x1:1, x2:0, stop:0 hsl({h}%,100%,50%), stop:1 #fff);")
        self.colorChanged.emit()

    def rgbChanged(self):
        r,g,b = self.i(self.ui.red.text()), self.i(self.ui.green.text()), self.i(self.ui.blue.text())
        self.color = self.rgb2hsv(r,g,b)
        self._setHSV(self.color)
        self._setHex(self.rgb2hex((r,g,b)))
        self.ui.color_vis.setStyleSheet(f"background-color: rgb({r},{g},{b})")
        self.colorChanged.emit()

    def hexChanged(self):
        hex = self.ui.hex.text()
        r,g,b = self.hex2rgb(hex)
        self.color = self.hex2hsv(hex)
        self._setHSV(self.color)
        self._setRGB(self.hex2rgb(hex))
        self.ui.color_vis.setStyleSheet(f"background-color: rgb({r},{g},{b})")
        self.colorChanged.emit()


    ## internal setting functions ##
    def _setRGB(self, c):
        r,g,b = c
        self.ui.red.setText(str(self.i(r)))
        self.ui.green.setText(str(self.i(g)))
        self.ui.blue.setText(str(self.i(b)))

    def _setHSV(self, c):
        self.ui.hue_selector.move(7, int((100 - c[0]) * 1.85))
        self.ui.color_view.setStyleSheet(f"border-radius: 5px;background-color: qlineargradient(x1:1, x2:0, stop:0 hsl({c[0]}%,100%,50%), stop:1 #fff);")
        self.ui.selector.move(int(c[1] * 2 - 6), int((200 - c[2] * 2) - 6))

    def _setHex(self, c):
        self.ui.hex.setText(c)


    ## external setting functions ##
    def setRGB(self, c):
        self._setRGB(c)
        self.rgbChanged()

    def setHSV(self, c):
        self._setHSV(c)
        self.hsvChanged()

    def setHex(self, c):
        self._setHex(c)
        self.hexChanged()


    ## Color Utility ##
    def hsv2rgb(self, h_or_color, s = 0, v = 0):
        if type(h_or_color).__name__ == "tuple": h,s,v = h_or_color
        else: h = h_or_color
        r,g,b = colorsys.hsv_to_rgb(h / 100.0, s / 100.0, v / 100.0)
        return self.clampRGB((r * 255, g * 255, b * 255))

    def rgb2hsv(self, r_or_color, g = 0, b = 0):
        if type(r_or_color).__name__ == "tuple": r,g,b = r_or_color
        else: r = r_or_color
        h,s,v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
        return (h * 100, s * 100, v * 100)

    def hex2rgb(self, hex):
        if len(hex) < 6: hex += "0"*(6-len(hex))
        elif len(hex) > 6: hex = hex[0:6]
        rgb = tuple(int(hex[i:i+2], 16) for i in (0,2,4))
        return rgb

    def rgb2hex(self, r_or_color, g = 0, b = 0):
        if type(r_or_color).__name__ == "tuple": r,g,b = r_or_color
        else: r = r_or_color
        hex = '%02x%02x%02x' % (int(r),int(g),int(b))
        return hex

    def hex2hsv(self, hex):
        return self.rgb2hsv(self.hex2rgb(hex))

    def hsv2hex(self, h_or_color, s = 0, v = 0):
        if type(h_or_color).__name__ == "tuple": h,s,v = h_or_color
        else: h = h_or_color
        return self.rgb2hex(self.hsv2rgb(h,s,v))


    # selector move function
    def moveSVSelector(self, event):
        if event.buttons() == Qt.LeftButton:
            pos = event.pos()
            if pos.x() < 0: pos.setX(0)
            if pos.y() < 0: pos.setY(0)
            if pos.x() > 200: pos.setX(200)
            if pos.y() > 200: pos.setY(200)
            self.ui.selector.move(pos - QPoint(6,6))
            self.hsvChanged()

    def moveHueSelector(self, event):
        if event.buttons() == Qt.LeftButton:
            pos = event.pos().y() - 7
            if pos < 0: pos = 0
            if pos > 185: pos = 185
            self.ui.hue_selector.move(QPoint(7,pos))
            self.hsvChanged()

    def i(self, text):
        try: return int(text)
        except: return 0

    def clampRGB(self, rgb):
        r,g,b = rgb
        if r<0.0001: r=0
        if g<0.0001: g=0
        if b<0.0001: b=0
        if r>255: r=255
        if g>255: g=255
        if b>255: b=255
        return (r,g,b)

# class picker(QtWidgets.QPushButton):
#     '''
#     Custom Qt Widget to show a chosen color.

#     Left-clicking the button shows the color-chooser, while
#     right-clicking resets the color to None (no-color).
#     '''

#     colorChanged = pyqtSignal(object)

#     def __init__(self, *args, color=None, **kwargs):
#         super(picker, self).__init__(*args, **kwargs)

#         self._color = None
#         self._default = color
#         self.pressed.connect(self.onColorPicker)

#         # Set the initial/default state.
#         self.setColor(self._default)

#     def setColor(self, color):
#         if color != self._color:
#             self._color = color
#             self.colorChanged.emit(color)

#         if self._color:
#             self.setStyleSheet("background-color: %s;" % self._color)
#         else:
#             self.setStyleSheet("")

#     def color(self):
#         return self._color

#     def onColorPicker(self):
#         '''
#         Show color-picker dialog to select color.

#         Qt will use the native dialog by default.

#         '''
#         dlg = QtWidgets.QColorDialog(self)
#         if self._color:
#             dlg.setCurrentColor(QtGui.QColor(self._color))

#         if dlg.exec_():
#             self.setColor(dlg.currentColor().name())

#     def mousePressEvent(self, e):
#         if e.button() == Qt.RightButton:
#             self.setColor(self._default)

#         return super(picker, self).mousePressEvent(e)

class ScribbleArea(QWidget):
    def __init__(self, parent=None):
        super(ScribbleArea, self).__init__(parent)

        self.setAttribute(Qt.WA_StaticContents)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 1
        self.myPenColor = Qt.blue
        self.image = QImage()
        self.lastPoint = QPoint()

    def openImage(self, fileName):
        loadedImage = QImage()
        if not loadedImage.load(fileName):
            return False

        newSize = loadedImage.size().expandedTo(self.size())
        self.resizeImage(loadedImage, newSize)
        self.image = loadedImage
        self.modified = False
        self.update()
        return True

    def saveImage(self, fileName, fileFormat):
        visibleImage = self.image
        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName, fileFormat):
            self.modified = False
            return True
        else:
            return False

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        self.image.fill(qRgb(255, 255, 255))
        self.modified = True
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.scribbling = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.scribbling:
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.scribbling:
            self.drawLineTo(event.pos())
            self.scribbling = False

    def paintEvent(self, event):
        painter = QPainter(self)
        dirtyRect = event.rect()
        painter.drawImage(dirtyRect, self.image, dirtyRect)

    def resizeEvent(self, event):
        if self.width() > self.image.width() or self.height() > self.image.height():
            newWidth = max(self.width() + 128, self.image.width())
            newHeight = max(self.height() + 128, self.image.height())
            self.resizeImage(self.image, QSize(newWidth, newHeight))
            self.update()

        super(ScribbleArea, self).resizeEvent(event)

    def drawLineTo(self, endPoint):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.myPenColor, self.myPenWidth, Qt.SolidLine,
                Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        rad = self.myPenWidth // 2 + 2
        self.update(QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        self.lastPoint = QPoint(endPoint)

    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        newImage = QImage(newSize, QImage.Format_RGB32)
        newImage.fill(qRgb(255, 255, 255))
        painter = QPainter(newImage)
        painter.drawImage(QPoint(0, 0), image)
        self.image = newImage

    def print_(self):
        printer = QPrinter(QPrinter.HighResolution)

        printDialog = QPrintDialog(printer, self)
        if printDialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)
            painter.end()

    def isModified(self):
        return self.modified

    def penColor(self):
        return self.myPenColor

    def penWidth(self):
        return self.myPenWidth


class PaintWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.main_layout = QVBoxLayout()
        
        # self.picker = picker()
        self.picker = ColorPicker()

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(1,50)
        self.slider.setSingleStep(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)
        # self.slider.valueChanged.connect(lambda value: print('val:', value))
        # self.slider.sliderMoved.connect(lambda value: print('pos', value))
        # self.slider.sliderPressed.connect(lambda: print('pressed'))
        # self.slider.sliderReleased.connect(lambda: print('released'))
        self.slider_value = QLabel(str(self.slider.value()))
        self.slider_value.setFont(QFont("Arial", 16))
        self.slider.valueChanged.connect(lambda value: self.slider_value.setText(str(value)))

        slider_layout = QVBoxLayout()
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.slider_value)

        # self.toolbar = QWidget()
        tool_layout = QHBoxLayout()
        tool_layout.addWidget(self.picker)
        # tool_layout.addWidget(self.slider)
        tool_layout.addLayout(slider_layout)

        self.scribbleArea = ScribbleArea()
        # self.main_layout.addWidget(self.slider)
        # self.main_layout.addWidget(self.picker)
        self.main_layout.addLayout(tool_layout, 3)
        self.main_layout.addWidget(self.scribbleArea, 7)
        self.setLayout(self.main_layout)

        # self.resize(800, 600)
        # self.setWindowTitle('nice window')
        # QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())
        # self.show()

class DrawingWidget(QWidget):
    def __init__(self):
        super(DrawingWidget, self).__init__()

        self.saveAsActs = []

        # self.scribbleArea = ScribbleArea()
        self.painter = PaintWidget()
        self.scribbleArea = self.painter.scribbleArea
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.painter)

        self.painter.picker.colorChanged.connect(self.ganti_warna)
        self.painter.slider.valueChanged.connect(self.ganti_tebal)

        self.createActions()
        self.createMenus()

        # self.setWindowTitle("Scribble")
        # self.resize(500, 500)

    def ganti_warna(self):
        ambil = self.painter.picker.getRGB()
        newColor = QColor()
        newColor.setRgb(*[int(i) for i in ambil])
        if newColor.isValid():
            self.scribbleArea.setPenColor(newColor)

    def ganti_tebal(self, nilai):
        self.scribbleArea.setPenWidth(nilai)

    def closeEvent(self, event):
        if self.maybeSave():
            event.accept()
        else:
            event.ignore()

    def open(self):
        if self.maybeSave():
            fileName, _ = QFileDialog.getOpenFileName(self, "Open File",
                    QDir.currentPath())
            if fileName:
                self.scribbleArea.openImage(fileName)

    def save(self):
        action = self.sender()
        fileFormat = action.data()
        self.saveFile(fileFormat)

    def penColor(self):
        newColor = QColorDialog.getColor(self.scribbleArea.penColor())
        if newColor.isValid():
            self.scribbleArea.setPenColor(newColor)

    def penWidth(self):
        newWidth, ok = QInputDialog.getInt(self, "Scribble",
                "Select pen width:", self.scribbleArea.penWidth(), 1, 50, 1)
        if ok:
            self.scribbleArea.setPenWidth(newWidth)

    def about(self):
        QMessageBox.about(self, "About Scribble",
                "<p>The <b>Scribble</b> example shows how to use "
                "QMainWindow as the base widget for an application, and how "
                "to reimplement some of QWidget's event handlers to receive "
                "the events generated for the application's widgets:</p>"
                "<p> We reimplement the mouse event handlers to facilitate "
                "drawing, the paint event handler to update the application "
                "and the resize event handler to optimize the application's "
                "appearance. In addition we reimplement the close event "
                "handler to intercept the close events before terminating "
                "the application.</p>"
                "<p> The example also demonstrates how to use QPainter to "
                "draw an image in real time, as well as to repaint "
                "widgets.</p>")

    def createActions(self):
        self.openAct = QAction("&Open...", self, shortcut="Ctrl+O",
                triggered=self.open)

        for format in QImageWriter.supportedImageFormats():
            format = str(format)

            text = format.upper() + "..."

            action = QAction(text, self, triggered=self.save)
            action.setData(format)
            self.saveAsActs.append(action)

        self.printAct = QAction("&Print...", self,
                triggered=self.scribbleArea.print_)

        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
                triggered=self.close)

        self.penColorAct = QAction("&Pen Color...", self,
                triggered=self.penColor)

        self.penWidthAct = QAction("Pen &Width...", self,
                triggered=self.penWidth)

        self.clearScreenAct = QAction("&Clear Screen", self, shortcut="Ctrl+L",
                triggered=self.scribbleArea.clearImage)

        self.aboutAct = QAction("&About", self, triggered=self.about)

        self.aboutQtAct = QAction("About &Qt", self,
                triggered=QApplication.instance().aboutQt)

    def createMenus(self):
        self.saveAsMenu = QMenu("&Save As", self)
        for action in self.saveAsActs:
            self.saveAsMenu.addAction(action)

        fileMenu = QMenu("&File", self)
        fileMenu.addAction(self.openAct)
        fileMenu.addMenu(self.saveAsMenu)
        fileMenu.addAction(self.printAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)

        optionMenu = QMenu("&Options", self)
        optionMenu.addAction(self.penColorAct)
        optionMenu.addAction(self.penWidthAct)
        optionMenu.addSeparator()
        optionMenu.addAction(self.clearScreenAct)

        helpMenu = QMenu("&Help", self)
        helpMenu.addAction(self.aboutAct)
        helpMenu.addAction(self.aboutQtAct)

        # self.menuBar().addMenu(fileMenu)
        # self.menuBar().addMenu(optionMenu)
        # self.menuBar().addMenu(helpMenu)
        self.file_menu = fileMenu
        self.option_menu = optionMenu
        self.help_menu = helpMenu

    def maybeSave(self):
        if self.scribbleArea.isModified():
            ret = QMessageBox.warning(self, "Scribble",
                        "The image has been modified.\n"
                        "Do you want to save your changes?",
                        QMessageBox.Save | QMessageBox.Discard |
                        QMessageBox.Cancel)
            if ret == QMessageBox.Save:
                return self.saveFile('png')
            elif ret == QMessageBox.Cancel:
                return False

        return True

    def saveFile(self, fileFormat):
        initialPath = QDir.currentPath() + '/untitled.' + fileFormat

        fileName, _ = QFileDialog.getSaveFileName(self, "Save As", initialPath,
                "%s Files (*.%s);;All Files (*)" % (fileFormat.upper(), fileFormat))
        if fileName:
            return self.scribbleArea.saveImage(fileName, fileFormat)

        return False


# if __name__ == '__main__':

#     import sys

#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
