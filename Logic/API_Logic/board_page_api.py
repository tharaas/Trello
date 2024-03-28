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

    def search_board_name_in_search_api(self, search_board_name):
        response = self.api_wrapper.api_search_get_request(self.url, search_board_name)
        if response.ok:
            data = response.json()
            boards = data.get('boards', [])

            # Check if the list of boards is non-empty
            if boards:
                return True
            else:
                return False
        else:
            return f"Error: {response.status_code}"

    def create_card_from_api(self, list_name):
        card_url_id = f"{self.url}/cards"
        response = self.api_wrapper.api_post_request(card_url_id, list_name)
        return response
