# pylint: disable=dangerous-default-value
# pylint: disable=invalid-name
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=multiple-imports
# pylint: disable=ungrouped-imports
# pylint: disable=unused-import
# pylint: disable=wrong-import-order
# pylint: disable=wrong-import-position
import os
import sys
import json

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    SystemMessage,
    FunctionMessage,
    ToolMessage,
    AIMessage,
    AnyMessage,
    AIMessageChunk
)

if __name__ == '__main__':
    sys.path.insert(0, r'c:\users\usef\work\sidoarjo')

# from schnell.app.llmutils.langchainutils.llms import gemini_accounts, gemini_vision_accounts, randomly_select_account
from schnell.app.llmutils.langchainutils.llm_config import gemini_accounts, gemini_vision_accounts
from schnell.app.llmutils.langchainutils.utils import randomly_select_account
from schnell.app.printutils import indah4
from schnell.app.cryptoutils import dekripsi
from schnell.app.llmutils.langchainutils.llm_config import all_accounts
# https://python.langchain.com/docs/integrations/llms/google_ai
# https://ai.google.dev/tutorials/python_quickstart
from schnell.app.llmutils.langchainutils.llms import with_memory
from schnell.app.llmutils.langchainutils.llm_config import google_models, google_models_get_default, google_models_get_default_for_vision
from schnell.app.llmutils.langchainutils.llms import use_memory


# from schnell.app.llmutils.langchainutils.llms.llm_gemini import chat_gemini
# Modify chat_gemini to accept memory
def new_chat_gemini(gemini_key=None, model=None, temperature=None, max_tokens=None, memory=None, top_p=None):
    if not model:
        model = google_models[google_models_get_default()]
    if not gemini_key:
        gemini_key = randomly_select_account(gemini_accounts)
    if gemini_accounts[gemini_key]['instance']:
        print(f"{gemini_key}/{gemini_accounts[gemini_key]['name']} reused with model {model}.")
        return gemini_accounts[gemini_key]['instance']

    used_temperature = temperature if temperature is not None else all_accounts['temperature']

    llm = ChatGoogleGenerativeAI(
        model = model,
        temperature = used_temperature,
        google_api_key = dekripsi(gemini_accounts[gemini_key]['key']),
        verbose = True,
        max_output_tokens = max_tokens if max_tokens is not None else all_accounts['max_output_tokens'],
        top_p = top_p if top_p is not None else all_accounts['top_p'],
        convert_system_message_to_human = True,
        memory = memory
    )
    gemini_accounts[gemini_key]['instance'] = llm
    print(f"{gemini_key}/{gemini_accounts[gemini_key]['name']} selected with model {model} with temp {used_temperature} and memory={memory}.")
    return llm

# from schnell.app.llmutils.langchainutils.llms.llm_gemini import create_llm_chat
def create_llm_chat(gemini_key=None, model=None, temperature=None, max_tokens=None, top_p=None):
    if not model:
        model = google_models[google_models_get_default()]
    if not gemini_key:
        gemini_key = randomly_select_account(gemini_accounts)
    if gemini_accounts[gemini_key]['instance']:
        print(f"{gemini_key}/{gemini_accounts[gemini_key]['name']} reused with model {model}.")
        return gemini_accounts[gemini_key]['instance']

    # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_google_genai\chat_models.py
    # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\google\generativeai\generative_models.py
    llm = ChatGoogleGenerativeAI(
        model = model,
        # temperature = temperature if temperature is not None else gemini_accounts[gemini_key]['temperature'],
        temperature = temperature if temperature is not None else all_accounts['temperature'],
        google_api_key = dekripsi(gemini_accounts[gemini_key]['key']),
        verbose = True,
        # max_output_tokens = max_tokens if max_tokens is not None else gemini_accounts[gemini_key]['max_tokens'],
        max_output_tokens = max_tokens if max_tokens is not None else all_accounts['max_output_tokens'],
        top_p = top_p if top_p is not None else all_accounts['top_p'],
        convert_system_message_to_human = True
    )
    gemini_accounts[gemini_key]['instance'] = llm
    print(f"{gemini_key}/{gemini_accounts[gemini_key]['name']} selected with model {model}.")
    return llm


