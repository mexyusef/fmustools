# https://python.langchain.com/docs/integrations/llms/together
# pip install --user --upgrade --quiet langchain-together
import json, requests
import os, sys

from langchain_together import Together
from openai import OpenAI

# from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)

if __name__ == "__main__":
    sys.path.insert(0, r"c:\users\usef\work\sidoarjo")

from schnell.app.llmutils.langchainutils.llms import (
    together_accounts,
    randomly_select_account,
)
from schnell.app.printutils import indah4
from schnell.app.cryptoutils import dekripsi

# together_models = {
#     # https://docs.together.ai/docs/quickstart
#     # https://docs.together.ai/docs/inference-models
#     "deepseek": "deepseek-ai/deepseek-coder-33b-instruct",  # 33b, 16k
#     "codellama70b": "codellama/CodeLlama-70b-Python-hf",  # 70b, 4k
#     "codellama34b": "codellama/CodeLlama-34b-Python-hf",  # 34b, 16k
#     "phind": "Phind/Phind-CodeLlama-34B-v2",  # 34b, 16k
#     "wizard": "WizardLM/WizardCoder-Python-34B-V1.0",  # 34b, 8k
#     "mistral7b": "mistralai/Mistral-7B-Instruct-v0.2",  # 7b, 32k
#     "mixtral7b": "mistralai/Mixtral-8x7B-Instruct-v0.1",  # 7b, 32k
#     "redpajama": "togethercomputer/RedPajama-INCITE-7B-Base",  # 7b, 2k
#     # '4_preview': "gpt-4-turbo-preview",
# }

# To switch to using the Together API,
# simply switch out the API key to your Together API key,
# base_url to https://api.together.xyz/v1, and model to one of our chat models.
# https://docs.together.ai/docs/inference-models

# https://api.together.xyz/v1/completions
# https://docs.together.ai/reference/completions
together_image_models = {
    # Prompt Hero	    Openjourney v4	        prompthero/openjourney
    # Runway ML	        Stable Diffusion 1.5	runwayml/stable-diffusion-v1-5
    # SG161222	        Realistic Vision 3.0	SG161222/Realistic_Vision_V3.0_VAE
    # Stability AI	    Stable Diffusion 2.1	stabilityai/stable-diffusion-2-1
    # Stability AI	    Stable Diffusion XL 1.0	stabilityai/stable-diffusion-xl-base-1.0
    # Wavymulder	    Analog Diffusion	    wavymulder/Analog-Diffusion
}

# https://api.together.xyz/v1/chat/completions
# https://docs.together.ai/reference/chat-completions

# Exception Together received an invalid payload: {
# "error":{
# "message":
# "Input validation error: 
# `inputs` tokens + `max_new_tokens` must be <= 4097. 
# Given: 240 `inputs` tokens and 4096 `max_new_tokens`",
# "type":"invalid_request_error",
# "param":"max_tokens",
# "code":null}
# }
# gak bs kasih 4096 tokens
MAX_TOKENS = 2048

together_chat_models = {
    "deepseek"      : {
        "model"     : "deepseek-ai/deepseek-coder-33b-instruct",  # 33b, 16k
        "temperature": 0.1,
        "max_tokens": MAX_TOKENS, # 16384,
    },
    "mistral7b"     : {
        "model"     : "mistralai/Mistral-7B-Instruct-v0.2",  # 7b, 32k
        "temperature": 0.1,
        "max_tokens": MAX_TOKENS, # 32768,
    },
    "mixtral7b"     : {
        "model"     : "mistralai/Mixtral-8x7B-Instruct-v0.1",  # 7b, 32k
        "temperature": 0.1,
        "max_tokens": MAX_TOKENS, # 32768,
    },
}

# https://api.together.xyz/v1/completions
# https://docs.together.ai/reference/completions
together_language_models = {}
# https://api.together.xyz/v1/completions
# https://docs.together.ai/reference/completions

