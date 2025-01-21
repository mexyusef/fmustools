
import json
import chardet

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

data_json = """
[
    {
        "name": "dashboard",
        "icon": "images/fmus-us.png"
    },
    {
        "name": "WeChat management",
        "icon": "images/fmus.png",
        "badge": [
            "hot",
            "#F8AC54"
        ],
        "items": [
            {
                "name": "Crawler project management",
                "icon": "images/fmus-us.png",
                "badge": [
                    "recommend",
                    "#23C6C9"
                ],
                "items": [
                    {
                        "name": "Tencent Classroom"
                    },
                    {
                        "name": "Taobao"
                    },
                    {
                        "name": "JD.com"
                    },
                    {
                        "name": "Tmall"
                    },
                    {
                        "name": "Retractor"
                    },
                    {
                        "name": "BOSS direct employment"
                    }
                ]
            }
        ]
    },
    {
        "name": "Crawler Deployment Management",
        "icon": "images/fmus-us.png"
    },
    {
        "name": "Crawler monitoring and management",
        "icon": "images/fmus-us.png"
    },
    {
        "name": "PyQt",
        "url": "https://github.com/mexyusef"
    }
]
"""

parsejson_stylesheet = """QTreeView {
    outline: 0px;
    /* background: rgb(47, 64, 78); */
    background: red;
}

QTreeView::item {
    min-height: 72px;    
}

QTreeView::item:hover {
    /* background: rgb(41, 56, 71); */
    background: darkviolet;
}

QTreeView::item:selected {
    /* background: rgb(41, 56, 71); */
    background: fuchsia;
}

QTreeView::item:selected:active{
    /* background: rgb(41, 56, 71); */
    background: gold;
}

QTreeView::item:selected:!active{
    /* background: rgb(41, 56, 71); */
    background: indigo;
}

QTreeView::branch:open:has-children {
    background: rgb(41, 56, 71);
}

QTreeView::branch:has-siblings:!adjoins-item {
    background: green;
}

QTreeView::branch:closed:has-children:has-siblings {
    /* background: rgb(47, 64, 78); */
    background: blue;
}

QTreeView::branch:has-children:!has-siblings:closed {
    /* background: rgb(47, 64, 78); */
    background: cyan;
}

QTreeView::branch:open:has-children:has-siblings {
    /* background: rgb(41, 56, 71); */
    background: teal;
}

QTreeView::branch:open:has-children:!has-siblings {
    /* background: rgb(141, 56, 71); */
    background: chartreuse;
}

QTreeView:branch:hover {
    /* background: rgb(241, 56, 71); */
    background: darkorange;
}

QTreeView:branch:selected {
    /* background: rgb(41, 56, 71); */
    background: lightblue;
}
"""

badge_stylesheet = """min-width: 80px;
max-width: 80px;
min-height: 38px; 
max-height: 38px;
color: white;
border:none;
border-radius: 4px;
background: %s"""

class ItemWidget(QWidget):
    """custom item"""

    def __init__(self, text, badge, *args, **kwargs):
        super(ItemWidget, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(QLabel(text, self, styleSheet='color: white;'))
        layout.addSpacerItem(QSpacerItem(60, 1, QSizePolicy.Maximum, QSizePolicy.Minimum))
        if badge and len(badge) == 2:  # Colored label on the back
            layout.addWidget(QLabel(
                badge[0], 
                self, 
                alignment=Qt.AlignCenter, 
                styleSheet = badge_stylesheet % badge[1]
            ))


class JsonTreeWidget(QTreeWidget):

    def __init__(self, *args, **kwargs):
        super(JsonTreeWidget, self).__init__(*args, **kwargs)
        self.setStyleSheet(parsejson_stylesheet)
        self.setEditTriggers(self.NoEditTriggers)
        self.header().setVisible(False)
        # Help point click event
        self.itemClicked.connect(self.onItemClicked)

        self.loadData()

    def onItemClicked(self, item):
        """item click event"""
        if item.url:  # Call the browser to open the URL
            # webbrowser.open_new_tab(item.url)
            print(item.url)

    def parseData(self, datas, parent=None):
        """Parse json data"""
        for data in datas:
            url = data.get('url', '')
            items = data.get('items', [])
            # generate item
            _item = QTreeWidgetItem(parent)
            _item.setIcon(0, QIcon(data.get('icon', '')))
            _widget = ItemWidget(
                data.get('name', ''),
                data.get('badge', []),
                self
            )
            _item.url = url  # Variable values can be set directly
            self.setItemWidget(_item, 0, _widget)
            if url:
                continue  # jump over
            # Parse children
            if items:
                self.parseData(items, _item)

    def loadData(self, path='data.json'):
        # aslinya load dari file
        # datas = open(path, 'rb').read()
        # datas = datas.decode(chardet.detect(datas).get('encoding', 'utf-8'))
        # self.parseData(json.loads(datas), self)

        # gunakan string data
        self.parseData(json.loads(data_json), self)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.main_layout = QHBoxLayout()    
        self.main_layout.addWidget(JsonTreeWidget())
        self.setLayout(self.main_layout)
        self.resize(800, 600)
        self.setWindowTitle('gila')
        self.show()

if __name__ == '__main__':
    import sys
    app = QApplication([])
    w = MainWindow()
    sys.exit(app.exec_())
