from .text import HyperbolicLLM
from .image import HyperbolicImageGenerator
from .audio import HyperbolicAudioGenerator

# # Initialize the client for text generation
# text_generator = HyperbolicLLM(api_key="your_api_key")
# response = text_generator.generate_text(system_content="You are a gourmet.", user_content="Tell me about Chinese hotpot")
# print("Generated Text:", response)

# # Generate an image
# image_generator = HyperbolicImageGenerator(api_key="your_api_key")
# image_generator.generate_image(prompt="a photo of an astronaut riding a horse on mars", output_file="astronaut.jpg")

# # Generate an audio file
# audio_generator = HyperbolicAudioGenerator(api_key="your_api_key")
# audio_generator.generate_audio(text="Hi! Welcome to Hyperbolic. I am happy to help you today.", output_file="greeting.mp3")

from schnell.app.llmutils.langchainutils.llm_config import hyperbolic_accounts
from schnell.app.llmutils.langchainutils.utils import randomly_select_account
from schnell.app.llmutils.langchainutils.llm_config import all_accounts


# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\llm_config\hyperbolic_accounts.py
def hyperbolic(hyperbolic_key=None, model=None, temperature=None, max_tokens=None, top_p=None, memory=None):
    if not hyperbolic_key:
        hyperbolic_key = randomly_select_account(hyperbolic_accounts)

    # if not model:
    #     model = google_models[google_models_get_default()]

    # temperature = temperature if temperature is not None else all_accounts['temperature']
    # max_output_tokens = max_tokens if max_tokens is not None else all_accounts['max_output_tokens']
    # top_p = top_p if top_p is not None else all_accounts['top_p']

    if hyperbolic_accounts[hyperbolic_key]['instance']:
        # print(f"{hyperbolic_key}/{hyperbolic_accounts[hyperbolic_key]['name']} reused with model {model}.")
        return hyperbolic_accounts[hyperbolic_key]['instance']

    llm = HyperbolicLLM(api_key=hyperbolic_accounts[hyperbolic_key]['key'])
    hyperbolic_accounts[hyperbolic_key]['instance'] = llm
    # print(f"{hyperbolic_key}/{hyperbolic_accounts[hyperbolic_key]['name']} selected with model {model} with temp {used_temperature} and memory={memory}.")
    return llm

# g "/ref)schnell.app.llmutils.langchainutils.llms.llm_hyperbolic/gentext/query=create a funny short story|print_output=True"
# from schnell.app.llmutils.langchainutils.llms.llm_hyperbolic import gentext
def gentext(query, system_content="You are an expert assistant.", print_output=False):
    response = hyperbolic().generate_text(system_content=system_content, user_content=query)
    if print_output:
        print(response)
    return response

# https://pypi.org/project/llm-hyperbolic/0.4.8/
# https://github.com/ghostofpokemon/llm-hyperbolic/blob/main/llm_hyperbolic.py
# https://docs.hyperbolic.xyz/docs/getting-started

# https://docs.hyperbolic.xyz/docs/hyperbolic-ai-inference-pricing
# "meta-llama/Meta-Llama-3.1-70B-Instruct"
# $10 credit for free trial
# Text-to-text:
# Instruct models:
# Llama 3.1 8B (BF16): $0.1 per 1M tokens
# Llama 3.1 70B (BF16): $0.4 per 1M tokens
# Llama 3 70B (BF16): $0.4 per 1M tokens
# Hermes 3 70B (BF16): $0.4 per 1M tokens
# Llama 3.1 405B (BF16): $4 per 1M tokens
# DeepSeek V2.5(BF16): $2 per 1M tokens
# Qwen 2.5 72B (BF16): $0.4 per 1M tokens
# Llama 3.2 3B (BF16): $0.1 per 1M tokens
# Base models:
# Llama 3.1 405B parameters BASE (FP8): $2 per 1M tokens
# Llama 3.1 405B parameters BASE (BF16): $4 per 1M tokens
