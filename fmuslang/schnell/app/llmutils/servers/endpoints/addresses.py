from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os
import shutil
import fnmatch


# Define the data model
class URLData(BaseModel):
    url: str
    description: str

# Sample data
urls = [
    {
        "url": "https://notebooklm.google.com/",
        "description": "Notebook LM"
    },
    {
        "url": "https://inference.cerebras.ai/",
        "description": "Quick inference with cerebras.ai"
    },
    {
        "url": "https://www.reddit.com",
        "description": "Reddit - Forum and Community"
    },
]


def endpoint_addresses(app, basefolder):
    # Endpoint to get the URLs and descriptions
    @app.get("/important_addresses", response_model=List[URLData])
    async def get_urls():
        return urls
