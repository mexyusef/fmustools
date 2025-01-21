import json
import os
import random
import re
import time
import asyncio
import logging
import traceback
from datetime import datetime, timedelta
from functools import wraps
from textwrap import dedent

from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import Dict
from typing import Union

# from fastapi import FastAPI, HTTPException
# from fastapi import File, UploadFile
from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks, Form, Request
# Lifespan
from fastapi.staticfiles import StaticFiles
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

import asyncio
import aiofiles
# from aiortc import RTCPeerConnection, RTCSessionDescription, VideoStreamTrack, MediaStreamTrack
# from aiortc.contrib.signaling import BYE
from aiortc import RTCPeerConnection, RTCSessionDescription, RTCIceCandidate
# from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.signaling import BYE

if __name__ == "__main__":
    import sys
    from dotenv import load_dotenv
    load_dotenv(r"C:\Users\usef\work\sidoarjo\schnell\.env.crypt")
    sys.path.insert(0, r"c:\users\usef\work\sidoarjo")
    from startup import initialize_programming_data
    initialize_programming_data()


# from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm
from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm_all
from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm_active
from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm_code_query
from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm_error_query
from schnell.app.llmutils.langchainutils.llm_config import invoke_all, all_accounts, change_active_model, llm_models
from schnell.app.llmutils.langchainutils.tools_config import tools_config
from schnell.app.printutils import indah4, print_list_warna, indah3
from schnell.app.dirutils import dirname_if_not_dir, isfile, isdir, joiner
from schnell.app.fileutils import get_daftar_isi, define_filepath_barisentry, define_filepath_equal
from schnell.app.fmusutils import (
    # utk jalankan filepath=barisentry berisi fmuslang
    run_fmus_for_file_in_thread,
    run_fmus_for_file,
    # utk jalankan literal fmuslang
    run_fmus_for_content_in_thread,
    run_fmus_for_content,
)
from schnell.app.llmutils.servers.rag.pdf_qa import rag_file_with_embedding_and_llm
from schnell.app.llmutils.langchainutils.tools.tavily import Tapir
from schnell.app.llmutils.langchainutils.tools.youtube import U2

from schnell.app.llmutils.langchainutils.llms.llm_openai import invoke_llm_vision_chat_by_screen_capture as openai_vision
from schnell.app.llmutils.langchainutils.llms.llm_gemini import invoke_llm_vision_chat_by_screen_capture

from schnell.app.llmutils.servers.summarization.youtube import summarize_youtube_video, default_youtube_prompt
from schnell.app.llmutils.servers.summarization.youtube import extract_transcript_from_youtube
from schnell.app.llmutils.servers.summarization.youtube import generate_summary

from schnell.app.ocrutils_new import ocr_by_tesseract
from schnell.app.ocrutils_new import ocr_by_openai
from schnell.app.ocrutils_new import instructions
from schnell.app.ocrutils_new import capture_and_copy_screenshot
from schnell.app.llmutils.servers.parser.gptresearch import perform_research
from schnell.app.llmutils.servers.tools.project_creator import create_project


from schnell.app.llmutils.servers.types import *

# Set up logging
logging.basicConfig(level=logging.INFO)
# TODO
# C:\tmp>python C:\Users\usef\work\sidoarjo\schnell\app\llmutils\servers\serve.py
# USER_AGENT environment variable not set, consider setting it to identify your requests.
# C:\Python311\Lib\site-packages\pydantic\_internal\_fields.py:132: UserWarning: Field "model_name" in GPT4AllEmbeddings has conflict with protected namespace "model_".

# You may be able to resolve this warning by setting `model_config['protected_namespaces'] = ()`.
#   warnings.warn(
# coba oprek GPT4AllEmbeddings


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}
        self.peer_connections: dict[str, RTCPeerConnection] = {}

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections[username] = websocket
        self.peer_connections[username] = RTCPeerConnection()

    def disconnect(self, username: str):
        if username in self.active_connections:
            del self.active_connections[username]
        if username in self.peer_connections:
            self.peer_connections[username].close()
            del self.peer_connections[username]

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections.values():
            await connection.send_text(message)

    def get_active_connections_count(self):
        return len(self.active_connections)

    def get_active_users(self):
        return list(self.active_connections.keys())


app = FastAPI()
manager = ConnectionManager()

# chrome yusef
# https://claude.ai/chat/f4813725-5009-4fda-9357-519bb6dbb35d
@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)
    try:
        await manager.broadcast(f"{username} joined the chat")
        while True:
            data = await websocket.receive_text()
            print(f"Received message from {username}: {data}.")  # Log received message
            if data == "get_count":
                count = manager.get_active_connections_count()
                await manager.send_personal_message(f"Connected clients: {count}", websocket)
            elif data == "get_users":
                users = manager.get_active_users()
                await manager.send_personal_message(f"Connected users: {', '.join(users)}", websocket)
            else:
                await manager.broadcast(f"Hello this is server, I thank {username} for sending this: {data}.")
    except WebSocketDisconnect:
        manager.disconnect(username)
        await manager.broadcast(f"{username} left the chat")

# WebRTC handler
pcs_webrtc = set()
# Allow CORS from all origins (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/offer")
# async def offer(request: dict):
async def offer(request: Request):
    # params = json.loads(request)
    params = await request.json()
    offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])

    pc = RTCPeerConnection()
    pcs_webrtc.add(pc)

    @pc.on("datachannel")
    def on_datachannel(channel):
        @channel.on("message")
        def on_message(message):
            if isinstance(message, str) and message.startswith(BYE):
                print("Received BYE")
                coro = pc.close()
                asyncio.ensure_future(coro)
                pcs_webrtc.discard(pc)

    @pc.on("icecandidate")
    def on_icecandidate(candidate):
        if candidate is None:
            response = {
                "sdp": pc.localDescription.sdp,
                "type": pc.localDescription.type,
            }
            return response

    await pc.setRemoteDescription(offer)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    response = {
        "sdp": pc.localDescription.sdp,
        "type": pc.localDescription.type,
    }

    return response

# @app.post("/ice_candidate")
# # async def ice_candidate(request: dict):
# async def ice_candidate(request: Request):
#     params = await request.json()

#     candidate = {
#         "candidate": params["candidate"],
#         "sdpMid": params["sdpMid"],
#         "sdpMLineIndex": params["sdpMLineIndex"],
#     }

#     for pc in pcs_webrtc:
#         ice_candidate = RTCIceCandidate(**candidate)
#         await pc.addIceCandidate(ice_candidate)

