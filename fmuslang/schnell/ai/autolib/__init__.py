import os
from schnell.app.dirutils import joiner, ayah, here
from schnell.app.utils import env_set

# https://pypi.org/project/autopy/
# load credentials

credfile = 'bantuan-315802-249434968500.json'
sini = here(__file__)
env_set('GOOGLE_APPLICATION_CREDENTIALS', joiner(sini, credfile))

from .repl import auto_process
