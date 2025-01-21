from openai import OpenAI

openai_model = 'gpt-4o-mini'
OPENAI_API_KEY='sk-none'
client = OpenAI(api_key=OPENAI_API_KEY)
# client = OpenAI(api_key=config_app['openai_key'])


def create_client(key):
    global client
    client = OpenAI(api_key=key)


def get_response(pertanyaan, model=openai_model, temperature=0):
    try:
        completion =  client.chat.completions.create(
            model=model,
            messages=[
                {
                    'role': 'user', 
                    'content': pertanyaan
                }
            ],
            temperature=temperature,
        )
        reply_content = completion.choices[0].message.content
        return reply_content
    except Exception as err:
        return str(err)


def get_stream(pertanyaan, callback=None, model=openai_model, temperature=0):
    try:
        completion =  client.chat.completions.create(
            model=model,
            messages=[
                {
                    'role': 'user', 
                    'content': pertanyaan
                }
            ],
            temperature=temperature,
            stream=True,
        )
        chunk_message = chunk.choices[0].delta.content
        collected_messages = []
        for chunk in completion:
            # chunk_time = time.time() - start_time  # calculate the time delay of the chunk
            # collected_chunks.append(chunk)  # save the event response
            chunk_message = chunk.choices[0].delta.content  # extract the message
            if chunk_message:
                collected_messages.append(chunk_message)  # save the message
                if callback:
                    callback(chunk_message)
        collected_messages = [m for m in collected_messages if m is not None]
        full_reply_content = ''.join([m for m in collected_messages])
        return full_reply_content
    except Exception as err:
        return str(err)

# # Example of an OpenAI ChatCompletion request
# # https://platform.openai.com/docs/guides/chat

# # record the time before the request is sent
# start_time = time.time()

# # send a ChatCompletion request to count to 100
# completion =  client.chat.completions.create(
#     model='gpt-3.5-turbo',
#     messages=[
#         {
#             'role': 'user', 
#             'content': 'Count to 100, with a comma between each number and no newlines. E.g., 1, 2, 3, ...'
#         }
#     ],
#     temperature=0,
# )
# # calculate the time it took to receive the response
# response_time = time.time() - start_time

# # print the time delay and text received
# print(f"Full response received {response_time:.2f} seconds after request")
# print(f"Full response received:\n{completion}")
# reply = completion.choices[0].message
# print(f"Extracted reply: \n{reply}")
# # ini yg kita cari
# reply_content = completion.choices[0].message.content
# print(f"Extracted content: \n{reply_content}")




# completion = client.chat.completions.create(
#     model='gpt-3.5-turbo',
#     messages=[
#         {'role': 'user', 'content': "What's 1+1? Answer in one word."}
#     ],
#     temperature=0,
#     stream=True  # this time, we set stream=True
# )

# for chunk in completion:
#     print(chunk)
#     print(chunk.choices[0].delta.content)
#     print("****************")


# # Example of an OpenAI ChatCompletion request with stream=True
# # https://platform.openai.com/docs/guides/chat

# # record the time before the request is sent
# start_time = time.time()

# # send a ChatCompletion request to count to 100
# completion = client.chat.completions.create(
#     model='gpt-3.5-turbo',
#     messages=[
#         {
#             'role': 'user', 
#             'content': 'Count to 100, with a comma between each number and no newlines. E.g., 1, 2, 3, ...'
#         }
#     ],
#     temperature=0,
#     stream=True  # again, we set stream=True
# )
# # create variables to collect the stream of chunks
# collected_chunks = []
# collected_messages = []
# # iterate through the stream of events
# for chunk in completion:
#     chunk_time = time.time() - start_time  # calculate the time delay of the chunk
#     collected_chunks.append(chunk)  # save the event response
#     chunk_message = chunk.choices[0].delta.content  # extract the message
#     collected_messages.append(chunk_message)  # save the message
#     print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")  # print the delay and text

# # print the time delay and text received
# print(f"Full response received {chunk_time:.2f} seconds after request")
# # clean None in collected_messages
# collected_messages = [m for m in collected_messages if m is not None]
# full_reply_content = ''.join([m for m in collected_messages])
# print(f"Full conversation received: {full_reply_content}")


def pembantu():
    # https://platform.openai.com/docs/assistants/overview
    assistant = client.beta.assistants.create(
        name="Math Tutor",
        instructions="You are a personal math tutor. Write and run code to answer math questions.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-1106-preview"
    )
    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions="Please address the user as Jane Doe. The user has a premium account."
    )
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

def image_generate():
    response = client.images.generate(
        model="dall-e-3",
        prompt="a white siamese cat",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url

def image_edit():
    response = client.images.edit(
        model="dall-e-2",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo",
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url

def image_variation():
    response = client.images.create_variation(
        image=open("image_edit_original.png", "rb"),
        n=2,
        size="1024x1024"
    )

    image_url = response.data[0].url

def vision_quickstart():
    # from openai import OpenAI
    # client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s in this image?"},
                {
                "type": "image_url",
                "image_url": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                },
                },
            ],
            }
        ],
        max_tokens=300,
    )

    print(response.choices[0])

def vision_upload_image():
    import base64
    import requests

    # OpenAI API Key
    api_key = "YOUR_OPENAI_API_KEY"

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Path to your image
    image_path = "path_to_your_image.jpg"

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What’s in this image?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    print(response.json())

def vision_multiple_image_inputs():
    # from openai import OpenAI
    # client = OpenAI()
    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "What are in these images? Is there any difference between them?",
            },
            {
            "type": "image_url",
            "image_url": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            },
            },
            {
            "type": "image_url",
            "image_url": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )
    print(response.choices[0])

def vision_lo_hi_fidelity():
    # from openai import OpenAI
    # client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "What’s in this image?"},
            {
            "type": "image_url",
            "image_url": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                "detail": "high"
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )

    print(response.choices[0].message.content)


def tts_quickstart():
    from pathlib import Path
    # from openai import OpenAI
    # client = OpenAI()

    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Today is a wonderful day to build something people love!"
    )

    response.stream_to_file(speech_file_path)

def tts_streaming_audio():
    # from openai import OpenAI
    # client = OpenAI()

    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input="Hello world! This is a streaming test.",
    )

    response.stream_to_file("output.mp3")

def speechtotext_quickstart():
    # from openai import OpenAI
    # client = OpenAI()

    audio_file= open("/path/to/file/audio.mp3", "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )
def speechtotext_quickstart2():
    # from openai import OpenAI
    # client = OpenAI()

    audio_file = open("speech.mp3", "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
    )

def translate_audio():
    # from openai import OpenAI
    # client = OpenAI()

    audio_file= open("/path/to/file/german.mp3", "rb")
    transcript = client.audio.translations.create(
    model="whisper-1", 
    file=audio_file
    )

def longer_audio():
    from pydub import AudioSegment

    song = AudioSegment.from_mp3("good_morning.mp3")

    # PyDub handles time in milliseconds
    ten_minutes = 10 * 60 * 1000

    first_10_minutes = song[:ten_minutes]

    first_10_minutes.export("good_morning_10.mp3", format="mp3")

