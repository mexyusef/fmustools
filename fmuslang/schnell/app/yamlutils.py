import yaml


# def read_yaml(filepath):
#     # Read YAML file
#     with open(filepath, 'r', encoding='utf8') as f:
#         yaml_data = yaml.safe_load(f)
#         # programming_data['yaml'] = yaml_data
#         return yaml_data

def convert_newlines(yaml_data):
    if isinstance(yaml_data, dict):
        return {key: convert_newlines(value) for key, value in yaml_data.items()}
    elif isinstance(yaml_data, list):
        return [convert_newlines(item) for item in yaml_data]
    elif isinstance(yaml_data, str):
        return yaml_data.replace(r'\n', '\n')
    else:
        return yaml_data

def read_yaml(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        yaml_data = yaml.safe_load(f)
        converted_data = convert_newlines(yaml_data)
        return converted_data
