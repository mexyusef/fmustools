# https://python.langchain.com/docs/integrations/llms/ollama

# C:\work\ciledug\ciledug\fmusperintah\vendor\langgraph\examples\rag\langgraph_adaptive_rag_local.ipynb
# %pip install --upgrade --quiet langchain-community
# from langchain_community.chat_models.ollama import ChatOllama
from langchain_community.chat_models import ChatOllama

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import StrOutputParser


llm = ChatOllama(model=local_llm, format="json", temperature=0)
# llm = ChatOllama(model=local_llm, format="json", temperature=0)

# prompt = hub.pull("rlm/rag-prompt")
prompt = PromptTemplate(
    template="""You are an expert at routing a user question to a vectorstore or web search. \n
    Use the vectorstore for questions on LLM  agents, prompt engineering, and adversarial attacks. \n
    You do not need to be stringent with the keywords in the question related to these topics. \n
    Otherwise, use web-search. Give a binary choice 'web_search' or 'vectorstore' based on the question. \n
    Return the a JSON with a single key 'datasource' and no premable or explaination. \n
    Question to route: {question}""",
    input_variables=["question"],
)

# rag_chain = prompt | llm | StrOutputParser()
question_router = prompt | llm | JsonOutputParser()


question = "llm agent memory"
docs = retriever.get_relevant_documents(question)
doc_txt = docs[1].page_content

result = question_router.invoke({"question": question})

# question = "agent memory"
# result = rag_chain.invoke({"context": docs, "question": question})

