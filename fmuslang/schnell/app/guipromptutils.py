from PyQt5 import QtCore, QtGui, QtWidgets


def gui_masuk(judul='Masukkan', isi='Masukkan nama:'):
	# from PyQt5 import QtCore, QtGui, QtWidgets
	# app = QtWidgets.QApplication(sys.argv)
	name, done = QtWidgets.QInputDialog.getText(None, judul, isi)
	print(f"""[gui_masuk][hasil input]
	name = {name}
	done = {done}
	""")	
	return name

def gui_pilih(pilihan=['C', 'C++', 'Java', 'Python', 'Javascript'], judul='Masukkan pilihan', isi='Pilih bahasa:'):	
	# app = QtWidgets.QApplication(sys.argv)
	name, done = QtWidgets.QInputDialog.getItem(None, judul, isi, pilihan)
	name = str(name)
	print(f"""[gui_pilih][hasil input]
	name = {name}
	done = {done}
	""")
	return name

def gui_masuk_int(judul='Masukkan', isi='Masukkan integer:'):
	# from PyQt5 import QtCore, QtGui, QtWidgets
	# app = QtWidgets.QApplication(sys.argv)
	name, done = QtWidgets.QInputDialog.getInt(None, judul, isi)
	print(f"""[gui_masuk_int][hasil input]
	name = {name}
	done = {done}
	""")
	return name
gmi = gui_masuk_int


def gui_masuk_double(judul='Masukkan', isi='Masukkan double:'):
	# from PyQt5 import QtCore, QtGui, QtWidgets
	# app = QtWidgets.QApplication(sys.argv)
	name, done = QtWidgets.QInputDialog.getDouble(None, judul, isi)
	print(f"""[gui_masuk_double][hasil input]
	name = {name}
	done = {done}
	""")
	return name
