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

    def create_issue(self, summery, description, project_key, issue_type="Bug"):
        issue_dict = {
            'project': {'key': project_key},
            'summary': f'failed test: {summery}',
            'description': description,
            'issuetype': {'name': issue_type},
        }
        new_issue = self.auth_jira.create_issue(fields=issue_dict)
        return new_issue.key

'''
        try:
            self.driver.quit()
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="test-reports"))
        except AssertionError as e:
            jira_report = JiraReport()
            error_message = f"Assertion failed: {e}"
            issue_summary = "Test Assertion Failure"
            issue_description = f"Test failed with the following error: {error_message}"
            jira_report.create_issue(issue_summary, issue_description, jira_report.jira_project_key)
            print("Issue Created")
            raise e
'''