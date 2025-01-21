from schnell.app.dirutils import (
	joiner,
	ayah,
	tempdir, 
	under_tempdir,
	timestamp,
)
from schnell.app.fileutils import (
	path_filename,
	get_filename,
	get_extension,
)
from schnell.app.printutils import (
	indah3,
)
from schnell.app.utils import (
	perintah, perintahsp_simple,
	PBPASTE,PBCOPY,LANGUAGES,
)


def create_newfilename(self, filename, basefolder):
	extension = 'java'  
	if get_extension(filename):
		filename_noext = get_filename(filename)
		extension = get_extension(filename)
	else:
		filename_noext = filename

	filename = filename_noext + '.' + extension # HelloWorld.java
	filepath = joiner(basefolder, filename)
	return filepath, filename_noext


def exejava(filepath=None):
	"""
	ingat:
	go run *.go
	???
	jk ada file selain main.go
	"""
	if filepath is None:
		filename = None
		filename_noext = None
		basefolder = tempdir()
		while not filename:
			filename = input("Masukkan nama file: ")
			if filename:
				filepath, filename_noext = create_newfilename(filename, basefolder)

		# command = f"{PBPASTE} > {filepath} && go run {filepath} && rm -f {filepath}"
		command = f"({PBPASTE} > {filepath} && javac {filepath} && cd {basefolder} && java {filename_noext})"
		
	else:
		basefolder = ayah(filepath, 1)
		filename = path_filename(filepath)
		filename_noext = get_filename(filepath)
		command = f"(javac {filepath} && cd {basefolder} && java {filename_noext})"

	
	indah3(f'exejava = {command}', warna='red')

	perintah(command)
	return 'OK'
