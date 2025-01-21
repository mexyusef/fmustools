import requests
from urllib.parse import urlparse
import shutil
import urllib.request
import tempfile


def get_content(url):
	"""utk text"""
	return requests.get(url).content.decode('utf8')


def save_image_stream(url, savefilepath):
	"""utk image"""
	response = requests.get(url, stream=True)
	with open(savefilepath, 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response
	return savefilepath


def save_image_shutil(url, savefilepath):
	print('save_image2, url:', url)
	with urllib.request.urlopen(url) as url_response:
		with open(savefilepath, 'wb') as out_file:
			shutil.copyfileobj(url_response, out_file)
	return savefilepath


def save_image(url, savefilepath):
	response = requests.get(url)
	if (response.content):
		with open(savefilepath, 'wb') as fd:
	  		fd.write(response.content)


def save_image_to_temp(urlpath):
	with urllib.request.urlopen(urlpath) as response:
		with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
			tmp_file.write(response.read())
			savefilepath = tmp_file.name
	return savefilepath


# https://stackoverflow.com/questions/44113335/extract-domain-from-url-in-python
# print(urlparse('http://abc.hostname.com/somethings/anything/'))
# >> ParseResult(
#     scheme='http',
#     netloc='abc.hostname.com',
#     path='/somethings/anything/',
#     params='',
#     query='',
#     fragment=''
# )
def parse_url(url):
	res = urlparse(url)
	return res.netloc, res.path, res.params, res.query, res.fragment, res.scheme


def first_path(url):
	_, path, _, _, _, _ = parse_url(url)
	if path.startswith('/'):
		return path[1:].split('/')[0]
	else:
		return path.split('/')[0]



def run_url(urlpath):
	"""
	buka url
	|			tampilkan firefox profiles
	url			buka di default browser
	prof|url	buka url di firefox profile
	
	"""
	from .systemutils import firefox_profiles, open_url_with_firefox
	from .printutils import print_list_warna
	from startup import buka as buka_internet

	firefox_profiles_list = firefox_profiles()
	if urlpath == '|':
		print_list_warna(firefox_profiles_list)
	elif '|' in urlpath:
		firefox_profile, url = [e.strip() for e in urlpath.split("|")]
		if firefox_profile == '*':  # *|url utk list profile
			content = '\n'.join(firefox_profiles_list)
			print(content)
		else:
			wanted = firefox_profile.lower()
			if wanted in firefox_profiles_list:
				open_url_with_firefox(url, wanted)
			else:
				found = [item for item in firefox_profiles_list if wanted in item]
				if found:
					wanted = found[0]
					open_url_with_firefox(url, wanted)
	else:
		buka_internet(urlpath)

