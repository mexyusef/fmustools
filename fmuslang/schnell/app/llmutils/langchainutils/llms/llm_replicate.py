import os, sys

# from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# pip install --user replicate
from langchain_community.llms import Replicate
from langchain_core.prompts import PromptTemplate
# from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
# from langchain_community.llms import HuggingFaceEndpoint
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

from schnell.app.llmutils.langchainutils.llms import replicate_accounts, randomly_select_account
from schnell.app.printutils import indah4
from schnell.app.cryptoutils import dekripsi

# https://python.langchain.com/docs/integrations/llms/replicate/

# https://replicate.com/explore
# https://replicate.com/collections/language-models

# C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\replicate\client.py
# C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_community\llms\replicate.py

# https://replicate.com/mistralai/mixtral-8x7b-instruct-v0.1/examples?input=python
#     "mistralai/mixtral-8x7b-instruct-v0.1:cf18decbf51c27fed6bbdc3492312c1c903222a56e3fe9ca02d6cbe5198afc10",
#     input={
#         "top_k": 50,
#         "top_p": 0.9,
#         "prompt": "Write a short poem about dosa",
#         "temperature": 0.6,
#         "max_new_tokens": 512,
#         "prompt_template": "<s>[INST] {prompt} [/INST]"
#     }

# https://replicate.com/replicate/dolly-v2-12b/examples?input=python
#     "replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5",
#     input={
#         "top_k": 50,
#         "top_p": 1,
#         "prompt": "Who was Dolly the sheep?",
#         "decoding": "top_p",
#         "max_length": 500,
#         "temperature": 0.75,
#         "repetition_penalty": 1.2
#     }
# llm = Replicate(
#     model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",
#     model_kwargs={"temperature": 0.75, "max_length": 500, "top_p": 1},
# )
# prompt = """
# User: Answer the following yes/no question by reasoning step by step. Can a dog drive a car?
# Assistant:
# """
# llm(prompt)

# REPLICATE_API_TOKEN
def create_llm_chat(replicate_key=None, model=None, temperature=0.01):
    if not replicate_key:
        replicate_key = randomly_select_account(replicate_accounts)
    if replicate_accounts[replicate_key]['instance']:
        print(f"{replicate_key}/{replicate_accounts[replicate_key]['name']} reused.")
        return replicate_accounts[replicate_key]['instance']

    token_key = dekripsi(replicate_accounts[replicate_key]['key'])

    # indah4(f"""create_llm_chat/replicate
    # replicate_key   = {replicate_key}
    # replicate_accounts[replicate_key]   = {replicate_accounts[replicate_key]}
    # token_key       = {token_key}
    # """, warna='yellow')

    # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_community\llms\huggingface_endpoint.py
    # pydantic.v1.error_wrappers.ValidationError: 1 validation error for Replicate
    # model
    # field required (type=value_error.missing)
        # model=(
        #     "stability-ai/stable-diffusion: "
        #     "27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
        # ),
        # model_kwargs={"image_dimensions": "512x512"},
    # model_str, version_str = self.model.split(":")
    #     ^^^^^^^^^^^^^^^^^^^^^^
    # ValueError: not enough values to unpack (expected 2, got 1)
    os.environ['REPLICATE_API_TOKEN'] = token_key
    llm = Replicate(
        model = "mistralai/mixtral-8x7b-instruct-v0.1:cf18decbf51c27fed6bbdc3492312c1c903222a56e3fe9ca02d6cbe5198afc10",
        # temperature = temperature if temperature is not None else replicate_accounts[replicate_key]['temperature'],
        replicate_api_token=token_key,
    )
    replicate_accounts[replicate_key]['instance'] = llm
    print(f"{replicate_key}/{replicate_accounts[replicate_key]['name']} selected.")
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
