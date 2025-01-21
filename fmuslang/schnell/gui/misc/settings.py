from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets

settings_stylesheet = """
/*左侧*/
#listWidget {
    outline: 0px;
    max-width: 165px;
    background-color: rgb(240, 240, 240);
}

#listWidget::item {
    min-height: 45px;
}

#listWidget::item:hover {
    background-color: rgb(225, 230, 235);
}

#listWidget::item:selected {
    color: black;
    background-color: rgb(255, 255, 255);
}

/*右侧*/
#titleLabel1,#titleLabel2,#titleLabel3,#titleLabel4,#titleLabel5,#titleLabel6,#titleLabel7,#titleLabel8 {
    min-width: 75px;
    max-width: 75px;
}

#right1,#right2,#right3,#right4,#right5,#right6 {
    margin-left: 25px;
    color: rgb(128, 128, 128);
}

/*所有按钮*/
QPushButton {
    max-width: 80px;
    max-height: 24px;
    min-height: 24px;
    border-radius: 3px;
    background-color: rgb(244, 244, 244);
    border: 1px solid rgb(167, 167, 167);
}

QPushButton:hover {
    background-color: rgb(190, 231, 253);
}

QPushButton:pressed {
    background-color: rgb(244, 244, 244);
}

QComboBox {
    max-width: 80px;
    max-height: 20px;
    min-height: 20px;
}

QComboBox {
    border: 1px solid rgb(167, 167, 167);
    border-radius: 3px;
}

#listWidgetUser {
    min-width: 290px;
    max-width: 290px;
    max-height: 120px;
    min-height: 120px;
    border-radius: 2px;
    border: 1px solid rgb(227, 236, 242);
    background-color: rgb(244, 250, 253);
}

QScrollBar::vertical {
    background: rgb(178, 178, 178);
    border: -5px solid grey;
    margin: 0px 0px 0px 0px;
    width: 10px;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: white;
}
"""

