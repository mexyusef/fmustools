import os, sys


from langchain_community.llms import Clarifai

# from langchain_nvidia_ai_endpoints import ChatNVIDIA
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

from schnell.app.llmutils.langchainutils.llms import clarifyai_accounts, randomly_select_account
from schnell.app.printutils import indah4
from schnell.app.cryptoutils import dekripsi


USER_ID     = "openai"
APP_ID      = "chat-completion"
MODEL_ID    = "GPT-3_5-turbo"
clarifyai_models = {
    "default"       : "GPT-3_5-turbo",
    "llama2"        : "llama2_13b"
    # 'mixtral'       : "mixtral-8x7b-32768",
    # 'llama2'        : "llama2-70b-4096",
    # '4_preview'     : "gpt-4-turbo-preview",
}


# C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_community\llms\clarifai.py
# model_url: Optional[str] = None
# """Model url to use."""
# model_id: Optional[str] = None
# """Model id to use."""
# model_version_id: Optional[str] = None
# """Model version id to use."""
# app_id: Optional[str] = None
# """Clarifai application id to use."""
# user_id: Optional[str] = None
# """Clarifai user id to use."""
# pat: Optional[str] = Field(default=None, exclude=True)  #: :meta private:
# """Clarifai personal access token to use."""
# token: Optional[str] = Field(default=None, exclude=True)  #: :meta private:
# """Clarifai session token to use."""
# model: Any = Field(default=None, exclude=True)  #: :meta private:
# api_base: str = "https://api.clarifai.com"

def create_llm_chat(clarifyai_key=None, model=clarifyai_models['default'], temperature=None):
    if not clarifyai_key:
        clarifyai_key = randomly_select_account(clarifyai_accounts)
    if clarifyai_accounts[clarifyai_key]['instance']:
        print(f"{clarifyai_key}/{clarifyai_accounts[clarifyai_key]['name']} reused.")
        return clarifyai_accounts[clarifyai_key]['instance']

    # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_cohere\llms.py
    llm = Clarifai(
        user_id = USER_ID,
        app_id = APP_ID,
        model_id = model,
        pat = dekripsi(clarifyai_accounts[clarifyai_key]['key']),
        # inference_params = dict(
        #     temperature=str(
        #         temperature if temperature is not None 
        #         else clarifyai_accounts[clarifyai_key]['temperature']
        #     )
        # ),
    )
    clarifyai_accounts[clarifyai_key]['instance'] = llm
    print(f"{clarifyai_key}/{clarifyai_accounts[clarifyai_key]['name']} selected.")
    return llm


def create_llm(clarifyai_key=None, model=clarifyai_models['default'], temperature=None):
    if not clarifyai_key:
        clarifyai_key = randomly_select_account(clarifyai_accounts)
    if clarifyai_accounts[clarifyai_key]['instance']:
        print(f"{clarifyai_key}/{clarifyai_accounts[clarifyai_key]['name']} reused.")
        return clarifyai_accounts[clarifyai_key]['instance']

    llm = Clarifai(
        user_id = USER_ID,
        app_id = APP_ID,
        model_id = model,
        pat = dekripsi(clarifyai_accounts[clarifyai_key]['key']),
        # inference_params = dict(
        #     temperature=str(
        #         temperature if temperature is not None 
        #         else clarifyai_accounts[clarifyai_key]['temperature']
        #     )
        # ),
    )
    clarifyai_accounts[clarifyai_key]['instance'] = llm
    print(f"{clarifyai_key}/{clarifyai_accounts[clarifyai_key]['name']} selected.")
    return llm

# C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_community\llms\clarifai.py
# ada call yg terima prompt dan generate yg terima prompts
# keduanya menerima inference_params, jadi params ini bukan waktu bikin llm, tapi waktu () atau generate.


def test_create_llm_chat():
    question = "What's the difference between Nextjs 14 App router and pages router? Give example."
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
