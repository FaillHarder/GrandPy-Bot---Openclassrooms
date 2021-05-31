from config import HERE_API_KEY

import requests


class HereApi:
    """
    Class make a request to here API
    Take as parameter a user_input parser by ParserSentence()
    Return a dictionary
    """

    def get_request(self, sentence_parser):

        url = "https://discover.search.hereapi.com/v1/discover"
        params = {
            "apiKey": HERE_API_KEY,
            "limit": 2,
            "at": "0,0",
            "q": sentence_parser
        }
        response = requests.get(url, params)
        if response.ok:
            response_json = response.json()
            return self.parse_address_lat_lng(response_json)

    def parse_address_lat_lng(self, data):

        try:
            infos_api = data["items"]
            address = infos_api[0]["address"]["label"]
            lat = infos_api[0]["position"]["lat"]
            lng = infos_api[0]["position"]["lng"]
            return {
                "address": address,
                "lat": lat,
                "lng": lng
                }
        except IndexError:
            return None


HereApi().get_request("parc des princes")
