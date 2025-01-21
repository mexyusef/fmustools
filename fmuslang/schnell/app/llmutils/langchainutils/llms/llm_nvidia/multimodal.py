# https://build.nvidia.com/nvidia/neva-22b
# nvidia / neva-22b
# Multi-modal vision-language model that understands text/images and generates informative responses

import requests, base64

invoke_url = "https://ai.api.nvidia.com/v1/vlm/nvidia/neva-22b"
stream = True

with open("dog.png", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode()

assert len(image_b64) < 180_000, \
  "To upload larger images, use the assets API (see docs)"

headers = {
  "Authorization": "Bearer $API_KEY_REQUIRED_IF_EXECUTING_OUTSIDE_NGC",
  "Accept": "text/event-stream" if stream else "application/json"
}

payload = {
  "messages": [
    {
      "role": "user",
      "content": f'Describe what you see in this image. <img src="data:image/png;base64,{image_b64}" />'
    }
  ],
  "max_tokens": 1024,
  "temperature": 0.20,
  "top_p": 0.70,
  "seed": 0,
  "stream": stream
}

response = requests.post(invoke_url, headers=headers, json=payload)

if stream:
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))
else:
    print(response.json())


# https://build.nvidia.com/microsoft/microsoft-kosmos-2
# microsoft / kosmos-2

import requests, base64

invoke_url = "https://ai.api.nvidia.com/v1/vlm/microsoft/kosmos-2"

with open("soccer.png", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode()

assert len(image_b64) < 180_000, \
  "To upload larger images, use the assets API (see docs)"

headers = {
  "Authorization": "Bearer $API_KEY_REQUIRED_IF_EXECUTING_OUTSIDE_NGC",
  "Accept": "application/json"
}

payload = {
  "messages": [
    {
      "role": "user",
      "content": f'Who is in this photo? <img src="data:image/png;base64,{image_b64}" />'
    }
  ],
  "max_tokens": 1024,
  "temperature": 0.20,
  "top_p": 0.20
}

response = requests.post(invoke_url, headers=headers, json=payload)

print(response.json())

# https://build.nvidia.com/adept/fuyu-8b
# adept / fuyu-8b

import requests, base64

invoke_url = "https://ai.api.nvidia.com/v1/vlm/adept/fuyu-8b"
stream = True

with open("mountain.png", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode()

assert len(image_b64) < 180_000, \
  "To upload larger images, use the assets API (see docs)"

headers = {
  "Authorization": "Bearer $API_KEY_REQUIRED_IF_EXECUTING_OUTSIDE_NGC",
  "Accept": "text/event-stream" if stream else "application/json"
}

payload = {
  "messages": [
    {
      "role": "user",
      "content": f'What do you see in the following image? <img src="data:image/png;base64,{image_b64}" />'
    }
  ],
  "max_tokens": 1024,
  "temperature": 0.20,
  "top_p": 0.70,
  "seed": 0,
  "stream": stream
}

response = requests.post(invoke_url, headers=headers, json=payload)

if stream:
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))
else:
    print(response.json())
