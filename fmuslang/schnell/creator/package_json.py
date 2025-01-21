import json
from schnell.app.dirutils import (
	dirs,
  files, 
	files_noext,
	sdirs, sfiles, 
	joiner, 
	here, 
	isdir, isfile,
	abs_dir,
	ayah,
)
from schnell.app.fileutils import (
	file_lines,
	line_contains,
	get_definition_by_key_permissive_start,
	get_definition_by_key_permissive_start_with_lineno,
	get_daftar,
	create_if_empty_file,
	replace_if_contain_links,
  json_from_string,
)
# from schnell.app.mediautils import (
# 	stringified_image_asb64,
# 	capture_gambar,
# 	lihat_gambar,
# 	capture_lihat_gambar,
# 	capture_lihat_stringified_image_asb64,
# 	get_lihat_stringified_image_asb64,
# 	requests_get_lihat_stringified_image_asb64,
# )
from schnell.app.printutils import print_list_warna
from schnell.app.utils import (
	# env_exist,
	# env_get, env_int,
	# perintah,
	# python_package,
	# trycopy,
  trypaste,
)


import requests


def get_npm_package_versions(package_name):
  url = f'https://registry.npmjs.org/{package_name}'
  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()
    if 'versions' in data:
      return list(data['versions'].keys())

  return []

def search_npm_packages(keyword='state manager', number=20):
  url = f'https://registry.npmjs.org/-/v1/search'
  # You can adjust the 'size' parameter to control the number of results.
  params = {'text': keyword, 'size': number}

  response = requests.get(url, params=params)

  if response.status_code == 200:
    data = response.json()
    if 'objects' in data:
      packages_info = data['objects']
      print_list_warna(list(packages_info.keys()))
      return [(package_info['package']['name'], package_info['package']['description']) \
        for package_info in packages_info]

  return []

# if __name__ == '__main__':
#   keyword = 'state manager'
#   packages = search_npm_packages(keyword)

#   if packages:
#     print(f"Packages related to '{keyword}':")
#     for package_name, package_description in packages:
#       print(f"Package Name: {package_name}")
#       print(f"Description: {package_description}\n")
#   else:
#     print(f"No packages found related to '{keyword}'.")


# if __name__ == '__main__':
#   package_name = 'react-dom'
#   versions = get_npm_package_versions(package_name)
#   print(f"Versions of {package_name}:")
#   for version in versions:
#     print(version)


def get_scripts(jsoncontent):
  if 'scripts' in jsoncontent:
    return jsoncontent['scripts']

  return None


def get_devdeps(jsoncontent):
  """
  kembalikan json 'devDependencies'
  """
  if 'devDependencies' in jsoncontent:
    return jsoncontent['devDependencies']

  return None


def get_deps(jsoncontent):
  """
  kembalikan json 'dependencies'
  """
  if 'dependencies' in jsoncontent:
    return jsoncontent['dependencies']

  return None


def keys(json_part):
  if json_part is None:
    return []
  return json_part.keys()


def vals(json_part):
  if json_part is None:
    return []
  return json_part.values()


def keyvals(json_part):
  return json_part.items()


def get_deps_keys(jsoncontent):
  json_part = get_deps(jsoncontent)
  # print('get_deps_keys+values:', json_part)
  return keys(json_part)


def get_devdeps_keys(jsoncontent):
  json_part = get_devdeps(jsoncontent)
  return keys(json_part)


def get_deps_kv(jsoncontent, versions=[]):
  """
  versions = ['port-jw', 'ass-trans']

  json_part = {'@nestjs/common': '^7.0.5',
 '@nestjs/websockets': '^7.0.5',
 'argon2': '^0.26.2',
 'class-transformer': '^0.2.3',
 'class-validator': '^0.11.1',
 'passport-jwt': '^4.0.0',
 'reflect-metadata': '^0.1.13',
 'typescript': '^3.8.3'}

  normalify = ['class-transformer', 'passport-jwt']
  withversions = ['class-transformer@^0.2.3', 'passport-jwt@^4.0.0']
  """
  json_part = get_deps(jsoncontent)
  key_list = get_deps_keys(jsoncontent)
  if len(versions)==0:
    return [f'{k}@{v}' for k,v in json_part.items()]
  else:
    '''
    versions tdk normal itemsnya, normalkan dg ambil dari 
    '''
    normalify = [k for k in key_list for l in versions if l.lower() in k.lower()]
    noversions = [k for k in key_list if k not in normalify]
    withversions = [k+'@'+v for (k,v) in json_part.items() if k in normalify]

    return withversions+noversions


def get_devdeps_kv(jsoncontent, versions=[]):
  json_part = get_devdeps(jsoncontent)
  if json_part is None:
    return None
  key_list = get_devdeps_keys(jsoncontent)
  if len(versions)==0:
    return [f'{k}@{v}' for k,v in json_part.items()]
  else:
    '''
    versions tdk normal itemsnya, normalkan dg ambil dari 
    '''
    normalify = [k for k in key_list for l in versions if l.lower() in k.lower()]
    noversions = [k for k in key_list if k not in normalify]
    withversions = [k+'@'+v for (k,v) in json_part.items() if k in normalify]

    return withversions+noversions

def process_packagejson_internal(content, manager='yarn', versions=None):
  """
  versions:
  None -> no versions
  [] -> all versions
  [one,two,three] -> filter
  """
  jsoncontent = json_from_string(content)
  # print('dari string clipboard menjadi:', jsoncontent)

  if versions is not None:
    deps_list = get_deps_kv(jsoncontent, versions)
    devdeps_list = get_devdeps_kv(jsoncontent, versions)
  else:
    deps_list = get_deps_keys(jsoncontent)
    # print('process_packagejson_internal => get_deps_keys:', deps_list)
    devdeps_list = get_devdeps_keys(jsoncontent)

  adder_devdeps = 'yarn add --dev'
  adder_deps = 'yarn add'
  if manager == 'npm':
    adder_deps = 'npm i -S'
    adder_devdeps = 'npm i -D'
  elif manager == 'pnpm':
    adder_deps = 'pnpm add'
    adder_devdeps = 'pnpm add --dev'

  adder1, adder2 = '', ''
  if deps_list:
    adder1 = f"{adder_deps} " + ' '.join(deps_list)
  if devdeps_list:
    adder2 = f"{adder_devdeps} " + ' '.join(devdeps_list)
  return f"\n{adder1}\n\n{adder2}"


def process_packagejson(manager='yarn', versions=None):
  content = trypaste()
  if content:
    print('terima:', content[:500], '...', 'dg versions:', versions)
    result = process_packagejson_internal(content, manager, versions)
    return result

  return None
