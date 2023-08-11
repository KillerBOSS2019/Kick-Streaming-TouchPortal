import websocket
import json
from TouchPortalAPI.logger import Logger

logger = Logger(__name__)

class KickWebSockets():
    WS_ADDRESS = "wss://ws-us2.pusher.com/app/eb1d5f283081a78b932c?protocol=7&client=js&version=7.6.0&flash=false"

    def __init__(self, onMessage, kick) -> None:
        self.ws = websocket.WebSocketApp(self.WS_ADDRESS, on_message=onMessage, on_close=self.on_close, on_error=self.onError)
        self.kick = kick

    def on_close(self, ws, close_status_code, close_msg):
        print(f"WS Closed: {close_status_code} {close_msg}")

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

    def close(self):
        self.ws.close()

    def run(self):
        # Thread(target=self.ws.run_forever).start()
        self.ws.run_forever()