# gptutils

pemikiran
kita pengen masukkan ini ke dalam mkhelp.
alih2 get_input
kita gunakan ctrl+g/p/t sbg prompt...
lalu kapan chatbot dibuat?
bagusnya pas shift,ctrl,something saja. jd satu searcher satu chatbot.

knp hrs maksimalkan chatgpt
krn kita pengen segera cepat2 upwork+medium.

"""
chatbot = Chatbot({
   # This could be blank but the dict should be here
})

def __init__(self, config, conversation_id=None, parent_id=None, debug=False, request_timeout=100,
                captcha_solver=None, base_url="https://chat.openai.com/", max_rollbacks=20):


- `config` (`:obj:`json``): The configuration json
- `conversation_id` (`:obj:`str`, optional`): The conversation ID
- `parent_id` (`:obj:`str`, optional`): The parent ID
- `debug` (`:obj:`bool`, optional`): Whether to enable debug mode
- `refresh` (`:obj:`bool`, optional`): Whether to refresh the session
- `request_timeout` (`:obj:`int`, optional`): The network request timeout seconds
- `base_url` (`:obj:`str`, optional`): The base url to chat.openai.com backend server,
useful when set up a reverse proxy to avoid network issue.

!help - Show this message
!reset - Forget the current conversation
    chatbot.reset_chat()
    Reset the conversation ID and parent ID.
!refresh - Refresh the session authentication
    chatbot.refresh_session()
    Refresh the session.
!rollback - Rollback the conversation by 1 message
    num = int(prompt.split(" ")[1])
    num = 1
    chatbot.rollback_conversation(num)
    Rollback the conversation.
!config - Show the current configuration
    print(json.dumps(config, indent=4))
!exit - Exit the program

async def get_chat_response(prompt: str,
                            output="text",
                            conversation_id=None,
                            parent_id=None) -> dict or None
Get the chat response.
- `prompt` (`:obj:`str``): The message sent to the chatbot
- `output` (`:obj:`str`, optional`): The output type `text` or `stream`

`:obj:`dict` or :obj:`None``: 
The chat response `{"message": "Returned messages", "conversation_id": "conversation ID", "parent_id": "parent ID"}` or None

message = chatbot.get_chat_response(prompt)
print(message["message"])

lines_printed = 0
print("Chatbot: ")
formatted_parts = []
for message in chatbot.get_chat_response(prompt, output="stream"):
    # Split the message by newlines
    message_parts = message["message"].split("\n")
    # Wrap each part separately
    formatted_parts = []
    for part in message_parts:
        formatted_parts.extend(textwrap.wrap(part, width=80))
        for _ in formatted_parts:
            if len(formatted_parts) > lines_printed + 1:
                print(formatted_parts[lines_printed])
                lines_printed += 1
print(formatted_parts[lines_printed])

## Desktop environments:
A Chrome/Chromium/Firefox window will show up.
1. Wait for the Cloudflare checks to pass
2. Log into OpenAI via the open browser (Google/Email-Password/Etc)
3. It should automatically redirect you to `https://chat.openai.com/chat` after logging in. If it doesn't, go to this link manually after logging in.
4. The window should close automatically
5. You are good to go

## Servers:
You must define the session token in the config:

You can find the session token manually from your browser:
1. Go to `https://chat.openai.com/api/auth/session`
2. Press `F12` to open console
3. Go to `Application` > `Cookies`
4. Copy the session token value in `__Secure-next-auth.session-token`
5. Paste it into `config.json` in the current working directory
```json
{"session_token":"<YOUR_TOKEN>"}
```

{
    "session_token": "<YOUR TOKEN>",
    "cf_clearance": "<cf_clearance cookie value>",
    "user_agent": "<USER_AGENT>"
}

{
  "session_token": "<token>",
  "proxy":"<proxy>",
  "accept_language": "en-US,en"
}
"""

# ffmpeg
https://github.com/kkroening/ffmpeg-python
pip install ffmpeg-python

stream = ffmpeg.input('dummy.mp4')
stream = ffmpeg.filter(stream, 'fps', fps=25, round='up')
stream = ffmpeg.output(stream, 'dummy2.mp4')
ffmpeg.run(stream)

(
  ffmpeg
  .input('dummy.mp4')
  .filter('fps', fps=25, round='up')
  .output('dummy2.mp4')
  .run()
)

import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpg')
im_resized = cv2.resize(im, (224, 224), interpolation=cv2.INTER_LINEAR)

plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
plt.show()

from pylab import imread,subplot,imshow,show

import matplotlib.pyplot as plt

image = imread('...')  // choose image location

plt.imshow(image)

from IPython.display import display, Image
display(Image(filename='path/to/image.jpg'))

/tmp/hapus,d
  &append
  $code /home/usef/danger/by-examples/generated/session
  #$qterminal -w /home/usef/danger/by-examples/generated/session 2>/dev/null