class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(498, 498)

        self.horizontalLayout = QHBoxLayout(Setting)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.listWidget = QListWidget(Setting)
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setObjectName("listWidget")
        
        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(0)
        item.setText("Log in")

        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(1)
        item.setText("main panel")

        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(2)
        item.setText("state")

        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(3)
        item.setText("session window")

        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(4)
        item.setText("Information display")

        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(5)
        item.setText("remind")

        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(6)
        item.setText("hotkey")

        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(7)
        item.setText("show")

        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(8)
        item.setText("sound")

        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(9)
        item.setText("Software update")

        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(10)
        item.setText("file management")

        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(11)
        item.setText("File Sharing")

        item = QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(12)
        item.setText("Audio and video calls")

        self.horizontalLayout.addWidget(self.listWidget)
        Setting.setWindowTitle("Imitation QQ settings panel")
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.scrollArea = QScrollArea(Setting)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -810, 460, 1308))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(35, 20, 35, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")

        # GROUP 1
        self.widget_0 = QWidget(self.scrollAreaWidgetContents)
        self.widget_0.setObjectName("widget_0")

        self.formLayout = QFormLayout(self.widget_0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.titleLabel1 = QLabel(self.widget_0)
        self.titleLabel1.setObjectName("titleLabel1")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.titleLabel1)

        self.CheckBox = QCheckBox(self.widget_0)
        self.CheckBox.setObjectName("CheckBox")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.CheckBox)

        self.checkBox = QCheckBox(self.widget_0)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.checkBox)

        self.checkBox_2 = QCheckBox(self.widget_0)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.widget_0)
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.widget_0)
        self.checkBox_4.setObjectName("checkBox_4")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.widget_0)
        self.checkBox_5.setObjectName("checkBox_5")
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.widget_0)
        self.checkBox_6.setObjectName("checkBox_6")
        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.checkBox_6)

        # group 1, Projects
        self.titleLabel1.setText("Log in:")
        self.CheckBox.setText("incremental")  # true
        self.checkBox.setText("composite")  # true
        self.checkBox_2.setText("tsBuildInfoFile")  # ./.tsbuildinfo
        self.checkBox_3.setText("disableSourceOfProjectReferenceRedirect")  # true
        self.checkBox_4.setText("disableSolutionSearching")  # true
        self.checkBox_5.setText("disableReferencedProjectLoad")   # true
        self.checkBox_6.setText("ganti")
        self.verticalLayout.addWidget(self.widget_0)

        # GROUP 2
        self.widget_1 = QWidget(self.scrollAreaWidgetContents)
        self.widget_1.setObjectName("widget_1")

        self.formLayout_8 = QFormLayout(self.widget_1)
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.formLayout_8.setObjectName("formLayout_8")
        self.titleLabel2 = QLabel(self.widget_1)
        self.titleLabel2.setObjectName("titleLabel2")
        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.titleLabel2)
        self.checkBox_26 = QCheckBox(self.widget_1)
        self.checkBox_26.setObjectName("checkBox_26")
        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.checkBox_26)
        self.checkBox_27 = QCheckBox(self.widget_1)
        self.checkBox_27.setObjectName("checkBox_27")
        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.checkBox_27)
        self.checkBox_28 = QCheckBox(self.widget_1)
        self.checkBox_28.setObjectName("checkBox_28")
        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.checkBox_28)
        self.checkBox_29 = QCheckBox(self.widget_1)
        self.checkBox_29.setObjectName("checkBox_29")
        self.formLayout_8.setWidget(3, QFormLayout.FieldRole, self.checkBox_29)
        self.label_10 = QLabel(self.widget_1)
        self.label_10.setObjectName("label_10")
        self.formLayout_8.setWidget(4, QFormLayout.FieldRole, self.label_10)
        self.right1 = QRadioButton(self.widget_1)
        self.right1.setObjectName("right1")
        self.formLayout_8.setWidget(5, QFormLayout.FieldRole, self.right1)
        self.right2 = QRadioButton(self.widget_1)
        self.right2.setChecked(True)
        self.right2.setObjectName("right2")
        self.formLayout_8.setWidget(6, QFormLayout.FieldRole, self.right2)
        self.label_11 = QLabel(self.widget_1)
        self.label_11.setObjectName("label_11")
        self.formLayout_8.setWidget(7, QFormLayout.FieldRole, self.label_11)
        self.right3 = QPushButton(self.widget_1)
        self.right3.setObjectName("right3")
        self.formLayout_8.setWidget(8, QFormLayout.FieldRole, self.right3)

        self.verticalLayout.addWidget(self.widget_1)

        # group 2, Language and Environment
        self.titleLabel2.setText("Main panel:")
        self.checkBox_26.setText("target")  # es2016
        self.checkBox_27.setText("lib")  # []
        self.checkBox_28.setText("jsx")  # preserve
        self.checkBox_29.setText("experimentalDecorators")  # true
        self.label_10.setText("When closing the main panel:")
        self.right1.setText("Hide to the taskbar notification area without exiting the program")
        self.right2.setText("exit the program")
        self.label_11.setText("You can freely customize the panels and functions that suit you, and use QQ more efficiently")
        self.right3.setText("interface manager")


        # GROUP 3
        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName("widget_2")

        self.formLayout_9 = QFormLayout(self.widget_2)
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.formLayout_9.setObjectName("formLayout_9")
        self.titleLabel3 = QLabel(self.widget_2)
        self.titleLabel3.setObjectName("titleLabel3")
        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.titleLabel3)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.comboBox = QComboBox(self.widget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout_9.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)
        self.checkBox_30 = QCheckBox(self.widget_2)
        self.checkBox_30.setObjectName("checkBox_30")
        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.checkBox_30)
        self.right4 = QLabel(self.widget_2)
        self.right4.setObjectName("right4")
        self.formLayout_9.setWidget(2, QFormLayout.FieldRole, self.right4)
        self.checkBox_31 = QCheckBox(self.widget_2)
        self.checkBox_31.setObjectName("checkBox_31")
        self.formLayout_9.setWidget(3, QFormLayout.FieldRole, self.checkBox_31)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.formLayout_9.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.verticalLayout.addWidget(self.widget_2)
        # group 3
        self.titleLabel3.setText("state:")
        self.label_13.setText("After logging in, the status is:")
        self.comboBox.setItemText(0, "i am online")
        self.comboBox.setItemText(1, "Q me")
        self.comboBox.setItemText(2, "leave")
        self.comboBox.setItemText(3, "Busy")
        self.comboBox.setItemText(4, "do not disturb")
        self.comboBox.setItemText(5, "stealth")
        self.checkBox_30.setText("Switch to 'busy' state when running a full-screen program")
        self.right4.setText("Only valid in the 'Q me' and I'm online status")
        self.checkBox_31.setText("Automatic reply when away, busy, do not disturb (within 100 words)")
        self.pushButton_5.setText("Autoresponder settings")
        self.pushButton_4.setText("Quick reply settings")


        # GROUP 4
        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName("widget_3")

        self.formLayout_2 = QFormLayout(self.widget_3)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.titleLabel4 = QLabel(self.widget_3)
        self.titleLabel4.setObjectName("titleLabel4")
        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.titleLabel4)
        self.CheckBox_2 = QCheckBox(self.widget_3)
        self.CheckBox_2.setChecked(True)
        self.CheckBox_2.setObjectName("CheckBox_2")
        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.CheckBox_2)
        self.checkBox_7 = QCheckBox(self.widget_3)
        self.checkBox_7.setObjectName("checkBox_7")
        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.checkBox_7)
        self.checkBox_8 = QCheckBox(self.widget_3)
        self.checkBox_8.setObjectName("checkBox_8")
        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.checkBox_8)
        self.checkBox_9 = QCheckBox(self.widget_3)
        self.checkBox_9.setChecked(True)
        self.checkBox_9.setObjectName("checkBox_9")
        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.checkBox_9)
        self.checkBox_10 = QCheckBox(self.widget_3)
        self.checkBox_10.setChecked(True)
        self.checkBox_10.setObjectName("checkBox_10")
        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.checkBox_10)
        self.checkBox_11 = QCheckBox(self.widget_3)
        self.checkBox_11.setChecked(True)
        self.checkBox_11.setObjectName("checkBox_11")
        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.checkBox_11)
        self.checkBox_12 = QCheckBox(self.widget_3)
        self.checkBox_12.setChecked(True)
        self.checkBox_12.setObjectName("checkBox_12")
        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.checkBox_12)
        self.checkBox_13 = QCheckBox(self.widget_3)
        self.checkBox_13.setChecked(True)
        self.checkBox_13.setObjectName("checkBox_13")
        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.checkBox_13)
        self.checkBox_14 = QCheckBox(self.widget_3)
        self.checkBox_14.setChecked(True)
        self.checkBox_14.setObjectName("checkBox_14")
        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.checkBox_14)
        self.checkBox_15 = QCheckBox(self.widget_3)
        self.checkBox_15.setChecked(True)
        self.checkBox_15.setObjectName("checkBox_15")
        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.checkBox_15)

        self.verticalLayout.addWidget(self.widget_3)
        # group 4
        self.titleLabel4.setText("Session window:")
        self.CheckBox_2.setText("Chat with colorful bubbles")
        self.checkBox_7.setText("Do not display ads (membership setting item)")
        self.checkBox_8.setText("Allow automatic popup windows when incoming messages")
        self.checkBox_9.setText("Use Tencent Video to play video files by default")
        self.checkBox_10.setText("Allow autoplay of magic emotes and super emotes")
        self.checkBox_11.setText("Allow the use of QQ show chat emoji")
        self.checkBox_12.setText("Always show friend chat window sidebar")
        self.checkBox_13.setText("Allow receive window jitter")
        self.checkBox_14.setText("Show hot word search hints")
        self.checkBox_15.setText("Show message history")

        # GROUP 5
        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName("widget_4")

        self.formLayout_3 = QFormLayout(self.widget_4)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.titleLabel5 = QLabel(self.widget_4)
        self.titleLabel5.setObjectName("titleLabel5")
        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.titleLabel5)
        self.checkBox_16 = QCheckBox(self.widget_4)
        self.checkBox_16.setChecked(True)
        self.checkBox_16.setObjectName("checkBox_16")
        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.checkBox_16)
        self.checkBox_17 = QCheckBox(self.widget_4)
        self.checkBox_17.setChecked(True)
        self.checkBox_17.setObjectName("checkBox_17")
        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.checkBox_17)
        self.checkBox_18 = QCheckBox(self.widget_4)
        self.checkBox_18.setChecked(True)
        self.checkBox_18.setObjectName("checkBox_18")
        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.checkBox_18)
        self.checkBox_19 = QCheckBox(self.widget_4)
        self.checkBox_19.setChecked(True)
        self.checkBox_19.setObjectName("checkBox_19")
        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.checkBox_19)

        self.verticalLayout.addWidget(self.widget_4)
        # group 5
        self.titleLabel5.setText("Information display:")
        self.checkBox_16.setText("Show level icons on profile and mini info cards")
        self.checkBox_17.setText("Display update searches on profile and mini cards")
        self.checkBox_18.setText("Show a friend's update summary in the chat window")
        self.checkBox_19.setText("Display the friend interaction logo in the chat window")

        # GROUP 6
        self.widget_5 = QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName("widget_5")

        self.formLayout_4 = QFormLayout(self.widget_5)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.titleLabel6 = QLabel(self.widget_5)
        self.titleLabel6.setObjectName("titleLabel6")
        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.titleLabel6)
        self.checkBox_20 = QCheckBox(self.widget_5)
        self.checkBox_20.setObjectName("checkBox_20")
        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.checkBox_20)
        self.checkBox_21 = QCheckBox(self.widget_5)
        self.checkBox_21.setObjectName("checkBox_21")
        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.checkBox_21)
        self.checkBox_22 = QCheckBox(self.widget_5)
        self.checkBox_22.setObjectName("checkBox_22")
        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.checkBox_22)
        self.checkBox_23 = QCheckBox(self.widget_5)
        self.checkBox_23.setObjectName("checkBox_23")
        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.checkBox_23)
        self.checkBox_24 = QCheckBox(self.widget_5)
        self.checkBox_24.setObjectName("checkBox_24")
        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.checkBox_24)
        self.right5 = QLabel(self.widget_5)
        self.right5.setObjectName("right5")
        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.right5)
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.label_3)
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.label_4)
        self.radioButton = QRadioButton(self.widget_5)
        self.radioButton.setObjectName("radioButton")
        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.radioButton)
        self.radioButton_2 = QRadioButton(self.widget_5)
        self.radioButton_2.setObjectName("radioButton_2")
        self.formLayout_4.setWidget(9, QFormLayout.FieldRole, self.radioButton_2)
        self.radioButton_3 = QRadioButton(self.widget_5)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.formLayout_4.setWidget(10, QFormLayout.FieldRole, self.radioButton_3)
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.listWidgetUser = QListWidget(self.widget_5)
        self.listWidgetUser.setFrameShape(QFrame.NoFrame)
        self.listWidgetUser.setObjectName("listWidgetUser")
        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.listWidgetUser)
        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.pushButton)
        self.formLayout_4.setLayout(11, QFormLayout.FieldRole, self.formLayout_5)

        self.verticalLayout.addWidget(self.widget_5)
        # group 6
        self.titleLabel6.setText("remind:")
        self.checkBox_20.setText("Conversation message reminder")
        self.checkBox_21.setText("New email alert")
        self.checkBox_22.setText("Enable QQ Kandian News")
        self.checkBox_23.setText("Enable one greeting message")
        self.checkBox_24.setText("Enable device connection reminders")
        self.right5.setText("When inserting an Android device, it will prompt to install or update the QQ mobile version")
        self.label_3.setText("<html><head/><body><p>You can set whether to receive notifications from Qzone in the lower right corner of the screen,<a href=\"#\"><span style=\" text-decoration: none; color:#00aaff;\">go to settings</span></a>。</p></body></html>")
        self.label_4.setText("Friends online reminder")
        self.radioButton.setText("Turn off friend online reminder")
        self.radioButton_2.setText("All friends online reminder")
        self.radioButton_3.setText("The following friends are online reminder")
        self.pushButton.setText("Add to")


        # GROUP 7
        self.widget_6 = QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setObjectName("widget_6")

        self.formLayout_6 = QFormLayout(self.widget_6)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.titleLabel7 = QLabel(self.widget_6)
        self.titleLabel7.setObjectName("titleLabel7")
        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.titleLabel7)
        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName("label_6")
        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.label_6)
        self.pushButton_2 = QPushButton(self.widget_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.pushButton_2)

        self.verticalLayout.addWidget(self.widget_6)
        # group 7
        self.titleLabel7.setText("Hotkeys:")
        self.label_6.setText("You can select the hotkey you want to change by clicking")
        self.pushButton_2.setText("set hotkey")

        # GROUP 8
        self.widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName("widget_7")

        self.formLayout_7 = QFormLayout(self.widget_7)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formLayout_7.setObjectName("formLayout_7")
        self.titleLabel8 = QLabel(self.widget_7)
        self.titleLabel8.setObjectName("titleLabel8")
        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.titleLabel8)
        self.checkBox_25 = QCheckBox(self.widget_7)
        self.checkBox_25.setObjectName("checkBox_25")
        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.checkBox_25)
        self.right6 = QLabel(self.widget_7)
        self.right6.setObjectName("right6")
        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.right6)

        self.verticalLayout.addWidget(self.widget_7)
        # group 8
        self.titleLabel8.setText("show:")
        self.checkBox_25.setText("Enable QQ to adapt to the screen DPI")
        self.right6.setText("After the option is turned off, QQ will keep the default size. After setting, you need to log in again to take effect.")


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Setting)
        self.listWidget.setCurrentRow(0)
        QMetaObject.connectSlotsByName(Setting)

        Setting.setTabOrder(self.listWidget, self.scrollArea)
        Setting.setTabOrder(self.scrollArea, self.CheckBox)
        Setting.setTabOrder(self.CheckBox, self.checkBox)
        Setting.setTabOrder(self.checkBox, self.checkBox_2)
        Setting.setTabOrder(self.checkBox_2, self.checkBox_3)
        Setting.setTabOrder(self.checkBox_3, self.checkBox_4)
        Setting.setTabOrder(self.checkBox_4, self.checkBox_5)
        Setting.setTabOrder(self.checkBox_5, self.checkBox_6)
        Setting.setTabOrder(self.checkBox_6, self.checkBox_26)
        Setting.setTabOrder(self.checkBox_26, self.checkBox_27)
        Setting.setTabOrder(self.checkBox_27, self.checkBox_28)
        Setting.setTabOrder(self.checkBox_28, self.checkBox_29)
        Setting.setTabOrder(self.checkBox_29, self.right1)
        Setting.setTabOrder(self.right1, self.right2)
        Setting.setTabOrder(self.right2, self.right3)
        Setting.setTabOrder(self.right3, self.comboBox)
        Setting.setTabOrder(self.comboBox, self.checkBox_30)
        Setting.setTabOrder(self.checkBox_30, self.checkBox_31)
        Setting.setTabOrder(self.checkBox_31, self.pushButton_5)
        Setting.setTabOrder(self.pushButton_5, self.pushButton_4)
        Setting.setTabOrder(self.pushButton_4, self.CheckBox_2)
        Setting.setTabOrder(self.CheckBox_2, self.checkBox_7)
        Setting.setTabOrder(self.checkBox_7, self.checkBox_8)
        Setting.setTabOrder(self.checkBox_8, self.checkBox_9)
        Setting.setTabOrder(self.checkBox_9, self.checkBox_10)
        Setting.setTabOrder(self.checkBox_10, self.checkBox_11)
        Setting.setTabOrder(self.checkBox_11, self.checkBox_12)
        Setting.setTabOrder(self.checkBox_12, self.checkBox_13)
        Setting.setTabOrder(self.checkBox_13, self.checkBox_14)
        Setting.setTabOrder(self.checkBox_14, self.checkBox_15)
        Setting.setTabOrder(self.checkBox_15, self.checkBox_16)
        Setting.setTabOrder(self.checkBox_16, self.checkBox_17)
        Setting.setTabOrder(self.checkBox_17, self.checkBox_18)
        Setting.setTabOrder(self.checkBox_18, self.checkBox_19)
        Setting.setTabOrder(self.checkBox_19, self.checkBox_20)
        Setting.setTabOrder(self.checkBox_20, self.checkBox_21)
        Setting.setTabOrder(self.checkBox_21, self.checkBox_22)
        Setting.setTabOrder(self.checkBox_22, self.checkBox_23)
        Setting.setTabOrder(self.checkBox_23, self.checkBox_24)
        Setting.setTabOrder(self.checkBox_24, self.radioButton)
        Setting.setTabOrder(self.radioButton, self.radioButton_2)
        Setting.setTabOrder(self.radioButton_2, self.radioButton_3)
        Setting.setTabOrder(self.radioButton_3, self.listWidgetUser)
        Setting.setTabOrder(self.listWidgetUser, self.pushButton)
        Setting.setTabOrder(self.pushButton, self.pushButton_2)
        Setting.setTabOrder(self.pushButton_2, self.checkBox_25)

    def retranslateUi(self, Setting):
        _translate = QCoreApplication.translate


