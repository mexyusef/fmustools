import groq
from configuration_values import config_keys

# https://console.groq.com/docs/models
# Supported Models
# GroqCloud currently supports the following models:

# LLaMA2-70b
# Developer: Meta
# Model Name: LLaMA2-70b-chat
# Context Window: 4,096 tokens
# API String: llama2-70b-4096

# Mixtral-8x7b
# Developer: Mistral
# Model Name: Mixtral-8x7b-Instruct-v0.1
# Context Window: 32,768 tokens
# API String: mixtral-8x7b-32768

# Gemma-7b-it
# Developer: Google
# Model Name: Gemma-7b-it
# Context Window: 8,192 tokens
# API String: Gemma-7b-it


def generate_groq_response(
    prompt="Explain the importance of low latency LLMs",
    model=config_keys["models"]["groq"]["default"],
    max_tokens=1024,
    stream=False,
):
    client = groq.Groq(api_key=config_keys["keys"]["groq-hayya"])
    # response = client.generate(model=model, prompt=prompt, max_tokens=max_tokens, stream=stream)
    # return response.generations[0].text
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )

    response = chat_completion.choices[0].message.content
    return response


def test_generate_groq_response():
    result = generate_groq_response(
        prompt="How to create ToDo REST application using Scala with any popular framework?"
    )
    print(result)
