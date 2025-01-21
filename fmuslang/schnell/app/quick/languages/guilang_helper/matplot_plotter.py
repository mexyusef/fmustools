
class MatplotPlotter(QWidget):

    def plotting(self):
        # random data
        data = [random.random() for i in range(10)]
        # clearing old figure
        self.canvas.figure.clear()
        # create an axis
        ax = self.canvas.figure.add_subplot(111)
        # plot data
        ax.plot(data, '*-')
        # refresh canvas
        self.canvas.draw()

    def __init__(self, *args, **kwargs):
        super(MatplotPlotter, self).__init__(*args, **kwargs)
        self.canvas = MatplotCanvas(self, width=5, height=4, dpi=100)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.main_layout = QVBoxLayout(self)

        self.plot_button = QPushButton('Plot matplotter')
        self.plot_button.clicked.connect(self.plotting)
        self.plot_button.setStyleSheet('background-color: bisque;')

        self.main_layout.addWidget(self.plot_button)
        self.main_layout.addWidget(self.toolbar)
        self.main_layout.addWidget(self.canvas)

        self.canvas.axes.plot([0,1,2,3,4], [10,1,20,3,40])
