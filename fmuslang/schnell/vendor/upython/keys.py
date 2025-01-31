
from __future__ import absolute_import

import string
from six.moves import range


class KeyMap(object):

    def __init__(self, default=''):
        self.map = {}
        self.default = default

    def __getitem__(self, key):
        if not key:
            # Unbound key
            return self.default
        elif key in self.map:
            return self.map[key]
        else:
            raise KeyError('Configured keymap (%s)' % key +
                           ' does not exist in bpython.keys')

    def __delitem__(self, key):
        del self.map[key]

    def __setitem__(self, key, value):
        self.map[key] = value


cli_key_dispatch = KeyMap(tuple())
urwid_key_dispatch = KeyMap('')

# fill dispatch with letters
for c in string.ascii_lowercase:
    cli_key_dispatch['C-%s' % c] = (chr(string.ascii_lowercase.index(c) + 1),
                                    '^%s' % c.upper())

for c in string.ascii_lowercase:
    urwid_key_dispatch['C-%s' % c] = 'ctrl %s' % c
    urwid_key_dispatch['M-%s' % c] = 'meta %s' % c

# fill dispatch with cool characters
cli_key_dispatch['C-['] = (chr(27), '^[')
cli_key_dispatch['C-\\'] = (chr(28), '^\\')
cli_key_dispatch['C-]'] = (chr(29), '^]')
cli_key_dispatch['C-^'] = (chr(30), '^^')
cli_key_dispatch['C-_'] = (chr(31), '^_')

# fill dispatch with function keys
for x in range(1, 13):
    cli_key_dispatch['F%d' % x] = ('KEY_F(%d)' % x,)

for x in range(1, 13):
    urwid_key_dispatch['F%d' % x] = 'f%d' % x

