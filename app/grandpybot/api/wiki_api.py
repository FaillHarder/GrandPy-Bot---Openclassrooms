import requests


class WikiApi:
    """
    Class make a request to wiki API
    Return a description
    """

    def request_get_by_title(self, sentence_parser):
        """
        Make a first request,
        take as parameter a user_input parser by ParserSentence()
        Return a pageID
        """

        url = "https://fr.wikipedia.org/w/api.php?action=query"
        param = {
            "list": "search",
            "srsearch": sentence_parser,
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
        """
        Make a second request,
        take as parameter the pageID
        Return a description
        """

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
        """
        Method uses a double request to return a description
        """
        pageid = self.request_get_by_title(title)
        if not pageid:
            return None
        else:
            description = self.request_get_by_pageid()
            return description
