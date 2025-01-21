import json, os
from process_wrapper import process_language
from debug import Debug


class Configuration:
	default_configuration = {}
	CONFIG='config.json'

	def __init__(self):
		self.run_configuration = {}
		here = os.path.dirname(__file__) # os.getcwd()
		# print(__file__, os.path.dirname(__file__), os.path.basename(__file__))
		config_file = os.path.join(here, Configuration.CONFIG)
		with open(config_file) as json_file:
			Configuration.default_configuration = json.load(json_file)
	
		Configuration.default_configuration['default']['cwd'] = here
		self.read_config()


	def read_config(self):
		"""
		os.path.join(self.run_configuration['outputdir']
			/tmp
		self.run_configuration['output']
			target
		"""
		self.run_configuration = Configuration.default_configuration['default']
		self.run_configuration['templatesdir'] = os.path.join(self.run_configuration['cwd'], self.run_configuration['templates'])
		self.run_configuration['programsdir'] = os.path.join(self.run_configuration['cwd'], self.run_configuration['programs'])
		self.run_configuration['projectdir'] = os.path.join(self.run_configuration['outputdir'], self.run_configuration['project'])


config = Configuration()


def process_csv(debug = Debug(config.run_configuration['is_debug'])):
	debug('***    CSV')
	debug('=>     {sql,sequelize,alchemy}email,s')
	code = 1

	while code != '' and code != 'x':
		try:
			code = input('CSV>> ')
			code = code.strip()

			if code == 'bahasa':
				from .grammar import bahasa
				print(bahasa)

			if code .startswith('%%'): # %% utk mulai multiline, akhiri dg enter atau %
				code = code.strip('%%').strip()
				multiline = code

				while code != '%' and code != '':
					code = input('.. ')
					code = code.strip()
					if code != '' and code != '%':
						multiline += '\n'
						multiline += code

				if multiline:
					# print(f'process multiline: [{multiline}]')
					process_language(config.run_configuration, debug, multiline)

			elif code != '' and code != 'x':
				process_language(config.run_configuration, debug, code)

		except EOFError:
			break
		except Exception as err:
			print(err)

"""
{@mytable}username,v(100)
{@mytable}username,v(100),N
{@mytable}username,v(100),N,u
{@mytable}username,v(100),N,u,df=funkifyme
{@public/mytable}username,v(100),N,u,df=funkifyme
{@mytable}username,s;email,s;password,s;desc,t

schnell/langs/ucsv/ucsv

username,s;email,s;password,s;desc,t
harusnya bisa:
class User(models.Model):
	id          = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4)
	username    = models.CharField(max_length=64, blank=True, null=True, verbose_name=_('nama pengguna'))
	email       = models.EmailField(max_length=200, unique=True, verbose_name=_('alamat email'))
	password    = models.CharField(max_length=256, blank=False, null=False, verbose_name=_('kata kunci'))
	created_at  = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=_('waktu buat'))
	updated_at  = models.DateTimeField(auto_now=True, blank=True, verbose_name=_('waktu update'))
"""

if __name__ == '__main__':
	process_csv(Debug())
