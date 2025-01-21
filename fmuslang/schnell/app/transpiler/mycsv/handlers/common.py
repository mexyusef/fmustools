
default_table_name = "Monyong"

from schnell.app.dirutils import (
  joiner, ayah
)

disini = joiner(ayah(__file__,1))

pemisah = '\n' + '// ' + '*'*5 + ' __TITLE__' + '\n'*2