#     return {"status": "success"}
@app.post("/ice_candidate")
async def ice_candidate(request: Request):
    params = await request.json()

    ice_candidate = RTCIceCandidate(
        component=params["component"],
        foundation=params["foundation"],
        ip=params["ip"],
        port=params["port"],
        priority=params["priority"],
        protocol=params["protocol"],
        type=params["type"],
        relatedAddress=params.get("relatedAddress"),
        relatedPort=params.get("relatedPort"),
        sdpMid=params.get("sdpMid"),
        sdpMLineIndex=params.get("sdpMLineIndex"),
        tcpType=params.get("tcpType")
    )

    for pc in pcs_webrtc:
        await pc.addIceCandidate(ice_candidate)

    return {"status": "success"}
# @app.post("/ice_candidate")
# async def ice_candidate(request: Request):
#     params = await request.json()
#     candidate = params["candidate"]
#     sdpMid = params["sdpMid"]
#     sdpMLineIndex = params["sdpMLineIndex"]

#     ice_candidate = RTCIceCandidate(candidate=candidate, sdpMid=sdpMid, sdpMLineIndex=sdpMLineIndex)
#     for pc in pcs_webrtc:
#         await pc.addIceCandidate(ice_candidate)
#     return {"status": "success"}


# # Shutdown handler to close all peer connections
# @app.on_event("shutdown")
# async def on_shutdown():
#     coros = [pc.close() for pc in pcs_webrtc]
#     await asyncio.gather(*coros)
#     pcs_webrtc.clear()
# Lifespan handler for server startup and shutdown events
# @app.on_event("lifespan")
# async def lifespan_handler():
#     yield  # Code before the yield runs on startup, code after runs on shutdown
#     logging.info("Server is shutting down.")
#     coros = [pc.close() for pc in pcs_webrtc]
#     await asyncio.gather(*coros)
#     pcs_webrtc.clear()
# Lifespan handler for server startup and shutdown events

# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\servers\serve_fastapi.py:203: DeprecationWarning:
#         on_event is deprecated, use lifespan event handlers instead.
#         Read more about it in the
#         [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
#   @app.on_event("startup")
# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\servers\serve_fastapi.py:207: DeprecationWarning:
#         on_event is deprecated, use lifespan event handlers instead.
#         Read more about it in the
#         [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
#   @app.on_event("shutdown")

# @app.on_event("startup")
# async def startup_event():
#     logging.info("Server is starting up.")

# @app.on_event("shutdown")
# async def shutdown_event():
#     logging.info("Server is shutting down.")
#     coros = [pc.close() for pc in pcs_webrtc]
#     await asyncio.gather(*coros)
#     pcs_webrtc.clear()

from contextlib import asynccontextmanager
# Define the lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Server is starting up.")
    yield
    logging.info("Server is shutting down.")
    coros = [pc.close() for pc in pcs_webrtc]
    await asyncio.gather(*coros)
    pcs_webrtc.clear()

app.router.lifespan_context = lifespan
#################################### new webrtc support: START
# /create-room: Creates a new room for WebRTC peers to connect.
# /rooms/{room_id}/offer: Allows sending and receiving WebRTC offers.
# /rooms/{room_id}/answer: Allows sending and receiving WebRTC answers.
# /rooms/{room_id}/ice-candidate: Handles ICE candidates for establishing peer
# In-memory store for simplicity. In a real application, use a database.
rooms = {}



@app.post("/create-room")
async def create_room():
    import uuid
    room_id = str(uuid.uuid4())
    rooms[room_id] = {"offers": [], "answers": [], "ice_candidates": []}
    return {"room_id": room_id}

@app.post("/rooms/{room_id}/offer")
async def send_offer(room_id: str, offer: Offer):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")
    rooms[room_id]["offers"].append(offer.dict())
    return {"message": "Offer received"}

@app.get("/rooms/{room_id}/offer")
async def get_offer(room_id: str):
    if room_id not in rooms or not rooms[room_id]["offers"]:
        raise HTTPException(status_code=404, detail="No offer available")
    return rooms[room_id]["offers"][-1]

@app.post("/rooms/{room_id}/answer")
async def send_answer(room_id: str, answer: Answer):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")
    rooms[room_id]["answers"].append(answer.dict())
    return {"message": "Answer received"}

@app.get("/rooms/{room_id}/answer")
async def get_answer(room_id: str):
    if room_id not in rooms or not rooms[room_id]["answers"]:
        raise HTTPException(status_code=404, detail="No answer available")
    return rooms[room_id]["answers"][-1]

@app.post("/rooms/{room_id}/ice-candidate")
async def send_ice_candidate(room_id: str, candidate: IceCandidate):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")
    rooms[room_id]["ice_candidates"].append(candidate.dict())
    return {"message": "ICE candidate received"}

@app.get("/rooms/{room_id}/ice-candidates")
async def get_ice_candidates(room_id: str):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")
    return rooms[room_id]["ice_candidates"]
#################################### new webrtc support: END

# Mount the static directory
# app.mount("/static", StaticFiles(directory="static"), name="static")
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "static")
# Mount the static directory
app.mount("/static", StaticFiles(directory=static_dir), name="static")
trigger_char = "$"
fmus_completion_path = os.path.join(current_dir, "completion")

from prompts.code_query_prompt import code_query_prompt
from prompts.error_query_prompt import error_query_prompt

app_configuration = {
    'active_file'   : 'default.fmus',
    'openai:vision:system_prompt': instructions,  # app_configuration['openai:vision:system_prompt']
    'openai:vision:gpt4vision_over_gpt4o': True,  # app_configuration['openai:vision:gpt4vision_over_gpt4o']
    'code_query_prompt': [
        code_query_prompt,
    ],
    'error_query_prompt': [
        error_query_prompt,
    ],
}


def remove_markdown_code_tags(text):
    # Define regular expression pattern to match markdown code tags
    pattern = r'^```(?:\w+)?\n(.*?)\n```$'
    # Remove markdown code tags from the start and end of the string
    cleaned_text = re.sub(pattern, r'\1', text, flags=re.DOTALL)
    return cleaned_text.strip()

# # Test the function
# text = "```typescript\nbody\n```"
# cleaned_text = remove_markdown_code_tags(text)
# print(cleaned_text)  # Output: "body"
# Decorator function
from langchain_core.messages import AIMessage
def remove_markdown_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Apply remove_markdown_code_tags to arguments
        processed_args = tuple(
            remove_markdown_code_tags(arg) if isinstance(arg, str) else arg for arg in args
        )
        processed_kwargs = {
            key: remove_markdown_code_tags(value) if isinstance(value, str) else value for key, value in kwargs.items()
        }
        llm_invocation = func(*processed_args, **processed_kwargs)
        if isinstance(llm_invocation, AIMessage):
            llm_invocation = llm_invocation.content
        return remove_markdown_code_tags(llm_invocation)
    return wrapper


