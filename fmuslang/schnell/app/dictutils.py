import json

"""
in my python program i have a deeply nested dict structure.
i want to get all keys in the dict and the path to each key in a form of tuple.
so i get a list of tuple (key, path-to-key)
mydict = {
    a: 1,
        
    d: {
        b: 2,
        c: 3,
        e: "ok",
        f: {
            name: "john"
        }
    }
}

so i get [('a', 'a'), ('d', 'd'), ('b', 'd/b'), ('c', 'd/c'), ('e', 'd/e'), ('f', 'd/f'), ('name', 'd/f/name')]
i want to have a function to get that list.

===============

You can achieve this by writing a recursive function that explores the nested dictionary and builds the path to each key as it traverses the structure. Here's a Python function that does exactly that:

```python
def get_key_paths(d, parent_path="", separator="/"):
    key_paths = []

    for key, value in d.items():
        path = f"{parent_path}{separator}{key}" if parent_path else key

        if isinstance(value, dict):
            key_paths.extend(get_key_paths(value, path, separator))
        else:
            key_paths.append((key, path))

    return key_paths

# Example usage:
mydict = {
    'a': 1,
    'd': {
        'b': 2,
        'c': 3,
        'e': "ok",
        'f': {
            'name': "john"
        }
    }
}

result = get_key_paths(mydict)
print(result)
```

Output:
```
[('a', 'a'), ('d', 'd'), ('b', 'd/b'), ('c', 'd/c'), ('e', 'd/e'), ('f', 'd/f'), ('name', 'd/f/name')]
```

The `get_key_paths` function takes the nested dictionary `d`, the `parent_path` which represents the path to the current dictionary, and the `separator` used to separate keys in the path (default is '/'). It recursively explores the dictionary and constructs the path for each key. When a nested dictionary is encountered, it calls itself with the updated `parent_path`. When a leaf key is reached (i.e., a non-dictionary value), it adds the key and its path to the result list.
"""


class DictToObject:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)


def get_key_paths(d, parent_path="", separator="/", stringified=True, indent=2):
    key_paths = []

    for key, value in d.items():
        path = f"{parent_path}{separator}{key}" if parent_path else key

        if isinstance(value, dict):
            key_paths.extend(get_key_paths(value, path, separator))
        else:
            key_paths.append((key, path))

    if stringified:
        return json.dumps(key_paths, indent=indent)
    return key_paths


def test_get_key_paths():
    mydict = {
        'a': 1,
        'd': {
            'b': 2,
            'c': 3,
            'e': "ok",
            'f': {
                'name': "john"
            }
        }
    }

    result = get_key_paths(mydict)
    print(result)


def search_nested_dict(data, target_key, delimiter='/', current_path='', fuzzy=False):
    """
    Search for keys in a deeply nested dictionary and print the full paths to the keys.

    Parameters:
    - data: The nested dictionary to search.
    - target_key: The key to search for.
    - delimiter: The character to use as a path separator (default is '/').
    - current_path: Internal parameter for recursion. Do not provide a value when calling the function.
    """
    # from .printutils import print_json
    # print_json(data)
    for key, value in data.items():
        print(f'target_key = {target_key}, key = {key}')
        result = None
        path = f"{current_path}{key}{delimiter}"
        if fuzzy and target_key in key:
            result = path[:-1]
        elif key == target_key:
            # print(path[:-1])  # Remove the trailing delimiter and print the full path
            result = path[:-1]
        if isinstance(value, dict):
            result = search_nested_dict(value, target_key, delimiter, path)
    return result


def test_search_nested_dict():
    nested_dict = {
        'root': {
            'a': {
                'b': {
                    'c': 1,
                    'd': 2
                },
                'e': {
                    'f': {
                        'g': 3
                    }
                }
            },
            'h': {
                'i': {
                    'j': 4
                }
            }
        }
    }

    search_nested_dict(nested_dict, 'g', delimiter='/')


def print_tree(dictionary, indent=0, space_amount=2):
    output = []
    for key, value in dictionary.items():
        # print(" " * (indent * 4) + f"|__ {key}")
        res = " " * (indent * space_amount) + f"|__ {key}"
        output.append(res)
        if isinstance(value, dict):
            res = print_tree(value, indent + 1)
            output.append(res)
    return '\n'.join(output)


def dict_paths(dictionary, indent=0, parent=''):
    output = []
    for key, value in dictionary.items():
        # print(" " * (indent * 4) + f"|__ {key}")
        # res = " " * (indent * space_amount) + f"|__ {key}"
        res = (f'{parent}/' if parent else '') + key
        output.append(res)
        if isinstance(value, dict):
            res = dict_paths(value, indent + 1, parent=parent+'/'+key)
            output.append(res)
    return '\n'.join(output)


def first_key(my_dict):
    key_list = list(my_dict.keys())
    return key_list[0]


