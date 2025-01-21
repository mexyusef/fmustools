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

if __name__ == '__main__':    
    sys.path.insert(0, r'c:\users\usef\work\sidoarjo')

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
# print('invoke1')
# from schnell.app.llmutils.langchainutils.llms.llm_gemini import create_llm_chat, create_llm
# from schnell.app.llmutils.langchainutils.agents import give_me_code
from schnell.app.llmutils.langchainutils.llms.llm_gemini import (
    create_llm_chat as chat_gemini,
    create_llm as gemini,
    # new_chat_gemini,
)
# print('invoke2')
from schnell.app.llmutils.langchainutils.llms.llm_cohere import (
    create_llm_chat as chat_cohere,
    create_llm as cohere
)
# print('invoke3')
from schnell.app.llmutils.langchainutils.llms.llm_groq import (
    create_llm_chat as chat_groq
)
# print('invoke4')
from schnell.app.llmutils.langchainutils.llms.llm_together import (
    create_llm_chat as chat_together,
    create_llm as together
)
# print('invoke5')
from schnell.app.llmutils.langchainutils.llms.llm_openai import (
    create_llm_chat as chat_openai,
    create_llm as openai
)
# print('invoke6')
from schnell.app.llmutils.langchainutils.llms.llm_huggingface import (
    create_llm_chat as chat_huggingface
)
# print('invoke7')
from schnell.app.llmutils.langchainutils.llms.llm_gooseai import (
    create_llm_chat as chat_gooseai
)
# print('invoke8')
from schnell.app.llmutils.langchainutils.llms.llm_clarify import (
    create_llm_chat as chat_clarify
)
# print('invoke9')
from schnell.app.llmutils.langchainutils.llms.llm_nvidia import (
    create_llm_chat as chat_nvidia
)
# print('invoke10')
from schnell.app.llmutils.langchainutils.llms.llm_replicate import (
    create_llm_chat as chat_replicate
)
# print('invoke11')
from schnell.app.llmutils.langchainutils.llm_config import invoke_all, all_accounts
# print('invoke12')
from schnell.app.printutils import indah4
# from schnell.app.llmutils.langchainutils.llms import with_memory, use_memory, memory_instances


# from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm
# result = invoke_llm(current_line, all_accounts['active'])
# indah3(result, warna='yellow')

mem_groq        = chat_groq         # with_memory()(chat_groq)
mem_openai      = chat_openai       # with_memory()(chat_openai)
mem_gemini      = chat_gemini       # with_memory()(chat_gemini)
mem_together    = chat_together     # with_memory()(chat_together)
mem_cohere      = chat_cohere       # with_memory()(chat_cohere)
mem_nvidia      = chat_nvidia       # with_memory()(chat_nvidia)
mem_replicate   = chat_replicate    # with_memory()(chat_replicate)

llms = {
    'groq'      : mem_groq,
    'gemini'    : mem_gemini,
    'openai'    : mem_openai,
    'together'  : mem_together,
    'cohere'    : mem_cohere,
    'nvidia'    : mem_nvidia,
    'replicate' : mem_replicate,
}

# Modify invoke_llm to use memory
# @use_memory(memory_type='buffer')  # Default to 'buffer', change as needed
def invoke_llm(masukan, llm_name='gemini', verbose=False): # , memory=memory_instances['buffer']):
    indah4(f'[invoke_llm] {llm_name}:\n{masukan}', warna='green')
    if llm_name == 'groq':
        result = chat_groq().invoke(masukan).content  # AIMessage
        # llm = use_memory(memory_type='buffer')(chat_groq)
        # result = llm().invoke(masukan).content
    else:
        llm_map = {
            # 'gemini'    : lambda: new_chat_gemini(memory=memory),
            'gemini'    : chat_gemini,
            'openai'    : chat_openai,
            'together'  : chat_together,
            'cohere'    : chat_cohere,
            'nvidia'    : chat_nvidia,
            'replicate' : chat_replicate,
            'huggingface' : chat_huggingface,
            # 'sambanova'   : chat_sambanova,
            # 'hyperbolic'  : chat_hyperbolic,
        }.get(llm_name)
        result = llm_map().invoke(masukan)
        # llm = use_memory(memory_type='buffer')(llm_map)
        # result = llm().invoke(masukan)

    if isinstance(result, AIMessage):
        old_result = result
        result = result.content
        if verbose:
            result += '\n\nUsage:\n' + json.dumps(old_result.response_metadata, indent=2)

    return result

