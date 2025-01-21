import datetime, os, shutil, subprocess, sys

PROJECTNAME = 'datagenerator-' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
# PROJECTDIR = os.path.join(os.getcwd(), 'urepl', PROJECTNAME)
# PROJECTDIR = os.getcwd()
PROJECTDIR = os.path.join('/tmp', 'data-faker-lang')
ASSET_SRC = os.path.join(PROJECTDIR, 'assets_src')
ASSET_DST = os.path.join(PROJECTDIR, 'assets')

project_config = {
	'workpath': PROJECTDIR,
	# 'filename': '%s.html' % PROJECTNAME,
	'asset_src': ASSET_SRC,
	'asset_dst': ASSET_DST
}
SEQUELIZE = "C:\\Users\\mexus\\AppData\\Roaming\\npm\\sequelize.cmd"
SEQUELIZE_AUTO = "C:\\Users\\mexus\\AppData\\Roaming\\npm\\sequelize.cmd-auto.cmd"
SEQUELIZE_CLI = "C:\\Users\\mexus\\AppData\\Roaming\\npm\\sequelize.cmd-cli.cmd"


def create_config_json():
	from helper import config_json_template
	
	print(f"Writing to config.json file: {config_json_template}")
	# filepath = os.path.join(project_config['workpath'], 'config', 'config.json')
	# with open(filepath, 'w') as fd:
	# 	fd.write(config_json_template)


def create_projectdir():
	print('\ncreating projectdir...\n')
	# if not os.path.exists(project_config['workpath']):
	# 	os.makedirs(project_config['workpath'])


def create_seederfile(tablename, data_to_write):
	print(f'\nwriting seeders file for tablename {tablename}: [{data_to_write}]\n')
	# filepath = os.path.join(project_config['workpath'], 'seeders', seeder_filename(tablename))
	# with open(filepath, 'w') as fd:
	# 	fd.write(data_to_write)


def delete_seeders():
	print('\ndeleting seeders...\n')
	# seeder_folder = os.path.join(project_config['workpath'], 'seeders')
	# shutil.rmtree(seeder_folder)
	# os.makedirs(seeder_folder)


def exec_cmd_under_projectdir(cmd_args):
	create_projectdir() # jk belum kebuat
	# p = subprocess.Popen([command, argument1,...], cwd=project_config['workpath'])
	print('exec_cmd_under_projectdir:', cmd_args)
	# if sys.platform == 'win32':
	# 	p = subprocess.Popen(cmd_args, cwd=project_config['workpath'], shell=True)
	# else:
	# 	p = subprocess.Popen(cmd_args, cwd=project_config['workpath'])
	# p.wait()


def run_migration():
	exec_cmd_under_projectdir([SEQUELIZE, 'db:migrate'])


def run_seed():
	exec_cmd_under_projectdir([SEQUELIZE, 'db:seed:all'])


def seeder_filename(seeder_name):
	""" 
	jika mau timpa hasil seed:generate utk programmatically modify content dg insert data
	"""
	return "%s-%s.js" % (datetime.datetime.now().strftime('%Y%m%d%H%M%S'), seeder_name)


def sequelize_init():
	exec_cmd_under_projectdir([SEQUELIZE, 'init', '--force'])


def sequelize_generate_seed(seeder_name):
	exec_cmd_under_projectdir([SEQUELIZE, 'seed:generate', '--name', seeder_name])
