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
            raise ValueError("URL environment variable is not set")
        return url

    def get_token(self):
        token = os.getenv("TOKEN")
        if token is None:
            raise ValueError("TOKEN environment variable is not set")
        return token

    def get_key(self):
        key = os.getenv("KEY")
        if key is None:
            raise ValueError("KEY environment variable is not set")
        return key

    def get_jira_token(self):
        jira_token = os.getenv("JIRA_TOKEN")
        if jira_token is None:
            raise ValueError("JIRA_TOKEN environment variable is not set")
        return jira_token

    def get_jira_url(self):
        jira_url = os.getenv("JIRA_URL")
        if jira_url is None:
            raise ValueError("JIRA_URL environment variable is not set")
        return jira_url

    def get_jira_email(self):
        jira_email = os.getenv("JIRA_EMAIL")
        if jira_email is None:
            raise ValueError("Email environment variable is not set")
        return jira_email

    def get_jira_project_key(self):
        jira_project_key = os.getenv("JIRA_PROJECT_KEY")
        if jira_project_key is None:
            raise ValueError("jira project key environment variable is not set")
        return jira_project_key
