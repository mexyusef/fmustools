import os, re, shutil, time, threading
from schnell.app.appconfig import programming_data
from schnell.app.autoutils import prompt
from schnell.app.datetimeutils import isofied
from schnell.app.dirutils import (
    ayah,
    normy,
    isdir,
    dirname,
    isabsolute,
    bongkar,
    chdir,
    tempdir,
    joiner,
)
from schnell.app.fileutils import (
    get_definition_by_key_permissive_start,
    file_content,
    is_file_binary,
    append_file,
    file_content_add_newline,
    handle_content_start_end,
    file_append_lines,
)
from schnell.app.fmus import Fmus
from schnell.app.mediautils import get_stringified_image_asb64
from schnell.app.notifutils import notify
from schnell.app.printutils import indah4
from schnell.app.stringutils import replace_non_alpha, tab_tab, tab_space2, tab_space4
from schnell.app.utils import trypaste, env_get, env_int
from schnell.langs.ucsv import processor as ucsv_processor


fmus = Fmus()
FOOTER = "--#"
HEADER = "--% "
INDEX = "index/fmus"


def get_rootnode(program):
    """
    program bisa "1" (alfanumerik) dll utk dummy
    """
    RootNode = ucsv_processor(program, print)
    return RootNode


def run_us_in_folder_in_thread_(targetDir, us_filepath, start_fresh=True):
    program = file_content_add_newline(us_filepath)
    chdir(targetDir)
    fmus.set_dir_template(targetDir, start_fresh=start_fresh)
    fmus.process(program)


def run_us_in_folder_in_thread(targetDir, us_filepath, start_fresh=True):
    x = threading.Thread(
        target=run_us_in_folder_in_thread_, args=(targetDir, us_filepath, start_fresh)
    )
    x.start()
    return x


def run_fmus_for_file(
    filepath,
    baris_entry="index/fmus",
    start_fresh=True,
    change_to_current_directory=False,
    new_working_folder=None,
):
    if '\\' in filepath: # dari vscode gak jalan
        filepath = filepath.replace('\\', '/')
    program = get_definition_by_key_permissive_start(filepath, baris_entry)
    if programming_data["debug"]:
        indah4(
            f"""[fmusutils][run_fmus_for_file]
		program = [{program}]
		filepath = {filepath}
		baris_entry = {baris_entry}
		start_fresh = {start_fresh}
		""",
            warna="cyan",
        )
    if not program:
        indah4(
            f"""
		[fmusutils][run_fmus_for_file]
		program = get_definition_by_key_permissive_start(filepath, baris_entry) is empty
		{program} = get_definition_by_key_permissive_start({filepath}, {baris_entry})
		""",
            warna="red",
        )
        return
    if change_to_current_directory:
        fmus.set_file_dir_template(
            filepath, dir_template=os.getcwd(), start_fresh=start_fresh
        )
    elif new_working_folder:
        fmus.set_file_dir_template(
            filepath, dir_template=new_working_folder, start_fresh=start_fresh
        )
    else:
        fmus.set_file_dir_template(filepath, start_fresh=start_fresh)
    fmus.process(program)


def run_fmus_for_file_in_thread2(sourcefilePath, baris_entry="index/fmus"):
    # change_to_current_directory
    x = threading.Thread(target=run_fmus_for_file, args=(sourcefilePath, baris_entry))
    x.start()
    return x


def run_fmus_for_file_in_thread(sourcefilePath, baris_entry="index/fmus", **kwargs):
    # Example usage:
    # extra_params = [param1, param2]
    # thread = run_fmus_for_file_in_thread(sourcefilePath, baris_entry, *extra_params, start_fresh=True, change_to_current_directory=True)
    # change_to_current_directory
    main_args = (sourcefilePath, baris_entry)
    # new_args_kwargs = {
    # 	'*args': args,
    # 	'**kwargs': kwargs
    # }
    # print(f"""[run_fmus_for_file_in_thread9]
    # new_args_kwargs = {new_args_kwargs}
    #    """)
    x = threading.Thread(target=run_fmus_for_file, args=main_args, kwargs=kwargs)
    x.start()
    return x


