from Utils.read_from_env_file_like_username_password import Credentials


class BoardPageAPI:
    def __init__(self, api_wrapper):
        self.api_wrapper = api_wrapper
        self.credential = Credentials()
        self.url = self.credential.get_url()

    def get_board_from_api(self, id):
        board_url_id = f"{self.url}/boards/{id}"
        response = self.api_wrapper.api_get_request(board_url_id)
        if response.ok:
            data = response.json()
            board_name = data["name"]
            return board_name
        else:
            return f"Error: {response.status_code}"

    def delete_board_from_api(self, id):
        board_url_id = f"{self.url}/boards/{id}"
        response = self.api_wrapper.api_delete_request(board_url_id)
        if response.ok:
            return True
        else:
            return f"Error: {response.status_code}"
