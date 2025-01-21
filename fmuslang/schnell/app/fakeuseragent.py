# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import random
from threading import Lock

import logging

import os
import tempfile

__version__ = '0.1.11'

DB = os.path.join(
    tempfile.gettempdir(),
    'fake_useragent_{version}.json'.format(
        version=__version__,
    ),
)

CACHE_SERVER = 'https://fake-useragent.herokuapp.com/browsers/{version}'.format(  # noqa
    version=__version__,
)

BROWSERS_STATS_PAGE = 'https://www.w3schools.com/browsers/default.asp'

BROWSER_BASE_PAGE = 'http://useragentstring.com/pages/useragentstring.php?name={browser}'  # noqa

BROWSERS_COUNT_LIMIT = 50

REPLACEMENTS = {
    ' ': '',
    '_': '',
}

SHORTCUTS = {
    'internet explorer': 'internetexplorer',
    'ie': 'internetexplorer',
    'msie': 'internetexplorer',
    'edge': 'internetexplorer',
    'google': 'chrome',
    'googlechrome': 'chrome',
    'ff': 'firefox',
}

OVERRIDES = {
    'Edge/IE': 'Internet Explorer',
    'IE/Edge': 'Internet Explorer',
}

HTTP_TIMEOUT = 5

HTTP_RETRIES = 2

HTTP_DELAY = 0.1


class FakeUserAgentError(Exception):
    pass


# common alias
UserAgentError = FakeUserAgentError

logger = logging.getLogger(__package__)

# from fake_useragent import settings
# from fake_useragent.errors import FakeUserAgentError
# from fake_useragent.log import logger
# from fake_useragent.utils import load, load_cached, str_types, update

import contextlib
import inspect
import io
import json
import os
import re
import ssl

# from fake_useragent.log import logger

try:  # Python 2 # pragma: no cover
    from urllib2 import urlopen, Request, URLError
    from urllib import quote_plus

    str_types = (unicode, str)  # noqa
    text = unicode  # noqa
except ImportError:  # Python 3 # pragma: no cover
    from urllib.request import urlopen, Request
    from urllib.parse import quote_plus
    from urllib.error import URLError

    str_types = (str,)
    text = str

# gevent monkey patched environment check
try:  # pragma: no cover
    import socket
    import gevent.socket

    if socket.socket is gevent.socket.socket:
        from gevent import sleep
    else:
        from time import sleep
except (ImportError, AttributeError):  # pragma: no cover
    from time import sleep


try:
    urlopen_args = inspect.getfullargspec(urlopen).kwonlyargs
except AttributeError:
    urlopen_args = inspect.getargspec(urlopen).args

urlopen_has_ssl_context = 'context' in urlopen_args


def get(url, verify_ssl=True):
    attempt = 0

    while True:
        request = Request(url)

        attempt += 1

        try:
            if urlopen_has_ssl_context:
                if not verify_ssl:
                    context = ssl._create_unverified_context()
                else:
                    context = None

                with contextlib.closing(urlopen(
                    request,
                    timeout=HTTP_TIMEOUT,
                    context=context,
                )) as response:
                    return response.read()
            else:  # ssl context is not supported ;(
                with contextlib.closing(urlopen(
                    request,
                    timeout=HTTP_TIMEOUT,
                )) as response:
                    return response.read()
        except (URLError, OSError) as exc:
            logger.debug(
                'Error occurred during fetching %s',
                url,
                exc_info=exc,
            )

            if attempt == HTTP_RETRIES:
                raise FakeUserAgentError('Maximum amount of retries reached')
            else:
                logger.debug(
                    'Sleeping for %s seconds',
                    HTTP_DELAY,
                )
                sleep(HTTP_DELAY)


