# pylint: disable=W0105
import os
from schnell.app.dirutils import basename, isabsolute
from schnell.app.fmusutils import (
  get_input_from_user_or,
  get_input_from_user,
  get_input_from_user_gui,
)
from schnell.app.printutils import indah4
from schnell.app.utils import env_int
from .common import Common, input_keyword
from .treehelper import get_direct_children, get_all_tree_children, get_siblings_after


def update_root(kunci_variable, root_tree):
  if not hasattr(root_tree, 'input_keys'):
    root_tree.input_keys = [kunci_variable]
  else:
    root_tree.input_keys .append(kunci_variable)
  # item.input_key = kunci_variable # utk menjejak key utk gampang peroleh "masukan"
  # root_tree.input_key = kunci_variable # utk menjejak key utk gampang peroleh "masukan"
  root_tree.input_keys_index = len(root_tree.input_keys) - 1


def update_children(masukan, item):
  for anak_langsung in get_direct_children(item):
    # cek %anak
    if hasattr(anak_langsung, 'variables'):
      for k,v in anak_langsung.variables.items():
        if v == input_keyword:
          anak_langsung.variables[k] = masukan


def update_after_siblings(masukan, item, kunci_variable):
  for sodara in get_siblings_after(item):
    if (hasattr(sodara, 'old_name') and sodara.old_name == kunci_variable 
        and kunci_variable in sodara.original):
      temp_ganti = sodara.name
      sodara.name = masukan
      sodara.workdir = sodara.workdir.replace(temp_ganti, masukan)
      for sepupu in get_all_tree_children(sodara):
        if hasattr(sepupu, 'variables') and len(sepupu.variables) > 0:
          for k,v in sepupu.variables.items():
            if v==input_keyword:
              if k in item.variables:
                nilai_untuk_anak_following_sibling = item.variables[k]
                sepupu.variables[k] = nilai_untuk_anak_following_sibling
        sepupu.workdir = sepupu.workdir.replace(input_keyword, masukan, 1)
    else:
      indah4(f"""[simpan_temp_vars][update_after_siblings]
      bermasalah mengenai: ubah __TEMPLATE_WHATEVER dari following-siblingnya %
      tidak diproses krn gak penuhi kriteria (hrs True semua)
      hasattr(sodara, 'old_name') = {hasattr(sodara, 'old_name')}
      and sodara.old_name == kunci_variable = {sodara.old_name == kunci_variable}
      and kunci_variable in sodara.original = {kunci_variable in sodara.original}
      pada item:
      {item}
      """, warna='red')


def condition_to_process_sodara(sodara, item, root_tree, is_debugging=0):
  """  
  %MYVAR=__OPENFILE__
  kunci_variable=MYVAR
  item.singkat=MYVAR
  item.panjang=__OPENFILE__
  item.variables[item.singkat] = masukan
  e.g. variables={'MYVAR': 'C:/hapus/get-pip.py'}

  sodara.content contains item.panjang
  sodara.original contains item.singkat
  """
  if is_debugging:
    indah4(f"""condition_to_process_sodara, item [{item.original}], sodara [{sodara.original}]
      item {item}
      sodara {sodara}
      """, warna='cyan', layar='blue')
  # kunci_variable = item.singkat
  if (hasattr(sodara, 'old_name') and sodara.old_name == item.singkat
      and item.singkat in sodara.original):
    if is_debugging:
      print(f"[condition_to_process_sodara] process [{sodara.original}] gaya #1 => {sodara}")
    return True
  if item.panjang in ['__OPENFILE__','__SAVEFILE__'] and item.singkat in sodara.original:
    # or (hasattr() and item.panjang in sodara.content):
    if hasattr(sodara, 'content') and item.panjang in sodara.content:
      if is_debugging:
        print(f"[condition_to_process_sodara] process [{sodara.original}] gaya #2a => {sodara}")
      return True
    elif (sodara.name=='simpan_temp_vars'
      and sodara.old_panjang_sebelum_replace_from_configuration==item.singkat+'|basename'):
      value_for_sodara = item.variables[item.singkat]
      nilai_proses = basename(value_for_sodara)
      sodara.variables[sodara.singkat] = nilai_proses
      if hasattr(root_tree, 'variables'):
        root_tree.variables[sodara.singkat] = nilai_proses
      else:
        root_tree.variables= {sodara.singkat: nilai_proses}
      # sodara:
      # old_panjang_sebelum_replace_from_configuration='MYVAR|basename'
      # singkat='ANOTHERVAR',
      # panjang='__OPENFILE__|basename'
      # singkat_panjang={'ANOTHERVAR': 'MYVAR|basename'}
      # variables={'ANOTHERVAR': '__OPENFILE__|basename'}
      if is_debugging:
        print(f"[condition_to_process_sodara] process [{sodara.original}] gaya #2b => {sodara}")
      return True
  if is_debugging:
    print(f"  [condition_to_process_sodara] NO process [{sodara.original}] gaya #99")
  return False


