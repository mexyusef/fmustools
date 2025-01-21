
from __future__ import absolute_import

import re


class LazyReCompile(object):
    """Compile regular expressions on first use

    This class allows one to store regular expressions and compiles them on
    first use."""

    def __init__(self, regex, flags=0):
        self.regex = regex
        self.flags = flags
        self.compiled = None

    def compile_regex(method):
        def _impl(self, *args, **kwargs):
            if self.compiled is None:
                self.compiled = re.compile(self.regex, self.flags)
            return method(self, *args, **kwargs)
        return _impl

    @compile_regex
    def finditer(self, *args, **kwargs):
        return self.compiled.finditer(*args, **kwargs)

    @compile_regex
    def search(self, *args, **kwargs):
        return self.compiled.search(*args, **kwargs)

    @compile_regex
    def match(self, *args, **kwargs):
        return self.compiled.match(*args, **kwargs)

    @compile_regex
    def sub(self, *args, **kwargs):
        return self.compiled.sub(*args, **kwargs)