# from schnell.app.llmutils.langchainutils.llms.llm_gemini import create_llm
def create_llm(gemini_key=None, model=None, temperature=None, verbose=False, max_tokens=None, top_p=None):
    if not model:
        model = google_models[google_models_get_default()]
    if not gemini_key:
        gemini_key = randomly_select_account(gemini_accounts)
    if gemini_accounts[gemini_key]['instance']:
        print(f"{gemini_key}/{gemini_accounts[gemini_key]['name']} reused.")
        return gemini_accounts[gemini_key]['instance']

    token_key = dekripsi(gemini_accounts[gemini_key]['key'])

    if verbose:
        indah4(f"""create_llm/gemini
        gemini_key      = {gemini_key}
        gemini_accounts[gemini_key]   = {gemini_accounts[gemini_key]}
        token_key       = {token_key}
        """, warna='yellow')

    llm = GoogleGenerativeAI(
        model = model,
        # temperature = temperature if temperature is not None else gemini_accounts[gemini_key]['temperature'],
        temperature = temperature if temperature is not None else all_accounts['temperature'],
        google_api_key = token_key,
        verbose = True,
        # max_output_tokens = max_tokens if max_tokens is not None else gemini_accounts[gemini_key]['max_tokens'],
        max_output_tokens = max_tokens if max_tokens is not None else all_accounts['max_output_tokens'],
        top_p = top_p if top_p is not None else all_accounts['top_p'],
        convert_system_message_to_human = True
    )
    gemini_accounts[gemini_key]['instance'] = llm
    print(f"{gemini_key}/{gemini_accounts[gemini_key]['name']} selected.")
    return llm


# https://python.langchain.com/docs/integrations/platforms/google
# https://ai.google.dev/tutorials/python_quickstart
# import google.ai.generativelanguage as glm
# model = genai.GenerativeModel('gemini-pro-vision')
# response = model.generate_content(
#     glm.Content(
#         parts = [
#             glm.Part(text="Write a short, engaging blog post based on this picture."),
#             glm.Part(
#                 inline_data=glm.Blob(
#                     mime_type='image/jpeg',
#                     data=pathlib.Path('image.jpg').read_bytes()
#                 )
#             ),
#         ],
#     ),
#     stream=True)
# response.resolve()
# to_markdown(response.text[:100] + "... [TRIMMED] ...")
def create_llm_vision_chat(gemini_key=None, model=None, temperature=None, max_tokens=None, top_p=None):
    if not model:
        model = google_models[google_models_get_default_for_vision()]
    if not gemini_key:
        gemini_key = randomly_select_account(gemini_vision_accounts)
    if gemini_vision_accounts[gemini_key]['vision_instance']:
        print(f"{gemini_key}/{gemini_vision_accounts[gemini_key]['name']} reused with model {model}.")
        return gemini_vision_accounts[gemini_key]['vision_instance']

    llm = ChatGoogleGenerativeAI(
        model = model,
        # temperature = temperature if temperature is not None else gemini_vision_accounts[gemini_key]['temperature'],
        temperature = temperature if temperature is not None else all_accounts['temperature'],
        google_api_key = dekripsi(gemini_vision_accounts[gemini_key]['key']),
        verbose = True,
        # max_output_tokens = max_tokens if max_tokens is not None else gemini_vision_accounts[gemini_key]['max_tokens'],
        max_output_tokens = max_tokens if max_tokens is not None else all_accounts['max_output_tokens'],
        top_p = top_p if top_p is not None else all_accounts['top_p'],
        convert_system_message_to_human = True
    )
    gemini_vision_accounts[gemini_key]['vision_instance'] = llm
    print(f"{gemini_key}/{gemini_vision_accounts[gemini_key]['name']} selected with model {model}.")
    return llm


def create_llm_vision(gemini_key=None, model=None, temperature=None, max_tokens=None, top_p=None):
    if not model:
        model = google_models[google_models_get_default_for_vision()]
    if not gemini_key:
        gemini_key = randomly_select_account(gemini_vision_accounts)
    if gemini_vision_accounts[gemini_key]['vision_instance']:
        print(f"{gemini_key}/{gemini_vision_accounts[gemini_key]['name']} reused with model {model}.")
        return gemini_vision_accounts[gemini_key]['vision_instance']

    llm = GoogleGenerativeAI(
        model = model,
        # temperature = temperature if temperature is not None else gemini_vision_accounts[gemini_key]['temperature'],
        temperature = temperature if temperature is not None else all_accounts['temperature'],
        google_api_key = dekripsi(gemini_vision_accounts[gemini_key]['key']),
        verbose = True,
        # max_output_tokens = max_tokens if max_tokens is not None else gemini_vision_accounts[gemini_key]['max_tokens'],
        max_output_tokens = max_tokens if max_tokens is not None else all_accounts['max_output_tokens'],
        top_p = top_p if top_p is not None else all_accounts['top_p'],
        convert_system_message_to_human = True
    )
    gemini_vision_accounts[gemini_key]['vision_instance'] = llm
    print(f"{gemini_key}/{gemini_vision_accounts[gemini_key]['name']} selected with model {model}.")
    return llm