def run_fmus_for_file_in_folder_in_thread(
    targetDir, sourcefilePath, baris_entry="index/fmus"
):
    """
    menjalankan filepath=barisentry dengan pertama kali mengcopy filepath ke targetDir (jika targetDir berbeda dg dirname dari sourcefilePath)
    def run_fmus_in_directory_in_thread(self, targetDir, sourcefilePath, barisEntry):
            if os.path.isfile(targetDir):
                    targetDir = os.path.dirname(targetDir)
            run_fmus_for_file_in_folder_in_thread(targetDir, sourcefilePath, barisEntry)

    menu_per_file.addAction(entry, functools.partial(self.run_fmus_in_directory_in_thread, filePath, mk_filename, entry))

    for mk_filename,v in context_menu_for_files_with_entries.items():
            filename = os.path.basename(mk_filename).removesuffix('.mk').removesuffix('.fmus')
            menu_per_file = QMenu(filename, menu_provider)
            for entry in v:
                    menu_per_file.addAction(entry, functools.partial(self.run_fmus_in_directory_in_thread, dirPath, mk_filename, entry))
            menu_provider.addMenu(menu_per_file)
    menu_provider.addAction(get_icon(), 'Reload', lambda: self.reload_context_menu_providers_for_file(filePath))
    """
    sourcedirPath = dirname(sourcefilePath)
    # ternyata perlu manual nih
    # karena kita lakukan: fmus.set_file_dir_template(filepath, dir_template=os.getcwd(), start_fresh=start_fresh)
    # os.getcwd()
    chdir(targetDir)
    if sourcedirPath != targetDir:  # pastikan tidak copy ke diri sendiri
        targetfilePath = shutil.copy2(sourcefilePath, targetDir)
    else:
        targetfilePath = sourcefilePath
    x = threading.Thread(
        target=run_fmus_for_file, args=(targetfilePath, baris_entry, True)
    )
    x.start()
    return targetfilePath, x


def run_fmus_for_content(content, dirpath=tempdir(), filepath=None, start_fresh=True):
    """
    update utk dukung:
    my-springboot-docker-backend-project,d
            Dockerfile,f(F=__CONTENT_START__)
    FROM openjdk:11-jdk-slim
    VOLUME /tmp
    COPY target/*.jar app.jar
    ENTRYPOINT ["java","-jar","/app.jar"]
    __CONTENT_END__
    """
    content = handle_content_start_end(content)
    if not content.endswith("\n"):
        content += "\n"
    # ternyata perlu manual nih
    chdir(dirpath)
    if filepath:
        # dir_template perlu diisi, otherwise, projectdir disamakan dg lokasi filepath
        fmus.set_file_dir_template(
            filepath, dir_template=dirpath, start_fresh=start_fresh
        )
    elif dirpath:
        fmus.set_dir_template(dirpath, start_fresh=start_fresh)
    fmus.process(content)


# import pythoncom
def run_fmus_for_content_in_thread(content, dirpath=tempdir(), filepath=None):
    # pythoncom.CoInitialize()  # Initialize COM library
    # try:
    x = threading.Thread(
        target=run_fmus_for_content, args=(content, dirpath, filepath, True)
    )
    x.start()
    # finally:
    #     pythoncom.CoUninitialize()  # Uninitialize COM library when done
    return x


def run_fmus_for_content_in_thread_notify(
    content, dirpath=tempdir(), filepath=None, title="judul", body="badan", durasi=2
):
    indah4(
        f"""[fmusutils][run_fmus_for_content_in_thread_notify]\n[{content[:1000]}]""",
        warna="green",
    )
    if not content.endswith("\n"):
        content += "\n"
    x = threading.Thread(
        target=run_fmus_for_content, args=(content, dirpath, filepath, True)
    )
    x.start()
    notify(title, body, duration=durasi)
    return x


def run_fmus_from_coordinator(
    coordinator,
    coordinator_param_list=None,
    baris_entry="index/fmus",
    coordinator_kwargs=None,
):
    """
    def __init__(self, RootNode, filename, project_dir='__INPUT__'):
    param_list = [RootNode, filename, project_dir]

    def __init__(self, RootNode, project_dir='__INPUT__'):
    param_list = [RootNode, project_dir]
    """
    if coordinator_param_list:
        generator = coordinator(*coordinator_param_list)
    elif coordinator_kwargs:
        generator = coordinator(**coordinator_kwargs)
    generator.generate()
    filepath = generator.output()
    program = get_definition_by_key_permissive_start(filepath, baris_entry)
    fmus.set_file_dir_template(filepath)
    fmus.process(program)


