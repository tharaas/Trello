import os
from dotenv import load_dotenv

load_dotenv()


class Credentials:

    def get_email(self):
        email = os.getenv("EMAIL_TXT")
        if email is None:
            raise ValueError("EMAIL_TXT environment variable is not set")
        return email

    def get_password(self):
        password = os.getenv("PASSWORD")
        if password is None:
            raise ValueError("PASSWORD environment variable is not set")
        return password

    def get_url(self):
        url = os.getenv("URL")
        if url is None:
            raise ValueError("bio text environment variable is not set")
        return url

    def change_bio(self):
        bio_text = os.getenv("NEW_BIO_TEXT")
        if bio_text is None:
            raise ValueError("bio text environment variable is not set")
        return bio_text

    def get_token(self):
        token = os.getenv("TOKEN")
        if token is None:
            raise ValueError("token environment variable is not set")
        return token

    def get_key(self):
        key = os.getenv("KEY")
        if key is None:
            raise ValueError("key environment variable is not set")
        return key

    def new_title_for_board(self):
        board_title = os.getenv("BOARD_TITLE")
        if board_title is None:
            raise ValueError("key environment variable is not set")
        return board_title
