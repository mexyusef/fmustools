# from schnell.app.autoutils import confirm
import os, re, json
from ast import literal_eval as literal
from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter

# from anytree.importer import JsonImporter, DictImporter
from anytree.search import find, findall

from database.langnew import programming_languages


from schnell.app.appconfig import programming_data

from schnell.vendor.lark import Lark
from schnell.app.dirutils import joiner, isdir, isfile, ayah, pemisah_unix_to_windows
from schnell.app.fileutils import (
    file_lines,
    line_contains,
    get_definition_by_key_permissive_start,
    get_definition_by_key_permissive_start_with_lineno,
    get_daftar,
    create_if_empty_file,
    replace_if_contain_links,
)
from schnell.app.fmusutils import fmus
from schnell.app.printutils import (
    indah0,
    indah4,
    indah_enumerate,
    print_copy,
    print_copy_enumerate_list,
    print_file,
    print_file_pigmen,
    filter_print_latest_files,
)
from schnell.app.utils import (
    env_exist,
    env_get,
    env_int,
    env_expand,
    perintah,
    perintahsp_simple,
    perintah_shell,
    python_package,
    platform,
    Launcher,
    perintah as komando,
    wslpath_to_linuxpath,
    trycopy,
    trypaste,
    perintahsp_outerr_as_shell,
    tidur,
)
from schnell.app.vscodeutils import vscode_edit_at_line
from schnell.app.stringutils import startswith_absolute_folder
from schnell.app.generator import Generator
from schnell.ai.autolib import auto_process

from schnell.creator.declarative.handler import (
    remove_mapper_keys,
    add_mapper_keys,
    values_from_clipboard,
    reset_mapper_keys,
)
from schnell.creator.context import (
    current_decl_filename,
    context,
    context as creator_context,
    languages,
    Lang,
    embeddable,
    modifiers,
    get_replaceable,
    get_filepath,
    context_subdirs,
)
from schnell.creator.helper import (
    template_default_entry,
    template_use_entry,
    template_reverse_entry,
    template_entrify,
    template_index_mk,
    template_link,
    CODE,
    TERM,
    template_unless,
    template_pick,
)
from schnell.creator.bindings import process_fmus
from schnell.creator.config import Configuration
from schnell.creator.grammar import bahasa
from schnell.creator.language import TheProcessor

from schnell.creator.declarative import root_declarative
from schnell.creator.declarative.handler import load_from_ini_file
from schnell.creator.declarative.mapper import reload_values
from schnell.creator.declarative.mapper import (
    elem_mapper,
    attr_mapper,
    cdata_mapper,
    value_mapper,
)

from schnell.creator.package_json import process_packagejson

from schnell.db.replservice_clipboard import provide_for_clipboard
from schnell.db.replservice_helper import declarative


ULIBPY_MKFILE_KEY = programming_data["j"]["schnell"]["app"]["configuration"][
    "ULIBPY_MKFILE_KEY"
]
ULIBPY_BARIS_CARI_SEPARATOR = programming_data["j"]["schnell"]["app"]["configuration"][
    "ULIBPY_BARIS_CARI_SEPARATOR"
]
ULIBPY_WIEKES_TEMPLATE_PREFIX = programming_data["j"]["schnell"]["app"][
    "configuration"
]["ULIBPY_WIEKES_TEMPLATE_PREFIX"]
ULIBPY_WIEKES_CAPITALIZE_SYMBOL = programming_data["j"]["schnell"]["app"][
    "configuration"
]["ULIBPY_WIEKES_CAPITALIZE_SYMBOL"]
ULIBPY_WIEKES_PLURALIZE_SYMBOL = programming_data["j"]["schnell"]["app"][
    "configuration"
]["ULIBPY_WIEKES_PLURALIZE_SYMBOL"]
ULIBPY_WIEKES_LOWERIZE_SYMBOL = programming_data["j"]["schnell"]["app"][
    "configuration"
]["ULIBPY_WIEKES_LOWERIZE_SYMBOL"]
ULIBPY_WIEKES_UPPERIZE_SYMBOL = programming_data["j"]["schnell"]["app"][
    "configuration"
]["ULIBPY_WIEKES_UPPERIZE_SYMBOL"]
ULIBPY_SEPARATE_CONTENT_RESULT = programming_data["j"]["schnell"]["app"][
    "configuration"
]["ULIBPY_SEPARATE_CONTENT_RESULT"]
ULIBPY_WSL_ADDRESS = programming_data["j"]["schnell"]["app"]["configuration"][
    "ULIBPY_WSL_ADDRESS"
]
ULIBPY_BASEDIR = programming_data["j"]["schnell"]["app"]["configuration"][
    "ULIBPY_BASEDIR"
]

category_delimiter = "|"
entry_bahasa = [
    item
    for item in bahasa.splitlines()
    if item and ":" in item and "HURUF" not in item and item.endswith('"')
]