def replace_input_workdir(item):
    """ """
    input0 = env_get("ULIBPY_FMUS_INPUT_KEYWORD")
    if input0 in item.workdir:
        ayahitem = ayah(item.workdir, 1)
        if ayahitem != item.parent.workdir:
            item.workdir = item.workdir.replace(input0, item.parent.name)
    return item.workdir


def replace_from_configuration_replacer(
    program_source, self_run_configuration_replacer
):
    for k, v in self_run_configuration_replacer.items():
        # UPDATE:
        # normy
        # cuma bisa jadi non path...
        # replacer bs berisi __COUNTER__ dg v int
        if isinstance(v, int):
            v = str(v)
        # print(f'k {k}, v {v}')
        program_source = program_source.replace(k, v)

    return program_source


def replace_from_configuration(program_source, self_run_configuration):
    for k, v in self_run_configuration["replacer"].items():
        # UPDATE:
        # normy
        # cuma bisa jadi non path...
        # replacer bs berisi __COUNTER__ dg v int
        if isinstance(v, int):
            v = str(v)
        # print(f'k {k}, v {v}')
        program_source = program_source.replace(k, v)

    return program_source


def filepath_samadengan_barisentry(filepath_baris_entry):
    """
    menerima
    filepath=barisentry
    spt dari: /D>=filepath=barisentry
    """

    filepath, baris_entry = filepath_baris_entry.split("=")
    filepath = bongkar(filepath)

    # indah4(f'''[fmusutils][filepath_samadengan_barisentry]
    # filepath_baris_entry = {filepath_baris_entry}
    # dipecah menjadi => {filepath}, {baris_entry}
    # ''', warna='red')

    program = get_definition_by_key_permissive_start(filepath, baris_entry)

    # indah4(f'''[fmusutils][filepath_samadengan_barisentry]
    # hasil => {program}
    # ''', warna='white')

    return program


def replace_from_configuration_new_replacer_input(
    self_run_configuration, item, request, removeprefix="/"
):
    if "new_replacer_input" in self_run_configuration:
        request = item.original.removeprefix(removeprefix)
        # ubah dari item.command ke item.original
        # jangan lupa remove prefix quick /
        # krn item.command sudah jadi __INPUT__ semua...
        for k, v in self_run_configuration["new_replacer_input"].items():
            request = request.replace(k, v)

    return request


def replace_from_configuration_new_replacer_input_if_input(
    self_run_configuration,
    content_command_request,
    original=None,
    remove_prefix="",
    pengirim="",
    check_absdir=False,
    parent=None,
):
    """
    kita tambah parent
    ternyata jk ada __INPUT__ di item.workdir
    dan item.workdir menjadi both: content_command_request dan original
    kita hanya punya dari dalam new_replacer_input: __TEMPLATE_DJANGOPROJECT: nilai (misal "coba")
    tapi kita gak tau apakah __INPUT__ memang terpetakan ke __TEMPLATE_DJANGOPROJECT
    jadi kita minta bantuan parent
    yg punya:
            input_keys=['__TEMPLATE_DJANGOPROJECT']
            input_keys_index=0
            variables={'__TEMPLATE_DJANGOPROJECT': 'coba'}
    """
    is_debugging = env_int("ULIBPY_FMUS_DEBUG") > 1
    # indah4(f'''[fmusutils]
    # replace_from_configuration_new_replacer_input_if_input
    # terima content_command_request = {content_command_request}
    # original = {original}
    # ''', warna='yellow')

    if (
        "__INPUT__" in content_command_request
        or "__INPUTGUI__" in content_command_request
        or "__INPUT||" in content_command_request
    ):
        """
        jika
        $* python ...__INPUT__...
        maka new_replacer_input gak ada di runconfig
        jadi hrs minta input saat ini juga!
        """
        if "new_replacer_input" in self_run_configuration:
            if original is not None and remove_prefix:
                content_command_request = original.removeprefix(remove_prefix)
            # indah4('masuk newreplacerinput', warna='yellow')
            for k, v in self_run_configuration["new_replacer_input"].items():
                if is_debugging:
                    indah4(
                        f"[app.fmusutils][new_replacer_input] coba replacing {k} dg {v}",
                        warna="cyan",
                    )
                if (
                    parent
                    and hasattr(parent, "input_keys")
                    and hasattr(parent, "variables")
                    and k in parent.input_keys
                ):
                    # kita ambil nilai dari parent saja
                    # ingat yg kita replace __INPUT__, bukan __TEMPLATE_DJANGOPROJECT
                    if is_debugging:
                        indah4(
                            f"""[app.fmusutils][new_replacer_input] '__INPUT__' => parent.variables[k] = {parent.variables[k]}""",
                            warna="magenta",
                        )
                    # content_command_request = content_command_request.replace('__INPUT__', parent.variables[k])
                    content_command_request = content_command_request.replace(
                        k, parent.variables[k]
                    )
                    # remove dari parent now, stlh pake
                    # del parent.variables[k]
                    # parent.input_keys.remove(k)
                else:
                    content_command_request = content_command_request.replace(k, v)
        else:
            content_command_request = get_input_generic(
                content_command_request, pengirim=pengirim, check_absdir=check_absdir
            )

    # still masih ada...
    if (
        "__INPUT__" in content_command_request
        or "__INPUTGUI__" in content_command_request
        or "__INPUT||" in content_command_request
    ):
        content_command_request = get_input_generic(
            content_command_request, pengirim=pengirim, check_absdir=check_absdir
        )

    return content_command_request


