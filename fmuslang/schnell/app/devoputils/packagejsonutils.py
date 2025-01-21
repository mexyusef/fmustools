# pip install --user jq
# https://www.cs.unm.edu/~jeffk/jq/jq-1.4.0-cp311-cp311-win_amd64.whl
from jq import jq
import json
import requests, subprocess, traceback
from schnell.app.printutils import indah4


def retrieve_and_print_json(url='https://jsonplaceholder.typicode.com/todos/1', jq_query=None):
    # Retrieve JSON response from the given URL
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse JSON content
        json_content = response.json()

        # Apply jq_query if provided
        if jq_query:
            try:
                json_content = jq(jq_query).transform(json_content)
            except Exception as e:
                print(f"Error applying jq_query: {e}")
                return

        # Print the JSON content
        # print(json_content)
        return json_content
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")

def test_retrieve_and_print_json():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    jq_query = ".title"
    retrieve_and_print_json(url, jq_query)


def prettify_section(package_json_path='package.json', jq_query='.scripts.start'):
    # print('oprek:', package_json_path)
    # Read the content of the package.json file
    with open(package_json_path, 'r') as f:
        package_json_data = json.load(f)

    try:
        # Define the jq query for the specified section
        query = jq(jq_query)
        # Transform the data using jq
        section_data = query.transform(package_json_data)
    except Exception as err:
        traceback.print_exception(err)

    # Check if the section exists
    if section_data:
        # print(f"found section_data: [{section_data}].")
        # Print the prettified section
        indah4(json.dumps(section_data, indent=2), warna='blue')
    else:
        print(f'Section "{jq_query}" not found in package.json')

def test_prettify_section():
    prettify_section('package.json', '.scripts.start')
    prettify_section('package.json', '.scripts.build')
    prettify_section('package.json', '.scripts.test')
    prettify_section('package.json', '.dependencies')
    # ... and so on


def update_script(package_json_path='package.json', script_name='start', new_value='new-command'):
    # Read the content of the package.json file
    with open(package_json_path, 'r') as f:
        package_json_data = json.load(f)

    # Define the jq query for the specified script
    jq_query = f'.scripts.{script_name} |= "{new_value}"'

    # Transform the data using jq
    updated_package_json = jq(jq_query).transform(package_json_data)

    # Write the updated data back to the package.json file
    with open(package_json_path, 'w') as f:
        json.dump(updated_package_json, f, indent=2)

def test_update_script():
    update_script('package.json', 'start', 'npm run dev')
    update_script('package.json', 'dev', 'new-dev-command')

def run_jq_on_windows(query, json_data, jq_exe='c:/work/bin/jq.exe'):
    # Convert the JSON data to a string
    json_string = json.dumps(json_data)

    # Run jq as a subprocess
    result = subprocess.run([jq_exe, query], input=json_string.encode('utf-8'), capture_output=True, text=True)

    # Check for errors
    if result.returncode != 0:
        print(f"Error running jq: {result.stderr}")
        return None

    # Parse the output as JSON and return it
    try:
        output_data = json.loads(result.stdout)
        return output_data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

def test_run_jq():
    json_data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    query = '.age'
    result = run_jq_on_windows(query, json_data)

    if result is not None:
        print(f"Result: {result}")
