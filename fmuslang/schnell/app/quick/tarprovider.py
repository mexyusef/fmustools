# tar folder, etc to provide scp from android to network
from schnell.app.dirutils import get_cwd
from schnell.app.netutils import CURRENT_IP_ETH0
from schnell.app.printutils import indah4
from schnell.app.utils import perintah


def tarprovider(code):
	"""
	u -e/foldername|exclude1,exclude2
	u -e/foldername*|exclude1,exclude2

	u -e"/tar>monoproject*|node_modules,__pycache__"
	scp -P 8022 u0_a194@192.168.0.102:/data/data/com.termux/files/usef/work/random-numbers.tgz .
	"""
	foldername = ''
	excludes = []
	gz = False
	ext = 'tar'
	opts = 'cvf'
	exclusion = ''
	if '|' in code:
		foldername, excludes = code.split('|')
		excludes = [item.strip() for item in excludes.split(',')]
	else:
		foldername = code

	if foldername.endswith('*'):
		foldername = foldername.removesuffix('*')
		gz = True
		ext = 'tgz'
		opts = 'cvzf'

	if excludes:
		temp = [f"--exclude='{item}'" for item in excludes]
		exclusion = ' '.join(temp)

	if foldername:
		'''
		tar --exclude='' --exclude='' opts foldername.ext foldername
		'''
		cmd = f"tar {exclusion} -{opts} {foldername}.{ext} {foldername}"		
		perintah(cmd)
		indah4(f"""
			perintah: 	[{cmd}]
			scp: 		scp -P 8022 u0_a194@192.168.0.102:{get_cwd()}/{foldername}.{ext} .
			""", warna='green')
