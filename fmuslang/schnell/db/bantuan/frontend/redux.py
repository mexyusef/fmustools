import json, os, pyperclip, subprocess, sys
import schnell.vendor.lark
from schnell.vendor.lark import (
	Lark,
	InlineTransformer,
)
# from lark.visitors import InlineTransformer
# from lark import (
# 	Lark,
# 	# InlineTransformer,
# )
# from lark.visitors import InlineTransformer
from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter
from anytree.importer import JsonImporter, DictImporter
from anytree.search import find, findall

from .redux_grammar import redux_grammar as bahasa
from .mapper import part_item_mapper


class TheProcessor(InlineTransformer):
	def keseluruhan(self, *instructions):
		return instructions


# @{c,r,u,d}_products
# @{a}_book
peta = lambda data: part_item_mapper[data] if data in part_item_mapper else data

def actionTypes(result, quote="'"):
	ec = 'export const'
	ready = map(lambda item: f"{ec} {item.upper()} = {quote}{item.upper()}{quote};", result)
	return '\n'.join(ready)


def process_redux_action(root):
	result = []
	for action_type in root.children:
		simple_or_compound = action_type.children[0]
		if simple_or_compound.data == 'action_type_simple':
			data = str(simple_or_compound.children[0])
			data = part_item_mapper[data] if data in part_item_mapper else data
			# print('simple:', data)
			data = peta(data)
			result.append(data)
		elif simple_or_compound.data == 'action_type_compound_left':
			indivs = simple_or_compound.children[0]
			shared = simple_or_compound.children[1]
			bersama = str(shared.children[0])
			items = [str(elem.children[0]) for elem in indivs.children]
			items = [peta(item) for item in items]
			result += [item + bersama for item in items]
		elif simple_or_compound.data == 'action_type_compound_right':
			indivs = simple_or_compound.children[1]
			shared = simple_or_compound.children[0]
			bersama = str(shared.children[0])
			items = [str(elem.children[0]) for elem in indivs.children]
			items = [peta(item) for item in items]
			result += [bersama + item for item in items]

	print('*'*40)
	print('\n'.join(result))
	return actionTypes(result)


def process_redux(code):
	kembali = ''
	parser = Lark(bahasa, start='keseluruhan').parse
	print('='*80, code, '\n')
	parsed_tree = parser(code)
	instructions = TheProcessor().transform(parsed_tree)
	
	for insn in instructions: # instructions adlh tuple
		print('insn:', insn.data)
		for tree in insn.children: # insn adlh Tree			
			# print('tree:', tree.data)
			print(tree.pretty())
			if tree.data == 'action_statement':
				action_types_statement = tree.children[0]
				kembali = process_redux_action(action_types_statement)

	return kembali


def main():
	code = 1
	while code != 'x':
		try:
			code = input('myrepl>> ')
			code = code.strip()
			if code == 'bahasa':
				print(bahasa)
			elif code != '' and code != 'x':
				res = process_redux(code)
				print(res)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)


if __name__ == '__main__':
	main()

