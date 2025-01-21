import re

"""
ini tentu rumit, tapi perlu...spy gak perlu banyak mikir...
"""

def hour_expression(request):
    r"""
    misal:
    1h4m3s
    1h30s
    4m
    4m5s

    >>> re.search(r'(\d+h)?(\d+m)?(\d+s)?', '1h4m3s').groups()
    ('1h', '4m', '3s')

    >>> re.search(r'(\d+h)?(\d+m)?(\d+s)?', '4m').groups()
    (None, '4m', None)

    >>> re.search(r'(\d+h)?(\d+m)?(\d+s)?', '1h30s').groups()
    ('1h', None, '30s')
    """
    hours, minutes, seconds = 0,0,0
    if 'h' in request:
        hours = re.search(r'(\d+h)?(\d+m)?(\d+s)?', request).groups() [0].replace('h','')
    if 'm' in request:
        minutes = re.search(r'(\d+h)?(\d+m)?(\d+s)?', request).groups() [1].replace('m','')
    if 's' in request:
        seconds = re.search(r'(\d+h)?(\d+m)?(\d+s)?', request).groups() [2].replace('s','')
    return hours, minutes, seconds
