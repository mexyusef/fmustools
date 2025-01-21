--% getting started
semuanya dimulai dimana app/ atau creator/?
sptnya app/grammar.py
dimana kita mengawali kehidupan dg /quick-code, *special-code, namafile,f, namadir,d, %tempdir, dst.
--#

--% app/grammar.py

```
keseluruhan: insn+

insn: filename "," filetype fileoperation?
	| "$" system_operation_type
	| "/" quick_command
	| "/" -> empty_quick_command
	| "*" special_command
	| "@" "(" pesan_instruksi_dari_template ")"
	| "@" pesan_instruksi
	| "~" branch_instruksi
	| "?" pickone_instruksi
	| "%" save_variables
	| request_operation_from_user
	| "#" comment
	| "#" "(" komentar_dari_template ")"
	| "x=" pexpect_operation

fileoperation: "(" file_dir_operation_type ("," file_dir_operation_type)* ")"

file_dir_operation_type: file_operation_type	//
	| "/" dir_operation_type 					// agar fileop dan dirop bs share cmd, maka dirop prefix dg /
	| "@" operation_attributes

file_operation_type: "f" "=" HURUF_FOLDER 	-> load_from_file // dari templates -> mending dari item.workdir
	| "F" "=" HURUF_FOLDER 					-> load_from_file_absolute // dari abs dir
	| "D" "=" HURUF_FOLDER_LAMA_BERBINTANG	-> load_from_dir_with_filter
	| "i" "="												-> input_from_user_with_prompt
	| "c" "=" 												-> paste_from_clipboard_with_pause
	| "t"	"="												-> touch_file
	| "n"	"="	ISI_CONTENT_FILE_BISA_URL		-> content_file
	| "e" "=" singkat_folder "=" HURUF_FOLDER_NEXTJS 		-> ambil_entry_dari_file_template
	| "cg" langchoice? "=" singkat_folder "=" HURUF_FOLDER_NEXTJS -> ambil_entry_codegen
	| "code" langchoice "=" ISI_FILE_TERMASUK_KOMA_TAMBAH_PERSEN -> ambil_replify_here
	| "b64" "=" singkat_folder "=" HURUF_FOLDER_LAMA 		-> ambil_terdekod_dari_file_template
	| "img" "=" HURUF_FOLDER_LAMA 							-> generate_image
	| "h" "=" ALAMAT 										-> url_file

operation_attributes: operation_attr // ("," operation_attr)*

operation_attr: "b"									-> binary_file_operation 		// @b
	| "x" "[" pattern ("," pattern)* "]"			-> excluding_in_copy
	| "a" 	-> appending_mode // (e=template=main.scala/baris1,@a) biar bisa */baris2 dst
	| "ts" 	-> tab_to_space
	| "ib" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> insert_before
	| "ia" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> insert_after
	| "iA" "=" singkat "=" BILBUL_BERTANDA -> insert_at // f=capcay.txt,iA=barisentry=-1
	| "ra" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> replace_at
	| "rf" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> replace_from
	| "rm" "=" jumlah_hapus "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> remove_lines
	| "re" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> replace_entry
	| "rb" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> replace_between
	| "rs" "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> replace_string
	| "rc" "=" singkat -> replace_content // whole file replace
	// yg pertama: komentar symbol spt # atau //, yg kedua baris yg mau dicomment
	| "cf" "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> commenting_file

```
--#

--% app/fmus/fmus.py
--#

--% app/fmus/processor.py
--#

--% app/fmus/generator.py
--#

--% "$" system_operation_type
| "$" system_operation_type
--#

--% "/" quick_command
| "/" quick_command
--#

--% "/" -> empty_quick_command
| "/" -> empty_quick_command
--#

--% "*" special_command
| "*" special_command

app/fmus/special_command.py
```SpecialCommand(salin).run()```
app/specialcmd.py
```
def run(self):
if self.command == 'android':
elif self.command == 'append':
elif self.command .startswith ('showtext') or self.command .startswith ('showfile'):
elif self.command .startswith ('ujian'):
elif self.command .startswith ('server'):
elif self.command.startswith('wnd_create'):
elif self.command.startswith('wnd_left'):
elif self.command.startswith('wnd_right'):
elif self.command.startswith('wnd_sbs'):
elif self.command.startswith('wnd_vert'):
elif self.command.startswith('wnd_focus'):
elif self.command.startswith('wnd_title'):
elif self.command.startswith('wait'):
elif self.command.startswith('elapsed'):
elif self.command.startswith('pause'):
elif self.command.startswith('wsltype'):
elif self.command.startswith('wsl_ngetik'):
elif self.command.startswith('wnd_ngetik'):
elif self.command.startswith('picsum'):
elif self.command.startswith('unsplash'):
elif self.command.startswith('favico'):
elif self.command.startswith('favgen'):
elif self.command.startswith('favmake'):
elif self.command.startswith('notif'):
elif self.command.startswith('sccap'):
elif self.command.startswith('screc'):
elif self.command.startswith('W='):
elif self.command.startswith('*'):
elif self.command.startswith('@'):
elif self.command.startswith('/'):
elif self.command.startswith('l '):
elif self.command.startswith('>'):
	request = self.command.removeprefix('>')
	from .special import genfile
	genfile(request)

	json
	json2
	csv
	sql

	removeprefix: **>
	**>json,namafile|kode
		u -e'**>json,namafile|{@User=#5}username,s'
		u -e "**>json,namafile\|{@User=#5}username,s"
	**>json2,namafile|kode
	**>csv,namafile|kode
	**>sql,namafile|kode
	ingat: csv_statement				: "C^" program_csv "^"

	u -e'**>json,namafile|{@User=#15}username,s;password,s'
	u -e'**>json2,namafile|{@User=#15}username,s;password,s'
	u -e'**>csv,namafile|{@User=#15}username,s;password,s'
	u -e'**>sql,namafile|{@User=#15}username,s;password,s'

	bisa juga generate docker-compose utk pg dan mg
	u -e '**>dc,pg' docker compose utk pg
	u -e '**>dc,mg' docker compose utk mongo
	u -e '**>dc,ma' docker compose utk mariadb
	u -e '**>dc,my' docker compose utk mysql
	u -e '**>dc,ms' docker compose utk mssql

	u -e '**>env|jwt,mongo,postgre,prisma'
	u -e '**>us|config,pgadm' -> sesuai nama configstore, pgadmin (cukup subset nama)

	u -e"**>credentials.json"
elif self.command.startswith('%'):
elif self.command.startswith('term'):
elif self.command.startswith('VF'):
elif self.command.startswith('lalang'):
elif self.command.startswith('decl'):
elif self.command.startswith('css'):
elif self.command.startswith('be'):
elif self.command.startswith('flu'):
elif self.command.startswith('E'):
	u -e**Edbg=0/1
	from .special.envplay import envplay
	envplay(self.command.removeprefix('E'))
```

--#

--% "@" "(" pesan_instruksi_dari_template ")"
| "@" "(" pesan_instruksi_dari_template ")"
--#

--% "@" pesan_instruksi
| "@" pesan_instruksi
--#

--% "~" branch_instruksi
| "~" branch_instruksi
--#

--% "?" pickone_instruksi
| "?" pickone_instruksi
--#

--% "%" save_variables
| "%" save_variables
--#

--% request_operation_from_user
| request_operation_from_user
--#

--% "#" comment
| "#" comment
--#

--% "#" "(" komentar_dari_template ")"
| "#" "(" komentar_dari_template ")"
--#

--% "x=" pexpect_operation
| "x=" pexpect_operation
--#

