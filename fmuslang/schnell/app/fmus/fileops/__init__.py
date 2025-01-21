import re


def replace_left_of_query(query, filepath, replacer, encoding='utf-8'):
    try:
        # Read the file and store its content
        with open(filepath, 'r', encoding=encoding) as file:
            lines = file.readlines()

        # Find the line containing the query string
        for i, line in enumerate(lines):
            if query in line:
                # Replace anything on the left of the query string with the new replacer
                lines[i] = line.replace(line.split(query)[0], replacer)
                break  # Stop searching after the first occurrence

        # Write the modified content back to the file
        with open(filepath, 'w', encoding=encoding) as file:
            file.writelines(lines)

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# # Example usage:
# replace_left_of_query("query_string", "example.txt", "new_replacer")
def replace_right_of_query(query, filepath, replacer, encoding='utf-8'):
    try:
        # Read the file and store its content
        with open(filepath, 'r', encoding=encoding) as file:
            lines = file.readlines()

        # Find the line containing the query string
        for i, line in enumerate(lines):
            if query in line:
                # Replace anything to the right of the query string with the new replacer
                lines[i] = line.replace(line.split(query)[1], replacer, 1)
                break  # Stop searching after the first occurrence

        # Write the modified content back to the file
        with open(filepath, 'w', encoding=encoding) as file:
            file.writelines(lines)

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# # Example usage:
# replace_right_of_query("query_string", "example.txt", "new_replacer")

def replace_query(query, filepath, replacer, encoding='utf-8'):
    try:
        # Read the file and store its content
        with open(filepath, 'r', encoding=encoding) as file:
            lines = file.readlines()

        # Find the line containing the query string
        for i, line in enumerate(lines):
            if query in line:
                # Replace the query string with the new replacer
                lines[i] = line.replace(query, replacer)
                break  # Stop searching after the first occurrence

        # Write the modified content back to the file
        with open(filepath, 'w', encoding=encoding) as file:
            file.writelines(lines)

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# # Example usage:
# replace_query("query_string", "example.txt", "new_replacer")
def insert_at_lines(filepath, string_to_insert, lines_to_insert_at, encoding='utf-8', line_index_start=0):
    try:
        # Read the file and store its content
        with open(filepath, 'r', encoding=encoding) as file:
            lines = file.readlines()

        # Insert the string at specified lines
        for line_number in lines_to_insert_at:
            # Ensure the line number is within the valid range
            if line_index_start <= line_number < len(lines)+line_index_start:
                # kurangi dg index start
                # jk string_to_insert berisi bbrp \n, jadi double line
                lines.insert(line_number-line_index_start, string_to_insert)

        # print('lines:\n', lines)
        # Write the modified content back to the file
        with open(filepath, 'w', encoding=encoding) as file:
            file.writelines(lines)

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# # Example usage:
# insert_at_lines("example.txt", "inserted_string\n", [2, 5, 8])
def insert_after_query(query, filepath, string_to_insert, encoding='utf-8'):
    try:
        # Read the file and store its content
        with open(filepath, 'r', encoding=encoding) as file:
            lines = file.readlines()

        # Find the line containing the query string
        for i, line in enumerate(lines):
            if query in line:
                # Insert the string after the line containing the query
                lines.insert(i + 1, string_to_insert)
                break  # Stop searching after the first occurrence
        else:
            print(f"No line matching the query: {query}. Skipping.")

        # Write the modified content back to the file
        with open(filepath, 'w', encoding=encoding) as file:
            file.writelines(lines)

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# # Example usage:
# insert_after_query("query_string", "example.txt", "inserted_string\n")

def insert_after_regex(regex_pattern, filepath, string_to_insert, encoding='utf-8'):
    try:
        # Read the file and store its content
        with open(filepath, 'r', encoding=encoding) as file:
            lines = file.readlines()

        # Find the line matching the regex pattern
        for i, line in enumerate(lines):
            if re.search(regex_pattern, line):
                # Insert the string after the matching line
                lines.insert(i + 1, string_to_insert)
                break  # Stop searching after the first occurrence
        else:
            print(f"No line matching the regex pattern: {regex_pattern}. Skipping.")

        # Write the modified content back to the file
        with open(filepath, 'w', encoding=encoding) as file:
            file.writelines(lines)

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# # Example usage:
# insert_after_regex(r'\d+', "example.txt", "inserted_string\n")
# import re

