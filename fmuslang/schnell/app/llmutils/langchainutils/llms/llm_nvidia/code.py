from openai import OpenAI
import json, requests
import os, sys
if __name__ == '__main__':
    sys.path.insert(0, r'c:\users\usef\work\sidoarjo')
from schnell.app.llmutils.langchainutils.llms import randomly_select_account, nvidia_accounts


nvidia_code_models = {
  "mixtral": {
    "base_url": "https://integrate.api.nvidia.com/v1",
    # Traceback (most recent call last):
    #   File "C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\llms\llm_nvidia\code.py", line 396, in <module>
    #     llm_query_openai(prompt, model=model)
    #   File "C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\llms\llm_nvidia\code.py", line 263, in llm_query_openai
    #     completion = llm.chat.completions.create(
    #                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #   File "C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\openai\_utils\_utils.py", line 275, in wrapper
    #     return func(*args, **kwargs)
    #           ^^^^^^^^^^^^^^^^^^^^^
    #   File "C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\openai\resources\chat\completions.py", line 667, in create
    #     return self._post(
    #           ^^^^^^^^^^^
    #   File "C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\openai\_base_client.py", line 1208, in post
    #     return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
    #                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #   File "C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\openai\_base_client.py", line 897, in request
    #     return self._request(
    #           ^^^^^^^^^^^^^^
    #   File "C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\openai\_base_client.py", line 988, in _request
    #     raise self._make_status_error_from_response(err.response) from None
    # openai.NotFoundError: 404 page not found
    "profile_url": "https://build.nvidia.com/mistralai/mixtral-8x7b-instruct",
    "model": "mistralai/mixtral-8x7b-instruct-v0.1",
    "temperature": 0.5,
    "top_p": 1,
    "max_tokens": 1024,
  },
  "mistral": {
    "base_url": "https://integrate.api.nvidia.com/v1",
    "model": "mistralai/mistral-7b-instruct-v0.2",
    "temperature": 0.5,
    "top_p": 1,
    "max_tokens": 1024,
  },
  "codellama-70b": {
    "base_url": "https://integrate.api.nvidia.com/v1",
    "model": "meta/codellama-70b",
    "temperature": 0.1,
    "top_p": 1,
    "max_tokens": 1024,
  },
  "gemma": {
    "base_url": "https://integrate.api.nvidia.com/v1",
    "profile_url": "https://build.nvidia.com/explore/discover",
    "model": "google/gemma-7b",
    "temperature": 0.5,
    "top_p": 1,
    "max_tokens": 1024,
  },
  "llama2-70b": {
    "base_url": "https://integrate.api.nvidia.com/v1",
    "profile_url": "https://build.nvidia.com/meta/llama2-70b",
    "model": "meta/llama2-70b",
    "temperature": 0.5,
    "top_p": 1,
    "max_tokens": 1024,
  },
}