class ReplService:
    def __init__(self):
        # self.printer = output_callback
        self.output = ""
        self.metaresult = {}
        self.complete_output = False
        self.last_file = None
        self.last_lineno = 0

        self.config = Configuration(self)

        self.parser = Lark(bahasa, start="keseluruhan").parse
        self.processor = TheProcessor()
        self.pohon = AnyNode(name="root", type="root", level=0)
        self.previous_pohon = self.pohon

        self.replaceable = get_replaceable()

    def clear_pohon(self):
        self.pohon = AnyNode(name="root", type="root", level=0)
        self.pohon.children = []

    def create_node(self, insn, ayah, level):
        kwargs = {
            "name": insn.data,
            "parent": ayah,
            # 'workdir'		: ayah.workdir,
            "type": "dahan",
            "level": level,
            "language": context["current_language"],
        }
        if insn.data == "dirspec":
            kwargs.update(
                {
                    "filetype": "dir",
                }
            )
        elif insn.data == "filespec":
            kwargs.update(
                {
                    "filetype": "file",
                }
            )
        # tambah kemampuan utk choose dari alternatif code generation di file
        if insn.data.endswith("_ask"):
            strip = insn.data.replace("_ask", "", 1)
            kwargs["name"] = strip
            kwargs["choosing"] = 1

        elif insn.data.endswith("_filter"):
            strip = insn.data.replace("_filter", "", 1)
            kwargs["name"] = strip
            kwargs["filtering"] = 1

        dahan = AnyNode(**kwargs)
        return dahan

    def generate_program(self, instructions, root=None, level=1):
        ayah = self.pohon if root is None else root
        self.program_mode = "normal"

        for insn in instructions:  # instructions adlh tuple
            if insn.data == "declarative_program":
                self.pohon, self.output = root_declarative(insn, as_service=True)
                self.program_mode = "declarative"
                continue

            # utk bentuk tree token
            # maka perlu skip sblm generate node
            # otherwise: 'Token' obj has no attribute 'data'
            # jk insn adlh dirconfig maka kita attach ke parent/root = dirspec
            elif insn.data == "dirconfig":
                dirname = str(insn.children[0])  # Token
                root.dirname = dirname
                continue

            elif insn.data == "fileconfig":
                filename = str(insn.children[0])  # Token
                root.filename = filename
                continue

            elif insn.data == "library_usage":
                libraryname = str(insn.children[0])  # Token
                root.library_usage = libraryname
                continue

            elif insn.data == "frontend_usage":
                libraryname = str(insn.children[0])  # Token
                root.frontend_usage = libraryname
                continue

            # elif insn.data == 'statement_berbaris_cari':
            # 	"""
            # 	| statement baris_cari
            # 	baris_cari: "`" HURUF_FOLDER_LAMA_BERBINTANG
            # 	utk oprek
            # 	statement ` baris_cari
            # 	^ ayah      ^ insn
            # 	insn sekarang (baris_cari) tidak menjadi node
            # 	tapi jadi atribut utk insn sebelumnya = ayah

            # 	insn: program
            # 	statement_berbaris_cari
            # 		statement
            # 			null
            # 		baris_cari  nullab
            # 	"""
            # 	# modify statement -> null
            # 	node_statement = insn.children[0]
            # 	real_node_statement = insn.children[0].children[0]
            # 	node_baris_cari = insn.children[1]
            # 	text_node_baris_cari = str(node_baris_cari.children[0])
            # 	real_node_statement.baris_cari = text_node_baris_cari
            # 	continue

            elif insn.data == "baris_cari":
                """
                insn: statement_berbaris_cari
                        statement <- sebelumnya
                                list <- kucari
                        baris_cari    java
                hasil gabung:
                AnyNode(
                        baris_cari='java', counter=12, id=12, language='py', level=7,
                        name='list', nick=12, type='dahan', workdir='/tmp')
                """
                content = str(insn.children[0])
                children = [node for node in root.children]
                if children:
                    aku = len(children) - 1  # children.index(insn)
                    if aku >= 0:
                        sebelumnya = children[aku - 1]
                        # sebelumnya adlh parent utk node statement spt: var, const, function, null dst
                        if sebelumnya and len(sebelumnya.children) == 1:
                            kucari = sebelumnya.children[0]
                            # bisa assing attr ke kucari krn node kucari sudah dicreatednode.
                            kucari.baris_cari = content

                continue

            elif insn.data == "edit_fmus" or insn.data == "exec_fmus":
                """
                insn: insn
                        filespec
                                programs
                                        program
                                                statement
                                                        statement
                                                                devops_scraper
                                                        exec_fmus
                                        program
                """
                # content = str(insn.children[0])
                children = [node for node in root.children]
                if children:
                    aku = len(children) - 1  # children.index(insn)
                    if aku >= 0:
                        # ini adlh anynode bukan lagi astnode, name bukan data.
                        wrapping_statement = children[aku - 1]
                        # indah0(f'edit_fmus => ketemu {wrapping_statement}\n', warna='white', bold=True)
                        if wrapping_statement.name == "statement_berbaris_cari":
                            wrapping_statement = wrapping_statement.children[0]

                        if wrapping_statement and len(wrapping_statement.children) == 1:
                            kucari = wrapping_statement.children[0]
                            if insn.data == "edit_fmus":
                                kucari.edit_fmus = 1
                            else:
                                kucari.exec_fmus = 1

                continue

            elif insn.data == "wieke":
                """
                program
                        statement_berwiekes					<- root
                                statement_berbaris_cari
                                        statement					<- wrapping_statement
                                                const					<- kucari
                                        baris_cari  gun
                                wieke satu						<- insn + content @aku
                """
                content = str(insn.children[0])
                children = [node for node in root.children]
                if children:
                    aku = len(children) - 1  # children.index(insn)
                    if aku >= 0:
                        # ini adlh anynode bukan lagi astnode, name bukan data.
                        wrapping_statement = children[aku - 1]
                        # indah0(f'wieke => ketemu {wrapping_statement}\n', warna='white', bold=True)
                        if wrapping_statement.name == "statement_berbaris_cari":
                            wrapping_statement = wrapping_statement.children[0]

                        if wrapping_statement and len(wrapping_statement.children) == 1:
                            kucari = wrapping_statement.children[0]
                            if hasattr(kucari, "wiekes"):
                                kucari.wiekes.append(content)
                            else:
                                kucari.wiekes = [content]

                continue

            elif insn.data == "only_toc":
                """
                program
                        statement_show_only_toc
                                statement									<- wrapping_statement
                                        const									<- kucari
                                only_toc									<- we are here
                """
                children = [node for node in root.children]
                if children:
                    aku = len(children) - 1  # children.index(insn)
                    if aku >= 0:
                        wrapping_statement = children[aku - 1]
                        if wrapping_statement and len(wrapping_statement.children) == 1:
                            kucari = wrapping_statement.children[0]
                            kucari.show_only_toc = True
                            if env_int("ULIBPY_FMUS_DEBUG"):
                                indah0(
                                    f"\nshow only toc for: {kucari}\n",
                                    newline=True,
                                    blink=True,
                                    warna="green",
                                    bold=True,
                                    reverse=True,
                                )

            dahan = self.create_node(insn, ayah, level)

            if hasattr(insn, "children"):
                self.generate_program(insn.children, dahan, level + 1)

    def generate_file(self, generate_fmus=True):
        """
        dipanggil dengan $ gen
        """
        # createdir = joiner(self.config.run_configuration['cwd'], 'createdb')
        # libdir = joiner(createdir, 'libraries')
        # libfile = 'tasks.mk'
        # frontenddir = joiner(createdir, 'web', 'react')
        baris = ULIBPY_MKFILE_KEY  # env_get('ULIBPY_MKFILE_KEY', 'default') # careful jk dijalankan dari sistem yg gak load .env!
        dahanz = []  # daftar keyword file yg diproses
        daftarz = []
        filepath_terprocezz = []
        # utk generate fmus, konversi pohon ke dir+file
        # dan program content semua masuk file
        for pohon in findall(self.pohon, lambda node: node.type == "dir"):
            pohon.operations = ["create_dir"]

        files_clipboard_content = ""
        # ini akibatnya, hanya generate content jk dia dicakup dalam file
        for pohon in findall(self.pohon, lambda node: node.type == "file"):
            # proses masing-masing file, generate code dan hilangkan children
            pohon.workdir += "/" + pohon.filename  # + '.' + pohon.language

            if not hasattr(pohon, "children"):
                pohon.operations = ["content_file=EMPTY"]
            else:
                content = ""
                for node in PreOrderIter(pohon):
                    if embeddable(node.name):
                        content += node.name + " "
                        dahanz.append(node.name)

                    elif node.type == "dahan" and node.name in self.replaceable:
                        # filepath = joiner(self.createdir, 'by-langs', node.name + '.' + context['current_language'] + '.mk')
                        # update 11 dec 22, bisa replaceable language
                        active_language = context["current_language"]
                        if context["override_language"]:
                            active_language = context["override_language"]
                        filepath = get_filepath(node.name, active_language)
                        if context["override_language"]:
                            # clear after usage
                            context["override_language"] = None
                        # if int(env_get('ULIBPY_FMUS_DEBUG')):
                        # 	indah0(f'dahan [{node.name}] itu replaceable, filepath: {filepath}', warna='red', reverse=True, newline=True)

                        self.last_file = filepath  # agar bisa ~e utk edit

                        if isfile(filepath):
                            # stlh ketemu filepath, tinggal tentukan baris_cari/baris
                            # _ask/choosing diminta pilih sekarang
                            # if hasattr(node, 'choosing'):
                            # 	indah0(f"Choose variance {filepath}", warna='bright_green', reverse=True, newline=True)
                            # 	baris = self.temporary_prompt(HTML(f"Masukkan pilihan \"{node.name}\": "), choices=get_daftar(filepath))

                            if hasattr(node, "baris_cari"):
                                baris = node.baris_cari.rstrip()
                                # cek jk ada bentuk: cari1~cari2~cari3 maka semuanya jadi kondisi
                                cari_separator = ULIBPY_BARIS_CARI_SEPARATOR  # env_get('ULIBPY_BARIS_CARI_SEPARATOR')

                                if cari_separator in baris:
                                    daftar = get_daftar(filepath)
                                    temu = [
                                        item
                                        for item in daftar
                                        if all(
                                            [
                                                elem in item
                                                for elem in baris.split(cari_separator)
                                            ]
                                        )
                                    ]
                                    if temu:
                                        baris = temu[0]

                                # if int(env_get('ULIBPY_FMUS_DEBUG')):
                                # 	indah0(f"Use baris_cari [{baris}] for node [{node.name}].", warna='bright_green', reverse=True, newline=True)

                            # print(f'[replservice][generate_file] filepath={filepath}, baris={baris}')
                            (
                                result,
                                lineno,
                            ) = get_definition_by_key_permissive_start_with_lineno(
                                filepath, baris
                            )
                            # print(f'[replservice][generate_file] result={result}, lineno={lineno}')
                            result = result.strip()
                            if hasattr(node, "show_only_toc"):
                                # hanya keluarkan toc
                                result = get_daftar(filepath, stringified=True)
                            self.last_lineno = lineno

                            # replacer wieke
                            if hasattr(node, "wiekes"):
                                prefix = ULIBPY_WIEKES_TEMPLATE_PREFIX  # env_get('ULIBPY_WIEKES_TEMPLATE_PREFIX')
                                capper = ULIBPY_WIEKES_CAPITALIZE_SYMBOL  # env_get('ULIBPY_WIEKES_CAPITALIZE_SYMBOL')
                                wiekeplural = ULIBPY_WIEKES_PLURALIZE_SYMBOL  # ('ULIBPY_WIEKES_PLURALIZE_SYMBOL')
                                wiekelower = ULIBPY_WIEKES_LOWERIZE_SYMBOL  # ('ULIBPY_WIEKES_LOWERIZE_SYMBOL')
                                wiekeupper = ULIBPY_WIEKES_UPPERIZE_SYMBOL  # env_get('ULIBPY_WIEKES_UPPERIZE_SYMBOL')
                                replacers = node.wiekes
                                # __wiekes01, __wiekes02 krn gak mungkin sampai > 100
                                templates = [
                                    prefix + str(angka).zfill(2)
                                    for angka in range(1, len(replacers) + 1)
                                ]

                                for index, wieke in enumerate(replacers):
                                    """
                                    misal
                                    const [__wieke01, set__wieke00^^] = useState...
                                    \monkey
                                    hasilkan:
                                    const [monkey, setMonkey] == useState...
                                    """
                                    result = result.replace(
                                        templates[index] + capper, wieke.capitalize()
                                    )
                                    result = result.replace(
                                        templates[index] + wiekeplural, wieke + "s"
                                    )
                                    result = result.replace(
                                        templates[index] + wiekelower, wieke.lower()
                                    )
                                    result = result.replace(
                                        templates[index] + wiekeupper, wieke.upper()
                                    )
                                    result = result.replace(templates[index], wieke)

                            dahanz.append(f"{node.name}/{baris}")
                            if filepath not in filepath_terprocezz:
                                daftarz.append(get_daftar(filepath))

                            # hanya tambah pemisah jk >1 entries dan stlh entry pertama
                            # if env_exist('ULIBPY_SEPARATE_CONTENT_RESULT') and filepath_terprocezz:
                            # 	content += env_get('ULIBPY_SEPARATE_CONTENT_RESULT') + f" {node.name}/{baris}\n"
                            if filepath_terprocezz:
                                content += ULIBPY_SEPARATE_CONTENT_RESULT  # env_get('ULIBPY_SEPARATE_CONTENT_RESULT') + f" {node.name}/{baris}\n"

                            filepath_terprocezz.append(filepath)
                            # node.name bisa embedded (public, static, void/int) -> space
                            # atau non-embedded (full statement) -> \n
                            content += result + "\n"
                            baris = ULIBPY_MKFILE_KEY  # env_get('ULIBPY_MKFILE_KEY') # 'default' # kembalikan, klo gak next node menggunakan baris dari hasil choosing node skrg

                    pohon.operations = ["content_file=" + content]

                pohon.children = []

            if not generate_fmus:
                """
                gabungkan content dari berbagai statement ke satu content besar ready to print
                """
                # if int(env_get('ULIBPY_FMUS_DEBUG')):
                # 	indah0(f"*FINAL* adding to files_clipboard_content = [{content[:100]}\n...]", warna='bright_green', bold=True, newline=True)
                files_clipboard_content += content

        # """
        # daftar isi bisa di atas atau dibawah dg ULIBPY_DAFTARZ_ABOVE
        # daftar isi bisa dipisah | atau \n dg jumlah entries dg ULIBPY_DAFTARZ_BYLINE_AFTER
        # """
        pipa = " | "
        nl = "\n"
        entries_mulai_newline = env_int("ULIBPY_DAFTARZ_BYLINE_AFTER")
        pipa_or_newline = (
            lambda entries: pipa if len(entries) <= entries_mulai_newline else nl
        )
        # daftarz_sorted = sorted(daftarz) if env_int('ULIBPY_DAFTARZ_SORTED') else daftarz
        daftarz_sorted = daftarz  # sudah tersorted

        daftar_isi = "\n".join(
            [
                (pipa_or_newline(entries)).join(sorted(entries))
                for entries in daftarz_sorted
            ]
        )
        isi_terpilih = "-" * 10 + " | ".join(dahanz) + "-" * 10

        if env_int("ULIBPY_DAFTARZ_ABOVE"):
            indah4(daftar_isi, warna="blue")
            self.metaresult.update({"toc": daftar_isi})
            if self.complete_output:
                self.output += daftar_isi + "\n"
                self.output += "-" * 40 + "\n"

        self.output += files_clipboard_content
        trycopy(files_clipboard_content)
        indah4(isi_terpilih, warna="yellow")
        self.metaresult.update({"filter": isi_terpilih})
        if self.complete_output:
            self.output += isi_terpilih + "\n"

        if not env_int("ULIBPY_DAFTARZ_ABOVE"):
            indah4(daftar_isi, warna="blue")
            self.metaresult.update({"toc": daftar_isi})
            if self.complete_output:
                self.output += "-" * 40 + "\n"
                self.output += daftar_isi + "\n"

    def fastmapper(self, text, meta_input=None, strip=True):
        from .fastmapper import fast_mapper

        self.output = ""

        if strip:
            text = text.strip()

        if text == "ping":
            self.output = "pong (fastmapper)"
        elif text == "reload":
            fast_mapper.reload()
            self.output = fast_mapper.toc()
        elif text.startswith("load"):
            filename = text.removeprefix("load").strip()
            if filename:
                fast_mapper.load(filename)
            self.output = fast_mapper.toc()
        elif text == "toc":
            self.output = fast_mapper.toc()
        elif text == "files":
            self.output = fast_mapper.files()
        elif text == "edit":
            fast_mapper.edit()
            self.output = "OK"
        elif text == "tree":
            if meta_input:
                docinfo = meta_input["metaDocument"]
                filepath = docinfo["filename"]
                folder = ayah(filepath, 1)
                out, err = perintahsp_outerr_as_shell(f"tree {folder}")
                if out:
                    self.output = out
                elif err:
                    self.output = err
        else:
            self.output, self.metaresult = fast_mapper.process(text)
            if not self.output:
                print("replservice, output empty tapi ada metaresult:", self.metaresult)

        return self.output, self.metaresult

    def run_program(self, text):
        """
        jalankan spt ff dsb
        tapi kita pengen bisa
        scala/ff
        kt/ff
        sblm self.parser(text)

        di generate_file ada
        filepath = get_filepath(node.name, context['current_language'])
        """
        self.clear_pohon()

        parsed_tree = None
        try:
            parsed_tree = self.parser(text)
        except Exception as err:
            indah4(
                f"""[replservice][run_program exception]
			err = {err}
			""",
                warna="red",
            )
            return
        instructions = self.processor.transform(parsed_tree)
        self.generate_program(instructions)
        current_workdir = self.config.run_configuration["working_folder"]

        for counter, node in enumerate(PreOrderIter(self.pohon)):
            node.counter = counter
            node.id = counter  # default sama dg counter tapi bisa diubah
            node.nick = counter  # default sama dg counter tapi bisa diubah
            node.workdir = current_workdir

            if hasattr(node, "filetype"):
                if getattr(node, "filetype") == "dir":
                    current_workdir = node.workdir + "/" + node.dirname
                    node.workdir = current_workdir
                    node.type = "dir"

                elif getattr(node, "filetype") == "file":
                    node.type = "file"
                    if not hasattr(node, "filename"):
                        node.filename = node.name + "_" + str(node.counter)

        anak = self.pohon.children
        if len(anak) > 0:
            self.pohon = self.pohon.children[0]

        self.previous_pohon = self.pohon

        # generate file ini copy clipboard juga...
        if (
            self.config.run_configuration["print_after_process"]
            and self.program_mode == "normal"
        ):
            self.generate_file(False)

    def set_last_file_lineno(self, filepath, lineno=0):
        self.last_file = filepath
        self.last_lineno = lineno

    def process(self, text, meta_input=None, strip=True):
        self.output = ""
        self.metaresult = {}

        if strip:
            text = text.strip()

        if text == "ping":
            self.output = "pong"

        elif text.startswith("#"):  # oprek: elem, attr, cdata, value, dll
            """
            #+p
            #+clip(e,a,c,v)
            #+e
            #+a
            #+c
            #+v
            #-e
            #-a
            #-c
            #-v
            UPD 25/3/23, reloadvalues
            ###
            """
            text = text.removeprefix("#").strip()
            kembali = ""
            if text == "##":
                # C:\Users\usef\work\sidoarjo\schnell\creator\declarative\mapper.py
                reload_values()
                self.output += "values reloaded..."
            elif text == "ls":  # ls
                self.output += "*" * 20 + f"elem_mapper\n"
                self.output += json.dumps(elem_mapper, indent=4)
                self.output += "*" * 20 + f"attr_mapper\n"
                self.output += json.dumps(attr_mapper, indent=4)
                self.output += "*" * 20 + f"cdata_mapper\n"
                self.output += json.dumps(cdata_mapper, indent=4)
                self.output += "*" * 20 + f"value_mapper\n"
                self.output += json.dumps(value_mapper, indent=4)
            elif text.startswith("load="):
                """
                #load=ULIBPY_ROOTDIR/reactnative.ini
                #load=0|ULIBPY_ROOTDIR/reactnative.ini
                #load=1|ULIBPY_ROOTDIR/reactnative.ini
                #load=2|ULIBPY_ROOTDIR/reactnative.ini
                #load=3|ULIBPY_ROOTDIR/reactnative.ini
                """
                code = text.removeprefix("load=").strip()
                if code:
                    which = 0
                    if "|" in code:
                        which, filepath = [item.strip() for item in code.split("|")]
                        which = int(which)  # oh lord
                        load_from_ini_file(filepath, which=which)
                        self.output += f"{which} loaded from {filepath}"
                    else:
                        load_from_ini_file(code, 0)
                        self.output += f"{which} loaded from {code}"
            elif text.startswith("+p:"):
                """
                #+p:a-z
                #+p:a-k,p
                #+p:abcde
                """
                code = text.removeprefix("+p:").strip()
                self.output += provide_for_clipboard(code)
            elif text.startswith("+clip"):
                """
                isi clipboard dg
                k1=v1
                k2=v2
                #+clipe
                #+clipa
                #+clipc
                #+clipv
                """
                code = text.removeprefix("+clip").strip()
                if code == "e":
                    print("[db.replservice] clipboarding elem")
                    kembali = values_from_clipboard(which=0)
                elif code == "a":
                    print("[db.replservice] clipboarding attr")
                    kembali = values_from_clipboard(which=1)
                elif code == "c":
                    print("[db.replservice] clipboarding cdata/text")
                    kembali = values_from_clipboard(which=2)
                elif code == "v":
                    print("[db.replservice] clipboarding value-attr")
                    kembali = values_from_clipboard(which=3)
                self.output += str(kembali)
            elif text.startswith("+e"):
                """
                #+e
                tambah elem/tag ke kamus
                """
                code = text.removeprefix("+e").strip()
                if code:
                    print("[db.replservice] literalling:", code)
                    kode = literal(code)
                    if isinstance(kode, dict):
                        kembali = add_mapper_keys(kode)
                        self.output += str(kembali)
            elif text.startswith("+a"):
                """
                tambah attribute/key ke kamus
                """
                code = text.removeprefix("+a").strip()
                if code:
                    print("[db.replservice] literalling:", code)
                    kode = literal(code)
                    if isinstance(kode, dict):
                        kembali = add_mapper_keys(kode, which=1)
                        self.output += str(kembali)
            elif text.startswith("+c"):
                """
                tambah cdata/text ke kamus
                """
                code = text.removeprefix("+c").strip()
                if code:
                    print("[db.replservice] literalling:", code)
                    kode = literal(code)
                    if isinstance(kode, dict):
                        kembali = add_mapper_keys(kode, which=2)
                        self.output += str(kembali)
            elif text.startswith("+v"):
                """
                tambah value attr ke kamus
                """
                code = text.removeprefix("+v").strip()
                if code:
                    print("[db.replservice] literalling:", code)
                    kode = literal(code)
                    if isinstance(kode, dict):
                        kembali = add_mapper_keys(kode, which=3)
                        self.output += str(kembali)
            elif text.startswith("-e"):
                """
                hapus elem/tag ke kamus
                """
                code = text.removeprefix("-e").strip()
                if code:
                    print("[db.replservice] literalling:", code)
                    kode = literal(code)
                    if isinstance(kode, list):
                        kembali = remove_mapper_keys(kode)
                        self.output += str(kembali)
            elif text.startswith("-a"):
                """
                hapus attribute/key ke kamus
                """
                code = text.removeprefix("-a").strip()
                if code:
                    print("[db.replservice] literalling:", code)
                    kode = literal(code)
                    if isinstance(kode, list):
                        kembali = remove_mapper_keys(kode, which=1)
                        self.output += str(kembali)
            elif text.startswith("-c"):
                """
                hapus cdata/text ke kamus
                """
                code = text.removeprefix("-c").strip()
                if code:
                    print("[db.replservice] literalling:", code)
                    kode = literal(code)
                    if isinstance(kode, list):
                        kembali = remove_mapper_keys(kode, which=2)
                        self.output += str(kembali)
            elif text.startswith("-v"):
                """
                <input disabled=t> -> t = true
                hapus value attr ke kamus
                """
                code = text.removeprefix("-v").strip()
                if code:
                    print("[db.replservice] literalling:", code)
                    kode = literal(code)
                    if isinstance(kode, list):
                        kembali = remove_mapper_keys(kode, which=3)
                        self.output += str(kembali)
            else:
                preprocessed_code = declarative(text, meta_input)
                self.run_program(preprocessed_code)

        elif text.startswith(
            "**"
        ):  # run fmus dari vscode, e.g. **(fmus code spt **showtext=...)
            """
            run fmus dari vscode
            """
            # fmus
            program = text.removeprefix("**").lstrip()
            # tambah newline
            program += "\n"

            # fmus = Fmus(env_int('ULIBPY_FMUS_DEBUG'))
            if meta_input:
                """
                ok ada berbagai kasus
                1) /tmp/absolute
                        __FILE__
                        __CURDIR__
                ini tentu hrs setup dir/file template
                2) /tmp/absolute
                        tanpa __FILE__ atau __CURDIR__
                3) relative,d
                        __FILE__
                        __CURDIR__
                4) relative,d
                        tanpa __FILE__ atau __CURDIR__
                kasus 3 dan 4 sama, krn docinfo/filename sama dengan __FILE__
                """
                docinfo = meta_input["metaDocument"]
                filepath = docinfo["filename"]

                # dimulai_dengan_absolute_path = program.startswith('/') and program.count(',d')>0
                # kita kasih ,d, krn bisa saja program itu app.quick spt /D> atau /b) yg oneliner dan tdk diakhiri ,d
                dimulai_dengan_absolute_path = startswith_absolute_folder(
                    program, pattern_suffix=",d"
                )
                # masalah jika:
                # repl adlh wsl/linux => terima filepath: linux path
                # redis subscriber adlh dos/windows, dan handle kode berikut ini
                # sebaiknya: subscriber adlh linux juga...
                prefix = ULIBPY_WSL_ADDRESS  # env_get('ULIBPY_WSL_ADDRESS')
                if not dimulai_dengan_absolute_path:
                    if isfile(filepath):
                        fmus.set_file_dir_template(filepath)
                    elif platform in ["win32", "windows"] and filepath.startswith("/"):
                        # jk handle subscriber di windows dan filepath/code dari path linux
                        # prefix = '\\\\wsl$\\Ubuntu-20.04'
                        filepath = prefix + pemisah_unix_to_windows(filepath)
                        if isfile(filepath):
                            print(
                                "\n*** memperoleh filepath linux di windows, ubah menjadi {filepath}\n"
                            )
                            fmus.set_file_dir_template(filepath)
                    elif platform() == "wsl":
                        modifypath = wslpath_to_linuxpath(filepath)
                        indah4(
                            f"[replservice] ubah wslpath {filepath} ke {modifypath}",
                            warna="magenta",
                        )
                        filepath = modifypath
                        # jangan lupa
                        fmus.set_file_dir_template(filepath)
                else:
                    if "__FILE__" in program or "__CURDIR__" in program:
                        if "__FILE__" in program:
                            fmus.set_file_template(filepath)
                        if "__CURDIR__" in program:
                            fmus.set_dir_template_from_file(filepath)
                    else:
                        indah4(
                            f"""[db.replservice] >>{program[:50]}...<<
						dimulai dengan absolute path, not setting __FILE__/__CURDIR__""",
                            warna="magenta",
                        )

            # Running program [.,d
            #   rust-cli,d(/mk)
            #     __init__.py,f(t=)
            #     index-input.mk,f(t=)
            # ] at [\\wsl$\Ubuntu-20.04\home\usef\work\ulibs\schnell\app\transpiler\frontend\fslang\misc\work.fmus]
            # curpwd_from_vscode = ayah(filepath, 1)
            os.environ["ULIBPY__PWD__"] = ayah(filepath, 1)

            indah4(
                f"[replservice] Running program [{program}] at [{filepath}]",
                warna="yellow",
            )

            if env_int("ULIBPY_FMUS_CAPTURE_STDOUT_STDERR"):
                fmus.process(program, capture_outerr=True)
                if "$*" in program:
                    """
                    jika ada sysop command kita tertarik pada outputnya
                    sleep .5s dulu utk pastikan output tercapture ke fmus
                    """
                    tidur(ms=env_int("ULIBPY_STDOUT_CAPTURE_SLEEP_MS"))
                    if fmus.stdout or fmus.stderr:
                        self.output = fmus.stdout if fmus.stdout else fmus.stderr
            else:
                fmus.process(program)

        elif text.startswith(
            "*@"
        ):  # run C:\Users\usef\work\sidoarjo\schnell\ai\autolib\repl.py
            """
            *@ocr
            *@s:/home/usef/lihat.jpg
            """
            code = text.removeprefix("*@").strip()
            result, meta = auto_process(code, True)
            self.output = result if result else ""
            self.metaresult.update({"ocr_imagefile": meta})

        elif text.startswith("*#"):  # *#@alamat|kode xpath|text dll utk scraping...
            """
            scraping service dg xpath

            utk css selection
            *#@alamat|kode xpath|text
            *#@alamat|kode xpath|range|text
            utk xpath selection
            *##alamat|kode xpath|text
            *##alamat|kode xpath|range|text
            xpath
            'perus0'    : '//*[@id="category-2"]/article/ul/li[__INDEX]/a/span[1]',
            'job0'      : '//*[@id="category-2"]/article/ul/li[__INDEX]/a/span[2]',
            'location0' : '//*[@id="category-2"]/article/ul/li[__INDEX]/a/span[6]',
            gonta_ganti = xpath.replace('__INDEX', str(n))
            """
            code = text.removeprefix("*#").strip()
            is_xp = 1
            if code.startswith("#"):
                code = code.removeprefix("#")
            elif code.startswith("@"):
                code = code.removeprefix("@")
                is_xp = 0

            if is_xp:
                # harus internal import
                # ModuleNotFoundError: No module named 'PyQt5.QtWebKit'
                from schnell.app.scrape.scraper import scrape_service

                result = scrape_service(code)
                self.output = result if result else ""
                self.metaresult.update({"original": code})

        elif text.startswith(
            "*!"
        ):  # * ! kanan-kiri (biasanya utk vscode), *!help, dahsyat
            """
            help, dahsyat, etc

            *!<code data csv>
                    <- default ini sementara blm support
            *!grpc/<code data csv>
            """
            # ImportError: cannot import name 'bantupeople' from partially initialized module 'schnell.db.bantuan' (most likely due to a circular import) (c:\users\usef\work\sidoarjo\schnell\db\bantuan\__init__.py)
            from schnell.db.bantuan import bantupeople

            code = text.removeprefix("*!").strip()
            # input(f'terima *! code yakni: {code}, cek apa direktori langsung dibuat?')
            if code.startswith("help"):
                code = code.removeprefix("help")
                self.output = bantupeople.help(code)
            elif code.startswith("dahsyat:"):
                """
                *!dahsyat:/tmp/hapus/whatever|codes
                """
                code = code.removeprefix("dahsyat:")
                # input(f'sblm oprek dahsyat utk code {code}')
                self.output = bantupeople.dahsyat(code)
                if env_int("ULIBPY_FMUS_DEBUG") > 1:
                    indah4(f"bantupeople.dahsyat: [{self.output}]", warna="yellow")
            elif code.count(category_delimiter) == 1:
                """
                *!<kategori>|kode -> generate
                """
                category, program = code.split(category_delimiter)
                if category and program:
                    result, meta = bantupeople.generate(program, category)
                    self.output = result if result else ""
                    self.metaresult.update({"bantu_meta": meta})
                    if env_int("ULIBPY_FMUS_DEBUG") > 1:
                        indah4(f"bantupeople.generate: [{self.output}]", warna="yellow")
            elif code.count(category_delimiter) == 2:
                """
                *!antd/bs|kode|dummy -> new_generate
                """
                category, config, program = code.split(category_delimiter)
                result, meta = bantupeople.new_generate(category, config, program)
                self.output = result if result else ""
                self.metaresult.update({"bantu_meta": meta})
                if env_int("ULIBPY_FMUS_DEBUG") > 1:
                    indah4(f"bantupeople.new_generate: [{self.output}]", warna="yellow")
            else:
                """ """
                result, meta = bantupeople.generate(code, "default")
                self.output = result if result else ""
                self.metaresult.update({"bantu_meta": meta})
                if env_int("ULIBPY_FMUS_DEBUG") > 1:
                    indah4(
                        f"bantupeople.generate default: [{self.output}]", warna="yellow"
                    )

        elif text.startswith(
            "*%"
        ):  # * % kanan tengah, *%redux|{c,r,u,d}_products,vlc_{wieke,lara}
            """
            *%redux|{c,r,u,d}_products,vlc_{wieke,lara}
            """
            code = text.removeprefix("*%")
            if code.count(category_delimiter) == 1:
                category, program = code.split(category_delimiter)
                if category and program:
                    program = "@" + program  # redux frontend code compliant
                    result, meta = bantupeople.frontend(program, category)
                    self.output = result if result else ""
                    self.metaresult.update({"bantu_meta": meta})

        elif text.startswith(
            "*~"
        ):  # * ~ kanan ekstrim-kiri, curly lang, *~localhost:9000/items
            """
            *~localhost:9000/items p header {}
            jk kita kasih data: {}
            maka hrs kasih header json
            """
            program = text.removeprefix("*~").strip()
            from .generator import process_curl

            out, err = process_curl(program, True)
            self.metaresult.update({"original": program})
            if not out:
                self.output += err
            else:
                self.output += out
                if err:
                    self.metaresult.update({"stderr": err})

        elif text == "gen":
            """
            generator mk file gaya wmc
            """
            code = text.removeprefix("gen").strip()
            if meta_input:
                docinfo = meta_input["metaDocument"]
                filepath = docinfo["filename"]
                basedir = ayah(filepath, 1)
                if isdir(basedir):
                    Generator().ask_with_qt(basedir, use_same_folder_for_generated=True)

            else:
                Generator().ask_with_qt()

        elif text.startswith("wmc"):
            code = text.removeprefix("wmc").strip()
            schnelldir = ULIBPY_BASEDIR  # env_get('ULIBPY_BASEDIR')
            wmcfilepath = joiner(schnelldir, "app", "wmc.py")
            indah4(
                f"[db.replservice] running wmc {wmcfilepath} with args {code}",
                warna="white",
            )

            if code and isdir(code):
                laksanakan = f"qterminal -e python {wmcfilepath} {code} &"
                komando(laksanakan)
            else:
                if meta_input:
                    docinfo = meta_input["metaDocument"]
                    filepath = docinfo["filename"]
                    basedir = ayah(filepath, 1)
                    if isdir(basedir):
                        laksanakan = f"qterminal -e python {wmcfilepath} {basedir} &"
                        indah4(
                            f"[db.replservice] running wmc {wmcfilepath} with args {basedir}",
                            warna="white",
                        )
                        komando(laksanakan)
                    else:
                        laksanakan = f"qterminal -e python {wmcfilepath} {schnelldir} &"
                        indah4(
                            f"[db.replservice] running wmc {wmcfilepath} with args {schnelldir}",
                            warna="white",
                        )
                        komando(laksanakan)
                else:
                    laksanakan = f"qterminal -e python {wmcfilepath} {schnelldir} &"
                    indah4(
                        f"[db.replservice] running wmc {wmcfilepath} with args {schnelldir}",
                        warna="white",
                    )
                    komando(laksanakan)

        elif text == "f12":
            """
            generator wmc
            """
            indah4(
                f"[db.replservice] oprek f12, self.last_file => [{self.last_file}]",
                warna="magenta",
            )
            if self.last_file and isfile(self.last_file):
                vscode_edit_at_line(self.last_file, self.last_lineno)

        elif text.startswith(":"):
            """
            : 		-> info language dan filepath dari meta_input
            :py		-> language dari code, filepath digenerate
            :py~~~print('hello, world')
            kita pastikan ~~~ tidak muncul dalam program
            """
            tidak_ada_dalam_code = "~~~"
            code = text.removeprefix(":").strip()
            from .executor import file_executor

            if code:
                if code.count(tidak_ada_dalam_code) > 0:
                    language, complete_program = code.split(tidak_ada_dalam_code)
                    file_executor.exec(language, complete_program=complete_program)
                else:
                    language = code
                    file_executor.exec(language)
            else:
                if meta_input:
                    docinfo = meta_input["metaDocument"]
                    filepath = docinfo["filename"]
                    if isfile(filepath):
                        language = docinfo["language"]
                        file_executor.exec(language, filepath=filepath)

        elif text == "lengkap":
            self.complete_output = not self.complete_output
            self.output = "output sekarang (lengkap/normal): " + (
                "VERBOSE" if self.complete_output else "NORMAL"
            )

        elif text == "term" or text.startswith("term "):
            from .replservice_helper import term_handler

            term_handler(text, meta_input)

        elif text == "explorer" or text.startswith("explorer "):
            filepath = meta_input["metaDocument"]["filename"]
            folder = ayah(filepath, 1)
            print("\nexplorer => file:", filepath, "folder:", folder)
            from .replservice_helper import explorer_handler

            explorer_handler(text, meta_input)

        elif text.startswith("package.json"):
            """
            package.json
            package.json*
            package.json|package1,package2
            """
            perintah = ""
            if text == "package.json":
                perintah = process_packagejson()
            elif text == "package.json*":
                """all with versions -> packagename@version"""
                perintah = process_packagejson(versions=[])
            elif "|" in text:
                pkgs = text.split("|")[1]
                versions = pkgs.split(",")
                perintah = process_packagejson(versions=versions)

            # print_copy(perintah)
            self.output = perintah

        elif text.startswith("l "):
            code = text.removeprefix("l ").strip()
            Launcher.launch(code)

        elif text.startswith("/"):
            from .redis_repl_search_service import redis_repl_search_service

            code = text.removeprefix("/").strip()
            # hasil, meta = redis_repl_search_service(code)
            hasil, meta = redis_repl_search_service(code, self)
            self.output += hasil
            if "last_file" in meta:
                self.last_file = meta["last_file"]

        elif text.startswith("H") or text.startswith("`"):
            if text == "``":
                # print_copy(template_default_entry)
                self.output += template_default_entry
            elif text == "`#":
                # print_copy(template_use_entry)
                self.output += template_use_entry
            elif text == "`r":
                self.output += template_reverse_entry
            elif text == "`u":
                self.output += template_unless
            elif text == "`p":
                self.output += template_pick
            elif text == "`##":
                # print_copy(template_use_entry + '\n' + template_default_entry)
                self.output += template_use_entry + "\n" + template_default_entry
            elif text == "```":
                # print_copy(template_index_mk)
                self.output += template_index_mk
            elif text == "`l":
                # print_copy(template_link)
                self.output += template_link
            elif text == "`@":
                """kita entryfy isi clipboard"""
                # cek jk multiline
                clip = trypaste()
                if "\n" in clip:
                    entrified = [
                        template_entrify.replace("__TITLE__", item)
                        for item in clip.splitlines()
                        if item
                    ]
                    hasil = "\n".join(entrified)
                    print_copy(hasil)
                else:
                    hasil = template_entrify.replace("__TITLE__", clip)
                    # print_copy(hasil)
                self.output += hasil
            elif re.match(r"`(\d+)", text):
                m = re.match(r"`(\d+)", text)
                if m and m.group(1):
                    angka = int(m.group(1))
                    for _ in range(angka):
                        self.output += template_default_entry + "\n"
            elif text.startswith("`,"):
                # kita tambah `,something jadi --% something
                # kita lower kan, krn ini seringnya begitu
                code = text.removeprefix("`,").lstrip().lower()
                self.output += f"--% {code}"
            elif text == "`." or text == "`.`":
                # kita tambah `. jadi --#
                # kita terima juga `.` krn tau sendiri vscode suka sok pintar
                self.output += "--#"
            elif text.startswith("`/"):
                code = text.removeprefix("`/").lstrip().lower()
                self.output += code
            elif text == "`ctx":
                creator_context["petik_vscode"] = not creator_context["petik_vscode"]
            elif (
                text.startswith("`") and text != "`" and creator_context["petik_vscode"]
            ):
                """
                ini berbahaya krn memakan misalnya `react padahal kita pengen baris entry react...
                tapi memang dibutuhkan utk vscode
                jd gimana?

                tambah "and text != '`'" agar tidak makan single ` yg harusnya list entry bahasa
                `Something -> apa adanya
                ``Something -> lower kan header (baris_entry) saja
                ```Something -> lower kan header+body
                """
                lower_header, lower_body = False, False
                code = text.removeprefix("`")
                if code.startswith("`"):
                    code = code.removeprefix("`")
                    lower_header = True
                if code.startswith("`"):
                    code = code.removeprefix("`")
                    lower_body = True
                code_header, code_body = code, code
                if lower_header:
                    code_header = code.lower()
                if lower_body:
                    code_body = code.lower()
                # kita lower kan krn kadang hasil copy paste
                self.output += f"--% {code_header}\n{code_body}\n--#\n"
            else:
                prefix = "H" if text.startswith("H") else "`"
                # from schnell.creator.grammar import bahasa
                baris = entry_bahasa
                if text.startswith(f"{prefix}*"):
                    baris = sorted(baris)
                    code = text.replace(f"{prefix}*", "", 1).strip()
                else:
                    code = text.replace(f"{prefix}", "", 1).strip()

                if code:
                    baris = [item for item in baris if code in item]
                else:
                    # jika masukkan ` saja
                    # kita pengen reverse dari mulai vars...
                    vars = [item for item in baris if '"V"' in item]
                    if vars:
                        vars = vars[0]
                        varindex = baris.index(vars)
                        if varindex >= 0:
                            baris = baris[varindex:] + baris[:varindex]

                hasil = "\n".join(baris)
                # print(hasil)
                self.output += hasil

        elif text.startswith("\\"):
            """
            \py
            \hs
            """
            jawab = text.replace("\\", "", 1).strip()
            if jawab and jawab in languages:
                self.config.run_configuration["current_language"] = jawab
                context["current_language"] = jawab
                self.output += f"language changed to {jawab}"

        elif text.startswith("%"):
            """
            %load
            %<word>
                    jk cuma 1 maka define
            %#<word>
                    define
            %*<word>
                    edit
            %<123>
            %$1
            random sebanyak 1
            %$1*
            random sebanyak 1 + definisi
            """
            from .writer_service import process_writer

            result = process_writer(text.removeprefix("%"))
            self.output += result

        else:
            """
            cek jk minta override language
            context['override_language']
            """
            if "/" in text:
                checklang, rest = text.split("/", 1)
                if any([item for item in programming_languages if checklang == item]):
                    context["override_language"] = checklang
                    text = rest
            self.run_program(text)

        return self.output, self.metaresult


def printer(data):
    print("*" * 80)
    print(data)
    print("*" * 80)


# harusnya setiap output jadi string dan dilempar ke redis publish
repl_service = ReplService()