def invoke_llm_active(masukan, verbose=False): # , memory_type='buffer'):
    return invoke_llm(masukan, all_accounts['active'], verbose=verbose) #, memory=memory_instances[memory_type])

# # Example usage:
# result = invoke_llm_active("Hello, how are you?", memory_type='buffer')
# print(result)

def invoke_llm_gagal(masukan, llm_name='gemini', verbose=False):
    # prompt = prompt_template.format(number_of_alternatives=jumlah, code_query=masukan)
    indah4(f'[invoke_llm] {llm_name}:\n{masukan}', warna='green')

    # if llm_name == 'groq':
    #     # result = chat_groq().invoke(masukan).content  # AIMessage
    #     result = mem_groq.invoke(masukan).content  # AIMessage
    # else:
    #     llm = {
    #         'gemini'    : mem_gemini, # gemini,
    #         'openai'    : mem_openai, # chat_openai,
    #         # 'openai'    : openai,
    #         # chat_groq() kembalikan ChatGroq, ChatGroq() kembalikan AIMessage
    #         # 'groq': lambda: chat_groq()()['content'],
    #         'together'  : mem_together, # together,
    #         'cohere'    : mem_cohere, # cohere,
    #         'nvidia'    : mem_nvidia, # chat_nvidia,
    #         'replicate' : mem_replicate, # chat_replicate,
    #     }.get(llm_name)
    #     result = llm().invoke(masukan)

    # # Get the LLM function from the mapping
    # llm = llms.get(llm_name)

    # # Ensure the LLM function is found
    # if llm is None:
    #     raise ValueError(f"LLM with name '{llm_name}' not found.")

    # # Call the LLM with the user input
    # result = llm(masukan)
    # Get the LLM function from the mapping
    llm_func = llms.get(llm_name)

    # Ensure the LLM function is found
    if llm_func is None:
        raise ValueError(f"LLM with name '{llm_name}' not found.")

    # Create the LLM instance and call the `invoke` method
    llm_instance = llm_func()
    result = llm_instance.invoke(masukan)

    # if llm_name=='openai' and isinstance(result, AIMessage):
    # ternyata gemini juga bisa AIMessage
    if isinstance(result, AIMessage):
        old_result = result
        result = result.content
        if verbose:
            result += '\n\nUsage:\n' + json.dumps(old_result.response_metadata, indent=2)

    # print(result)
    return result


# from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm_active
def invoke_llm_active_ganti(masukan, verbose=False):
    return invoke_llm(masukan, all_accounts['active'], verbose=verbose)

# from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm_code_query
def invoke_llm_code_query(masukan, verbose=False):
    return invoke_llm(masukan, all_accounts['code_query'], verbose=verbose)

# from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm_error_query
def invoke_llm_error_query(masukan, verbose=False):
    return invoke_llm(masukan, all_accounts['error_query'], verbose=verbose)

# from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm_all
def invoke_llm_all(masukan, verbose=False):
    result = {}

    for model, active in invoke_all.items():
        if active:
            if model == 'groq':
                result[model] = chat_groq().invoke(masukan).content
            else:
                result[model] = invoke_llm(masukan, llm_name=model, verbose=verbose)

    # result['groq'] = chat_groq().invoke(masukan).content
    # for llm_name in ['gemini', 'openai', 'cohere']: # , 'together', 'nvidia']:
    #     result[llm_name] = invoke_llm(masukan, llm_name=llm_name)

    return result
