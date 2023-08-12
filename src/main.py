import json
from datetime import datetime
from sys import exit
from threading import Thread, Timer
from time import sleep

from TouchPortalAPI import TYPES, Tools

from kickapi import Kick, KickWebSockets, KickSaveSession
from Plugin import Plugin

class KickTP(Plugin):
    __version__ = 10108

    PLUGIN_ID = "com.github.killerboss2019.kicktp"

    TP_PLUGIN_INFO = {
        "sdk": 6,
        "version": __version__,
        "name": "Kick-Streaming",
        "id": PLUGIN_ID,
        "plugin_start_cmd_windows": "%TP_PLUGIN_FOLDER%kick\\tp_kick.exe",
        'plugin_start_cmd_linux': "sh %TP_PLUGIN_FOLDER%TPSpeedTest\\start.sh tp_kick",
        'plugin_start_cmd_mac': "sh %TP_PLUGIN_FOLDER%TPSpeedTest\\start.sh tp_kick",
        "configuration": {
            "colorDark": "#15843e",
            "colorLight": "#1ca950"
        }
    }

    TP_PLUGIN_SETTINGS = {}

    TP_PLUGIN_CATEGORIES = {
        "main": {
            "id": PLUGIN_ID + ".main",
            "name": "Kick - Profile",
            "imagepath": "%TP_PLUGIN_FOLDER%kick\\kick.png"
        },
        "chat": {
            "id": PLUGIN_ID + ".chat",
            "name": "Kick - Chat",
            "imagepath": "%TP_PLUGIN_FOLDER%kick\\kick.png"
        },
        "poll": {
            "id": PLUGIN_ID + ".poll",
            "name": "Kick - Poll",
            "imagepath": "%TP_PLUGIN_FOLDER%kick\\kick.png"
        },
        "socials": {
            "id": PLUGIN_ID + ".socials",
            "name": "Kick - Socials",
            "imagepath": "%TP_PLUGIN_FOLDER%kick\\kick.png"
        },
        "streaminfo": {
            "id": PLUGIN_ID + ".streaminfo",
            "name": "Kick - Stream Info",
            "imagepath": "%TP_PLUGIN_FOLDER%kick\\kick.png"
        },
        "raid": {
            "id": PLUGIN_ID + ".raid",
            "name": "Kick - Raid",
            "imagepath": "%TP_PLUGIN_FOLDER%kick\\kick.png"
        }
    }

    TP_PLUGIN_CONNECTORS = {}

    TP_PLUGIN_ACTIONS = {}
    
    TP_PLUGIN_STATES = {
        # Profile
        "profile_image": {
            "id": PLUGIN_ID + ".state.profile_image",
            "type": "text",
            "desc": "Kick Profile Image",
            "default": "None",
            "parentGroup": "Kick profile",
            "category": "main"
        },
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

        # Socials
        "instagram": {
            "id": PLUGIN_ID + ".state.instagram",
            "type": "text",
            "desc": "Kick Profile Instagram",
            "default": "None",
            "parentGroup": "Kick - Socials",
            "category": "socials"
        },
        "twitter": {
            "id": PLUGIN_ID + ".state.twitter",
            "type": "text",
            "desc": "Kick Profile Twitter",
            "default": "None",
            "parentGroup": "Kick - Socials",
            "category": "socials"
        },
        "youtube": {
            "id": PLUGIN_ID + ".state.youtube",
            "type": "text",
            "desc": "Kick Profile Youtube",
            "default": "None",
            "parentGroup": "Kick - Socials",
            "category": "socials"
        },
        "discord": {
            "id": PLUGIN_ID + ".state.discord",
            "type": "text",
            "desc": "Kick Profile Discord",
            "default": "None",
            "parentGroup": "Kick - Socials",
            "category": "socials"
        },
        "tiktok": {
            "id": PLUGIN_ID + ".state.tiktik",
            "type": "text",
            "desc": "Kick Profile TikTok",
            "default": "None",
            "parentGroup": "Kick - Socials",
            "category": "socials"
        },
        "facebook": {
            "id": PLUGIN_ID + ".state.facebook",
            "type": "text",
            "desc": "Kick Profile Facebook",
            "default": "None",
            "parentGroup": "Kick - Socials",
            "category": "socials"
        },
        
        # Stream Info
        "streaming_status": {
            "id": PLUGIN_ID + ".state.streaming_status",
            "type": "text",
            "desc": "Kick is Live",
            "default": "False",
            "parentGroup": "Kick stream info",
            "category": "streaminfo"
        },
        "streaming_title": {
            "id": PLUGIN_ID + ".state.streaming_title",
            "type": "text",
            "desc": "Kick Stream Title",
            "default": "None",
            "parentGroup": "Kick stream info",
            "category": "streaminfo"
        },
        "streaming_viewers": {
            "id": PLUGIN_ID + ".state.streaming_viewers",
            "type": "text",
            "desc": "Kick stream viewer count",
            "default": "0",
            "parentGroup": "Kick stream info",
            "category": "streaminfo"
        },
        "streaming_duration": {
            "id": PLUGIN_ID + ".state.streaming_duration",
            "type": "text",
            "desc": "Kick Stream Duration",
            "default": "0",
            "parentGroup": "Kick stream info",
            "category": "streaminfo"
        },
        "is_mature": {
            "id": PLUGIN_ID + ".state.is_mature",
            "type": "text",
            "desc": "Kick Stream is Mature",
            "default": "False",
            "parentGroup": "Kick stream info",
            "category": "streaminfo"
        },
        "stream_lang": {
            "id": PLUGIN_ID + ".state.stream_lang",
            "type": "text",
            "desc": "Kick Stream Language",
            "default": "None",
            "parentGroup": "Kick stream info",
            "category": "streaminfo"
        },
        "stream_thumbnail": {
            "id": PLUGIN_ID + ".state.stream_thumbnail",
            "type": "text",
            "desc": "Kick Stream Thumbnail",
            "default": "None",
            "parentGroup": "Kick stream info",
            "category": "streaminfo"
        },
        "stream_topic": {
            "id": PLUGIN_ID + ".state.stream_topic",
            "type": "text",
            "desc": "Kick Stream Topic",
            "default": "None",
            "parentGroup": "Kick stream info",
            "category": "streaminfo"
        },

        # Chat
        "latest_follower": {
            "id": PLUGIN_ID + ".state.latest_follower",
            "type": "text",
            "desc": "Kick Latest Follower",
            "default": "",
            "parentGroup": "Kick chat",
            "category": "chat"
        },
        "latest_unfollower": {
            "id": PLUGIN_ID + ".state.latest_unfollower",
            "type": "text",
            "desc": "Kick Latest Unfollower",
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

        # Poll states
        "poll_question": {
            "id": PLUGIN_ID + ".state.poll_question",
            "type": "text",
            "desc": "Kick poll question",
            "default": "None",
            "parentGroup": "Kick poll",
            "category": "poll"
        },
        "option1_votes": {
            "id": PLUGIN_ID + ".state.option1_votes",
            "type": "text",
            "desc": "Kick poll option 1 votes",
            "default": "0",
            "parentGroup": "Kick poll",
            "category": "poll"
        },
        "option1_label": {
            "id": PLUGIN_ID + ".state.option1_label",
            "type": "text",
            "desc": "Kick poll option 1 label",
            "default": "None",
            "parentGroup": "Kick poll",
            "category": "poll"
        },
        "option2_votes": {
            "id": PLUGIN_ID + ".state.option2_votes",
            "type": "text",
            "desc": "Kick poll option 2 votes",
            "default": "0",
            "parentGroup": "Kick poll",
            "category": "poll"
        },
        "option2_label": {
            "id": PLUGIN_ID + ".state.option2_label",
            "type": "text",
            "desc": "Kick poll option 2 label",
            "default": "None",
            "parentGroup": "Kick poll",
            "category": "poll"
        },
        "option3_votes": {
            "id": PLUGIN_ID + ".state.option3_votes",
            "type": "text",
            "desc": "Kick poll option 3 votes",
            "default": "0",
            "parentGroup": "Kick poll",
            "category": "poll"
        },
        "option3_label": {
            "id": PLUGIN_ID + ".state.option3_label",
            "type": "text",
            "desc": "Kick poll option 3 label",
            "default": "None",
            "parentGroup": "Kick poll",
            "category": "poll"
        },
        "option4_votes": {
            "id": PLUGIN_ID + ".state.option4_votes",
            "type": "text",
            "desc": "Kick poll option 4 votes",
            "default": "0",
            "parentGroup": "Kick poll",
            "category": "poll"
        },
        "option4_label": {
            "id": PLUGIN_ID + ".state.option4_label",
            "type": "text",
            "desc": "Kick poll option 4 label",
            "default": "None",
            "parentGroup": "Kick poll",
            "category": "poll"
        },
        "option5_votes": {
            "id": PLUGIN_ID + ".state.option5_votes",
            "type": "text",
            "desc": "Kick poll option 5 votes",
            "default": "0",
            "parentGroup": "Kick poll",
            "category": "poll"
        },
        "option5_label": {
            "id": PLUGIN_ID + ".state.option5_label",
            "type": "text",
            "desc": "Kick poll option 5 label",
            "default": "None",
            "parentGroup": "Kick poll",
            "category": "poll"
        },
        "option6_votes": {
            "id": PLUGIN_ID + ".state.option6_votes",
            "type": "text",
            "desc": "Kick poll option 6 votes",
            "default": "0",
            "parentGroup": "Kick poll",
            "category": "poll"
        },
        "option6_label": {
            "id": PLUGIN_ID + ".state.option6_label",
            "type": "text",
            "desc": "Kick poll option 6 label",
            "default": "None",
            "parentGroup": "Kick poll",
            "category": "poll"
        },
        "is_poll_running": {
            "id": PLUGIN_ID + ".state.is_poll_running",
            "type": "text",
            "desc": "Kick is poll running",
            "default": "False",
            "parentGroup": "Kick poll",
            "category": "poll"
        },

        # raids
        "latest_raid_name": {
            "id": PLUGIN_ID + ".state.latest_raid_name",
            "type": "text",
            "desc": "Kick latest raid name",
            "default": "None",
            "parentGroup": "Kick raid",
            "category": "raid"
        },
        "latest_raid_viewers": {
            "id": PLUGIN_ID + ".state.latest_raid_viewers",
            "type": "text",
            "desc": "Kick latest raid viewers count",
            "default": "0",
            "parentGroup": "Kick raid",
            "category": "raid"
        },
        "latest_raid_optional_message": {
            "id": PLUGIN_ID + ".state.latest_raid_optional_message",
            "type": "text",
            "desc": "Kick latest raid optional message",
            "default": "None",
            "parentGroup": "Kick raid",
            "category": "raid"
        },
    }

    TP_PLUGIN_EVENTS = {
        "onSlowMode": {
            "id": PLUGIN_ID + ".event.onSlowMode",
            "name": "On slow mode",
            "format": "When slow mode is $val",
            "type": "communicate",
            "valueType": "choice",
            "valueChoices": [
                "True",
                "False"
            ],
            "valueStateId": TP_PLUGIN_STATES["slow_mode_enabled"]["id"],
            "category": "chat"
        },
        "onFollowerMode": {
            "id": PLUGIN_ID + ".event.onFollowerMode",
            "name": "On follower mode",
            "format": "When follower mode is $val",
            "type": "communicate",
            "valueType": "choice",
            "valueChoices": [
                "True",
                "False"
            ],
            "valueStateId": TP_PLUGIN_STATES["follower_mode_enabled"]["id"],
            "category": "chat"
        },
        "onEmoteOnlyMode": {
            "id": PLUGIN_ID + ".event.onEmoteOnlyMode",
            "name": "On emote only mode",
            "format": "When emote only mode is $val",
            "type": "communicate",
            "valueType": "choice",
            "valueChoices": [
                "True",
                "False"
            ],
            "valueStateId": TP_PLUGIN_STATES["emote_only_mode_enabled"]["id"],
            "category": "chat"
        },
        "onSubMode": {
            "id": PLUGIN_ID + ".event.onSubMode",
            "name": "On sub mode",
            "format": "When sub mode is $val",
            "type": "communicate",
            "valueType": "choice",
            "valueChoices": [
                "True",
                "False"
            ],
            "valueStateId": TP_PLUGIN_STATES["sub_mode_enabled"]["id"],
            "category": "chat"
        },
        "onAdvAntibot": {
            "id": PLUGIN_ID + ".event.onAdvAntibot",
            "name": "On advanced antibot",
            "format": "When advanced antibot is $val",
            "type": "communicate",
            "valueType": "choice",
            "valueChoices": [
                "True",
                "False"
            ],
            "valueStateId": TP_PLUGIN_STATES["adv_antibot_enabled"]["id"],
            "category": "chat"
        },
        "onPollRunning": {
            "id": PLUGIN_ID + ".event.onPollRunning",
            "name": "On poll",
            "format": "When poll is started $val",
            "type": "communicate",
            "valueType": "choice",
            "valueChoices": [
                "True",
                "False"
            ],
            "valueStateId": TP_PLUGIN_STATES["is_poll_running"]["id"],
            "category": "poll"
        },
        "onStreamStart": {
            "id": PLUGIN_ID + ".event.onStreamStart",
            "name": "On stream start",
            "format": "When stream is started $val",
            "type": "communicate",
            "valueType": "choice",
            "valueChoices": [
                "True",
                "False"
            ],
            "valueStateId": TP_PLUGIN_STATES["streaming_status"]["id"],
            "category": "streaminfo"
        },
    }

    def __init__(self):
        super().__init__(self.PLUGIN_ID, logFileName=self.TP_PLUGIN_INFO["name"] + ".log")
        self.add_listener(TYPES.onShutdown, self.on_tpclose)
        self.add_listener(TYPES.onError, self.onError)
        self.update_thread = Thread(target=self.update_state)
        self.setLogLevel("DEBUG")
        self.kick:Kick = None
        self.kick_ws:KickWebSockets = None
        self.socket_id = 0
        self.email = ""
        self.password = ""
        self.stream_time = None
        self.chatlength = 5
        self.chat_buffer = {}
        self.profile_updated = False
        self.chatroom_id = ""
        self.followed_image_cache = {}
        self.chat_time_format = "%I:%M:%S %p"
        self.poll_timer_thread = None
    
    def update_user_data(self, user_data):
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
            self.log.info("profile image updated")

    def update_followed_user(self):
        data = self.kick.get_followed_user()

        if data.status_code == 200:
            json_data = data.json()

            for user in json_data["channels"]:
                requireUpdate = False
                user_index = json_data["channels"].index(user) + 1
                name = user["user_username"]

                if user["user_username"] not in self.followed_image_cache or self.followed_image_cache.get(user["user_username"]) != user["profile_picture"]:
                    requireUpdate = True
                    self.log.info(f"User {name} profile image updated")

                self.createStateMany([
                    {
                        "id": self.PLUGIN_ID + f".followed_users.{user_index}.username",
                        "desc": f"Get followed index {user_index} username",
                        "type": "text",
                        "value": f"{name}",
                        "parentGroup": "Followed Users",
                    },
                    {
                        "id": self.PLUGIN_ID + f".followed_users.{user_index}.isLive",
                        "desc": f"Get followed index {user_index} is live",
                        "type": "text",
                        "value": f"{user['is_live']}",
                        "parentGroup": "Followed Users",
                    },
                    {
                        "id": self.PLUGIN_ID + f".followed_users.{user_index}.viewer",
                        "desc": f"Get followed index {user_index} viewer count",
                        "type": "text",
                        "value": f"{user['viewer_count']}",
                        "parentGroup": "Followed Users",
                    },
                ])

                if requireUpdate:
                    self.followed_image_cache[user["user_username"]] = user["profile_picture"]
                    self.createState(self.PLUGIN_ID + f".followed_users.{user_index}.profile_image",
                                     f"Get followed index {user_index} profile image",
                                     Tools.convertImage_to_base64(user["profile_picture"], "Web"),
                                     "Followed Users")

    def update_stream_info(self):
        self.log.info("updating stream info")
        data = self.kick.getUserData()

        if not data: return;
    
        data = data.json()
        live_stream = data["livestream"]
        chatroom = data["chatroom"]

        channel_users = data.get("channel_users", [])

        for user in range(len(channel_users)):
            self.createStateMany([
                {
                    "id": self.PLUGIN_ID + f".channelusers.{user+1}.username",
                    "desc": f"Get moderator index {user+1} username",
                    "type": "text",
                    "value": f"{channel_users[user]['user']['username']}",
                    "parentGroup": "Moderators",
                },
                {
                    "id": self.PLUGIN_ID + f".channelusers.{user+1}.role",
                    "desc": f"Get moderator index {user+1} role",
                    "type": "text",
                    "value": f"{channel_users[user]['role']}",
                    "parentGroup": "Moderators",
                },
                {
                    "id": self.PLUGIN_ID + f".channelusers.{user}.bio",
                    "desc": f"Get moderator index {user} bio",
                    "type": "text",
                    "value": f"{channel_users[user]['user']['bio']}",
                    "parentGroup": "Moderators",
                },
            ])

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
        self.chatroom_id = chatroom["id"]
        # print(chatroom)

    def sub_init_events(self):
        user_data = self.kick.getUserData()
        # if not user_data.status_code == 200: return;
        user_data = user_data.json()
        self.kick_ws.subscribe(event=f"channel.{user_data['chatroom']['channel_id']}")
        self.kick_ws.subscribe(event=f"chatrooms.{user_data['chatroom']['id']}.v2")
        for event in [f"private-channel.{user_data['id']}", f"private-channel_{user_data['id']}",
                      f"private-chatroom_{user_data['chatroom']['id']}", f"private-userfeed.{user_data['user_id']}"]:
            auth = self.kick.broadcasting_auth(channel=event, socket_id=self.socket_id).json()["auth"]
            self.kick_ws.subscribe(event=event, socket_id=self.socket_id, auth=auth)

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
                },
                {
                    "id": self.PLUGIN_ID + f".chatbuffer.{message_state}.user_color",
                    "desc": f"Get index {message_state} user color",
                    "type": "text",
                    "value": "",
                    "parentGroup": "Chat Buffer"
                },
                {
                    "id": self.PLUGIN_ID + f".chatbuffer.{message_state}.time",
                    "desc": f"Get index {message_state} time",
                    "type": "text",
                    "value": "",
                    "parentGroup": "Chat Buffer"
                }
            ])
            self.chat_buffer[message_state] = {"message": "", "username": "", "badge": "", "user_color": "", "time": ""}

    def update_chat_state(self, index, message, username, badge, color, time):
        self.chat_buffer[index]["message"] = message
        self.chat_buffer[index]["username"] = username
        self.chat_buffer[index]["badge"] = badge
        self.chat_buffer[index]["user_color"] = color
        self.chat_buffer[index]["time"] = time
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
            },
            {
                "id": self.PLUGIN_ID + f".chatbuffer.{index}.user_color",
                "value": color
            },
            {
                "id": self.PLUGIN_ID + f".chatbuffer.{index}.time",
                "value": time
            }
        ])

    def update_message(self, message_data):
        if self.chat_buffer:
            for state in range(len(self.chat_buffer.keys()), 1, -1):
                self.update_chat_state(state, self.chat_buffer[state - 1]["message"], 
                                       self.chat_buffer[state - 1]["username"], 
                                       self.chat_buffer[state - 1]["badge"],
                                       self.chat_buffer[state - 1]["user_color"],
                                       self.chat_buffer[state - 1]["time"])

            message = self.kick.decode_emotes(message_data["content"])
            username = message_data["sender"]["username"]
            user_color = message_data["sender"]["identity"]["color"]
            time = datetime.now().strftime(self.chat_time_format)
            badge_string = ""
            if badges := message_data["sender"]["identity"]["badges"]:
                badge_string = ",".join(f'"{badge["type"]}:{badge["text"]}"' for badge in badges)

            self.update_chat_state(1, message, username, badge_string, user_color, time)

    def reset_poll(self):
        # self.stateUpdate(self.TP_PLUGIN_STATES["poll_question"]["id"], "")
        self.stateUpdate(self.TP_PLUGIN_STATES["is_poll_running"]["id"], "False")

        # for option in range(1, 7):
        #     self.stateUpdate(self.TP_PLUGIN_STATES[f"option{option}_votes"]["id"], "")
        #     self.stateUpdate(self.TP_PLUGIN_STATES[f"option{option}_label"]["id"], "")

    def update_poll(self, poll_data):
        poll_data = poll_data["poll"]
        self.stateUpdate(self.TP_PLUGIN_STATES["poll_question"]["id"], poll_data["title"])
        self.stateUpdate(self.TP_PLUGIN_STATES["is_poll_running"]["id"], "True")

        for option in range(1, 7):
            if option <= len(poll_data["options"]):
                self.stateUpdate(self.TP_PLUGIN_STATES[f"option{option}_votes"]["id"], str(poll_data["options"][option-1]["votes"]))
                self.stateUpdate(self.TP_PLUGIN_STATES[f"option{option}_label"]["id"], str(poll_data["options"][option-1]["label"]))
            else:
                self.stateUpdate(self.TP_PLUGIN_STATES[f"option{option}_votes"]["id"], "")
                self.stateUpdate(self.TP_PLUGIN_STATES[f"option{option}_label"]["id"], "")

    def on_message(self, ws, message):
        msg = json.loads(message)
        msg_data = json.loads(msg["data"])
        self.log.info(f"WS Message: {msg}")

        match msg["event"]:
            case "pusher:connection_established":
                self.socket_id = msg_data["socket_id"]
                self.create_chatbuffer()
                self.kick.session.headers.update({"X-Socket-Id": self.socket_id})
                self.sub_init_events()

            case "App\\Events\\StreamerIsLive":
                self.stateUpdate(self.TP_PLUGIN_STATES["streaming_status"]["id"], "True")

            case "App\\Events\\StartStream":
                for event in [f"private-livestream-updated.{msg_data['id']}", f"private-livestream_{msg_data['id']}"]:
                    auth = self.kick.broadcasting_auth(channel=event, socket_id=self.socket_id).json()
                    self.kick_ws.subscribe(socket_id=self.socket_id, event=event, auth=auth["auth"])
                user_info = self.kick.getUserData().json();
                self.update_stream_info()
                self.stateUpdate(self.TP_PLUGIN_STATES["stream_topic"]["id"], msg_data["category"]["name"])

                thumbnail = ""
                if user_info["livestream"]["thumbnail"]:
                    thumbnail = Tools.convertImage_to_base64(user_info["livestream"]["thumbnail"]["url"])
                self.stateUpdate(self.TP_PLUGIN_STATES["stream_thumbnail"]["id"], thumbnail)
                self.stream_time = datetime.now()

            case "App\\Events\\StopStreamBroadcast":
                self.stateUpdate(self.TP_PLUGIN_STATES["streaming_status"]["id"], "False")
                self.kick_ws.unsubscribe(f"private-livestream-updated.{msg_data['livestream']['id']}")
                self.stateUpdate(self.TP_PLUGIN_STATES["stream_topic"]["id"], "")
                self.stateUpdate(self.TP_PLUGIN_STATES["stream_thumbnail"]["id"], "")
                self.stream_time = None

            case "App\\Events\\ChatMessageEvent":
                if msg_data["type"] == "message":
                    self.update_message(msg_data)

            case "App\\Events\\FollowersUpdatedForChannelOwner":
                if msg_data["followed"] and msg_data["username"]:
                    self.stateUpdate(self.TP_PLUGIN_STATES["latest_follower"]["id"], str(msg_data["username"]))
                else:
                    self.stateUpdate(self.TP_PLUGIN_STATES["latest_unfollower"]["id"], str(msg_data["username"]))

                self.stateUpdate(self.TP_PLUGIN_STATES["profile_follower_count"]["id"], str(msg_data["followers_count"]))
            case "App\\Events\\ChatroomUpdatedEvent":
                self.update_chatroominfo(msg_data)
            
            case "App\\Events\\ChatroomClearEvent":
                ...

            case "App\\Events\\PollUpdateEvent":
                if self.poll_timer_thread == None:
                    self.poll_timer_thread = Timer(msg_data["poll"]["duration"], self.reset_poll)
                    self.poll_timer_thread.start()

                self.update_poll(msg_data)

            case "App\\Events\\PollDeleteEvent":
                if self.poll_timer_thread != None:
                    self.poll_timer_thread.cancel()
                    self.poll_timer_thread = None
                self.reset_poll()
            
            case "App\\Events\\StreamHostEvent":
                if msg_data.get("host_username") and msg_data.get("number_viewers"):
                    self.stateUpdate(self.TP_PLUGIN_STATES["latest_raid_name"]["id"], msg_data["host_username"])
                    self.stateUpdate(self.TP_PLUGIN_STATES["latest_raid_viewers"]["id"], str(msg_data["number_viewers"]))
                    self.stateUpdate(self.TP_PLUGIN_STATES["latest_raid_optional_message"]["id"], msg_data["optional_message"])

                

    def update_state(self):
        timer = 57

        while self.isConnected():
            if timer % 30 == 0: # update every 30s
                self.update_stream_info()
                self.update_followed_user()

            if timer >= 60:
                if self.kick.isUserLoggedIn:
                    self.kick_ws.send_ping() # keep ws alive
                    self.kick.update_emotes() # update emotes
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

    def is_diffent_account(self, email, password):
        token = KickSaveSession._loadToken()
        if token.get("user", False):
            token_email = token["user"]["email"]
            token_password = token["user"]["password"]

            return email != token_email or password != token_password
        return True

    @Plugin.onStart()
    def onStart(self, data):
        self.log.info(f"Connected to TP v{data.get('tpVersionString', '?')}, plugin v{data.get('pluginVersion', '?')}.")
        self.log.debug(f"Connection: {data}")

        self.state_usedefault()
        email = data["settings"][0]["email"]
        password = data["settings"][1]["password"]

        if email and password:
            is_different = self.is_diffent_account(email, password)
            if is_different:
                import os
                try:
                    self.log.info("Different account. removing old token file")
                    os.remove("./token.txt")
                except FileNotFoundError:
                    self.log.info("No token file found")

            self.kick = Kick(email, password)
            self.kick.handleLogin() # does login and automatically handle save session
            if (self.kick.isUserLoggedIn):
                self.kick.setData()
                self.update_thread.start()
                self.kick_ws = KickWebSockets(self.on_message, self.kick)
                self.kick_ws.run()
            else:
                self.disconnect() # Don't want the plugin to run if not logged in

    @Plugin.settingsRegister(name="email", type="text")
    @Plugin.addDoc("Email used to login to kick")
    def setting_email(self, value):
        # print("new setting email setting")
        ...

    @Plugin.settingsRegister(name="password", type="text", isPassword=True)
    @Plugin.addDoc("Password used to login to kick")
    def setting_password(self, value):
        # print("new pass setting")
        ...

    @Plugin.settingsRegister(name="chat buffer", type="text", default="5")
    @Plugin.addDoc("Number of states will be created to show chat history. eg 5 will show 5 latest messages")
    def setting_chat_buffer(self, value):
        self.chat_length = int(value)

    @Plugin.settingsRegister(name="logging", type="text", default="DEBUG")
    @Plugin.addDoc("Debugging level. eg DEBUG, INFO, WARNING, ERROR, CRITICAL")
    def set_logging(self, value):
        # self.setLogLevel(value)
        ...

    @Plugin.settingsRegister(name="Message Time format", type="text", default="%I:%M:%S %p")
    @Plugin.addDoc("Time format for chat message. help with formatting can be found here https://strftime.org/")
    def setting_time_format(self, value):
        self.time_format = value

    @Plugin.actionRegister(id="send_message", category="chat", name="Send Chat Message", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                           format="Send $[message]")
    @Plugin.addDoc("Send message to chat")
    @Plugin.data(id="message", type="text", label="Message to send to chat", default="Hello World!")
    def send_message(self, data):
        if self.kick is not None:
            response = self.kick.sendMessage(self.kick.encode_emotes(data["message"]), self.chatroom_id)
            if response.status_code == 200:
                self.update_message(response.json()["data"])

    @Plugin.actionRegister(id="clearChat", category="chat", name="Clear Chat", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                           format="Clear Chat")
    @Plugin.addDoc("Clear chat")
    def clear_chat(self, data):
        if self.kick is not None:
            self.kick.clearChat()

    @Plugin.actionRegister(id="setModerator", category="chat", name="Add or Remove Moderator", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                           format="$[option]$[username] as moderator")
    @Plugin.addDoc("Add or remove moderator")
    @Plugin.data(id="username", type="text", label="Username", default="")
    @Plugin.data(id="option", type="choice", label="Option", default="Add", valueChoices=["Add", "Remove"])
    def set_moderator(self, data):
        if self.kick is not None and data["username"] != "":
            self.kick.setModerator(data["username"], data["option"] == "Add")

    @Plugin.actionRegister(id="follow", category="chat", name="Follow or Unfollow User", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                           format="$[option]$[username]")
    @Plugin.addDoc("Follow or unfollow user")
    @Plugin.data(id="username", type="text", label="Username", default="")
    @Plugin.data(id="option", type="choice", label="Option", default="Follow", valueChoices=["Follow", "Unfollow"])
    def follow(self, data):
        if self.kick is not None and data["username"] != "":
            self.kick.follow(data["username"], data["option"] == "Follow")

    @Plugin.actionRegister(id="CreatePoll", category="chat", name="Create Poll", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                           format="Create Poll: $[question] duration: $[duration] result displayed for $[result_duration] with $[option1] $[option2] $[option3] $[option4] $[option5] $[option6]")
    @Plugin.addDoc("Create poll. requires at least 2 options")
    @Plugin.data(id="question", type="text", label="Question", default="")
    @Plugin.data(id="option1", type="text", label="Option 1", default="")
    @Plugin.data(id="option2", type="text", label="Option 2", default="")
    @Plugin.data(id="option3", type="text", label="Option 3", default="")
    @Plugin.data(id="option4", type="text", label="Option 4", default="")
    @Plugin.data(id="option5", type="text", label="Option 5", default="")
    @Plugin.data(id="option6", type="text", label="Option 6", default="")
    @Plugin.data(id="duration", type="choice", label="Duration", default="30", valueChoices=["30 seconds", "2 minutes", "3 minutes", "4 minutes", "5 minutes"])
    @Plugin.data(id="result_duration", type="choice", label="Result Duration", default="15 seconds", valueChoices=["15 seconds", "30 seconds", "2 minutes", "3 minutes", "4 minutes", "5 minutes"])
    def create_poll(self, data):
        if self.kick is not None:
            time_table = {"15 seconds": 15, "30 seconds": 30, "2 minutes": 120, "3 minutes": 180, "4 minutes": 240, "5 minutes": 300}
            options = [data["option1"], data["option2"], data["option3"], data["option4"], data["option5"], data["option6"]]

            question = data["question"]
            options = [option for option in options if option != ""]
            duration = time_table.get(data["duration"], 30)
            result_duration = time_table.get(data["result_duration"], 15)

            # print(question, options, duration, result_duration)

            self.kick.create_poll(question, options, duration, result_duration)

    @Plugin.actionRegister(id="VotePoll", category="chat", name="Vote Poll", prefix="",
                           format="Vote Poll: $[option]")
    @Plugin.addDoc("Vote poll 1-6 depending on the number of options in the poll")
    @Plugin.data(id="option", type="choice", label="Option", default="Option 1", valueChoices=["Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Option 6"])
    def vote_poll(self, data):
        if self.kick is not None:
            option_table = {"Option 1": 0, "Option 2": 1, "Option 3": 2, "Option 4": 3, "Option 5": 4, "Option 6": 5}
            self.kick.vote_poll(option_table[data["option"]])

    @Plugin.actionRegister(id="EndPoll", category="chat", name="End Poll", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                            format="End Poll")
    @Plugin.addDoc("Delete / Cancel current active poll")
    def end_poll(self, data):
        if self.kick is not None:
            self.kick.end_poll()

    @Plugin.actionRegister(id="tempBan", category="chat", name="Temporary Ban User", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                           format="Temporary Ban: $[username] for $[duration]minutes with reason: $[reason]")
    @Plugin.addDoc("Temporary ban specific user with reason and duration in minutes")
    @Plugin.data(id="username", type="text", label="Username", default="")
    @Plugin.data(id="duration", type="text", label="Duration", default="1")
    @Plugin.data(id="reason", type="text", label="Reason", default="")
    def temp_ban(self, data):
        if self.kick is not None and data["username"] != "":
            try:
                duration = int(data["duration"])
            except ValueError:
                duration = 1
            
            self.kick.ban(username=data["username"], duration=duration, reason=data["reason"])

    @Plugin.actionRegister(id="ban", category="chat", name="Ban", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                            format="Ban: $[username] with reason: $[reason]")
    @Plugin.addDoc("Permanently ban specific user")
    @Plugin.data(id="username", type="text", label="Username", default="")
    @Plugin.data(id="reason", type="text", label="Reason", default="")
    def ban(self, data):
        if self.kick is not None and data["username"] != "":
            self.kick.ban(username=data["username"], reason=data["reason"], permanent=True)

    @Plugin.actionRegister(id="unban", category="chat", name="Unban", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                            format="Unban: $[username]")
    @Plugin.addDoc("Unban specific user")
    @Plugin.data(id="username", type="text", label="Username", default="")
    def unban(self, data):
        if self.kick is not None and data["username"] != "":
            self.kick.unban(username=data["username"])

    @Plugin.actionRegister(id="startRaid", category="chat", name="Start Raid", prefix=TP_PLUGIN_CATEGORIES["chat"]["name"],
                            format="Start Raid/Host $[username]")
    @Plugin.addDoc("Start Raid/Host specific user")
    @Plugin.data(id="username", type="text", label="Username", default="")
    def start_raid(self, data):
        if self.kick is not None and data["username"] != "":
            self.kick.host(username=data["username"])

    def onError(self, data):
        self.log.debug(f"Error: {data}", exc_info=True)

    def on_tpclose(self, data):
        self.log.info("TP closed")
        self.disconnect()
        self.update_thread.join()

        self.kick_ws.close()
        
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
    TP_PLUGIN_EVENTS = kicktp.TP_PLUGIN_EVENTS

    
    

    