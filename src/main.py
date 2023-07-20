from kick import Kick
from Plugin import Plugin

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

    TP_PLUGIN_STATES = {}

    TP_PLUGIN_EVENTS = {}

    def __init__(self):
        super().__init__(self.PLUGIN_ID, autoClose=True)
        self.email = ""
        self.password = ""

    @Plugin.settingRegister(name="email", type="text")
    def email(self, value):
        self.kick.email = value

    @Plugin.settingRegister(name="password", type="text", isPassword=True)
    def password(self, value):
        self.kick.password = value