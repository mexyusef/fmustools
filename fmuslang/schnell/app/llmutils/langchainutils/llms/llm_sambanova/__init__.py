import os
from openai import OpenAI
from anthropic import Anthropic

class LLMProvider:
    """A library to interface with LLM providers like x.ai's Grok via OpenAI, Anthropic, and SambaNova APIs."""

    def __init__(self, provider: str):
        self.api_key = os.getenv(f"{provider.upper()}_API_KEY")
        self.provider = provider.lower()
        self.client = self._initialize_client()

    def _initialize_client(self):
        """Initializes the appropriate client based on the provider name."""
        if self.provider == "openai":
            return OpenAI(api_key=self.api_key, base_url="https://api.x.ai/v1")
        elif self.provider == "anthropic":
            return Anthropic(api_key=self.api_key, base_url="https://api.x.ai")
        elif self.provider == "sambanova":
            return OpenAI(api_key=self.api_key, base_url="https://api.sambanova.ai/v1")  # Reusing OpenAI SDK for SambaNova
        else:
            raise ValueError("Invalid provider specified. Choose either 'openai', 'anthropic', or 'sambanova'.")

    def get_completion(self, prompt: str, model: str = "grok-beta", max_tokens: int = 128, temperature: float = 0.7, top_p: float = 0.9) -> str:
        """
        Gets a completion response from the specified LLM provider.

        Args:
            prompt (str): The user input prompt.
            model (str): The model name to use (default is "grok-beta" for OpenAI/Anthropic, "Meta-Llama-3.1-8B-Instruct" for SambaNova).
            max_tokens (int): Maximum tokens for the response (default is 128).
            temperature (float): Sampling temperature for output randomness (default is 0.7).
            top_p (float): Nucleus sampling cutoff (default is 0.9).

        Returns:
            str: The LLM completion response.
        """
        messages = [
            {"role": "system", "content": "You are a helpful assistant." if self.provider == "sambanova" else "You are Grok, a chatbot inspired by the Hitchhiker's Guide to the Galaxy."},
            {"role": "user", "content": prompt},
        ]

        if self.provider == "openai":
            return self._get_openai_completion(messages, model)
        elif self.provider == "anthropic":
            return self._get_anthropic_completion(messages, model, max_tokens)
        elif self.provider == "sambanova":
            return self._get_sambanova_completion(messages, model, temperature, top_p)
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

    def _get_sambanova_completion(self, messages, model, temperature, top_p) -> str:
        """Gets completion from SambaNova client."""
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                top_p=top_p
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error with SambaNova completion: {e}")
            return ""

# Usage example:
# openai_client = LLMProvider("openai")
# anthropic_client = LLMProvider("anthropic")
# sambanova_client = LLMProvider("sambanova")
# print(openai_client.get_completion("What is the meaning of life, the universe, and everything?"))
# print(anthropic_client.get_completion("What is the meaning of life, the universe, and everything?"))
# print(sambanova_client.get_completion("Hello"))


# https://docs.sambanova.ai/sambastudio/latest/vision-models.html
