# from creator.grammar.base import base_grammar

# from .grammar import bahasa
from grammar import bahasa

import json, os, pyperclip, subprocess, sys
import lark
from lark import (
	Lark,
	InlineTransformer,
)

# from redux_grammar import redux_grammar as bahasa
class TheProcessor(InlineTransformer):
	def keseluruhan(self, *instructions):
		return instructions


def process(code):
	parser = Lark(bahasa, start='keseluruhan').parse
	print('='*80, code, '\n')
	parsed_tree = parser(code)
	instructions = TheProcessor().transform(parsed_tree)
	for insn in instructions: # instructions adlh tuple
		for tree in insn.children: # insn adlh Tree
			print(tree.pretty())


from prompt_toolkit import prompt       
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from os.path import expanduser

myPromptSession = PromptSession(history = FileHistory(expanduser('/tmp/.langterrahist')))

def main():
	code = 1
	while code != 'x':
		try:
			# code = input('myrepl>> ')
			code = myPromptSession.prompt('myrepl>> ')
			code = code.strip()
			if code == 'bahasa':
				print(bahasa)
			elif code != '' and code != 'x':
				process(code)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)

if __name__ == '__main__':
	main()
