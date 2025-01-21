explorer

**fslang,d
  backend_statement.py,f(t=)
  frontend_statement.py,f(t=)

fullstack
  statement_config
  csv_statement
  frontend_statement
  backend_statement
--
kita coba:
bahasa django, fastapi, flask
bahasa dg bbrp flavor: gaya tulis dan java/kotlin
dropwizard
micronaut
quarkus
springboot
jakartaee

# Cara Kerja (biar gak lupa)

fullstack.py
statement: 
	| statement_config? csv_statement? backend_statement? frontend_statement?

  handler -> masuk ke csv_statement
    for item in anak(tree):
      jenis = data(item)
      if jenis == 'statement_config':
        res = statement_config(item) <-- ini yg beri program_config['be'] dst
      elif jenis == 'csv_statement':
        res = csv_statement(item)
        program_config.update(res) <-- program_config menentukan nama backed to call

  process_language
  myrepl

csv_statement.py
from app.transpiler.frontend.fslang.common import program_config
def get_konfigurasi_backend():
	hasil = None
	try:
		hasil = program_config["config"]["be"]
def csv_statement(tree):
  konfigurasi_backend = get_konfigurasi_backend()
  generator = generator_by_backend[konfigurasi_backend] (RootNode) # fullstack_generator
	generator.generate()
  frontend_config.update({
		# 'filepath': bc.mkfile_output_filepath,
		'filepath': generator.output(),
		'baris_entry': 'index/fmus',
	})
  return frontend_config