def is_input(text):
    if "__INPUT__" in text or "__INPUTGUI__" in text or "__INPUT||" in text:
        return True
    return False


def get_input_from_user_or(original_pattern, default_value, pengirim=""):
    # indah0(pengirim+'| ', warna='white')
    # indah0(f'|| Masukkan nilai untuk [{original_pattern}] ["Enter" = "{default_value}"]:', warna='magenta', bold=True, underline=True)
    # masukan = input(' ')
    message = f'{pengirim}nMasukkan nilai untuk [{original_pattern}] ["ENTER" = "{default_value}"]'
    masukan = prompt(message)
    if not masukan:
        return default_value
    return masukan


def get_input_from_user(original_pattern, pengirim=""):
    # indah0(pengirim+'| ', warna='white')
    # indah0(f'Masukkan nilai untuk [{original_pattern}]:', warna='magenta', bold=True, underline=True)
    # masukan = input(' ')
    message = f"{pengirim}\nMasukkan nilai untuk [{original_pattern}]"
    masukan = prompt(message)
    return masukan


def get_input_from_user_gui(
    original_pattern="",
    initial_text="",
    pengirim="",
    basedir=tempdir(),
    get_filepath=False,
    delay=0.5,
):
    """
    item.command pada $
    item.content pada @
    """
    from schnell.app.showtextwindow import showtextwindow
    from schnell.app.timeutils import timestamp

    if not original_pattern:
        filename = timestamp()
    else:
        filename = replace_non_alpha(original_pattern)  # + isofied()
    filepath = joiner(basedir, filename)
    showtextwindow(
        filepath,
        title=pengirim + "| " + original_pattern,
        content_from_clipboard=False,
        content_text=initial_text,
    )
    time.sleep(delay)
    masukan = file_content(filepath)
    # indah4(f'''[fmusutils][get_input_from_user_gui]
    # input gui dari user {masukan}
    # ''', warna='cyan')
    if get_filepath:
        return masukan, filepath
    # if get_window:
    # 	return masukan, wnd
    return masukan


def get_input_simpan_temp_vars(templatekey, templatevalue, item, pengirim=""):
    """
    %__TEMPLATEKEY=__INPUT__ atau __INPUTGUI__ atau __INPUT||defaultvalue
    """

    if templatevalue == "__INPUTGUI__":
        masukan = get_input_from_user_gui(templatekey, pengirim=pengirim)

        # dari gui perlukah jadikan __INPUT__ biasa dulu?
        # indah4(f'''[simpan_temp_vars] __INPUTGUI__
        # lanjut peroleh masukan = {masukan}
        # ''', warna='blue')

        item.variables[templatekey] = "__INPUT__"

    elif templatevalue.startswith("__INPUT||"):
        vv = templatevalue.removeprefix("__INPUT||")
        item.variables[templatekey] = "__INPUT__"  # biar @, $ dll memproses
        masukan = get_input_from_user_or(templatekey, vv, pengirim=pengirim)

        # indah4(f'''[simpan_temp_vars] __INPUT||
        # lanjut peroleh masukan = {masukan}
        # ''', warna='blue')

    else:
        masukan = get_input_from_user(templatekey, pengirim=pengirim)

    return masukan


