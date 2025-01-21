import os, sys, pathlib, traceback


def print_err(err=''):
    from .printutils import indah4
    if err:
        indah4(str(err), warna='red')
    trace = traceback.format_exc()
    indah4(trace, warna='magenta')
