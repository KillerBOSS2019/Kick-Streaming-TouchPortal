from curl_cffi import requests
import websocket
import json
import re
import threading

class Kick:
    baseurl = "https://kick.com/"
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        # "accept": "application/json, text/plain, */*",
        "accept-language": "en-US",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Brave\";v=\"114\"",
        "sec-ch-ua-mobile": "?0",
        "Authorization": "Bearer null",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "Cookie": "",
        "X-Xsrf-Token": ""
    })

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.user_data = {}
        self.user_info = {}
        self.isLoggedin = False
        self.cookie = {}
        self.retry_login = True
        self.ws_address = "wss://ws-us2.pusher.com/app/eb1d5f283081a78b932c?protocol=7&client=js&version=7.6.0&flash=false"
        self.ws = None

    def generate_cookie(self):
        if self.cookie:
            cookie = "; ".join([f"{key}={value}" for key, value in self.cookie.items()])
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
                    self.cookie[cookie_name] = cookie_value
            
            self.session.headers.update({"Cookie": self.generate_cookie()})
            if "XSRF-TOKEN" in self.cookie:
                self.session.headers.update({"X-XSRF-TOKEN": self.cookie["XSRF-TOKEN"]})

    def request(self, url, method="GET", data=None):
        try:
            print(f"Request -> {method} {url} {data}")
            if method == "GET":
                data = self.session.get(url, data=data, impersonate="chrome101")
            elif method == "POST":
                data = self.session.post(url, data=data, impersonate="chrome101")
            elif method == "PUT":
                data = self.session.put(url, data=data, impersonate="chrome101")
            print(f"Request <-- {data.status_code} {data.text}")
        except Exception as e:
            print(f"Something went wrong in request with url:{url} method:{method} data:{data} error:{e}")
            return None
        
        self.set_headers(data.headers)
        # print(data.headers)
            # print(self.session.headers)

        return data
    
    def _getToken(self):
        url = self.baseurl + "kick-token-provider"
        data = self.request(url)
        return data
    
    def _saveToken(self, headers):
        with open("token.json", "w") as f:
            json.dump(headers, f)

    def _loadToken(self):
        try:
            with open("token.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return None
        
    def save_cookie(self):
        token = self._loadToken()
        if token.get("Authorization", None):
            token["cookie"] = self.cookie
            self._saveToken(token)
            
    def _requestLogin(self):
        token = self._getToken().json()
        data = {
            "email": self.email,
            "password": self.password,
            "isMobileRequest": True,
            token["nameFieldName"]: "",
            token["validFromFieldName"]: token["encryptedValidFrom"],
        }
        url = self.baseurl + "mobile/login"
        data = self.request(url, data=data, method="POST")
        
        return data

    def login(self):
        token = self._loadToken()
        is_login_requested = False

        if not token or not token.get("Authorization", None):
            is_login_requested = True
            login = self._requestLogin()
            if 200 <= login.status_code <= 299:
                token = {"Authorization": login.json()["token"]}
                self._saveToken(token)
                self.save_cookie()
            else:
                print(f"Incorrect login credentials")
                self.retry_login = False

        if token:
            self.session.headers["Authorization"] = "Bearer " + token["Authorization"]
            if not is_login_requested:
                self.cookie = token.get("cookie", {})
                self.session.headers["Cookie"] = self.generate_cookie()
                if "XSRF-TOKEN" in self.cookie:
                    self.session.headers["X-XSRF-TOKEN"] = token["cookie"]["XSRF-TOKEN"]
                

        user = self.getUser().json()

        if user:
            self.isLoggedin = True
            self.user_data = user
            self.user_info = self.getUserInfo().json()
            return True

        if self.retry_login:
            self.session.headers["Cookie"] = ""
            self.session.headers["X-XSRF-TOKEN"] = ""
            self.retry_login = False
            self._saveToken({})
            self.login()
        else:
            return False
    
    def getUser(self):
        url = self.baseurl + "api/v1/user"
        data = self.session.get(url, impersonate="chrome101")
        return data

    def getUserInfo(self):
        url = self.baseurl + "api/v2/channels/" + self.user_data.get("username")
        data = self.request(url)
        return data
    
    def broadcasting_auth(self, socket_id, channel):
        url = self.baseurl + "broadcasting/auth"
        body = f"socket_id={socket_id}&channel_name={channel}"
        data = self.request(url, method="POST", data=body)
        return data
    
    def send_ping(self):
        data = {
            "event": "pusher:ping",
            "data": {}
        }
        self.ws.send(json.dumps(data))

    def subscribe_to_chatroom(self):
        data = {
            "event": 
                "pusher:subscribe",
                "data": {
                    "auth": "",
                    "channel": f"chatrooms.{self.user_info['chatroom']['id']}.v2"
                }
            }
        self.ws.send(json.dumps(data))

    def subscribe_to_channel(self):
        data = {
            "event": 
                "pusher:subscribe",
                "data": {
                    "auth": "",
                    "channel": f"channel.{self.user_info['chatroom']['channel_id']}"
                }
            }
        self.ws.send(json.dumps(data))

    def subscribe(self, socket_id, event):
        auth = self.broadcasting_auth(socket_id, event)
        auth = auth.json()
        data = {
            "event":
                "pusher:subscribe",
                "data": {"channel": event, "auth": auth["auth"]}
        }
        self.ws.send(json.dumps(data))

    def unsubscribe(self, event):
        data = {
            "event":"pusher:unsubscribe",
            "data": {"channel": event}
        }
        self.ws.send(json.dumps(data))
    
    def getMessages(self):
        url = self.baseurl + "api/v2/channels/" + str(self.chatroom_id) + "/messages"
        return self.session.get(url)
    
    def sendMessage(self, message):
        url = self.baseurl + "api/v2/messages/send/" + str(self.user_info["chatroom"]["id"])
        return self.request(url, data={"content": str(message), "type": "message"}, method="POST")
    
    def enable_slowmode(self, option, interval):
        url = self.baseurl + "api/v2/channels/" + self.user_data.get("username") + "/chatroom"
        data = {"slow_mode": option}
        if option:
            data["message_interval"] = interval
        return self.request(url, data=data, method="PUT")
    
    def enable_followersmode(self, option, duration):
        url = self.baseurl + "api/v2/channels/" + self.user_data.get("username") + "/chatroom"
        data = {"followers_only": option}
        if option:
            data["following_min_duration"] = duration
        return self.request(url, data=data, method="PUT")
    
    def emote_only(self, option):
        url = self.baseurl + "api/v2/channels/" + self.user_data.get("username") + "/chatroom"
        data = {"emote_only": option}
        return self.request(url, data=data, method="PUT")
    
    def adv_antibot(self, option):
        url = self.baseurl + "api/v2/channels/" + self.user_data.get("username") + "/chatroom"
        data = {"advanced_bot_protection": option}
        return self.request(url, data=data, method="PUT")

    def connect_ws(self, on_message):
        self.ws = websocket.WebSocketApp(self.ws_address, on_message=on_message)
        threading.Thread(target=self.ws.run_forever).start()
        
# kick = Kick("email", "pass")
# kick.login()
# print(kick.user_info)
# kick.connect_ws()