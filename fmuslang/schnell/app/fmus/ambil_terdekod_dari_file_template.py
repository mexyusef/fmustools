import ast
from .common import Common
from schnell.app.mediautils import (
	baca_tulis_text
)
from schnell.app.printutils import (
  indah, 
  indah3,
  indah0,   
)
from schnell.app.utils import env_int


def ambil_terdekod_dari_file_template(oper, item, root_tree, self_debug, self_run_configuration):
  """
  icons.zip,f(b64=__FILE__=C:/work/zpt/ChatGPTWieke/icons.zip)
  | "b64" "=" singkat_folder "=" HURUF_FOLDER_LAMA 		-> ambil_terdekod_dari_file_template

  b64=file_template=cari_baris_berisi_data_terencode_base64
  sementara ini sama dg ambil_entry_dari_file_template

  singkat = maybe_operasi_value.children[0]  
  file_template = str(singkat)
  operasi_value = str({file_template:cari_baris})
  cari_baris = str(operasi.children[0].children[1])

  operasi_value = '' if not operasi_value else '='+operasi_value # ini jadi "=filepath:barisentry"
  operations.append(operasi_type + operasi_value)
  NewNode.operations = operations

  oper = "ambil_terdekod_dari_file_template=filepath:barisentry"
  for oper in item.operations:
    ambil_terdekod_dari_file_template(oper, item, root_tree, self.debug, self.run_configuration)
  """
  dict_file_baris = oper.split('=') [1]
  dict_file_baris = ast.literal_eval(dict_file_baris)

  for kunci, nilai in dict_file_baris.items():
    template_file = kunci
    if hasattr(root_tree, 'variables') and kunci in root_tree.variables:
      template_file = root_tree.variables[kunci]
      if env_int('ULIBPY_FMUS_DEBUG')>1:
        indah0('[ambil_terdekod_dari_file_template] <<kunci: ' + kunci + ', file: ' + template_file + ', baris: '+ nilai, newline=True)
    else:
      for k,v in self_run_configuration['replacer'].items():
        '''file template bisa berisi __CURDIR atau __FILE
        '''
        template_file = template_file.replace(k, v)

		# """
		# gagal hadapi:
		# kunci: utama, file: /home/usef/next-argon.mk, baris: /nextjs-argon-dashboard/assets/fonts/nucleo.woff
		# kunci: utama, file: /home/usef/next-argon.mk, baris: /nextjs-argon-dashboard/assets/fonts/nucleo.woff2
		# tulis image file /home/usef/tmp/_dahsyat/javascript/next-argon/assets/fonts/nucleo.woff2
		# """

    # TODO: add ocr support, jk filepath = kunci pada dict_file_baris = tempate_file = OCR
    # filecapture.jpg,f(b64=OCR=whatever)
    ocr_keyword = "OCR"
    if template_file == ocr_keyword:
      from schnell.app.ocrutils import ocr_screenshot
      # ocr_screenshot(output_file = None, DATADIR = env_get('ULIBPY_MEMO_DATADIR'), delay=1.0)
      ocr_screenshot(item.workdir)
      return

    entries = Common.list_grep(nilai, template_file)
    # cek jika ada bbrp entries hasil list_grep barisentry di filepath
    if entries:
      if len(entries) == 1:
        # TODO: add jk pengen dari hasil ocr...
        '''
        biasanya
        item.workdir,f(b64=filepath=barisentry)
        tambah bisa juga pake ocr
        item.workdir,f(b64=ocr=ocr)
        '''
        hasil = entries[0]
        isi = Common.definisi(hasil, template_file)
        baca_tulis_text(isi, item.workdir)
        if env_int('ULIBPY_FMUS_DEBUG')>1:
          indah0(f"[ambil_terdekod_dari_file_template] tulis image file {item.workdir}>>", warna='yellow', newline=True)
        # self_debug('\n'*2)
      else:
        '''
        sementara jk ada 2 entries hasil cari dlm 1 file
        kita bypass dulu utk b64 image, gak spt e=...
        UPDATE: benerin

        kunci: utama, file: /home/usef/next-argon.mk, baris: /nextjs-argon-dashboard/assets/plugins/nucleo/fonts/nucleo-icons.woff
        kunci: utama, file: /home/usef/next-argon.mk, baris: /nextjs-argon-dashboard/assets/plugins/nucleo/fonts/nucleo-icons.woff2
        tulis image file /home/usef/tmp/_dahsyat/javascript/next-argon//assets/plugins/nucleo/fonts/nucleo-icons.woff2
        '''
        # yg paling pendek filepath nya pasti yg diinginkan
        # namafile dan namafile2 matches, tentu yg dipengenkan adlh namafile
        hasil = min(entries, key=len)
        isi = Common.definisi(hasil, template_file)
        baca_tulis_text(isi, item.workdir)
        indah0(f"[ambil_terdekod_dari_file_template] tulis image file {item.workdir}>>", warna='yellow', newline=True)
        # self_debug('\n'*2)
