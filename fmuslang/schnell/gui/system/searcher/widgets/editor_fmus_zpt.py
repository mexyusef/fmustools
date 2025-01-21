import os
import sys
import openai

from schnell.app.dirutils import joiner, suffix_filename
from schnell.app.envutils import env_get
from schnell.app.imageutils import windows_photo_viewer
from schnell.app.regexutils import detect_format, convert_to_valid_version
from schnell.app.urlutils import save_image_shutil
from schnell.app.utils import trycopy, env_get
from schnell.app.notifutils import notifpy

openai.api_key = env_get("ULIBPY_OPENAI_API_KEY")
# openai.Model.list()

# lokasi = r'C:\work\ciledug\Bard-API'
sys.path.append(env_get('ULIBPY_BARD_SOURCE'))
os.environ['_BARD_API_KEY']=env_get('ULIBPY_BARD_KEY')

Barder = None

# Barder = bardapi.core.Bard(timeout=20)
# https://analyzingalpha.com/openai-api-python-tutorial

def with_different_responses(prompt, model="text-davinci-003", temperature=0.6, max_tokens=1024, n=3):
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=n,
    )
    return [item['text'] for item in response.choices]


def with_tokens(prompt, model="text-davinci-003", temperature=0.6, max_tokens=1024):
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].text


def no_tokens(prompt, model="text-davinci-003", temperature=0.6):
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
    )
    return response.choices[0].text


def process_zpt(bariskalimat):
    model = "text-davinci-003"
    tokens = 100
    temp = 0.6
    code, result_tuple = detect_format(bariskalimat)
    print(f"""[process_zpt]
    bariskalimat = {bariskalimat}
    code = {code}
    result_tuple = {result_tuple}
    """)
    if code == 1:
        tokens, text = result_tuple
        tokens = int(tokens)
        result = with_tokens(text, max_tokens=tokens)
    elif code == 2:
        tokens, temp, text = result_tuple
        tokens = int(tokens)
        temp = float(temp)
        result = with_tokens(text, temperature=temp, max_tokens=tokens)
    elif code == 3:
        tokens, temp, model, text = result_tuple
        tokens = int(tokens)
        temp = float(temp)
        result = with_tokens(text, model, temp, tokens)
    else:
        result = no_tokens(bariskalimat, model, temp)
    return result


def process_zpt_image(prompt, n=1, size='512x512'):
    result = 'NOK'
    response = openai.Image.create(prompt=prompt, n=n, size=size)
    # if n==1:
    #     result = response['data'][0]['url']
    # else:
    #     result = [item['url'] for item in response['data'] ]
    # return result
    return [item['url'] for item in response['data'] ]


def wrap_process_zpt_image(filepath_or_dirpath, prompt, n=1, size='512x512'):
    """
    filepath_or_dirpath
        jk n==1, berharap filepath
        else, berharap dirpath
    hasil AI akan disimpan ke filepath_or_dirpath, lalu diviewed dg photo viewer
    """
    results = process_zpt_image(prompt, n=n, size=size)
    print(f"""[wrap_process_zpt_image_variation]
    results = {results}
    """)
    result = ''
    if n==1:
        url = results[0] # str
        result = save_image_shutil(url, filepath_or_dirpath)
    else:
        filename = convert_to_valid_version(prompt[:20])
        for i, url in enumerate(results, 1):
            filepath = joiner(filepath_or_dirpath, f'{filename}_{i}.jpg')
            result = save_image_shutil(url, filepath)
    windows_photo_viewer(result)
    notifpy('image creation', f'{result}')
    trycopy(result)


def process_zpt_image_edit(prompt, image_input, image_mask, n=1, size='512x512'):
    """
    openai.Image.create_edit()
    """
    result = 'NOK'
    response = openai.Image.create_edit(
        prompt=prompt, n=n, size=size,
        image=open(image_input, 'rb'),
        mask=open(image_mask, 'rb')
    )
    if n==1:
        result = response['data'][0]['url']
    else:
        result = [item['url'] for item in response['data'] ]
    return result


def process_zpt_image_variation(image_input, n=1, size='512x512'):
    """
    https://youtu.be/1TMu4hrqv5k?t=625
    openai.Image.create_variation()
    """
    result = 'NOK'
    response = openai.Image.create_variation(image=open(image_input, 'rb'), n=n, size=size)
    # if n==1:
    #     result = response['data'][0]['url']
    # else:
    #     result = [item['url'] for item in response['data'] ]
    # return result
    return [item['url'] for item in response['data'] ]


def wrap_process_zpt_image_variation(filepath_or_dirpath, image_input, n=1, size='512x512'):
    """
    filepath_or_dirpath
        jk n==1, berharap filepath
        else, berharap dirpath
    hasil AI akan disimpan ke filepath_or_dirpath, lalu diviewed dg photo viewer

    openai.error.InvalidRequestError: Uploaded image must be a PNG and less than 4 MB.
    """
    results = process_zpt_image_variation(image_input, n=n, size=size)
    print(f"""[wrap_process_zpt_image_variation]
    results = {results}
    """)
    result = ''
    if n==1:
        url = results[0] # str
        result = save_image_shutil(url, filepath_or_dirpath)
    else:
        # filename = convert_to_valid_version(prompt[:20])
        for i, url in enumerate(results, 1):
            filepath = suffix_filename(image_input, f'_{i}')
            result = save_image_shutil(url, filepath)
    windows_photo_viewer(result)
    notifpy('image variation', f'{result}')
    trycopy(result)


def bard_prompt(message):
    global Barder
    if not Barder:
        import bardapi
        Barder = bardapi.core.Bard(timeout=20)
    response = Barder.get_answer(message)
    return response['content']