nvidia_code_nonopenai_models = {
  "starcoder": {
    "invoke_url": "https://api.nvcf.nvidia.com/v2/nvcf/pexec/functions/6acada03-fe2f-4e4d-9e0a-e711b9fd1b59",
    "profile_url": "https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-foundation/models/starcoder2-15b/api",
    "name": "StarCoder2-15B",
    "payload": {
      "prompt": "",
      "temperature": 0.2,
      "top_p": 0.7,
      "max_tokens": 1024,
      "seed": 42,
      "bad": None,
      "stop": None,
      "stream": True
    }
  },
  "codellama-13b": {
    "invoke_url": "https://api.nvcf.nvidia.com/v2/nvcf/pexec/functions/f6a96af4-8bf9-4294-96d6-d71aa787612e",
    "profile_url": "https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-foundation/models/codellama-13b",
    "name": "Code Llama 13B",
    "payload": {
      "messages": [
        {
          "content": "",
          "role": "user"
        }
      ],
      "temperature": 0.2,
      "top_p": 0.7,
      "max_tokens": 1024,
      "seed": 42,
      "stream": True
    }
  },
  "llama2-13b": {
    "invoke_url": "https://api.nvcf.nvidia.com/v2/nvcf/pexec/functions/e0bb7fb9-5333-4a27-8534-c6288f921d3f",
    "profile_url": "https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-foundation/models/llama2-13b",
    "name": "Llama 2 13B",
    "payload": {
      "messages": [
        {
          "content": "",
          "role": "user"
        }
      ],
      "temperature": 0.2,
      "top_p": 0.7,
      "max_tokens": 1024,
      "seed": 42,
      "stream": True
    }

  },
  "nv-llama2-70b": {
    "invoke_url": "https://api.nvcf.nvidia.com/v2/nvcf/pexec/functions/7b3e3361-4266-41c8-b312-f5e33c81fc92",
    "profile_url": "https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-foundation/models/nv-llama2-70b-rlhf/api",
    "name": "NV-Llama2-70B-RLHF",
    "payload": {
      "messages": [
        {
          "content": "",
          "role": "user"
        }
      ],
      "temperature": 0.2,
      "top_p": 0.7,
      "max_tokens": 1024,
      "seed": 42,
      "stream": True
    }
  },
  "phi2": {
    "invoke_url": "https://api.nvcf.nvidia.com/v2/nvcf/pexec/functions/6251d6d2-54ee-4486-90f4-2792bf0d3acd",
    "profile_url": "https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-foundation/models/phi-2/api",
    "name": "Phi-2",
    "payload": {
      "messages": [
        {
          "content": "",
          "role": "user"
        }
      ],
      "temperature": 0.2,
      "top_p": 0.7,
      "max_tokens": 1024,
      "seed": 42,
      "bad": None,
      "stop": None,
      "stream": True
    }
  },
  "yi": {
    "invoke_url": "https://api.nvcf.nvidia.com/v2/nvcf/pexec/functions/347fa3f3-d675-432c-b844-669ef8ee53df",
    "profile_url": "https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-foundation/models/yi-34b/api",
    "name": "Yi-34B",
    "payload": {
      "messages": [
        {
          "content": "",
          "role": "user"
        }
      ],
      "temperature": 0.2,
      "top_p": 0.7,
      "max_tokens": 1024,
      "seed": 42,
      # "bad": None,
      # "stop": None,
      "stream": True
    }
  },
  # "nemotron-qa": {
  #   "invoke_url": "https://api.nvcf.nvidia.com/v2/nvcf/pexec/functions/0c60f14d-46cb-465e-b994-227e1c3d5047",
  #   "profile_url": "https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-foundation/models/nemo-8b-qa/api",
  #   "name": "Nemotron-3-8B-QA",
  #   "payload": {
  #     "messages": [
  #       # {
  #       #   "content": "",
  #       #   "role": "context"
  #       # },
  #       {
  #         "content": "",
  #         "role": "user"
  #       },
  #     ],
  #     "temperature": 0.2,
  #     "top_p": 0.7,
  #     "max_tokens": 1024,
  #     "seed": 42,
  #     "bad": None,
  #     "stop": None,
  #     "stream": True
  #   }
  # },
  "nemotron-chat": {
    "invoke_url": "https://api.nvcf.nvidia.com/v2/nvcf/pexec/functions/1423ff2f-d1c7-4061-82a7-9e8c67afd43a",
    "profile_url": "https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-foundation/models/nemo-8b-steerlm/api",
    "name": "Nemotron-3-8B-Chat-SteerLM",
    "payload": {
      "messages": [
        {
          "content": "",
          "role": "user"
        },
        # {
        #   "labels": {
        #     "complexity": 9,
        #     "creativity": 0,
        #     "verbosity": 9
        #   },
        #   "role": "assistant"
        # },
      ],
      "temperature": 0.2,
      "top_p": 0.7,
      "max_tokens": 1024,
      "seed": 42,
      "bad": None,
      "stop": None,
      "stream": True
    }
  },
}


def create_llm(nvidia_key=None, model=None): # , model=nvidia_code_models["mixtral"]):
  if not nvidia_key:
    nvidia_key = randomly_select_account(nvidia_accounts)
  if not model:
    model = randomly_select_account(nvidia_code_models)
  if nvidia_accounts[nvidia_key]['instance']:
    print(f"{nvidia_key}/{nvidia_accounts[nvidia_key]['name']} reused.")
    return nvidia_accounts[nvidia_key]['instance']

  # if "base_url" in nvidia_accounts[nvidia_key]:
  #   # C:\Users\usef\AppData\Roaming\Python\Python311\site-packages\openai\_client.py
  #   # def __init__(
  #   #     self,
  #   #     *,
  #   #     api_key: str | None = None,
  #   #     organization: str | None = None,
  #   #     base_url: str | httpx.URL | None = None,
  #   #     timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
  #   #     max_retries: int = DEFAULT_MAX_RETRIES,
  #   #     default_headers: Mapping[str, str] | None = None,
  #   #     default_query: Mapping[str, object] | None = None,
  #   #     # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
  #   #     http_client: httpx.Client | None = None,
  #   #     # Enable or disable schema validation for data returned by the API.
  #   #     # When enabled an error APIResponseValidationError is raised
  #   #     # if the API responds with invalid data for the expected schema.
  #   #     # This parameter may be removed or changed in the future.
  #   #     # If you rely on this feature, please open a GitHub issue
  #   #     # outlining your use-case to help us decide if it should be
  #   #     # part of our public interface in the future.
  #   #     _strict_response_validation: bool = False,
  #   # ) -> None:
  base_url = nvidia_code_models[model]['base_url']
  print(f"model = {model}, base_url = {base_url}.")
  llm = OpenAI(
    base_url = base_url,
    api_key = nvidia_accounts[nvidia_key]['key'],
  )
  nvidia_accounts[nvidia_key]['instance'] = llm
  print(f"{nvidia_key}/{nvidia_accounts[nvidia_key]['name']} selected.")
  return llm