def get_input_generic(text, pengirim="", check_absdir=False):
    """
    text:
    hari ini akan hujan
    hari ini akan panas
    hari ini akan __INPUT__

    check_absdir jk minta replace item.workdir = path
    """
    result = text

    if is_input(text):
        if "__INPUT||" in text:
            found = re.search(
                r"(?P<everything>.*)__INPUT\|\|(?P<nilaidefault>[^\s]+)", text
            )
            # indah4(f'''[sysop_command]
            # text = {text}
            # regex found = {found} => {found.groups()}
            # ''', warna='cyan')
            if found:
                masukan = get_input_from_user_or(
                    found.group("everything"),
                    found.group("nilaidefault"),
                    pengirim=pengirim,
                )
                if masukan:
                    result = found.group("everything") + masukan
        elif "__INPUTGUI__" in text:
            masukan = get_input_from_user_gui(text, pengirim=pengirim)
            if masukan:
                result = text.replace("__INPUTGUI__", masukan)
        elif "__INPUT__" in text:
            masukan = get_input_from_user(text, pengirim=pengirim)
            if masukan:
                if check_absdir:
                    # kita coba expand dulu
                    if masukan.startswith("%") or masukan.startswith("$"):
                        masukan = bongkar(masukan)
                    # juga mungkin bisa masukkan __PWD
                    if isabsolute(masukan):
                        result = masukan
                        input(
                            f"[fmusutils/get_input_generic] {masukan} adlh absdir... "
                        )
                else:
                    result = text.replace("__INPUT__", masukan)

    return result


def get_input_generic_if_input_not_from_template(text, root_dir, pengirim=""):
    """
    ada 2 jenis input
    1)
            %__TEMPLATE_CONTOH=__INPUT__
            $ ...__TEMPLATE_CONTOH			ini input from template
            @ ...__TEMPLATE_CONTOH			ini input from template

    2)
            $ ...__INPUT__					ini input direct
            @ ...__INPUT__					ini input direct

    contoh pake utk replace "direct input" di item.workdir: content_file, load_program_from
    """
    # jk bukan input from template maka minta input direct
    if not (hasattr(root_dir, "input_keys") and len(root_dir.input_keys)):
        text = get_input_generic(text, pengirim=pengirim)
    return text