def get_browsers(verify_ssl=True):
    """
    very very hardcoded/dirty re/split stuff, but no dependencies
    """
    html = get(BROWSERS_STATS_PAGE, verify_ssl=verify_ssl)
    html = html.decode('utf-8')
    try:
        # bukan w3, ws
        # html = html.split('<table class="w3-table-all notranslate">')[1]
        html = html.split('<table class="ws-table-all notranslate">')[1]
    except Exception as err:
        print(f'''
        gagal {err}
        cek apa ['<table class="w3-table-all notranslate">'] ada di html?
        ada? {'<table class="w3-table-all notranslate">' in html}
        kalo <table class="ws-table-all notranslate">
        ada? {'<table class="ws-table-all notranslate">' in html}

        <th class="right"><a href="browsers_chrome.asp">Chrome</a></th>
        <th class="right"><a href="browsers_explorer.asp">Edge</a></th>
        <th class="right"><a href="browsers_firefox.asp">Firefox</a></th>
        <th class="right"><a href="browsers_safari.asp">Safari</a></th>
        <th class="right"><a href="browsers_opera.asp">Opera</a></th>

        html adlh: 
        {html[:100]}
        ''')
    # html = html.split('</table>')[0]

    # pattern = r'\.asp">(.+?)<'
    # browsers = re.findall(pattern, html, re.UNICODE)

    # browsers = [
    #     OVERRIDES.get(browser, browser)
    #     for browser in browsers
    # ]

    # pattern = r'td\sclass="right">(.+?)\s'
    # browsers_statistics = re.findall(pattern, html, re.UNICODE)

    # return list(zip(browsers, browsers_statistics))
    return ['Chrome', '80.3', 'Edge', '7.5', 'Firefox', '5.3', 'Safari', '3.7', 'Opera', '2.3']


def get_browser_versions(browser, verify_ssl=True):
    """
    very very hardcoded/dirty re/split stuff, but no dependencies
    """
    html = get(
        BROWSER_BASE_PAGE.format(browser=quote_plus(browser)),
        verify_ssl=verify_ssl,
    )
    html = html.decode('iso-8859-1')
    html = html.split('<div id=\'liste\'>')[1]
    html = html.split('</div>')[0]

    pattern = r'\?id=\d+\'>(.+?)</a'
    browsers_iter = re.finditer(pattern, html, re.UNICODE)

    browsers = []

    for browser in browsers_iter:
        if 'more' in browser.group(1).lower():
            continue

        browsers.append(browser.group(1))

        if len(browsers) == BROWSERS_COUNT_LIMIT:
            break

    if not browsers:
        raise FakeUserAgentError(
            'No browsers version found for {browser}'.format(browser=browser))

    return browsers


def load(use_cache_server=True, verify_ssl=True):
    browsers_dict = {}
    randomize_dict = {}

    try:
        for item in get_browsers(verify_ssl=verify_ssl):
            browser, percent = item

            browser_key = browser

            for value, replacement in REPLACEMENTS.items():
                browser_key = browser_key.replace(value, replacement)

            browser_key = browser_key.lower()

            browsers_dict[browser_key] = get_browser_versions(
                browser,
                verify_ssl=verify_ssl,
            )

            # it is actually so bad way for randomizing, simple list with
            # browser_key's is event better
            # I've failed so much a lot of years ago.
            # Ideas for refactoring
            # {'chrome': <percantage|int>, 'firefox': '<percatage|int>'}
            for _ in range(int(float(percent) * 10)):
                randomize_dict[str(len(randomize_dict))] = browser_key
    except Exception as exc:
        if not use_cache_server:
            raise exc

        logger.warning(
            'Error occurred during loading data. '
            'Trying to use cache server %s',
            CACHE_SERVER,
            exc_info=exc,
        )
        try:
            ret = json.loads(get(
                CACHE_SERVER,
                verify_ssl=verify_ssl,
            ).decode('utf-8'))
        except (TypeError, ValueError):
            raise FakeUserAgentError('Can not load data from cache server')
    else:
        ret = {
            'browsers': browsers_dict,
            'randomize': randomize_dict,
        }

    if not isinstance(ret, dict):
        raise FakeUserAgentError('Data is not dictionary ', ret)

    for param in ['browsers', 'randomize']:
        if param not in ret:
            raise FakeUserAgentError('Missing data param: ', param)

        if not isinstance(ret[param], dict):
            raise FakeUserAgentError('Data param is not dictionary', ret[param])  # noqa

        if not ret[param]:
            raise FakeUserAgentError('Data param is empty', ret[param])

    return ret


# TODO: drop these useless functions


def write(path, data):
    with io.open(path, encoding='utf-8', mode='wt') as fp:
        dumped = json.dumps(data)

        if not isinstance(dumped, text):  # Python 2
            dumped = dumped.decode('utf-8')

        fp.write(dumped)