together_code_models = {
    "codellama70b"  : {
        "model"     : "codellama/CodeLlama-70b-Python-hf",  # 70b, 4k
        "max_tokens": MAX_TOKENS,
        "temperature": 0.0,
        "stop"      : ["</s>"]
    },
    "codellama34b"  : {
        "model"     : "codellama/CodeLlama-34b-Python-hf",  # 34b, 16k
        "max_tokens": MAX_TOKENS, # 16384
        "temperature": 0.0,
        "stop"      : ["</s>"]
    },
    "phind"         : {
        "model"     : "Phind/Phind-CodeLlama-34B-v2",  # 34b, 16k
        "max_tokens": MAX_TOKENS, # 16384
        "temperature": 0.0,
        "stop"      : ["</s>"]
    },
    "wizard"        : {
        "model"     : "WizardLM/WizardCoder-Python-34B-V1.0",  # 34b, 8k
        "max_tokens": MAX_TOKENS, # 8192
        "temperature": 0.0,
        "stop"      : ["</s>"]
    },
}

together_chat_and_code_models = together_chat_models
together_chat_and_code_models.update(together_code_models)

# versi langchain
# https://python.langchain.com/docs/integrations/llms/together
def create_llm_chat(
    together_key=None,
    model=None, # together_chat_and_code_models["mixtral7b"],
    temperature=None,
    max_tokens=None,
):
    if not together_key:
        together_key = randomly_select_account(together_accounts)

    if not model:
        model = randomly_select_account(together_chat_and_code_models)

    if together_accounts[together_key]["instance"]:
        print(f"{together_key}/{together_accounts[together_key]['name']} reused.")
        return together_accounts[together_key]["instance"]

    # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_together\llms.py
    llm = Together(
        together_api_key = dekripsi(together_accounts[together_key]['key']),
        model = together_chat_and_code_models[model]['model'],
        temperature = temperature if temperature is not None else together_chat_and_code_models[model]['temperature'],

        # apa mending kita matikan max_tokens? biar dia ambil paling maksimum???
        # max_tokens=max_tokens if max_tokens else together_chat_and_code_models[model]['max_tokens'],
        # max_tokens=128,
        # top_k=1,
    )
    together_accounts[together_key]["instance"] = llm
    print(f"{together_key}/{together_accounts[together_key]['name']} selected.")
    return llm


def create_llm(  # code
    together_key=None,
    # model=together_models["redpajama"],
    model=None, # together_code_models["mixtral7b"],
    temperature=None,
    max_tokens=None,
):
    if not together_key:
        together_key = randomly_select_account(together_accounts)

    if not model:
        model = randomly_select_account(together_code_models)

    if together_accounts[together_key]["instance"]:
        print(f"{together_key}/{together_accounts[together_key]['name']} reused.")
        return together_accounts[together_key]["instance"]

    llm = Together(
        together_api_key = dekripsi(together_accounts[together_key]['key']),
        model = together_code_models[model]['model'],
        temperature = temperature if temperature is not None else together_code_models[model]['temperature'],
        max_tokens = max_tokens if max_tokens else together_code_models[model]['max_tokens'],
        # max_tokens=128,
        # top_k=1,
    )
    together_accounts[together_key]["instance"] = llm
    print(f"{together_key}/{together_accounts[together_key]['name']} selected.")
    return llm