class SettingsWindow(QWidget, Ui_Setting):

    def __init__(self, *args, **kwargs):
        super(SettingsWindow, self).__init__(*args, **kwargs)
        self.setStyleSheet(settings_stylesheet)
        self.setupUi(self)
        self.resize(700, 435)
        self._blockSignals = False

        # Bind scrollbar and left item events
        self.scrollArea.verticalScrollBar().valueChanged.connect(self.onValueChanged)
        self.listWidget.itemClicked.connect(self.onItemClicked)

    def onValueChanged(self, value):
        """scroll bar"""
        if self._blockSignals:
            # Preventing the change of the scroll bar when the item is clicked will trigger here
            return
        for i in range(8):  # Because there are 8 widgets on the right here
            widget = getattr(self, 'widget_%d' % i, None)
            # widget is not empty and is visible
            if widget and not widget.visibleRegion().isEmpty():
                self.listWidget.setCurrentRow(i)  # Set item selection
                return

    def onItemClicked(self, item):
        """left item"""
        row = self.listWidget.row(item)  # Get the index of the clicked item
        # Since the widget on the right is a relatively standardized method named widget_0 widget_1, it can be found through getattr
        widget = getattr(self, 'widget_%d' % row, None)
        if not widget:
            return
        # Position right position and scroll
        self._blockSignals = True
        self.scrollArea.verticalScrollBar().setSliderPosition(widget.pos().y())
        self._blockSignals = False


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    # app.setStyleSheet(open('style.qss', 'rb').read().decode('utf-8'))
    w = SettingsWindow()
    w.show()
    sys.exit(app.exec_())
