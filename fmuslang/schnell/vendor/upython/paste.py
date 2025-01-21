
from __future__ import absolute_import

from locale import getpreferredencoding
from six.moves.urllib_parse import quote as urlquote, urljoin, urlparse
from string import Template
import errno
import requests
import subprocess
import unicodedata

# from .translations import _


class PasteFailed(Exception):
    pass


class PastePinnwand(object):
    def __init__(self, url, expiry, show_url, removal_url):
        self.url = url
        self.expiry = expiry
        self.show_url = show_url
        self.removal_url = removal_url

    def paste(self, s):
        """Upload to pastebin via json interface."""

        url = urljoin(self.url, '/json/new')
        payload = {
            'code': s,
            'lexer': 'pycon',
            'expiry': self.expiry
        }

        try:
            response = requests.post(url, data=payload, verify=True)
            response.raise_for_status()
        except requests.exceptions.RequestException as exc:
            raise PasteFailed(exc.message)

        data = response.json()

        paste_url_template = Template(self.show_url)
        paste_id = urlquote(data['paste_id'])
        paste_url = paste_url_template.safe_substitute(paste_id=paste_id)

        removal_url_template = Template(self.removal_url)
        removal_id = urlquote(data['removal_id'])
        removal_url = removal_url_template.safe_substitute(
            removal_id=removal_id)

        return (paste_url, removal_url)


class PasteHelper(object):
    def __init__(self, executable):
        self.executable = executable

    def paste(self, s):
        """Call out to helper program for pastebin upload."""

        try:
            helper = subprocess.Popen('',
                                      executable=self.executable,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE)
            helper.stdin.write(s.encode(getpreferredencoding()))
            output = helper.communicate()[0].decode(getpreferredencoding())
            paste_url = output.split()[0]
        except OSError as e:
            if e.errno == errno.ENOENT:
                raise PasteFailed('Helper program not found.')
            else:
                raise PasteFailed('Helper program could not be run.')

        if helper.returncode != 0:
            raise PasteFailed('Helper program returned non-zero exit '
                                'status %d.' % (helper.returncode, ))

        if not paste_url:
            raise PasteFailed('No output from helper program.')
        else:
            parsed_url = urlparse(paste_url)
            if (not parsed_url.scheme or
                any(unicodedata.category(c) == 'Cc'
                    for c in paste_url)):
                raise PasteFailed('Failed to recognize the helper '
                                    'program\'s output as an URL.')

        return paste_url, None
