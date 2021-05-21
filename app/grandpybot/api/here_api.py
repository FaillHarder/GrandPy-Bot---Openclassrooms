
import requests
apiKey = "sWGnfLzvhwaNV5-9-Kuf043yeX5GMy2byCllEXpFr4k"


class HereApi:

    def get_request(self, sentence_parser):

        url = "https://geocode.search.hereapi.com/v1/geocode"
        params = {
            "apiKey": apiKey,
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
