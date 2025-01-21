https://docs.together.ai/docs/vision-overview
from together import Together

client = Together()

getDescriptionPrompt = "You are a UX/UI designer. Describe the attached screenshot or UI mockup in detail. I will feed in the output you give me to a coding model that will attempt to recreate this mockup, so please think step by step and describe the UI in detail. Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. Match the colors and sizes exactly. Make sure to mention every part of the screenshot including any headers, footers, etc. Use the exact text from the screenshot."

imageUrl = "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png"


stream = client.chat.completions.create(
    model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": getDescriptionPrompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": imageUrl,
                    },
                },
            ],
        }
    ],
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
#
Meta	(Free) Llama 3.2 11B Vision Instruct Turbo*	meta-llama/Llama-Vision-Free	131072
Meta	Llama 3.2 11B Vision Instruct Turbo	meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo	131072
Meta	Llama 3.2 90B Vision Instruct Turbo	meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo	131072
#

https://docs.together.ai/docs/examples

https://docs.together.ai/docs/inference-streaming-tokens

https://docs.together.ai/docs/integrations

# Langchain

LangChain is a framework for developing context-aware, reasoning applications powered by language models.

To install LangChain run:

pip install langchain

Here's sample code to get you started with Langchain + Together AI:
```py
from langchain.llms import Together

llm = Together(
    model="togethercomputer/RedPajama-INCITE-7B-Base",
    temperature=0.7,
    max_tokens=128,
    top_k=1,
    # together_api_key="..."
)

input_ = """You are a teacher with a deep knowledge of machine learning and AI. \
You provide succinct and accurate answers. Answer the following question: 

What is a large language model?"""
print(llm(input_))
```
Output:
```sh
A: A large language model is a neural network that is trained on a large amount of text data. It is able to generate text that is similar to the training data, and can be used for tasks such as language translation, question answering, and text summarization.

A: A large language model is a neural network that is trained on a large amount of text data. It is able to generate text that is similar to the training data, and can be used for tasks such as language translation, question answering, and text summarization.

A: A large language model is a neural network that is trained on
```

# LlamaIndex

LlamaIndex is a simple, flexible data framework for connecting custom data sources to large language models (LLMs).

Here's sample code to get you started with Llama Index + Together AI:
```py
!pip install llama-index langchain

from llama_index.llms import OpenAILike

llm = OpenAILike(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    api_base="https://api.together.xyz/v1",
    api_key="<API KEY>",
    is_chat_model=True,
    is_function_calling_model=True,
    temperature=0.1,
)

response = llm.complete("Write up to 500 words essay explaining Large Language Models")

print(response)
```

https://docs.together.ai/reference/chat-completions
```py
import requests

url = "https://api.together.xyz/v1/chat/completions"

payload = {
    "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
    "stop": ["</s>"]
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer eb2fdc71ab7fb8165627ba7b11ea93cf328563f98a7522cbaac602369356a7f8"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

https://docs.together.ai/reference/completions

```py
import requests

url = "https://api.together.xyz/v1/completions"

payload = {
    "model": "mistralai/Mixtral-8x7B-v0.1",
    "prompt": "List all of the states in the USA and their capitals in a table.",
    "max_tokens": 200,
    "stop": ["</s>"]
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer eb2fdc71ab7fb8165627ba7b11ea93cf328563f98a7522cbaac602369356a7f8"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```
https://docs.together.ai/reference/complete

# Complete

together.Complete.create()

    prompt (string, required) -- A string providing context for the model to complete
    model (string, optional) -- Model string to query. Default: togethercomputer/RedPajama-INCITE-7B-Chat
    max_tokens (integer, optional) -- Maximum number of tokens the model should generate. Default: 128
    stop (List[str], optional) -- List of stop words the model should stop generation at. Default: ["<human>"]
    temperature(float, optional) -- A decimal number that determines the degree of randomness in the response. Default: 0.7
    top_p (float, optional) -- Used to dynamically adjust the number of choices for each predicted token based on the cumulative probabilities. A value of 1 will always yield the same output. A temperature less than 1 favors more correctness and is appropriate for question answering or summarization. A value greater than 1 introduces more randomness in the output. Default: 0.7
    top_k (integer, optional) -- Used to limit the number of choices for the next predicted word or token. It specifies the maximum number of tokens to consider at each step, based on their probability of occurrence. This technique helps to speed up the generation process and can improve the quality of the generated text by focusing on the most likely options. Default: 50
    repetition_penalty (float, optional) -- A number that controls the diversity of generated text by reducing the likelihood of repeated sequences. Higher values decrease repetition. Default: 1

Example:
```py
import together

together.api_key = "xxxxx"

# generate response
response = together.Complete.create(prompt="List places to visit in San Francisco.")

print(response)
```

together.Complete.create_streaming()

    prompt (string, required) -- A string providing context for the model to complete
    model (string, optional) -- Model string to query. Default: togethercomputer/RedPajama-INCITE-7B-Chat
    max_tokens (integer, optional) -- Maximum number of tokens the model should generate. Default: 128
    stop (List[str], optional) -- List of stop words the model should stop generation at. Default: ["<human>"]
    temperature(float, optional) -- A decimal number that determines the degree of randomness in the response. Default: 0.7
    top_p (float, optional) -- Used to dynamically adjust the number of choices for each predicted token based on the cumulative probabilities. A value of 1 will always yield the same output. A temperature less than 1 favors more correctness and is appropriate for question answering or summarization. A value greater than 1 introduces more randomness in the output. Default: 0.7
    top_k (integer, optional) -- Used to limit the number of choices for the next predicted word or token. It specifies the maximum number of tokens to consider at each step, based on their probability of occurrence. This technique helps to speed up the generation process and can improve the quality of the generated text by focusing on the most likely options. Default: 50
    repetition_penalty (float, optional) -- A number that controls the diversity of generated text by reducing the likelihood of repeated sequences. Higher values decrease repetition. Default: 1

Example:
```py
import together

together.api_key = "xxxxx"

prompt = "List places to visit in San Francisco."

for token in together.Complete.create_streaming(prompt=prompt):
    print(token, end="", flush=True)
print("\n")
```

https://docs.together.ai/reference/image

# Image
together.Image.create()

    prompt (string, required) -- A string providing context for the model to complete
    model (string, optional) -- Model string to query. Default: runwayml/stable-diffusion-v1-5
    steps (integer, optional) -- Sampling steps is the number of iterations that the model runs to go from random noise to a recognizable image based on the text. Default: 20
    seed (integer, optional) -- Random seed used for generation. Default: 42
    results (integer, optional) -- Number of result images to generate. Default: 1
    height (integer, optional) -- Height of the image to generate in number of pixels. Default: 256
    width (integer, optional) -- Width of the image to generate in number of pixels. Default: 256

Example:
```py
import together
import base64

together.api_key = "xxxxx"

# generate image 
response = together.Image.create(prompt="Space robots")

# save the first image
image = response["output"]["choices"][0]
with open("spacerobots.png", "wb") as f:
    f.write(base64.b64decode(image["image_base64"]))
```