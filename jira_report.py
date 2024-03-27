from jira import JIRA
from Utils.read_from_env_file_like_username_password import Credentials


class JiraReport:

    def __init__(self):
        self.credentials = Credentials()
        self.jira_token = self.credentials.get_jira_token()
        self.jira_url = self.credentials.get_jira_url()
        self.jira_email = self.credentials.get_jira_email()
        self.jira_project_key = self.credentials.get_jira_project_key()
        self.auth_jira = JIRA(basic_auth=(self.jira_email, self.jira_token), options={'server': self.jira_url})

    #create an issue in jira
    def create_issue(self, summery, description, issue_type="Bug"):
        issue_dict = {
            'project': {'key': self.jira_project_key},
            'summary': f'failed test: {summery}',
            'description': description,
            'issuetype': {'name': issue_type},
        }
        new_issue = self.auth_jira.create_issue(fields=issue_dict)
        return new_issue.key