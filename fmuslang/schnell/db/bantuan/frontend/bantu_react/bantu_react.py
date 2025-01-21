from app.dirutils import joiner
from app.fileutils import file_content, file_write
from app.utils import env_get
from creator.bindings import run_fmus
from db.bantuan.common import output_folder

category_mkfile_mapper = {
  'mts': joiner(env_get('ULIBPY_BASEDIR'), 'db/bantuan/frontend/bantu_react/mui-ts/mts.mk'),
  'mts2': joiner(env_get('ULIBPY_BASEDIR'), 'db/bantuan/frontend/bantu_react/mui-ts/mts2.mk'),
  'mts3': joiner(env_get('ULIBPY_BASEDIR'), 'db/bantuan/frontend/bantu_react/mui-ts/mts3.mk'),
  'bs': joiner(env_get('ULIBPY_BASEDIR'), 'db/bantuan/frontend/bantu_react/bs/bs2.mk'),
  'antd': joiner(env_get('ULIBPY_BASEDIR'), 'db/bantuan/frontend/bantu_react/antd/antd.mk'),
  'med': joiner(env_get('ULIBPY_BASEDIR'), 'db/bantuan/frontend/bantu_react/med/med.mk'),
  'rts': joiner(env_get('ULIBPY_BASEDIR'), 'db/bantuan/frontend/bantu_react/mui-ts/rts.mk'),
  'argon': joiner(env_get('ULIBPY_BASEDIR'), 'db/bantuan/frontend/bantu_react/next/argon.mk'),
  'muikit': joiner(env_get('ULIBPY_BASEDIR'), 'db/bantuan/frontend/bantu_react/next/muikit.mk'),
  'material': joiner(env_get('ULIBPY_BASEDIR'), 'db/bantuan/frontend/bantu_react/next/material.mk'),
  'backoffice': joiner(env_get('ULIBPY_BASEDIR'), 'db/bantuan/frontend/karya/sucor.mk'),
  'sucor': joiner(env_get('ULIBPY_BASEDIR'), 'db/bantuan/frontend/karya/sucor.mk'),
}

mts_group = list(category_mkfile_mapper.keys())

def process_mts(category, config, program, projectdir='input', mtsdir='react-mts-input', wpname='webpack-mts-01'):
  # default
  # projectdir = 'input'
  # mtsdir = 'react-mts-input'
  # wpname = 'webpack-mts-01'

  if config.count(',') == 2:
    _projectdir, _mtsdir, _wpname = config.split(',')
    if _projectdir:
      projectdir = _projectdir
    if _mtsdir:
      mtsdir = _mtsdir
    if _wpname:
      wpname = _wpname
  
  print(f"process_mts => projectdir {projectdir}, mtsdir {mtsdir}, wpname {wpname}")

  templatefile = category_mkfile_mapper.get(category, None)
  if not templatefile:
    print('not oprekking', category, '=>', category_mkfile_mapper.keys())
    return None

  templatecontent = file_content(templatefile)
  templatecontent = templatecontent.replace('__TEMPLATE_PROJECT_DIR__', projectdir)
  templatecontent = templatecontent.replace('__TEMPLATE_MTS_DIR__', mtsdir)
  templatecontent = templatecontent.replace('__TEMPLATE_WEBPACK_NAME__', wpname)
  templatecontent = templatecontent.replace('__TEMPLATE_ADDITIONAL_IMPORTS__', '')
  templatecontent = templatecontent.replace('__TEMPLATE_ADDITIONAL_PLUGINS__', '')

  filename = projectdir.replace('/', '_')
  mkfileout = joiner(output_folder, f'{filename}-output.mk')
  print(f"process_mts => mkfileout {mkfileout}")
  file_write(mkfileout, templatecontent + '\n')
  print('fmus >> start...')
  run_fmus(mkfileout)
  print('...fmus >> end')

  return f"OK, projectdir {projectdir}, mtsdir {mtsdir}, wpname {wpname}"

def bantu_react(category, config, program):
  """
  *!<category>|<config>|<program>
		config
			__TEMPLATE_PROJECT_DIR__ -> lokasi basedir atau input
			__TEMPLATE_MTS_DIR__ -> lokasi source react
			__TEMPLATE_WEBPACK_NAME__ -> nama webpack...dg default
  """
  result = f'OK: {config}'
  meta_result = 'OK'

  if category in mts_group:
    if category == 'bs':
      process_mts(category, config, program, mtsdir='react-bs-01', wpname='webpack-bs-01')
    elif category == 'antd':
      process_mts(category, config, program, mtsdir='react-antd-01', wpname='webpack-antd-01')
    else:
      process_mts(category, config, program)

  return result, meta_result
