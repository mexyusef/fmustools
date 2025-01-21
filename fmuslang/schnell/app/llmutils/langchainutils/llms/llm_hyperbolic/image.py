import openai
import requests
import base64
import os


class HyperbolicImageGenerator:
    def __init__(self, api_key: str, base_url: str = "https://api.hyperbolic.xyz/v1"):
        """Initialize the Hyperbolic image generator client."""
        self.api_key = api_key
        self.base_url = base_url

    def generate_image(self, prompt: str, model_name: str = "SDXL1.0-base", height: int = 1024, width: int = 1024, backend: str = "auto", output_file: str = "result.jpg") -> None:
        """
        Generate an image based on the provided prompt and model.
        
        Args:
            prompt (str): The text prompt to generate the image.
            model_name (str): The model to use for generation.
            height (int): Height of the image.
            width (int): Width of the image.
            backend (str): The backend for processing the image.
            output_file (str): Path to save the generated image.
        """
        url = f"{self.base_url}/image/generation"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "model_name": model_name,
            "prompt": prompt,
            "height": height,
            "width": width,
            "backend": backend
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Ensure we handle errors

        image_data = response.json()["images"][0]["image"]
        with open(output_file, "wb") as image_file:
            image_file.write(base64.b64decode(image_data))
        print(f"Image saved as {output_file}")

