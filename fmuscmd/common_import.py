import os, sys

__this_folder__ = os.path.dirname(__file__) # fmuscmd
__parent_folder__ = os.path.dirname(__this_folder__) # fmustools

__prompt_toolkit__ = os.path.join(__this_folder__, 'cli')
sys.path.insert(0, __prompt_toolkit__)

ciledugdir = os.path.join(__parent_folder__, 'fmuslang')
sys.path.insert(0, ciledugdir)

# sidoarjodir = r'c:\users\usef\work\sidoarjo'
# sys.path.insert(0, sidoarjodir)
PERINTAH_JSON = os.path.join(ciledugdir, 'config_perintah.json')

import timeit

def measure_import_time(import_statement):
    start_time = timeit.default_timer()
    exec(import_statement)
    elapsed_time = timeit.default_timer() - start_time
    print(f"Time taken for {import_statement} import: {elapsed_time:.6f} seconds")

# measure_import_time('import module1')
# measure_import_time('import module2')
from context import global_context, command_prompt_data, command_prompt_data_extension
