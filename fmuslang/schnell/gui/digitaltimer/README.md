requirements
https://pypi.org/project/absresgetter/
https://pypi.org/project/pyqt-notifier/
https://pypi.org/project/pyqt-resource-helper/
https://pypi.org/user/yjg30737/
https://pypi.org/project/pyqt-timer-label/

File "C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\pyqt_responsive_label\responsiveLabel.py", line 27, in __setApproximateFontSize
self.setFont(QFont('Arial', max(12, min(self.widthMM()//2, self.height()-2) // dpr)))
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: arguments did not match any overloaded call:
QFont(): too many arguments
QFont(str, pointSize: int = -1, weight: int = -1, italic: bool = False): argument 2 has unexpected type 'float'
QFont(QFont, QPaintDevice): argument 1 has unexpected type 'str'
QFont(QFont): argument 1 has unexpected type 'str'
QFont(Any): too many arguments

C:\Users\usef\work\sidoarjo\schnell\gui\digitaltimer>

# pyqt-transparent-timer
PyQt transparent timer

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-transparent-timer.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-timer.git">pyqt-timer</a> - Parent package
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>

## Usage
* Press the escape button if you want to quit.
* If you want to know more about how to use this, see <a href="https://github.com/yjg30737/pyqt-timer/blob/main/README.md">README of pyqt-timer</a>

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_transparent_timer import TransparentTimer


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    tm = TransparentTimer()
    tm.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/149067604-650f7927-5470-44a2-b505-c863e28d8237.png)

When mouse cursor is hovering over the widget, border and background will show up.

![image](https://user-images.githubusercontent.com/55078043/149068105-d399fa18-1e48-4556-9d29-90c4f7a3e53e.png)

Except for graphics, this module operates the same way as pyqt-timer.

## See also
* <a href="https://github.com/yjg30737/pyqt-timer.git">pyqt-timer</a>
* <a href="https://github.com/yjg30737/pyqt-timer-label.git">pyqt-timer-label</a>
