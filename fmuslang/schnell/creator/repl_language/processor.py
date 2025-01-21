from anytree import (
	AnyNode,
	# AsciiStyle,
	# Node,
	PreOrderIter,
	RenderTree,
)
# from anytree.importer import JsonImporter, DictImporter
# from anytree.search import find, findall
# import lark
from schnell.vendor.lark import (
	Lark,
	# InlineTransformer,
)
# from lark import (
# 	Lark,
# 	# InlineTransformer,
# )
# from schnell.app.grammar import (
# 	bahasa,
# 	filedir_bahasa,
# )
from schnell.creator.grammar import bahasa
from schnell.app.fmus.processor import TheProcessor
from schnell.app.printutils import print_copy, indah0
from schnell.app.utils import env_int


def create_node(insn, ayah, level, langchoice='py'):
  kwargs = {
			'name'			: insn.data,
			'parent'		: ayah,
			# 'workdir'		: ayah.workdir,
			'type'			: 'dahan',
			'level'			: level,
			'language'	: langchoice,
		}
  if insn.data == 'dirspec':
    kwargs.update({ 'filetype'			: 'dir', })
  elif insn.data == 'filespec':
    kwargs.update({ 'filetype'			: 'file', })

  dahan = AnyNode(**kwargs)
  return dahan


def generate_program(pohon, instructions, root=None, level=1, langchoice='py'):
  ayah = pohon if root is None else root

  for insn in instructions:

    if insn.data == 'declarative_program':
      from schnell.creator.declarative import root_declarative
      pohon = root_declarative(insn)
      # program_mode = 'declarative'
      continue

    elif insn.data == 'dirconfig':
      dirname = str(insn.children[0]) # Token
      root.dirname = dirname
      continue

    elif insn.data == 'fileconfig':
      filename = str(insn.children[0]) # Token
      root.filename = filename
      continue

    elif insn.data == 'baris_cari':
      '''
      insn: statement_berbaris_cari
        statement <- sebelumnya
          list <- kucari
        baris_cari    java
      hasil gabung:
      AnyNode(
        baris_cari='java', counter=12, id=12, language='py', level=7, 
        name='list', nick=12, type='dahan', workdir='/tmp')
      '''
      content = str(insn.children[0])
      children = [node for node in root.children]
      if children:
        aku = len(children) - 1 # children.index(insn)
        if aku >= 0:
          sebelumnya = children[aku - 1]
          # sebelumnya adlh parent utk node statement spt: var, const, function, null dst
          if sebelumnya and len(sebelumnya.children)==1:
            kucari = sebelumnya.children[0]
            # bisa assing attr ke kucari krn node kucari sudah dicreatednode.
            kucari.baris_cari = content
            if env_int('ULIBPY_FMUS_DEBUG'):
              indah0(f"\nFound baris cari {content} for node: {kucari}\n", \
                newline=True, blink=True, warna='green', bold=True, reverse=True)
      continue

    elif insn.data == 'edit_fmus' or insn.data == 'exec_fmus':
      '''
      insn: insn
        filespec
          programs
            program
              statement
                statement
                  devops_scraper
                exec_fmus
            program
      '''
      # content = str(insn.children[0])
      children = [node for node in root.children]
      if children:
        aku = len(children) - 1 # children.index(insn)
        if aku >= 0:						
          # ini adlh anynode bukan lagi astnode, name bukan data.
          wrapping_statement = children[aku - 1]
          indah0(f'edit_fmus => ketemu {wrapping_statement}\n', warna='white', bold=True)
          if wrapping_statement.name == 'statement_berbaris_cari':
            wrapping_statement = wrapping_statement.children[0]

          if wrapping_statement and len(wrapping_statement.children)==1:
            kucari = wrapping_statement.children[0]
            if insn.data == 'edit_fmus':
              kucari.edit_fmus = 1
            else:
              kucari.exec_fmus = 1
            if env_int('ULIBPY_FMUS_DEBUG'):
              indah0(f"\nNode: {kucari} ber-{insn.data} !\n", \
                newline=True, blink=True, warna='green', bold=True, reverse=True)
      continue

    elif insn.data == 'wieke':
      '''
      f<code>\replacer1\replacer2
      jk hanya backslash/wieke
      program
        statement_berwiekes					<- root
          statement									<- wrapping_statement
            const										<- kucari
          baris_cari  gun
          wieke satu								<- insn + content @aku
      
      jk ada `/baris_cari bersama backslash/wieke

      program
        statement_berwiekes					<- root
          statement_berbaris_cari		
            statement								<- wrapping_statement
              const									<- kucari
            baris_cari  gun
          wieke satu								<- insn + content @aku
      '''
      content = str(insn.children[0])
      children = [node for node in root.children]
      if children:
        aku = len(children) - 1 # children.index(insn)
        if aku >= 0:
          # ini adlh anynode bukan lagi astnode, name bukan data.
          wrapping_statement = children[aku - 1]
          indah0(f'wieke => ketemu {wrapping_statement}\n', warna='white', bold=True)
          if wrapping_statement.name == 'statement_berbaris_cari':
            wrapping_statement = wrapping_statement.children[0]

          if wrapping_statement and len(wrapping_statement.children)==1:
            kucari = wrapping_statement.children[0]
            if hasattr(kucari, 'wiekes'):
              kucari.wiekes.append(content)
            else:
              kucari.wiekes = [content]
            if env_int('ULIBPY_FMUS_DEBUG'):
              indah0(f"\nNode: {kucari} berwiekes [{kucari.wiekes}]\n", \
                newline=True, blink=True, warna='green', bold=True, reverse=True)
      continue

    elif insn.data == 'only_toc':
      '''
      f<code>#
      program
        statement_show_only_toc
          statement									<- wrapping_statement
            const										<- kucari
          only_toc									<- we are here
      '''
      children = [node for node in root.children]
      if children:
        aku = len(children) - 1 # children.index(insn)
        if aku >= 0:
          wrapping_statement = children[aku - 1]
          if wrapping_statement and len(wrapping_statement.children)==1:
            kucari = wrapping_statement.children[0]
            kucari.show_only_toc = True
            if env_int('ULIBPY_FMUS_DEBUG'):
              indah0(f"\nshow only toc for: {kucari}\n",
                newline=True, blink=True, warna='green', bold=True, reverse=True)

    elif insn.data == 'show_content':
      '''
      f<code>*
      program
        statement_show_content
          statement									<- wrapping_statement
            const										<- kucari
          show_content							<- we are here
      '''
      children = [node for node in root.children]
      if children:
        aku = len(children) - 1 # children.index(insn)
        if aku >= 0:
          wrapping_statement = children[aku - 1]
          if wrapping_statement and len(wrapping_statement.children)==1:
            kucari = wrapping_statement.children[0]
            kucari.show_content = True
            if env_int('ULIBPY_FMUS_DEBUG'):
              indah0(f"\nshow content for: {kucari}\n",
                newline=True, blink=True, warna='green', bold=True, reverse=True)

    if env_int('ULIBPY_FMUS_DEBUG')>1:
      print('[creator.repl_language.processor][generate_program] insn:', insn.pretty())

    dahan = create_node(insn, ayah, level, langchoice)
    # dahan = AnyNode(**kwargs)
    if hasattr(insn, 'children'):
      generate_program(pohon, insn.children, dahan, level+1, langchoice=langchoice)


