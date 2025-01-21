from schnell.app.dirutils import joiner, isfile
from schnell.app.fileutils import (
    create_if_empty_file,
    insert_after_then_tabify,
    insert_before_then_tabify,
	get_definition_by_key_permissive_start,
	file_content,
    file_append,
    comment_file,
    replace_file_content,
	join_lines,
	replace_string_in_file,
	insert_at,
	comment_file_by_linenumber,
	comment_file_by_prefix,
	append_file_by_linenumber,
    append_file_by_content,
    prepend_line_by_content,
	against_regex,
	remove_lines_by_prefix,
	join_lines_by_prefix,
	remove_lines_by_no,
	replace_line_by_no,
	indent_file,
	dedent_file,
	tab_to_space_start,
	space_to_tab_start,
    space_to_space_start,
	insert_after,
	insert_before,
    uncomment_file,
    remove_prefix_by_regex,
    remove_prefix_by_lineno_and_regex,
    sort_lines,
    replace_from,
    replace_between,
    replace_until,
    indent_file_by_pattern,
    dedent_file_by_pattern,
)
from schnell.app.printutils import indah4
from schnell.app.stringutils import sanitize_chars
from schnell.app.fmusutils import (
    fmus,
    filepath_samadengan_barisentry,
    replace_from_configuration_replacer
)
from schnell.app.dirutils import bongkar, isabsolute
from schnell.app.utils import env_int