def simpan_temp_vars(root_tree, item, is_debugging, self_run_configuration):
  """
  processor setiap kali menemukan
  save_variables
  dari grammar: | "%" save_variables
  maka akan simpan:
  'variables'			: {singkat:panjang},
  di item.

  6 june 2022
  kita bedakan minta input dan ambil dari yg sudah ada

  ini ngambil input:
    variables={'__TEMPLATE_DJANGOAPP': '__INPUT__'}
    old_panjang_sebelum_replace_from_configuration='__INPUT__'
    singkat_panjang={'__TEMPLATE_DJANGOAPP': '__INPUT__'}
    root:
      variables={'__TEMPLATE_DJANGOPROJECT': 'coba'} <- __TEMPLATE_DJANGOAPP tidak ada
  ini harusnya ambil dari yg sudah ada:
    variables={'__TEMPLATE_MODELCAP__': '__INPUT__'}    
    old_panjang_sebelum_replace_from_configuration='__TEMPLATE_DJANGOAPP'
    singkat_panjang={'__TEMPLATE_MODELCAP__': '__TEMPLATE_DJANGOAPP'}
    text_operations=['text_capitalize']
    root:
      variables={'__TEMPLATE_DJANGOPROJECT': 'coba', '__TEMPLATE_DJANGOAPP': 'film'}
  """

  # is_debugging = 2 # paksa sementara
  is_debugging = env_int('ULIBPY_FMUS_DEBUG') > 1
  if is_debugging:
    indah4(f"""[simpan_temp_vars] [START] for [{item.original}]
      item.variables = {item.variables}
      item = {item}
      root_tree = {root_tree}
      is_debugging = {is_debugging}
      """, warna='blue', layar='white')

  # newdict_for_modelify = {}

  # kita bikin item.variables bisa terima input dari user
  for kunci_variable,nilai_variable in item.variables.items():

    if (nilai_variable in [input_keyword, '__INPUTGUI__', '__OPENFILE__']
       or nilai_variable.startswith('__INPUT||')):
      original_varname = kunci_variable
      done = False

      while not done:

        masukan = None

        if nilai_variable == '__INPUTGUI__':
          masukan = get_input_from_user_gui(kunci_variable, pengirim='simpan_temp_vars')
          # dari gui perlukah jadikan __INPUT__ biasa dulu?
          # indah4(f'''[simpan_temp_vars] __INPUTGUI__
          # lanjut peroleh masukan = {masukan}
          # ''', warna='blue')
          item.variables[kunci_variable] = input_keyword

        elif nilai_variable == '__OPENFILE__':
          from schnell.app.promptutils import tkopenfile
          masukan = tkopenfile(initial_directory=item.workdir)
          # ini sebetulnya gak perlu nanti direplace oleh masukan
          item.variables[kunci_variable] = input_keyword

        elif nilai_variable == '__SAVEFILE__':
          from schnell.app.promptutils import tksavefile
          masukan = tksavefile(initial_directory=item.workdir)
          # ini sebetulnya gak perlu nanti direplace oleh masukan
          item.variables[kunci_variable] = input_keyword

        elif nilai_variable.startswith('__INPUT||'):
          default_value_for_input = nilai_variable.removeprefix('__INPUT||')
          item.variables[kunci_variable] = input_keyword # biar @, $ dll memproses
          masukan = get_input_from_user_or(
            kunci_variable, default_value_for_input, pengirim='simpan_temp_vars')

        else:
          '''
          cek dulu apakah __INPUT__ bisa diambil dari variable terdeclared/simpan sebelumnya,
          jk ya, nilainya ambil dari situ dan item.variables[kunci_variable] = masukan
          '''
          aslinya = item.old_panjang_sebelum_replace_from_configuration
          if (nilai_variable == input_keyword
              and aslinya != input_keyword and (aslinya in root_tree.variables)):
            masukan = root_tree.variables[aslinya]
            item.variables[kunci_variable] = masukan
          else:
            masukan = get_input_from_user(kunci_variable, pengirim='simpan_temp_vars')

        if masukan:  # proses nilai __INPUT__* yang barusan dimasukkan oleh user

          # masukan ini bisa absolute path
          # jk dia absolute path maka sibling bisa saja berada dlm direktori variable __INPUT__ tsb
          # jk demikian, sibling jangan string-replace workdirnya, tapi total replace
          apakah_dir_absolute = isabsolute(masukan)

          item.variables[kunci_variable] = masukan

          # percobaan, masukkan replacer
          # self_run_configuration['replacer'][kunci_variable] = masukan
          if not 'new_replacer_input' in self_run_configuration:
            self_run_configuration['new_replacer_input'] = {}
          self_run_configuration['new_replacer_input'][kunci_variable] = masukan

          # proses root
          if not hasattr(root_tree, 'input_keys'):
            root_tree.input_keys = [kunci_variable]
          else:
            root_tree.input_keys .append(kunci_variable)
          # item.input_key = kunci_variable # utk menjejak key utk gampang peroleh "masukan"
          # root_tree.input_key = kunci_variable # utk menjejak key utk gampang peroleh "masukan"
          root_tree.input_keys_index = len(root_tree.input_keys) - 1
          done = True

          # proses anak
          for anak_langsung in get_direct_children(item):
            # cek %anak
            if hasattr(anak_langsung, 'variables'):
              for k,v in anak_langsung.variables.items():
                if v == input_keyword:
                  if is_debugging:
                    indah4(f'replacing {k} with {masukan}', warna='magenta')
                  anak_langsung.variables[k] = masukan

          # proses sibling
          for sodara in get_siblings_after(item):

            if is_debugging:
              indah4(f'''[simpan_temp_vars] #2 check sibling for item [{item.original}]
              sibling [{sodara}]
              ''', warna='white')

            if condition_to_process_sodara(sodara, item, root_tree, is_debugging):
              '''
              misal bentuk:
              %MYVAR=__OPENFILE__
                item.singkat=MYVAR
                item.panjang=__OPENFILE__
                item.variables={MYVAR:masukan}
              @file yang diperoleh adalah: MYVAR...*
              '''

              # replace content sodara
              if hasattr(sodara, 'content'):
                if is_debugging:
                  print(f"""\t[simpan_temp_vars] #3 replacing [{item.panjang}] with [{masukan}]
                    in [{sodara.content}]""")
                sodara.content = sodara.content.replace(item.panjang, masukan)


              if is_debugging:
                indah4(f"""[simpan_temp_vars] #4 proses item => sodara [{sodara.original}]
                item = {item}
                sodara = {sodara}
                """, warna='green', layar='blue')

              # # replace workdir sodara
              # if apakah_dir_absolute:
              #   # indah4(f"""ganti sodara.workdir dengan masukan #1\n{sodara.workdir} <= {masukan}""", warna='black', layar='yellow')
              #   sodara.workdir = masukan
              # else:  # item.panjang adlh __INPUT__, masukan adlh replacer dari user
              #   sodara.workdir = sodara.workdir.replace(item.panjang, masukan)

              # oprek sodara
              if apakah_dir_absolute and input_keyword in sodara.workdir:
                sodara.original_workdir=sodara.workdir
                if sodara.workdir != input_keyword:
                  if not sodara.workdir.startswith(input_keyword):  # berarti __INPUT__ di tengah atau akhir
                    dihapus, dikeep = sodara.workdir.split(input_keyword, 1)
                    sodara.workdir = os.path.join(masukan, dikeep)
                  else:  # jk __INPUT__ di awal dan absolute, tinggal replace
                    sodara.workdir = sodara.workdir.replace(input_keyword, masukan, 1)
                else:
                  sodara.workdir = masukan
                indah4(f"[simpan_temp_vars] #4b original={sodara.original_workdir} menjadi={sodara.workdir}", warna='yellow', layar='blue')
              elif input_keyword in sodara.workdir:
                sodara.original_workdir=sodara.workdir
                sodara.workdir = sodara.workdir.replace(input_keyword, masukan, 1)

              # oprek sepupu (anak sodara)
              for sepupu in get_all_tree_children(sodara):

                if is_debugging:
                  indah4(f"""[simpan_temp_vars] #5 proses item => sodara => sepupu [{sepupu.original}]: START
                  item = {item}
                  sodara = {sodara}
                  sepupu = {sepupu}
                  """, warna='green', layar='blue')

                # sementara hanya proses(replace input dg masukan) utk node % yg punya .variables
                if hasattr(sepupu, 'variables') and len(sepupu.variables) > 0:
                  for k,v in sepupu.variables.items():
                    if v==input_keyword:
                      # harusnya cek dulu apakah k ada di sebelumnya, jangan k (__TEMPLATE_*) baru dikasih "masukan" yg sama
                      if k in item.variables:
                        nilai_untuk_anak_following_sibling = item.variables[k]
                        sepupu.variables[k] = nilai_untuk_anak_following_sibling
                        # sepupu.workdir = sepupu.workdir.replace(input_keyword, masukan)

                # if apakah_dir_absolute and input_keyword in sepupu.workdir:
                #   # indah4(f"""ganti sepupu.workdir dengan masukan #2\n{sepupu.workdir} <= {masukan}""", warna='black', layar='yellow')
                #   original_workdir=sepupu.workdir
                #   proses = '5a'
                #   if sepupu.workdir != input_keyword:
                #     if not sepupu.workdir.startswith(input_keyword):  # berarti __INPUT__ di tengah atau akhir
                #       dihapus, dikeep = sepupu.workdir.split(input_keyword, 1)
                #       sepupu.workdir = os.path.join(masukan, dikeep)
                #       proses = '5a'
                #     else:  # jk __INPUT__ di awal dan absolute, tinggal replace
                #       sepupu.workdir = sepupu.workdir.replace(input_keyword, masukan, 1)
                #       proses = '5b'
                #   else:
                #     sepupu.workdir = masukan
                #     proses = '5c'
                #   indah4(f"""[simpan_temp_vars] #{proses} masukan={masukan}
                #   sepupu/original={original_workdir} sepupu/menjadi={sepupu.workdir}
                #   sodara/asal={sodara.workdir}
                #   sodara={sodara}
                #   """, warna='yellow', layar='blue')
                # else:
                #   sepupu.workdir = sepupu.workdir.replace(input_keyword, masukan, 1)
                # stlh sodara punya original_workdir, skrg jd simple utk anak2nya
                if apakah_dir_absolute and input_keyword in sepupu.workdir and hasattr(sodara, 'original_workdir'):
                  sepupu.workdir = sepupu.workdir.replace(sodara.original_workdir, masukan, 1)

                if is_debugging:
                  indah4(f"""[simpan_temp_vars] #6 proses item => sodara => sepupu [{sepupu.original}]: END
                  item = {item}
                  sodara = {sodara}
                  sepupu = {sepupu}
                  """, warna='green', layar='blue')

            else:
              # cek di sini jika ada "variable" di item yg dipake di sodara.content/command
              ketemu = False
              if hasattr(sodara, 'command'):
                for kunci, nilai in item.variables.items():
                  if kunci in sodara.command:
                    sodara.command = sodara.command.replace(kunci, nilai)
                    ketemu = True
              elif hasattr(sodara, 'content'):
                for kunci, nilai in item.variables.items():
                  if kunci in sodara.content:
                    sodara.content = sodara.content.replace(kunci, nilai)
                    ketemu = True
              if not ketemu and is_debugging:
                indah4(f"""[simpan_temp_vars] #7 condition_to_process_sodara && NOT ketemu
            => not-if-condition mengenai: ubah __TEMPLATE_WHATEVER dari following-siblingnya %
            tidak diproses krn gak penuhi kriteria (hrs True semua)
              1. hasattr(sodara, 'old_name') = {hasattr(sodara, 'old_name')}
              2. and sodara.old_name == original_varname
              3. and original_varname [{original_varname}] in sodara.original [{sodara.original}] = {original_varname in sodara.original}
            pada sodara:
              {sodara}
            item:
              {item}
            item parent:
              {root_tree}
              """, warna='red')

    # %__TEMPLATE_VAR=nilai [@cap, @title, @lower, @upper, @plural]
    if hasattr(item, 'text_operations'):
      if is_debugging:
        indah4(f"""[simpan_temp_vars] #8
          text_operations = [{item.text_operations}]
          """, warna='yellow', layar='green')

      populate_modelify_ke_siblings = {}
      for oper in item.text_operations:
        if is_debugging:
          indah4(f"""[simpan_temp_vars] #9
          oper = {oper}
          item = {item}
          kunci_variable = {kunci_variable}
          item.variables[{kunci_variable}] = {item.variables[kunci_variable]}
          """, warna='yellow', layar='green')
        if oper == 'text_capitalize':
          item.variables[kunci_variable] = item.variables[kunci_variable].capitalize()
        elif oper == 'text_title':
          item.variables[kunci_variable] = item.variables[kunci_variable].title()
        elif oper == 'text_lower':
          item.variables[kunci_variable] = item.variables[kunci_variable].lower()
        elif oper == 'text_upper':
          item.variables[kunci_variable] = item.variables[kunci_variable].upper()
        elif oper == 'text_plural':
          item.variables[kunci_variable] = item.variables[kunci_variable] + 's'
        elif oper == 'dot_to_under':
          item.variables[kunci_variable] = item.variables[kunci_variable].replace('.', '_')
        elif oper == 'under_to_dot':
          item.variables[kunci_variable] = item.variables[kunci_variable].replace('_', '.')
        elif oper == 'dot_to_slash':
          item.variables[kunci_variable] = item.variables[kunci_variable].replace('.', '/')
        elif oper == 'slash_to_dot':
          item.variables[kunci_variable] = item.variables[kunci_variable].replace('/', '.')
        elif oper == 'dot_to_path':
          item.variables[kunci_variable] = item.variables[kunci_variable].replace('.', os.pathsep)
        elif oper == 'path_to_dot':
          item.variables[kunci_variable] = item.variables[kunci_variable].replace(os.pathsep, '.')
        elif oper == 'hyphen_to_underscore':
          item.variables[kunci_variable] = item.variables[kunci_variable].replace('-', '_')
        # | "@dot_to_under" -> dot_to_under
        # | "@under_to_dot" -> under_to_dot // a_b_c jadi a.b.c
        # | "@dot_to_path" -> dot_to_path
        # | "@path_to_dot" -> path_to_dot
        elif oper == 'modelify':
          if kunci_variable == item.variables[item.singkat]:
            pass
          elif kunci_variable == item.singkat + '_LOWER__':
            item.variables[kunci_variable] = item.variables[item.singkat].lower()
            populate_modelify_ke_siblings[item.variables[item.singkat]+ '_LOWER__'] = item.variables[kunci_variable]

          elif kunci_variable == item.singkat + '_UPPER__':
            item.variables[kunci_variable] = item.variables[item.singkat].upper()
            populate_modelify_ke_siblings[item.variables[item.singkat]+ '_UPPER__'] = item.variables[kunci_variable]

          elif kunci_variable == item.singkat + '_PLURAL__':
            item.variables[kunci_variable] = item.variables[item.singkat] + 's'
            populate_modelify_ke_siblings[item.variables[item.singkat]+ '_PLURAL__'] = item.variables[kunci_variable]

          elif kunci_variable == item.singkat + '_CASE__':
            item.variables[kunci_variable] = item.variables[item.singkat] + 's'
            populate_modelify_ke_siblings[item.variables[item.singkat]+ '_CASE__'] = item.variables[kunci_variable]

          elif kunci_variable == item.singkat + '_PLURAL_LOWER__':
            item.variables[kunci_variable] = item.variables[item.singkat].lower() + 's'
            populate_modelify_ke_siblings[item.variables[item.singkat]+ '_PLURAL_LOWER__'] = item.variables[kunci_variable]

          elif kunci_variable == item.singkat + '_PLURAL_UPPER__':
            item.variables[kunci_variable] = item.variables[item.singkat].upper() + 's'
            populate_modelify_ke_siblings[item.variables[item.singkat]+ '_PLURAL_UPPER__'] = item.variables[kunci_variable]

          elif kunci_variable == item.singkat + '_PLURAL_CAP__':
            item.variables[kunci_variable] = item.variables[item.singkat].capitalize() + 's'
            populate_modelify_ke_siblings[item.variables[item.singkat]+ '_PLURAL_CAP__'] = item.variables[kunci_variable]

          elif kunci_variable == item.singkat + '_CAP_PLURAL__':
            item.variables[kunci_variable] = item.variables[item.singkat].capitalize() + 's'
            populate_modelify_ke_siblings[item.variables[item.singkat]+ '_CAP_PLURAL__'] = item.variables[kunci_variable]

          elif kunci_variable == item.singkat + '_PLURAL_CASE__':
            item.variables[kunci_variable] = item.variables[item.singkat].capitalize()
            populate_modelify_ke_siblings[item.variables[item.singkat]+ '_PLURAL_CASE__'] = item.variables[kunci_variable]

          if is_debugging:
            indah4(f"""kunci_variable={kunci_variable}
          item.singkat={item.singkat}
          item.variables[item.singkat]={item.variables[item.singkat]}
          item.variables[kunci_variable]={item.variables[kunci_variable]}
          """, warna='magenta')

        # indah4(f"""[simpan_temp_vars] #9b
        #   oper = {oper}
        #   item = {item}
        #   item.variables = {item.variables}
        #   kunci_variable = {kunci_variable}
        #   item.variables[{kunci_variable}] = {item.variables[kunci_variable]}
        #   """, warna='yellow', layar='cyan')

      # stlh modify current item, sodara juga mungkin perlu
      # TODO: ini masih belum efektif krn banyak looping utk cek sodara+anak
      # seharusnya di awal ada register tiap var, ke root_tree, lalu node2 mana saja yg membutuhkan/meminta
      for sodara in get_siblings_after(item):
        # sodara bisa macam2: ada yg punya content, ada yg punya variables, dll
        # yg bikin susah, mereka ini berbeda tergantung jenis statementnya
        # indah4(f"""[simpan_temp_vars] #xxx stlh text_operations, coba apply ke sodara:
        #   sodara = {sodara}""", warna='yellow', layar='blue')
        if is_debugging:
          indah4(f"""[simpan_temp_vars] #9 stlh text_operations, coba apply ke sodara:
          sodara = {sodara}""", warna='yellow', layar='blue')
        if hasattr(sodara, 'content'):
          # # yang kita cari:
          # mungkin_sudah_ganti = item.variables[item.singkat]
          # yang_kita_cari = [
          #   # # aslinya masih spt ini
          #   # item.singkat + '_LOWER__',
          #   # item.singkat + '_UPPER__',
          #   # item.singkat + '_PLURAL__',
          #   # item.singkat + '_PLURAL_LOWER__',
          #   # item.singkat + '_PLURAL_UPPER__',
          #   # item.singkat + '_PLURAL_CAP__',
          #   # item.singkat + '_CAP_PLURAL__',
          #   # item.singkat + '_CASE__',
          #   # ada kemungkinan (most likely) sodara sudah modifikasi item.singkat ke item.variables[item.singkat]
          #   mungkin_sudah_ganti + '_LOWER__',
          #   mungkin_sudah_ganti + '_UPPER__',
          #   mungkin_sudah_ganti + '_PLURAL__',
          #   mungkin_sudah_ganti + '_PLURAL_LOWER__',
          #   mungkin_sudah_ganti + '_PLURAL_UPPER__',
          #   mungkin_sudah_ganti + '_PLURAL_CAP__',
          #   mungkin_sudah_ganti + '_CAP_PLURAL__',
          #   mungkin_sudah_ganti + '_CASE__',
          # ]
          for cari_katakunci, nilaiperubahan in populate_modelify_ke_siblings.items():
            sodara.content = sodara.content.replace(cari_katakunci, nilaiperubahan)


  if is_debugging:
    indah4(f"""[simpan_temp_vars] #10
    item = {item}
    """, warna='yellow', layar='blue')
  

  if hasattr(root_tree, 'variables'):
    # indah4(f"before: root_tree.variables: {root_tree.variables}", warna='yellow')
    # new %var bisa gunakan previous %var
    root_tree.variables .update(item.variables)
    # indah4(f"after: root_tree.variables: {root_tree.variables}", warna='green')
  else:
    root_tree.variables = item.variables

  if is_debugging:
    indah4(f"""[simpan_temp_vars] #11 [{item.original}] [END]
      item = {item}
      item.workdir = {item.workdir}
      item.variables = {item.variables}
      root_tree.variables = {root_tree.variables}
      """, warna='blue', layar='white')
