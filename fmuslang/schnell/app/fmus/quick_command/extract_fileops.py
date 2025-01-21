import re


def extract_fileops(text):
    """
    [...content...]
    """
    found = re.search(r'^\[(?P<operations>.*)\|(?P<filename>.*)\](?P<code>.*)', text)
    if found:
        return (found.group('operations'), found.group('filename'), found.group('code'))
    return (None, None, None)

