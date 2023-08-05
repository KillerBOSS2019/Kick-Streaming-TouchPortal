from curl_cffi import requests
import websocket
import json
import re
import threading
import urllib.parse
from tkinter import *
import base64
from TouchPortalAPI.logger import Logger

logger = Logger(__name__)

class Kick2FA:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Kick 2FA")
        self.root.geometry("300x100")
        self.root.resizable(False, False)
        self.authCode = ""

        label = Label(self.root, text="Enter your 2FA code")
        label.pack()
        self.entry = Entry(self.root)
        self.entry.pack()
        button = Button(self.root, text="Submit", command=self.submit)
        button.pack()
    
    def submit(self):
        self.authCode = self.entry.get()
        self.root.destroy()

    def getPasscode(self):
        self.root.mainloop()
        return self.authCode
    
class KickSaveSession:
    def __init__(self) -> None:
        pass
    
    def _saveToken(self, headers):
        with open("token.txt", "w") as f:
            f.write(base64.b64encode(json.dumps(headers).encode("utf-8")).decode("utf-8"))

    def _loadToken(self) -> dict:
        try:
            with open("token.txt", "r") as f:
                file = f.read()
                return json.loads(base64.b64decode(file.encode("utf-8")).decode("utf-8"))
        except FileNotFoundError:
            return {}
    
    def save_cookie(self, cookie):
        token = self._loadToken()
        if token.get("Authorization", None):
            token["cookie"] = cookie
            self._saveToken(token)

class KickBase(KickSaveSession):
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        # "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "accept-language": "en-US",
        "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        "sec-ch-ua-mobile": "?0",
        "Authorization": "Bearer null",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "Cookie": "",
        "X-Xsrf-Token": ""
    })

    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.cookie_jar = {}

    def generate_cookie(self):
        if self.cookie_jar:
            cookie = "; ".join([f"{key}={value}" for key, value in self.cookie_jar.items()])
            return cookie
        return ""

    def set_headers(self, headers):
        if "set-cookie" in headers:
            pattern = r"([A-Za-z0-9_-]+)=([^;,\s]+)"
            matches = re.findall(pattern, headers["set-cookie"])
            for match in matches:
                cookie_name = match[0]
                cookie_value = match[1]
                if not cookie_name in ["expires", "path", "domain"] and len(cookie_value) > 10:
                    self.cookie_jar[cookie_name] = cookie_value
                    self.session.headers.update({"Cookie": self.generate_cookie()})
                self.save_cookie(self.cookie_jar)

            if "XSRF-TOKEN" in self.cookie_jar:
                self.session.headers.update({"X-XSRF-TOKEN": self.cookie_jar["XSRF-TOKEN"]})
    
    def is_success_status_code(self, status_code):
        return 200 <= status_code < 300

    def request(self, url, method="GET", data=None, header=None):
        print(f"Request --> method:{method} url:{url}")
        headers = self.session.headers
        if header:
            headers.update(header)
        if method == "GET":
            data = self.session.get(url, data=data, impersonate="chrome101", headers=headers)
        elif method == "POST":
            data = self.session.post(url, data=data, impersonate="chrome101", headers=headers)
        elif method == "PUT":
            data = self.session.put(url, data=data, impersonate="chrome101", headers=headers)

        if 200 <= data.status_code < 300:
            # Update header with response header
            self.set_headers(data.headers)
            print(f"Request <-- method:{method} url:{url} status_code:{data.status_code}")
        else:
            print(f"Request <-- method:{method} url:{url} status_code:{data.status_code} error:{data.text}")

        return data
    
class KickLogin(KickBase):
    BASE_URL = "https://kick.com/"

    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    def getTokenProvider(self):
        response = self.request(self.BASE_URL + "kick-token-provider", method="GET", header={"Content-Type": "application/x-www-form-urlencoded"})
        if response.status_code == 200:
            return response.json()
        return None
    
    def loadSession(self):
        token = self._loadToken()
        if token:
            self.session.headers.update({"Authorization": f'Bearer {token["Authorization"]}'})
            if token.get("cookie", None):
                self.cookie_jar = token["cookie"]
                self.session.headers.update({"Cookie": self.generate_cookie()})
                self.session.headers.update({"X-XSRF-TOKEN": self.cookie_jar.get("XSRF-TOKEN", "")})

    def isLoggedin(self):
        url = self.BASE_URL + "api/v1/user"
        data = self.request(url)
        return data.json()

    def login(self, authCode=None):
        tokenProvider = self.getTokenProvider()
        if not tokenProvider:
            print("Failed to get token provider.")
            return False

        data = {
            "email": self.email,
            "password": self.password,
            "isMobileRequest": True,
            tokenProvider["nameFieldName"]: "",
            tokenProvider["validFromFieldName"]: tokenProvider["encryptedValidFrom"],
        }

        if authCode:
            data["one_time_password"] = authCode

        url = self.BASE_URL + "mobile/login"
        response = self.request(url, method="POST", data=data)

        if response.status_code == 400 and (jsonResponse := response.json()):
            if jsonResponse["2fa_required"]:
                kick2fa = Kick2FA()
                authCode = kick2fa.getPasscode()

                return self.login(authCode=authCode)
        elif self.is_success_status_code(response.status_code):
            self.session.headers.update({"Authorization": f"Bearer {response.json()['token']}"})
            self._saveToken({"Authorization": response.json()['token']})
            return True
        
        return False
    
class KickWebSockets():
    WS_ADDRESS = "wss://ws-us2.pusher.com/app/eb1d5f283081a78b932c?protocol=7&client=js&version=7.6.0&flash=false"

    def __init__(self, onMessage, kick) -> None:
        self.ws = websocket.WebSocketApp(self.WS_ADDRESS, on_message=onMessage, on_close=self.on_close, on_error=self.onError)
        self.kick = kick

    def on_close(self, ws):
        print(f"Ws closed. {ws}")

    def send_ping(self):
        data = {
            "event": "pusher:ping",
            "data": {}
        }
        self.ws.send(json.dumps(data))

    def subscribe(self, event, socket_id=0, auth=""):
        data = {
            "event":
                "pusher:subscribe",
                "data": {"auth": auth, "channel": event}
        }
        self.ws.send(json.dumps(data))

    def unsubscribe(self, event):
        data = {
            "event":"pusher:unsubscribe",
            "data": {"channel": event}
        }
        self.ws.send(json.dumps(data))

    def onError(self, ws, error):
        logger.error(f"Error: {error}", exc_info=True)

    def run(self):
        self.ws.run_forever()

class Kick(KickLogin):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.isUserLoggedIn = False
        self.username = ""

    def handleLogin(self):
        self.loadSession()
        
        if self.isLoggedin():
            self.isUserLoggedIn = True
        else:
            if self.login():
                self.isUserLoggedIn = True

        return self.isUserLoggedIn
    
    def broadcasting_auth(self, socket_id, channel):
        url = self.BASE_URL + "broadcasting/auth"
        body = f"socket_id={socket_id}&channel_name={channel}"
        data = self.request(url, method="POST", data=body, header={"Content-Type": "application/x-www-form-urlencoded"})
        return data
    
    def setData(self):
        user_info = self.isLoggedin()
        if (user_info):
            self.username = user_info["username"]
    
    def getUserData(self):
        url = self.BASE_URL + "api/v2/channels/" + self.username
        data = self.request(url)
        return data

    def sendMessage(self, message):
        url = self.BASE_URL + "api/v2/messages/send/" + str(self.user_info["chatroom"]["id"])
        return self.request(url, data={"content": str(message), "type": "message"}, method="POST")