# Decorate invoke_llm_active function
invoke_llm_active = remove_markdown_decorator(invoke_llm_active)
invoke_llm_code_query = remove_markdown_decorator(invoke_llm_code_query)
invoke_llm_error_query = remove_markdown_decorator(invoke_llm_error_query)


def get_completion_file():
    return joiner(fmus_completion_path, app_configuration['active_file'])


def get_suggestions():
    if app_configuration['active_file']=='EMPTY':
        return []
    completion_file = get_completion_file()
    toc = get_daftar_isi(completion_file)
    return [f"{item}\n{define_filepath_barisentry(completion_file, item)}" for item in toc]


# Serve HELP.md file
@app.get("/help")
def get_help():
    return {"help_url": "/static/HELP.md"}

class TextInput(BaseModel):
    text: str

# Create an endpoint to receive the text
@app.post("/submit-text/")
async def receive_text(input: TextInput):
    # Process the text as needed
    received_text = input.text
    return {"message": "Text received", "text": received_text}


@app.post("/capture_screenshot")
async def capture_screenshot(request: ScreenshotRequest):
    try:
        # print('#1', request)
        saved_file = capture_and_copy_screenshot(
            output_file=request.output_file,
            datadir=request.datadir,
            # delay=request.delay
        )
        # print('#2', saved_file)
        return {
            "output_file": saved_file
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/list_fmus_files", response_model=List[str])
async def list_fmus_files():
    files = [f for f in os.listdir(fmus_completion_path) if f.endswith('.fmus')] + ['EMPTY']
    return files


@app.post("/select_active_fmus_file")
async def select_active_fmus_file(request: SelectFileRequest):
    selected_file = request.selected_file
    print('******* select_file *******')
    print(selected_file)
    print('******* select_file *******')
    app_configuration['active_file'] = selected_file
    return {"message": "File selected", "file": selected_file}


@app.post("/change_vision_system_prompt")
async def change_vision_system_prompt(request: SystemPromptRequest):
    system_prompt = request.system_prompt
    print('******* system_prompt *******')
    print(system_prompt)
    print('******* system_prompt *******')
    app_configuration['openai:vision:system_prompt'] = system_prompt
    return {"message": "System prompt change", "prompt": system_prompt}


@app.post("/select_misc_command")
async def select_misc_command(request: SelectCommandRequest):
    """
    @TODO:
    tambah utk generate "model" => zod, yup, SQL, django model, fastapi model, flask model, express/pg model, express/mongoose model, nest CRUD, ...

    fast article/medium/blog

    fast planner: pengen ..., create plan utk achieve ... (optional: assumption)
        job advertisement to plan
        upwork job to plan

    fast scheduler: pengen ..., create schedule utk achieve ... (optional: constraint => hrs selesai dlm 1 hari, etc)

    fast (bullet/key) points utk ...

    fast analogy/memorizer/visual imagery/mental image/visual image utk ...

    logic/fallacy/reason identifier dlm tulisan, pros dan cons

    create "search term" dan "llm prompt" to learn more about ... sekaligus
    """
    user_prompt = request.prompt.strip()
    user_command = request.command.strip()
    response = f"Unknown command {user_command}."

    if not user_command:
        return { "response": response }

    user_command = user_command.lower()

    if user_command == 'hackernews':
        from schnell.app.llmutils.servers.parser.hackernews import parse_hackernews_stringified
        response = parse_hackernews_stringified()
    elif user_command == 'analyze_page':
        from schnell.app.llmutils.servers.parser.page_analyzer import analyze_page
        response = analyze_page(user_prompt)
    elif user_command == 'analyze_text':
        from schnell.app.llmutils.servers.parser.text_analyzer import analyze_text
        response = analyze_text(user_prompt)
    elif user_command == 'fix_grammar':
        from schnell.app.llmutils.servers.parser.fix_grammar import learn_language
        response = learn_language(user_prompt)

    elif user_command == 'learn_english':
        from schnell.app.llmutils.servers.parser.learn_english import learn_english
        if user_prompt:  # jika kita specify past stories yg jangan digunakan lagi
            response = learn_english(user_prompt)
        else:
            response = learn_english()
    elif user_command == 'learn_spanish':
        from schnell.app.llmutils.servers.parser.learn_spanish import learn_language
        response = learn_language()
    elif user_command == 'learn_german':
        from schnell.app.llmutils.servers.parser.learn_german import learn_language
        response = learn_language()
    elif user_command == 'learn_russian':
        from schnell.app.llmutils.servers.parser.learn_russian import learn_language
        response = learn_language()
    elif user_command == 'learn_dutch':
        from schnell.app.llmutils.servers.parser.learn_dutch import learn_language
        response = learn_language()
    elif user_command == 'learn_french':
        from schnell.app.llmutils.servers.parser.learn_french import learn_language
        response = learn_language()
    elif user_command == 'learn_mandarin':
        from schnell.app.llmutils.servers.parser.learn_mandarin import learn_language
        response = learn_language()

    elif user_command == 'learn_programming':
        from schnell.app.llmutils.servers.parser.learn_programming import learn_language
        response = learn_language()

    elif user_command == 'pdf_question_with_gemini':
        from schnell.app.llmutils.tests.gemini_flash import question_pdf
        filepath, question = [e.strip() for e in user_prompt.split('\n',1)]
        if filepath and question:
            result = question_pdf(filepath, question)
            indah3(result)
        else:
            indah4(f"no file_path and question separated by a newline within {user_prompt}", warna='red')

    # response = invoke_llm_active(user_query, verbose=False)
    # indah4('requesting...', warna='magenta')
    # print(request, '\n===>', response)
    return {
        "response": response
    }


# rewrite:
# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\just_implement\role_just_implement.py
# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\servers\tools\project_creator.py
@app.post("/create-project")
def create_project_endpoint(background_tasks: BackgroundTasks, request: ProjectRequest):
    print("/create-project, request:", request)
    background_tasks.add_task(
        create_project,
        request.project_prompt,
        request.workdir,
        request.llm,
        # request.recursion_limit
    )
    # return {"response": f"Project creation started in {os.getcwd()}"}
    return {"response": f"\n\n\n⭐️{request.workdir}"}


def process_file(file_location: str):
    try:
        rag_chain, system_prompt_context = rag_file_with_embedding_and_llm(file_path=file_location)
        # Optionally, save system_prompt_context or any necessary information for later use
    except Exception as e:
        # Handle any exceptions that occur during processing
        print(f"Error processing file: {str(e)}")


@app.post("/save_pdf/")
# async def save_pdf(file: UploadFile = File(...)):
# async def save_pdf(file: UploadFile = File(...), background_tasks: BackgroundTasks):
async def save_pdf(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    file_location = f"./{file.filename}"
    # file_location = os.path.abspath(f"./{file.filename}")
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    try:
        # rag_chain, system_prompt_context = rag_file_with_embedding_and_llm(file_path=file_location)
        # Add the long-running task to the background tasks
        background_tasks.add_task(process_file, file_location)
        # return {"file_path": file_location, "system_prompt_context": system_prompt_context}
        return {
            "status": "OK",
            "file_path": file_location,
            "message": f"{file_location} saved.",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")


@app.post("/query_pdf/")
async def query_pdf(query: QueryRequest):
    try:
        # query_file = query.file_path
        query_file = os.path.abspath(query.file_path)
        print(f'query_pdf #1 file: {query_file}')
        rag_chain, system_prompt_context = rag_file_with_embedding_and_llm(file_path=query_file)
        print(f'query_pdf #2 Q: {query.question}, context: [{system_prompt_context}].')
        results = rag_chain.invoke({
            "context": system_prompt_context,
            "input": query.question
        })
        print(f'query_pdf #3 {query_file}')
        response = {
            "number_of_results": len(results['context']),
            # "results": results,
            "answer": results['answer'],
            "context_details": [
                {
                    "index": idx,
                    "metadata": doc.metadata,
                    "page_content": doc.page_content
                }
                for idx, doc in enumerate(results['context'])
            ]
        }
        print(f"query_pdf #4 ans: <<<{results['answer']}>>>, len docs = {len(results['context'])}.")
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")


@app.post("/ocr/tesseract")
async def ocr_tesseract():
    try:
        result = ocr_by_tesseract()
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ocr/openai")
async def ocr_openai(
    user_prompt: str = Form(...),
    urls_or_filename: Union[str, List[str], None] = Form(None)
):
    try:
        result = ocr_by_openai(
            urls_or_filename,
            user_prompt,
            system_message=app_configuration['openai:vision:system_prompt'],
            gpt4vision_over_gpt4o=app_configuration['openai:vision:gpt4vision_over_gpt4o']
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/vision-prompt-gemini")
async def vision_prompt_with_gemini(request: VisionRequest):
    print('request:', request)
    try:
        current_line = request.text.strip()
        if current_line:
            result = invoke_llm_vision_chat_by_screen_capture(
                user_prompt=current_line,
                base_folder=r'C:\Users\usef\Desktop\Screenshots\llms-vscode',
                image_file=request.image_file,  # Pass the image_path if provided
                wait_alert=False,
                model="gemini-1.5-flash",
                verbose=False,
            )
            indah3(result, warna='yellow')
            return {"result": result}
        else:
            raise HTTPException(status_code=400, detail="No text provided")
    except Exception as e:
        print('Exception vision-prompt-gemini:', e)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/vision-prompt-openai")
async def vision_prompt_with_openai(request: VisionRequest):
    print('request:', request)
    try:
        current_line = request.text.strip()
        if current_line:
            result = openai_vision(
                current_line,
                base_folder=r'C:\Users\usef\Desktop\Screenshots\llms-vscode',
                image_file=request.image_file,  # Pass the image_path if provided
            )
            indah3(result, warna='yellow')
            return {"result": result}
        else:
            raise HTTPException(status_code=400, detail="No text provided")
    except Exception as e:
        print('Exception vision-prompt-openai:', e)
        trace = traceback.format_exc()
        indah4(trace, warna='red')
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/summarize_youtube_video_new")
async def summarize_youtube_video_new_endpoint(video_url: VideoURL):
    prompt_text = default_youtube_prompt
    transcript_text, video_title = extract_transcript_from_youtube(video_url.url)
    if transcript_text:
        summary = generate_summary(prompt=prompt_text, transcript_text='\n'.join(transcript_text))
        if summary:
            return {
                "video_title": video_title,
                # "transcripts": transcript_text,
                # "transcripts": '\n---\n'.join(transcript_text),
                "transcripts": '\n\n'.join(transcript_text),
                "summary": summary,
            }
        else:
            # raise HTTPException(status_code=500, detail="Failed to generate summary.")
            return {
                "video_title": video_title,
                # "transcripts": transcript_text,
                # "transcripts": '\n---\n'.join(transcript_text),
                "transcripts": '\n\n'.join(transcript_text),
                "summary": "Failed to generate summary.",
            }
    else:
        raise HTTPException(status_code=404, detail="Failed to extract transcript.")


@app.post("/summarizeYoutubeVideo")
async def summarize_youtube_video_endpoint(request: PromptRequest):
    from schnell.app.llmutils.servers.summarize_youtube_prompt import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt)
    )
    return {
        "response": response
    }


@app.post("/podomoro_planner")
async def podomoro_planner(request: PromptRequest):
    # from schnell.app.llmutils.servers.summarize_youtube_prompt import get_prompt
    if not hasattr(request, 'prompt'):
        raise HTTPException(status_code=500, detail=f"Request body has no prompt: {str(request)}")
    from schnell.app.llmutils.servers.tools.prompts.podomoro_planner import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt)
    )
    return {
        "response": response
    }


