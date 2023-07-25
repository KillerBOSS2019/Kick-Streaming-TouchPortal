from kick import Kick
from Plugin import Plugin
import json
from time import sleep
from threading import Thread
from TouchPortalAPI import Tools
from TouchPortalAPI import TYPES
from sys import exit
from datetime import datetime

class KickTP(Plugin):
    __version__ = 60

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
            "default": "None",
            "parentGroup": "Kick profile",
            "category": "main"
        },
        "profile_follower_count": {
            "id": PLUGIN_ID + ".state.profile_follower_count",
            "type": "text",
            "desc": "Kick Profile Follower Count",
            "default": "0",
            "parentGroup": "Kick profile",
            "category": "main"
        },
        "profile_bio": {
            "id": PLUGIN_ID + ".state.profile_bio",
            "type": "text",
            "desc": "Kick Profile Bio",
            "default": "None",
            "parentGroup": "Kick profile",
            "category": "main"
        },
        "country": {
            "id": PLUGIN_ID + ".state.country",
            "type": "text",
            "desc": "Kick Profile Country",
            "default": "None",
            "parentGroup": "Kick profile",
            "category": "main"
        },
        "state": {
            "id": PLUGIN_ID + ".state.state",
            "type": "text",
            "desc": "Kick Profile State",
            "default": "None",
            "parentGroup": "Kick profile",
            "category": "main"
        },
        "city": {
            "id": PLUGIN_ID + ".state.city",
            "type": "text",
            "desc": "Kick Profile City",
            "default": "None",
            "parentGroup": "Kick profile",
            "category": "main"
        },
        "instagram": {
            "id": PLUGIN_ID + ".state.instagram",
            "type": "text",
            "desc": "Kick Profile Instagram",
            "default": "None",
            "parentGroup": "Kick profile",
            "category": "main"
        },
        "twitter": {
            "id": PLUGIN_ID + ".state.twitter",
            "type": "text",
            "desc": "Kick Profile Twitter",
            "default": "None",
            "parentGroup": "Kick profile",
            "category": "main"
        },
        "youtube": {
            "id": PLUGIN_ID + ".state.youtube",
            "type": "text",
            "desc": "Kick Profile Youtube",
            "default": "None",
            "parentGroup": "Kick profile",
            "category": "main"
        },
        "discord": {
            "id": PLUGIN_ID + ".state.discord",
            "type": "text",
            "desc": "Kick Profile Discord",
            "default": "None",
            "parentGroup": "Kick profile",
            "category": "main"
        },
        "tiktok": {
            "id": PLUGIN_ID + ".state.tiktik",
            "type": "text",
            "desc": "Kick Profile TikTok",
            "default": "None",
            "parentGroup": "Kick profile",
            "category": "main"
        },
        "facebook": {
            "id": PLUGIN_ID + ".state.facebook",
            "type": "text",
            "desc": "Kick Profile Facebook",
            "default": "None",
            "parentGroup": "Kick profile",
            "category": "main"
        },
        "profile_image": {
            "id": PLUGIN_ID + ".state.profile_image",
            "type": "text",
            "desc": "Kick Profile Image",
            "default": "None",
            "parentGroup": "Kick profile",
            "category": "main"
        },
        "streaming_status": {
            "id": PLUGIN_ID + ".state.streaming_status",
            "type": "text",
            "desc": "Kick is Live",
            "default": "False",
            "parentGroup": "Kick stream info",
            "category": "main"
        },
        "streaming_title": {
            "id": PLUGIN_ID + ".state.streaming_title",
            "type": "text",
            "desc": "Kick Stream Title",
            "default": "None",
            "parentGroup": "Kick stream info",
            "category": "main"
        },
        "streaming_viewers": {
            "id": PLUGIN_ID + ".state.streaming_viewers",
            "type": "text",
            "desc": "Kick stream viewer count",
            "default": "0",
            "parentGroup": "Kick stream info",
            "category": "main"
        },
        "streaming_duration": {
            "id": PLUGIN_ID + ".state.streaming_duration",
            "type": "text",
            "desc": "Kick Stream Duration",
            "default": "0",
            "parentGroup": "Kick stream info",
            "category": "main"
        },
        "is_mature": {
            "id": PLUGIN_ID + ".state.is_mature",
            "type": "text",
            "desc": "Kick Stream is Mature",
            "default": "False",
            "parentGroup": "Kick stream info",
            "category": "main"
        },
        "stream_lang": {
            "id": PLUGIN_ID + ".state.stream_lang",
            "type": "text",
            "desc": "Kick Stream Language",
            "default": "None",
            "parentGroup": "Kick stream info",
            "category": "main"
        },
        "stream_thumbnail": {
            "id": PLUGIN_ID + ".state.stream_thumbnail",
            "type": "text",
            "desc": "Kick Stream Thumbnail",
            "default": "None",
            "parentGroup": "Kick stream info",
            "category": "main"
        },
        "stream_topic": {
            "id": PLUGIN_ID + ".state.stream_topic",
            "type": "text",
            "desc": "Kick Stream Topic",
            "default": "None",
            "parentGroup": "Kick stream info",
            "category": "main"
        },
        "latest_message_content": {
            "id": PLUGIN_ID + ".state.latest_message_content",
            "type": "text",
            "desc": "Kick Latest Message",
            "default": "",
            "parentGroup": "Kick chat",
            "category": "chat"
        },
        "latest_message_sender": {
            "id": PLUGIN_ID + ".state.latest_message_sender",
            "type": "text",
            "desc": "Kick Latest Message Sender",
            "default": "",
            "parentGroup": "Kick chat",
            "category": "chat"
        },
        "latest_message_badges": {
            "id": PLUGIN_ID + ".state.latest_message_badges",
            "type": "text",
            "desc": "Kick Latest Message Badges",
            "default": "",
            "parentGroup": "Kick chat",
            "category": "chat"
        },
        "latest_follower": {
            "id": PLUGIN_ID + ".state.latest_follower",
            "type": "text",
            "desc": "Kick Latest Follower",
            "default": "",
            "parentGroup": "Kick chat",
            "category": "chat"
        },
        "slow_mode_enabled": {
            "id": PLUGIN_ID + ".state.slow_mode_enabled",
            "type": "text",
            "desc": "Kick is Slow mode enabled",
            "default": "False",
            "parentGroup": "Kick chat",
            "category": "chat"
        },
        "slow_mode_delay": {
            "id": PLUGIN_ID + ".state.slow_mode_delay",
            "type": "text",
            "desc": "Kick slow mode delay in seconds",
            "default": "0",
            "parentGroup": "Kick chat",
            "category": "chat"
        },
        "follower_mode_enabled": {
            "id": PLUGIN_ID + ".state.follower_mode_enabled",
            "type": "text",
            "desc": "Kick is Followers-only chat enabled",
            "default": "False",
            "parentGroup": "Kick chat",
            "category": "chat"
        },
        "follower_mode_delay": {
            "id": PLUGIN_ID + ".state.follower_mode_delay",
            "type": "text",
            "desc": "Kick followers mode delay in minutes",
            "default": "0",
            "parentGroup": "Kick chat",
            "category": "chat"
        },
        "emote_only_mode_enabled": {
            "id": PLUGIN_ID + ".state.emote_only_mode_enabled",
            "type": "text",
            "desc": "Kick is emote only mode enabled",
            "default": "False",
            "parentGroup": "Kick chat",
            "category": "chat"
        },
        "adv_antibot_enabled": {
            "id": PLUGIN_ID + ".state.adv_antibot_enabled",
            "type": "text",
            "desc": "Kick is Advanced bot protection enabled",
            "default": "False",
            "parentGroup": "Kick chat",
            "category": "chat"
        },
        "adv_antibot_remaintime": {
            "id": PLUGIN_ID + ".state.adv_antibot_remaintime",
            "type": "text",
            "desc": "Kick Advanced bot protection remaining time",
            "default": "0",
            "parentGroup": "Kick chat",
            "category": "chat"
        },
        "sub_mode_enabled": {
            "id": PLUGIN_ID + ".state.sub_mode_enabled",
            "type": "text",
            "desc": "Kick is Subscribers-only chat enabled",
            "default": "False",
            "parentGroup": "Kick chat",
            "category": "chat"
        },
    }

    TP_PLUGIN_EVENTS = {}

    def __init__(self):
        super().__init__(self.PLUGIN_ID, logFileName=self.TP_PLUGIN_INFO["name"] + ".log")
        self.add_listener(TYPES.onShutdown, self.on_tpclose)
        self.update_thread = Thread(target=self.update_state)
        self.kick = None
        self.socket_id = 0
        self.email = ""
        self.password = ""
        self.is_loggedin = False
        self.stream_time = None
        self.setLogLevel("DEBUG")
        self.chatlength = 5
        self.chat_buffer = {}
        self.profile_updated = False
    
    def update_user_data(self, user_data):
        # print(user_data)
        self.stateUpdate(self.TP_PLUGIN_STATES["profile_name"]["id"], user_data["user"]["username"])
        self.stateUpdate(self.TP_PLUGIN_STATES["profile_follower_count"]["id"], str(user_data["followers_count"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["profile_bio"]["id"], user_data["user"]["bio"])
        self.stateUpdate(self.TP_PLUGIN_STATES["country"]["id"], user_data["user"]["country"])
        self.stateUpdate(self.TP_PLUGIN_STATES["state"]["id"], user_data["user"]["state"])
        self.stateUpdate(self.TP_PLUGIN_STATES["city"]["id"], user_data["user"]["city"])
        self.stateUpdate(self.TP_PLUGIN_STATES["instagram"]["id"], user_data["user"]["instagram"])
        self.stateUpdate(self.TP_PLUGIN_STATES["twitter"]["id"], user_data["user"]["twitter"])
        self.stateUpdate(self.TP_PLUGIN_STATES["youtube"]["id"], user_data["user"]["youtube"])
        self.stateUpdate(self.TP_PLUGIN_STATES["facebook"]["id"], user_data["user"]["facebook"])
        self.stateUpdate(self.TP_PLUGIN_STATES["discord"]["id"], user_data["user"]["discord"])
        self.stateUpdate(self.TP_PLUGIN_STATES["tiktok"]["id"], user_data["user"]["tiktok"])

        if not self.profile_updated:
            profile_pic = ""
            if user_data["user"]["profile_pic"]:
                profile_pic = user_data["user"]["profile_pic"].replace("\\", "")
                profile_pic = Tools.convertImage_to_base64(profile_pic, "Web")
            self.stateUpdate(self.TP_PLUGIN_STATES["profile_image"]["id"], profile_pic)
            self.profile_updated = True

    def update_stream_info(self):
        self.log.info("updating stream info")
        data = self.kick.getUserInfo()

        if not data: return;
    
        data = data.json()
        self.kick.user_info = data
        live_stream = data["livestream"]
        chatroom = data["chatroom"]

        if isinstance(live_stream, dict) and live_stream.get("is_live", False):
            self.stateUpdate(self.TP_PLUGIN_STATES["streaming_title"]["id"], live_stream["session_title"])
            self.stateUpdate(self.TP_PLUGIN_STATES["streaming_viewers"]["id"], str(live_stream["viewer_count"]))
            self.stateUpdate(self.TP_PLUGIN_STATES["is_mature"]["id"], str(live_stream["is_mature"]))
            self.stateUpdate(self.TP_PLUGIN_STATES["stream_lang"]["id"], live_stream["language"])

        self.update_user_data(data)
        
        self.stateUpdate(self.TP_PLUGIN_STATES["slow_mode_enabled"]["id"], str(chatroom["slow_mode"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["slow_mode_delay"]["id"], str(chatroom["message_interval"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["follower_mode_enabled"]["id"], str(chatroom["followers_mode"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["follower_mode_delay"]["id"], str(chatroom["following_min_duration"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["emote_only_mode_enabled"]["id"], str(chatroom["emotes_mode"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["sub_mode_enabled"]["id"], str(chatroom["subscribers_mode"]))

    def sub_init_events(self):
        self.kick.subscribe(event=f"channel.{self.kick.user_info['chatroom']['channel_id']}", auth_required=False)
        self.kick.subscribe(event=f"chatrooms.{self.kick.user_info['chatroom']['id']}.v2", auth_required=False)
        self.kick.subscribe(socket_id=self.socket_id, event=f"private-channel.{self.kick.user_info['id']}")
        self.kick.subscribe(socket_id=self.socket_id, event=f"private-channel_{self.kick.user_info['id']}")
        self.kick.subscribe(socket_id=self.socket_id, event=f"private-chatroom_{self.kick.user_info['chatroom']['id']}")
        self.kick.subscribe(socket_id=self.socket_id, event=f"private-userfeed.{self.kick.user_info['user_id']}")

    def update_chatroominfo(self, chatroom_info):
        self.stateUpdate(self.TP_PLUGIN_STATES["slow_mode_enabled"]["id"], str(chatroom_info["slow_mode"]["enabled"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["slow_mode_delay"]["id"], str(chatroom_info["slow_mode"]["message_interval"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["sub_mode_enabled"]["id"], str(chatroom_info["subscribers_mode"]["enabled"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["follower_mode_enabled"]["id"], str(chatroom_info["followers_mode"]["enabled"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["follower_mode_delay"]["id"], str(chatroom_info["followers_mode"]["min_duration"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["emote_only_mode_enabled"]["id"], str(chatroom_info["emotes_mode"]["enabled"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["adv_antibot_enabled"]["id"], str(chatroom_info["advanced_bot_protection"]["enabled"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["adv_antibot_remaintime"]["id"], str(chatroom_info["advanced_bot_protection"]["remaining_time"]))

    def create_chatbuffer(self):
        for state in list(self.chat_buffer.keys()):
            self.removeState(self.PLUGIN_ID + f".chatbuffer.{state}.message")
            self.removeState(self.PLUGIN_ID + f".chatbuffer.{state}.username")
            self.removeState(self.PLUGIN_ID + f".chatbuffer.{state}.badge")
        self.chat_buffer = {}

        for message_state in range(1, self.chatlength+1):
            self.createStateMany([
                {
                    "id": self.PLUGIN_ID + f".chatbuffer.{message_state}.message",
                    "desc": f"Get index {message_state} message",
                    "type": "text",
                    "value": "",
                    "parentGroup": "Chat Buffer",
                },
                {
                    "id": self.PLUGIN_ID + f".chatbuffer.{message_state}.username",
                    "desc": f"Get index {message_state} username",
                    "type": "text",
                    "value": "",
                    "parentGroup": "Chat Buffer",
                },
                {
                    "id": self.PLUGIN_ID + f".chatbuffer.{message_state}.badge",
                    "desc": f"Get index {message_state} badge",
                    "type": "text",
                    "value": "",
                    "parentGroup": "Chat Buffer",
                }
            ])
            self.chat_buffer[message_state] = {"message": "", "username": "", "badge": ""}

    def update_chat_state(self, index, message, username, badge):
        self.chat_buffer[index]["message"] = message
        self.chat_buffer[index]["username"] = username
        self.chat_buffer[index]["badge"] = badge
        self.stateUpdateMany([
            {
                "id": self.PLUGIN_ID + f".chatbuffer.{index}.message",
                "value": message
            },
            {
                "id": self.PLUGIN_ID + f".chatbuffer.{index}.username",
                "value": username
            },
            {
                "id": self.PLUGIN_ID + f".chatbuffer.{index}.badge",
                "value": badge
            }
        ])

    def update_message(self, message_data):
        if self.chat_buffer:
            for state in range(len(self.chat_buffer.keys()), 1, -1):
                self.update_chat_state(state, self.chat_buffer[state - 1]["message"], self.chat_buffer[state - 1]["username"], self.chat_buffer[state - 1]["badge"])

            message = message_data["content"]
            username = message_data["sender"]["username"]
            badge_string = ""
            if badges := message_data["sender"]["identity"]["badges"]:
                badge_string = ",".join(f'"{badge["type"]}:{badge["text"]}"' for badge in badges)

            self.update_chat_state(1, message, username, badge_string)

    def on_message(self, ws, message):
        print(message)
        msg = json.loads(message)
        msg_data = json.loads(msg["data"])
        self.log.info(f"WS Message: {msg}")

        match msg["event"]:
            case "pusher:connection_established":
                self.socket_id = msg_data["socket_id"]
                self.log.info(f"Socket ID: {self.socket_id}")
                self.create_chatbuffer()
                self.kick.session.headers.update({"X-Socket-Id": self.socket_id})
                self.sub_init_events()

            case "App\\Events\\StreamerIsLive":
                self.stateUpdate(self.TP_PLUGIN_STATES["streaming_status"]["id"], "True")

            case "App\\Events\\StartStream":
                self.kick.subscribe(socket_id=self.socket_id, event=f"private-livestream-updated.{msg_data['id']}")
                self.kick.subscribe(socket_id=self.socket_id, event=f"private-livestream_{msg_data['id']}")
                self.update_stream_info()
                self.stateUpdate(self.TP_PLUGIN_STATES["stream_topic"]["id"], msg_data["category"]["name"])
                self.stateUpdate(self.TP_PLUGIN_STATES["stream_thumbnail"]["id"], Tools.convertImage_to_base64(self.kick.user_info["livestream"]["thumbnail"]["url"]))
                self.stream_time = datetime.now()

            case "App\\Events\\StopStreamBroadcast":
                self.stateUpdate(self.TP_PLUGIN_STATES["streaming_status"]["id"], "False")
                self.kick.unsubscribe(f"private-livestream-updated.{msg_data['livestream']['id']}")
                self.stateUpdate(self.TP_PLUGIN_STATES["stream_topic"]["id"], "")
                self.stateUpdate(self.TP_PLUGIN_STATES["stream_thumbnail"]["id"], "")
                self.stream_time = None

            case "App\\Events\\ChatMessageEvent":
                if msg_data["type"] == "message":
                    self.update_message(msg_data)

            case "App\\Events\\FollowersUpdated":
                if msg_data["followed"]:
                    self.stateUpdate(self.TP_PLUGIN_STATES["latest_follower"]["id"], str(msg_data["username"]))
                    self.stateUpdate(self.TP_PLUGIN_STATES["profile_follower_count"]["id"], str(msg_data["followers_count"]))
            case "App\\Events\\ChatroomUpdatedEvent":
                self.update_chatroominfo(msg_data)
    
    def on_close(self, error):
        self.log.info(f"WS Closed: {error}")

    def do_login(self):
        if self.kick == None and not self.is_loggedin:
            self.kick = Kick(self.email, self.password, self.log)
            self.kick.login()
            if self.kick.isLoggedin:
                self.is_loggedin = True
                self.update_user_data(self.kick.user_info)
                self.kick.connect_ws(on_message=self.on_message, on_close=self.on_close)
        else:
            self.log.debug("Already logged in")

    def update_state(self):
        timer = 0

        while self.isConnected():
            if timer % 30 == 0: # update every 30s
                self.update_stream_info()

            if timer >= 60:
                if self.is_loggedin:
                    self.kick.send_ping() # keep ws alive
                    self.kick.save_cookie()
                    timer = 0

            if self.stream_time != None:
                difference = datetime.now() - self.stream_time
                time_string = str(difference).split(".")[0]
                self.stateUpdate(self.TP_PLUGIN_STATES["streaming_duration"]["id"], time_string)

            sleep(1)
            timer += 1

    def state_usedefault(self):
        for state in self.TP_PLUGIN_STATES.values():
            self.stateUpdate(state["id"], state["default"])

    @Plugin.onStart()
    def onStart(self, data):
        self.log.info(f"Connected to TP v{data.get('tpVersionString', '?')}, plugin v{data.get('pluginVersion', '?')}.")
        self.log.debug(f"Connection: {data}")
        self.state_usedefault()
        if data["settings"][2]["email"] and data["settings"][3]["password"]:
            self.do_login()
            self.update_thread.start()
        

    @Plugin.settingsRegister(name="email", type="text")
    def setting_email(self, value):
        self.email = value
        # self.do_login()

    @Plugin.settingsRegister(name="password", type="text", isPassword=True)
    def setting_password(self, value):
        self.password = value
        # self.do_login()

    @Plugin.settingsRegister(name="chat buffer", type="text", default="5")
    def setting_chat_buffer(self, value):
        self.chat_length = int(value)

    @Plugin.settingsRegister(name="logging", type="text", default="DEBUG")
    def set_logging(self, value):
        self.setLogLevel(value)

    @Plugin.actionRegister(id="send_message", category="chat", name="Send message", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                           format="Send $[message]")
    @Plugin.data(id="message", type="text", label="Message to send to chat", default="Hello World!")
    def send_message(self, data):
        if self.is_loggedin:
            response = self.kick.sendMessage(data["message"])
            if response.status_code == 200:
                self.update_message(response.json()["data"])

    # @Plugin.actionRegister(id="Slow Mode", category="chat", name="Slow Mode", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
    #                        format="$[option]slow mode with $[value]second message interval")
    # @Plugin.data(id="value", type="text", label="Message interval", default="10")
    # @Plugin.data(id="option", type="choice", label="Option", default="Enable", valueChoices=["Enable", "Disable"])
    # def slow_mode(self, data):
    #     try:
    #         value = int(data["value"])
    #     except ValueError:
    #         self.log.error(f"slow_mode cannot convert {data['value']} to int, using default value of 10 seconds instead")
    #         value = 10
    #     self.kick.enable_slowmode(data["option"] == "Enable", value)

    # @Plugin.actionRegister(id="followers_mode", category="chat", name="Followers Only Mode", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
    #                        format="$[option]followers only mode with $[value]minutes duration")
    # @Plugin.data(id="value", type="text", label="Duration", default="10")
    # @Plugin.data(id="option", type="choice", label="Option", default="Enable", valueChoices=["Enable", "Disable"])
    # def followers_mode(self, data):
    #     try:
    #         value = int(data["value"])
    #     except ValueError:
    #         self.log.error(f"followers_mode cannot convert {data['value']} to int, using default value of 6 minutes instead")
    #         value = 6
    #     self.kick.enable_followersmode(data["option"] == "Enable", value)

    # @Plugin.actionRegister(id="emote_only_mode", category="chat", name="Emotes-Only Chat", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
    #                        format="$[option]emotes-only chat")
    # @Plugin.data(id="option", type="choice", label="Option", default="Enable", valueChoices=["Enable", "Disable"])
    # def emote_only(self, data):
    #     self.kick.emote_only(data["option"] == "Enable")

    # @Plugin.actionRegister(id="antibotprotection", category="chat", name="Advanced bot protection", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
    #                        format="$[option]advanced bot protection")
    # @Plugin.data(id="option", type="choice", label="Option", default="Enable", valueChoices=["Enable", "Disable"])
    # def antibotprotection(self, data):
    #     self.kick.adv_antibot(data["option"] == "Enable")

    def on_tpclose(self, data):
        self.log.info("TP closed")
        self.update_thread.join()
        if self.kick != None:
            self.kick.ws.close()
        
if __name__ == "__main__":
    kicktp = KickTP()
    kicktp.start()

else:
    kicktp = KickTP()
    kicktp.startRegister()
    
    __version__ = kicktp.__version__

    TP_PLUGIN_INFO = kicktp.TP_PLUGIN_INFO
    TP_PLUGIN_SETTINGS = kicktp.TP_PLUGIN_SETTINGS
    TP_PLUGIN_CATEGORIES = kicktp.TP_PLUGIN_CATEGORIES
    TP_PLUGIN_CONNECTORS = kicktp.TP_PLUGIN_CONNECTORS
    TP_PLUGIN_ACTIONS = kicktp.TP_PLUGIN_ACTIONS
    TP_PLUGIN_STATES = kicktp.TP_PLUGIN_STATES

    
    

    