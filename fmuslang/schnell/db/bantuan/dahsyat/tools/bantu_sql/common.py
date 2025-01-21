from app.dirutils import (
  here, joiner
)
from db.bantuan.common import (
  output_folder,
)
disini = here(__file__)

filename_input = 'bantu_sql'
filename_input_ext = f'{filename_input}.mk'
filepath_input = joiner(disini, filename_input_ext)

filepath_output = joiner(output_folder, f'{filename_input}-output.mk')
