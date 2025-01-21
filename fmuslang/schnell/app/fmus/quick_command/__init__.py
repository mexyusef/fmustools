import os
from schnell.app.autoutils import confirm
from schnell.app.fmusutils import get_input_generic
from schnell.app.printutils import indah3, indah4
from schnell.app.utils import env_get

from schnell.app.quick import process_language as quick_process_language
from schnell.app.quick import print_info
from schnell.app.quick.fileops import fileops
from schnell.app.dirutils import files_filter, joinhere, joiner
from schnell.app.dirutils import walk_fullpath, pemisah_direktori, subtract_normy_pathlist, normy, isdir, sdirs, isfile
from schnell.app.printutils import print_list_warna, indah4
from schnell.app.quick import handle_publish_to_redis
from schnell.app.utils import perintah_shell, linuxify, platform, env_int

from schnell.app.transpiler.frontend.main import process_language as declarative_process_language
from schnell.app.transpiler.frontend.fullstack import process_language as fullstack_process_language

# from schnell.app.transpiler.lalang import process_language as lalang_process_language
# from schnell.app.transpiler.refactor import process_language as lalang_process_language
from schnell.app.transpiler.nonredis import process_language as lalang_process_language

from schnell.app.transpiler.mycsv.process import process_language as mycsv_process_language
from schnell.autolang import handle_typing
from schnell.app.fmusutils import replace_from_configuration_replacer
from ..common import input_keyword, input_keyword_gui

quick_folder = joinhere(__file__, '../../quick')
blitz_folder = joinhere(__file__, '../../quick/blitz')
fileoperation_placeholder = '@@@'