# versi chat together
def llm_query_openai_chat(
    user_prompt,
    together_key=None,
    model=None, # together_chat_models["mixtral7b"],
    # ini gak specify temp/token/stop etc
    # temperature=0.3,
    # max_tokens=None,
    system_prompt=None, # "You are an expert and helpful assistant.",
):
    """
    https://docs.together.ai/reference/chat-completions
    import requests
    url = "https://api.together.xyz/v1/chat/completions"
    payload = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "stop": ["</s>"]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer eb2fdc71ab7fb8165627ba7b11ea93cf328563f98a7522cbaac602369356a7f8"
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    """
    if not together_key:
        together_key = randomly_select_account(together_accounts)
    if not model:
        model = randomly_select_account(together_chat_models)
    client = OpenAI(
        api_key=together_key,
        base_url="https://api.together.xyz/v1",
    )
    messages = []
    if system_prompt:
        messages += [{
            "role": "system",
            "content": system_prompt,
        }]
    messages += [{
        "role": "user",
        "content": user_prompt,
    }]
    chat_completion = client.chat.completions.create(
        messages = messages,
        # messages=[
        #     {
        #         "role": "system",
        #         "content": system_prompt,
        #     },
        #     {
        #         "role": "user",
        #         "content": user_prompt,
        #     },
        # ],
        model=together_chat_models[model]['model'],
    )
    result = chat_completion.choices[0].message.content
    return result


# versi non-chat code
def llm_query_openai_code(
    user_prompt,
    together_key=None,
    model=None, # together_code_models["wizard"]["model"],
    # temperature=0.3,
    max_tokens=None,
    stop=None,
):
    if not together_key:
        together_key = randomly_select_account(together_accounts)
    if not model:
        model = randomly_select_account(together_code_models)
    payload = {
        "model": together_code_models[model]["model"], # "mistralai/Mixtral-8x7B-v0.1",
        "prompt": user_prompt,
        "max_tokens": max_tokens if max_tokens else together_code_models[model]["max_tokens"],
        "stop": stop if stop else together_code_models[model]["stop"]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {together_key}"
    }
    url = "https://api.together.xyz/v1/completions"
    response = requests.post(url, json=payload, headers=headers)
    result = response.text
    return result


# versi image
def llm_query_openai_image(
    user_prompt,
    together_key=None,
    model=None, # together_image_models["wizard"]["model"],
    # temperature=0.3,
    max_tokens=None,
    stop=None,
):
    if not together_key:
        together_key = randomly_select_account(together_accounts)
    if not model:
        model = randomly_select_account(together_image_models)
    payload = {
        "model": together_image_models[model]["model"], # "mistralai/Mixtral-8x7B-v0.1",
        "prompt": user_prompt,
        "max_tokens": max_tokens if max_tokens else together_image_models[model]["max_tokens"],
        "stop": stop if stop else together_image_models[model]["stop"]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {together_key}"
    }
    url = "https://api.together.xyz/v1/completions"
    response = requests.post(url, json=payload, headers=headers)
    result = response.text
    return result


# llm = Together(
#     model="togethercomputer/RedPajama-INCITE-7B-Base",
#     temperature=0.7,
#     max_tokens=128,
#     top_k=1,
#     # together_api_key="..."
# )

# input_ = """You are a teacher with a deep knowledge of machine learning and AI.
# You provide succinct and accurate answers. Answer the following question:

# What is a large language model?"""
# print(llm.invoke(input_))

def instantiate_all_as_chats():
    for key in together_accounts.keys():
        create_llm_chat(together_key=key)


def invoker(query, index=0, choice=['chat', 'once', 'vision']):
    choose = choice[index]
    if choose == 'chat':
        return create_llm_chat().invoke(query)
    elif choose == 'once':
        return create_llm().invoke(query)


def test_create_llm_chat():
    question = "What's the difference between Nextjs 14 App router and pages router? "
    template = """Question: {question}

    Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)
    # repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
    llm = create_llm_chat()

    # https://python.langchain.com/docs/versions/migrating_chains/llm_chain/
    # llm_chain = LLMChain(prompt=prompt, llm=llm)
    llm_chain = ChatPromptTemplate.from_messages([("user", prompt)],) | llm | StrOutputParser()

    result = llm_chain.invoke(question)
    # print(result)
    if isinstance(result, dict):
        for k,v in result.items():
            indah4(k, warna='cyan')
            indah4(v, warna='green')
    elif isinstance(result, (AIMessage, HumanMessage)):
        indah4(result.content, warna='green')
    else:
        indah4(result, warna='green')


if __name__ == '__main__':
    test_create_llm_chat()
