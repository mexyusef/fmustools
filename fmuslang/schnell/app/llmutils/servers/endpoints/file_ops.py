from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os
import shutil
import fnmatch


# Configuration
# IGNORED_DIRS = {'node_modules', '.git', '__pycache__', 'venv'}
IGNORED_DIR_PATTERNS = {'node_modules', '.git', '__pycache__', 'venv', '.aider*'}

class File(BaseModel):
    name: str
    size: int
    relative_path: str

class OperationRequest(BaseModel):
    files: List[str]
    operation: str
    destination: Optional[str] = None

# def get_files_recursive(directory):
#     files = []
#     for root, dirs, filenames in os.walk(directory):
#         dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
#         for filename in filenames:
#             if filename.endswith('.txt'):
#                 full_path = os.path.join(root, filename)
#                 relative_path = os.path.relpath(full_path, directory)
#                 size = os.path.getsize(full_path)
#                 files.append(File(name=filename, size=size, relative_path=relative_path))
#     return files
IGNORED_EXTENSIONS = {'.pyc', '.pyo', '.pyd', '.db', '.gitignore', '.bak'}  # Add more as needed
def should_ignore_dir(dir_name):
    return any(fnmatch.fnmatch(dir_name, pattern) for pattern in IGNORED_DIR_PATTERNS)

# def get_files_recursive(directory):
#     files = []
#     for root, dirs, filenames in os.walk(directory):
#         # Remove ignored directories
#         dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        
#         for filename in filenames:
#             # Check if the file extension is not in the ignored list
#             if not any(filename.endswith(ext) for ext in IGNORED_EXTENSIONS):
#                 full_path = os.path.join(root, filename)
#                 relative_path = os.path.relpath(full_path, directory)
#                 size = os.path.getsize(full_path)
#                 files.append(File(name=filename, size=size, relative_path=relative_path))
#     return files
def get_files_recursive(directory):
    files = []
    for root, dirs, filenames in os.walk(directory):
        # Remove ignored directories
        dirs[:] = [d for d in dirs if not should_ignore_dir(d)]
        
        for filename in filenames:
            # Check if the file extension is not in the ignored list
            if not any(filename.endswith(ext) for ext in IGNORED_EXTENSIONS):
                full_path = os.path.join(root, filename)
                relative_path = os.path.relpath(full_path, directory)
                size = os.path.getsize(full_path)
                files.append(File(name=filename, size=size, relative_path=relative_path))
    return files

def endpoint_file_ops(app, basefolder):

    @app.get("/file_ops/", response_model=List[File])
    async def list_files(directory: str):
        # full_path = os.path.join(BASE_DIR, directory)
        full_path = directory # pastikan nilai absolute yg diperoleh
        if not os.path.exists(full_path):
            raise HTTPException(status_code=404, detail="Directory not found")
        return get_files_recursive(full_path)

    @app.post("/file_ops/operate/")
    async def operate_on_files(request: OperationRequest):
        BASE_DIR = "/path/to/base/directory"  # Replace with your actual base directory
        # BASE_DIR = request.base_folder
        if request.operation not in ["copy", "move", "delete"]:
            raise HTTPException(status_code=400, detail="Invalid operation")

        results = []
        for file_path in request.files:
            full_path = os.path.join(BASE_DIR, file_path)
            # full_path = file_path # pastikan nilai absolute yg diperoleh
            if not os.path.exists(full_path):
                results.append({"file": file_path, "status": "error", "message": "File not found"})
                continue

            try:
                if request.operation == "delete":
                    os.remove(full_path)
                    results.append({"file": file_path, "status": "success", "message": "File deleted"})
                elif request.operation in ["copy", "move"]:
                    if not request.destination:
                        raise HTTPException(status_code=400, detail="Destination is required for copy/move operations")
                    
                    dest_path = os.path.join(BASE_DIR, request.destination, os.path.basename(file_path))
                    if request.operation == "copy":
                        shutil.copy2(full_path, dest_path)
                        results.append({"file": file_path, "status": "success", "message": "File copied"})
                    else:  # move
                        shutil.move(full_path, dest_path)
                        results.append({"file": file_path, "status": "success", "message": "File moved"})
            except Exception as e:
                results.append({"file": file_path, "status": "error", "message": str(e)})

        return {"results": results}
