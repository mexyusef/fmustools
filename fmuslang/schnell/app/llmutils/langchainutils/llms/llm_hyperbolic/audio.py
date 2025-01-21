import openai
import requests
import base64
import os

class HyperbolicAudioGenerator:
    def __init__(self, api_key: str, base_url: str = "https://api.hyperbolic.xyz/v1"):
        """Initialize the Hyperbolic audio generator client."""
        self.api_key = api_key
        self.base_url = base_url

    def generate_audio(self, text: str, output_file: str = "result.mp3") -> None:
        """
        Generate an audio file based on the provided text.
        
        Args:
            text (str): The input text to generate speech from.
            output_file (str): Path to save the generated audio.
        """
        url = f"{self.base_url}/audio/generation"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {"text": text}

        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        audio_data = response.json()["audio"]
        with open(output_file, "wb") as audio_file:
            audio_file.write(base64.b64decode(audio_data))
        print(f"Audio saved as {output_file}")