@app.post("/completion")
async def get_completion_suggestions(request: CompletionRequest):
    # print(json.dumps(request, indent=2))
    print(request)
    # C:\portfolio\fmus-lib\fmus-ts\z03\src\extension.ts
    prompt = request.text
    # Simulate processing and provide completion suggestions
    try:
        suggestions = get_suggestions()
        # suggestions = [
        #     f"suggestion1 for {prompt}",
        #     f"suggestion2 for {prompt}",
        #     f"suggestion3 for {prompt}",
        # ]
        # Return suggestions
        return {"suggestions": suggestions}
    except Exception as e:
        # Return error message if any exception occurs
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/completion_llm")
async def get_completion_by_llm_suggestions(request: CompletionRequest):
    # print(json.dumps(request, indent=2))
    print(request)
    # C:\portfolio\fmus-lib\fmus-ts\z03\src\extension.ts
    prompt = request.text
    if prompt:
        prompt = prompt.strip().removesuffix(trigger_char).strip()
    # Simulate processing and provide completion suggestions
    try:
        # Simulate processing to get completion suggestions
        suggestions = [invoke_llm_active(prompt)]
        # Return suggestions
        return {"suggestions": suggestions}
    except Exception as e:
        # Return error message if any exception occurs
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/run_fmus")
async def run_fmus(request: RequestData):
# async def run_fmus(request):
    # run_fmus_for_content(content)
    # run_fmus_for_content(content, dirpath=os.getcwd(), filepath=filepath)
    # run_fmus_for_content(text, dirpath=os.getcwd())
    # run_fmus_for_content_in_thread(text, dirpath=os.getcwd())
    # thread = run_fmus_for_content_in_thread(text, dirpath=os.getcwd())
    # run_fmus_for_content_in_thread(content, dirpath=os.getcwd(), filepath=filepath)
    print('run_fmus=>', request)

    content = request.content
    # kadang ada \r dari text editor
    content = content.replace('\r', '')
    meta_document_fs_path = request.meta.metaDocument.fsPath
    if not meta_document_fs_path:
        meta_document_fs_path = os.getcwd()

    if not content or not meta_document_fs_path:
        raise HTTPException(status_code=400, detail="Content or metaDocument.fsPath is missing")

    # # Process the data here as needed
    # # For example, print to console or log to file
    print(f"Content: [{content}]")
    print(f"Meta Document FS Path: [{meta_document_fs_path}]")

    file_cwd = dirname_if_not_dir(meta_document_fs_path)

    if content.startswith('fmuslang:'):
        content = content.removeprefix('fmuslang:')
        print(f"New content: {content}. file_cwd = {file_cwd}.")
        if isfile(meta_document_fs_path):
            # run_fmus_for_content_in_thread(content, dirpath=file_cwd, filepath=meta_document_fs_path)
            run_fmus_for_content(content, dirpath=file_cwd, filepath=meta_document_fs_path)
        else:
            # run_fmus_for_content_in_thread(content, dirpath=file_cwd)
            run_fmus_for_content(content, dirpath=file_cwd)

    # response = invoke_llm_active(request.prompt)
    # indah4('requesting...', warna='magenta')
    # print(request, '\n===>', response)
    # return {
    #     "response": response
    # }

    response = json.dumps({
        "message": "OK",
        "content": content,
        "metaDocumentFsPath": meta_document_fs_path
    }, indent=2)

    return {
        "response": response
    }


