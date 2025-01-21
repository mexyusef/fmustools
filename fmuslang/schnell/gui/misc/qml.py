import sys
from time import time
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot, pyqtSignal, QTimer
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QVBoxLayout, QPushButton, QTextBrowser

QML = """import QtQuick 2.0
import QtQuick.Controls 1.6
import QtQuick.Layouts 1.3

ApplicationWindow {
    visible: true
    width: 400
    height: 400
    id: root
    title: "editor"

    // Define a signal slot
    signal valueChanged(int value)
    
    Component.onCompleted: {
        // Bind signals and slots to functions in python
        //valueChanged.connect(_Window.onValueChanged)
        // Bind signals in python to functions in qml
        //_Window.timerSignal.connect(appendText)
    }
    
    function appendText(text) {
        // Define the add text function
        textArea.append(text)
    }

    ColumnLayout {
        id: columnLayout
        anchors.fill: parent

        Button {
            id: button
            text: qsTr("Button")
            Layout.fillWidth: true
            onClicked: {
                // Click the button to call the function in python and get the return value
                //var ret = _Window.testSlot("Button")
                var ret = 0
                textArea.append("I called the testSlot function to get the return value: " + ret)
            }
        }

        Slider {
            id: sliderHorizontal
            Layout.fillWidth: true
            stepSize: 1
            minimumValue: 0
            maximumValue: 100
            // Send a signal when the pull bar value changes
            onValueChanged: root.valueChanged(value)
        }

        TextArea {
            id: textArea
            Layout.fillWidth: true
        }
    }

}
"""


def main():
    try:
        QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    except:
        pass

    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    # Provide a communication object _Window, which must be a class that inherits QObject
    # engine.rootContext().setContextProperty('_Window', w)

    engine.objectCreated.connect(lambda obj, _: QMessageBox.critical(None, 'error', 'Failed to run, please check') if not obj else 0)
    engine.loadData(QML.encode())

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

