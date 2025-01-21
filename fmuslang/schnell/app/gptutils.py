# Credits to github.com/rawandahmad698/PyChatGPT
import re
import urllib
import base64
# pip install tls-client
# pip install cf_clearance2
# pip install playwright
# pip install nest-asyncio
# pip install httpx
# pip install tls-client cf_clearance2 playwright nest-asyncio httpx --user
import tls_client
import json
import uuid
import asyncio
import httpx
import nest_asyncio
from typing import List
# from playwright.async_api import async_playwright
# from cf_clearance2 import async_cf_retry, async_stealth
# from cf_clearance import async_cf_retry, async_stealth
import textwrap
from os.path import exists
from os import getenv
from sys import argv, exit

from .fileutils import file_write_timestamped_under_rootdir
from .printutils import indah4


def generate_uuid() -> str:
    """
    Generate a UUID for the session -- Internal use only

    :return: a random UUID
    :rtype: :obj:`str`
    """
    uid = str(uuid.uuid4())
    return uid


USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'


class Debugger:
    def __init__(self, debug: bool = False):
        # C:\Users\usef\work\sidoarjo\data\gpt-data\README.md
        # def file_write_timestamped_under_rootdir(filename, content, foldername='data/guilang-output', formatter='%Y%m%d_%H%M%S', write_mode='w'):
        if debug:
            print("Debugger enabled on OpenAIAuth")
        self.debug = debug
        # self.filename = 'gpt-chat.txt'
        # self.foldername = 'data/gpt-data'

    # def write(self, content):
    #     file_write_timestamped_under_rootdir(self.filename, content, self.foldername, write_mode='a+')

    def set_debug(self, debug: bool):
        self.debug = debug

    def log(self, message: str, end: str = "\n"):
        if self.debug:
            print(message, end=end)
        # self.write(message)  # debug or not, tetap log


class ChatGPTException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class AuthError(ChatGPTException):
    pass


class ExpiredAccessToken(AuthError):
    pass


class InvalidAccessToken(AuthError):
    pass


class InvalidCredentials(AuthError):
    pass


class APIError(ChatGPTException):
    pass


class NetworkError(ChatGPTException):
    pass


class HTTPError(NetworkError):
    pass


class HTTPStatusError(HTTPError):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code