def quick_command(root_tree, item, self_run_configuration_replacer=None, self_run_configuration=None):
  '''
  ini jadi senjata utama menghadapi berbagai interview dan coding test.
  | "/" quick_command
  | "*" special_command
  special_command: MENGANDUNG_AMPERSAND_DAN_TANDASERU
  quick_command: MENGANDUNG_AMPERSAND_DAN_TANDASERU

  /<perintah fullstack>
  /something,*/kode csv
  /uecommdj,*/B^..^
  biasanya:
  u -e'***uecommdj,*/B^^'
  sekarang jadi:
  u -e/uecommdj,*/B^^

  kita tambah berikut:
  jk item.command dimulai dg / maka search spt special command
  //uecommdj, dll < jangan lupa // bukan /
  '''

  if env_int('ULIBPY_FMUS_DEBUG')>1:
    indah4(f"""[quick_command.__init__:quick_command] INITIAL
      root_tree   = {root_tree}
      item        = {item}
      """, warna='yellow')

  os.chdir(item.workdir)
  request = item.command
  # sementara baru @ dan / yg dukung __WORKDIR__
  request = request.replace('__WORKDIR__', item.workdir)

  # if env_int('ULIBPY_FMUS_DEBUG')>=1:
  #   indah4(f"""[quick_command.__init__:quick_command] #step 1
  #     root_tree   = {root_tree}
  #     item        = {item}
  #     """, warna='yellow')

  # skip jk __INPUT__ dari template yg akan diproses dg new_replacer_input
  if not (hasattr(root_tree, 'input_keys') and len(root_tree.input_keys)):
    request = get_input_generic(request)

  if request == '/': # //
    '''
    -e//
    -e// strip -e/ hasilkan /
    sama/setara dg -e/i/
    '''    
    print_info()

  elif request == ')':
    '''
    -e/)
    kita print semua file .txt di schnell/app/quick
    kita berada di schnell/app/fmus/quick_command
    '''    
    files = files_filter(quick_folder, extension=['.txt'])
    print_list_warna(files)
    indah4('Masukkan nomer utk file:', warna='cyan', newline=False)
    masuk = input(' ')
    if masuk:
      if masuk.isdigit():
        angka = int(masuk)
        if 0<=angka<len(files):
          pilih = files[angka]
          # print('terima:', pilih)
          print_info(pilih)

  elif request .startswith('))'):
    '''
    -e/))
    -e/))py
    -e/))react
    '''
    global blitz_folder
    request = request.removeprefix('))')
    if request == '/':
      # /))/
      print_list_warna(sdirs(blitz_folder))
      blitz_folder = None
    elif request == '//':
      # /))//
      cmd = f"wsl tree -d -I 'node_modules' -I '__pycache__' {linuxify(normy(blitz_folder))}"
      # sementara hanya pada windows yg mendukung wsl      
      if platform() == 'desktop':
        cmd = f"tree {normy(blitz_folder)}"      
      # indah4(f'''
      #   platform = {platform()}
      #   cmd = {cmd}
      #   ''', warna='green')
      perintah_shell(cmd)
      blitz_folder = None
    elif request .startswith ('///'):
      # /))///
      if request == '///':
        cmd = f"wsl tree -I 'node_modules' -I 'output.fmus' -I '__pycache__' {linuxify(normy(blitz_folder))}"
        if platform() == 'desktop':
          cmd = f"tree /F \"{normy(blitz_folder)}\""
        # perintahsp_simple(cmd) # desktop gak mau
        perintah_shell(cmd)
      else:
        #find_patterns(code, basedir, config=None)
        from schnell.app.dirutils import find_patterns
        code = request.removeprefix('///')
        edit_file = False
        if code.endswith('*'):
          code = code.removesuffix('*').strip()
          edit_file = True

        res = find_patterns(code, blitz_folder, kurangi_prefix=blitz_folder, returning=True)
        # print('kembalian:', res)

        if edit_file and len(res)==1:
          perintah_shell(f'code {res[0]}')

      blitz_folder = None

    elif request:
      # /))something
      blitz_folder = joiner(blitz_folder, request)
      # indah4(f'''
      # request {request} in targetfolder {blitz_folder}
      # ''', warna='blue')
    else:
      indah4(f'''
      not processing {request} in {blitz_folder}
      ''', warna='red')

    if blitz_folder and isdir(blitz_folder):
      # files = files_filter(target_folder, extension=['.fmus'])
      files = walk_fullpath(blitz_folder, filtered_ends='.fmus')
      # kita di /quick/blitz/ tentu hilangkan semua ini
      # plus hilangkan juga yg diminta oleh user (request), ))react -> hilangkan quick/blitz/react
      # biar gak terlalu rame
      relative_prefix = normy('app/quick/blitz/' + request )
      hapus = normy(env_get('ULIBPY_BASEDIR')+pemisah_direktori()+relative_prefix)
      # indah4(f'''
      #   request = {request}
      #   relative_prefix = {relative_prefix}
      #   hapus = {hapus}
      # ''', warna='blue')
      # krn kadang \react\one.fmus, maka hilangkan \ di awal jk ada
      res = [item.removeprefix(pemisah_direktori()) for item in subtract_normy_pathlist(files, hapus)]
      print_list_warna(res)
      indah4(f'''
        u -e"/b>react/news1"
        u -e/)        choose txt to read
        u -e/))
        u -e/))py
        u -e/))/      dirs
        ''', warna='cyan')
    else:
      if blitz_folder:
        indah4(f'''
        not processing "{request}" in {blitz_folder}
          isfile:{isfile(blitz_folder)}
          isdir: {isdir(blitz_folder)}
        perhaps you meant: 
        u -e"/b>{request}"
        instead of
        u -e/)){request}
        ''', warna='red')
      # else:
      #   indah4('''
      #   not processing "{request}" in {blitz_folder}
      #   blitz_folder is None.
      #   ''', warna='red')

  elif request.startswith('('):
    '''
    u -e/(type/params
    '''
    request = request.removeprefix('(')
    from schnell.app.quick.fakerer import handle_faker
    handle_faker(request)

  # ini sudah tidak ada
  elif request.startswith('/'): # //query
    '''
    u -e//kata-cari
    '''
    request = request.removeprefix('/')
    # from schnell.db import redis_repl
    from schnell.db.myredis import redis_repl
    redis_repl(request, None)

  elif request.startswith('f.'):
    '''
    mending gini, ada 4 bahasa: fs, mycsv, lalang, frontend/declarative

    from schnell.app.transpiler.frontend.fullstack import process_language
    -e/f. <kode fullstack-process-language>

    biasanya kita bisa
    u -e/crajs/1
    ini tapi dari bahasa quick

    gimana lakukan hal yg sama di sini?
    u -e"/f. nda/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^"
    u -e"/f. mrcli/B"
      statement
        statement_config
          statement_config_list
            misc_rustcli
        backend_statement

      handler: statement
      hasil statement_config_list {'be': 'rustcli'}
      backend_statement: backend_statement
      'be'
      Traceback (most recent call last):
        File fullstack.py, line 233, in process_language
          hasil = handler(insn)
        File fullstack.py", line 198, in handler
          res = backend_statement(item)
        File backend_statement.py, line 124, in backend_statement
          if program_config['config']['be'] in generator_utils.keys():
      KeyError: 'be'
    u -e"/f. mrcli,*/B"
    '''    
    request = request.removeprefix('f.').lstrip()
    filepath, barisentry = fullstack_process_language(request, returning=True)
    indah4(f'''
    filepath    = {filepath}
    barisentry  = {barisentry}
    ''', warna='cyan')

  elif request.startswith('c.'):
    '''
    u -e"/c. go/{@User}username,s;email,s"
    u -e"/c. pris/{@User}username,s;email,s"
    u -e"/c. ts/{@User}username,s;email,s"

    u -e"/c. [i/0/@@@|main.go] go/{@User}username,s;email,s"
    '''
    request = request.removeprefix('c.').lstrip()
    operations, filename = '', ''
    if request.startswith('['):
      '''
      @@@ utk direplace dg hasil csvlang, misal:
      c.[i/0/@@@|main.go]go/{@Fact}ID,i;Description,s
      '''
      indah4(f'''[app.fmus.quick_command]
      request = {request} berisi '['
      ''', warna='blue')

      from .extract_fileops import extract_fileops
      operations, filename, csvcode = extract_fileops(request)
      if operations and filename and csvcode:
        # fileops(f'touch|{filename}')
        # fileops(operations)
        request = csvcode.strip()
        indah4(f'''
        request fileops
        operations    = {operations}
        filename      = {filename}
        csvcode       = {csvcode}
        request       = {request}
        ''', warna='green')
    hasil = mycsv_process_language(request, returning=True)
    # stringify
    hasil = '\n'.join(hasil)

    if operations and filename:
      # jika hasil ke file
      hasil = hasil.replace('|', '__PP').replace('/', '__SL')
      # kita add new line dari hasil
      # i/0/@@@, ganti fileoperation_placeholder @@@ dg hasil
      operations = operations.replace(fileoperation_placeholder, hasil+'__NL')
      # indah4(f'''
      # fileops: {operations}
      # ''', warna='red')
      fileops(f'touch|{filename}', item=item)
      fileops(operations + '|' + filename, item=item)
    else:
      # jika hasil ke stdout
      indah4(f'''[quick_command/mycsv_process_language]''', warna='yellow')
      indah3(hasil, warna='white')
      # # publish juga ke yellownote
      # handle_publish_to_redis(hasil)

  elif request.startswith('l.'):
    '''
    u -e"/l. go/Pmynewpackage"
    u -e"/l. [i/0/@@@|pkg.go] go/Pmynewpackage"
    '''
    request = request.removeprefix('l.').lstrip()

    # jk meminta nulis ke file utk output
    operations, filename = '', ''
    if request.startswith('['):
      indah4(f'''
      request = {request} berisi '['
      ''', warna='blue')
      from .extract_fileops import extract_fileops
      operations, filename, csvcode = extract_fileops(request)
      if operations and filename and csvcode:
        # fileops(f'touch|{filename}')
        # fileops(operations)
        request = csvcode.strip()
        indah4(f'''
        request fileops
        operations    = {operations}
        filename      = {filename}
        csvcode       = {csvcode}
        request       = {request}
        ''', warna='green')

    hasil = lalang_process_language(request, returning=True)
    # stringify
    if isinstance(hasil, list):
      hasil = '\n'.join(hasil)

    if operations and filename:
      # ini klo gak salah, menjadikan output ke file
      hasil = hasil.replace('|', '__PP').replace('/', '__SL')
      operations = operations.replace(fileoperation_placeholder, hasil+'__NL')
      fileops(f'touch|{filename}', item=item)
      fileops(operations + '|' + filename, item=item)
    else:
      indah4(f'''[quick_command/lalang_process_language]''', warna='yellow')
      indah3(hasil, warna='white')
      # # publish juga ke yellownote
      # handle_publish_to_redis(hasil)

  elif request.startswith('d.'):
    # u -e"/d. <a<b(<c/disabled/<d<e/nilai=kuda/sampurasun(<f<g))"
    # ;r /d. <a<b(<c[disabled]<d<e[nilai=kuda]|sampurasun(<f<g))
    # u -e"/d. [i/0/@@@|main.html] <a<b(<c/disabled/<d<e/nilai=kuda/sampurasun(<f<g))"

    request = request.removeprefix('d.').lstrip()
    operations, filename = '', ''
    if request.startswith('['):
      indah4(f'''
      request = {request} berisi '['
      ''', warna='blue')
      from .extract_fileops import extract_fileops
      operations, filename, csvcode = extract_fileops(request)
      if operations and filename and csvcode:
        # fileops(f'touch|{filename}')
        # fileops(operations)
        request = csvcode.strip()
        indah4(f'''
        request fileops
        operations    = {operations}
        filename      = {filename}
        csvcode       = {csvcode}
        request       = {request}
        ''', warna='green')
    # hasil = mycsv_process_language(request, returning=True)
    hasil = declarative_process_language(request, returning=True)
    if isinstance(hasil, list):
      hasil = '\n'.join(hasil)
    if operations and filename:
      hasil = hasil.replace('|', '__PP').replace('/', '__SL')
      operations = operations.replace(fileoperation_placeholder, hasil+'__NL')
      fileops(f'touch|{filename}', item=item)
      fileops(operations + '|' + filename, item=item)
    else:
      indah4(f'''[quick_command/declarative_process_language]''', warna='yellow')
      indah3(hasil, warna='white')
      # handle_publish_to_redis(hasil)

  elif request.startswith('b.'):
    request = request.removeprefix('b.').lstrip()
    # print('[quick_command][b.] code utk backend:', request)
    if not request:
      indah4('''[quick_command/backend_process_language]
      ../b.
      ../b. #api/users@gp#cors|hello, boyz!;
      ../b. #api/users@gp#cors/200|huruf text bahasa;
      ../b. #api/users@gp#cors/200|{1=satu,2=dua,3=tiga};
      ../b. #api/users@gp#cors/200|@ts/%name='usef';
      ../b. dj#api/users@gp#cors/200|@ts/$name='wieke';
      ../b. [:8000][/tempdb]dj#api/users@gp#cors/200|@ts/%name='usef';
      ../b. [:8000][usef:rahasia@localhost:6379/tempdb]dj#api/users@gp#cors/200|@ts/%name='usef';
      ../b. [0.0.0.0:8000][usef:rahasia@localhost:6379/tempdb]dj#api/users@gp#cors/200|@ts/%name='usef';

      ../b. nd#/api/users@g |@ts/||/sc/{?+'hello'; ?+'wieke'; ?+'monyong'; res.send('kuda')} ;;
      ../b. nd#/api/users@g |@ts/||{?+'hello'; ?+'wieke'; ?+'monyong'; res.send('kuda')} ;;
      ''', warna='green')
    else:
      from schnell.app.transpiler.backend.main import process_language as backend_process_language
      backend_process_language(request)

  elif request.startswith('y.'):
    '''
    ../y. localhost:9222/users/update_password p json {identitas=Wiranto,password=rahasia}
    '''    
    request = request.removeprefix('y.').lstrip()
    if not request:
      indah4('''[quick_command/curly_process_language]
      ../y. localhost:9000/items p json {user=name}
      ../y. localhost:9001/rest/books p raw <{allBooks{isn;title}}>
      ../y. localhost:9222/users/update_password p json {identitas=Wiranto,password=rahasia}
      ../y. https://www.upwork.com/nx/jobs/search/?q=fullstack&from_recent_search=true&sort=recency
      ../y. https://www.upwork.com/Ss13U803/captcha/PXSs13U803/captcha.js?a=c&m=0&u=5c889419-c1f3-11ec-a7d9-5845654c7671&v=
      ''', warna='green')
    else:
      from db.generator.curly import process_language as curly_process_language
      hasil, err = curly_process_language(request, force=True)
      indah4(f'''[quick_command/curly_process_language]''', warna='yellow')
      indah3(hasil, warna='white')
      # # publish juga ke yellownote
      # handle_publish_to_redis(hasil)

  elif request == 'F.':
    from schnell.app.transpiler.frontend.fullstack import quick_repl
    quick_repl()

  elif request == 'C.':
    from schnell.app.transpiler.mycsv.process import quick_repl
    quick_repl()

  elif request == 'L.':
    from schnell.app.transpiler.lalang import quick_repl
    quick_repl()

  elif request == 'D.':
    from schnell.app.transpiler.frontend.main import quick_repl
    quick_repl()

  elif request == 'B.':
    '''
    fm//B.
    '''
    from schnell.app.transpiler.backend.main import quick_repl
    quick_repl()

  elif request.startswith('git/'):
    '''
    /git/ perintah...
    '''
    import schnell.app.gitutils as gitter
    code = request.removeprefix('git/').strip()
    # fungsi, args = map(str.strip, code.split(' ', 1))
    # indah4('''
    # repo_index(dirpath)
    # git_add(repo, file)
    # git_adds(repo, files)
    # git_status(repo)
    # git_commit(repo, msg)
    # index_commit(index, msg)
    # rh_status(key)
    #   /git/rh_status sido
    #   /git/rh_status mmm
    #   /git/rh_status sejarah
    # ''', warna='white')
    if code:
      pecah = [item.strip() for item in code.split(' ', 1)]
      if pecah:
        fungsi = pecah[0]
        if len(pecah)==2:
          res = getattr(gitter, fungsi)(pecah[1])
        else:
          res = getattr(gitter, fungsi)()
        indah4(res, warna='green')

  elif request.startswith('lara/'):
    query = request.removeprefix('lara/').strip()
    handle_typing('T:(lara 01031995)~1000,900/~1000,900|'+query)

  elif request.startswith('gaia/'):
    query = request.removeprefix('gaia/').strip()
    handle_typing('T:(gaia 01031997)~1000,900/~1000,900|'+query)

  elif request.startswith('wieke/'):
    query = request.removeprefix('wieke/').strip()
    handle_typing('T:(wieke 01031999)~1000,900/~1000,900|'+query)

  else: # /others = quick language
    '''
    -e/<app-quick-process-language>
    -e/ masuk sini (front menu)
    -e/i/ masuk sini
    -e/ls/ juga masuk sini
    '''
    # cek jk ada __INPUT__ pada item.command/request
    # indah4('>>before quick language', warna='cyan')
    if input_keyword in request or input_keyword_gui in request:
      '''
      "new_replacer_input": {
        "__TEMPLATE_NOMOR_BARIS": "9",
        "__TEMPLATE_ALAMAT_URL": "kk"
      }
      request adlh  file>i/__INPUT__/c.Visit("http://__INPUT__")|main.go
      command     ='file>i/__INPUT__/c.Visit("http://__INPUT__")|main.go'
      original    ='/file>i/__TEMPLATE_NOMOR_BARIS/c.Visit("http://__TEMPLATE_ALAMAT_URL")|main.go'
      '''
      if "new_replacer_input" in self_run_configuration:
        request = item.original.removeprefix('/')
        # ubah dari item.command ke item.original
        # jangan lupa remove prefix quick /
        # krn item.command sudah jadi __INPUT__ semua...
        for k,v in self_run_configuration["new_replacer_input"].items():
          request = request.replace(k, v)

        # indah4(f'''
        # skrg request adlh {request}
        # ''', warna='yellow')

    if self_run_configuration_replacer:
      # request mungkin ada __FILE__ atau __CURDIR__
      # misal: /D>=filepath=barisentry      
      request = replace_from_configuration_replacer(request, self_run_configuration_replacer)

    quick_process_language(request, root_tree, item, self_run_configuration_replacer)
    # indah4('>>after quick language', warna='cyan')
