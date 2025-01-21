# from schnell.app.llmutils.langchainutils.llm_config import *
from .cohere_accounts import cohere_accounts
from .gemini_accounts import gemini_accounts
from .groq_accounts import groq_accounts
from .nvidia_accounts import nvidia_accounts
from .openai_accounts import openai_accounts
from .claude_accounts import claude_accounts
from .together_accounts import together_accounts
from .gooseai_accounts import gooseai_accounts
from .replicate_accounts import replicate_accounts
from .openrouter_accounts import openrouter_accounts
from .huggingface_accounts import huggingface_accounts
from .clarifyai_accounts import clarifyai_accounts

# from schnell.app.llmutils.langchainutils.llm_config import hyperbolic_accounts
from .hyperbolic_accounts import hyperbolic_accounts

import copy
gemini_vision_accounts = copy.deepcopy(gemini_accounts)
openai_vision_accounts = copy.deepcopy(openai_accounts)

# from schnell.app.llmutils.langchainutils.llm_config import llm_models
llm_models = {

    'cohere_models': {
        'command'       : "command",
        'command-r'     : "command-r",
        'llama2'        : "llama2-70b-4096",
    },
    'cohere_models:default' : 'command',

    # https://ai.google.dev/gemini-api/docs/models/gemini
    # Latest: gemini-1.5-flash-latest
    # Latest stable: gemini-1.5-flash
    # Stable:
    # gemini-1.5-flash-001
    # gemini-1.5-flash-002
    # https://ai.google.dev/gemini-api/docs/models/experimental-models
    # gemini-1.5-flash-8b-exp-0924
    # gemini-1.5-flash-8b-exp-0827
    # gemini-1.5-flash-exp-0827
    # model>-<generation>-<variation>-latest
    # generation: 1.0, 1.5
    # variation: pro, flash
    'gemini_models': {
        # https://x.com/OfficialLoganK/status/1795595681593487400/photo/1
        # ranking
        #     gpt-4o-2024-05-13
        # gemini-1.5-pro-api-0514
        # gemini-advanced-0514
        # gemini-1.5-pro-api-0409-preview
        #     gpt-4-turbo-2024-04-09
        #     gpt-4-1106-preview
        #     gpt-4-0125-preview
        # gemini-1.5-flash-api-0514
        # gemini-pro

        'gemini-pro'        : "gemini-pro",
        'gemini-vision'     : "gemini-pro-vision",

        # https://github.com/AnubhavGupta11/Hands-On-Gemini-Flash-Gemini-pro-vision/blob/main/Gemini-Flash.py
        'gemini-new'        : 'gemini-1.5-flash-exp-0827',
        'gemini-flash'      : "gemini-1.5-flash-latest",  # "gemini-1.5-flash"

        # langchain_google_genai.chat_models.ChatGoogleGenerativeAIError: Invalid argument provided to Gemini: 400 Add an image to use models/gemini-pro-vision, or switch your model to a text model.
        # 'correct-vision': "models/gemini-pro-vision",

        # https://www.kaggle.com/code/prathameshbang/gemini-1-5-pro-api-starter-notebook
        # import google.generativeai as genai
        # genai.configure(api_key = apiKey)
        # model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
        # newsarticles = ""
        # for filename in os.listdir(directory):
        #     file = open(f'{directory}{filename}', "r")
        #     newsarticles = f'{newsarticles}\n{file.read()}'
        # prompt = f'Read the following compilation of BBC news articles: {newsarticles}. Now tell me how much UK Coal had in losses in 2004.'
        # response = model.generate_content(prompt)
        # to_markdown(response.text)
        # model.count_tokens(prompt)
        'gemini-15'         : "models/gemini-1.5-pro-latest",

        'correct-vision'    : "gemini-pro-vision",
        'bison'             : "models/text-bison-001",

        'embedding-001'     : "models/embedding-001",
    },
    # 'gemini_models:default'             : 'gemini-pro',
    'gemini_models:default'             : 'gemini-flash',
    # 'gemini_models:vision:default'      : 'gemini-vision',
    'gemini_models:vision:default'      : 'gemini-flash',
    'gemini_models:embedding:default'   : 'embedding-001',


    'groq_models': {
        # https://console.groq.com/docs/models
        # sementara hanya paying customer
        "llama3_405"    : "llama-3.1-405b-reasoning",
        "llama3_70"     : "llama-3.1-70b-versatile",
        "llama3_8"      : "llama-3.1-8b-instant",

        "llama3_groq"   : "llama3-groq-70b-8192-tool-use-preview",

        'mixtral'       : "mixtral-8x7b-32768",
        'llama3'        : "llama3-8b-8192",
        'llama370b'     : "llama3-70b-8192",
        'gemma'         : "gemma-7b-it",
        'llama2'        : "llama2-70b-4096",
        # '4_preview'   : "gpt-4-turbo-preview",
    },
    'groq_models:default'   : 'mixtral',

    'huggingface_models': {
        'mistral'           : "mistralai/Mistral-7B-Instruct-v0.2",
        # 'mixtral'           : "mixtral-8x7b-32768",
        # 'llama2'            : "llama2-70b-4096",
        # '4_preview'         : "gpt-4-turbo-preview",
    },
    'huggingface_models:default': 'mistral',

    # https://platform.openai.com/docs/models
    'openai_models': {
        '35'            : 'gpt-3.5-turbo',
        '35_16k'        : 'gpt-3.5-turbo-16k',
        '35_1106'       : "gpt-3.5-turbo-1106",
        '35_0613'       : "gpt-3.5-turbo-0613",
        '35_instruct'   : "gpt-3.5-turbo-instruct",
        '4o_mini'       : 'gpt-4o-mini',    # 16k output tokens
        '4o'            : 'gpt-4o',         # 4k output tokens
        # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\screenshot2code\backend\llm.py
        '4o_preview'    : "gpt-4o-2024-05-13",

        '4_preview'     : "gpt-4-turbo-preview",
        "4_125"         : "gpt-4-0125-preview",

        # "gpt-4",
        # "gpt-4-0314",
        # "gpt4",
        # "gpt-4-32k",
        # "gpt-4-32k-0314",
        # "gpt-4-32k-v0314"
    },
    # 'openai_models:default'             : '35_16k',
    'openai_models:default'             : '4o_mini',
    # 'openai_models:vision:default'      : '4o',
    'openai_models:vision:default'      : '4o_mini',


    'together_models': {
        "codellama70b"  : "codellama/CodeLlama-70b-Python-hf",  # 70b, 4k
        "codellama34b"  : "codellama/CodeLlama-34b-Python-hf",  # 34b, 16k
        "phind"         : "Phind/Phind-CodeLlama-34B-v2",  # 34b, 16k
        "wizard"        : "WizardLM/WizardCoder-Python-34B-V1.0",  # 34b, 8k

        "deepseek"      : "deepseek-ai/deepseek-coder-33b-instruct",  # 33b, 16k
        "mistral7b"     : "mistralai/Mistral-7B-Instruct-v0.2",  # 7b, 32k
        "mixtral7b"     : "mistralai/Mixtral-8x7B-Instruct-v0.1",  # 7b, 32k
    },
    'together_models:default' : 'codellama70b',
}