@app.post("/run_ketik")
async def run_fmus_ketik(request: RequestData):
    # print('run_fmus_ketik=>', request)
    content = request.content.strip()
    meta_document_fs_path = request.meta.metaDocument.fsPath
    if not meta_document_fs_path:
        meta_document_fs_path = os.getcwd()

    if not content or not meta_document_fs_path:
        raise HTTPException(status_code=400, detail="Content or metaDocument.fsPath is missing")

    file_cwd = dirname_if_not_dir(meta_document_fs_path)

    if isfile(meta_document_fs_path):
        run_fmus_for_content("/ketik)"+content, dirpath=file_cwd, filepath=meta_document_fs_path)
    else:
        run_fmus_for_content("/ketik)"+content, dirpath=file_cwd)

    response = json.dumps({
        "message": "OK",
        "content": content,
        "metaDocumentFsPath": meta_document_fs_path
    }, indent=2)

    return {
        "response": response
    }


@app.post("/run_ketik_for_project")
async def run_ketik_for_project(request: RequestData):
    print('run_fmus_ketik=>', request)
    content = request.content.strip()
    currentProjectFolder = request.meta.currentProjectFolder.strip()
    if not currentProjectFolder:
        currentProjectFolder = os.getcwd()

    if not content or not currentProjectFolder:
        raise HTTPException(status_code=400, detail="Content or currentProjectFolder is missing")

    # file_cwd = meta_document_fs_path

    run_fmus_for_content("/ketik)"+content, dirpath=currentProjectFolder)

    response = json.dumps({
        "message": "OK",
        "content": content,
        "currentProjectFolder": currentProjectFolder
    }, indent=2)

    return {
        "response": response
    }


@app.post("/run_fmus_for_project")
async def run_fmus_for_project(request: RequestData):
    print('run_fmus_for_project=>', request)

    content = request.content.strip()
    currentProjectFolder = request.meta.currentProjectFolder.strip()
    if not currentProjectFolder:
        currentProjectFolder = os.getcwd()

    if not content or not currentProjectFolder:
        raise HTTPException(status_code=400, detail="Content or currentProjectFolder is missing")

    if content.startswith('fmuslang:'):
        content = content.removeprefix('fmuslang:')
    # berbeda dg run_fmus, ini gak pake prefix
    print(f"New content: {content}. currentProjectFolder = {currentProjectFolder}.")
    run_fmus_for_content(content, dirpath=currentProjectFolder)

    response = json.dumps({
        "message": "OK",
        "content": content,
        "currentProjectFolder": currentProjectFolder
    }, indent=2)

    return {
        "response": response
    }



@app.get("/get_invoke_all")
def get_invoke_all():
    return invoke_all


@app.post("/update_invoke_all")
def update_invoke_all(config: ConfigUpdate):
    print('Request for updating invoke_all:', json.dumps(invoke_all, indent=2))
    for key, value in config.invoke_all.items():
        if key in invoke_all:
            invoke_all[key] = value
        else:
            raise HTTPException(status_code=400, detail=f"Invalid key: {key}")
    indah4(json.dumps(config.invoke_all, indent=2), warna='yellow')
    return invoke_all


@app.get("/get_active_old")
def get_active_old():
    return {"active": all_accounts["active"], "options": list(invoke_all.keys())}


@app.get("/get_active")
def get_active():
    active_account = all_accounts["active"]
    options = list(invoke_all.keys())
    options.remove(active_account)
    options.insert(0, active_account)
    return {"active": active_account, "options": options}


@app.post("/update_active")
def update_active(active_update: ActiveUpdate):
    if active_update.active in invoke_all:
        all_accounts["active"] = active_update.active
        return all_accounts
    else:
        raise HTTPException(status_code=400, detail="Invalid active value")


@app.get("/get_secondary_active")
def get_secondary_active():
    active_account = all_accounts["secondary_active"]
    options = list(invoke_all.keys())
    options.remove(active_account)
    options.insert(0, active_account)
    return {"secondary_active": active_account, "options": options}


@app.post("/update_secondary_active")
def update_secondary_active(active_update: SecondaryActiveUpdate):
    if active_update.secondary_active in invoke_all:
        all_accounts["secondary_active"] = active_update.secondary_active
        return all_accounts
    else:
        raise HTTPException(status_code=400, detail="Invalid active value")


# New endpoint to get current active model for the active provider
@app.get("/get_active_model")
def get_active_model():
    active_provider = all_accounts['active']

    # Assuming models are grouped under the provider name (like 'gemini_models' for 'gemini')
    if f"{active_provider}_models" not in llm_models:
        raise HTTPException(status_code=400, detail=f"No models available for {active_provider}")

    active_models = llm_models[f'{active_provider}_models']
    current_default = llm_models.get(f'{active_provider}_models:default', None)

    options = list(active_models.keys())
    if current_default in options:
        options.remove(current_default)
        options.insert(0, current_default)
    return {"active_model": current_default, "options": options}


# New endpoint to update the active model for the active provider
class ActiveModelUpdate(BaseModel):
    active_model: str

