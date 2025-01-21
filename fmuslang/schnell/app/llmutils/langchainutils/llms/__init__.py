import copy
import json
import os
import random
import time
from functools import wraps
from langchain.chains.conversation.memory import ConversationBufferMemory, ConversationSummaryMemory
# C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\configs.py
from schnell.app.llmutils.langchainutils.llm_config import *

# https://github.com/aws/sagemaker-python-sdk/issues/4123
# Sagemaker continuously complains about config, so we'll suppress it
import logging
logging.getLogger("sagemaker.config").setLevel(logging.WARNING)

# Custom Memory Classes with newline separation
class CustomConversationBufferMemory(ConversationBufferMemory):
    def save_context(self, inputs, outputs):
        if self.buffer:
            self.buffer += f"\n{inputs} {outputs}"
        else:
            self.buffer = f"{inputs} {outputs}"
    def load_memory_variables(self, inputs):
        buffer = super().load_memory_variables(inputs)
        if self.buffer:
            buffer['history'] = "\n".join(self.buffer.split(" "))
        return buffer

class CustomConversationSummaryMemory(ConversationSummaryMemory):
    def save_context(self, inputs, outputs):
        if self.buffer:
            self.buffer += f"\n{inputs} {outputs}"
        else:
            self.buffer = f"{inputs} {outputs}"
    def load_memory_variables(self, inputs):
        buffer = super().load_memory_variables(inputs)
        if self.buffer:
            buffer['history'] = "\n".join(self.buffer.split(" "))
        return buffer


# Decorator to use memory
# from schnell.app.llmutils.langchainutils.llms import use_memory
def use_memory(memory_type='buffer'):

    # c:\users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\llms\__init__.py:40: LangChainDeprecationWarning: Please see the migration guide at: https://python.langchain.com/docs/versions/migrating_memory/
    # buffer_memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    # sagemaker.config INFO - Not applying SDK defaults from location: C:\ProgramData\sagemaker\sagemaker\config.yaml
    # sagemaker.config INFO - Not applying SDK defaults from location: C:\Users\usef\AppData\Local\sagemaker\sagemaker\config.yam

    # Initialize memory instances
    # buffer_memory = CustomConversationBufferMemory() # gagal nih
    # https://python.langchain.com/docs/versions/migrating_memory/
    buffer_memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    # buffer_memory = ConversationBufferMemory()
    # summary_memory = ConversationSummaryMemory()

    # Dictionary to hold memory instances
    memory_instances = {
        'buffer': buffer_memory,
        # 'summary': summary_memory
    }

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            memory = memory_instances.get(memory_type)
            if 'memory' in kwargs:
                return func(*args, **kwargs)
            else:
                return func(*args, memory=memory, **kwargs)
        return wrapper
    return decorator

# from schnell.app.llmutils.langchainutils.llms import with_memory_static
def with_memory_static(use_memory=False, memory_type='buffer'):
    def decorator(create_llm_func):
        @wraps(create_llm_func)
        def wrapper(*args, **kwargs):
            llm = create_llm_func(*args, **kwargs)
            if use_memory:
                if memory_type == 'buffer':
                    memory = ConversationBufferMemory()
                elif memory_type == 'summary':
                    memory = ConversationSummaryMemory()
                else:
                    raise ValueError("Invalid memory type. Choose 'buffer' or 'summary'.")
                return lambda input_text: llm(input_text, memory=memory)
            return llm
        return wrapper
    return decorator

# from schnell.app.llmutils.langchainutils.llms import with_memory
def with_memory_not_ok(use_memory=True, memory_type='buffer'):
    def decorator(create_llm_func):
        @wraps(create_llm_func)
        def wrapper(*args, **kwargs):
            llm = create_llm_func(*args, **kwargs)
            if use_memory:
                if memory_type == 'buffer':
                    memory = ConversationBufferMemory()
                elif memory_type == 'summary':
                    memory = ConversationSummaryMemory()
                else:
                    raise ValueError("Invalid memory type. Choose 'buffer' or 'summary'.")
                return lambda input_text: llm(input_text, memory=memory)
            return llm
        return wrapper
    return decorator

