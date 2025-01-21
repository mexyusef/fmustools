from langchain_community.embeddings import CohereEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain.tools.retriever import create_retriever_tool
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.tools.tavily_search import TavilySearchResults
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage







from langchain_cohere import ChatCohere
from langchain_cohere.llms import Cohere
if __name__ == '__main__':
    import os, sys
    sys.path.insert(0, r'c:\users\usef\work\sidoarjo')

from schnell.app.llmutils.langchainutils.llm_config import all_accounts
from schnell.app.llmutils.langchainutils.llms import cohere_accounts, randomly_select_account
from schnell.app.cryptoutils import dekripsi
from schnell.app.llmutils.langchainutils.llm_config import cohere_models, cohere_models_get_default

def create_llm_chat(cohere_key=None, model=None, temperature=None):
    if not model:
        model = cohere_models[cohere_models_get_default()]
    if not cohere_key:
        cohere_key = randomly_select_account(cohere_accounts)
    if cohere_accounts[cohere_key]['instance']:
        print(f"{cohere_key}/{cohere_accounts[cohere_key]['name']} reused.")
        return cohere_accounts[cohere_key]['instance']

    llm = ChatCohere(
        model = model,
        temperature = temperature if temperature is not None else all_accounts['temperature'],
        cohere_api_key = dekripsi(cohere_accounts[cohere_key]['key']),
        verbose = True,
    )
    cohere_accounts[cohere_key]['instance'] = llm
    print(f"{cohere_key}/{cohere_accounts[cohere_key]['name']} selected.")
    return llm


def create_llm(cohere_key=None, model=None, temperature=None):
    if not model:
        model = cohere_models[cohere_models_get_default()]
    if not cohere_key:
        cohere_key = randomly_select_account(cohere_accounts)
    if cohere_accounts[cohere_key]['instance']:
        print(f"{cohere_key}/{cohere_accounts[cohere_key]['name']} reused.")
        return cohere_accounts[cohere_key]['instance']

    llm = Cohere(
        temperature = temperature if temperature is not None else all_accounts['temperature'],
        cohere_api_key = dekripsi(cohere_accounts[cohere_key]['key']),
        verbose = True,
    )
    cohere_accounts[cohere_key]['instance'] = llm
    print(f"{cohere_key}/{cohere_accounts[cohere_key]['name']} selected.")
    return llm


def test_cohere():
    """
    content="Sure! Here's a table of contents for a book about Advanced Scala, with an estimated length of 400 pages: \n\n1. Introduction to Advanced Scala \n2. Monads in Depth\n   - Understanding Monads\n   - Common Monads in Scala (Option, List, Future, etc.)\n   - Building Custom Monads\n3. Functional Data Structures\n   - Immutability and Persistent Data Structures\n   - Trees, Graphs, and Specialized Data Structures\n   - Practical Functional Data Structures \n4. Advanced Functional Programming\n   - Higher-Kinded Types and Typeclasses\n   - Typelevel Programming with Scala Zippers\n   - Category Theory and Scala \n5. Mixins and Dependency Injection\n   - Understanding Mixins\n   - Implementing Mixins in Scala\n   - Dependency Injection Techniques\n6. Metaprogramming and Macros\n   - Scala's Reflection API\n   - Implementing Domain-Specific Languages (DSLs)\n   - Writing Macros for Code Generation\n7. Advanced Concurrency and Parallelism\n   - Beyond Threads: Actors and Reactive Programming\n   - Parallel Collections and Future-based Programming\n   - Building Concurrent Applications \n8. Scalable Architecture and Design\n   - Designing Scalable Systems with Scala\n   - Integration with Java Libraries\n   - Best Practices for Large-Scale Applications\n9. Advanced Testing and Debugging\n   - Testing Asynchronous Code\n   - Mocking and Stubbing in Scala\n   - Debugging Techniques \n10. Optimizing Scala Applications\n    - Performance Tuning\n    - Code Optimization Techniques\n    - Profiling and Monitoring \n11. Real-World Functional Programming\n   - Case Studies of Functional Architecture\n   - Functional Patterns in Practice\n   - Success Stories and Lessons Learned\n12. Conclusion and Future Directions\n   - Summary of Advanced Topics\n   - Preview of Upcoming Trends in Scala\n\nThis table of contents covers a wide range of advanced topics in Scala, providing an in-depth guide for developers looking to enhance their Scala skills. Each chapter will delve into the practical application of these concepts, offering a comprehensive and practical guide to advanced Scala programming. \n\nRemember, this is just an illustrative table of contents, and the book's actual scope and organization may vary based on specific requirements and depth of coverage for each topic." 
    response_metadata={
        'documents': None, 
        'citations': None, 
        'search_results': None, 
        'search_queries': None, 
        'token_count': {'prompt_tokens': 122, 'response_tokens': 438, 'total_tokens': 560, 'billed_tokens': 488}
    }
    """


    chat_history = [
        HumanMessage(content="hi! my name is wieke"),
        AIMessage(content="Hello Wieke! How can I assist you today?"),
        HumanMessage(content="""You are tasked to write a book about *Advanced Scala* with length approximately 400 pages.
    Please provide the table of contents for the book.""")
    ]
    current_message_and_history = chat_history
    res = cohere_chat_model.invoke(current_message_and_history)


def instantiate_all_as_chats():
    for key in cohere_accounts.keys():
        create_llm_chat(cohere_key=key)


def invoker(query, index=0, choice=['chat', 'once', 'vision']):
    choose = choice[index]
    if choose == 'chat':
        return create_llm_chat().invoke(query)
    elif choose == 'once':
        return create_llm().invoke(query)


if __name__ == '__main__':
    test_cohere()
