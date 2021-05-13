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
        response_json = response.json()
        infos_api = response_json["items"]
        self.address = infos_api[0]["address"]["label"]
        self.lat = infos_api[0]["position"]["lat"]
        self.lng = infos_api[0]["position"]["lng"]
        return {"address": self.address,
                "lat": self.lat,
                "lng": self.lng 
                }

texte = "le piton de la fournaise"
text = HereApi().get_request(texte)
print(text)