def reverse_folder(
    base_folder,
    output_fmus=None,
    TAB="",
    dont_skip_binary=True,
    create_index=False,
    skip_dirs=None,
    skip_files=None,
    skip_ext=None,
):
    base_folder = os.path.normpath(base_folder)
    content_result = {}

    project_name = os.path.basename(base_folder)
    if not output_fmus:
        output_fmus = project_name + ".fmus"
    parent_base_folder = os.path.dirname(base_folder)
    output_filepath = os.path.join(parent_base_folder, output_fmus)
    startpath = base_folder

    indah4(f"[fmusutils:reverse_folder] {startpath} => {output_filepath}", warna="cyan")

    if not TAB:
        tab_ = programming_data["j"]["schnell"]["app"]["fmusutils"][
            "indent_for_reverse_fmus"
        ]
        if tab_ == "space4":
            TAB = tab_space4
        elif tab_ == "space2":
            TAB = tab_space2
        else:
            TAB = tab_tab
    if skip_dirs is None:
        skip_dirs = programming_data["j"]["schnell"]["app"]["fmusutils"]["skip_folders"]
    if skip_files is None:
        skip_files = programming_data["j"]["schnell"]["app"]["fmusutils"]["skip_files"]
    if skip_ext is None:
        skip_ext = programming_data["j"]["schnell"]["app"]["fmusutils"][
            "skip_extensions"
        ]

    for root, subdirs, files in os.walk(startpath, topdown=True):
        subdirs[:] = [d for d in subdirs if d not in skip_dirs]
        files = [
            f
            for f in files
            if (
                not (f in skip_files)
                and not ([ext for ext in skip_ext if f.endswith(ext)])
            )
        ]

        # buat index/fmus
        if create_index:
            level = root.replace(startpath, "").count(os.sep)
            subindent = TAB * (level + 1)
            indent = TAB * (level)
            # if level == 0:
            namadir = os.path.basename(root)
            # handle nextjs-type folders
            # if '@' in namadir or '[' in namadir or ']' in namadir:
            if [item in namadir for item in ["@", "[", "]", "(", ")", ","]]:
                namadir = (
                    namadir.replace("@", "__AT__")
                    .replace("[", "__LK__")
                    .replace("]", "__RK__")
                    .replace("(", "__LP")
                    .replace(")", "__RP")
                    .replace(",", "__COMMA__")
                )
            value = "%s%s,d(/mk)" % (indent, namadir)
            if INDEX not in content_result:
                content_result[INDEX] = [value]
            else:
                content_result[INDEX].append(value)
            # else:

        for filename in files:
            fullpath = os.path.join(root, filename)
            # tidak boleh ada ( dan ) di barisentry karena bentrok dg specifier file => f(...)
            relative = (
                os.path.relpath(fullpath, startpath)
                .replace("\\", "/")
                .replace("(", "__LP")
                .replace(")", "__RP")
                .replace(
                    "=", "__EQ__"
                )  # filename,f(e=__FILE__=relative_gak_boleh_ada_sama_dengan)
                .replace("$", "__DOLLAR__")  # baris entry gak boleh ada $
            )
            biner = is_file_binary(fullpath)
            if not biner:
                nilai = file_content(fullpath)
                content_result[relative] = [nilai]
            elif dont_skip_binary:
                nilai = get_stringified_image_asb64(fullpath)
                content_result[relative] = [nilai]

            filename = (
                filename.replace(",", "__COMMA__")  # nama file gak boleh ada ,
                .replace("=", "__EQ__")  # nama file gak boleh ada =
                .replace("$", "__DOLLAR__")  # nama file gak boleh ada $
            )

            if create_index:
                text_binary = "b64" if biner else "e"
                filerepr = f"{filename},f({text_binary}=__FILE__={relative})"
                value = "%s%s" % (
                    subindent,
                    filerepr,
                )  # subindent sudah diassign di if create_index sblmnya
                if INDEX not in content_result:
                    content_result[INDEX] = [value]
                else:
                    content_result[INDEX].append(value)
                # indah4(f"content_result[INDEX] = [value] => content_result[{INDEX}] = [{value}]", warna='yellow')

    for k in content_result.keys():
        lines = content_result[k]
        stringified = "\n".join(lines).rstrip()
        header = HEADER + (project_name + "/" if k != INDEX else "") + k
        entry = f"{header}\n{stringified}\n{FOOTER}\n\n"
        append_file(output_filepath, entry)

    print(f'[fmusutils][reverse_folder] "{base_folder}" done.')


def reverse_folder_onlydirs(base_folder, output_fmus=None, save_to_cwd=True):
    """ """
    base_folder = bongkar(base_folder)
    all_subfolders = [
        item
        for item in os.listdir(base_folder)
        if os.path.isdir(os.path.join(base_folder, item))
    ]
    # all_subfolders = [ f.path for f in os.scandir(base_folder) if f.is_dir() ]
    # print(f'found {all_subfolders} in {base_folder}')
    project_name = os.path.basename(base_folder)
    if not output_fmus:
        output_fmus = project_name + ".fmus"
    parent_base_folder = os.path.dirname(base_folder)

    if save_to_cwd:
        parent_base_folder = os.getcwd()

    output_filepath = os.path.join(parent_base_folder, output_fmus)

    for k in all_subfolders:
        fullpath = os.path.join(base_folder, k).replace(
            "\\", "/"
        )  # agar ,f(D=) bisa jalan
        # header = HEADER + fullpath  # terlalu panjang
        header = HEADER + k
        stringified = f"{k},f(D={fullpath})"
        entry = f"{header}\n{stringified}\n{FOOTER}\n\n"
        # print('writing:', entry)
        append_file(output_filepath, entry)

    print(
        f'[fmusutils][reverse_folder_onlydirs] "{base_folder}" to {output_filepath} done.'
    )


def create_fmusfile_from_clipboard(output_filepath):
    content = trypaste()
    if content:
        lines = content.splitlines()
        result = [
            f"{HEADER + line}\n{line}\n{FOOTER}\n\n" for line in lines if line.strip()
        ]
        if result:
            file_append_lines(output_filepath, result)
            return True
    return False


def create_fmusfile_from_commaseparatedstring(output_filepath, commaseparatedstring):
    lines = [e.strip() for e in commaseparatedstring.split(",") if e.strip()]
    if lines:
        result = [
            f"{HEADER + line}\n{line}\n{FOOTER}\n\n" for line in lines if line.strip()
        ]
        if result:
            file_append_lines(output_filepath, result)
            return True
    return False