def llm_query_openai(user_query, model=None, temperature=None, max_tokens=None, stream=True):
  llm = create_llm()
  if not model:
    model = randomly_select_account(nvidia_code_models)
  completion = llm.chat.completions.create(
    messages = [
      {
        "role": "user",
        "content": user_query
      }
    ],
    model = model,
    temperature = temperature if temperature else nvidia_code_models[model]['temperature'],
    top_p = nvidia_code_models[model]['top_p'],
    max_tokens = max_tokens if max_tokens else nvidia_code_models[model]['max_tokens'],
    stream = stream
  )
  for chunk in completion:
    if chunk.choices[0].delta.content is not None:
      print(chunk.choices[0].delta.content, end="")
      # if line_str.startswith("data: "):
      #   data_str = line_str[len("data: "):]  # Remove "data: " prefix
      #   try:
      #     data_dict = json.loads(data_str)
      #     if 'choices' in data_dict:
      #       for choice in data_dict['choices']:
      #         if choice['finish_reason'] != 'stop':
      #           print(choice['delta']['content'], end='')
      #   except json.decoder.JSONDecodeError as e:  # data: [DONE]
      #     pass

def llm_query_nonopenai(user_query, nvidia_key=None, model=None, temperature=0.1, max_tokens=None, stream=True):
  if not nvidia_key:
    nvidia_key = randomly_select_account(nvidia_accounts)
  if not model:
    model = randomly_select_account(nvidia_code_nonopenai_models)

  print(f"selected api-key: {nvidia_key}/{nvidia_accounts[nvidia_key]['name']}, model: {model}.")

  headers = {
    "Authorization": f"Bearer {nvidia_accounts[nvidia_key]['key']}",
    "accept": "text/event-stream",
    "content-type": "application/json",
  }

  invoke_url = nvidia_code_nonopenai_models[model]['invoke_url']
  payload = nvidia_code_nonopenai_models[model]['payload']
  if model in ['starcoder']:
    payload['prompt'] = user_query
    # payload["seed"]   42
    # payload["bad"]    None
    # payload["stop"]   None
  else:
    payload['messages'][0]['content'] = user_query
  # payload = {
  #   "prompt": user_query,
  #   "temperature": 0.2,
  #   "top_p": 0.7,
  #   "max_tokens": 1024,
  #   "seed": 42,
  #   "bad": None,
  #   "stop": None,
  #   "stream": True
  # }
  payload['stream'] = stream
  if temperature:
    payload['temperature'] = temperature
  if max_tokens:
    payload['max_tokens'] = max_tokens
  response = requests.post(invoke_url, headers=headers, json=payload, stream=stream)

  # data: {"id":"ea9a43b8-f1a5-4097-b742-76527c05890d","choices":[{"index":0,"delta":"","finish_reason":"stop"}]}
  # data: [DONE]
  for line in response.iter_lines():
    if line:
      line_str = line.decode("utf-8")
      # starcoder handling
      if model in ['starcoder']:
        if line_str.startswith("data: "):
          data_str = line_str[len("data: "):]  # Remove "data: " prefix
          try:
            data_dict = json.loads(data_str)
            if 'choices' in data_dict:
              for choice in data_dict['choices']:
                if choice['finish_reason'] != 'stop':
                  print(choice['delta'], end='')
          except json.decoder.JSONDecodeError as e:  # data: [DONE]
            pass
      elif model in ['codellama-13b', 'llama2-13b', 'nv-llama2-70b', 'phi2', 'yi', 'nemotron-qa', 'nemotron-chat']:
        if line_str.startswith("data: "):
          data_str = line_str[len("data: "):]  # Remove "data: " prefix
          try:
            data_dict = json.loads(data_str)
            if 'choices' in data_dict:
              for choice in data_dict['choices']:
                if choice['finish_reason'] != 'stop':
                  print(choice['delta']['content'], end='')
          except json.decoder.JSONDecodeError as e:  # data: [DONE]
            pass
      # ini beda sendiri: llama2-13b
      # try:
      # original way of handling
      # if model in ['llama2-13b']:
      else:
        for line in response.iter_lines():
          if line:
            print(line.decode("utf-8"))

      #   # print(line.decode("utf-8"))
      #   response_item = line.decode("utf-8")
      #   if response_item.strip():
      #     data = json.loads(response_item)
      #     if 'choices' in data:
      #       for choice in data['choices']:
      #         if choice['finish_reason'] != 'stop':
      #           print(choice['delta'])
      # except json.JSONDecodeError as e:
      #   # print("Error decoding JSON:", e)
      #   pass

if __name__ == '__main__':
  prompt = 'Show some code of advanced features of Rust'
  # model = 'starcoder'
  # model = 'nv-llama2-70b'
  # model = 'yi'
  # model = 'nemotron-chat'
  # model = 'codellama-13b'
  # model = 'llama2-13b'
  # model = 'phi2'
  # llm_query_nonopenai(prompt, model=model)
  # versi openai-like endpoint, tapi not found itu base-url
  model = "mixtral"
  # model = "mistral"
  # model = "codellama-70b"
  # model = "gemma"
  # model = "llama2-70b"
  llm_query_openai(prompt, model=model)
