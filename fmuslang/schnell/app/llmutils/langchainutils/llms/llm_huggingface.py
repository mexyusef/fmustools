import os, sys
from langchain_community.llms import HuggingFaceEndpoint
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

# https://www.youtube.com/watch?v=T6XhRFeDbPY
# Hugging Face x LangChain:A new partner package in LangChain
# Huggingface And Langchain are happy toannounce the launch of langchain_huggingface, a partner package in LangChain jointly maintained by Hugging Face and LangChain. This new Python package is designed to bring the power of the latest development of Hugging Face into LangChain and keep it up to date.
# https://colab.research.google.com/drive/1l3jLGdWaDn24NlP1kNo_ALhlH_2N84jI

if __name__ == '__main__':
    sys.path.insert(0, r'c:\users\usef\work\sidoarjo')

from schnell.app.llmutils.langchainutils.llms import huggingface_accounts, randomly_select_account
from schnell.app.printutils import indah4
from schnell.app.cryptoutils import dekripsi
from schnell.app.llmutils.langchainutils.llm_config import all_accounts
# https://python.langchain.com/docs/integrations/llms/huggingface_endpoint
# https://python.langchain.com/docs/integrations/chat/huggingface
# https://python.langchain.com/docs/integrations/platforms/huggingface
# pip install --user --upgrade --quiet huggingface_hub
# llama3...

# huggingface_models = {
#     'mistral'           : "mistralai/Mistral-7B-Instruct-v0.2",
#     # 'mixtral'           : "mixtral-8x7b-32768",
#     # 'llama2'            : "llama2-70b-4096",
#     # '4_preview'         : "gpt-4-turbo-preview",
# }

# # get a token: https://huggingface.co/docs/api-inference/quicktour#get-your-api-token
# from getpass import getpass
# HUGGINGFACEHUB_API_TOKEN = getpass()
# # import os
# # os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

# question = "Who won the FIFA World Cup in the year 1994? "
# template = """Question: {question}

# Answer: Let's think step by step."""
# prompt = PromptTemplate.from_template(template)
# # repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
# llm = HuggingFaceEndpoint(
#     repo_id=repo_id,
#     max_length=128,
#     temperature=0.5,
#     token=HUGGINGFACEHUB_API_TOKEN
# )
# llm_chain = LLMChain(prompt=prompt, llm=llm)
# print(llm_chain.run(question))
from schnell.app.llmutils.langchainutils.llm_config import huggingface_models, huggingface_models_get_default


# from schnell.app.llmutils.langchainutils.llms.llm_groq import create_llm_chat
def create_llm_chat(hf_key=None, model=None, temperature=0.01):
    if not model:
        model = huggingface_models[huggingface_models_get_default()]
    if not hf_key:
        hf_key = randomly_select_account(huggingface_accounts)
    if huggingface_accounts[hf_key]['instance']:
        print(f"{hf_key}/{huggingface_accounts[hf_key]['name']} reused.")
        return huggingface_accounts[hf_key]['instance']

    token_key = dekripsi(huggingface_accounts[hf_key]['key'])
    # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_community\llms\huggingface_endpoint.py
    llm = HuggingFaceEndpoint(
        repo_id = model,
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
        # temperature = temperature if temperature is not None else huggingface_accounts[hf_key]['temperature'],
        temperature = temperature if temperature is not None else all_accounts['temperature'],
        huggingfacehub_api_token = token_key,
    )
    huggingface_accounts[hf_key]['instance'] = llm
    print(f"{hf_key}/{huggingface_accounts[hf_key]['name']} selected.")
    return llm


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


def instantiate_all_as_chats():
    for key in huggingface_accounts.keys():
        create_llm_chat(hf_key=key)


def invoker(query, index=0, choice=['chat', 'once', 'vision']):
    choose = choice[index]
    if choose == 'chat':
        return create_llm_chat().invoke(query)
    # elif choose == 'once':
    #     return create_llm().invoke(query)


# # streaming
# llm = HuggingFaceEndpoint(
#     endpoint_url=f"{your_endpoint_url}",
#     max_new_tokens=512,
#     top_k=10,
#     top_p=0.95,
#     typical_p=0.95,
#     temperature=0.01,
#     repetition_penalty=1.03,
#     streaming=True,
# )
# llm("What did foo say about bar?", callbacks=[StreamingStdOutCallbackHandler()])


# paid account
# # Set the url to your Inference Endpoint below
# your_endpoint_url = "https://fayjubiy2xqn36z0.us-east-1.aws.endpoints.huggingface.cloud"
# llm = HuggingFaceEndpoint(
#     endpoint_url=f"{your_endpoint_url}",
#     max_new_tokens=512,
#     top_k=10,
#     top_p=0.95,
#     typical_p=0.95,
#     temperature=0.01,
#     repetition_penalty=1.03,
# )
# llm("What did foo say about bar?")

if __name__ == '__main__':
    test_create_llm_chat()
