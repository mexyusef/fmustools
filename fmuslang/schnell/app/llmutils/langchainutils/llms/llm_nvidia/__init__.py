import os, sys

# ternyata sudah ada
# https://python.langchain.com/docs/integrations/chat/nvidia_ai_endpoints
# pip install --user --upgrade langchain-nvidia-ai-endpoints
from langchain_nvidia_ai_endpoints import ChatNVIDIA
# from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import PromptTemplate
# from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

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

from schnell.app.llmutils.langchainutils.llms import nvidia_accounts, randomly_select_account
from schnell.app.printutils import indah4
from schnell.app.cryptoutils import dekripsi


nvidia_models = {
    "default"       : "mixtral_8x7b",
    "llama2"        : "llama2_13b"
    # 'mixtral'       : "mixtral-8x7b-32768",
    # 'llama2'        : "llama2-70b-4096",
    # '4_preview'     : "gpt-4-turbo-preview",
}


# sepertinya gak bisa bikin LLM? bisanya hanya langsung query/invoke?
# hrs cari tau gimana langchain support LLM baru
# wah ternyata simple
# C:\work\ciledug\ciledug\fmusperintah\vendor\langchain\libs\community\langchain_community\llms\together.py
# C:\work\ciledug\ciledug\fmusperintah\vendor\langchain\libs\community\langchain_community\llms\modal.py
# C:\work\ciledug\ciledug\fmusperintah\vendor\langchain\libs\community\langchain_community\llms\gooseai.py
# C:\work\ciledug\ciledug\fmusperintah\vendor\langchain\libs\community\langchain_community\llms\cohere.py
# C:\work\ciledug\ciledug\fmusperintah\vendor\langchain\libs\community\langchain_community\llms\databricks.py


def create_llm_chat(nvidia_key=None, model=nvidia_models['default']):
    if not nvidia_key:
        nvidia_key = randomly_select_account(nvidia_accounts)
    if nvidia_accounts[nvidia_key]['instance']:
        print(f"{nvidia_key}/{nvidia_accounts[nvidia_key]['name']} reused.")
        return nvidia_accounts[nvidia_key]['instance']

    token_key = dekripsi(nvidia_accounts[nvidia_key]['key'])

    os.environ['NVIDIA_API_KEY'] = token_key

    indah4(f"""create_llm_chat/nvidia
    nvidia_key      = {nvidia_key}
    nvidia_accounts[nvidia_key]   = {nvidia_accounts[nvidia_key]}
    token_key       = {token_key}
    """, warna='yellow')
    # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_nvidia_ai_endpoints\chat_models.py
    # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_nvidia_ai_endpoints\_common.py
    llm = ChatNVIDIA(
        model = model,
        api_key = token_key,
    )

    nvidia_accounts[nvidia_key]['instance'] = llm
    print(f"{nvidia_key}/{nvidia_accounts[nvidia_key]['name']} selected.")
    return llm


def create_llm(nvidia_key=None, model=nvidia_models['default']):
    pass


# import getpass
# import os

# if not os.environ.get("NVIDIA_API_KEY", "").startswith("nvapi-"):
#     nvapi_key = getpass.getpass("Enter your NVIDIA API key: ")
#     assert nvapi_key.startswith("nvapi-"), f"{nvapi_key[:5]}... is not a valid key"
#     os.environ["NVIDIA_API_KEY"] = nvapi_key

# ## Core LC Chat Interface
from pprint import pprint as pp
def print_models():
    # result = ChatNVIDIA.get_available_models()
    llm = create_llm_chat()
    result = llm.get_available_models()
    # print(result)
    for model in result:
        pp(model)

# llm = ChatNVIDIA(model="mixtral_8x7b")
# result = llm.invoke("Write a ballad about LangChain.")
# print(result.content)

# print(llm.batch(["What's 2*3?", "What's 2*6?"]))
# # Or via the async API
# # await llm.abatch(["What's 2*3?", "What's 2*6?"])

# for chunk in llm.stream("How far can a seagull fly in one day?"):
#     # Show the token separations
#     print(chunk.content, end="|")

# async for chunk in llm.astream(
#     "How long does it take for monarch butterflies to migrate?"
# ):
#     print(chunk.content, end="|")



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
    # print_models()
