import json, os, subprocess
import imghdr
from schnell.app.fileutils import fmusfile_entry
from schnell.app.threadutils import mulai
from prompt_toolkit.completion import Completer, Completion


class DictToObject:
	def __init__(self, dictionary):
		for key, value in dictionary.items():
			setattr(self, key, value)


class LoggedDict(dict):
	def __init__(self, original_dict, *args, **kwargs):
		# print("Initializing LoggedDict")
		super().__init__(original_dict, *args, **kwargs)

	def keys(self):
		# Override keys() to return processed keys
		return [key for key in super().keys()]

	def items(self):
		# Override items() to return processed key-value pairs
		return [(key, self[key]) for key in super().keys()]

	def __getitem__(self, key):

		if key in self:
			filepath = super().__getitem__(key).get('filepath', '')
			barisentry = super().__getitem__(key).get('barisentry', '')
			processed_value = f"{filepath}|{barisentry}"
			# Return a regular dictionary
			return {'filepath': filepath, 'barisentry': barisentry, 'processed_value': processed_value}

		return {'filepath': '', 'barisentry': '', 'processed_value': 'Not Found'}


class LoggedCompleter(Completer):
	def __init__(self, logged_dict, max_metadict_content=200):
		self.logged_dict = logged_dict
		self.selected_entry = None
		self.max_metadict_content = max_metadict_content

	def get_completions(self, document, complete_event):
		# Implement your completion logic here.
		# Use self.logged_dict to access __getitem__.

		# Example: return keys as completions
		for key in self.logged_dict:
			display_meta_text = 'meta for ' + key
			value_content = self.logged_dict.get(key, None)
			if value_content:
				filepath = value_content.get('filepath')
				barisentry = value_content.get('barisentry')
				# 24/12/2023
				# ini bisa bahaya jk content sangat panjang
				# menu akan jadi sangat lambat
				# display_meta_text = fmusfile_entry(filepath, barisentry)
				# display_meta_text = fmusfile_entry(filepath, barisentry)[:self.max_metadict_content]
				display_meta_text = f"{filepath[-20:]}|{barisentry}"

				# publish_to_redis_channel(display_meta_text, redis_channel='percobaan')
				# display_meta_text = to_formatted_text(display_meta_text)

			yield Completion(key, start_position=-document.cursor_position, display_meta=display_meta_text)
			# # jika user ngetik sampai ketemu key
			# # harusnya if document.text_before_cursor.startswith(key)
			# if key == document.text_before_cursor:
			# 	self.selected_entry = key
			# 	print(f"Selected: {self.selected_entry}")


def logged_dict_to_content(logged_dict, kunci):
	content = None
	nilai = logged_dict.get(kunci, None)
	if nilai:
		filepath = nilai.get('filepath')
		barisentry = nilai.get('barisentry')
		# print(f"kita oprek: {filepath}={barisentry}")
		content = fmusfile_entry(filepath, barisentry)
	return content


def read_json(filepath):
	try:
		with open(filepath, 'r', encoding='utf8') as f:
			json_data = json.load(f)
		return json_data
	except Exception as exc:
		# print(f"{filepath} => {str(exc)}.")  # kadang terlalu rame
		return None


def run_vscode(argumen):
	from configuration_values import config_app
	subprocess.Popen([
		# "C:\\Users\\usef\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
		config_app["vscode"],
		argumen
	])


def run_code_writer():
	app_directory = r"C:\Program Files\WindowsApps\ActiproSoftwareLLC.562882FEEB491_4.2.42.0_x64__24pqs290vpjk0"
	executable_path = fr"{app_directory}\codewriter.exe"
	subprocess.run([executable_path])


def is_image_file(filepath):
	"""
	Check if a file is an image file based on its extension and content.

	Args:
	- filepath (str): The path to the file.

	Returns:
	- bool: True if the file is determined to be an image file, False otherwise.
	"""
	# Check if the file exists
	if not os.path.exists(filepath):
		return False

	# Check if the file has a valid image extension
	valid_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
	_, file_extension = os.path.splitext(filepath)
	if file_extension.lower() not in valid_extensions:
		return False

	# Check if the file has a valid image header (content)
	with open(filepath, 'rb') as f:
		header = f.read(32)  # Read the first 32 bytes to identify the file type
		image_type = imghdr.what(None, header)

	return image_type is not None


def test_is_image_file():
	file_path = "path/to/your/image.jpg"
	if is_image_file(file_path):
		print(f"{file_path} is an image file.")
	else:
		print(f"{file_path} is not an image file.")


def jalankan_prompt(event, text):
	event.app.current_buffer.insert_text(text)
	event.app.current_buffer.validate_and_handle()


def terima_prompt(event):
	event.app.current_buffer.text = ""
	event.app.current_buffer.validate_and_handle()  # jk empty bs terima input
