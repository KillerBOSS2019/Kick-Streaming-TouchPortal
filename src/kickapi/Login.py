from . Base import KickBase
from . Kick2FA import Kick2FA
from tkinter import messagebox
from TouchPortalAPI.logger import Logger

logger = Logger(__name__)


class KickLogin(KickBase):
    BASE_URL = "https://kick.com/"

    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.retry = True

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
            logger.info("Failed to get token provider.")
            return False

        data = {
            "email": self.email,
            "password": self.password,
            "isMobileRequest": True,
            tokenProvider["nameFieldName"]: "",
            tokenProvider["validFromFieldName"]: tokenProvider["encryptedValidFrom"],
        }

        if authCode is not None:
            data["one_time_password"] = authCode

        url = self.BASE_URL + "mobile/login"
        response = self.request(url, method="POST", data=data)

        try:
            jsonResponse = response.json()

            if jsonResponse["2fa_required"]:
                if self.retry:
                    self.retry = False

                    kick2fa = Kick2FA()
                    authCode = kick2fa.getPasscode()
                    
                    return self.login(authCode=authCode)
        except Exception as e:
            logger.info(f"Error has occured: {e}")

        if self.is_success_status_code(response.status_code):
            self.session.headers.update({"Authorization": f"Bearer {response.json()['token']}"})
            self._saveToken({"Authorization": response.json()['token'], "user": {"email": self.email, "password": self.password}})
            if data.get("one_time_password", None):
                messagebox.showinfo("Success", "Login success")

            return True
        
        if "one_time_password" in data:
            messagebox.showwarning("Error", "Login failed")
        return False