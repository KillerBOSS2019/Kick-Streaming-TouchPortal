import base64
import json

class KickSaveSession:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def _saveToken(headers):
        with open("token.txt", "w") as f:
            f.write(base64.b64encode(json.dumps(headers).encode("utf-8")).decode("utf-8"))

    @staticmethod
    def _loadToken() -> dict:
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