# from schnell.app.llmutils.langchainutils.llm_config import invoke_all
# C:\work\ciledug\ciledug\fmusperintah\main.py
# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\llms\invoker.py
# invoke_llm_all
# C:\work\ciledug\ciledug\fmusperintah\keybinders\pageup.py
# peta_operasi = {
#     'P'             : 'prompt for gemini, openai, together, cohere',
# }
# def handle_operasi(llm_name, current_line, kunci, nilai):
#     elif kunci == 'P':
#         res = invoke_llm_all(skeleton_code_prompt)
invoke_all = {
    'gemini'        : 1,
    'groq'          : 1,
    'cohere'        : 1,

    'openai'        : 0,
    'huggingface'   : 0,
    'together'      : 0,

    'clarifyai'     : 0,
    'nvidia'        : 0,
    'replicate'     : 0,

    'gemini_vision'        : 0,
    'openai_vision'        : 0,
}

# from schnell.app.llmutils.langchainutils.llm_config import gemini_accounts, groq_accounts
# from schnell.app.llmutils.langchainutils.llm_config import all_accounts
all_accounts = {
    # all_accounts['active']
    'active'        : 'gemini',
    # 'active'        : 'groq',
    'secondary_active' : 'groq',

    'code_query'    : 'groq',
    'error_query'   : 'groq',

    'temperature'           : 0.2,
    'max_output_tokens'     : 4096,
    'top_p'                 : 0.9,
    'recursion_limit'       : 75,

    # all_accounts['minimize_window_before_vision']
    'minimize_window_before_vision': False,

    # https://python.langchain.com/v0.2/docs/integrations/tools/
    # https://python.langchain.com/v0.2/docs/integrations/tools/brave_search/
    # https://python.langchain.com/v0.2/docs/integrations/tools/exa_search/
    # https://python.langchain.com/v0.2/docs/integrations/tools/google_serper/
    # https://python.langchain.com/v0.2/docs/integrations/tools/searchapi/
    # https://python.langchain.com/v0.2/docs/integrations/tools/searx_search/
    # https://python.langchain.com/v0.2/docs/integrations/tools/serpapi/
    # https://python.langchain.com/v0.2/docs/integrations/tools/you/
    # all_accounts['search_tool']
    'search_tool': 'tavily',
    # 'search_tool': 'duckduckgo',
    # 'search_tool': 'duckduckgo_results',
    # 'search_tool': 'googlecustomsearch',


    # ini konfigurasi declang utk pretty print, seharusnya tdk ditempatkan di sini
    # kita pake misalnya di C:\users\usef\work\sidoarjo\schnell\app\transpiler\frontend\main.py
    # all_accounts['declang_verbose']
    'declang_verbose': True,

    'mode'          : 'random',
    'mode:list'     : ['random', 'fixed', 'roundrobin'],
    'fixed'         : 'random',
    'roundrobin'    : 'random',
}

