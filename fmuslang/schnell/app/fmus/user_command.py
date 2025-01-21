import os
# elif item.type == 'user_command':
def user_command():
  perintah = input(f'Masukkan perintah untuk dijalankan: ')
  if perintah != '':
    if perintah.startswith('cd '): # special utk cd -> %%% di kode, input = cd folder
      perintah = perintah.replace('cd ', '', 1)
      if perintah != '':
        os.chdir(perintah)
    else:
      os.system(perintah)
