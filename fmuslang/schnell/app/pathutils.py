import re

def convert_to_valid_filename(path):
    """
    Convert a given path into a valid filename.

    This removes any strange characters and spaces in the path.

    Args:
        path (str): The path to convert.

    Returns:
        str: The valid filename.
    """
    filename = re.sub(r'[:<>|?*\\/]', '_', path)
    filename = re.sub(r'\s+', '_', filename)
    return filename


import unittest

class TestPathUtils(unittest.TestCase):
    def test_convert_to_valid_filename(self):
        cases = [
            ('this is a test', 'this_is_a_test'),
            ('this is a test:<>|?*\\/', 'this_is_a_test___'),
            ('  multiple  spaces  ', 'multiple_spaces'),
            ('this  is  a  test', 'this__is__a__test'),
            ('::::::::::::::::', '_______________')
        ]

        for path, expected_filename in cases:
            self.assertEqual(convert_to_valid_filename(path), expected_filename)

if __name__ == '__main__':
    # unittest.main()
    res = convert_to_valid_filename(r'C:\Users\usef\work\sidoarjo\schnell\app\pathutils.py')
    print(res)