@app.post("/update_active_model")
def update_active_model(active_model_update: ActiveModelUpdate):
    active_provider = all_accounts['active']
    provider_models_key = f'{active_provider}_models'

    if provider_models_key not in llm_models:
        raise HTTPException(status_code=400, detail=f"No models available for {active_provider}")

    active_models = llm_models[provider_models_key]
    if active_model_update.active_model not in active_models:
        raise HTTPException(status_code=400, detail="Invalid model selection")

    llm_models[f'{active_provider}_models:default'] = active_model_update.active_model
    return {"message": f"Active model for {active_provider} updated to {active_model_update.active_model}"}

# Example Payload for /update_active_model:
# {
#     "active_model": "gemini-pro"
# }

@app.get("/get_mode")
def get_mode():
    return {"mode": all_accounts["mode"], "options": all_accounts["mode:list"]}


@app.post("/update_mode")
def update_mode(mode_update: ModeUpdate):
    if mode_update.mode in all_accounts["mode:list"]:
        all_accounts["mode"] = mode_update.mode
        return all_accounts
    else:
        raise HTTPException(status_code=400, detail="Invalid mode value")


@app.post("/changeConfiguration")  # active=groq, all=gemini,groq
async def change_configuration(request: PromptRequest):
    print(request)
    config = request.prompt
    if config.startswith('active='):
        nilai = config.removeprefix("active=").strip()
        if nilai and nilai in invoke_all:
            change_active_model(nilai)
            return {
                "response": json.dumps(all_accounts, indent=2)
            }
    elif config.startswith('all='):
        nilai = config.removeprefix("all=").strip()
        if nilai and nilai in invoke_all:
            selected = [e.strip() for e in nilai.split(',')]
            if selected:
                for key in invoke_all:
                    if key in selected:
                        invoke_all[key] = 1
                    else:
                        invoke_all[key] = 0
                return {
                    "response": json.dumps(invoke_all, indent=2)
                }
    # elif text.startswith("models:active="):
    #     from schnell.app.llmutils.langchainutils.llm_config import invoke_all, all_accounts, change_active_model
    #     nilai = text.removeprefix("models:active=").strip()
    #     if nilai and nilai in invoke_all.keys():
    #         change_active_model(nilai)
    #         print_json(all_accounts)
    # elif text.startswith("invoke_all="):  # config:invoke_all=gemini,cohere, config:invoke_all=
    #     # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\llm_config.py
    #     # C:\Users\usef\work\sidoarjo\schnell\app\promptutils.py
    #     from schnell.app.llmutils.langchainutils.llm_config import invoke_all
    #     nilai = text.removeprefix("invoke_all=").strip()
    #     if nilai and nilai in invoke_all.keys():
    #         selected = [e.strip() for e in nilai.split(',')]
    #         if selected:
    #             for key in invoke_all:
    #                 if key in selected:
    #                     invoke_all[key] = 1
    #                 else:
    #                     invoke_all[key] = 0
    #             self.refresh_completer()
    return {
        "response": (f"""unknown configuration: {config}
        active llm:\n{json.dumps(all_accounts, indent=2)}


        all accounts:\n{json.dumps(invoke_all, indent=2)}""")
    }


@app.get("/config_get_temperature", response_model=AllAccountTemperatureConfig)
def config_get_temperature():
    return AllAccountTemperatureConfig(
        temperature=all_accounts['temperature'],
        # max_output_tokens=all_accounts['max_output_tokens']
    )


@app.post("/config_set_temperature", response_model=AllAccountTemperatureConfig)
def config_set_temperature(config: AllAccountTemperatureConfig):
    if not (0.0 <= config.temperature <= 1.0):
        raise HTTPException(status_code=400, detail="Temperature must be between 0.0 and 1.0")
    all_accounts['temperature'] = config.temperature
    return config


@app.get("/config_get_maxtokens", response_model=AllAccountMaxTokensConfig)
def config_get_maxtokens():
    return AllAccountMaxTokensConfig(
        # temperature=all_accounts['temperature'],
        max_output_tokens=all_accounts['max_output_tokens']
    )


@app.post("/config_set_maxtokens", response_model=AllAccountMaxTokensConfig)
def config_set_maxtokens(config: AllAccountMaxTokensConfig):
    # if not (0.0 <= config.temperature <= 1.0):
    #     raise HTTPException(status_code=400, detail="Temperature must be between 0.0 and 1.0")
    if config.max_output_tokens <= 0:
        raise HTTPException(status_code=400, detail="max_output_tokens must be greater than 0")

    # all_accounts['temperature'] = config.temperature
    all_accounts['max_output_tokens'] = config.max_output_tokens
    return config


@app.get("/config_get_top_p", response_model=AllAccountTopPConfig)
def config_get_top_p():
    return AllAccountTopPConfig(
        top_p=all_accounts['top_p'],
    )


@app.post("/config_set_top_p", response_model=AllAccountTopPConfig)
def config_set_top_p(config: AllAccountTopPConfig):
    if not (0.0 <= config.top_p <= 1.0):
        raise HTTPException(status_code=400, detail="Top P must be between 0.0 and 1.0")
    all_accounts['top_p'] = config.top_p
    return config


@app.get("/config_get_recursion_limit", response_model=AllAccountMaxRecursionLimit)
def config_get_recursion_limit():
    return AllAccountMaxRecursionLimit(
        recursion_limit=all_accounts['recursion_limit']
    )


@app.post("/config_set_recursion_limit", response_model=AllAccountMaxRecursionLimit)
def config_set_recursion_limit(config: AllAccountMaxRecursionLimit):
    if config.recursion_limit <= 0:
        raise HTTPException(status_code=400, detail="recursion_limit must be greater than 0")

    all_accounts['recursion_limit'] = config.recursion_limit
    return config


from schnell.app.llmutils.langchainutils.tools.github import GithubWrapper


@app.post("/searchGithub")
async def search_github(request: PromptRequest):
    keyword = request.prompt.strip()
    kwargs = {
        'keyword': keyword
    }
    if hasattr(request, 'sort_method'):
        kwargs.update({'sort_method': request.sort_method})
    else:
        kwargs.update({'sort_method': tools_config['github']["sort_method"]})
    result = GithubWrapper().search_github(**kwargs)
    result = "\n**********\n\n".join([
        f"{item[0]}\n{item[1]}\n{item[2]}"
        for item in result
    ])
    return {"response": result}


@app.post("/githubIssues")
async def github_issues(request: PromptRequest):
    github_repo = request.prompt.strip()
    return {
        "response": GithubWrapper().issues(
            github_repo, tools_config['github']["load_issues_since"]
        )
    }


class GithubConfigMaxResults(BaseModel):
    max_search_results: int


