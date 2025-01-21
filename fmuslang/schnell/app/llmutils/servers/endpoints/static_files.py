from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter()

# Base directory for markdown files
MARKDOWN_DIR = r"C:\ai\fulled\extensions\fulled\src\docs"

# @router.get("/get_markdown/{filename}")
# async def get_markdown(filename: str):
#     file_path = os.path.join(MARKDOWN_DIR, filename)
#     print(f'get_markdown filename: {filename}, file_path: {file_path}')
#     if not os.path.exists(file_path):
#         raise HTTPException(status_code=404, detail="File not found")
#     return FileResponse(file_path, media_type="text/markdown")
# from fastapi.middleware.cors import CORSMiddleware

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Specify your frontend URL in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@router.get("/markdown/{filename}")
async def get_markdown(filename: str):
    file_path = os.path.join(MARKDOWN_DIR, filename)
    print(f"Attempting to access file: {file_path}")  # Debug print
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")  # Debug print
        raise HTTPException(status_code=404, detail=f"File not found: {file_path}")
    return FileResponse(file_path, media_type="text/markdown")

# Optional: endpoint to list available markdown files
@router.get("/list_markdown_files")
async def list_markdown_files():
    files = [f for f in os.listdir(MARKDOWN_DIR) if f.endswith('.md')]
    return {"markdown_files": files}


# from fastapi import FastAPI
# from markdown_router import router as markdown_router
# app = FastAPI()
# app.include_router(markdown_router, prefix="/api")

# // Fetch the markdown content from your FastAPI endpoint
# const fetchMarkdown = async () => {
#     try {
#         const response = await fetch('http://localhost:8000/api/get_markdown/BANTUAN.md');
#         const text = await response.text();
#         setMarkdownText(text);
#     } catch (error) {
#         console.error('Error fetching markdown:', error);
#         setMarkdownText('Error loading markdown content.');
#     }
# };
# fetchMarkdown();

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import os
import json

router = APIRouter()

# Serve the entire config file
@router.get("/api/config")
async def get_config():
    config_path = "C:/Users/usef/Downloads/api-keys-config.json"
    try:
        with open(config_path, 'r') as file:
            config_data = json.load(file)
            return JSONResponse(content=config_data)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Config file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON in config file")

# Get next available provider (with least uses)
@router.get("/api/config/next-provider")
async def get_next_provider():
    # config_path = "C:/Users/usef/Downloads/api-keys-config.json"
    config_path = os.path.join(os.path.dirname(__file__), "api-keys.json")
    try:
        with open(config_path, 'r') as file:
            config_data = json.load(file)
            providers = config_data['providers']
            
            # Find provider with minimum uses
            min_uses = min(p['uses'] for p in providers)
            eligible_providers = [p for p in providers if p['uses'] == min_uses]
            
            # Get first eligible provider (or you could randomize)
            if eligible_providers:
                selected = eligible_providers[0]
                
                # Update uses count
                for p in providers:
                    if p['name'] == selected['name']:
                        p['uses'] += 1
                
                # Save updated config
                with open(config_path, 'w') as f:
                    json.dump(config_data, f, indent=2)
                
                return JSONResponse(content=selected)
            
            raise HTTPException(status_code=404, detail="No providers available")
            
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Config file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON in config file")

# Reset uses counter
@router.post("/api/config/reset-uses")
async def reset_uses():
    # config_path = "C:/Users/usef/Downloads/api-keys.json"
    config_path = os.path.join(os.path.dirname(__file__), "api-keys.json")
    try:
        with open(config_path, 'r') as file:
            config_data = json.load(file)
            
        # Reset all uses to 0
        for provider in config_data['providers']:
            provider['uses'] = 0
            
        # Save updated config
        with open(config_path, 'w') as f:
            json.dump(config_data, f, indent=2)
            
        return JSONResponse(content={"message": "Uses reset successfully"})
            
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Config file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON in config file")
