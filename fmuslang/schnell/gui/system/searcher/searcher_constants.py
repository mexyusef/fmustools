
searcher_stylesheet = """
SearchInput {
	padding: 15px;
	width: 400px;
	height: 50px;
	font-size: 24px;
	border-radius: 15px;
}

SearchSuggestion {
	border-radius: 10px;
}

CenterListView {
	border-radius: 10px;
}

CenterListView::item {
	background: #EEEEEE;
	padding: 5px;
	margin: 0;
}

CenterListView::item:hover {
	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1);
}

CenterListView::item:selected {
	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6a6ea9, stop: 1 #888dd9);
}

/* https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar */
QTabWidget::pane { /* The tab widget frame */
  border-top: 2px solid #C2C7CB;
}

QTabWidget::tab-bar {
  left: 5px; /* move to the right by 5px */
}

/* Style the tab using the tab sub-control. Note that
  it reads QTabBar _not_ QTabWidget */
QTabBar::tab {
  background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                              stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                              stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
  border: 2px solid #C4C4C3;
  border-bottom-color: #C2C7CB; /* same as the pane color */
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  /* min-width: 8ex; */
  min-width: 100px;
  padding: 2px;
  margin: 2px;
  font-size: 10pt;
}

QTabBar::tab:selected, QTabBar::tab:hover {
  background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                              stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                              stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
}

QTabBar::tab:selected {
  border-color: gold;
  background-color: bisque;
  border-bottom-color: #C2C7CB; /* same as pane color */
}

QTabBar::tab:!selected {
  margin-top: 2px; /* make non-selected tabs look smaller */
}
"""