@app.get("/config_github_max_results_get", response_model=GithubConfigMaxResults)
def config_github_max_results_get():
    return GithubConfigMaxResults(
        max_search_results=tools_config['github']["max_search_results"],
    )


@app.post("/config_github_max_results_set", response_model=GithubConfigMaxResults)
def config_github_max_results_set(config: GithubConfigMaxResults):
    if not (1 <= config.max_search_results <= 1000):
        raise HTTPException(status_code=400, detail="max_search_results must be between 1 and 1000")
    tools_config['github']["max_search_results"] = config.max_search_results
    return config


class GithubConfigSortMethod(BaseModel):
    sort_method: str


@app.get("/config_github_sort_method_get", response_model=GithubConfigSortMethod)
def config_github_sort_method_get():
    return GithubConfigSortMethod(
        sort_method=tools_config['github']["sort_method"],
    )


@app.post("/config_github_sort_method_set", response_model=GithubConfigSortMethod)
def config_github_sort_method_set(config: GithubConfigSortMethod):
    if not config.sort_method in ['updated', 'stars']:
        raise HTTPException(status_code=400, detail="sort_method must be [updated, stars]")
    tools_config['github']["sort_method"] = config.sort_method
    return config


@app.post("/quickQuery")
async def quick_query(request: PromptRequest):
    user_query = request.prompt.strip()
    response = invoke_llm_active(user_query, verbose=False)
    indah4('requesting...', warna='magenta')
    print(user_query, '\n===>', response)
    return {
        "response": response
    }


@app.post("/code_query")
async def code_query(request: PromptRequest):
    user_query = request.prompt.strip()
    response = invoke_llm_code_query(
        app_configuration['code_query_prompt'][-1]
            .replace('__USER_PROMPT__', user_query),
        verbose=False
    )
    indah4('requesting...', warna='magenta')
    print(user_query, '\n===>', response)
    return {
        "response": response
    }


@app.post("/generateCodeFromFuzzyPrompt")
async def generate_code_from_fuzzy_prompt(request: PromptRequest):
    # schnell.app.llmutils.servers.fuzzy_prompt.template_str
    from schnell.app.llmutils.servers.fuzzy_prompt import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt),
        verbose=False
    )
    return {
        "response": response
    }


@app.post("/error_query")
async def error_query(request: PromptRequest):
    user_query = request.prompt.strip()
    # response = invoke_llm_error_query(user_query, verbose=False)
    response = invoke_llm_error_query(
        app_configuration['error_query_prompt'][-1]
            .replace('__USER_PROMPT__', user_query),
        verbose=False
    )
    indah4('requesting...', warna='magenta')
    print(user_query, '\n===>', response)
    return {
        "response": response
    }


@app.post("/multiQueries")
async def multi_queries(request: PromptRequest):
    user_query = request.prompt.strip()
    response = invoke_llm_all(user_query, verbose=False)
    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\llms\invoker.py
    # C:\work\ciledug\ciledug\fmusperintah\keybinders\pageup.py
    # for k,v in response.items():
    #     indah4(f"=== {k} ===\n\n{v}\n", warna=random.choice(['green', 'blue', 'cyan', 'yellow', 'magenta', 'red']))
    response_all = '\n'.join(f"=== {k} ===\n\n{v}\n" for k,v in response.items())
    return {
        "response": response_all
    }


@app.post("/explainCode")
async def explain_code(request: PromptRequest):
    from schnell.app.llmutils.servers.explain_code_prompt import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt)
    )
    return {
        "response": response
    }


@app.post("/criticCode")
async def critic_code(request: PromptRequest):
    from schnell.app.llmutils.servers.critic_code_prompt import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt)
    )
    return {
        "response": response
    }


@app.post("/refactorCodeWithExplanation")
async def refactor_code_with_explanation(request: PromptRequest):
    from schnell.app.llmutils.servers.refactor_code_prompt import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt)
    )
    return {
        "response": response
    }


@app.post("/createTest")
async def create_test(request: PromptRequest):
    from schnell.app.llmutils.servers.create_test_prompt import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt)
    )
    return {
        "response": response
    }


@app.post("/createDocumentation")
async def create_documentation(request: PromptRequest):
    from schnell.app.llmutils.servers.create_documentation import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt)
    )
    return {
        "response": response
    }


@app.post("/createProjectSkeleton")
async def create_project_skeleton(request: PromptRequest):
    from schnell.app.llmutils.servers.project_structure_prompt import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt)
    )
    return {
        "response": response
    }


# invoke_llm_active(schnell.app.llmutils.servers.research_prompt#get_prompt)
@app.post("/researchWithTools")
async def research_with_tools(request: PromptRequest):
    from schnell.app.llmutils.servers.research_prompt import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt)
    )
    return {
        "response": response
    }


@app.post("/role_researcher")
async def role_researcher(request: PromptRequest):
    from schnell.app.llmutils.langchainutils.agents.role_researcher import researcher_active
    response = researcher_active(request.prompt)
    return {
        "response": response
    }


# from schnell.app.llmutils.servers.parser.gptresearch import perform_research
@app.post("/perform_research")
async def research_endpoint(request: ResearchRequest):
    try:
        # result = await perform_research(request.query)
        # return {"result": result["result"]}
        start_time = time.time()
        result = await perform_research(request.query)
        end_time = time.time()
        duration = end_time - start_time
        return {"result": result, "time_taken": duration}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# gptresearcher
# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\workers\researcher\sample.py
# os.system("python " + r'C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\workers\researcher\sample.py '+user_query)


@app.post("/role_just_scrape_generate_code")
async def role_just_scrape_generate_code(request: PromptRequest):
    from schnell.app.llmutils.langchainutils.agents.role_just_scrape import generate_code_active
    response = generate_code_active(request.prompt)
    return {
        "response": response
    }


@app.post("/role_just_understand_code")
async def role_just_understand_code(request: PromptRequest):
    from schnell.app.llmutils.langchainutils.agents.role_just_understand import understand_code_active
    response = understand_code_active(request.prompt)
    return {
        "response": response
    }

@app.post("/fixEnglishGrammar")
async def fix_english_grammar(request: PromptRequest):
    from schnell.app.llmutils.servers.grammar_tweet_prompt import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt)
    )
    return {
        "response": response
    }


@app.post("/createMemorableStory")
async def create_memorable_story(request: PromptRequest):
    from schnell.app.llmutils.servers.create_story_prompt import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt)
    )
    return {
        "response": response
    }


@app.post("/generateBlogPost")
async def generate_blog_post(request: PromptRequest):
    from schnell.app.llmutils.servers.generate_blog_prompt import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt)
    )
    return {
        "response": response
    }


@app.post("/generateTechnicalArticle")
async def generate_technical_article(request: PromptRequest):
    from schnell.app.llmutils.servers.generate_article_prompt import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt)
    )
    return {
        "response": response
    }


