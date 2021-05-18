from config import apiKey
import requests



class HereApi:

    def get_request(self, sentence_parser):

        url = "https://geocode.search.hereapi.com/v1/geocode"
        params = {
            "apiKey": apiKey,
            "q" : sentence_parser
        }
        response = requests.get(url, params)
        if response.ok:
            response_json = response.json()
            
            try:
                infos_api = response_json["items"]
                address = infos_api[0]["address"]["label"]
                lat = infos_api[0]["position"]["lat"]
                lng = infos_api[0]["position"]["lng"]
                return {"address": address,
                "lat": lat,
                "lng": lng 
                }
            except IndexError:
                return None
                




# text = HereApi().get_request("parc des princes")
# print(text["address"])
# print(text["lat"], text["lng"])





