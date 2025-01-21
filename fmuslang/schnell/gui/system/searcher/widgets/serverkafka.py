
"""
terima location...rootpath
abis itu python httpserver...
sekaligus dg ngrokker...
"""

import os, random, string, sys, shutil, functools, threading, time, subprocess, re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *


# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# rootdir = os.environ['ULIBPY_ROOTDIR']
# sys.path.extend([rootdir, schnelldir])
from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
# schnelldir = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
#                              file        wid    sea    sys    gui    sch    sido
sys.path.append(sidoarjodir)

class CallbackRunner:

    def __init__(self):
        self._running = True
        
    def terminate(self):
        self._running = False
        
    def run(self, callback):
        while self._running:
            callback() # masalahnya jk callback blocking...maka self._running tdk pernah dibaca
            # time.sleep(0.1)
        print('runner terminating...')


def start_runner(callback):
    c = CallbackRunner()
    t = threading.Thread(target=c.run, args=(callback,))
    t.daemon = True
    t.start()
    return t, c


def stop_runner(t, c):
    print('stop_runner, calling terminate')
    c.terminate()
    print('stop_runner, calling join')
    # t.join()
    u = threading.Thread(target=t.join)
    u.daemon = True
    u.start()
    print('stop_runner, END.')


class ServerKafkaWidget(QWidget):

    def __init__(self, publisher=None):
        super().__init__()
        self.publisher=publisher
        self.initUI()
        self.initSignals()

    def toggle_start_stop_kafka(self, checked):
        if checked:
            # masuk start
            self.start_kafka.setIcon(self.stop_icon)
            self.start_kafka.setText('Stop')
            callback = lambda: subprocess.run(self.command_kafka_start.split(), text=True)
            self.kafkathread, self.kafkarunner = start_runner(callback)
            print('start_runner, kafka')
        else:
            stop_runner(self.kafkathread, self.kafkarunner)
            self.start_kafka.setIcon(self.start_icon)
            print('stop_runner, kafka')
            self.start_kafka.setText('Start')

    def toggle_start_stop_zookeeper(self, checked):
        if checked:
            # masuk start
            self.start_zookeeper.setIcon(self.stop_icon)
            self.start_zookeeper.setText('Stop')
            callback = lambda: subprocess.run(self.command_zookeeper_start.split(), text=True)
            self.zoothread, self.zoorunner = start_runner(callback)
            print('start_runner, zookeeper')
            # t = threading.Thread(target=start_runner, args=(callback,))
        else:
            print('stopping...')
            stop_runner(self.zoothread, self.zoorunner)
            self.start_zookeeper.setIcon(self.start_icon)
            self.start_zookeeper.setText('Start')
            print('stop_runner, zookeeper')

    def create_kafka_topic(self):
        topic = self.topic_create_lineedit.text().strip()
        if topic:
            perintah = self.command_create_topic + f' {topic}'
            print('buat topic dg:', perintah)
            def run_in_thread():
                result = subprocess.run(perintah.split(), capture_output=True, text=True)
                out, err = result.stdout, result.stderr
                print(f"""create_kafka_topic
                out [{out}]
                err [{err}]
                """)
                if not err:
                    self.list_kafka_topic()
                    # out = out.removeprefix('__consumer_offsets').strip()
                    # self.list0.clear()
                    # self.list0.addItems(out.splitlines())
            x = threading.Thread(target=run_in_thread)
            x.start()

    def change_rootpath(self, rootpath):
        self.rootpath = rootpath
        self.rootpath_control.setText(self.rootpath)
        self.mkhelp_widget.change_rootpath(self.rootpath)

    def create_zookeeper_box(self):
        self.groupbox_zookeeper = QGroupBox("Zookeeper Server")
        formlayout_http = QFormLayout()
        self.zookeeper_command = r'C:/bin/kafka_2.13-3.2.1/bin/windows/zookeeper-server-start.bat C:/bin/kafka_2.13-3.2.1/config/zookeeper.properties'
        self.zookeeper_lineedit = QLineEdit(self.zookeeper_command)
        self.zookeeper_lineedit.setStyleSheet('background-color: linen; min-width: 300px;')
        formlayout_http.addRow('Zookeeper:', self.zookeeper_lineedit)

        self.start_zookeeper = QPushButton('Start')
        self.start_zookeeper.setStyleSheet("""
QPushButton {
    background-color: greenyellow;
}

QPushButton:checked {
    background-color: darksalmon;
}

QPushButton:hover {
    background-color: cornsilk;
}
""")
        self.start_zookeeper.setCheckable(True)
        self.start_zookeeper.setChecked(False)
        self.start_zookeeper.setIcon(self.start_icon)
        # self.start_zookeeper.setObjectName("button_start_http")
        self.start_zookeeper.toggled.connect(self.toggle_start_stop_zookeeper)

        layouth_zookeeper = QHBoxLayout()
        layouth_zookeeper.addLayout(formlayout_http)
        # layouth_zookeeper.addStretch(1)
        layouth_zookeeper.addSpacing(25)
        layouth_zookeeper.addWidget(self.start_zookeeper, alignment=Qt.AlignRight)
        layout_boxhttpserver = QVBoxLayout()
        layout_boxhttpserver.addLayout(layouth_zookeeper)
        self.groupbox_zookeeper.setLayout(layout_boxhttpserver)

    def create_kafka_box(self):
        self.groupbox_kafka = QGroupBox("Kafka Server")
        formlayout_http = QFormLayout()
        self.kafka_command = r'C:/bin/kafka_2.13-3.2.1/bin/windows/kafka-server-start.bat C:/bin/kafka_2.13-3.2.1/config/server.properties'
        self.kafka_lineedit = QLineEdit(self.kafka_command)
        self.kafka_lineedit.setStyleSheet('background-color: linen; min-width: 300px;')
        formlayout_http.addRow('Kafka:', self.kafka_lineedit)

        self.start_kafka = QPushButton('Start')
        self.start_kafka.setStyleSheet("""
QPushButton {
    background-color: greenyellow;
}

QPushButton:checked {
    background-color: darksalmon;
}

QPushButton:hover {
    background-color: cornsilk;
}
""")
        self.start_kafka.setCheckable(True)
        self.start_kafka.setChecked(False)
        self.start_kafka.setIcon(self.start_icon)
        # self.start_kafka.setObjectName("button_start_http")
        self.start_kafka.toggled.connect(self.toggle_start_stop_kafka)

        layouth_kafka = QHBoxLayout()
        layouth_kafka.addLayout(formlayout_http)
        # layouth_kafka.addStretch(1)
        layouth_kafka.addSpacing(25)
        layouth_kafka.addWidget(self.start_kafka, alignment=Qt.AlignRight)
        layout_boxhttpserver = QVBoxLayout()
        layout_boxhttpserver.addLayout(layouth_kafka)
        self.groupbox_kafka.setLayout(layout_boxhttpserver)

    def create_topic_box(self):
        self.groupbox_topic_create = QGroupBox("Create Topic")
        formlayout_http = QFormLayout()
        # self.topic_create_command = 'NAMATOPIK'
        self.topic_create_lineedit = QLineEdit()
        self.topic_create_lineedit.setPlaceholderText('NAMATOPIK')
        self.topic_create_lineedit.setStyleSheet('background-color: linen; min-width: 300px;')
        formlayout_http.addRow('Topic:', self.topic_create_lineedit)

        self.create_topic = QPushButton('Create')
        self.create_topic.clicked.connect(self.create_kafka_topic)

        layouth_kafka = QHBoxLayout()
        layouth_kafka.addLayout(formlayout_http)
        layouth_kafka.addStretch(1)
        layouth_kafka.addWidget(self.create_topic)
        layout_boxhttpserver = QVBoxLayout()
        layout_boxhttpserver.addLayout(layouth_kafka)
        self.groupbox_topic_create.setLayout(layout_boxhttpserver)

    def detail_kafka_topic(self):
        """
out [Topic: sample5 TopicId: rx1RklWrQjqzbAtMYf96ww PartitionCount: 1       ReplicationFactor: 1    Configs: segment.bytes=1073741824
        Topic: sample5  Partition: 0    Leader: 0       Replicas: 0     Isr: 0
]
        """
        # self.command_detail_kafka
        topic = self.topic_detail_lineedit.text().strip()
        print(f"detail_kafka_topic [{topic}]")
        if topic:
            perintah = self.command_detail_kafka + ' ' + topic
            print(f'coba jalankan [{perintah}]')
            def run_in_thread():
                result = subprocess.run(perintah.split(), capture_output=True, text=True)
                out, err = result.stdout, result.stderr
                print(f"""detail_kafka_topic
                out [{out}]
                err [{err}]
                """)
                if not err and out:
                    # out = '\n'.join(re.split(r'\s{2,}', out))
                    out = '\n'.join(re.split(r'\t', out))
                    # self.plain0.setPlainText(out)
                    self.content_for_plainedit.emit(out)
            x = threading.Thread(target=run_in_thread)
            x.start()

    def list_kafka_topic(self):
        print(f'coba jalankan [{self.command_list_kafka}]')
        result = subprocess.run(self.command_list_kafka.split(), capture_output=True, text=True)
        out, err = result.stdout, result.stderr
        print(f"""list_kafka_topic
        out [{out}]
        err [{err}]
        """)
        if not err:
            out = out.removeprefix('__consumer_offsets').strip()
            # self.list0.clear()
            # self.list0.addItems(out.splitlines())
            self.content_for_listwidget.emit(out.splitlines())


    def detail_topic_box(self):
        self.groupbox_topic_detail = QGroupBox("Topic Detail")
        formlayout_http = QFormLayout()
        # self.topic_detail_command = 'NAMATOPIK'
        self.topic_detail_lineedit = QLineEdit()
        self.topic_detail_lineedit.setPlaceholderText('NAMATOPIK')
        self.topic_detail_lineedit.setStyleSheet('background-color: linen; min-width: 300px;')
        formlayout_http.addRow('Topic:', self.topic_detail_lineedit)

        self.detail_topic = QPushButton('Detail')
        self.detail_topic.clicked.connect(self.detail_kafka_topic)

        layouth_kafka = QHBoxLayout()
        layouth_kafka.addLayout(formlayout_http)
        layouth_kafka.addStretch(1)
        layouth_kafka.addWidget(self.detail_topic)
        layout_boxhttpserver = QVBoxLayout()
        layout_boxhttpserver.addLayout(layouth_kafka)
        self.plain0 = QPlainTextEdit(self)
        layout_boxhttpserver.addWidget(self.plain0)
        self.groupbox_topic_detail.setLayout(layout_boxhttpserver)

    def create_topic_list_box(self):
        self.groupbox_topic_list = QGroupBox("List Topic")
        formlayout_http = QFormLayout()
        # kafka-topics.sh --bootstrap-server=localhost:9092 --list
        self.topic_list_command = 'C:/bin/kafka_2.13-3.2.1/bin/windows/kafka-topics --list --zookeeper localhost:2181'
        self.topic_list_lineedit = QLineEdit(self.topic_list_command)
        self.topic_list_lineedit.setStyleSheet('background-color: linen; min-width: 300px;')
        formlayout_http.addRow('Topic:', self.topic_list_lineedit)

        self.list_topic = QPushButton('List')
        self.list_topic.clicked.connect(self.list_kafka_topic)

        layouth_kafka = QHBoxLayout()
        layouth_kafka.addLayout(formlayout_http)
        layouth_kafka.addStretch(1)
        layouth_kafka.addWidget(self.list_topic)
        layout_boxhttpserver = QVBoxLayout()
        layout_boxhttpserver.addLayout(layouth_kafka)
        self.list0 = QListWidget(self)
        # self.list0.addItems(['satu', 'dua', 'tiga', 'empat', 'lima'])
        # self.list0.currentItemChanged.connect(lambda listitem: print('item changed:', listitem.text()))
        # self.list0.currentTextChanged.connect(lambda value: print('text changed:', value))
        layout_boxhttpserver.addWidget(self.list0)
        self.groupbox_topic_list.setLayout(layout_boxhttpserver)

    def command_prefixes(self):
        self.command_zookeeper_start = 'C:/bin/kafka_2.13-3.2.1/bin/windows/zookeeper-server-start.bat C:/bin/kafka_2.13-3.2.1/config/zookeeper.properties'
        self.command_kafka_start = 'C:/bin/kafka_2.13-3.2.1/bin/windows/kafka-server-start.bat C:/bin/kafka_2.13-3.2.1/config/server.properties'
        # Exception in thread "main" joptsimple.UnrecognizedOptionException: zookeeper is not a recognized option
        # self.command_create_topic = 'C:/bin/kafka_2.13-3.2.1/bin/windows/kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic'
        self.command_create_topic = 'C:/bin/kafka_2.13-3.2.1/bin/windows/kafka-topics.bat --create --bootstrap-server=localhost:9092 --replication-factor 1 --partitions 1 --topic'
        # err Exception in thread "main" joptsimple.UnrecognizedOptionException: zookeeper is not a recognized option
        # self.command_list_kafka = 'C:/bin/kafka_2.13-3.2.1/bin/windows/kafka-topics.bat --list --zookeeper localhost:2181'
        self.command_list_kafka = 'C:/bin/kafka_2.13-3.2.1/bin/windows/kafka-topics.bat --list --bootstrap-server=localhost:9092'
        self.command_detail_kafka = 'C:/bin/kafka_2.13-3.2.1/bin/windows/kafka-topics.bat --bootstrap-server=localhost:9092 --describe --topic'

    def initUI(self):

        # self.setStyleSheet(server_stylesheet)

        self.start_icon = QApplication.style().standardIcon(QStyle.SP_MediaPlay)
        self.stop_icon = QApplication.style().standardIcon(QStyle.SP_MediaStop)

        self.main_layout = QVBoxLayout()

        self.command_prefixes()
        self.create_zookeeper_box()
        self.create_kafka_box()
        self.create_topic_box()
        self.detail_topic_box()
        self.create_topic_list_box()

        server_group_layout = QVBoxLayout()        
        server_group_layout.addWidget(self.groupbox_zookeeper)
        server_group_layout.addWidget(self.groupbox_kafka)
        server_group_layout.addWidget(self.groupbox_topic_create)
        server_group_layout.addWidget(self.groupbox_topic_list)
        server_group_layout.addWidget(self.groupbox_topic_detail)
        self.main_layout.addLayout(server_group_layout)

        self.setLayout(self.main_layout)

    
    def initSignals(self):
        def set_plain_text(text):
            self.plain0.clear()
            self.plain0.setPlainText(text)
        self.content_for_plainedit.connect(lambda text: set_plain_text(text))
        self.content_for_listwidget.connect(lambda textlist: self.list0.addItems(textlist))
        self.list0.itemClicked.connect(self.klik_list_item)

    def klik_list_item(self, item: QListWidgetItem):
        a = item.text()
        print('klik:', a)
        self.topic_detail_lineedit.setText(a)
        

    content_for_plainedit = pyqtSignal(str)
    content_for_listwidget = pyqtSignal(list)


def main():
    app = QApplication([])
    ex = ServerKafkaWidget()
    # ex.setStyleSheet(background_image_stylesheet)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
