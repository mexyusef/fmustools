import os
import google.generativeai as genai
import google.ai.generativelanguage as glm
import pathlib
import textwrap

from IPython.display import display
from IPython.display import Markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

from schnell.app.fileutils import file_write_timestamped
from schnell.app.dirutils import joinhere
from schnell.app.printutils import indah4

from configuration_values import config_keys
GOOGLE_API_KEY=config_keys['keys']['gemini']

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat_history = []
global_chat = None


def stop_chat():
    global global_chat
    if global_chat:
        chat_history.append(global_chat.history)
        global_chat = None


def start_chat(prompt, history=[]):
    global global_chat
    stop_chat()
    global_chat = model.start_chat(history=history)
    response = global_chat.send_message(prompt)
    return response.text


def start_chat_stream(prompt, callback, history=[]):  # c-o, c-m
    global global_chat
    stop_chat()
    global_chat = model.start_chat(history=history)
    response = global_chat.send_message(prompt, stream=True)
    for chunk in response:
        callback(chunk.text)


def send_chat(prompt):
    if global_chat:
        response = global_chat.send_message(prompt)
        return response.text
    else:
        return start_chat(prompt)


def send_chat_stream(prompt, callback):  # c-o, m
    if global_chat:
        response = global_chat.send_message(prompt, stream=True)

        for chunk in response:
            try:
                # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\google\generativeai\types\generation_types.py
                callback(chunk.text)
            except ValueError as verr:
                indah4(str(verr), warna='red')
                if len(chunk.parts)>1:
                    callback('\n'.join([part.text for part in chunk.parts]))

    else:
        start_chat_stream(prompt, callback)


def list_model():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)


def get_response(pertanyaan):
    response = model.generate_content(pertanyaan)
    # return to_markdown(response.text)
    return response.text

def get_stream(pertanyaan, callback):
    response = model.generate_content(pertanyaan, stream=True)
    for chunk in response:
        callback(chunk.text)
        # print("_"*80)

gemini_prefix = '* '
gemini_prefix_len = len(gemini_prefix)

def gemini_header(bariskalimat):
	atasbawah = '*'*min(80, len(bariskalimat)+gemini_prefix_len)
	# bariskalimat bisa multi-baris, tiap baris jadi: 
	# * baris1
	# * baris2
	# dst.
	bisa_multi_baris = [gemini_prefix + baris for baris in bariskalimat.splitlines()]
	bisa_multi_baris = '\n'.join(bisa_multi_baris)
	return '\n' + atasbawah + '\n' + bisa_multi_baris + '\n' + atasbawah + '\n'

def print_chat_stream_template(msg, filepath):  # co, m (chat)
	file_write_timestamped(
        # joinhere(__file__, 'data/gemini', 'chat-stream.txt'),
        filepath,
        msg,
        write_mode='a',
        formatter='%Y%m%d-%H')
	# indah4(msg, warna='green', layar='yellow')