def flatten_dict(input_dict, delimiter='/', parent_key=''):
    result = []
    for key, value in input_dict.items():
        new_key = f"{parent_key}{delimiter}{key}" if parent_key else key
        if isinstance(value, dict):
            result.extend(flatten_dict(value, delimiter, new_key))
        elif value is None:
            result.append(new_key)
    return result


def test_flatten_dict():
    """
    a/b/c/d
    a/e
    a/f/g/h
    i
    """
    input_dict = {
        'a': {
            'b': {
                'c': {
                    'd': None
                }
            },
            'e': None,
            'f': {
                'g': {
                    'h': None
                }
            }
        },
        'i': None
    }

    delimiter = '/'
    result = flatten_dict(input_dict, delimiter)

    for path in result:
        print(path)


def fuzzy_search_nested_dict(data, query, delimiter='/', current_path=''):
    """
    Fuzzy search for keys in a deeply nested dictionary and return the full paths to the keys.

    Parameters:
    - data: The nested dictionary to search.
    - query: The query string for fuzzy matching.
    - delimiter: The character to use as a path separator (default is '/').
    - current_path: Internal parameter for recursion. Do not provide a value when calling the function.

    Returns:
    - A list of full paths to keys that match the fuzzy query.
    """
    from fuzzywuzzy import fuzz
    
    matches = []
    for key, value in data.items():
        path = f"{current_path}{key}{delimiter}"
        similarity = fuzz.partial_ratio(query, key)
        if similarity >= 80:  # You can adjust the similarity threshold as needed
            matches.append(path[:-1])  # Remove the trailing delimiter and add the path to matches
        if isinstance(value, dict):
            matches.extend(fuzzy_search_nested_dict(value, query, delimiter, path))
    return matches


def test_fuzzy_search_nested_dict():
    nested_dict = {
        'root': {
            'mylongkey': 'value1',
            'mylonglongkey': 'value2',
            'mysuperlongkey': 'value3',
            'otherkey': 'value4',
        }
    }

    query = 'long'
    result = fuzzy_search_nested_dict(nested_dict, query, delimiter='/')
    print(result)


from prompt_toolkit.completion import Completer
def contains_search_nested_dict(dict_source, query, delimiter='/', current_path=''):
    """
    "Contains" search for keys in a deeply nested dictionary and return the full paths to the keys.

    Parameters:
    - dict_source: The nested dictionary to search.
    - query: The substring to search for in keys.
    - delimiter: The character to use as a path separator (default is '/').
    - current_path: Internal parameter for recursion. Do not provide a value when calling the function.

    Returns:
    - A list of full paths to keys that contain the query.
    """
    matches = []
    for key, value in dict_source.items():
        path = f"{current_path}{key}{delimiter}"
        if query in key:
            matches.append(path[:-1])  # Remove the trailing delimiter and add the path to matches
        if isinstance(value, Completer):
            # matches += [word for word in value.words if query in word]
            matches += [f"{path}{word}" for word in value.words if query in word]
        elif isinstance(value, dict):
            matches.extend(contains_search_nested_dict(value, query, delimiter, path))
    return matches


def test_contains_search_nested_dict():
    nested_dict = {
        'root': {
            'mylongkey': 'value1',
            'mylonglongkey': 'value2',
            'mysuperlongkey': 'value3',
            'otherkey': 'value4',
        }
    }

    query = 'long'
    result = contains_search_nested_dict(nested_dict, query, delimiter='/')
    print(result)


from .greputils import pattern_search_from_string_to_list
def get_nested_dict_keys(dict_source, delimiter='/', current_path=''):
    matches = []
    for key, value in dict_source.items():
        path = f"{current_path}{key}{delimiter}"
        matches.append(path[:-1])
        # matches.append(path)
        if isinstance(value, Completer):
            # matches += value.words  # word completer
            matches += [f"{path}{word}" for word in value.words]  # word completer
        elif isinstance(value, dict):
            matches.extend(get_nested_dict_keys(value, delimiter, path))
    return matches

def pattern_search_nested_dict(dict_source, query, delimiter='/', current_path=''):
    """
    "Contains" search for keys in a deeply nested dictionary and return the full paths to the keys.

    Parameters:
    - dict_source: The nested dictionary to search.
    - query: The substring to search for in keys.
    - delimiter: The character to use as a path separator (default is '/').
    - current_path: Internal parameter for recursion. Do not provide a value when calling the function.

    Returns:
    - A list of full paths to keys that contain the query.
    """
    # pattern_search_list_refactor(list_source, pattern_code, aslist=True)
    # pattern_search_from_string_to_list(list_source, pattern_code)
    # matches = []
    all_keys = get_nested_dict_keys(dict_source=dict_source, delimiter=delimiter, current_path=current_path)
    # pprint(all_keys)
    matches = pattern_search_from_string_to_list(all_keys, query)
    return matches
