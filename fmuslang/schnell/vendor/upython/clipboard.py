
from __future__ import absolute_import

import subprocess
import os
import platform
from locale import getpreferredencoding


class CopyFailed(Exception):
    pass


class XClipboard(object):
    """Manage clipboard with xclip."""

    def copy(self, content):
        process = subprocess.Popen(['xclip', '-i', '-selection', 'clipboard'],
                                   stdin=subprocess.PIPE)
        process.communicate(content.encode(getpreferredencoding()))
        if process.returncode != 0:
            raise CopyFailed()


class OSXClipboard(object):
    """Manage clipboard with pbcopy."""

    def copy(self, content):
        process = subprocess.Popen(['pbcopy', 'w'], stdin=subprocess.PIPE)
        process.communicate(content.encode(getpreferredencoding()))
        if process.returncode != 0:
            raise CopyFailed()


def command_exists(command):
    process = subprocess.Popen(['which', command], stderr=subprocess.STDOUT,
                               stdout=subprocess.PIPE)
    process.communicate()

    return process.returncode == 0


def get_clipboard():
    """Get best clipboard handling implementation for current system."""

    if platform.system() == 'Darwin':
        if command_exists('pbcopy'):
            return OSXClipboard()
    if (platform.system() in ('Linux', 'FreeBSD', 'OpenBSD') and
            os.getenv('DISPLAY') is not None):
        if command_exists('xclip'):
            return XClipboard()

    return None