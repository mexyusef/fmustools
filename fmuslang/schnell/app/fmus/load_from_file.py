from .common import Common, input_keyword
from schnell.app.dirutils import (
  isfile, joiner, exists_in_dir, ayah, absolute,
)
from schnell.app.fileutils import (
	replace_from,
	replace_at,
	insert_after,
	insert_before,
  insert_at, # f=capcay.txt,iA=barisentry=-1
	remove_lines,
	replace_entry,
	replace_between,
	replace_string_in_file,
  replace_file_content,
  comment_file, # comment_file(filepath, baris_cari, comment='#', space='', how_many_lines=1)
	tab_to_space_start,
)
from schnell.app.treeutils import get_all_parent_variables
from schnell.app.printutils import indah0, indah4
from schnell.app.utils import env_int

# elif oper .startswith ('load_from_file') and not oper.startswith('load_from_file_absolute'):
def load_from_file(oper, item, self_debug, self_run_configuration, self_generator_replace_me):
  '''
  TODO:
  - perbaiki ambil sumber templates
  - utk insert before misanya baru bisa gini
  monyong.txt,f(f=huckleberry.txt,@ib=line_pengganti=Release Date)
  Release Date terlalu sederhana, pengen bisa ada ' koma, dst
  krn jk isi file panjang maka perlu spesifik line indicator nya.
  Release Date diambil dari HURUF_FOLDER_LAMA
  coba kita ganti ke MENGANDUNG_AMPERSAND_DAN_TANDASERU
  | "ib" "=" singkat "=" MENGANDUNG_AMPERSAND_DAN_TANDASERU -> insert_before
  kita coba dg line_indicator:
  Release Date: August, 1993 [eBook #76]
  '''

  # root_tree = item.parent

  # indah4(f'''OLD
  #   item = {item}
    
  #   workdir = {item.workdir}

  #   ''', warna='red')
  if input_keyword in item.workdir:
    '''
    root:
    input_keys=['__TEMPLATE_BASEFOLDER'], 
    input_keys_index=0
    variables={'__TEMPLATE_BASEFOLDER': 'emih', '__TEMPLATE_PORT': '8000'}
    item:
    workdir='C:\\work\\tmp\\__INPUT__'
    '''
    from schnell.app.treeutils import replace_workdir__INPUT__with_value_from_parent
    item.workdir = replace_workdir__INPUT__with_value_from_parent(item)
    # indah4(f'''NEW
    #   item = {item}
      
    #   workdir = {item.workdir}

    #   ''', warna='red')
    # input(' ...press utk lanjut... ')


  target = item.workdir
  sumber = oper.split('=') [1]

  # sumber di sini bisa berisi __FILE__ atau __CURDIR__
  # run_configuration['replacer']
  sumber = self_generator_replace_me(sumber)

  # kita normalize dan absolute-kan path dulu utk cek isfile
  from schnell.app.dirutils import absnormpath, isdir, isfile, isabsolute
  sumber = absnormpath(sumber)
  # print(f'load from file dari: {sumber} isfile={isfile(sumber)} dan target: {target}')

  if not isfile(sumber):
    templatedir_sumber_copy = self_run_configuration['templatesdir']
    # default dari templates
    if not isabsolute(sumber):
      source = joiner(templatedir_sumber_copy, sumber)
    else:
      source = sumber
    if not isfile(source):
      if hasattr(item, 'line_content') and hasattr(item, 'line_indicator'):
        # utk operasi insert/replace maka source dan target sama
        source = item.workdir
        if env_int('ULIBPY_FMUS_DEBUG')>=1:
          indah4(f'[load_from_file] setting source ke workdir {source} utk insert/replace')
      else:
        import os
        indah4(f'''[load_from_file]
        {source} tidak ditemukan!
        cek perbedaan CWD dan __CURDIR berikut:
        CWD       : {os.getcwd()}
        __CURDIR  : {self_run_configuration['replacer']['__CURDIR__']}
        __FILE    : {self_run_configuration['replacer']['__FILE__']}      
        oper      : {item.operations}
        workdir   : {item.workdir}
        item      : {item}
        templatedir_sumber_copy       : {templatedir_sumber_copy}
        sumber = oper.split('=') [1]  : {sumber}
        ''', warna='red', layar='black')
  else:
    # jk sudah filepath lengkap, berarti pengen langsung dari situ
    source = sumber

  
  # precedence: 1) item.workdir (file) 2) item.curdir (dir) + filename 3) templatesdir + filename
  # no 1) krn misal Cargo.toml sudah digenerate oleh perintah sebelumnya (cargo new ...)
  workdir = ayah(item.workdir, 1)
  if exists_in_dir(workdir, sumber):
    source = joiner(workdir, sumber)
    # print('ganti source ke:', source)

  if isfile(source):
    source = isfile(source) # do_bongkar jk ya ada filenya
    if env_int('ULIBPY_FMUS_DEBUG')>1:
      self_debug('[load_from_file]', source, 'ke:', target)
    # print('load_from_file', source, 'ke:', target, '\n* item:', item)
    # jk ada insert_replace dan line_indicator maka gak operasi copy
    # jg harus bedakan item.workdir yg sudah ada atau belum ada
    # source: Cargo.toml dan target: Cargo.toml
    # Cargo.toml,f(f=Cargo.toml)
    # Cargo.toml,f(f=some_random_file.toml)
    # operasi copy
    data = ''
    binary_mode = '' if not hasattr(item, 'binary_mode') else 'b'
    with open(source, 'r'+binary_mode) as fd:
      data = fd.read()
    if data:
      with open(target, 'w'+binary_mode) as fd:
        fd.write(data)
    
    # self_debug(os.listdir(os.path.dirname(target))) # workdir adlh file
    if hasattr(item, 'line_indicator') \
      and hasattr(item, 'line_content') \
      and hasattr(item, 'insert_replace'):

      # if env_int('ULIBPY_FMUS_DEBUG')>0:
      #   self_debug('[load_from_file] Masuk ada line_indicator/marker di target etc.\n')
      # indah0(f"\n\nreplace string from [{item.line_indicator}] to [{item.line_content}], utk node {item}\n\n", warna='white', bold=True)

      if item.insert_replace == 8:
        '''
        replace_string
        "rs" "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> replace_string
        myfile.txt,f(f,@rs="baru"="replace")
        di sini baru hapus sebanyak 1 string saja...yg pertama ditemukan
        '''
        replace_string_in_file(item.workdir, item.string_new, item.string_old)
      elif item.insert_replace == 10:
        '''
        comment_file
        '''
        # comment_file(filepath, baris_cari, comment='#', space='', how_many_lines=1)
        # NewNode.line_indicator = baris_untuk_dikomentari
        # NewNode.line_content = simbol_komentar
        # indah4(f'[load_from_file] commenting file [{item.workdir}] utk baris berisi [{item.line_indicator}]', warna='blue')
        # skip_starting_whitespace agar mulai simbol komnetar dari sejak ada karakter, skip whitespace di awal baris
        comment_file(item.workdir, item.line_indicator, comment=item.line_content, skip_starting_whitespace=True)
        # success, message = True, "OK"
      else:
        replacer_file = self_run_configuration['replacer']['__FILE__']
        # current_directory = self_run_configuration['replacer']['__CURDIR__']
        # if not absolute(item.workdir):
        #   item.workdir = joiner(current_directory, item.workdir)
        pengisi = Common.definisi(item.line_content, replacer_file)
        # proses replacer di dalam new string (yg adlh baris_entry)
        for k,v in self_run_configuration['replacer'].items():
          pengisi = pengisi.replace(k, str(v))
        # cari semua variabels dari parent
        
        node_variables = get_all_parent_variables(item, {})
        if env_int('ULIBPY_FMUS_DEBUG')>=1:
          indah4(f'[load_from_file] node variables: {node_variables}', warna='yellow')
        for k,v in node_variables.items():
          pengisi = pengisi.replace(k, str(v))

        # item.line_indicator berarti di sini literal ya...bukan dari entry file
        # mungkin nanti kasih startswith('*') utk ambil dari self.run_configuration['replacer']['__FILE__']
        
        if env_int('ULIBPY_FMUS_DEBUG')>=1:
          self_debug(f'[load_from_file] replacing [{item.line_indicator}] dengan [{pengisi}] dalam file: {item.workdir}.\n')
        # indah4(f'replacing [{item.line_indicator}] dengan [{pengisi}] dalam file: {item.workdir}, item adlh {item}, runconfig {self_run_configuration}.\n', warna='yellow')

        success, message = None, "Belum diproses"
        if item.insert_replace == 1:
          success, message =  insert_before(item.workdir, item.line_indicator, pengisi)
        elif item.insert_replace == 2:
          success, message =  insert_after(item.workdir, item.line_indicator, pengisi)
        elif item.insert_replace == 3:
          success, message =  replace_at(item.workdir, item.line_indicator, pengisi)
        elif item.insert_replace == 4:
          success, message =  replace_from(item.workdir, item.line_indicator, pengisi)
        elif item.insert_replace == 5:
          success, message =  remove_lines(item.workdir, item.line_indicator, int(item.jumlah_hapus))
        elif item.insert_replace == 6:
          success, message =  replace_entry(item.workdir, item.line_indicator, pengisi)
        elif item.insert_replace == 7:
          if hasattr(item, 'line_indicator_end'):
            success, message = replace_between(item.workdir, item.line_indicator, item.line_indicator_end, pengisi)
        elif item.insert_replace == 9:
          success, message = replace_file_content(item.workdir, pengisi)
        elif item.insert_replace == 11:
          '''
          insert_at utk bisa insert content disembarang line number
          
          insert_at(filepath, nomor_baris, content_to_insert)

          NewNode.insert_replace = 11 # 1 = ib, 2 = ia, 3 = ra, 4 = rf, 5 = remove lines
          NewNode.line_indicator = baris_entry
          NewNode.line_content = linenumber_lokasi_insert
          '''
          success, message = insert_at(item.workdir, int(item.line_content), pengisi)

        if not success:
          indah4(message, warna='red')

    if hasattr(item, 'tab_to_space'):
      # sementara fungsi ini hanya ada di file,f(f=...,@ts)
      if env_int('ULIBPY_FMUS_DEBUG')>=1:
        self_debug(f'[load_from_file] tab_to_space untuk [{item.workdir}]\n')
      tab_to_space_start(item.workdir)

    if hasattr(item, 'fileops_operation'):
      indah4(f"[load_from_file] found fileops_operation => {item.fileops_operation}", warna='black', layar='red')

