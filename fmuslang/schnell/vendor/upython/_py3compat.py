

"""
    Helper module for Python 3 compatibility.

    Defines the following attributes:

    - PythonLexer: Pygment's Python lexer matching the hosting runtime's
      Python version.
    - py3: True if the hosting Python runtime is of Python version 3 or later
"""

from __future__ import absolute_import

import sys
import threading

py3 = (sys.version_info[0] == 3)


if py3:
    from pygments.lexers import Python3Lexer as PythonLexer
else:
    from pygments.lexers import PythonLexer


if py3 or sys.version_info[:3] >= (2, 7, 3):
    def prepare_for_exec(arg, encoding=None):
        return arg
else:
    def prepare_for_exec(arg, encoding=None):
        return arg.encode(encoding)


if py3:
    def try_decode(s, encoding):
        return s
else:
    def try_decode(s, encoding):
        """Try to decode s which is str names. Return None if not decodable"""
        if not isinstance(s, unicode):
            try:
                return s.decode(encoding)
            except UnicodeDecodeError:
                return None
        return s


if py3:
    def is_main_thread():
        return threading.main_thread() == threading.current_thread()
else:
    def is_main_thread():
        return isinstance(threading.current_thread(), threading._MainThread)