from typing import ClassVar
class CustomConversationBufferMemory2(ConversationBufferMemory):

    # string_buffer = ""
    string_buffer: ClassVar[str] = ""  # Annotate as ClassVar

    def add_message(self, message):
        # Add a newline before appending the new message
        if self.string_buffer:
            self.string_buffer += "\n\n"
        self.string_buffer += message
    # def load_from_file(self, file_path):
    #     try:
    #         with open(file_path, 'r') as file:
    #             data = json.load(file)
    #             self.chat_memory.messages = data.get("messages", [])
    #             print(f"Memory loaded from {file_path}")
    #     except FileNotFoundError:
    #         print(f"No memory file found at {file_path}. Starting with empty memory.")
    #     except json.JSONDecodeError:
    #         print(f"Error decoding memory file at {file_path}. Starting with empty memory.")

    # def save_to_file(self, file_path):
    #     with open(file_path, 'w') as file:
    #         data = {
    #             "messages": self.chat_memory.messages
    #         }
    #         json.dump(data, file, indent=2)
    #         print(f"Memory saved to {file_path}")
    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.string_buffer = data.get("buffer", [])
                print(f"Memory loaded from {file_path}")
        except FileNotFoundError:
            print(f"No memory file found at {file_path}. Starting with empty memory.")
        except json.JSONDecodeError:
            print(f"Error decoding memory file at {file_path}. Starting with empty memory.")

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            data = {
                "buffer": self.string_buffer
            }
            json.dump(data, file, indent=2)
            print(f"Memory saved to {file_path}")


def inspect_methods(llm):
    methods = [method for method in dir(llm) if callable(getattr(llm, method))]
    print("Available methods:", methods)

# def with_memory(use_memory=True, memory_type='buffer', memory_file='c:/tmp/with_memory.json'):
#     def decorator(create_llm_func):
#         @wraps(create_llm_func)
#         def wrapper(*args, **kwargs):
#             llm = create_llm_func(*args, **kwargs)
#             if use_memory:
#                 if memory_type == 'buffer':
#                     memory = CustomConversationBufferMemory()
#                 elif memory_type == 'summary':
#                     memory = ConversationSummaryMemory()
#                 else:
#                     raise ValueError("Invalid memory type. Choose 'buffer' or 'summary'.")
                
#                 if memory_file:
#                     memory.load_from_file(memory_file)

#                 # # return lambda input_text: llm(input_text, memory=memory)
#                 # original_invoke = llm.invoke
#                 # def invoke_with_memory(input_text):
#                 #     return original_invoke(input_text, memory=memory)

#                 # llm.invoke = invoke_with_memory

#                 # Wrap the appropriate method
#                 original_method = getattr(llm, 'predict', None) or getattr(llm, 'generate', None)

#                 if original_method is None:
#                     raise AttributeError("LLM instance does not have a 'predict' or 'generate' method.")

#                 def method_with_memory(input_text):
#                     # Modify as needed based on actual LLM method
#                     response = original_method(input_text)
#                     if memory_file:
#                         memory.save_to_file(memory_file)
#                     return response

#                 setattr(llm, 'invoke', method_with_memory)
#                 # # Wrap the `invoke` method to include memory
#                 # original_invoke = llm.invoke
#                 # def invoke_with_memory(input_text):
#                 #     return original_invoke(input_text, memory=memory)
#                 # llm.invoke = invoke_with_memory

#                 # inspect_methods(llm)

#                 # # Wrap the correct method (assumed `predict` here, change as needed)
#                 # original_predict = llm.predict

#                 # def predict_with_memory(input_text):
#                 #     memory.chat_memory.add_user_message(input_text)
#                 #     response = original_predict(input_text)
#                 #     memory.chat_memory.add_ai_message(response)
#                 #     if memory_file:
#                 #         memory.save_to_file(memory_file)
#                 #     return response

#                 # llm.predict = predict_with_memory
#                 # # Wrap the correct method (assumed `generate` here)
#                 # original_generate = llm.generate

#                 # def generate_with_memory(input_text):
#                 #     response = original_generate(input_text)
#                 #     memory.chat_memory.add_user_message(input_text)
#                 #     memory.chat_memory.add_ai_message(response)
#                 #     if memory_file:
#                 #         memory.save_to_file(memory_file)
#                 #     return response

#                 # llm.generate = generate_with_memory

#             return llm
#         return wrapper
#     return decorator

