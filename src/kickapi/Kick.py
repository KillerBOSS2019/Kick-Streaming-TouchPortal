import json
import re

from TouchPortalAPI.logger import Logger
from . Login import KickLogin


logger = Logger(__name__)

class Kick(KickLogin):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.isUserLoggedIn = False
        self.username = ""
        self.emote_table = {}

    def handleLogin(self):
        self.loadSession()
        
        if self.isLoggedin():
            self.isUserLoggedIn = True
        else:
            print("Logging in...")
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
    
    def getModerators(self):
        url = self.BASE_URL + "api/internal/v1/user/moderators"
        data = self.request(url, method="GET")
        return data
    
    def get_followed_user(self):
        url = self.BASE_URL + "api/v2/channels/followed?cursor=0"
        data = self.request(url, method="GET")
        return data
    
    def decode_emotes(self, message):
        pattern = r'\[emote:(\d+):(\w+)\]'
        matches = re.findall(pattern, message)

        for match in matches:
            message = message.replace(f"[emote:{match[0]}:{match[1]}]", f"[{match[1]}]")

        return message

    def encode_emotes(self, message):
        pattern = r'\[(\w+)\]'
        matches = re.findall(pattern, message)

        for match in matches:
            if match in self.emote_table:
                message = message.replace(f"[{match}]", f"[emote:{self.emote_table[match]}:{match}]")
        
        return message
        

    def update_emotes(self):
        url = self.BASE_URL + "emotes/" + self.username
        data = self.request(url, method="GET")

        if data.status_code == 200:
            jsonResponse = data.json()

            for emotes in jsonResponse:
                for emote in emotes["emotes"]:
                    self.emote_table[emote["name"]] = emote["id"]

        return self.emote_table
                    

    def sendMessage(self, message, chatroomid):
        url = self.BASE_URL + "api/v2/messages/send/" + str(chatroomid)
        response = self.request(url, data={"content": str(message), "type": "message"}, method="POST")
        return response
    
    def setModerator(self, username, add=True):
        if add:
            url = self.BASE_URL + "api/internal/v1/channels/" + self.username + "/community/moderators"
            data = {
                "username": username
            }
            response = self.request(url, data=data, method="POST")
        else:
            url = self.BASE_URL + "api/internal/v1/channels/" + \
                self.username + "/community/moderators/" + username
            
            response = self.request(url, method="DELETE")

        return response
    
    def follow(self, username, follow=True):
        if follow:
            url = self.BASE_URL + "api/v2/channels/" + username + "/follow"
            response = self.request(url, method="POST")
        else:
            url = self.BASE_URL + "api/v2/channels/" + username + "/follow"
            response = self.request(url, method="DELETE")
        
        return response
    
    def clearChat(self):
        url = self.BASE_URL + "api/v2/channels/" + self.username + "/chat-commands"
        data = {"command": "clear"}
        response = self.request(url, data=data, method="POST")
        return response
    
    def create_poll(self, question, options:list[str], duration:int, display_result_duration:int):
        url = self.BASE_URL + "api/v2/channels/" + self.username + "/polls"
        data = {
            "title": question,
            "options": options,
            "duration": duration,
            "result_display_duration": 15
        }
        header = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json"
        }
        self.request(url, data=json.dumps(data), method="POST", header=header)
    
    def vote_poll(self, poll_id):
        url = self.BASE_URL + "api/v2/channels/" + self.username + "/polls/vote"
        data = {"id": poll_id}
        response = self.request(url, data=data, method="POST")
        return response
    
    def end_poll(self):
        url = self.BASE_URL + "api/v2/channels/" + self.username + "/polls"
        response = self.request(url, method="DELETE")
        return response
    
    def ban(self, username:str, reason:str = None, duration:int = None, permanent:bool = False):
        url = self.BASE_URL + "api/v2/channels/" + self.username + "/bans"
        header = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json"
        }
        data = {
            "banned_username": username,
            "permanent": permanent
        }
        if reason:
            data["reason"] = reason
        if duration:
            data["duration"] = duration
        response = self.request(url, data=json.dumps(data), method="POST", header=header)
        return response
    
    def unban(self, username:str):
        url = self.BASE_URL + "api/v2/channels/" + self.username + "/bans/" + username
        response = self.request(url, method="DELETE")
        return response
    
    def host(self, username:str):
        url = self.BASE_URL + "api/v2/channels/" + self.username + "/chat-commands"
        data = {"command": "host", "parameter": username}
        header = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json"
        }
        response = self.request(url, data=data, method="POST", header=header)
        return response
    
    def set_stream_title(self):
        ...