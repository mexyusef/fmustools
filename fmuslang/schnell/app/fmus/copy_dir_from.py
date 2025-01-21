import shutil
from schnell.app.dirutils import joiner


# elif oper .startswith ('copy_dir_from'):
def copy_dir_from(oper, item, self_debug, self_run_configuration):
  '''
  # ini utk operasi file f,(f=lokasi-relatif-terhadap-cwd) <- don't use
  # don't use krn kita sudah gak pake ini template dir
  # dan cwd juga gak rujuk ke folder yg kita gunakan sekarang

  "templates": "templates", <- filemanager/templates
  templates = os.path.join(workdir, run_configuration['templates'])
  TODO:
  ganti templatedir ke lokasi yg diconfigure dan absolute atau yg digunakan
  '''
  sumber = oper.split('=') [1]
  templatedir_sumber_copy = self_run_configuration['templatesdir'] # joiner(self.run_configuration['cwd'], self.run_configuration['templates'])
  source = joiner(templatedir_sumber_copy, sumber)
  self_debug('copy direktori dari', source)

  if hasattr(item, 'patterns'):
    shutil.copytree(source, item.workdir, ignore=shutil.ignore_patterns(*item.patterns))
  else:
    shutil.copytree(source, item.workdir)