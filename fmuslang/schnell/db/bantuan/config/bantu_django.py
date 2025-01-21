from schnell.app.utils import env_get
# input_django_mkfile_template = '/home/usef/common/working/redahsyat/input/django-input.mk'
redahsyat_output_folder = env_get('ULIBPY_REDAHSYAT_OUTPUT')
redahsyat_input_folder = env_get('ULIBPY_REDAHSYAT_INPUT') # /home/usef/common/working/redahsyat/input/
input_django_mkfile_template = f'{redahsyat_input_folder}django-input-conditional-user.mk'
output_django_mkfile = f'{redahsyat_output_folder}django-output.mk'

default_user_mk_entry = """
    user,d(/mk)
      signals.py,f(e=utama=/django-starter1/apps/user/signals.py)
      __init__.py,f(e=utama=/django-starter1/apps/user/__init__.py)
      renderers.py,f(e=utama=/django-starter1/apps/user/renderers.py)
      admin.py,f(e=utama=/django-starter1/apps/user/admin.py)
      views.py,f(e=utama=/django-starter1/apps/user/views.py)
      urls.py,f(e=utama=/django-starter1/apps/user/urls.py)
      backends.py,f(e=utama=/django-starter1/apps/user/backends.py)
      serializers.py,f(e=utama=/django-starter1/apps/user/serializers.py)
      models.py,f(e=utama=/django-starter1/apps/user/models.py)
"""
