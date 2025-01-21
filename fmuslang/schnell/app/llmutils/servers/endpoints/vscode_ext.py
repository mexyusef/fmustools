from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os
from schnell.app.fileutils import get_daftar_isi, define_filepath_barisentry, define_filepath_equal


# Define request model for TOC
class TocRequest(BaseModel):
    project: str
    framework: str

# Define request model for definition
class DefinitionRequest(BaseModel):
    project: str
    framework: str
    fmus_entry: str

def sanitize_project_framework(project, framework):
    project = project.lower().replace(' ', '_')
    framework = framework.lower().replace(' ', '_')
    return project, framework

def endpoint_vscode_ext(app, basefolder):

    # Error handler for FileNotFoundError
    @app.exception_handler(FileNotFoundError)
    async def file_not_found_exception_handler(request, exc: FileNotFoundError):
        return HTTPException(status_code=404, detail=str(exc))

    # Endpoint 1: Get table of contents
    @app.post("/vscode_toc")
    async def vscode_toc(request: TocRequest) -> List[str]:
        print(f"/vscode_toc => {request}")
        project, framework = request.project, request.framework
        print(f"/vscode_toc #1 => {project}, {framework}")
        project, framework = sanitize_project_framework(project, framework)
        print(f"/vscode_toc #2 => {project}, {framework}")

        fmus_filename = f"{project}_{framework}.fmus"
        fmus_filepath = os.path.join(basefolder, 'create_projects', fmus_filename)
        
        try:
            # Call the get_daftar_isi function
            toc: List[str] = get_daftar_isi(fmus_filepath)
        except FileNotFoundError as e:
            raise HTTPException(status_code=404, detail=f"File '{fmus_filename}' not found")
        
        return toc

    # Endpoint 2: Get definition of a specific entry
    @app.post("/vscode_definition")
    async def vscode_definition(request: DefinitionRequest) -> str:
        print(f"/vscode_definition => {request}")
        project, framework, fmus_entry = request.project, request.framework, request.fmus_entry
        print(f"/vscode_toc #2 => {project}, {framework}, {fmus_entry}")
        project, framework = sanitize_project_framework(project, framework)
        print(f"/vscode_toc #1 => {project}, {framework}, {fmus_entry}")
        
        fmus_filename = f"{project}_{framework}.fmus"
        fmus_filepath = os.path.join(basefolder, 'create_projects', fmus_filename)
        
        try:
            # Call the define_filepath_barisentry function
            definition: str = define_filepath_barisentry(fmus_filepath, fmus_entry)
        except FileNotFoundError as e:
            raise HTTPException(status_code=404, detail=f"File '{fmus_filename}' not found")
        
        return definition
