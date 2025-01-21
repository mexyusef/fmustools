import os, sys

from langchain_community.llms import GooseAI
from langchain_core.prompts import PromptTemplate

# from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain

from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)


if __name__ == '__main__':
    sys.path.insert(0, r'c:\users\usef\work\sidoarjo')

from schnell.app.llmutils.langchainutils.llms import gooseai_accounts, randomly_select_account
from schnell.app.printutils import indah4
from schnell.app.cryptoutils import dekripsi
from schnell.app.llmutils.langchainutils.llm_config import all_accounts
# https://python.langchain.com/docs/integrations/llms/gooseai/

# from getpass import getpass
# GOOSEAI_API_KEY = getpass()
# os.environ["GOOSEAI_API_KEY"] = GOOSEAI_API_KEY

# https://goose.ai/docs/models
# gpt-neo-20b
# fairseq-125m
# fairseq-1-3b
# fairseq-2-7b
# fairseq-6b-7b
# fairseq-13b
# gpt-j-6b
# gpt-neo-125m
# gpt-neo-1-3b
# gpt-neo-2-7b
# llm = GooseAI()
# template = """Question: {question}

# Answer: Let's think step by step."""
# prompt = PromptTemplate.from_template(template)
# llm_chain = LLMChain(prompt=prompt, llm=llm)
# question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"
# llm_chain.run(question)


# C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_community\llms\gooseai.py
# 
# model_name: str = "gpt-neo-20b"
def create_llm_chat(gooseai_key=None, model=None, temperature=0.01):
    if not gooseai_key:
        gooseai_key = randomly_select_account(gooseai_accounts)
    if gooseai_accounts[gooseai_key]['instance']:
        print(f"{gooseai_key}/{gooseai_accounts[gooseai_key]['name']} reused.")
        return gooseai_accounts[gooseai_key]['instance']

    token_key = dekripsi(gooseai_accounts[gooseai_key]['key'])
    # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_community\llms\huggingface_endpoint.py
    # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_community\llms\gooseai.py
    # vscode C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_community\llms\gooseai.py
    # #C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_community\llms\gooseai.py
    llm = GooseAI(
        # repo_id = model,
        # max_new_tokens=512,
        # top_k=10,
        # top_p=0.95,
        # typical_p=0.95,
        # temperature=0.01,
        # repetition_penalty=1.03,
        # callbacks=callbacks,
        # streaming=True,
        # temperature gak bisa 0.0
        # Input validation error: `temperature` must be strictly positive
        # temperature = temperature if temperature is not None else gooseai_accounts[gooseai_key]['temperature'],
        temperature = temperature if temperature is not None else all_accounts['temperature'],
        gooseai_api_key=token_key,
    )
    gooseai_accounts[gooseai_key]['instance'] = llm
    print(f"{gooseai_key}/{gooseai_accounts[gooseai_key]['name']} selected.")
    return llm

# File "C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_community\llms\gooseai.py", line 150, in _call
# response = self.client.create(engine=self.model_name, prompt=prompt, **params)
#             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# File "C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\openai\lib\_old_api.py", line 39, in __call__
# raise APIRemovedInV1(symbol=self._symbol)
# openai.lib._old_api.APIRemovedInV1:

# You tried to access openai.Completion, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.
# You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface.
# Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`
# A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742

def test_create_llm_chat():
    question = "What's the difference between Nextjs 14 App router and pages router? "
    template = """Question: {question}

    Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)
    # repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
    llm = create_llm_chat()
    llm_chain = LLMChain(prompt=prompt, llm=llm)
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
