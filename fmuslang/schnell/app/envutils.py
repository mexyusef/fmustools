from .utils import env_get, env_int, env_exist


def space_value():
	"""
	schnell/app/coordinator::BaseCoordinator
		def __init__(self,
			RootNode,
			project_dir='__INPUT__',
			provider='django',
			filename_input='index-input.mk',
			filename_output='output.fmus',
			disini=here(__file__),
			disini_output=here(__file__),
			baris_output_index='index/fmus',
			app_content_templatefile='',
			tab_mode='space4')
	default = 2
	"""
	nilai = 2
	from schnell.app.appconfig import programming_data
	nilai = programming_data['j']['schnell']['app']['configuration']['ULIBPY_SPACESIZE']
	# if env_exist('ULIBPY_SPACESIZE'):
	#     nilai = env_int('ULIBPY_SPACESIZE')
	if nilai == 2:
		return 'space2'
	elif nilai == 4:
		return 'space4'
	elif nilai == 8:
		return 'tab'
	return 'space2'


def get_space_value(nilai = 2):
	# if env_exist('ULIBPY_SPACESIZE'):
	# 	nilai = env_int('ULIBPY_SPACESIZE')
	from schnell.app.appconfig import programming_data
	nilai = programming_data['j']['schnell']['app']['configuration']['ULIBPY_SPACESIZE']
	return ' '*nilai
