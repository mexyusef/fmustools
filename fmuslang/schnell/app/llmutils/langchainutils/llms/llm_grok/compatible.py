import os
from openai import OpenAI
from anthropic import Anthropic
from typing import Optional

class LLMProvider:
    """A library to interface with LLM providers x.ai's Grok via OpenAI and Anthropic APIs."""

    def __init__(self, provider: str, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("XAI_API_KEY")
        self.provider = provider.lower() # openai, anthropic
        self.client = self._initialize_client()

    def _initialize_client(self):
        """Initializes the appropriate client based on the provider name."""
        if self.provider == "openai":
            return OpenAI(api_key=self.api_key, base_url="https://api.x.ai/v1")
        elif self.provider == "anthropic":
            return Anthropic(api_key=self.api_key, base_url="https://api.x.ai")
        else:
            raise ValueError("Invalid provider specified. Choose either 'openai' or 'anthropic'.")

    def get_completion(self, prompt: str, model: str = "grok-beta", max_tokens: int = 128) -> str:
        """
        Gets a completion response from the specified LLM provider.
        
        Args:
            prompt (str): The user input prompt.
            model (str): The model name to use (default is "grok-beta").
            max_tokens (int): Maximum tokens for the response (default is 128).
        
        Returns:
            str: The LLM completion response.
        """
        messages = [
            {"role": "system", "content": "You are Grok, a chatbot inspired by the Hitchhiker's Guide to the Galaxy."},
            {"role": "user", "content": prompt},
        ]

        if self.provider == "openai":
            return self._get_openai_completion(messages, model)
        elif self.provider == "anthropic":
            return self._get_anthropic_completion(messages, model, max_tokens)
        else:
            raise ValueError("Provider not supported.")

    def _get_openai_completion(self, messages, model) -> str:
        """Gets completion from OpenAI client."""
        try:
            completion = self.client.chat.completions.create(model=model, messages=messages)
            return completion.choices[0].message
        except Exception as e:
            print(f"Error with OpenAI completion: {e}")
            return ""

    def _get_anthropic_completion(self, messages, model, max_tokens) -> str:
        """Gets completion from Anthropic client."""
        try:
            message = self.client.messages.create(model=model, max_tokens=max_tokens, system=messages[0]["content"], messages=messages)
            return message.content
        except Exception as e:
            print(f"Error with Anthropic completion: {e}")
            return ""
