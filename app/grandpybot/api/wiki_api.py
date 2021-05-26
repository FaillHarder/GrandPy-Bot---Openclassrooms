import requests


class WikiApi:

    def request_get_by_title(self, title):

        url = "https://fr.wikipedia.org/w/api.php?action=query"
        param = {
            "list": "search",
            "srsearch": title,
            "format": "json"
        }
        response = requests.get(url, param)
        if response.ok:
            response_json = response.json()
            return self.parse_pageid(response_json)

    def parse_pageid(self, data):
        try:
            self.pageid = data["query"]["search"][0]["pageid"]
            return self.pageid
        except IndexError:
            return None

    def request_get_by_pageid(self):

        url = "https://fr.wikipedia.org/w/api.php?action=query"
        param = {
            "prop": "extracts",
            "pageids": self.pageid,
            "formatversion": 2,
            "exsentences": 2,
            "explaintext": 1,
            "exsectionformat": "plain",
            "format": "json"
        }
        response = requests.get(url, param)
        if response.ok:
            response_json = response.json()
            return self.parse_extract(response_json)

    def parse_extract(self, data):
        try:
            return data["query"]["pages"][0]["extract"]
        except KeyError:
            return None

    def get_description(self, title):
        pageid = self.request_get_by_title(title)
        if pageid is None:
            return None
        else:
            description = self.request_get_by_pageid()
            return description