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

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
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
# from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

if __name__ == '__main__':
    sys.path.insert(0, r'c:\users\usef\work\sidoarjo')
# from schnell.app.llmutils.langchainutils.llms import openai_accounts, randomly_select_account
from schnell.app.llmutils.langchainutils.llm_config import openai_accounts, openai_vision_accounts
from schnell.app.llmutils.langchainutils.utils import randomly_select_account
from schnell.app.printutils import indah4
from schnell.app.cryptoutils import dekripsi
from schnell.app.llmutils.langchainutils.llm_config import all_accounts
# The class `langchain_community.chat_models.openai.ChatOpenAI` was deprecated in langchain-community 0.0.10 and will be removed in 0.2.0. 
# An updated version of the class exists in the langchain-openai package and should be used instead. 
# To use it run `pip install -U langchain-openai` and import as `from langchain_openai import ChatOpenAI`.
# from langchain.chat_models import ChatOpenAI

# https://python.langchain.com/docs/integrations/llms/openai
# https://python.langchain.com/docs/get_started/quickstart
from schnell.app.llmutils.langchainutils.llms import with_memory
from schnell.app.llmutils.langchainutils.llm_config import openai_models, openai_models_get_default, openai_models_get_default_for_vision


def create_llm_chat(model=None, temperature=None, openai_key=None, max_tokens=None, top_p=None):
    if not model:
        model = openai_models[openai_models_get_default()]
    if not openai_key:
        openai_key = randomly_select_account(openai_accounts)

    if openai_key.startswith('sk-'):
        real_openai_key = openai_key
    else:
        real_openai_key = dekripsi(openai_accounts[openai_key]['key'])
        if openai_accounts[openai_key]['instance']:
            print(f"{openai_key}/{openai_accounts[openai_key]['name']} reused.")
            return openai_accounts[openai_key]['instance']

    # os.environ["OPENAI_API_KEY"] = ''

    llm = ChatOpenAI(
        openai_api_key = real_openai_key,
        model = model,
        temperature = (
            temperature if temperature is not None
            else all_accounts['temperature']
            # (
            #     openai_accounts[openai_key]['temperature']
            #     if not openai_key.startswith('sk-')
            #     else 0.01
            # )
        ),
        # max_tokens = max_tokens if max_tokens is not None else openai_accounts[openai_key]['max_tokens'],
        max_tokens = max_tokens if max_tokens is not None else all_accounts['max_output_tokens'],
        top_p = top_p if top_p is not None else all_accounts['top_p'],
    )

    if not openai_key.startswith('sk-'):
        openai_accounts[openai_key]['instance'] = llm
        print(f"{openai_key}/{openai_accounts[openai_key]['name']} selected.")
    return llm


# https://python.langchain.com/docs/integrations/llms/openai
def create_llm(model=None, temperature=None, openai_key=None, max_tokens=None, top_p=None):
    if not model:
        model = openai_models[openai_models_get_default()]
    if not openai_key:
        openai_key = randomly_select_account(openai_accounts)
    if openai_accounts[openai_key]['instance']:
        print(f"{openai_key}/{openai_accounts[openai_key]['name']} reused.")
        return openai_accounts[openai_key]['instance']
    # os.environ["OPENAI_API_KEY"] = ''
    llm = OpenAI(
        openai_api_key = dekripsi(openai_accounts[openai_key]['key']),
        model = model,
        # temperature = temperature if temperature is not None else openai_accounts[openai_key]['temperature'],
        temperature = temperature if temperature is not None else all_accounts['temperature'],
        # max_tokens = max_tokens if max_tokens is not None else openai_accounts[openai_key]['max_tokens'],
        max_tokens = max_tokens if max_tokens is not None else all_accounts['max_output_tokens'],
        top_p = top_p if top_p is not None else all_accounts['top_p'],
    )
    openai_accounts[openai_key]['instance'] = llm
    print(f"{openai_key}/{openai_accounts[openai_key]['name']} selected.")
    return llm

# https://github.com/topics/gpt4o?o=desc&s=forks
# https://github.com/topics/gpt4o?o=asc&s=forks
def create_llm_vision_chat(openai_key=None, model=None, temperature=None, max_tokens=None, top_p=None):
    if not model:
        model = openai_models[openai_models_get_default_for_vision()]
    if not openai_key:
        openai_key = randomly_select_account(openai_vision_accounts)
    if openai_vision_accounts[openai_key]['vision_instance']:
        print(f"{openai_key}/{openai_vision_accounts[openai_key]['name']} reused with model {model}.")
        return openai_vision_accounts[openai_key]['vision_instance']
    print(f"create_llm_vision_chat, model={model}.")
    llm = ChatOpenAI(
        model = model,
        # temperature = temperature if temperature is not None else openai_vision_accounts[openai_key]['temperature'],
        temperature = temperature if temperature is not None else all_accounts['temperature'],
        openai_api_key = dekripsi(openai_vision_accounts[openai_key]['key']),
        # max_tokens = max_tokens if max_tokens is not None else openai_vision_accounts[openai_key]['max_tokens'],
        max_tokens = max_tokens if max_tokens is not None else all_accounts['max_output_tokens'],
        top_p = top_p if top_p is not None else all_accounts['top_p'],
        # verbose = True,
        # max_output_tokens = 4096,
        # convert_system_message_to_human = True
    )
    openai_vision_accounts[openai_key]['vision_instance'] = llm
    print(f"{openai_key}/{openai_vision_accounts[openai_key]['name']} selected with model {model}.")
    return llm


