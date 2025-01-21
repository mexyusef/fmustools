import cohere
from configuration_values import config_keys

def generate_cohere_response(prompt='', model='command', max_tokens=1024, stream=False):
    co = cohere.Client(config_keys['keys']['cohere'])
    response = co.generate(model=model, prompt=prompt, max_tokens=max_tokens, stream=stream)
    return response.generations[0].text

def test_generate_cohere_response():
    result = generate_cohere_response(prompt='how to create todo rest application using scala with any popular framework?')
    print(result)
