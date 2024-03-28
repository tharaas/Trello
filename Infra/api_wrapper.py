import requests
from Utils.read_from_env_file_like_username_password import Credentials


class APIWrapper:

    #The APIWrapper obtains URLs from the API Logic to perform tasks such as fetching board or list data.
    def __init__(self):
        self.response = None
        self.my_request = requests
        self.credential = Credentials()
        self.token = self.credential.get_token()
        self.key = self.credential.get_key()

    def get_query(self):
        query = {
            'key': self.key,
            'token': self.token
        }
        return query

    #post request needs name
    def get_query_post(self, name):
        query = {
            'idList': name,
            'key': self.key,
            'token': self.token
        }
        return query

    def get_headers(self):
        headers = {
            "Accept": "application/json"
        }
        return headers

    def get_query_search(self, search_text):
        query = {
            'query': search_text,
            'key': self.key,
            'token': self.token
        }
        return query

    def api_get_request(self, url):
        self.query = self.get_query()
        self.headers = self.get_headers()
        self.response = self.my_request.get(url, headers=self.headers, params=self.query)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_search_get_request(self, url, search_text):
        url_search = f"{url}/search"
        self.query = self.get_query_search(search_text)
        self.headers = self.get_headers()
        self.response = self.my_request.get(url_search , headers=self.headers, params=self.query)
        if self.response.ok:
            return self.response
        else:
            return False

    def api_post_request(self, url, name):
        self.query_post = self.get_query_post(name)
        self.headers = self.get_headers()
        self.response = self.my_request.post(url, headers=self.headers, params=self.query_post)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_delete_request(self, url):
        self.query = self.get_query()
        self.headers = self.get_headers()
        self.response = self.my_request.delete(url, params=self.query)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_put_request(self, url):
        self.response = self.my_request.put(url, params=self.query)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code
