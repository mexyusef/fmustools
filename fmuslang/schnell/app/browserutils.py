from pprint import pprint
import webbrowser


def ff_newtab(alamat):
	pass


def ff_newwnd(alamat):
	pass


def ch_newtab(alamat):
	pass


def ch_newwnd(alamat):
	pass


def buka(alamat):
	from schnell.app.appconfig import programming_data
	# pprint(programming_data['j']["browsers"])
	try:
		# programming_data['j']["browsers"]["programs"]["firefox"]["exe"]
		if programming_data['j']["browsers"]["default"]:
			browser_choice = programming_data['j']["browsers"]["programs"][programming_data['j']["browsers"]["default"]]["exe"]
			print('browser_choice:', browser_choice)
			if programming_data['j']["browsers"]["default_method"]:
				if programming_data['j']["browsers"]["default_method"]=='window':
					webbrowser.get(browser_choice).open(alamat)
				else:
					webbrowser.get(browser_choice).open_tab(alamat)
			else:
				webbrowser.get(browser_choice).open(alamat)
		else:
			webbrowser.open(alamat)
	except Exception:
		webbrowser.open(alamat)