class OpenAIAuth:
    def __init__(
        self,
        email_address: str,
        password: str,
        proxy: str = None,
        debug: bool = False,
        use_captcha: bool = True,
        captcha_solver: any = None,
        cf_clearance: str = None,
        user_agent: str = None,
    ):
        self.session_token = None
        self.email_address = email_address
        self.password = password
        self.proxy = proxy
        self.session = tls_client.Session(
            client_identifier="chrome_105"
        )
        self.session.cookies.set("cf_clearance", cf_clearance)
        self.access_token: str = None
        self.debugger = Debugger(debug)
        self.use_capcha = use_captcha
        self.captcha_solver: any = captcha_solver
        self.user_agent = user_agent

    @staticmethod
    def url_encode(string: str) -> str:
        """
        URL encode a string
        :param string:
        :return:
        """
        return urllib.parse.quote(string)

    def begin(self) -> None:
        """
        Begin the auth process
        """
        self.debugger.log("Beginning auth process")
        if not self.email_address or not self.password:
            return

        if self.proxy:
            proxies = {
                "http": self.proxy,
                "https": self.proxy,
            }
            self.session.proxies = proxies

        # First, make a request to https://chat.openai.com/auth/login
        url = "https://chat.openai.com/auth/login"
        headers = {
            "Host": "ask.openai.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": self.user_agent,
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        response = self.session.get(
            url=url, headers=headers)
        if response.status_code == 200:
            self.part_two()
        else:
            self.debugger.log("Error in part one")
            self.debugger.log("Response: ", end="")
            self.debugger.log(response.text)
            self.debugger.log("Status code: ", end="")
            self.debugger.log(response.status_code)
            raise Exception("API error")

    def part_two(self) -> None:
        """
        In part two, We make a request to https://chat.openai.com/api/auth/csrf and grab a fresh csrf token
        """
        self.debugger.log("Beginning part two")

        url = "https://chat.openai.com/api/auth/csrf"
        headers = {
            "Host": "ask.openai.com",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "User-Agent": self.user_agent,
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Referer": "https://chat.openai.com/auth/login",
            "Accept-Encoding": "gzip, deflate, br",
        }
        response = self.session.get(
            url=url, headers=headers)
        if response.status_code == 200 and "json" in response.headers["Content-Type"]:
            csrf_token = response.json()["csrfToken"]
            self.part_three(token=csrf_token)
        else:
            self.debugger.log("Error in part two")
            self.debugger.log("Response: ", end="")
            self.debugger.log(response.text)
            self.debugger.log("Status code: ", end="")
            self.debugger.log(response.status_code)
            raise Exception("Error logging in")

    def part_three(self, token: str) -> None:
        """
        We reuse the token from part to make a request to /api/auth/signin/auth0?prompt=login
        """
        self.debugger.log("Beginning part three")
        self.session.cookies.clear()  # DEBUG
        url = "https://chat.openai.com/api/auth/signin/auth0?prompt=login"
        payload = f'callbackUrl=%2F&csrfToken={token}&json=true'
        headers = {
            "Host": "chat.openai.com",
            "Content-Length": str(len(payload)),
            "User-Agent": self.user_agent,
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Sec-Gpc": "1",
            "Accept-Language": "en-US,en;q=0.8",
            "Origin": "https://chat.openai.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://chat.openai.com/auth/login",
            "Accept-Encoding": "gzip, deflate",
        }
        self.debugger.log("Payload: " + payload)
        self.debugger.log("Payload length: " + str(len(payload)))
        self.debugger.log("Content length: " + headers["Content-Length"])
        response = self.session.post(url=url, headers=headers, data=payload)
        if response.status_code == 200 and "json" in response.headers["Content-Type"]:
            url = response.json()["url"]
            if url == "https://chat.openai.com/api/auth/error?error=OAuthSignin" or 'error' in url:
                self.debugger.log("You have been rate limited")
                raise Exception("You have been rate limited.")
            self.part_four(url=url)
        else:
            self.debugger.log("Error in part three")
            self.debugger.log("Response: ", end="")
            self.debugger.log(response.text)
            self.debugger.log("Status code: ", end="")
            self.debugger.log(response.status_code)
            self.debugger.log(response.headers)
            raise Exception("Unknown error")

    def part_four(self, url: str) -> None:
        """
        We make a GET request to url
        :param url:
        :return:
        """
        self.debugger.log("Beginning part four")
        headers = {
            "Host": "auth0.openai.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Connection": "keep-alive",
            # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
            # "Version/16.1 Safari/605.1.15",
            "User-Agent": USER_AGENT,
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://chat.openai.com/",
        }
        response = self.session.get(
            url=url, headers=headers)
        if response.status_code == 302:
            try:
                state = re.findall(r"state=(.*)", response.text)[0]
                state = state.split('"')[0]
                self.part_five(state=state)
            except IndexError as exc:
                self.debugger.log("Error in part four")
                self.debugger.log("Status code: ", end="")
                self.debugger.log(response.status_code)
                self.debugger.log("Rate limit hit")
                self.debugger.log("Response: " + str(response.text))
                raise Exception("Rate limit hit") from exc
        else:
            self.debugger.log("Error in part four")
            self.debugger.log("Response: ", end="")
            self.debugger.log(response.text)
            self.debugger.log("Status code: ", end="")
            self.debugger.log(response.status_code)
            self.debugger.log("Wrong response code")
            raise Exception("Unknown error")

    def part_five(self, state: str) -> None:
        """
        We use the state to get the login page & check for a captcha
        """
        self.debugger.log("Beginning part five")
        url = f"https://auth0.openai.com/u/login/identifier?state={state}"

        headers = {
            "Host": "auth0.openai.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Connection": "keep-alive",
            # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
            # "Version/16.1 Safari/605.1.15",
            "User-Agent": USER_AGENT,
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://chat.openai.com/",
        }
        response = self.session.get(url, headers=headers)
        if response.status_code == 200:
            captcha_code = None
            if re.search(r'<img[^>]+alt="captcha"[^>]+>', response.text):
                self.debugger.log("Captcha detected")
                if self.use_capcha == False:
                    self.debugger.log("Captcha detected but not used")
                    raise Exception("Captcha detected but not used")
                pattern = re.compile(
                    r'<img[^>]+alt="captcha"[^>]+src="(.+?)"[^>]+>')
                match = pattern.search(response.text)
                if match and self.captcha_solver:
                    captcha = match.group(1)
                    self.debugger.log("Captcha extracted")
                    # Save captcha (in JavaScript src format) to real svg file
                    captcha = captcha.replace("data:image/svg+xml;base64,", "")
                    # Convert base64 to svg
                    captcha = base64.b64decode(captcha)
                    captcha = captcha.decode("utf-8")
                    # Save captcha to file
                    captcha_code = self.captcha_solver.solve_captcha(
                        captcha)
                else:
                    self.debugger.log("Failed to find captcha")
                    raise ValueError("Captcha detected")
            self.part_six(state=state, captcha=captcha_code)
        else:
            self.debugger.log("Error in part five")
            self.debugger.log("Response: ", end="")
            self.debugger.log(response.text)
            self.debugger.log("Status code: ", end="")
            self.debugger.log(response.status_code)
            raise ValueError("Invalid response code")

    def part_six(self, state: str, captcha: str or None) -> None:
        """
        We make a POST request to the login page with the captcha, email
        :param state:
        :param captcha:
        :return:
        """
        self.debugger.log("Beginning part six")
        url = f"https://auth0.openai.com/u/login/identifier?state={state}"
        email_url_encoded = self.url_encode(self.email_address)
        payload = (
            f"state={state}&username={email_url_encoded}&captcha={captcha}&js-available=true&webauthn-available"
            f"=true&is-brave=false&webauthn-platform-available=true&action=default "
        )

        if captcha is None:
            payload = (
                f"state={state}&username={email_url_encoded}&js-available=false&webauthn-available=true&is"
                f"-brave=false&webauthn-platform-available=true&action=default "
            )

        headers = {
            "Host": "auth0.openai.com",
            "Origin": "https://auth0.openai.com",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
            # "Version/16.1 Safari/605.1.15",
            "User-Agent": USER_AGENT,
            "Referer": f"https://auth0.openai.com/u/login/identifier?state={state}",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = self.session.post(
            url, headers=headers, data=payload)
        if response.status_code == 302:
            self.part_seven(state=state)
        else:
            self.debugger.log("Error in part six")
            self.debugger.log("Response: ", end="")
            self.debugger.log(response.text)
            self.debugger.log("Status code: ", end="")
            self.debugger.log(response.status_code)
            raise Exception("Unknown error")

    def part_seven(self, state: str) -> None:
        """
        We enter the password
        :param state:
        :return:
        """
        url = f"https://auth0.openai.com/u/login/password?state={state}"
        self.debugger.log("Beginning part seven")
        email_url_encoded = self.url_encode(self.email_address)
        password_url_encoded = self.url_encode(self.password)
        payload = f"state={state}&username={email_url_encoded}&password={password_url_encoded}&action=default"
        headers = {
            "Host": "auth0.openai.com",
            "Origin": "https://auth0.openai.com",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
            # "Version/16.1 Safari/605.1.15",
            "User-Agent": USER_AGENT,
            "Referer": f"https://auth0.openai.com/u/login/password?state={state}",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        try:
            response = self.session.post(
                url, headers=headers, data=payload)
            self.debugger.log("Request went through")
        except Exception as exc:
            self.debugger.log("Error in part seven")
            self.debugger.log("Exception: ", end="")
            self.debugger.log(exc)
            raise Exception("Could not get response") from exc
        if response.status_code == 302:
            self.debugger.log("Response code is 302")
            try:
                new_state = re.findall(r"state=(.*)", response.text)[0]
                new_state = new_state.split('"')[0]
                self.debugger.log("New state found")
                self.part_eight(old_state=state, new_state=new_state)
            except Exception as exc:
                self.debugger.log("Error in part seven")
                self.debugger.log("Exception: ", end="")
                self.debugger.log(exc)
                raise Exception("State not found") from exc
        elif response.status_code == 400:
            self.debugger.log("Error in part seven")
            self.debugger.log("Status code: ", end="")
            self.debugger.log(response.status_code)
            raise Exception("Wrong email or password")
        else:
            self.debugger.log("Error in part seven")
            self.debugger.log("Status code: ", end="")
            self.debugger.log(response.status_code)
            raise Exception("Wrong status code")

    def part_eight(self, old_state: str, new_state) -> None:
        self.debugger.log("Beginning part eight")
        url = f"https://auth0.openai.com/authorize/resume?state={new_state}"
        headers = {
            "Host": "auth0.openai.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Connection": "keep-alive",
            # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
            # "Version/16.1 Safari/605.1.15",
            "User-Agent": USER_AGENT,
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Referer": f"https://auth0.openai.com/u/login/password?state={old_state}",
        }
        response = self.session.get(
            url, headers=headers, allow_redirects=True)
        is_200 = response.status_code == 200
        if is_200:
            # Access Token
            access_token = re.findall(
                r"accessToken\":\"(.*)\"",
                response.text,
            )
            if access_token:
                try:
                    access_token = access_token[0]
                    access_token = access_token.split('"')[0]
                except Exception as e:
                    self.debugger.log("Error in part eight")
                    self.debugger.log("Response: ", end="")
                    self.debugger.log(response.text)
                    self.debugger.log("Status code: ", end="")
                    self.debugger.log(response.status_code)
                    raise e
            else:
                self.debugger.log("Error in part eight")
                self.debugger.log("Response: ", end="")
                self.debugger.log(response.text)
                self.debugger.log("Status code: ", end="")
                self.debugger.log(response.status_code)
                raise Exception("Auth0 did not issue an access token")
            self.part_nine()
        else:
            self.debugger.log("Incorrect response code in part eight")
            raise Exception("Incorrect response code")

    def save_access_token(self, access_token: str) -> None:
        """
        Save access_token and an hour from now on ./Classes/auth.json
        :param access_token:
        :return:
        """
        self.access_token = access_token

    def part_nine(self) -> bool:
        self.debugger.log("Beginning part nine")
        url = "https://chat.openai.com/api/auth/session"
        headers = {
            "Host": "ask.openai.com",
            "Connection": "keep-alive",
            "If-None-Match": '"bwc9mymkdm2"',
            "Accept": "*/*",
            # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
            # "Version/16.1 Safari/605.1.15",
            "User-Agent": USER_AGENT,
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Referer": "https://chat.openai.com/chat",
            "Accept-Encoding": "gzip, deflate, br",
        }
        response = self.session.get(url, headers=headers)
        is_200 = response.status_code == 200
        if is_200:
            # Get session token
            self.session_token = response.cookies.get(
                "__Secure-next-auth.session-token",
            )
            if 'json' in response.headers['Content-Type']:
                json_response = response.json()
                access_token = json_response['accessToken']
                self.save_access_token(access_token=access_token)
                self.debugger.log("SUCCESS")
                return True
            else:
                self.debugger.log(
                    "Please try again with a proxy (or use a new proxy if you are using one)")
        else:
            self.debugger.log(
                "Please try again with a proxy (or use a new proxy if you are using one)")
        self.session_token = None
        self.debugger.log("Failed to get session token")
        raise Exception("Failed to get session token")


class CaptchaSolver:
    """
    Captcha solver
    """
    @staticmethod
    def solve_captcha(raw_svg):
        """
        Solves the captcha

        :param raw_svg: The raw SVG
        :type raw_svg: :obj:`str`

        :return: The solution
        :rtype: :obj:`str`
        """
        # Get the SVG
        svg = raw_svg
        # Save the SVG
        print("Saved captcha.svg")
        with open("captcha.svg", "w", encoding='utf-8') as f:
            f.write(svg)
        # Get input
        solution = input("Please solve the captcha: ")
        # Return the solution
        return solution


class AsyncChatbot:
    """
    Initialize the AsyncChatbot.

    See wiki for the configuration json:
    https://github.com/acheong08/ChatGPT/wiki/Setup

    :param config: The configuration json
    :type config: :obj:`json`

    :param conversation_id: The conversation ID
    :type conversation_id: :obj:`str`, optional

    :param parent_id: The parent ID
    :type parent_id: :obj:`str`, optional

    :param debug: Whether to enable debug mode
    :type debug: :obj:`bool`, optional

    :param refresh: Whether to refresh the session
    :type refresh: :obj:`bool`, optional

    :param request_timeout: The network request timeout seconds
    :type request_timeout: :obj:`int`, optional

    :param base_url: The base url to chat.openai.com backend server,
        useful when set up a reverse proxy to avoid network issue.
    :type base_url: :obj:`str`, optional

    :return: The Chatbot object
    :rtype: :obj:`Chatbot`
    """
    config: json
    conversation_id: str
    parent_id: str
    base_url: str
    headers: dict
    conversation_id_prev_queue: List
    parent_id_prev_queue: List
    request_timeout: int
    captcha_solver: any

    def __init__(self, config, conversation_id=None, parent_id=None, debugger=None, request_timeout=100,
                 captcha_solver=CaptchaSolver(), base_url="https://chat.openai.com/", max_rollbacks=20):
        self.debugger = debugger
        # self.debug = debug
        self.config = config
        self.conversation_id = conversation_id
        self.parent_id = parent_id if parent_id else generate_uuid()
        self.base_url = base_url
        self.request_timeout = request_timeout
        self.captcha_solver = captcha_solver
        self.max_rollbacks = max_rollbacks
        self.conversation_id_prev_queue = []
        self.parent_id_prev_queue = []
        self.config["accept_language"] = 'en-US,en' if "accept_language" not in self.config.keys(
        ) else self.config["accept_language"]
        
        # self.config["user_agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36" if "user_agent" not in self.config.keys(
        # ) else self.config["user_agent"]

        self.config["user_agent"] = USER_AGENT if "user_agent" not in self.config.keys(
        ) else self.config["user_agent"]

        self.headers = {
            "Accept": "text/event-stream",
            "Authorization": "Bearer ",
            "Content-Type": "application/json",
            "User-Agent": self.config["user_agent"],
            "X-Openai-Assistant-App-Id": "",
            "Connection": "close",
            "Accept-Language": self.config["accept_language"]+";q=0.9",
            "Referer": "https://chat.openai.com/chat",
        }
        self.refresh_session()

    def reset_chat(self) -> None:
        """
        Reset the conversation ID and parent ID.

        :return: None
        """
        self.conversation_id = None
        self.parent_id = generate_uuid()

    def __refresh_headers(self) -> None:
        """
        Refresh the headers -- Internal use only

        :return: None
        """
        if not self.config.get("Authorization"):
            self.config["Authorization"] = ""
        self.headers["Authorization"] = "Bearer " + \
            self.config["Authorization"]
        self.headers["User-Agent"] = self.config["user_agent"]

    async def __get_chat_stream(self, data) -> None:
        """
        Generator for the chat stream -- Internal use only

        :param data: The data to send
        :type data: :obj:`dict`

        :return: None
        """
        s = httpx.AsyncClient()
        # Set cloudflare cookies
        if "cf_clearance" in self.config:
            s.cookies.set(
                "cf_clearance",
                self.config["cf_clearance"],
            )
        async with s.stream(
            'POST',
            self.base_url + "backend-api/conversation",
            headers=self.headers,
            data=json.dumps(data),
            timeout=self.request_timeout,
        ) as response:
            async for line in response.aiter_lines():
                try:
                    line = line[:-1]
                    if line == "" or line == "data: [DONE]":
                        continue
                    line = line[6:]
                    line = json.loads(line)
                    if len(line["message"]["content"]["parts"]) == 0:
                        continue
                    message = line["message"]["content"]["parts"][0]
                    self.conversation_id = line["conversation_id"]
                    self.parent_id = line["message"]["id"]
                    yield {
                        "message": message,
                        "conversation_id": self.conversation_id,
                        "parent_id": self.parent_id,
                    }
                except Exception as exc:
                    self.debugger.log(
                        f"Error when handling response, got values [{line}]")
                    raise Exception(
                        f"Error when handling response, got values [{line}]") from exc

    async def __get_chat_text(self, data) -> dict:
        """
        Get the chat response as text -- Internal use only
        :param data: The data to send
        :type data: :obj:`dict`
        :return: The chat response
        :rtype: :obj:`dict`
        """
        # Create request session
        async with httpx.AsyncClient() as s:
            # set headers
            s.headers = self.headers
            # Set cloudflare cookies
            if "cf_clearance" in self.config:
                s.cookies.set(
                    "cf_clearance",
                    self.config["cf_clearance"],
                )
            # Set proxies
            if self.config.get("proxy", "") != "":
                s.proxies = {
                    "http": self.config["proxy"],
                    "https": self.config["proxy"],
                }
            response = await s.post(
                self.base_url + "backend-api/conversation",
                data=json.dumps(data),
                timeout=self.request_timeout,
            )
            try:
                response = response.text.splitlines()[-4]
                response = response[6:]
            except Exception as exc:
                self.debugger.log("Incorrect response from OpenAI API")
                raise Exception("Incorrect response from OpenAI API") from exc
            # Check if it is JSON
            if response.startswith("{"):
                response = json.loads(response)
                self.parent_id = response["message"]["id"]
                self.conversation_id = response["conversation_id"]
                message = response["message"]["content"]["parts"][0]
                return {
                    "message": message,
                    "conversation_id": self.conversation_id,
                    "parent_id": self.parent_id,
                }
            else:
                return None

    async def get_chat_response(self, prompt: str, output="text", conversation_id=None, parent_id=None) -> dict or None:
        """
        Get the chat response.

        :param prompt: The message sent to the chatbot
        :type prompt: :obj:`str`

        :param output: The output type `text` or `stream`
        :type output: :obj:`str`, optional

        :return: The chat response `{"message": "Returned messages", "conversation_id": "conversation ID", "parent_id": "parent ID"}` or None
        :rtype: :obj:`dict` or :obj:`None`
        """
        self.refresh_session(running_in_async=True)
        data = {
            "action": "next",
            "messages": [
                {
                    "id": str(generate_uuid()),
                    "role": "user",
                    "content": {"content_type": "text", "parts": [prompt]},
                },
            ],
            "conversation_id": conversation_id or self.conversation_id,
            "parent_message_id": parent_id or self.parent_id,
            "model": "text-davinci-002-render",
        }
        self.conversation_id_prev_queue.append(
            data["conversation_id"])  # for rollback
        self.parent_id_prev_queue.append(data["parent_message_id"])
        while len(self.conversation_id_prev_queue) > self.max_rollbacks:  # LRU, remove oldest
            self.conversation_id_prev_queue.pop(0)
        while len(self.parent_id_prev_queue) > self.max_rollbacks:
            self.parent_id_prev_queue.pop(0)
        if output == "text":
            return await self.__get_chat_text(data)
        elif output == "stream":
            return self.__get_chat_stream(data)
        else:
            raise ValueError("Output must be either 'text' or 'stream'")

    def rollback_conversation(self, num=1) -> None:
        """
        Rollback the conversation.
        :param num: The number of messages to rollback
        :return: None
        """
        for i in range(num):
            self.conversation_id = self.conversation_id_prev_queue.pop()
            self.parent_id = self.parent_id_prev_queue.pop()

    async def refresh_session(self, running_in_async=False) -> None:
        """
        Refresh the session.

        :return: None
        """
        if running_in_async:
            nest_asyncio.apply()
        # Either session_token, email and password or Authorization is required
        if not self.config.get("cf_clearance") or not self.config.get("session_token"):
            await self.__get_cf_cookies()
        if self.config.get("session_token") and self.config.get("cf_clearance"):
            s = httpx.Client()
            if self.config.get("proxy"):
                s.proxies = {
                    "http": self.config["proxy"],
                    "https": self.config["proxy"],
                }
            # Set cookies
            s.cookies.set(
                "__Secure-next-auth.session-token",
                self.config["session_token"],
            )

            s.cookies.set(
                "cf_clearance",
                self.config["cf_clearance"],
            )
            # s.cookies.set("__Secure-next-auth.csrf-token", self.config['csrf_token'])
            response = s.get(
                self.base_url + "api/auth/session",
                headers={
                    "User-Agent": self.config["user_agent"],
                },
            )
            # Check the response code
            if response.status_code != 200:
                if response.status_code == 403:
                    await self.__get_cf_cookies()
                    self.refresh_session(running_in_async=running_in_async)
                    return
                else:
                    self.debugger.log(
                        f"Invalid status code: {response.status_code}")
                    raise Exception("Wrong response code")
            # Try to get new session token and Authorization
            try:
                if 'error' in response.json():
                    self.debugger.log("Error in response JSON")
                    self.debugger.log(response.json()['error'])
                    raise Exception
                self.config["session_token"] = response.cookies.get(
                    "__Secure-next-auth.session-token",
                )
                self.config["Authorization"] = response.json()["accessToken"]
                self.__refresh_headers()
            # If it fails, try to login with email and password to get tokens
            except Exception as exc:
                # Check if response JSON is empty
                if response.json() == {}:
                    self.debugger.log("Empty response")
                    self.debugger.log("Probably invalid session token")
                # Check if ['detail']['code'] == 'token_expired' in response JSON
                # First check if detail is in response JSON
                elif 'detail' in response.json():
                    # Check if code is in response JSON
                    if 'code' in response.json()['detail']:
                        # Check if code is token_expired
                        if response.json()['detail']['code'] == 'token_expired':
                            self.debugger.log("Token expired")
                raise Exception("Failed to refresh session") from exc
            return
        else:
            self.debugger.log(
                "No session_token, email and password or Authorization provided")
            raise ValueError(
                "No session_token, email and password or Authorization provided")

    async def __get_cf_cookies(self) -> None:
        """
        Get cloudflare cookies.

        :return: None
        """
        async with async_playwright() as p:
            # browser = await p.chromium.launch(headless=False)
            # browser = await p.webkit.launch(headless=False)
            browser = await p.firefox.launch(headless=False)
            page = await browser.new_page()
            if 'session_token' in self.config:
                await async_stealth(page, pure=False)
            else:
                await async_stealth(page, pure=False)
            await page.goto('https://chat.openai.com/')
            page_wait_for_url = 'https://chat.openai.com/chat' if not self.config.get(
                'session_token') else None
            res = await async_cf_retry(
                page, wait_for_url=page_wait_for_url)
            if res:
                cookies = await page.context.cookies()
                for cookie in cookies:
                    if cookie.get('name') == 'cf_clearance':
                        cf_clearance_value = cookie.get('value')
                        self.debugger.log(cf_clearance_value)
                    elif cookie.get('name') == '__Secure-next-auth.session-token':
                        self.config['session_token'] = cookie.get('value')
                ua = await page.evaluate('() => {return navigator.userAgent}')
                self.debugger.log(ua)
            else:
                self.debugger.log("cf challenge fail")
                raise Exception("cf challenge fail")
            await browser.close()
            del browser
            self.config['cf_clearance'] = cf_clearance_value
            self.config['user_agent'] = ua

    def send_feedback(
        self,
        is_good: bool,
        is_harmful=False,
        is_not_true=False,
        is_not_helpful=False,
        description=None,
    ):
        from dataclasses import dataclass

        @ dataclass
        class ChatGPTTags:
            Harmful = "harmful"
            NotTrue = "false"
            NotHelpful = "not-helpful"

        url = self.base_url + "backend-api/conversation/message_feedback"

        data = {
            "conversation_id": self.conversation_id,
            "message_id": self.parent_id,
            "rating": "thumbsUp" if is_good else "thumbsDown",
        }

        if not is_good:
            tags = list()
            if is_harmful:
                tags.append(ChatGPTTags.Harmful)
            if is_not_true:
                tags.append(ChatGPTTags.NotTrue)
            if is_not_helpful:
                tags.append(ChatGPTTags.NotHelpful)
            data["tags"] = tags

        if description is not None:
            data["text"] = description

        response = httpx.post(
            url,
            headers=self.headers,
            data=json.dumps(data),
            timeout=self.request_timeout,
        )

        return response


class Chatbot(AsyncChatbot):
    """
    Initialize the Chatbot.

    See wiki for the configuration json:
    https://github.com/acheong08/ChatGPT/wiki/Setup

    :param config: The configuration json
    :type config: :obj:`json`

    :param conversation_id: The conversation ID
    :type conversation_id: :obj:`str`, optional

    :param parent_id: The parent ID
    :type parent_id: :obj:`str`, optional

    :param debug: Whether to enable debug mode
    :type debug: :obj:`bool`, optional

    :param refresh: Whether to refresh the session
    :type refresh: :obj:`bool`, optional

    :param request_timeout: The network request timeout seconds
    :type request_timeout: :obj:`int`, optional

    :param base_url: The base url to chat.openai.com backend server,
        useful when set up a reverse proxy to avoid network issue.
    :type base_url: :obj:`str`, optional

    :return: The Chatbot object
    :rtype: :obj:`Chatbot`
    """

    def refresh_session(self, running_in_async=False) -> None:
        try:
            # Check if running in nest use of asyncio.run()
            asyncio.run(self.async_func_for_check())
        except RuntimeError:
            self.debugger.log("detect nest use of asyncio")
            nest_asyncio.apply()
        return asyncio.run(super().refresh_session(running_in_async))

    def __get_chat_stream(self, data) -> None:
        """
        Generator for the chat stream -- Internal use only

        :param data: The data to send
        :type data: :obj:`dict`

        :return: None
        """
        s = httpx.Client()
        # Set cloudflare cookies
        if "cf_clearance" in self.config:
            s.cookies.set(
                "cf_clearance",
                self.config["cf_clearance"],
            )
        with s.stream(
            'POST',
            self.base_url + "backend-api/conversation",
            headers=self.headers,
            data=json.dumps(data),
            timeout=self.request_timeout,
        ) as response:
            for line in response.iter_lines():
                try:
                    line = line[:-1]
                    if line == "" or line == "data: [DONE]":
                        continue
                    line = line[6:]
                    line = json.loads(line)
                    if len(line["message"]["content"]["parts"]) == 0:
                        continue
                    message = line["message"]["content"]["parts"][0]
                    self.conversation_id = line["conversation_id"]
                    self.parent_id = line["message"]["id"]
                    yield {
                        "message": message,
                        "conversation_id": self.conversation_id,
                        "parent_id": self.parent_id,
                    }
                except Exception as exc:
                    self.debugger.log(
                        f"Error when handling response, got values [{line}]")
                    raise Exception(
                        f"Error when handling response, got values [{line}]") from exc

    def get_chat_response(self, prompt: str, output="text", conversation_id=None, parent_id=None) -> dict or None:
        """
        Get the chat response.

        :param prompt: The message sent to the chatbot
        :type prompt: :obj:`str`

        :param output: The output type `text` or `stream`
        :type output: :obj:`str`, optional

        :return: The chat response `{"message": "Returned messages", "conversation_id": "conversation ID", "parent_id": "parent ID"}` or None
        :rtype: :obj:`dict` or :obj:`None`
        """
        try:
            # Check if running in nest use of asyncio.run()
            asyncio.run(self.async_func_for_check())
        except RuntimeError:
            self.debugger.log("detect nest use of asyncio")
            nest_asyncio.apply()
        self.refresh_session()
        if output == "text":
            coroutine_object = super().get_chat_response(
                prompt, output, conversation_id, parent_id)
            return asyncio.run(coroutine_object)

        if output == "stream":
            data = {
                "action": "next",
                "messages": [
                    {
                        "id": str(generate_uuid()),
                        "role": "user",
                        "content": {"content_type": "text", "parts": [prompt]},
                    },
                ],
                "conversation_id": conversation_id or self.conversation_id,
                "parent_message_id": parent_id or self.parent_id,
                "model": "text-davinci-002-render",
            }
            self.conversation_id_prev_queue.append(
                data["conversation_id"])  # for rollback
            self.parent_id_prev_queue.append(data["parent_message_id"])
            return self.__get_chat_stream(data)

    async def async_func_for_check(self):
        pass


def get_input(printer, prompt):
    # prompt for input
    lines = []
    printer(prompt, end="")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    # Join the lines, separated by newlines, and print the result
    user_input = "\n".join(lines)
    # printer(user_input)
    return user_input


def verify_config(config):
    """
    Verifies the config

    :param config: The config
    :type config: :obj:`dict`
    """
    # Check if the config is empty
    if 'email' in config or 'password' in config:
        print("Email and passwords are no longer supported")


def configure(default_config="config.json"):
    try:
        config_files = [default_config]
        # xdg_config_home = getenv("XDG_CONFIG_HOME")
        # if xdg_config_home:
        #     config_files.append(f"{xdg_config_home}/revChatGPT/config.json")
        user_home = getenv("HOME")
        if user_home:
            config_files.append(f"{user_home}/.config/sidoarjo-schnell/config.json")

        config_file = next((f for f in config_files if exists(f)), None)
        if config_file:
            with open(config_file, encoding="utf-8") as f:
                config = json.load(f)
        else:
            print("No config file found.")
            config = {}
        if "--debug" in argv:
            print("Debugging enabled.")
            debug = True
        else:
            debug = False
        verify_config(config)
        # chatGPT_main(config, debug)
    except KeyboardInterrupt:
        print("\nGoodbye!")
        exit()
    except Exception as exc:
        print("Something went wrong! Please run with --debug to see the error.")
        print(exc)
        exit()
    return config

# self.filename = 'gpt-chat.txt'
# self.foldername = 'data/gpt-data'

# def write(self, content):
#     file_write_timestamped_under_rootdir(self.filename, content, self.foldername, write_mode='a+')

def get_response_stream(chatbot, printer, prompt):
    lines_printed = 0
    try:
        printer("== GPT: \n")
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
        printer(formatted_parts[lines_printed])
    except Exception as exc:
        printer("Response not in correct format!")
        printer(exc)


def get_response_text(chatbot, printer, prompt):
    try:
        printer("== GPT: \n")
        message = chatbot.get_chat_response(prompt)
        printer(message["message"])
    except Exception as exc:
        printer("Something went wrong!")
        printer(exc)


def create_chatbot(config='config.json', debug=True):
    return Chatbot(configure(config), debugger=Debugger(debug))


# perlu simpan semua history
# C:\Users\usef\work\sidoarjo\data\gpt-data\README.md
def demo(printer=print, stream_mode = True, debug = True):
    config = configure()
    # text_mode = True  # text vs stream
    # stream_mode = False    
    # chatbot = Chatbot(config, debugger=Debugger(debug), captcha_solver=CaptchaSolver())
    chatbot = Chatbot(config, debugger=Debugger(debug))

    while True:
        prompt = get_input(printer, "\nYou:\n")
        if stream_mode:
            lines_printed = 0
            try:
                printer("Chatbot: ")
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
                printer(formatted_parts[lines_printed])
            except Exception as exc:
                printer("Response not in correct format!")
                printer(exc)
                continue
        else:
            try:
                printer("Chatbot: ")
                message = chatbot.get_chat_response(prompt)
                printer(message["message"])
            except Exception as exc:
                printer("Something went wrong!")
                printer(exc)
                continue


# GPT_QUERY = 'chatgpt mozilla firefox -visual -wasp'
GPT_QUERY = 'new chat mozilla firefox -visual'


def activate_chatgpt(code='https://chat.openai.com/chat'):
    from schnell.app.quick.launcher import launcher
    from .autoutils import maxactive
    indah4(f"activate_chatgpt, code {code}.", warna='yellow')
    launcher(code)
    indah4(f"maximizing active window.", warna='yellow')
    maxactive()


def activate_if_not_active_chatgpt(title_query=''):
    """
    step 1/3
    """
    from .autoutils import inwindowtitles
    if not title_query:
        title_query=GPT_QUERY
    indah4(f"activate_if_not_active_chatgpt, cari title \"{title_query}\".", warna='yellow')
    if not inwindowtitles(title_query)[0]:
        activate_chatgpt()


def refresh_chatgpt(title_query=''):
    """
    step 1/3
    """
    from schnell.autolang import process_language
    if not title_query:
        title_query=GPT_QUERY
    process_language(f"hot:({title_query})ctrl,r")


def send_prompt_chatgpt(prompt, title_query='', x=660,y=920):
    """
    step 2/3
    au:
    T:(chatgpt mozilla firefox -wasp -visual)~660,920|give me an example of depth-first search in python
    ~110,175 utk new thread

    T:(chatgpt mozilla firefox -wasp -visual)~110,175\~660,920|what is the best way to run typescript code from inside python code
    """
    from schnell.autolang import process_language
    if not title_query:
        title_query=GPT_QUERY
    process_language(f"T:({title_query})~{x},{y}|{prompt}", choose_shortest_for_multiple_windows=True)


def copy_answer_chatgpt(tinggi_untuk_select_copy=1/4):
    """
    step 3/3
    """
    from .autoutils import gpt_op1
    gpt_op1(tinggi_untuk_select_copy)


def process12_chatgpt(prompt, title_query='', x=660,y=920):
    """
    activate alamat chatgpt di browser jk tidak ada
    kirim prompt sesuai yg disend
    """
    from .autoutils import sleep
    if not title_query:
        title_query=GPT_QUERY
    print(f'process12_chatgpt, step #1/3')
    try:
        activate_if_not_active_chatgpt(title_query)
    except Exception as err:
        print(f"Gagal 'activate_if_not_active_chatgpt': {err}")
        input('Press... ')
    sleep(0.9)
    print(f'process12_chatgpt, step #2/3')
    try:
        send_prompt_chatgpt(prompt, title_query, x, y)
    except Exception as err:
        print(f"Gagal 'send_prompt_chatgpt': {err}")
        input('Press... ')
    print(f'process12_chatgpt, step #3/3')


def process123_chatgpt(prompt, title_query='', x=660,y=920, tinggi_untuk_select_copy=1/4):
    from .autoutils import sleep
    if not title_query:
        title_query=GPT_QUERY
    activate_if_not_active_chatgpt(title_query)
    sleep(0.9)
    send_prompt_chatgpt(prompt, title_query, x, y)
    sleep(0.3)
    copy_answer_chatgpt(tinggi_untuk_select_copy)