def create_llm_vision(openai_key=None, model=None, temperature=None, max_tokens=None, top_p=None):
    if not model:
        model = openai_models[openai_models_get_default_for_vision()]
    if not openai_key:
        openai_key = randomly_select_account(openai_vision_accounts)
    if openai_vision_accounts[openai_key]['vision_instance']:
        print(f"{openai_key}/{openai_vision_accounts[openai_key]['name']} reused with model {model}.")
        return openai_vision_accounts[openai_key]['vision_instance']

    llm = OpenAI(
        model = model,
        # temperature = temperature if temperature is not None else openai_vision_accounts[openai_key]['temperature'],
        temperature = temperature if temperature is not None else all_accounts['temperature'],
        openai_api_key = dekripsi(openai_vision_accounts[openai_key]['key']),
        # max_tokens = max_tokens if max_tokens is not None else openai_vision_accounts[openai_key]['max_tokens'],
        max_tokens = max_tokens if max_tokens is not None else all_accounts['max_output_tokens'],
        top_p = top_p if top_p is not None else all_accounts['top_p'],
        # verbose = True,
        # max_output_tokens = 4096,
        # convert_system_message_to_human = True
    )
    openai_vision_accounts[openai_key]['vision_instance'] = llm
    print(f"{openai_key}/{openai_vision_accounts[openai_key]['name']} selected with model {model}.")
    return llm


# # ini gagal, mungkin perlu jalankan manual/local
# # GROQ_PROXY = 'https://groqcall.ai/proxy/groq'
# # GROQ_PROXY = "https://groqcall.ai/proxy/groq/v1/chat/completions"
# GROQ_PROXY = 'https://groqcall.ai/proxy/groq/v1'
# # from llm_gemini import gemini_accounts
# def create_llm_chat_by_groq(model='mixtral-8x7b-32768', proxy=GROQ_PROXY, key=''):
#     os.environ["OPENAI_API_KEY"] = key
#     llm = ChatOpenAI(model=model, openai_api_base=proxy)  # OPENAI_API_BASE
#     # llm = ChatOpenAI(model=model, openai_proxy=proxy)  # OPENAI_PROXY
#     res = llm.invoke("What's the difference between C++ RAII concept with Rust model?")
#     print(res)

def simple_query(query="What is implicit in Scala? what's the equivalent in Python?"):
    llm = create_llm_chat()
    res = llm.invoke(query)
    result = res.content
    return result


def test_query():
    llm = create_llm_chat()
    res = llm.invoke("What is implicit in Scala? what's the equivalent in Python?")
    # content='In Scala, implicit is a feature that allows the compiler to automatically insert certain values or conversions into the code at compile-time. It is used to provide a way to define default values, inject dependencies, or enable type conversions without explicitly specifying them.\n\nThe equivalent concept in Python is called "magic methods" or "dunder methods" (short for double underscore methods). These methods allow you to define how objects of a class behave in certain situations, such as arithmetic operations, comparisons, or attribute access. They are automatically called by the interpreter in response to specific events or operations. While not exactly the same as Scala\'s implicit, magic methods provide similar functionality in Python.'
    # response_metadata={
    #   'token_usage': {'completion_tokens': 133, 'prompt_tokens': 20, 'total_tokens': 153},
    #   'model_name': 'gpt-3.5-turbo-16k',
    #   'system_fingerprint': None,
    #   'finish_reason': 'stop',
    #   'logprobs': None
    # }
    print(res.content)


def simple_chain(
    user_prompt="how can langsmith help with testing?",
    openai_key=None,
    system_prompt="You are world class technical documentation writer."
):
    llm = create_llm_chat(openai_key=openai_key)
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "{input}")  # input adlh nama variable yg akan direplaced oleh user_prompt
    ])
    # chain = prompt | llm
    # chain.invoke({"input": "how can langsmith help with testing?"})
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    res = chain.invoke({"input": user_prompt})
    return res


def simple_chain_create_book():
    """
    """
    print("START.")
    res = simple_chain("""You are tasked to write a book about *Advanced Rust* with length approximately 400 pages.
    Please provide the table of contents for the book.""",
    )
    print(res)
    print("FINISH.")


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
    if isinstance(result, AIMessage):
        result = result.content
        if verbose:
            result += '\n\nUsage:\n' + json.dumps(result.response_metadata, indent=2)
    return result


