import re


class UrlAPI:

    def get_board_id(self, url):
       return re.search(r'/b/([A-Za-z0-9]+)/', url).group(1)
