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
        super().__init__(self.PLUGIN_ID)
        self.add_listener(TYPES.onShutdown, self.on_tpclose)
        self.update_thread = Thread(target=self.update_state)
        self.kick = None
        self.socket_id = 0
        self.email = ""
        self.password = ""
        self.is_loggedin = False
        self.stream_time = None
    
    def update_user_data(self, user_data):
        # print(user_data)
        self.stateUpdate(self.TP_PLUGIN_STATES["profile_name"]["id"], user_data["user"]["username"])
        self.stateUpdate(self.TP_PLUGIN_STATES["profile_follower_count"]["id"], str(user_data["followers_count"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["profile_bio"]["id"], user_data["user"]["bio"])

    def update_stream_info(self):
        print("updating stream info")
        data = self.kick.getUserInfo().json()
        self.kick.user_info = data
        live_stream = data["livestream"]
        chatroom = data["chatroom"]

        if isinstance(live_stream, dict) and live_stream.get("is_live", False):
            self.stateUpdate(self.TP_PLUGIN_STATES["streaming_title"]["id"], live_stream["session_title"])
            self.stateUpdate(self.TP_PLUGIN_STATES["streaming_viewers"]["id"], str(live_stream["viewer_count"]))
            self.stateUpdate(self.TP_PLUGIN_STATES["streaming_duration"]["id"], live_stream["duration"])
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
        self.kick.subscribe_to_channel()
        self.kick.subscribe_to_chatroom()
        self.kick.subscribe(self.socket_id, f"private-channel.{self.kick.user_info['id']}")
        self.kick.subscribe(self.socket_id, f"private-channel_{self.kick.user_info['id']}")
        self.kick.subscribe(self.socket_id, f"private-chatroom_{self.kick.user_info['chatroom']['id']}")
        self.kick.subscribe(self.socket_id, f"private-userfeed.{self.kick.user_info['user_id']}")

    def update_chatroominfo(self, chatroom_info):
        self.stateUpdate(self.TP_PLUGIN_STATES["slow_mode_enabled"]["id"], str(chatroom_info["slow_mode"]["enabled"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["slow_mode_delay"]["id"], str(chatroom_info["slow_mode"]["message_interval"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["sub_mode_enabled"]["id"], str(chatroom_info["subscribers_mode"]["enabled"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["follower_mode_enabled"]["id"], str(chatroom_info["followers_mode"]["enabled"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["follower_mode_delay"]["id"], str(chatroom_info["followers_mode"]["min_duration"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["emote_only_mode_enabled"]["id"], str(chatroom_info["emotes_mode"]["enabled"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["adv_antibot_enabled"]["id"], str(chatroom_info["advanced_bot_protection"]["enabled"]))
        self.stateUpdate(self.TP_PLUGIN_STATES["adv_antibot_remaintime"]["id"], str(chatroom_info["advanced_bot_protection"]["remaining_time"]))

    def on_message(self, ws, message):
        msg = json.loads(message)
        msg_data = json.loads(msg["data"])
        self.log.info(f"WS Message: {msg}")

        match msg["event"]:
            case "pusher:connection_established":
                self.socket_id = msg_data["socket_id"]
                print(f"Socket ID: {self.socket_id}")
                self.sub_init_events()

            case "App\\Events\\StreamerIsLive":
                self.stateUpdate(self.TP_PLUGIN_STATES["streaming_status"]["id"], "True")

            case "App\\Events\\StartStream":
                self.kick.subscribe(self.socket_id, f"private-livestream-updated.{msg_data['id']}")
                self.kick.subscribe(self.socket_id, f"private-livestream_{msg_data['id']}")
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
                    self.stateUpdate(self.TP_PLUGIN_STATES["latest_message_content"]["id"], msg_data["content"])
                    self.stateUpdate(self.TP_PLUGIN_STATES["latest_message_sender"]["id"], msg_data["sender"]["username"])
                    badge_string = ""
                    if badges := msg_data["sender"]["identity"]["badges"]:
                        for badge in badges:
                            badge_string += f"'{badge['type']}:{badge['text']}',"
                    self.stateUpdate(self.TP_PLUGIN_STATES["latest_message_badges"]["id"], badge_string)

            case "App\\Events\\FollowersUpdated":
                if msg_data["followed"]:
                    self.stateUpdate(self.TP_PLUGIN_STATES["latest_follower"]["id"], str(msg_data["username"]))
                    self.stateUpdate(self.TP_PLUGIN_STATES["profile_follower_count"]["id"], str(msg_data["followers_count"]))
            case "App\\Events\\ChatroomUpdatedEvent":
                self.update_chatroominfo(msg_data)

# private-channel.13993271
# private-chatroom_13795564
# private-channel_13993271
# private-userfeed.14762354

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

    @Plugin.actionRegister(id="send_message", category="chat", name="Send message", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                           format="Send $[message]")
    @Plugin.data(id="message", type="text", label="Message to send to chat", default="Hello World!")
    def send_message(self, data):
        if self.is_loggedin:
            self.kick.sendMessage(data["message"])

    @Plugin.actionRegister(id="Slow Mode", category="chat", name="Slow Mode", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                           format="$[option]slow mode with $[value]second message interval")
    @Plugin.data(id="value", type="text", label="Message interval", default="10")
    @Plugin.data(id="option", type="choice", label="Option", default="Enable", valueChoices=["Enable", "Disable"])
    def slow_mode(self, data):
        try:
            value = int(data["value"])
        except ValueError:
            self.log.error(f"slow_mode cannot convert {data['value']} to int, using default value of 10 seconds instead")
            value = 10
        self.kick.enable_slowmode(data["option"] == "Enable", value)

    @Plugin.actionRegister(id="followers_mode", category="chat", name="Followers Only Mode", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                           format="$[option]followers only mode with $[value]minutes duration")
    @Plugin.data(id="value", type="text", label="Duration", default="10")
    @Plugin.data(id="option", type="choice", label="Option", default="Enable", valueChoices=["Enable", "Disable"])
    def followers_mode(self, data):
        try:
            value = int(data["value"])
        except ValueError:
            self.log.error(f"followers_mode cannot convert {data['value']} to int, using default value of 6 minutes instead")
            value = 6
        self.kick.enable_followersmode(data["option"] == "Enable", value)

    @Plugin.actionRegister(id="emote_only_mode", category="chat", name="Emotes-Only Chat", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                           format="$[option]emotes-only chat")
    @Plugin.data(id="option", type="choice", label="Option", default="Enable", valueChoices=["Enable", "Disable"])
    def emote_only(self, data):
        self.kick.emote_only(data["option"] == "Enable")

    @Plugin.actionRegister(id="antibotprotection", category="chat", name="Advanced bot protection", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                           format="$[option]advanced bot protection")
    @Plugin.data(id="option", type="choice", label="Option", default="Enable", valueChoices=["Enable", "Disable"])
    def antibotprotection(self, data):
        self.kick.adv_antibot(data["option"] == "Enable")

    def on_tpclose(self, data):
        self.log.info("TP closed")
        self.update_thread.join()
        if self.kick != None:
            self.kick.ws.close()
        
if __name__ == "__main__":
    kicktp = KickTP()
    kicktp.start()
    # kicktp.generateEntry()

    
    

    