# from schnell.app.llmutils.langchainutils.llm_config import change_active_model
# elif text.startswith("models:active="):
#     nilai = text.removeprefix("models:active=").strip()
#     if nilai and nilai in invoke_all.keys():
#         change_active_model(nilai)
#         print_json(all_accounts)
def change_active_model(model):
    if model not in invoke_all:
        print(f"{model} not in {invoke_all.keys()}")
        return
    all_accounts['active'] = model

# from schnell.app.llmutils.langchainutils.llm_config import google_models_get_default
google_models = llm_models['gemini_models']
def google_models_get_default(set_model=None):
    if set_model and set_model in google_models:
        llm_models['gemini_models:default'] = set_model
        return set_model
    return llm_models['gemini_models:default']

# from schnell.app.llmutils.langchainutils.llm_config import gemini_models_get_default
gemini_models = llm_models['gemini_models']
def gemini_models_get_default(set_model=None):
    if set_model and set_model in gemini_models:
        llm_models['gemini_models:default'] = set_model
        return set_model
    return llm_models['gemini_models:default']

openai_models = llm_models['openai_models']
def openai_models_get_default(set_model=None):
    if set_model and set_model in openai_models:
        llm_models['openai_models:default'] = set_model
        return set_model
    return llm_models['openai_models:default']

groq_models = llm_models['groq_models']
def groq_models_get_default(set_model=None):
    if set_model and set_model in groq_models:
        llm_models['groq_models:default'] = set_model
        return set_model
    return llm_models['groq_models:default']

