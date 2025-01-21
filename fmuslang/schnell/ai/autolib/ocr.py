import datetime
# pip install gcloud
# pip install google-cloud
# pip install google-cloud-vision
from google.cloud import (
  # speech,
  # translate,
  # texttospeech,
  vision,
)
from schnell.app.dirutils import normy
from schnell.app.fileutils import (
  file_content_binary,
  file_remove,
)
# from schnell.app.utils import env_set, env_get
from schnell.app.mediautils import (
  capture_gambar,
	# stringified_image_asb64, 	
	# lihat_gambar, 
	# capture_lihat_gambar, 
	# capture_lihat_stringified_image_asb64,
	# get_lihat_stringified_image_asb64,
	# requests_get_lihat_stringified_image_asb64,
)
from schnell.app.envvalues import datadir_
# from schnell.app.autoutils import minimize_current_window


# def get_credentials():
#   return env_get('GOOGLE_APPLICATION_CREDENTIALS')

# def set_credentials(credfile = 'bantuan-315802-249434968500.json'):
#   sini = here(__file__)
#   env_set('GOOGLE_APPLICATION_CREDENTIALS', joiner(sini, credfile))
#   indah3('Creds: ' + get_credentials(), warna='green')

# from google.cloud.speech import enums
# from google.cloud.speech import types
# from google.cloud.vision import types

# sblm panggil methods, set credentials dulu
# set_credentials()

# translator = translate.Client()
# tts = texttospeech.TextToSpeechClient()
# recognizer = speech.SpeechClient()
ocrclient = vision.ImageAnnotatorClient()


def ocr_gettext(filepath):
  content = file_content_binary(filepath)

  # https://stackoverflow.com/questions/64226174/attributeerror-module-google-cloud-vision-has-no-attribute-types
  # image = vision.types.Image(content=content)
  image = vision.Image(content=content)
  response = ocrclient.text_detection(image=image)
  texts = response.text_annotations

  # print('Texts:')
  # print type(texts)
  # terlalu ribut...

  tulisan = texts[0].description
  return tulisan


def capture_to_text(output_file = None):
  if not output_file:
    output_file = datadir_() + f"/ocr-data/ocr_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    output_file = normy(output_file)
  # ternyata gambar jadi menyatu...
  # hapus dulu sblm capture
  file_remove(output_file)
  print('[schnell.ai.autolib.ocr][capture_to_text] saved screenshot:', output_file)
  # sblm capture, kita minimize dulu current window (misal repl terminal)
  # minimize_current_window()
  # err not working...
  capture_gambar(output_file)
  return ocr_gettext(output_file), output_file
