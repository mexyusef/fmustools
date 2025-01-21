# https://docs.x.ai/docs/quickstart#making-your-first-request
# https://docs.x.ai/api/integrations#openai-sdk
# xai_enterprise_api/endpoints/chat.py

# xai_enterprise_api/
# ├── __init__.py
# ├── client.py            # API client with request handling and session management
# ├── endpoints/
# │   ├── __init__.py
# │   ├── api_key.py       # API key management
# │   ├── chat.py          # Chat completions
# │   ├── completions.py   # Text completions
# │   ├── embeddings.py    # Embeddings
# │   └── models.py        # Language and embedding model listings and details
# └── exceptions.py        # Custom exception classes
# xai_enterprise_api/client.py

import requests
# from .exceptions import XAIAPIError
# xai_enterprise_api/exceptions.py

BASE_URL = "https://api.x.ai/v1"

class XAIAPIError(Exception):
    """Base class for exceptions in the xAI Enterprise API client."""
    pass

# xai_enterprise_api/endpoints/api_key.py

class APIKeyEndpoint:
    def __init__(self, client):
        self.client = client

    def get_api_key_info(self):
        return self.client.get("/api-key")
# xai_enterprise_api/endpoints/chat.py

# class ChatEndpoint:
#     def __init__(self, client):
#         self.client = client

#     def create_chat_completion(self, messages, model, **kwargs):
#         data = {
#             "messages": messages,
#             "model": model,
#             **kwargs
#         }
#         return self.client.post("/chat/completions", data=data)

class ChatEndpoint:
    def __init__(self, client):
        self.client = client

    def create_chat_completion(self, messages, model, stream=False, temperature=0, **kwargs):
        data = {
            "messages": messages,
            "model": model,
            "stream": stream,
            "temperature": temperature,
            **kwargs
        }
        return self.client.post("/chat/completions", data=data)

# xai_enterprise_api/endpoints/completions.py

class CompletionsEndpoint:
    def __init__(self, client):
        self.client = client

    def create_completion(self, prompt, model, **kwargs):
        data = {
            "prompt": prompt,
            "model": model,
            **kwargs
        }
        return self.client.post("/completions", data=data)
# xai_enterprise_api/endpoints/embeddings.py

class EmbeddingsEndpoint:
    def __init__(self, client):
        self.client = client

    def create_embedding(self, input_text, model, **kwargs):
        data = {
            "input": input_text,
            "model": model,
            **kwargs
        }
        return self.client.post("/embeddings", data=data)
    
    def list_embedding_models(self):
        return self.client.get("/embedding-models")
    
    def get_embedding_model(self, model_id):
        return self.client.get(f"/embedding-models/{model_id}")
# xai_enterprise_api/endpoints/models.py

class ModelsEndpoint:
    def __init__(self, client):
        self.client = client

    def list_models(self):
        return self.client.get("/models")
    
    def get_model(self, model_id):
        return self.client.get(f"/models/{model_id}")

class XAIClient:
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})
        
    def _request(self, method, endpoint, params=None, data=None):
        url = f"{BASE_URL}{endpoint}"
        try:
            response = self.session.request(method, url, params=params, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise XAIAPIError(f"Error in request to {url}: {e}")
    
    def get(self, endpoint, params=None):
        return self._request("GET", endpoint, params=params)
    
    def post(self, endpoint, data=None):
        return self._request("POST", endpoint, data=data)

class XAIEnterpriseAPI:
    def __init__(self, api_key):
        client = XAIClient(api_key)
        self.api_key = APIKeyEndpoint(client)
        self.chat = ChatEndpoint(client)
        self.completions = CompletionsEndpoint(client)
        self.embeddings = EmbeddingsEndpoint(client)
        self.models = ModelsEndpoint(client)


# # from xai_enterprise_api import XAIEnterpriseAPI
# api = XAIEnterpriseAPI(api_key="your_api_key")
# # API Key info
# api_info = api.api_key.get_api_key_info()
# # Chat completion
# response = api.chat.create_chat_completion(
#     messages=[{"role": "user", "content": "Hello"}],
#     model="chat-model-id"
# )

# # Text completion
# completion = api.completions.create_completion(
#     prompt="Translate to French: 'Hello, how are you?'",
#     model="text-model-id"
# )

# # Embeddings
# embedding = api.embeddings.create_embedding(input_text="Sample text", model="embedding-model-id")
# models = api.models.list_models()



# api = XAIEnterpriseAPI(api_key="your_api_key")
# response = api.chat.create_chat_completion(
#     messages=[
#         {"role": "system", "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."},
#         {"role": "user", "content": "What is the meaning of life, the universe, and everything?"}
#     ],
#     model="grok-beta",
#     stream=False,
#     temperature=0
# )

def generate_chat_response(user_prompt,
                           api_key, 
                           model="grok-beta", 
                           system_prompt="You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy.", 
                           stream=False,
                           temperature=0):
    """
    Generate a chat response from the xAI Enterprise API.

    Parameters:
        api_key (str): API key for authentication (required).
        user_prompt (str): The user's prompt message (required).
        model (str): The model ID to use for generating the response (default: "grok-beta").
        system_prompt (str): The system's prompt or context for the chat (default: "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy.").
        stream (bool): Whether to enable streaming responses (default: False).
        temperature (float): The randomness of the model's output (default: 0).

    Returns:
        dict: The API response.
    """
    # Initialize the API client with the provided API key
    # if api_key == None:
    #     api_key = 
    api = XAIEnterpriseAPI(api_key=api_key)
    
    # Create the chat completion with the provided parameters
    response = api.chat.create_chat_completion(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        model=model,
        stream=stream,
        temperature=temperature
    )
    
    return response
