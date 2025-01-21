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

from schnell.app.llmutils.langchainutils.llms.llm_gemini import (
    create_llm_chat as chat_gemini,
    create_llm as gemini
)

from schnell.app.llmutils.langchainutils.llms.llm_cohere import (
    create_llm_chat as chat_cohere,
    create_llm as cohere
)

from schnell.app.llmutils.langchainutils.llms.llm_groq import (
    create_llm_chat as chat_groq
)

from schnell.app.llmutils.langchainutils.llms.llm_together import (
    create_llm_chat as chat_together,
    create_llm as together
)

from schnell.app.llmutils.langchainutils.llms.llm_openai import (
    create_llm_chat as chat_openai,
    create_llm as openai
)

from schnell.app.llmutils.langchainutils.llms.llm_huggingface import (
    create_llm_chat as chat_huggingface
)

from schnell.app.llmutils.langchainutils.llms.llm_gooseai import (
    create_llm_chat as chat_gooseai
)

from schnell.app.llmutils.langchainutils.llms.llm_clarify import (
    create_llm_chat as chat_clarify
)

from schnell.app.llmutils.langchainutils.llms.llm_nvidia import (
    create_llm_chat as chat_nvidia
)

from schnell.app.llmutils.langchainutils.llms.llm_replicate import (
    create_llm_chat as chat_replicate
)

from schnell.app.llmutils.langchainutils.llm_config import all_accounts
# from schnell.app.llmutils.langchainutils.llms.active import get_active_llm
def get_active_llm():
    llm_name = all_accounts['active']
    # indah4(f'[get_active_llm] {llm_name}:', warna='green')
    llm = None
    if llm_name == 'groq':
        llm = chat_groq()
    else:
        llm = {
            'gemini'    : gemini,
            'openai'    : chat_openai,
            # 'openai'    : openai,
            # chat_groq() kembalikan ChatGroq, ChatGroq() kembalikan AIMessage
            # 'groq': lambda: chat_groq()()['content'],
            'together'  : together,
            'cohere'    : cohere,
            'nvidia'    : chat_nvidia,
            'replicate' : chat_replicate,
        }.get(llm_name)()
    return llm


# from schnell.app.llmutils.langchainutils.llms.active import get_secondary_active_llm
# jk yg aktif adlh groq maka kembalikan non-groq
# otherwise kembalikan groq
def get_secondary_active_llm():
    llm_name = all_accounts['active']
    llm = None
    if llm_name != 'groq':
        llm = chat_groq()
    else:
        llm = {
            'gemini'    : gemini,
            'openai'    : chat_openai,
            # 'openai'    : openai,
            # chat_groq() kembalikan ChatGroq, ChatGroq() kembalikan AIMessage
            # 'groq': lambda: chat_groq()()['content'],
            'together'  : together,
            'cohere'    : cohere,
            'nvidia'    : chat_nvidia,
            'replicate' : chat_replicate,
        }.get(llm_name)()
    return llm
