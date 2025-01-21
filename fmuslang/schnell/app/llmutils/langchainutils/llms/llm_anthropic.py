# https://github.com/langchain-ai/langgraph/blob/main/examples/branching.ipynb
# %pip install -qU langchain-anthropic
from langchain_anthropic import ChatAnthropic
from langchain_anthropic import AnthropicLLM
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

from langchain.chains import LLMChain
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)


if __name__ == '__main__':
    import os, sys
    sys.path.insert(0, r'c:\users\usef\work\sidoarjo')

from schnell.app.llmutils.langchainutils.llms import claude_accounts, randomly_select_account
from schnell.app.printutils import indah4
from schnell.app.cryptoutils import dekripsi
from schnell.app.llmutils.langchainutils.llm_config import all_accounts

anthropic_models = {
    'haiku'         : "claude-3-haiku-20240307",
    'opus'          : "claude-3-opus-20240229",
    'claude2'       : "claude-2.1",
}

# https://python.langchain.com/docs/integrations/llms/anthropic
def create_llm_chat(anthropic_key=None, model=anthropic_models["haiku"], temperature=None):
    # if not model:
    #     model = anthropic_models[anthropic_models_get_default()]
    if not anthropic_key:
        anthropic_key = randomly_select_account(claude_accounts)
    if claude_accounts[anthropic_key]['instance']:
        print(f"{anthropic_key}/{claude_accounts[anthropic_key]['name']} reused with model {model}.")
        return claude_accounts[anthropic_key]['instance']

    # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_anthropic\chat_models.py
    llm = ChatAnthropic(
        anthropic_api_key = dekripsi(claude_accounts[anthropic_key]['key']),
        model = model,
        # temperature = temperature if temperature is not None else claude_accounts[anthropic_key]['temperature'],
        temperature = temperature if temperature is not None else all_accounts['temperature'],
    )
    claude_accounts[anthropic_key]['instance'] = llm
    print(f"{anthropic_key}/{claude_accounts[anthropic_key]['name']} selected with model {model}.")
    return llm


# template = """Question: {question}

# Answer: Let's think step by step."""

# prompt = PromptTemplate.from_template(template)
# model = AnthropicLLM(model="claude-2.1")
# chain = prompt | model
# chain.invoke({"question": "What is LangChain?"})

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

