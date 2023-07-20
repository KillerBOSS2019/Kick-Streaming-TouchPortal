from kick import Kick
from Plugin import Plugin
import json

class KickTP(Plugin):
    __version__ = 100

    PLUGIN_ID = "com.github.killerboss2019.kicktp"

    TP_PLUGIN_INFO = {
        "sdk": 6,
        "version": __version__,
        "name": "Kick-Streaming",
        "id": PLUGIN_ID,
        "plugin_start_cmd_windows": "%TP_PLUGIN_FOLDER%kick\\tp_kick.exe",
        "configuration": {
            "colorDark": "#15843e",
            "colorLight": "#1ca950"
        }
    }

    TP_PLUGIN_SETTINGS = {}

    TP_PLUGIN_CATEGORIES = {
        "main": {
            "id": PLUGIN_ID + ".main",
            "name": "Kick",
            "imagepath": "%TP_PLUGIN_FOLDER%kick\\kick.png"
        },
        "chat": {
            "id": PLUGIN_ID + ".chat",
            "name": "Kick - Chat",
            "imagepath": "%TP_PLUGIN_FOLDER%kick\\kick_chat.png"
        }
    }

    TP_PLUGIN_CONNECTORS = {}

    TP_PLUGIN_ACTIONS = {}

    TP_PLUGIN_STATES = {
        "profile_name": {
            "id": PLUGIN_ID + ".state.profile_name",
            "type": "text",
            "desc": "Kick Profile Name",
            "default": "",
            "parentGroup": "Kick Profile",
            "category": "main"
        },
        "profile_follower_count": {
            "id": PLUGIN_ID + ".state.profile_follower_count",
            "type": "text",
            "desc": "Kick Profile Follower Count",
            "default": "",
            "parentGroup": "Kick Profile",
            "category": "main"
        },
        "profile_bio": {
            "id": PLUGIN_ID + ".state.profile_bio",
            "type": "text",
            "desc": "Kick Profile Bio",
            "default": "",
            "parentGroup": "Kick Profile",
            "category": "main"
        },
        "streaming_status": {
            "id": PLUGIN_ID + ".state.streaming_status",
            "type": "text",
            "desc": "Kick is Live",
            "default": "False",
            "parentGroup": "Kick Streaming",
            "category": "main"
        },
        "latest_message_content": {
            "id": PLUGIN_ID + ".state.latest_message_content",
            "type": "text",
            "desc": "Kick Latest Message",
            "default": "",
            "parentGroup": "Kick Streaming",
            "category": "main"
        },
        "latest_message_sender": {
            "id": PLUGIN_ID + ".state.latest_message_sender",
            "type": "text",
            "desc": "Kick Latest Message Sender",
            "default": "",
            "parentGroup": "Kick Streaming",
            "category": "main"
        },
    }

    TP_PLUGIN_EVENTS = {}

    def __init__(self):
        super().__init__(self.PLUGIN_ID, autoClose=True)
        self.kick = None
        self.socket_id = 0
        self.email = ""
        self.password = ""
        self.is_loggedin = False
    
    def update_user_data(self, user_data):
        # print(user_data)
        self.stateUpdate(self.TP_PLUGIN_STATES["profile_name"]["id"], user_data["user"]["username"])
        self.stateUpdate(self.TP_PLUGIN_STATES["profile_follower_count"]["id"], user_data["followers_count"])
        self.stateUpdate(self.TP_PLUGIN_STATES["profile_bio"]["id"], user_data["user"]["bio"])

    def on_message(self, ws, message):
        msg = json.loads(message)
        msg_data = json.loads(msg["data"])

        match msg["event"]:
            case "pusher:connection_established":
                self.socket_id = msg_data["socket_id"]
                # print(f"Socket ID: {self.socket_id}")
                self.kick.subscribe_to_channel()
                self.kick.subscribe_to_chatroom()
                # print(self.broadcasting_auth(self.socket_id, f"private-chatroom_13795564").text)
            case "App\\Events\\StreamerIsLive":
                self.stateUpdate(self.TP_PLUGIN_STATES["streaming_status"]["id"], "True")
                # print("Streamer is live")
                # self.subscribe_live_stream(msg_data["livestream"]["id"])
            case "App\\Events\\StopStreamBroadcast":
                self.stateUpdate(self.TP_PLUGIN_STATES["streaming_status"]["id"], "False")
                # print("Streamer is offline")
                # self.unsubscribe_live_stream(msg_data["livestream"]["id"])
            case "App\\Events\\ChatMessageEvent":
                self.stateUpdate(self.TP_PLUGIN_STATES["latest_message_content"]["id"], msg_data["content"])
                self.stateUpdate(self.TP_PLUGIN_STATES["latest_message_sender"]["id"], msg_data["sender"]["username"])
        self.log.info(f"Message: {msg}")

    def do_login(self):
        if self.kick == None and not self.is_loggedin:
            self.kick = Kick(self.email, self.password)
            self.kick.login()
            if self.kick.isLoggedin:
                self.is_loggedin = True
                self.update_user_data(self.kick.user_info)
                self.kick.connect_ws(on_message=self.on_message)
        else:
            self.log.debug("Already logged in")

    @Plugin.onStart()
    def onStart(self, data):
        self.log.info(f"Connected to TP v{data.get('tpVersionString', '?')}, plugin v{data.get('pluginVersion', '?')}.")
        self.log.debug(f"Connection: {data}")
        self.do_login()

    @Plugin.settingsRegister(name="email", type="text")
    def setting_email(self, value):
        self.email = value
        self.do_login()

    @Plugin.settingsRegister(name="password", type="text", isPassword=True)
    def setting_password(self, value):
        self.password = value
        self.do_login()

    @Plugin.actionRegister(id="send_message", category="chat", name="Send message", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                           format="Send $[message]")
    @Plugin.data(id="message", type="text", label="Message to send to chat", default="Hello World!")
    def send_message(self, data):
        if self.is_loggedin:
            self.kick.sendMessage(data["message"])

if __name__ == "__main__":
    kicktp = KickTP()
    kicktp.start()
    # kicktp.generateEntry()

    
    

    