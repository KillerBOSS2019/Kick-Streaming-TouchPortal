from curl_cffi import requests
from . KickSession import KickSaveSession
from TouchPortalAPI.logger import Logger
import re

logger = Logger(__name__)

class KickBase(KickSaveSession):
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        # "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "accept-language": "en-US",
        "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        "sec-ch-ua-mobile": "?0",
        "Authorization": "Bearer null",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "Cookie": "",
        "X-Xsrf-Token": ""
    })

    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.cookie_jar = {}

    def generate_cookie(self):
        if self.cookie_jar:
            cookie = "; ".join([f"{key}={value}" for key, value in self.cookie_jar.items()])
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
                    self.cookie_jar[cookie_name] = cookie_value
                    self.session.headers.update({"Cookie": self.generate_cookie()})
                self.save_cookie(self.cookie_jar)

            if "XSRF-TOKEN" in self.cookie_jar:
                self.session.headers.update({"X-XSRF-TOKEN": self.cookie_jar["XSRF-TOKEN"]})
    
    def is_success_status_code(self, status_code):
        return 200 <= status_code < 300

    def request(self, url, method="GET", data=None, header=None, as_body=False):
        logger.info(f"Request --> method:{method} url:{url}")
        headers = self.session.headers
        if header:
            headers.update(header)
        if method == "GET":
            data = self.session.get(url, data=data, impersonate="chrome101", headers=headers)
        elif method == "POST":
            if as_body:
                data = self.session.post(url, body=data, impersonate="chrome101", headers=headers)
            else:
                data = self.session.post(url, data=data, impersonate="chrome101", headers=headers)
        elif method == "DELETE":
            data = self.session.delete(url, data=data, impersonate="chrome101", headers=headers)
        elif method == "PUT":
            data = self.session.put(url, data=data, impersonate="chrome101", headers=headers)

        if 200 <= data.status_code < 300:
            # Update header with response header
            self.set_headers(data.headers)
            logger.info(f"Request <-- method:{method} url:{url} status_code:{data.status_code}")
        else:
            logger.info(f"Request <-- method:{method} url:{url} status_code:{data.status_code} error:{data.text}")

        return data