
class MatplotStatic(QWidget):
    def __init__(self, *args, **kwargs):
        super(MatplotStatic, self).__init__(*args, **kwargs)
        self.canvas = MatplotCanvas(self, width=5, height=4, dpi=100)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.toolbar)
        self.main_layout.addWidget(self.canvas)

        self.canvas.axes.plot([0,1,2,3,4], [10,1,20,3,40])