def invoke_llm_vision_chat_by_url(user_prompt, image_url="https://picsum.photos/seed/picsum/200/300", model=None, verbose=False):
    llm = create_llm_vision_chat(model=model)
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": user_prompt,
            },  # You can optionally provide text parts
            {
                "type": "image_url",
                "image_url": image_url
            },
        ]
    )
    result = llm.invoke([message])
    # print(result)
    if isinstance(result, AIMessage):
        result = result.content
        if verbose:
            result += '\n\nUsage:\n' + json.dumps(result.response_metadata, indent=2)
        # + '\n\nUsage:\n' + json.dumps(result.response_metadata, indent=2)
    return result


def invoke_llm_vision_chat_by_screen_capture(
    user_prompt,
    base_folder=None,
    image_file=None,
    model=None,
    wait_alert=True,
    verbose=True,
):
    from schnell.app.dirutils import joinhere, joiner, dirname, normy
    from schnell.app.autoutils import alert
    from schnell.app.fileutils import file_name_timestamped
    from schnell.app.ocrutils import take_screenshot, image_pil
    from schnell.app.windowsutils import minimize_terminal

    if all_accounts['minimize_window_before_vision']:
        minimize_terminal()

    if wait_alert:
        alert(f"Siapkan diri untuk ambil gambar dan disimpan di {base_folder}", "Click to continue")
    if not base_folder:
        base_folder = os.getcwd()
    if not image_file:
        image_file = file_name_timestamped('invoke_llm_vision_chat_by_screen_capture_gemini.png')
        filepath = joiner(base_folder, image_file)
        # buat screenshot jk gak specify image_file
        image_url = image_pil(take_screenshot(filepath))
    else:
        # jk specify image_file, gunakan langsung utk di-PIL-kan
        filepath = joiner(base_folder, image_file)
        image_url = image_pil(filepath)

    llm = create_llm_vision_chat(model=model)
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": user_prompt,
            },  # You can optionally provide text parts
            {
                "type": "image_url",
                "image_url": image_url
            },
        ]
    )
    result = llm.invoke([message])
    # print(result)
    if isinstance(result, AIMessage):
        result = result.content
        # if with_usage:
        #     result = '\n*** Usage:\n' + json.dumps(result.response_metadata, indent=2) + f"\n{'*'*10}\n" + result.content
        if verbose:
            result += '\n\nUsage:\n' + json.dumps(result.response_metadata, indent=2)
    return result


# https://python.langchain.com/docs/integrations/chat/google_generative_ai
# TODO: cari contoh baca bytes...
# Multimodal support
# To provide an image, pass a human message with contents of type List[dict],
# where each dict contains either an image value (type of image_url) or a text (type of text) value.
# The value of image_url can be any of the following:
# A public image URL
# An accessible gcs file (e.g., “gcs://path/to/file.png”)
# A local file path <= kita coba ini
# A base64 encoded image (e.g., data:image/png;base64,abcd124)
# A PIL image <= kita coba ini

# Gemini Prompting FAQs
# As of the time this doc was written (2023/12/12), Gemini has some restrictions on the types and structure of prompts it accepts. 
# Specifically:
# When providing multimodal (image) inputs, you are restricted to at most 1 message of “human” (user) type. 
#       You cannot pass multiple messages (though the single human message may have multiple content entries)
# System messages are not accepted.
# For regular chat conversations, messages must follow the human/ai/human/ai alternating pattern. 
#       You may not provide 2 AI or human messages in sequence.
# Message may be blocked if they violate the safety checks of the LLM. 
#       In this case, the model will return an empty response.
def test_create_llm_vision_chat(user_prompt, image_url="https://picsum.photos/seed/picsum/200/300"):
    llm = create_llm_vision_chat()
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": user_prompt,
            },  # You can optionally provide text parts
            {
                "type": "image_url",
                "image_url": image_url
            },
        ]
    )
    result = llm.invoke([message])
    # print(result)
    return result


def instantiate_all_as_chats():
    for key in gemini_accounts:
        create_llm_chat(gemini_key=key)


def invoker(query, index=0, choice=['chat', 'once', 'vision']):
    choose = choice[index]
    if choose == 'chat':
        return create_llm_chat().invoke(query)
    elif choose == 'once':
        return create_llm().invoke(query)