def process(text, current_workdir='/tmp', langchoice='py'):
  pohon = AnyNode(name='root', type='root', level=0)
  pohon.children = []
  parser = Lark(bahasa, start='keseluruhan').parse
  parsed_tree = parser(text)
  processor = TheProcessor()
  instructions = processor.transform(parsed_tree)
  # bikin nodes/anak dari puncak pohon
  generate_program(pohon, instructions, langchoice=langchoice)

  for counter, node in enumerate(PreOrderIter(pohon)):
    node.counter = counter
    node.id = counter
    node.workdir = current_workdir
    if hasattr(node, 'filetype'):
      if getattr(node, 'filetype')=='dir':
        node.type = 'dir'
        current_workdir = node.workdir + '/' + node.dirname
        node.workdir = current_workdir
      elif getattr(node, 'filetype')=='file':
        node.type = 'file'
        if not hasattr(node, 'filename'):
          node.filename = node.name + '_' + str(node.counter)
  anak = pohon.children
  if len(anak) > 0:
    pohon = pohon.children[0]

  hasil = RenderTree(pohon)
  if env_int('ULIBPY_FMUS_DEBUG')>1:      
    print('[repl_language.processor.process][RenderTree(pohon)]')
    print(hasil)
  # print_copy(hasil)
  # self.generate_file(False)
  return pohon
