from schnell.vendor.lark import Lark, InlineTransformer
from schnell.vendor.lark.visitors import InlineTransformer


class TheProcessor(InlineTransformer):
	def keseluruhan(self, *instructions):
		return instructions
