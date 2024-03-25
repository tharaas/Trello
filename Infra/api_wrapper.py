import requests


class APIWrapper:

    def __init__(self):
        self.response = None
        self.my_request = requests

    def api_get_request(self, url):
        self.response = self.my_request.get(url)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code