# # Convert the PIL image to base64
# image_url = pil_image_to_base64(image_pil(filepath))

# Exception Error code: 404 -
# {
#     'error': {
#         'message': 'The model `gpt-4o-2024-05-13` does not exist or you do not have access to it.',
#         'type': 'invalid_request_error',
#         'param': None,
#         'code': 'model_not_found'
#     }
# }



import base64
from io import BytesIO
from schnell.app.dirutils import joinhere, joiner, dirname, normy
from schnell.app.autoutils import alert
from schnell.app.fileutils import file_name_timestamped
from schnell.app.ocrutils import take_screenshot, image_pil
from schnell.app.windowsutils import minimize_terminal
from schnell.app.imageutils.codec import encode_image_to_base64

# def encode_image_to_base64(filepath):
#     with open(filepath, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# # Use the encoded base64 string instead of the file path
# image_url = encode_image_to_base64(filepath)

def pil_image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')


def invoke_llm_vision_chat_by_screen_capture(
    user_prompt,
    base_folder=None,
    image_file=None,
    # model="4o",
    model=None,
    openai_key="openai_9",
    wait_alert=True,
    verbose=False,
):

    if all_accounts['minimize_window_before_vision']:
        minimize_terminal()
        if wait_alert:
            alert(f"Siapkan diri untuk ambil gambar dan disimpan di {base_folder}", "Click to continue")

    llm = create_llm_vision_chat(
        openai_key=openai_key,
        model=model
    )
    result = None

    if not base_folder:
        base_folder = os.getcwd()

    if not image_file:
        image_file = file_name_timestamped('invoke_llm_vision_chat_by_screen_capture_openai.png')

        filepath = joiner(base_folder, image_file)
        # image_url = image_pil(take_screenshot(filepath))
        image_url = take_screenshot(filepath)
        # message = HumanMessage(
        #     content=[
        #         {
        #             "type": "text",
        #             "text": user_prompt,
        #         },  # You can optionally provide text parts
        #         {
        #             "type": "image_url",
        #             "image_url": encode_image_to_base64(image_url)
        #         },
        #     ]
        # )
        # result = llm.invoke([message])
    else:
        # jk specify image_file, gunakan langsung utk di-PIL-kan
        filepath = joiner(base_folder, image_file)
        # image_url = encode_image_to_base64(filepath)
        image_url = filepath
        print('\n*** invoke_llm_vision_chat_by_screen_capture image_url:', image_url)

        # # Pass the image file directly to the API
        # with open(image_url, "rb") as image_file:
        #     # llm = create_llm_vision_chat(openai_key=openai_key, model=model)
        #     message = HumanMessage(
        #         content=[
        #             {
        #                 "type": "text",
        #                 "text": user_prompt,
        #             },
        #             {
        #                 "type": "image_url",
        #                 "image_url": image_file
        #             },
        #         ]
        #     )
        #     result = llm.invoke([message])
    # Encode the image file to base64
    base64_image = encode_image_to_base64(image_url)
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": user_prompt,
            },
            {
                # raise self._make_status_error_from_response(err.response) from None
                # openai.BadRequestError: Error code: 400 - {'error': {'message': "Invalid value: 'image'.
                # Supported values are: 'text', 'image_url', 'audio_url', and 'refusal'.", 'type': 'invalid_request_error', 'param': 'messages[0].content[1].type', 'code': 'invalid_value'}}
                "type": "image_url",
                # "image_url": base64_image  # Send the base64-encoded image data
                # https://python.langchain.com/v0.2/docs/how_to/multimodal_inputs/
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            },
        ]
    )
    result = llm.invoke([message])

    # https://platform.openai.com/docs/guides/vision?lang=python
    # https://platform.openai.com/docs/guides/vision
    # https://python.langchain.com/v0.2/docs/how_to/multimodal_inputs/
    # message = HumanMessage(
    #     content=[
    #         {"type": "text", "text": "are these two images the same?"},
    #         {"type": "image_url", "image_url": {"url": image_url}},
    #         {"type": "image_url", "image_url": {"url": image_url}},
    #     ],
    # )
    # response = model.invoke([message])
    # print(response.content)


    if isinstance(result, AIMessage):
        result = result.content
        if verbose:
            result += '\n\nUsage:\n' + json.dumps(result.response_metadata, indent=2)

    return result


def instantiate_all_as_chats():
    for key in openai_accounts.keys():
        create_llm_chat(openai_key=key)


def invoker(query, index=0, choice=['chat', 'once', 'vision']):
    choose = choice[index]
    if choose == 'chat':
        return create_llm_chat().invoke(query)
    elif choose == 'once':
        return create_llm().invoke(query)


if __name__ == '__main__':
    # test_query()
    simple_chain_create_book()
