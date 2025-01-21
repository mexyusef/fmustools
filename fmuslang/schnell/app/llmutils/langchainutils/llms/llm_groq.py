# groq as openai
# https://youtu.be/3-q5GzRNEe0?t=375
# export GROQ_API_KEY=
# export LLM_MODEL=groq/mixtral-8x7b-32768

# https://python.langchain.com/docs/integrations/chat/groq
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_groq\chat_models.py
# #C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_groq

if __name__ == '__main__':
    import os, sys
    sys.path.insert(0, r'c:\users\usef\work\sidoarjo')

from schnell.app.llmutils.langchainutils.llms import groq_accounts, randomly_select_account
from schnell.app.cryptoutils import dekripsi
from schnell.app.llmutils.langchainutils.llm_config import all_accounts
from schnell.app.llmutils.langchainutils.llm_config import groq_models, groq_models_get_default


# from schnell.app.llmutils.langchainutils.llms.llm_groq import create_llm_chat
def create_llm_chat(groq_key=None, model=None, temperature=None):
    if not model:
        model = groq_models[groq_models_get_default()]
    if not groq_key:
        groq_key = randomly_select_account(groq_accounts)
    if groq_accounts[groq_key]['instance']:
        print(f"{groq_key}/{groq_accounts[groq_key]['name']} reused.")
        return groq_accounts[groq_key]['instance']

    # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_groq\chat_models.py
    llm = ChatGroq(
        model_name = model,
        # temperature = temperature if temperature is not None else groq_accounts[groq_key]['temperature'],
        temperature = temperature if temperature is not None else all_accounts['temperature'],
        groq_api_key = dekripsi(groq_accounts[groq_key]['key']),
        verbose = True,
        # convert_system_message_to_human = True,
        # convert_system_message_to_human is not default parameter.
        # convert_system_message_to_human was transferred to model_kwargs.
        # Please confirm that convert_system_message_to_human is what you intended.
        # TypeError: Completions.create() got an unexpected keyword argument 'convert_system_message_to_human'
    )
    groq_accounts[groq_key]['instance'] = llm
    print(f"{groq_key}/{groq_accounts[groq_key]['name']} selected.")
    return llm


# llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")
# llm = ChatGroq(temperature=0, groq_api_key="YOUR_API_KEY", model_name="mixtral-8x7b-32768")
# llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")
# llm = ChatGroq(temperature=0, model_name="llama2-70b-4096")


def chain_invoke(
    llm,
    key_in_query="topic",
    value_in_query="Black hole",
    query="Write something about {topic}",
    system_prompt="You are a helpful assistant."
):
    """
    system = "You are a helpful assistant."
    human = "{text}"
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
    chain = prompt | llm
    chain.invoke({"text": "Explain the importance of low latency LLMs."})

    prompt = ChatPromptTemplate.from_messages([("human", "Write a Limerick about {topic}")])
    chain = prompt | llm
    await chain.ainvoke({"topic": "The Sun"})

    """
    chain = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", f"{{{query}}}")  # query berisi key_in_query
        ]
        ) | llm
    res = chain.invoke({
        key_in_query: value_in_query
    })
    return res


def chain_print_stream(
    llm,
    key_in_query="topic",
    value_in_query="Black hole",
    query="Write something about {topic}",
    system_prompt="You are a helpful assistant."
):
    """
    prompt = ChatPromptTemplate.from_messages([("human", "Write a haiku about {topic}")])
    chain = prompt | llm
    for chunk in chain.stream({"topic": "The Moon"}):
        print(chunk.content, end="", flush=True)
    """
    chain = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", f"{{{query}}}")  # query berisi key_in_query
        ]
        ) | llm
    for chunk in chain.stream({ key_in_query: value_in_query }):
        print(chunk.content, end="", flush=True)



def instantiate_all_as_chats():
    for key in groq_accounts.keys():
        create_llm_chat(groq_key=key)


def invoker(query, index=0, choice=['chat', 'once', 'vision']):
    choose = choice[index]
    if choose == 'chat':
        return create_llm_chat().invoke(query)
    # elif choose == 'once':
    #     return create_llm().invoke(query)