def insert_between_queries(query1, query2, filepath, string_to_insert, encoding='utf-8'):
    try:
        # Read the file and store its content
        with open(filepath, 'r', encoding=encoding) as file:
            lines = file.readlines()

        # Find the lines containing query 1 and query 2
        index_query1 = next((i for i, line in enumerate(lines) if re.search(query1, line)), None)
        index_query2 = next((i for i, line in enumerate(lines) if re.search(query2, line)), None)

        # Insert the string between the lines with query 1 and query 2
        if index_query1 is not None and index_query2 is not None:
            lines.insert(index_query2, string_to_insert)
            lines.insert(index_query1 + 1, string_to_insert)
        else:
            print(f"Queries not found in the file. Skipping insertion.")

        # Write the modified content back to the file
        with open(filepath, 'w', encoding=encoding) as file:
            file.writelines(lines)

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# # Example usage:
# insert_between_queries("query1", "query2", "example.txt", "inserted_string\n")
# import re

def replace_between_queries_replace_each_line(query1, query2, filepath, string_to_replace, encoding='utf-8'):
    try:
        # Read the file and store its content
        with open(filepath, 'r', encoding=encoding) as file:
            lines = file.readlines()

        # Find the lines containing query 1 and query 2
        index_query1 = next((i for i, line in enumerate(lines) if re.search(query1, line)), None)
        index_query2 = next((i for i, line in enumerate(lines) if re.search(query2, line)), None)

        # Replace the content between the lines with query 1 and query 2
        if index_query1 is not None and index_query2 is not None:
            for i in range(index_query1 + 1, index_query2):
                lines[i] = string_to_replace
        else:
            print(f"Queries not found in the file. Skipping replacement.")

        # Write the modified content back to the file
        with open(filepath, 'w', encoding=encoding) as file:
            file.writelines(lines)

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# # Example usage:
# replace_between_queries("query1", "query2", "example.txt", "replaced_string\n")

def replace_between_queries(query1, query2, filepath, string_to_replace, encoding='utf-8'):
    try:
        # Read the file and store its content
        with open(filepath, 'r', encoding=encoding) as file:
            lines = file.readlines()

        # Find the lines containing query 1 and query 2
        index_query1 = next((i for i, line in enumerate(lines) if re.search(query1, line)), None)
        index_query2 = next((i for i, line in enumerate(lines) if re.search(query2, line)), None)

        # Replace the content between the lines with query 1 and query 2 with the specified string
        if index_query1 is not None and index_query2 is not None:
            lines[index_query1 + 1:index_query2] = [string_to_replace]
        else:
            print(f"Queries not found in the file. Skipping replacement.")

        # Write the modified content back to the file
        with open(filepath, 'w', encoding=encoding) as file:
            file.writelines(lines)

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# # Example usage:
# replace_between_queries("query1", "query2", "example.txt", "replaced_string\n")

def inclusive_replace_between_queries_inclusive(query1, query2, filepath, string_to_replace, encoding='utf-8'):
    try:
        # Read the file and store its content
        with open(filepath, 'r', encoding=encoding) as file:
            lines = file.readlines()

        # Find the lines containing query 1 and query 2
        index_query1 = next((i for i, line in enumerate(lines) if re.search(query1, line)), None)
        index_query2 = next((i for i, line in enumerate(lines) if re.search(query2, line)), None)

        # Replace the content between the lines with query 1 and query 2 (inclusive) with the specified string
        if index_query1 is not None and index_query2 is not None:
            lines[index_query1:index_query2 + 1] = [string_to_replace]
        else:
            print(f"Queries not found in the file. Skipping replacement.")

        # Write the modified content back to the file
        with open(filepath, 'w', encoding=encoding) as file:
            file.writelines(lines)

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# # Example usage:
# inclusive_replace_between_queries("query1", "query2", "example.txt", "replaced_string\n")
