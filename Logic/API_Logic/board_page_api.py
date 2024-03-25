import random

import requests

from Utils.read_from_env_file_like_username_password import Credentials


class BoardPageAPI:
    def __init__(self,  api_wrapper):
        self.api_wrapper = api_wrapper
        self.credentials = Credentials()
        self.url = self.credentials.get_url()
        self.api_key = self.credentials.get_key()
        self.api_token = self.credentials.get_token()

    def get_board_from_api(self, title):
        headers = {
            'Accept': 'application/json',
        }
        params = {
            'key': self.api_key,
            'token': self.api_token
        }
        board_url = f"{self.url}/boards/{title}"
        response = self.api_wrapper.api_get_request(board_url)
        if response.ok:
            data = response.json()
            return data
        else:
            return f"Error: {response.status_code}"
