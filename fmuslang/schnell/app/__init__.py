import sys

# ini agar pengguna via relative path (langs/flutter/flumain.py) bisa gunakan package ini
# print('name:', __name__)
# print(sys.modules[__name__])
str_module_main = str(sys.modules['__main__'])
# print(str_module_main)

if 'creator.repl' in str_module_main:
  from .app import Application
  from .utils import *
else:
  # agar bisa python schnell/main.py
  try:
    from .app import Application
  except Exception as err:
    # print(f"gagal 'from .app import Application' di schnell.app.__init__:", err)
    pass
