
import os, random, string, sys
import time, threading
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.animation import TimedAnimation
from matplotlib.lines import Line2D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.ticker as ticker

url = 'https://gist.githubusercontent.com/johnburnmurdoch/4199dbe55095c3e13de8d5b2e5e5307a/raw/fa018b25c24b7b5f47fd0568937ff6c04e384786/city_populations'
df = pd.read_csv(url)
colors = dict(zip(
    ["India", "Europe", "Asia", "Latin America", "Middle East", "North America", "Africa"],
    ["#adb0ff", "#ffb3ff", "#90d595", "#e48381", "#aafbff", "#f7bb5f", "#eafb50"]
))

# group_lk is mapping between name and group values.
# jadi utk kota x: negara/benua y => tentukan warna
group_lk = df.set_index('name')['group'].to_dict()
dff_dx_dict = {}
for tahun in range(1500,2020):
    hasil_dff = df[df['year'].eq(tahun)].sort_values(by='value', ascending=True).tail(10)
    hasil_dx = hasil_dff['value'].max() // 200
    hasil_warna = [colors[group_lk[x]] for x in hasil_dff['name']]
    value_name = zip(hasil_dff['value'], hasil_dff['name'])
    dff_dx_dict[tahun] = {
        'dff': hasil_dff,
        'dx': hasil_dx,
        'color': hasil_warna,
        'value_name': value_name,
    }

class MatplotRace(QWidget):

    def draw_barchart(self, current_year):
        dff = dff_dx_dict[current_year]['dff']
        dx = dff_dx_dict[current_year]['dx']
        warna = dff_dx_dict[current_year]['color']
        value_name = dff_dx_dict[current_year]['value_name']

        # print('tahun:', current_year, 'dff:', dff)
        self.static_canvas_axes.clear()
        # barh utk horizontal barchart
        self.static_canvas_axes.barh(dff['name'], dff['value'], color=warna)
        # iterate over the values to plot labels, values (Tokyo, Asia, 38194.2)
        for i, (value, name) in enumerate(value_name):
            # nama kota
            self.static_canvas_axes.text(value-dx, i,     name,             size=14, weight=600, ha='right', va='bottom')
            # group/benua
            self.static_canvas_axes.text(value-dx, i-.25, group_lk[name],   size=10, color='#444444', ha='right', va='baseline')
            # jumlah dalam ribu
            self.static_canvas_axes.text(value+dx, i,     f'{value:,.0f}',  size=14, ha='left', va='center')
        # Text tahun yg sedang berjalan
        self.static_canvas_axes.text(1, 0.4, current_year, transform=self.static_canvas_axes.transAxes, color='#777777', size=46, ha='right', weight=800)


    def sekali(self):
        self.static_canvas_axes.text(0, 1.06, 'Population', transform=self.static_canvas_axes.transAxes, size=12, color='#777777')
        self.static_canvas_axes.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
        self.static_canvas_axes.xaxis.set_ticks_position('top')
        self.static_canvas_axes.tick_params(axis='x', colors='#777777', labelsize=12)
        self.static_canvas_axes.margins(0, 0.01)
        self.static_canvas_axes.grid(which='major', axis='x', linestyle='-')
        self.static_canvas_axes.set_axisbelow(True)
        self.static_canvas_axes.text(0, 1.15, 'City fights from 1500 to 2018', transform=self.static_canvas_axes.transAxes, size=24, weight=600, ha='left', va='top')
        # self.static_canvas_axes.text(1, 0, 'yusef314159', transform=self.static_canvas_axes.transAxes, color='#777777', ha='right', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
        

    def __init__(self):
        super().__init__()
        self.prev_year = 0
        # self._main = QWidget()
        # self.setCentralWidget(self._main)
        layout = QVBoxLayout(self)

        self.static_canvas_figure = Figure(figsize=(15, 8))
        self.static_canvas_axes = self.static_canvas_figure.add_subplot()
        self.static_canvas = FigureCanvas(self.static_canvas_figure)

        # Ideally one would use self.addToolBar here, but it is slightly
        # incompatible between PyQt6 and other bindings, so we just add the
        # toolbar as a plain widget instead.
        layout.addWidget(NavigationToolbar(self.static_canvas, self))
        layout.addWidget(self.static_canvas)

        self.sekali()
        self.year = 1500

        self._timer = self.static_canvas.new_timer(250)
        self._timer.add_callback(self._update_canvas)
        self._timer.start()

    def _update_static(self):
        if self.year <= 2018:
            self.year += 1
            self.draw_barchart(self.year)
            self.static_canvas_figure.canvas.draw()

    def _update_canvas(self):
        # self._update_canvas_dynamic()
        self._update_static()
