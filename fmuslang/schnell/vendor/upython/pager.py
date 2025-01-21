
from __future__ import absolute_import

import curses
import errno
import os
import pydoc
import subprocess
import sys
import shlex

from ._py3compat import py3


def get_pager_command(default='less -rf'):
    command = shlex.split(os.environ.get('PAGER', default))
    return command


def page_internal(data):
    """A more than dumb pager function."""
    if hasattr(pydoc, 'ttypager'):
        pydoc.ttypager(data)
    else:
        sys.stdout.write(data)


def page(data, use_internal=False):
    command = get_pager_command()
    if not command or use_internal:
        page_internal(data)
    else:
        curses.endwin()
        try:
            popen = subprocess.Popen(command, stdin=subprocess.PIPE)
            if py3 or isinstance(data, unicode):
                data = data.encode(sys.__stdout__.encoding, 'replace')
            popen.stdin.write(data)
            popen.stdin.close()
        except OSError as e:
            if e.errno == errno.ENOENT:
                # pager command not found, fall back to internal pager
                page_internal(data)
                return
        except IOError as e:
            if e.errno != errno.EPIPE:
                raise
        while True:
            try:
                popen.wait()
            except OSError as e:
                if e.errno != errno.EINTR:
                    raise
            else:
                break
        curses.doupdate()
