import requests

def request_get_by_title(title):

        url = "https://fr.wikipedia.org/w/api.php?action=query"
        param = {
            "list": "search",
            "srsearch": title,
            "format":"json"
        }
        response = requests.get(url, param)
        if response.ok:
            response_json = response.json()
            try:
                pageid = response_json["query"]["search"][0]["pageid"]
                return pageid
            except IndexError:
                return None


test = request_get_by_title("sdf")
print(test)
