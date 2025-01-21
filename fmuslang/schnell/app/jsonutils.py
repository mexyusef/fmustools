import json, decimal, datetime, enum, re
from anytree import Node, AnyNode
import ctypes
from socketserver import TCPServer



class TCPServerEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, TCPServer):
			# Extract relevant information from the TCPServer object
			server_info = {
				"address": obj.server_address,
				"request_handler": str(obj.RequestHandlerClass),
				# Add any other attributes you want to include in the JSON representation
			}
			return server_info
		return super().default(obj)

# # Example usage
# if __name__ == "__main__":
#     server = TCPServer(("localhost", 8000), SomeRequestHandler)
#     server_json = json.dumps(server, cls=TCPServerEncoder)
#     print(server_json)

# Custom handle type using ctypes
class HANDLE(ctypes.c_void_p):
	pass


# Custom JSON encoder for HANDLE objects
class HANDLEEncoder(json.JSONEncoder):
	def default(self, obj):

		if isinstance(obj, HANDLE):
			return {'HANDLE': ctypes.addressof(obj)}

		elif isinstance(obj, set):
			return list(obj)
		elif isinstance(obj, decimal.Decimal):
			# return str(o)
			return float(obj)
		elif isinstance(obj, (datetime.date, datetime.datetime)):
			return obj.isoformat()

		return super().default(obj)


class MyJsonify(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, set):
			return list(obj)
		elif isinstance(obj, decimal.Decimal):
			# return str(o)
			return float(obj)
		elif isinstance(obj, (datetime.date, datetime.datetime)):
			return obj.isoformat()
		# elif isinstance(obj, datetime.datetime):
		#     return obj.strftime("%Y-%m-%d %H:%M:%S")
		# elif isinstance(obj, datetime.date):
		#     return obj.strftime("%Y-%m-%d")
		# elif isinstance(obj, numpy.int64):
		#   return int(obj)
		# elif isinstance(obj, numpy.integer):
		#   return int(obj)
		# elif isinstance(obj, numpy.floating):
		#   return float(obj)
		# elif isinstance(obj, numpy.ndarray):
		#   return obj.tolist()
		elif isinstance(obj, enum.Enum):
			return obj.value
		elif isinstance(obj, AnyNode):
			return str(obj)
		# elif isinstance(obj, bson.objectid.ObjectId):
		#   return str(obj)
		elif isinstance(obj, TCPServer):
			# Extract relevant information from the TCPServer object
			server_info = {
				"address": obj.server_address,
				"request_handler": str(obj.RequestHandlerClass),
				# Add any other attributes you want to include in the JSON representation
			}
			return server_info
		# return super(MyJsonify, self).default(obj)
		return json.JSONEncoder.default(self, obj)


def json_from_string(content):
	return json.loads(content)


def json_stringify(content, indent=True):
	if indent:
		return json.dumps(content, indent=4)
	return json.dumps(content)


def json_loads(content):
	return json.loads(content)


def json_dumps(content, indent=4):
	return json.dumps(content, indent=indent)


def json_file_write(file_path, data, indent=4):
	"""
	Save a Python dictionary to a JSON file.

	Parameters:
	- data: The dictionary to be saved.
	- file_path: The file path where the JSON file will be saved.
	"""
	with open(file_path, 'w') as json_file:
		json.dump(data, json_file, indent=indent)


def json_file_content(json_filepath):
	try:
		with open(json_filepath) as fd:
			return json.load(fd)
	except Exception as err:
		print(f'[jsonutils] opening: {json_filepath}', err)
		return None


def json_file_print(json_filepath):
	json_body = json_file_content(json_filepath)
	print(json.dumps(json_body, indent=4))
	return json_body


def read_json(filepath):
	with open(filepath, 'r', encoding='utf8') as f:
		json_data = json.load(f)
		return json_data


import pyperclip
def beautify_json_from_clipboard():
    from .printutils import indah4
    json_data = pyperclip.paste()

    try:
        # # Parse JSON data
        # parsed_json = json.loads(json_data)
        # Step 1: Replace single quotes with double quotes
        json_data = json_data.replace("'", '"')

        # Step 2: Quote unquoted keys and values
        json_data = re.sub(r'(?<!")(\b\w+\b)(?=\s*:)', r'"\1"', json_data)  # Quote keys
        json_data = re.sub(r'(?<=:\s)(\b\w+\b)(?!")', r'"\1"', json_data)  # Quote values

        # Step 3: Parse JSON data
        parsed_json = json.loads(json_data)

        # Beautify JSON
        beautified_json = json.dumps(parsed_json, indent=4)

        # Print beautified JSON
        indah4(beautified_json, warna='yellow')

    except json.JSONDecodeError:
        print(f"Invalid JSON data in clipboard.\n{json_data}")

# # Example usage
# beautify_json_from_clipboard()