cohere_models = llm_models['cohere_models']
def cohere_models_get_default(set_model=None):
    if set_model and set_model in cohere_models:
        llm_models['cohere_models:default'] = set_model
        return set_model
    return llm_models['cohere_models:default']

together_models = llm_models['together_models']
def together_models_get_default(set_model=None):
    if set_model and set_model in together_models:
        llm_models['together_models:default'] = set_model
        return set_model
    return llm_models['together_models:default']

huggingface_models = llm_models['huggingface_models']
def huggingface_models_get_default(set_model=None):
    if set_model and set_model in huggingface_models:
        llm_models['huggingface_models:default'] = set_model
        return set_model
    return llm_models['huggingface_models:default']

def gemini_models_get_default_for_vision(set_model=None):
    if set_model and set_model in google_models:
        llm_models['gemini_models:vision:default'] = set_model
        return set_model
    return llm_models['gemini_models:vision:default']
google_models_get_default_for_vision = gemini_models_get_default_for_vision

def openai_models_get_default_for_vision(set_model=None):
    if set_model and set_model in openai_models:
        llm_models['openai_models:vision:default'] = set_model
        return set_model
    return llm_models['openai_models:vision:default']


# from schnell.app.llmutils.langchainutils.llm_config import get_active_model
def get_active_model():
    active = all_accounts['active']
    if active == 'gemini':
        return gemini_models[gemini_models_get_default()]
    elif active == 'openai':
        return openai_models[openai_models_get_default()]
    elif active == 'groq':
        return groq_models[groq_models_get_default()]
    elif active == 'cohere':
        return cohere_models[cohere_models_get_default()]

    elif active == 'together':
        return together_models[together_models_get_default()]
    elif active == 'huggingface':
        return huggingface_models[huggingface_models_get_default()]

    elif active == 'gemini_vision':
        return gemini_models[google_models_get_default_for_vision()]
    elif active == 'openai_vision':
        return openai_models[openai_models_get_default_for_vision()]
    # elif active == 'openai':
    #     return gemini_models_get_default()
    # elif active == 'openai':
    #     return gemini_models_get_default()
    # elif active == 'openai':
    #     return gemini_models_get_default()
    # elif active == 'openai':
    #     return gemini_models_get_default()
    # elif active == 'openai':
    #     return gemini_models_get_default()
    else:
        print(f'get_active_model not implemented for {active}')

# from schnell.app.llmutils.langchainutils.llm_config import get_account_key_by_name, openai_accounts, openai_vision_accounts
def get_account_key_by_name(name, accounts_dict=gemini_accounts):
    for key, value in accounts_dict.items():
        if value["name"] == name:
            return key
    return None

def test_get_openai_account_key_by_name():
    name_to_find = "ulumus"
    account_key = get_account_key_by_name(name_to_find, accounts_dict=openai_accounts)
    print(account_key)  # Output: openai_5

    name_to_find = "jyw"
    account_key = get_account_key_by_name(name_to_find, accounts_dict=openai_accounts)
    print(account_key)  # Output: openai_9

# from schnell.app.llmutils.langchainutils.llm_config import get_encrypted_api_key_by_name, openai_vision_accounts
def get_encrypted_api_key_by_name(name, accounts_dict=gemini_accounts):
    account_key = get_account_key_by_name(name, accounts_dict)
    if account_key:
        result = accounts_dict[account_key]['key']
        return result
    return None

# from schnell.app.llmutils.langchainutils.llm_config import get_decrypted_api_key_by_name, openai_vision_accounts, gemini_accounts
from schnell.app.cryptoutils import dekripsi
def get_decrypted_api_key_by_name(name, accounts_dict=gemini_accounts):
    account_key = get_account_key_by_name(name, accounts_dict)
    if account_key:
        result = dekripsi(accounts_dict[account_key]['key'])
        return result
    return None
