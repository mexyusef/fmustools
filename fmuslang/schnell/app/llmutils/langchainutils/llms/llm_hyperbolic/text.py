import openai
import requests
import base64
import os


class HyperbolicLLM:
    def __init__(self, api_key: str, base_url: str = "https://api.hyperbolic.xyz/v1"):
        """Initialize the Hyperbolic LLM client."""
        self.client = openai.OpenAI(api_key=api_key, base_url=base_url)

    def generate_text(self, user_content: str,
        model: str = "meta-llama/Meta-Llama-3.1-70B-Instruct",
        temperature: float = 0.7,
        max_tokens: int = 1024,
        system_content: str = "You are an expert assistant.", 
    ) -> str:
        """
        Generate text based on system and user prompts.
        
        Args:
            system_content (str): Instruction or context for the system.
            user_content (str): User query or input.
            model (str): The model to use for generation. Default is Meta-Llama.
            temperature (float): The sampling temperature. Default is 0.7.
            max_tokens (int): Maximum number of tokens in the response.

        Returns:
            str: The generated text response.
        """
        chat_completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return chat_completion.choices[0].message.content

