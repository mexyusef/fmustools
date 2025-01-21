from app.dirutils import (
  here, 
  joiner, 
  within_same_folder,
)
# from db.bantuan.common import (
#   output_folder,
#   TEMPLATESDIR,
# )
disini = here(__file__)

# input_django_mkfile_template = '/home/usef/common/working/redahsyat/input/django-input.mk'
# input_django_mkfile_template = '/home/usef/common/working/redahsyat/input/django-input-conditional-user.mk'
# output_django_mkfile = '/home/usef/common/working/redahsyat/output/django-output.mk'

# filename_input = 'django-input-conditional-user'
# input_django_mkfile_template = within_same_folder(__file__, f'{filename_input}.mk')
# output_django_mkfile = joiner(output_folder, f'{filename_input}-output.mk')

tpl_appwebsocket = joiner(disini, 'templates/app_websocket.py')