@app.post("/generateBook")
async def generate_book(request: PromptRequest):
    from schnell.app.llmutils.servers.generate_book_prompt import get_prompt
    response = invoke_llm_active(
        get_prompt(request.prompt)
    )
    return {
        "response": response
    }


@app.post("/summarizeWebPage")
async def summarize_web_page(request: PromptRequest):
    # from schnell.app.llmutils.servers.summarize_url_prompt import get_prompt
    # response = invoke_llm_active(
    #     get_prompt(request.prompt)
    # )
    from schnell.app.llmutils.servers.summarization.summary2 import summarize_proxy
    from schnell.app.llmutils.servers.summarization.summary2 import summarize_webpage_by_gemini
    return {
        "response": summarize_webpage_by_gemini(request.prompt),
        # "response": summarize_proxy(request.prompt),
    }


def convert_publish_time(publish_time):
    now = datetime.now()
    if "bulan" in publish_time:
        months_ago = int(publish_time.split()[0])
        publish_date = now - timedelta(days=30 * months_ago)
    elif "tahun" in publish_time:
        years_ago = int(publish_time.split()[0])
        publish_date = now - timedelta(days=365 * years_ago)
    elif "hari" in publish_time:
        days_ago = int(publish_time.split()[0])
        publish_date = now - timedelta(days=days_ago)
    elif "minggu" in publish_time:
        weeks_ago = int(publish_time.split()[0])
        publish_date = now - timedelta(weeks=weeks_ago)
    elif "jam" in publish_time:
        hours_ago = int(publish_time.split()[0])
        publish_date = now - timedelta(hours=hours_ago)
    elif "menit" in publish_time:
        minutes_ago = int(publish_time.split()[0])
        publish_date = now - timedelta(minutes=minutes_ago)
    elif "detik" in publish_time:
        seconds_ago = int(publish_time.split()[0])
        publish_date = now - timedelta(seconds=seconds_ago)
    else:
        # If the format is different or not recognized, return current date as a fallback
        publish_date = now
    return publish_date

# Sample usage:
# publish_time = '1 bulan yang lalu'
# converted_time = convert_publish_time(publish_time)
# print(converted_time)

def format_video(video):
    youtube_url = "https://www.youtube.com"
    thumbnails = '\n'.join([f"{i+1}. {thumbnail}" for i, thumbnail in enumerate(video['thumbnails'])])
    full_url = youtube_url + video['url_suffix']
    return f"{video['title']}\n{full_url}\n{video['channel']} {video['id']}\nduration: {video['duration']}, views: {video['views']}, published: {video['publish_time']}\nthumbnails:\n{thumbnails}"

def format_video_list(video_list):
    # formatted_videos = [format_video(video) for video in video_list]
    # sorted_videos = sorted(video_list, key=lambda x: x['publish_time'])
    sorted_videos = sorted(video_list, key=lambda x: convert_publish_time(x['publish_time']), reverse=True)
    formatted_videos = [format_video(video) for video in sorted_videos]
    replaced_formatted_videos = []
    # for idx,item in enumerate(formatted_videos,1):
    #     replaced_formatted_videos.append(item.replace('NUMERO', str(idx)))
    return formatted_videos

@app.post("/searchYoutube")
async def search_youtube(request: PromptRequest):
    query = request.prompt
    result = U2().search(query)
    result = format_video_list(result)
    result = "\n********\n\n\n".join(result)
    print(type(result))
    print(result)
    # result = json.dumps(result, indent=2)
    return {"response": result}


@app.post("/searchInternet")
async def search_internet(request: PromptRequest):
    query = request.prompt
    result = Tapir().search(query)
    # result = json.dumps(result, indent=2)
    # return {"response": result}
    # Parse the JSON response
    # result_dict = json.loads(result)
    # results = result_dict.get("results", [])
    results = result.get("results", [])
    # Format the results
    formatted_results = ""
    for idx, item in enumerate(results, start=1):
        formatted_results += (
            f"{idx}. {item['title']}\n"
            f"{item['url']}\n"
            f"Score: {item['score']}\n"
            f"{item['content']}\n\n"
        )

    return {"response": formatted_results.strip()}


# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\proxy\litellm\proxy\proxy_server.py
# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\proxy\litellm\proxy\proxy_cli.py
# python C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\proxy\litellm\proxy\proxy_cli.py --model gemini/gemini-pro


# "http://localhost:8000/v1"
# https://platform.openai.com/docs/api-reference/streaming?lang=python
# from openai import OpenAI
# client = OpenAI(
#     api_key="sk-fake",
#     base_url="http://localhost:8000/v1"
# )
# user_prompt = "give sample of implicit in scala and compare it to python"
# stream = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": user_prompt}],
#     stream=True,
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")
from endpoints.vscode_ext import endpoint_vscode_ext
endpoint_vscode_ext(app, current_dir)

from endpoints.file_ops import endpoint_file_ops
endpoint_file_ops(app, current_dir)

from endpoints.addresses import endpoint_addresses
endpoint_addresses(app, current_dir)

from endpoints.static_files import router as markdown_router
# http://localhost:8000/api/get_markdown/BANTUAN.md
# http://localhost:8000/get_markdown/BANTUAN.md
# app.include_router(markdown_router, prefix="/api")
app.include_router(markdown_router)

from endpoints.litellm_endpoint import router as litellm_router
app.include_router(litellm_router)


@app.on_event("startup")
async def print_routes():
    routes = []
    for route in app.routes:
        route_info = f"Path: {route.path}, Method(s): {route.methods}"
        routes.append(route_info)
    print("\nAvailable routes:\n" + "\n".join(routes))

# # Optionally, you can also create a route to fetch available endpoints
# @app.get("/list_routes")
# async def list_routes():
#     routes = []
#     for route in app.routes:
#         print(route)
#         routes.append({"path": route.path, "methods": list(route.methods)})
#     return routes

@app.get("/list_routes")
async def list_routes():
    routes = []
    for route in app.routes:
        if hasattr(route, 'methods'):
            routes.append({"path": route.path, "methods": list(route.methods)})
        else:
            routes.append({"path": route.path, "type": type(route).__name__})  # Handle WebSocket routes
    return routes

# @app.get("/comboboxes/terminal-widget")
# async def get_terminal_widget_options():
#     return [
#         "Option 1 from server",
#         "Option 2 from server",
#         "Option 3 from server"
#     ]
import uvicorn
if __name__ == "__main__":
    # uvicorn app:app --host 127.0.0.1 --port 8000
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run(
        # "serve:app",  # Replace "serve" with the appropriate module name if needed
        app,
        host="0.0.0.0",
        port=8000,
        log_level="debug"  # Set log level to debug
    )