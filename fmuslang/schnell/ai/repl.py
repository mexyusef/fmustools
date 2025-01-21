import datetime, os, traceback
from textwrap import dedent

from .common import sample1, test_camera
from .hands import HandTracking
from .poses import PoseTracking
from .faces import FaceTracking, FaceMesh

keluar = [
	'x', 'q', 'exit', 'quit', 'bye'
]


class Session:
	def __init__(self, prompt):
		self.prompt = prompt

class Repl:
	def __init__(self):
		self.done = False
		self.session = Session(self.get_input)


	def get_input(self, message):
		print(message, end='')
		return input(' ')


	@property
	def prompt(self):
		now = datetime.datetime.now()
		return f'{now} ai>'


	def process(self, text):
		text = text.strip()
		print('process terima:', text)

		if text == 'sample1':
			sample1()
		elif text == 'test':
			test_camera()
		elif text == 'handtrack':
			ht = HandTracking()
			ht.run()
		elif text == 'bbox':
			ht = HandTracking()
			ht.bbox()
		elif text == 'paint':
			ht = HandTracking()
			ht.painter()
		elif text == 'dist':
			ht = HandTracking()
			ht.distance()
		elif text == 'pose1':
			ht = PoseTracking()
			ht.run()
		elif text == 'face1':
			ht = FaceTracking()
			ht.run()
		elif text == 'mesh':
			ht = FaceMesh()
			ht.run()
		else:
			print(dedent("""
			sample1
			test
			handtrack
			bbox
			paint
			dist
			pose1
			face1
			mesh
			"""))

	def run(self):
		while not self.done:
			try:
				# text = self.session.prompt(self.prompt, auto_suggest=AutoSuggestFromHistory())
				text = self.session.prompt(self.prompt)
				if text in keluar:
					break				
				elif text:
					self.process(text)
			except KeyboardInterrupt:
				continue
			except EOFError:
				break
			except Exception as error:
				print('repl run() err:', error)
				print(traceback.format_exc())

repl = Repl()

if __name__ == '__main__':
	# myrepl()
	try:
		repl.run()
	except Exception as err:
		print('terminal_repl.py:', err)
		print(traceback.format_exc())