def with_memory(use_memory=True, memory_type='buffer', memory_file='c:/tmp/with_memory.json'):
    def decorator(create_llm_func):
        @wraps(create_llm_func)
        def wrapper(*args, **kwargs):
            llm = create_llm_func(*args, **kwargs)
            if use_memory:
                if memory_type == 'buffer':
                    memory = CustomConversationBufferMemory()
                elif memory_type == 'summary':
                    memory = ConversationSummaryMemory()
                else:
                    raise ValueError("Invalid memory type. Choose 'buffer' or 'summary'.")
                
                if memory_file:
                    memory.load_from_file(memory_file)

                # Determine the correct method to wrap
                original_method = getattr(llm, 'generate', None)  # Use the appropriate method

                if original_method is None:
                    raise AttributeError("LLM instance does not have a 'generate' method.")

                def method_with_memory(input_text):
                    response = original_method(input_text)
                    if memory_file:
                        memory.save_to_file(memory_file)
                    return response

                setattr(llm, 'invoke', method_with_memory)
            return llm
        return wrapper
    return decorator


def with_memory0(use_memory=True, memory_type='buffer', file_path='c:/tmp/with_memory.json'):
    def decorator(create_llm_func):
        @wraps(create_llm_func)
        def wrapper(*args, **kwargs):
            llm = create_llm_func(*args, **kwargs)
            if use_memory:
                if memory_type == 'buffer':
                    # memory = ConversationBufferMemory()
                    memory = CustomConversationBufferMemory()
                elif memory_type == 'summary':
                    memory = ConversationSummaryMemory()
                else:
                    raise ValueError("Invalid memory type. Choose 'buffer' or 'summary'.")

                # # Wrap the `invoke` method to include memory
                # original_invoke = llm.invoke
                # def invoke_with_memory(input_text):
                #     return original_invoke(input_text, memory=memory)
                # llm.invoke = invoke_with_memory

                # # Wrap the `__call__` method to include memory
                # original_call = llm.__call__
                # def call_with_memory(input_text):
                #     memory.append_user_input(input_text)
                #     history = memory.load_memory_variables({})
                #     context_input = history['history'] + input_text
                #     response = original_call(context_input)
                #     memory.append_ai_output(response)
                #     return response
                # llm.__call__ = call_with_memory

                # Load memory from file
                memory.load_from_file(file_path)

                # Wrap the `__call__` method to include memory
                original_call = llm.__call__
                def call_with_memory(input_text):
                    memory.append_user_input(input_text)
                    history = memory.load_memory_variables({})
                    context_input = history['history'] + input_text
                    response = original_call(context_input)
                    memory.append_ai_output(response)
                    return response
                llm.__call__ = call_with_memory

                # Add save method to llm instance
                def save_memory():
                    memory.save_to_file(file_path)
                llm.save_memory = save_memory

            return llm
        return wrapper
    return decorator

# # Wrap the create_llm function with the desired memory settings
# create_llm_with_memory = with_memory(use_memory=True, memory_type='buffer')(create_llm)
# # Create LLM instance with memory enabled
# llm_with_memory = create_llm_with_memory(api_key, model, temperature, max_tokens)
# user_input = "Hello, how are you?"
# response = llm_with_memory(user_input)
# print(response)

# cara gunakan paling cepat:
# llm = with_memory()(create_llm)
# llm = with_memory(memory_type='buffer')(create_llm)
# llm = with_memory(memory_type='summary')(create_llm)

def cohere_instances():
    return [info['instance'] for (account, info) in cohere_accounts.items()]

gemini_vision_accounts = copy.deepcopy(gemini_accounts)

# gemini_accounts_instances = [account['instance'] for account in gemini_accounts]
def gemini_instances():
    return [info['instance'] for (account, info) in gemini_accounts.items()]

def groq_instances():
    return [info['instance'] for (account, info) in groq_accounts.items()]

def openai_instances():
    return [info['instance'] for (account, info) in openai_accounts.items()]

def together_instances():
    return [info['instance'] for (account, info) in together_accounts.items()]

def huggingface_instances():
    return [info['instance'] for (account, info) in huggingface_accounts.items()]

# from schnell.app.llmutils.langchainutils.llms import randomly_select_account, nvidia_accounts
def randomly_select_account(accounts=gemini_accounts):
    # seed = time.time()  # Use system time to generate seed
    seed = int.from_bytes(os.urandom(4), byteorder='big')
    random.seed(seed)
    selected_account = random.choice(list(accounts.keys()))
    return selected_account

def test_randomly_select_account():
    selected_key = randomly_select_account()
    print("Selected key:", selected_key)