def read(path):
    with io.open(path, encoding='utf-8', mode='rt') as fp:
        return json.loads(fp.read())


def exist(path):
    return os.path.isfile(path)


def rm(path):
    if exist(path):
        os.remove(path)


def update(path, use_cache_server=True, verify_ssl=True):
    rm(path)

    write(path, load(use_cache_server=use_cache_server, verify_ssl=verify_ssl))


def load_cached(path, use_cache_server=True, verify_ssl=True):
    if not exist(path):
        update(path, use_cache_server=use_cache_server, verify_ssl=verify_ssl)

    return read(path)


# from fake_useragent import settings  # noqa # isort:skip
# from fake_useragent.errors import FakeUserAgentError  # noqa # isort:skip


class FakeUserAgent(object):
    def __init__(
        self,
        cache=True,
        use_cache_server=True,
        path=DB,
        fallback=None,
        verify_ssl=True,
        safe_attrs=tuple(),
    ):
        assert isinstance(cache, bool), \
            'cache must be True or False'

        self.cache = cache

        assert isinstance(use_cache_server, bool), \
            'use_cache_server must be True or False'

        self.use_cache_server = use_cache_server

        assert isinstance(path, str_types), \
            'path must be string or unicode'

        self.path = path

        if fallback is not None:
            assert isinstance(fallback, str_types), \
                'fallback must be string or unicode'

        self.fallback = fallback

        assert isinstance(verify_ssl, bool), \
            'verify_ssl must be True or False'

        self.verify_ssl = verify_ssl

        assert isinstance(safe_attrs, (list, set, tuple)), \
            'safe_attrs must be list\\tuple\\set of strings or unicode'

        if safe_attrs:
            str_types_safe_attrs = [
                isinstance(attr, str_types) for attr in safe_attrs
            ]

            assert all(str_types_safe_attrs), \
                'safe_attrs must be list\\tuple\\set of strings or unicode'

        self.safe_attrs = set(safe_attrs)

        # initial empty data
        self.data = {}
        # TODO: change source file format
        # version 0.1.4+ migration tool
        self.data_randomize = []
        self.data_browsers = {}

        self.load()

    def load(self):
        try:
            with self.load.lock:
                if self.cache:
                    self.data = load_cached(
                        self.path,
                        use_cache_server=self.use_cache_server,
                        verify_ssl=self.verify_ssl,
                    )
                else:
                    self.data = load(
                        use_cache_server=self.use_cache_server,
                        verify_ssl=self.verify_ssl,
                    )

                # TODO: change source file format
                # version 0.1.4+ migration tool
                self.data_randomize = list(self.data['randomize'].values())
                self.data_browsers = self.data['browsers']
        except FakeUserAgentError:
            if self.fallback is None:
                raise
            else:
                logger.warning(
                    'Error occurred during fetching data, '
                    'but was suppressed with fallback.',
                )
    load.lock = Lock()

    def update(self, cache=None):
        with self.update.lock:
            if cache is not None:
                assert isinstance(cache, bool), \
                    'cache must be True or False'

                self.cache = cache

            if self.cache:
                update(
                    self.path,
                    use_cache_server=self.use_cache_server,
                    verify_ssl=self.verify_ssl,
                )

            self.load()
    update.lock = Lock()

    def __getitem__(self, attr):
        return self.__getattr__(attr)

    def __getattr__(self, attr):
        if attr in self.safe_attrs:
            return super(UserAgent, self).__getattr__(attr)

        try:
            for value, replacement in REPLACEMENTS.items():
                attr = attr.replace(value, replacement)

            attr = attr.lower()

            if attr == 'random':
                browser = random.choice(self.data_randomize)
            else:
                browser = SHORTCUTS.get(attr, attr)

            return random.choice(self.data_browsers[browser])
        except (KeyError, IndexError):
            if self.fallback is None:
                raise FakeUserAgentError('Error occurred during getting browser')  # noqa
            else:
                logger.warning(
                    'Error occurred during getting browser, '
                    'but was suppressed with fallback.',
                )

                return self.fallback


# common alias
UserAgent = FakeUserAgent