def fileops(request, root_tree=None, item=None, self_run_configuration_replacer=None, result_callback=None):
    """
    j/17|__PWD/contoh.txt
        join baris no 17 sebanyak 1 (dg next line)
    j/17/5|__PWD/contoh.txt
        join baris no 17 sebanyak 5 baris

    c/2,3/'-- '|__PWD/contoh.txt"
    c/1,4-6/'-- '|__PWD/contoh.txt"
                    ^^^^^ line expression
    C/TEXT/'-- '|__PWD/s_users.sql"

    C tidak terima leading space
    C2 bisa leading space

    C/SET/'-- '|__PWD/s_users.sql"
    comment_file_by_prefix c:\work/s_users.sql OK

    C/ALTER TABLE/'-- '|__PWD/s_users.sql"
    comment_file_by_prefix c:\work/s_users.sql OK

    C/ALTER SEQUENCE/'-- '|__PWD/s_users.sql"
    comment_file_by_prefix c:\work/s_users.sql OK

    C/SELECT /'-- '|__PWD/s_users.sql"
    comment_file_by_prefix c:\work/s_users.sql OK

    j/72/6|__PWD/s_users.sql"
    join_lines c:\work/s_users.sql OK

    C2/ADD CONSTRAINT /'-- '|__PWD/s_users.sql"
    comment_file_by_prefix c:\work/s_users.sql OK

    tambah:
    di-regex kan...tiap baris
    /re/fileregex|__PWD/filetarget
    /re/fileregex|filetarget
    disini kita bikin versi 'us' file, jadi gak pake entry

    remove lines
    -/<pola prefix>/<jumlah hapus>|<target "
    -/SELECT /3|__PWD/s_users.sql"

    replace strings in lines
    repl/string pertama/string kedua|filetarget

    TODO:
    ada increment dan ada size
    misal kita I/D sebanyak 2 spaces...bisa 2x, 3x, dst.		
    default increment = 1
    bisa by_lineno dan bisa by_prefix
    indent_tab(inc=1)
    indent_space(inc=1, size=2)
    dedent_tab(inc=1)
    dedent_space(inc=1, size=2)

    >lineexpr,t|filepath
    >lineexpr,t,1|filepath
        indent pada line nos = lineexpr, gunakan tab sebanyak 1
    >lineexpr,s|filepath
        indent pada line nos = lineexpr, gunakan space sebanyak 1 (default) dg space size = 2 (default)
    >lineexpr,s,1,4|filepath
        indent pada line nos = lineexpr, gunakan space sebanyak 1 dg space size = 4
    <lineexpr,t,1|filepath
    <lineexpr,s,1,4|filepath

    juga: (tentu ini apply to whole file)
    convert tab to space
    ts|filepath
    ts/4|filepath
    convert space to tab
    st|filepath
    st/4|filepath

    UPDATE:
    touch file
        touch|filename
    """

    ops, filepath = request.split('|')
    ops_with_args = ops.split('/') # c/xpr/cmt, C/txt/cmt, j/barisnoxpr

    if env_int('ULIBPY_FMUS_DEBUG')>1:
        indah4(f"""
        welcome to fileops: {request}
        ops             = {ops}
        filepath        = {filepath}
        ops_with_args   = {ops_with_args}
        """, warna='blue')
    if item and item.workdir and not isabsolute(filepath):
        # jk filename adlh relative, ambil parentdir dari item.workdir
        filepath = joiner(item.workdir, filepath)
    filepath = bongkar(filepath)

    if not isfile(filepath):
        if ops_with_args[0] == 'touch':
            filepath = joiner(fmus.get_cwd_pwd(), filepath)
            print(f'[fileops] new filepath from cwd to touch: {filepath}')
        elif isfile(joiner(fmus.get_cwd_pwd(), filepath)):
            filepath = joiner(fmus.get_cwd_pwd(), filepath)
            print(f'[fileops] new filepath from cwd: {filepath}')
        else:
            indah4(f'''[fileops]
            {filepath} tidak ditemukan
            request = {request}
            cwd = {fmus.get_cwd_pwd()}
            ''', warna='red')
            input(' ...press... ')
            return

    if ops_with_args:

        if ops_with_args[0] == 'touch':
            '''
            touch|filename
            '''
            # print(f'[fileops] touching {filepath}')
            create_if_empty_file(filepath)

        elif ops_with_args[0] == 'content':
            # file>content/content|file.txt
            # replace_file_content(filepath, content)
            content = ops_with_args[1]
            replace_file_content(filepath, content)

        elif ops_with_args[0] == 'CONTENT':
            # file>CONTENT/filepath=barisentry|file.txt
            # replace_file_content(filepath, content)
            perlu_filepath_samadengan_barisentry = '/'.join(ops_with_args[1:])
            print(f"[fileops][CONTENT] ops_with_args:", ops_with_args)
            print(f"[fileops][CONTENT] perlu_filepath_samadengan_barisentry:", perlu_filepath_samadengan_barisentry)
            content_to_insert = filepath_samadengan_barisentry(perlu_filepath_samadengan_barisentry)
            content_to_insert = sanitize_chars(content_to_insert)
            # START: replacer
            if env_int('ULIBPY_FMUS_DEBUG')>1:
                indah4(f"""[fileops][cek replacer, item, dll pada 'IB']
                item = {item}
                parent = {item.parent}
                root = {root_tree}
                """, warna='cyan', layar='blue')
            # ini handle ULIBPY_, __FILE, __PWD, etc
            content_to_insert = replace_from_configuration_replacer(content_to_insert, self_run_configuration_replacer)
            # ini handle __TEMPLATE_* dari %__TEMPLATE_...
            if hasattr(root_tree, 'variables'):
                content_to_insert = replace_from_configuration_replacer(content_to_insert, root_tree.variables)
            # END: replacer
            replace_file_content(filepath, content_to_insert)

        elif ops_with_args[0] == 'append':
            '''
            file_append
            /file)append/fmusfile=entry|filepath
            '''
            perlu_filepath_samadengan_barisentry = '/'.join(ops_with_args[1:])
            content_to_insert = filepath_samadengan_barisentry(perlu_filepath_samadengan_barisentry)
            # content_to_insert = sanitize_chars(content_to_insert)
            content_to_insert = replace_from_configuration_replacer(content_to_insert, self_run_configuration_replacer)
            if hasattr(root_tree, 'variables'):
                content_to_insert = replace_from_configuration_replacer(content_to_insert, root_tree.variables)
            file_append(filepath, content_to_insert)

        elif ops_with_args[0] == 'a':
            '''
            suffixer/appender ke lines dalam linespec
            a/linespec/suffixer|filepath

            append_file_by_linenumber => line append, not file append
            append comment (berarti di akhir)
            /file)a/10/isi komentar|file.txt
            ~ utk last line

            u -e"/file>a/2,3/'-- '|__PWD/contoh.txt"
            u -e"/file>a/1,4-6/'-- '|__PWD/contoh.txt"
            u -e"/file>a/1-~/'>)'|__PWD/field.txt"

            utk repr last line = ~, misal 1-~
            '''
            line_expression, comment_suffix = ops_with_args[1], ops_with_args[2]
            comment_suffix = comment_suffix.strip("'") # utk windows pake SQ utk apit comment, linux perlu pake DQ
            comment_suffix = sanitize_chars(comment_suffix)
            append_file_by_linenumber(filepath, line_expression, comment_suffix)

        elif ops_with_args[0] == 'aa':
            '''
            suffixer/appender ke lines yg berisi content-filter

            /file)aa/find me/#|targetfile
            append suffix to line
            /file)aa/find me/isi komentar|file.txt
            ~ utk last line
            '''
            content_filter, comment_suffix = ops_with_args[1], ops_with_args[2]
            comment_suffix = comment_suffix.strip("'") # utk windows pake SQ utk apit comment, linux perlu pake DQ
            comment_suffix = sanitize_chars(comment_suffix)
            append_file_by_content(filepath, content_filter, comment_suffix)

        elif ops_with_args[0] == 'bb':
            '''
            prepend prefix to line
            spt aa di atas tetapi utk prepend prefix alih2 append suffix
            '''
            content_filter, comment_suffix = ops_with_args[1], ops_with_args[2]
            comment_suffix = comment_suffix.strip("'") # utk windows pake SQ utk apit comment, linux perlu pake DQ
            comment_suffix = sanitize_chars(comment_suffix)
            prepend_line_by_content(filepath, content_filter, comment_suffix)

        elif ops_with_args[0] == 'j':
            '''
            join_lines
            join lines by line number
            '''
            if len(ops_with_args) == 2:
                # /file)j/17|filepath
                barisno = int(ops_with_args[1])-1
                join_lines(filepath, barisno)
            elif len(ops_with_args) == 3:
                # /file)j/17/5|filepath
                barisno = int(ops_with_args[1])-1
                how_many_lines = ops_with_args[2]
                join_lines(filepath, barisno, int(how_many_lines))

        elif ops_with_args[0] == 'J':
            '''
            join_lines_by_prefix
            join lines by regex ^
            /file)J/find me|filepath
            /file)J/find me/2|filepath
            '''
            prefix_pattern = ops_with_args[1]
            if len(ops_with_args) == 2:
                # /file)J/ALTER TABLE ONLY|s_users-schema.sql
                join_lines_by_prefix(filepath, prefix_pattern, how_many_lines=1)
            elif len(ops_with_args) == 3:
                # /file)J/ALTER TABLE ONLY/2|s_users-schema.sql
                how_many_lines = int(ops_with_args[2])
                join_lines_by_prefix(filepath, prefix_pattern, how_many_lines=how_many_lines)

        elif ops_with_args[0] == 'c':
            '''
            comment_file_by_linenumber
            comment dg line number
            /file)c/10/-- |file.txt
            '''
            line_expression, comment = ops_with_args[1], ops_with_args[2]
            comment = comment.strip("'") # utk windows pake SQ utk apit comment, linux perlu pake DQ
            comment_file_by_linenumber(filepath, line_expression, comment)

        elif ops_with_args[0] == 'C':
            '''
            comment_file_by_prefix
            comment dg regex ^
            /file)C/cari pattern/-- |file.txt
            '''
            prefix_text, comment = ops_with_args[1], ops_with_args[2:]
            comment = '/'.join(comment)
            comment = comment.strip("'") # utk windows pake SQ utk apit comment, linux perlu pake DQ
            prefix_text = prefix_text.replace("(", "\(").replace(")", "\)")
            comment = sanitize_chars(comment)
            indah4(f"""/file)C1 = comment_file_by_prefix
            comment_file_by_prefix(filepath, prefix_text, comment)
            filepath    = [{filepath}]
            prefix_text = [{prefix_text}]
            comment     = [{comment}]
            """, warna='cyan')
            # comment_file(filepath, baris_cari, comment='#', space='', how_many_lines=1, skip_starting_whitespace=False)
            # comment_file_by_prefix(filepath, prefix_pattern, comment='# ')
            comment_file_by_prefix(filepath, prefix_text, comment)

        elif ops_with_args[0] == 'C2':
            '''
            comment_file_by_prefix
            comment dg regex ^\s*
            /file)C2/cari pattern/-- |file.txt
            '''
            prefix_text,comment=ops_with_args[1],ops_with_args[2:]
            comment = '/'.join(comment)
            comment = comment.strip("'") # utk windows pake SQ utk apit comment, linux perlu pake DQ
            prefix_text = prefix_text.replace("(", "\(").replace(")", "\)")
            # if '.mk=' in content_to_insert or '.fmus=' in content_to_insert:
            #     content_to_insert = filepath_samadengan_barisentry(content_to_insert)
            comment = sanitize_chars(comment)
            # comment_file(filepath, baris_cari, comment='#', space='', how_many_lines=1, skip_starting_whitespace=False)
            # comment_file_by_prefix(filepath, prefix_pattern, comment='# ')
            # |MULAI
            # |        MULAI -> dimulai \s+
            indah4(f"""/file)C2 = comment_file_by_prefix
            comment_file_by_prefix(filepath, prefix_text, comment)
            filepath    = [{filepath}]
            prefix_text = [{prefix_text}]
            comment     = [{comment}]
            """, warna='cyan')
            comment_file_by_prefix(filepath, prefix_text, comment, re_prefixer=r'^\s+')

        elif ops_with_args[0] == 'U':
            '''
            uncomment_file

            /file)U/pola-cari/komen-to-remove/jumlah-baris|filepath
            uncomment_file(filepath, baris_cari, comment='#', how_many_lines=1, by_tersingkat=False, by_pertama=True)

            # apa nih???
            hapus substring berpola regex-expr pada baris2 line-expr
            /file)#-/line-expr/regex-expr|filepath
            '''
            baris_cari_untuk_diuncomment, komen_untuk_dilstrip,how_many_lines = ops_with_args[1], ops_with_args[2], ops_with_args[3]
            uncomment_file(filepath, baris_cari=baris_cari_untuk_diuncomment, comment=komen_untuk_dilstrip, how_many_lines=int(how_many_lines))

        # start: i.
        elif ops_with_args[0] == 'i':
            # insert at line number the following text
            # u -e"/file)i/3/DISALLOW HOST|settings.py"
            # insert_at(filepath, nomor_baris, content_to_insert)
            line_number, content_to_insert = ops_with_args[1], ops_with_args[2:]
            content_to_insert = '/'.join(content_to_insert)
            # line_number = int(line_number)-1 # index 1, convert ke
            if not line_number.startswith('-') and not line_number=='0':
                line_number = int(line_number)-1
            else: # -1 utk last line
                line_number = int(line_number)
            # ini fungsi lama di fileutils, gak ngeprint debug, hanya return kembalian
            if not isfile(filepath):
                if isfile(joiner(fmus.get_cwd_pwd(), filepath)):
                    filepath = joiner(fmus.get_cwd_pwd(), filepath)
                    print(f'[fileops:i] new filepath from cwd: {filepath}')
            # indah4(f'[fileops>insert] content: [{content_to_insert}]', warna='cyan')
            content_to_insert = sanitize_chars(content_to_insert)
            indah4(f'[fileops:i] barisno: {line_number}, content: [{content_to_insert.strip()[:50]} ...] filepath: {filepath}', warna='cyan')
            insert_at(filepath, line_number, content_to_insert)
        # end: i.

        # start: I.
        elif ops_with_args[0] == 'I':
            # /file)I/3/filepath=barisentry|settings.py
            line_number, perlu_filepath_samadengan_barisentry = ops_with_args[1], ops_with_args[2:]
            perlu_filepath_samadengan_barisentry = '/'.join(perlu_filepath_samadengan_barisentry)
            if not line_number.startswith('-') and not line_number=='0': # non-0 positive dikurang 1 krn indexing dari 0
                line_number = int(line_number)-1
            else:
                line_number = int(line_number) # 0 atau -1 stays as is
            if not isfile(filepath):
                if isfile(joiner(fmus.get_cwd_pwd(), filepath)):
                    filepath = joiner(fmus.get_cwd_pwd(), filepath)
                    print(f'[fileops] new filepath from cwd: {filepath}')
            content_to_insert = filepath_samadengan_barisentry(perlu_filepath_samadengan_barisentry)
            content_to_insert = sanitize_chars(content_to_insert)

            # START: replacer
            if env_int('ULIBPY_FMUS_DEBUG')>1:
                indah4(f"""[fileops][cek replacer, item, dll pada 'I' insert at lineno by filepath=baris]
                item = {item}
                parent = {item.parent}
                root = {root_tree}
                """, warna='cyan', layar='blue')
            # ini handle ULIBPY_, __FILE, __PWD, etc
            content_to_insert = replace_from_configuration_replacer(content_to_insert, self_run_configuration_replacer)
            # ini hadnle __TEMPLATE_* dari %__TEMPLATE_...
            if hasattr(root_tree, 'variables'):
                content_to_insert = replace_from_configuration_replacer(content_to_insert, root_tree.variables)
            # END: replacer

            # indah4(f'[file>insert] barisno {line_number}, content [{content_to_insert.strip()[:100]}...] filepath {filepath}', warna='cyan')
            insert_at(filepath, line_number, content_to_insert)
        # end: I.

        # start: ia.
        elif ops_with_args[0] == 'ia':
            # insert_after(filepath, baris_cari, content_to_insert)
            # u -e"/file)ia/baris cari/isi tulisan|settings.py"
            pattern_to_search, content_to_insert = ops_with_args[1],ops_with_args[2:]
            content_to_insert = '/'.join(content_to_insert)
            content_to_insert = sanitize_chars(content_to_insert)
            insert_after(filepath, pattern_to_search, content_to_insert)
        # end: ia.

        # start: IA.
        elif ops_with_args[0] == 'IA':
            # insert_after(filepath, baris_cari, content_to_insert)
            # u -e"/file)IA/baris cari/filepath=barisentry|settings.py"
            pattern_to_search, perlu_filepath_samadengan_barisentry = ops_with_args[1],ops_with_args[2:]
            perlu_filepath_samadengan_barisentry = '/'.join(perlu_filepath_samadengan_barisentry)
            content_to_insert = filepath_samadengan_barisentry(perlu_filepath_samadengan_barisentry)
            content_to_insert = sanitize_chars(content_to_insert)
            # START: replacer
            if env_int('ULIBPY_FMUS_DEBUG')>1:
                indah4(f"""[fileops][cek replacer, item, dll pada 'IA']
                item = {item}
                parent = {item.parent}
                root = {root_tree}
                """, warna='cyan', layar='blue')
            # ini handle ULIBPY_, __FILE, __PWD, etc
            content_to_insert = replace_from_configuration_replacer(content_to_insert, self_run_configuration_replacer)
            # ini hadnle __TEMPLATE_* dari %__TEMPLATE_...
            if hasattr(root_tree, 'variables'):
                content_to_insert = replace_from_configuration_replacer(content_to_insert, root_tree.variables)
            # END: replacer
            insert_after(filepath, pattern_to_search, content_to_insert)
        # end: IA.

        elif ops_with_args[0] == 'ib':
            # insert_before(filepath, baris_cari, content_to_insert)
            # u -e"/file)ib/baris cari/isi tulisan|settings.py"
            pattern_to_search, content_to_insert = ops_with_args[1],ops_with_args[2:]
            content_to_insert = '/'.join(content_to_insert)
            content_to_insert = sanitize_chars(content_to_insert)
            insert_before(filepath, pattern_to_search, content_to_insert)

        elif ops_with_args[0] == 'IB':
            # insert_before(filepath, baris_cari, content_to_insert)
            # u -e"/file)IB/baris cari/filepath=barisentry|settings.py"
            pattern_to_search, perlu_filepath_samadengan_barisentry = ops_with_args[1], ops_with_args[2:]
            perlu_filepath_samadengan_barisentry = '/'.join(perlu_filepath_samadengan_barisentry) # berarti barisentry mengandung /
            content_to_insert = filepath_samadengan_barisentry(perlu_filepath_samadengan_barisentry)
            content_to_insert = sanitize_chars(content_to_insert)
            pattern_to_search = sanitize_chars(pattern_to_search)
            # START: replacer
            if env_int('ULIBPY_FMUS_DEBUG')>=1:
                indah4(f"""[fileops][cek replacer, item, dll pada 'IB']
                item = {item}
                parent = {item.parent}
                root = {root_tree}
                filepath = {filepath}
                ops_with_args = {ops_with_args}
                perlu_filepath_samadengan_barisentry = {perlu_filepath_samadengan_barisentry}
                pattern_to_search = {pattern_to_search}
                content_to_insert = {content_to_insert[:100]}...
                """, warna='cyan', layar='blue')
            # ini handle ULIBPY_, __FILE, __PWD, etc
            content_to_insert = replace_from_configuration_replacer(content_to_insert, self_run_configuration_replacer)
            # ini handle __TEMPLATE_* dari %__TEMPLATE_...
            if hasattr(root_tree, 'variables'):
                content_to_insert = replace_from_configuration_replacer(content_to_insert, root_tree.variables)
            # END: replacer
            insert_before(filepath, pattern_to_search, content_to_insert)

        # start: IA>.
        elif ops_with_args[0] == 'IA>':
            '''
            IA> utk insert after then tabify (>)
            IA>/pattern-to-search/file=entry/tab-spec
            IA>/pattern-to-search/file-entry/tab-spec
            contoh tab-spec:
                s/3/2
                space
                3 tab/space(s)
                2-space size
            '''
            # insert_after(filepath, baris_cari, content_to_insert)
            # u -e"/file)IA/baris cari/filepath=barisentry|settings.py"
            def modify_content(content_to_insert):
                # START: replacer
                # if env_int('ULIBPY_FMUS_DEBUG')>1:
                indah4(f"""[fileops][START replacer, item, dll pada 'IA>']
                item = {item}
                parent = {item.parent}
                root = {root_tree}
                """, warna='cyan', layar='blue')
                # ini handle ULIBPY_, __FILE, __PWD, etc
                content_to_insert = replace_from_configuration_replacer(content_to_insert, self_run_configuration_replacer)
                # ini hadnle __TEMPLATE_* dari %__TEMPLATE_...
                if hasattr(root_tree, 'variables'):
                    content_to_insert = replace_from_configuration_replacer(content_to_insert, root_tree.variables)
                return content_to_insert
                # END: replacer
            insert_after_then_tabify(filepath, ops_with_args, modify_content_callback=modify_content)
        # end: IA>.

        elif ops_with_args[0] == 'IB>':
            # insert_before(filepath, baris_cari, content_to_insert)
            # u -e"/file)IB/baris cari/filepath=barisentry|settings.py"
            def modify_content(content_to_insert):
                # START: replacer
                # if env_int('ULIBPY_FMUS_DEBUG')>1:
                indah4(f"""[fileops][START replacer, item, dll pada 'IB>']
                item = {item}
                parent = {item.parent}
                root = {root_tree}
                """, warna='cyan', layar='blue')
                # ini handle ULIBPY_, __FILE, __PWD, etc
                content_to_insert = replace_from_configuration_replacer(content_to_insert, self_run_configuration_replacer)
                # ini hadnle __TEMPLATE_* dari %__TEMPLATE_...
                if hasattr(root_tree, 'variables'):
                    content_to_insert = replace_from_configuration_replacer(content_to_insert, root_tree.variables)
                return content_to_insert
                # END: replacer
            insert_before_then_tabify(filepath, ops_with_args, modify_content_callback=modify_content)

        elif ops_with_args[0] == 'rx':
            # apply regex pada "file regex" ke "file target"
            # nothing to be done yet
            # /file)rx/regexfile.txt|targetfile.txt
            regexfile = ops_with_args[1]
            if not isfile(regexfile):
                if isfile(joiner(fmus.get_cwd_pwd(), regexfile)):
                    regexfile = joiner(fmus.get_cwd_pwd(), regexfile)
                    print(f'[fileops] new regexfile from cwd: {regexfile}')
            indah4(f'''[fileops]
            regexfile = {regexfile}
            filepath = {filepath}
            ''', warna='green')
            found_lines = against_regex(regexfile, filepath)
            if result_callback:
                result_callback(found_lines)

        elif ops_with_args[0] == 'repl': # replace string in file #1
            # replace string in file
            # /file)repl/yang_mau_dihapus/nilai_pengganti|filetarget
            yang_mau_dihapus,nilai_pengganti=ops_with_args[1],ops_with_args[2]
            indah4(f'''[fileops]
            replacing string from "{yang_mau_dihapus}" to "{nilai_pengganti}"
            filepath = {filepath}
            ''', warna='green')
            # replace_string_in_file(filepath, old_string, new_string, replace_count=-1)
            replace_string_in_file(filepath, yang_mau_dihapus, nilai_pengganti, replace_count=-1)

        elif ops_with_args[0] == 'REPL': # replace string in file #2
            # replace string in file
            # /file)REPL/yang_mau_dihapus/filepath=barisentry|filetarget
            yang_mau_dihapus,perlu_filepath_samadengan_barisentry=ops_with_args[1],ops_with_args[2]
            nilai_pengganti = filepath_samadengan_barisentry(perlu_filepath_samadengan_barisentry)
            nilai_pengganti = sanitize_chars(nilai_pengganti)
            indah4(f'''[fileops]
            replacing string from "{yang_mau_dihapus}" to "{nilai_pengganti}"
            filepath = {filepath}
            ''', warna='green')
            # replace_string_in_file(filepath, old_string, new_string, replace_count=-1)
            replace_string_in_file(filepath, yang_mau_dihapus, nilai_pengganti, replace_count=-1)

        elif ops_with_args[0] == 'repline': # replace line by lineno in file #1
            # replace line at line number
            # /file)repline/3/ini baris pengganti|filetarget
            line_number, content_to_replace = ops_with_args[1], ops_with_args[2]
            # replace_line_by_no(filepath, barisno, content_to_replace)
            if not line_number.startswith('-') and not line_number=='0':
                line_number = int(line_number)-1
            else: # -1 utk last line, 0 utk first line
                line_number = int(line_number)
            content_to_replace = sanitize_chars(content_to_replace)
            replace_line_by_no(filepath, line_number, content_to_replace)

        elif ops_with_args[0] == 'REPLINE': # replace line by lineno in file #1
            # replace line at line number
            # /file)REPLINE/3/filepath=entry|filetarget
            line_number, perlu_filepath_samadengan_barisentry = ops_with_args[1], ops_with_args[2]
            # replace_line_by_no(filepath, barisno, content_to_replace)
            if not line_number.startswith('-') and not line_number=='0':
                line_number = int(line_number)-1
            else: # -1 utk last line, 0 utk first line
                line_number = int(line_number)

            content_to_replace = filepath_samadengan_barisentry(perlu_filepath_samadengan_barisentry)
            content_to_replace = sanitize_chars(content_to_replace)
            replace_line_by_no(filepath, line_number, content_to_replace)

        elif ops_with_args[0] == 'replinefrom': # unused
            # replace_from(filepath, baris_cari, content_to_insert)
            # replinefrom/pola/content|file
            # replinefrom/pola/file=entry|file
            pass

        elif ops_with_args[0] == 'replinebetween': # unused
            # replace_between(filepath, baris_cari_start, baris_cari_end, content_to_insert)
            # replinefrom/start/end/content|file
            # replinefrom/start/end/file=entry|file
            pass

        elif ops_with_args[0] == '--':
            """
            remove_lines_by_prefix
            remove by patterns: --/pattern|file
            u -e"/file)--/table_name|target.txt"
            u -e"/file)--/table_name/2|target.txt"
            remove_lines_by_prefix(filepath, prefix_pattern, how_many_lines=1, re_prefixer='^')
            prefix_pattern
            """
            if len(ops_with_args)==2:
                howmany=1
                prefix_pattern = ops_with_args[1]
            else:
                prefix_pattern, howmany = ops_with_args[1], ops_with_args[2]
            remove_lines_by_prefix(filepath, prefix_pattern, how_many_lines=int(howmany), re_prefixer='^')

        elif ops_with_args[0] == '-':
            """
            remove_lines_by_no
            remove by line no: -/no/howmany|file atau -/no|file
            perlu dukung juga hapus dg baris expression, jd bisa dibbrp tempat sekaligus (spt join)
            u -e"/file)-/34|target.txt"
            u -e"/file)-/34/4|target.txt"
            remove_lines_by_no(filepath, barisno, how_many_lines=1)
            """
            if len(ops_with_args)==2:
                howmany=1
                barisno=ops_with_args[1]
            else:
                barisno,howmany=ops_with_args[1],ops_with_args[2]
            if not barisno.startswith('-') and not barisno=='0':
                barisno = int(barisno)-1
            else: # -1 utk last line, 0 utk first line
                barisno = int(barisno)
            howmany = int(howmany)
            remove_lines_by_no(filepath, barisno, how_many_lines=howmany)

        elif ops_with_args[0] .startswith('>'):
            '''
            indent_file
            indent file taking line-expression with tab-spec
            /file)>lineexpr/t|filepath
            /file)>lineexpr/t/1|filepath
            /file)>lineexpr/s|filepath
            /file)>lineexpr/s/3|filepath
            /file)>lineexpr/s/3/4|filepath
            '''
            line_expression = ops_with_args[0].removeprefix('>')
            use_tab = True
            num_tab = 1
            space_size = 2
            if ops_with_args[1].lower() == 's':
                use_tab = False
            if len(ops_with_args) == 3:
                num_tab = int(ops_with_args[2])
            elif len(ops_with_args) == 4 and not use_tab:
                num_tab = int(ops_with_args[2])
                space_size = int(ops_with_args[3])
            indent_file(filepath, line_expression, use_tab=use_tab, num_tab=num_tab, space_size=space_size)

        elif ops_with_args[0] .startswith('<'):
            """
            dedent_file
            """
            line_expression = ops_with_args[0].removeprefix('<')
            use_tab = True
            num_tab = 1
            space_size = 2
            if ops_with_args[1].lower() == 's':
                use_tab = False
            if len(ops_with_args) == 3:
                num_tab = int(ops_with_args[2])
            elif len(ops_with_args) == 4 and not use_tab:
                num_tab = int(ops_with_args[2])
                space_size = int(ops_with_args[3])
            dedent_file(filepath, line_expression, use_tab=use_tab, num_tab=num_tab, space_size=space_size)

        elif ops_with_args[0] .startswith('^>'):
            '''
            indent_file_by_pattern
            /file)^>pattern-cari/t|filepath
            /file)^>pattern-cari/t/1|filepath
            /file)^>pattern-cari/s|filepath
            /file)^>pattern-cari/s/3|filepath
            /file)^>pattern-cari/s/3/4|filepath
            '''
            search_pattern = ops_with_args[0].removeprefix('^>')
            if not search_pattern:
                indah4(f'''[fileops][^>]
                ops_with_args = {ops_with_args}
                ops_with_args[0] = {ops_with_args[0]}
                search_pattern = {search_pattern}
                ''', warna='cyan')
                return
            use_tab = True
            num_tab = 1
            space_size = 2
            if ops_with_args[1].lower() == 's':
                use_tab = False
            if len(ops_with_args) == 3:
                num_tab = int(ops_with_args[2])
            elif len(ops_with_args) == 4 and not use_tab:
                num_tab = int(ops_with_args[2])
                space_size = int(ops_with_args[3])
            indent_file_by_pattern(filepath, search_pattern, use_tab=use_tab, num_tab=num_tab, space_size=space_size)

        elif ops_with_args[0] .startswith('^<'):
            """
            dedent_file_by_pattern
            """
            search_pattern = ops_with_args[0].removeprefix('^<')
            if not search_pattern:
                indah4(f'''[fileops][^<]
                ops_with_args = {ops_with_args}
                ops_with_args[0] = {ops_with_args[0]}
                search_pattern = {search_pattern}
                ''', warna='cyan')
                return
            use_tab = True
            num_tab = 1
            space_size = 2
            if ops_with_args[1].lower() == 's':
                use_tab = False
            if len(ops_with_args) == 3:
                num_tab = int(ops_with_args[2])
            elif len(ops_with_args) == 4 and not use_tab:
                num_tab = int(ops_with_args[2])
                space_size = int(ops_with_args[3])
            dedent_file_by_pattern(filepath, search_pattern, use_tab=use_tab, num_tab=num_tab, space_size=space_size)

        elif ops_with_args[0] == 'I>':
            """
            I>/lineno/file=entry/tab-spec|filetarget
            
            insert tabified (content of file=entry) at line number in filepath

            tabified specification: t, t/2 = 2 tab, s, s/3 (3 spaces), s/3/2 (3 space2), s/3/4 (3 space4)

            /file)I>/3/filepath=barisentry/t|settings.py
            /file)I>/3/filepath=barisentry/t/2|settings.py
            /file)I>/3/filepath=barisentry/s|settings.py
            /file)I>/3/filepath=barisentry/s/3|settings.py
            3 space dg size 2
            /file)I>/3/filepath=barisentry/s/3/2|settings.py
            3 space dg size 4
            /file)I>/3/filepath=barisentry/s/3/4|settings.py
                  00 1 2222222222222222222 3 4 5
            len   1  2 3                   4 5 6
            """
            line_number, perlu_filepath_samadengan_barisentry = ops_with_args[1], ops_with_args[2]
            if not line_number.startswith('-') and not line_number=='0':
                # -1 utk last line, 0 utk first line, jd jangan di -1
                line_number = int(line_number)-1
            else:
                line_number = int(line_number)
            if not isfile(filepath):
                # jk gak ketemu, coba prefix dg current cwd
                if isfile(joiner(fmus.get_cwd_pwd(), filepath)):
                    filepath = joiner(fmus.get_cwd_pwd(), filepath)
                    print(f'[fileops] new filepath from cwd: {filepath}')
            content_to_insert = filepath_samadengan_barisentry(perlu_filepath_samadengan_barisentry)
            content_to_insert = sanitize_chars(content_to_insert)
            # indah4(f'[file>insert] barisno {line_number}, content [{content_to_insert.strip()[:100]}...] filepath {filepath}', warna='cyan')
            # skrg content kita tabify dulu...
            use_tab = True
            num_tab = 1
            space_size = 2
            s_t = ops_with_args[3]
            if s_t.lower() == 's':
                use_tab = False
            if len(ops_with_args) == 5:
                num_tab = int(ops_with_args[4])
            elif len(ops_with_args) == 6 and not use_tab:
                num_tab = int(ops_with_args[4])
                space_size = int(ops_with_args[5])
            from schnell.app.usutils import tab # tab(num=1, space=TAB_SPACE_MULT*' ', tab='\t', use_space=True)	
            tabber = tab(num=num_tab, use_space=False) if use_tab else tab(num=num_tab, space=space_size*' ', use_space=True)
            content_to_insert = [tabber+baris for baris in content_to_insert.splitlines()]
            content_to_insert = '\n'.join(content_to_insert)
            insert_at(filepath, line_number, content_to_insert)

        elif ops_with_args[0] == 'i>':
            '''
            insert tabified (literal content) at line number in filepath
            i>/lineno/<content>/tab-spec|file

            i> mengikuti I> tapi gunakan text dari command langsung, gak perlu filepath=barisentry
            '''
            line_number, content_to_insert = ops_with_args[1], ops_with_args[2]
            if not line_number.startswith('-') and not line_number=='0':
                # -1 utk last line, 0 utk first line, jd jangan di -1
                line_number = int(line_number)-1
            else:
                line_number = int(line_number)
            if not isfile(filepath):
                # jk gak ketemu, coba prefix dg current cwd
                if isfile(joiner(fmus.get_cwd_pwd(), filepath)):
                    filepath = joiner(fmus.get_cwd_pwd(), filepath)
                    print(f'[fileops] new filepath from cwd: {filepath}')
            # content_to_insert = filepath_samadengan_barisentry(perlu_filepath_samadengan_barisentry)
            content_to_insert = sanitize_chars(content_to_insert)

            use_tab = True
            num_tab = 1
            space_size = 2
            s_t = ops_with_args[3]
            if s_t.lower() == 's':
                use_tab = False
            if len(ops_with_args) == 5:
                num_tab = int(ops_with_args[4])
            elif len(ops_with_args) == 6 and not use_tab:
                num_tab = int(ops_with_args[4])
                space_size = int(ops_with_args[5])
            from schnell.app.usutils import tab # tab(num=1, space=TAB_SPACE_MULT*' ', tab='\t', use_space=True)	
            tabber = tab(num=num_tab, use_space=False) if use_tab else tab(num=num_tab, space=space_size*' ', use_space=True)
            content_to_insert = [tabber+baris for baris in content_to_insert.splitlines()]
            content_to_insert = '\n'.join(content_to_insert)
            insert_at(filepath, line_number, content_to_insert)

        elif ops_with_args[0] == 'replF': # replace_from (dari lokasi ke bottom)
            '''
            /file)replF/text-baris-cari/text-content
            '''
            pattern_to_search, content_to_insert = ops_with_args[1], ops_with_args[2:]
            content_to_insert = '/'.join(content_to_insert) # berarti barisentry mengandung /
            # namanya patterns, kadang berisi /
            pattern_to_search_start = sanitize_chars(pattern_to_search_start)
            pattern_to_search_end = sanitize_chars(pattern_to_search_end)
            content_to_insert = sanitize_chars(pattern_to_search_end)
            if '.mk=' in content_to_insert or '.fmus=' in content_to_insert:
                content_to_insert = filepath_samadengan_barisentry(content_to_insert)
            replace_from(filepath, pattern_to_search, content_to_insert)

        elif ops_with_args[0] == 'replU': # replace_until (dari top ke lokasi)
            '''
            /file)replU/text-baris-cari/text-content
            '''
            pattern_to_search, content_to_insert = ops_with_args[1],ops_with_args[2:]
            content_to_insert = '/'.join(content_to_insert) # berarti barisentry mengandung /
            # namanya patterns, kadang berisi /
            pattern_to_search_start = sanitize_chars(pattern_to_search_start)
            pattern_to_search_end = sanitize_chars(pattern_to_search_end)
            content_to_insert = sanitize_chars(pattern_to_search_end)
            if '.mk=' in content_to_insert or '.fmus=' in content_to_insert:
                content_to_insert = filepath_samadengan_barisentry(content_to_insert)
            replace_until(filepath, pattern_to_search, content_to_insert)

        elif ops_with_args[0] == 'replB': # replace_between (antara 2 lokasi)
            '''
            /file)replB/pattern_to_search_start/pattern_to_search_end/content_to_insert|filepath
            '''
            pattern_to_search_start, pattern_to_search_end, content_to_insert = ops_with_args[1],ops_with_args[2],ops_with_args[3:]
            content_to_insert = '/'.join(content_to_insert) # berarti barisentry mengandung /
            # namanya patterns, kadang berisi /
            pattern_to_search_start = sanitize_chars(pattern_to_search_start)
            pattern_to_search_end = sanitize_chars(pattern_to_search_end)
            content_to_insert = sanitize_chars(content_to_insert)
            if '.mk=' in content_to_insert or '.fmus=' in content_to_insert:
                content_to_insert = filepath_samadengan_barisentry(content_to_insert)
            replace_between(filepath, pattern_to_search_start, pattern_to_search_end, content_to_insert)

        elif ops_with_args[0] == '^-':
            '''hapus substring pada semua baris yg match
            replace string dg '' pada baris yg match re.sub => [re.sub(regex_expression, '', line) for line in content]

            /file)^-/ekspresi-regex|filetarget
            def remove_prefix_by_regex(filepath, regex_expression):
            '''
            regex_pattern_to_search = ops_with_args[1]
            remove_prefix_by_regex(filepath, regex_pattern_to_search)

        elif ops_with_args[0] == '#-':
            '''hapus substring pada baris2 linespec yg match
            hapus substring berpola regex-expr pada baris2 line-expr

            /file)#-/line-expr/regex-expr|filepath
            remove_prefix_by_lineno_and_regex(filepath, line_expression, regex_expression)
            '''
            line_expression, regex_expression = ops_with_args[1], ops_with_args[2]
            remove_prefix_by_lineno_and_regex(filepath, line_expression, regex_expression)

        elif ops_with_args[0] == '@':
            '''
            /file)@/start,end
            /file)@/,
            def sort_lines(filepath, start, end):
            bisa juga seharusnya
            '''
            lineno_start, lineno_end = [item.strip() for item in ops_with_args[1].split(',')]
            if not lineno_start:
                start = 0
            else:
                start = int(lineno_start)
            if not lineno_end:
                end = -1
            else:
                end = int(lineno_end)
            sort_lines(filepath, start, end)

        elif ops_with_args[0] == 'ts':
            # /file)ts|filepath
            # /file)ts/4|filepath
            spacesize = 2
            if len(ops_with_args) == 2:
                spacesize = int(ops_with_args[1])
            tab_to_space_start(filepath, tabstop=spacesize)

        elif ops_with_args[0] == 'st':
            # /file)st|filepath
            # /file)st/4|filepath
            spacesize = 2
            if len(ops_with_args) == 2:
                spacesize = int(ops_with_args[1])
            space_to_tab_start(filepath, tabstop=spacesize)

        elif ops_with_args[0] == 'ss':
            # /file)ss/2/4|filepath     ubah dari space 2 ke space 4
            # /file)ss/4/2|filepath     ubah dari space 4 ke space 2
            # spacesize = 2
            # if len(ops_with_args) == 2:
            spaceold_size = int(ops_with_args[1])
            spacenew_size = int(ops_with_args[2])
            space_to_space_start(filepath, spaceold_size, spacenew_size)

        elif ops_with_args[0] == 'iax':
            '''
            insert after by regex
            /file)iax/regex-cari/content|filepath
            /file)iax//content|filepath

            /file)iax/content|filepath

            update:
            /file)iax/regex-cari/content|filepath
            dimana regex-cari bisa kosong, jk kosong baru minta input
            /file)iax//content|filepath
                  0  1 2
            '''
            from schnell.app.fileutils import insert_after_by_regex
            from schnell.app.promptutils import prompt
            regex_yang_bisa_kosong = ops_with_args[1]
            content_to_insert = ops_with_args[2:]
            content_to_insert = '/'.join(content_to_insert) # berarti barisentry mengandung /
            if '.mk=' in content_to_insert or '.fmus=' in content_to_insert:
                content_to_insert = filepath_samadengan_barisentry(content_to_insert)
            content_to_insert = sanitize_chars(content_to_insert)
            print(f'iax: inserting [{content_to_insert}]')
            if not regex_yang_bisa_kosong:
                regex_yang_bisa_kosong = prompt("Masukkan pola untuk text untuk insert after, whitespace termasuk newline:")
            insert_after_by_regex(filepath, regex_yang_bisa_kosong, content_to_insert)
            print(f'iax: {filepath} ok.')

        elif ops_with_args[0] == 'riax':
            '''spt iax, alih2 insert-after, dia replace.
            replace by regex
                  0  1 2
            '''
            from schnell.app.fileutils import replace_by_regex
            from schnell.app.promptutils import prompt
            regex_yang_bisa_kosong = ops_with_args[1]
            content_to_insert = ops_with_args[2:]
            content_to_insert = '/'.join(content_to_insert) # berarti barisentry mengandung /
            if '.mk=' in content_to_insert or '.fmus=' in content_to_insert:
                content_to_insert = filepath_samadengan_barisentry(content_to_insert)
            content_to_insert = sanitize_chars(content_to_insert)
            print(f'riax: inserting [{content_to_insert}]')
            if not regex_yang_bisa_kosong:
                regex_yang_bisa_kosong = prompt("Masukkan pola untuk text untuk insert after, whitespace termasuk newline:")
            replace_by_regex(filepath, regex_yang_bisa_kosong, content_to_insert)
            print(f'riax: {filepath} ok.')
