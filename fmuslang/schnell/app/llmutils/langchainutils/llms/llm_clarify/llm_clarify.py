# https://python.langchain.com/docs/integrations/llms/clarifai
# Install required dependencies
# pip install --user --upgrade clarifai

# Declare clarifai pat token as environment variable or you can pass it as argument in clarifai class.
import os, sys
from pprint import pprint

# Import the required modules
from langchain.chains import LLMChain
# vscode C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\langchain_community\llms\
from langchain_community.llms import Clarifai
from langchain_core.prompts import PromptTemplate


if __name__ == '__main__':
    sys.path.insert(0, r'c:\users\usef\work\sidoarjo')

from schnell.app.llmutils.langchainutils.llms import clarifyai_accounts, randomly_select_account
from schnell.app.printutils import indah4
from schnell.app.cryptoutils import dekripsi


os.environ["CLARIFAI_PAT"] = dekripsi(clarifyai_accounts['clarifyai_23']['key'])


######################### bikin llm gaya 1
USER_ID     = "openai"
APP_ID      = "chat-completion"
MODEL_ID    = "GPT-3_5-turbo"
# Initialize a Clarifai LLM
clarifai_llm = Clarifai(user_id=USER_ID, app_id=APP_ID, model_id=MODEL_ID)


######################### bikin llm gaya 2
# You can provide a specific model version as the model_version_id arg.
# MODEL_VERSION_ID = "MODEL_VERSION_ID"
# or
# MODEL_URL = "https://clarifai.com/openai/chat-completion/models/GPT-4"
# # Initialize through Model URL
# clarifai_llm = Clarifai(model_url=MODEL_URL)


###################################### dari contoh
# template = """Question: {question}

# Answer: Let's think step by step."""
# prompt = PromptTemplate.from_template(template)
# llm_chain = LLMChain(prompt=prompt, llm=clarifai_llm)
# question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"
# llm_chain.invoke(question)
# Intialize the parameters as dict.
# params = dict(temperature=str(0.3), max_tokens=100)
# params = dict(temperature=str(0.1))
# # clarifai_llm = Clarifai(user_id=USER_ID, app_id=APP_ID, model_id=MODEL_ID)
# llm_chain = LLMChain(
#     prompt=prompt, llm=clarifai_llm, llm_kwargs={"inference_params": params}
# )


params = dict(temperature=str(0.1))
# We can use _generate to generate the response for list of prompts.
prompts = [
        # "Help me summarize the events of american revolution in 5 sentences",
        # "Explain about rocket science in a funny way",
        # "Create a script for welcome speech for the college sports day",
        "Give me an interesting Scala code",
        "Give me an interesting Haskell code",
        "Give me an interesting Rust code",
    ]
result = clarifai_llm._generate(
    prompts,
    inference_params=params,
)
# pprint(result)

# LLMResult(
#     generations=[
#         [
#             Generation(text="The American Revolution was a colonial revolt against British rule that took place between 1765 and 1783. It began with the Stamp Act of 1765, which imposed taxes on the American colonies without their consent, leading to widespread protests and boycotts. The conflict escalated with events such as the Boston Tea Party in 1773 and the Battles of Lexington and Concord in 1775. The Declaration of Independence was adopted on July 4, 1776, declaring the colonies' independence from")
#         ], 
#         [
#             Generation(text='Rocket science is like trying to make a giant metal tube go whoosh into space without accidentally turning it into a very expensive firework. It\'s all about strapping a bunch of fuel to a pointy end and hoping for the best while doing some fancy math and engineering magic to make sure it goes in the right direction. So basically, it\'s like playing a high-stakes game of "Don\'t Mess This Up" with a side of "Please Work, Please Work, Please Work!"')
#         ], 
#         [
#             Generation(text='Certainly! Here is a sample script for a welcome speech for a college sports day:\n\n---\n\nGood morning/afternoon/evening everyone,\n\nOn behalf of [Name of College/University], I am delighted to welcome you all to our annual Sports Day. It is a day filled with excitement, competition, and camaraderie as we come together to celebrate the spirit of sportsmanship and athleticism.\n\nToday, we gather here not only to showcase our physical abilities but also to demonstrate our teamwork, dedication,')
#         ]
#     ],
#     llm_output=None,
#     run=None
# )
for idx, generation in enumerate(result.generations):
    gentext = generation[0].text
    indah4(prompts[idx] + '\n\n\n', warna='yellow')
    indah4(gentext, warna='green')
