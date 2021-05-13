import requests


class WikiApi:

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng
        self.title = ""

    def get_request_by_position(self):

        url = "https://fr.wikipedia.org/w/api.php?action=query"
        param = {
            "format": "json",
            "list": "geosearch",
            "gscoord": "{}|{}".format(self.lat, self.lng),
            "gsradius": "10",
            "gslimit": "10"
        }
        response = requests.get(url, param)
        response_json = response.json()
        self.title = response_json["query"]["geosearch"][0]["title"]
        return self.title


    def request_get_by_title(self):

        url = "https://fr.wikipedia.org/w/api.php"
        param = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "titles": self.title,
            "formatversion": 2,
            "exsentences": 2,
            "explaintext": 1,
            "exsectionformat": "plain"
        }
        response_json = requests.get(url, param).json()
        description = response_json["query"]["pages"][0]
        return description["extract"]

    def get_description(self):
        self.get_request_by_position()
        return self.request_get_by_title()
        
lat = 48.8414
lng = 2.25308
description = WikiApi(lat, lng).get_description()


def request_get_by_title(title):

    url = "https://fr.wikipedia.org/w/api.php?action=query"
    param = {
        "prop": "search",
        "srsearch": "taj mahal",
        "format":"json"
    }
    response_json = requests.get(url, param).json()
    description = response_json["query"]
    print(description)

title = "parc des princes"
request_get_by_title(title)