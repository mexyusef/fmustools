
import os, shutil


# elif oper .startswith ('copy_absolute_dir_from'):
def copy_absolute_dir_from(oper, item, self_debug):
  source = oper.split('=') [1]
  self_debug('copy ABSOLUTE direktori dari', source)
  if os.path.exists(item.workdir):
    shutil.rmtree(item.workdir)

  if hasattr(item, 'patterns'):
    shutil.copytree(source, item.workdir, ignore=shutil.ignore_patterns(*item.patterns))
  else:
    shutil.copytree(source, item.workdir)