from .bantu_django import (
  input_django_mkfile_template,
  output_django_mkfile,
)

from app.utils import env_get, env_exist
if not env_exist('ULIBPY_MK_FILEPATH_OUTPUT'):
  output_folder = '/mnt/c/tmp/working/output/'
else:
  output_folder = env_get('ULIBPY_MK_FILEPATH_OUTPUT')

ports = {
  'database': {
    'postgres': 7500,
    'mongo': 7501,
    'redis': 7502,
    'mariadb': 7503,
    'mysql': 7504,
    'mssql': 7505,
  },
  'backend': {
    'django': 8500,
    'flask': 8501,
    'fastapi': 8502,
    'node': 8503,
    'nodets': 8504,
    'springboot': 8505,
  },
  'frontend': {
    'react_antd': 9501,
    'react_bs': 9502,
    'react_mui': 9503,
    'next_antd': 9504,
    'next_bs': 9505,
    'next_mui': 9506,
  },  
}