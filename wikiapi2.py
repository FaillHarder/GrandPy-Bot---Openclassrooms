import requests

def request_get_by_title(title):

    url = "https://fr.wikipedia.org/w/api.php?action=query"
    param = {
        "list": "search",
        "srsearch": title,
        "format":"json"
    }
    response_json = requests.get(url, param).json()
    pageid = response_json["query"]["search"][0]["pageid"]
    return pageid


def request_get_by_pageid(pageid):

    url = "https://fr.wikipedia.org/w/api.php?action=query"
    param = {
        "prop": "extracts",
        "pageids": pageid,
        "formatversion": 2,
        "exsentences": 2,
        "explaintext": 1,
        "exsectionformat": "plain",
        "format":"json"
    }
    response_json = requests.get(url, param).json()
    description = response_json["query"]
    return description

title = "piton de la fournaise"
pageid = request_get_by_title(title)
article = request_get_by_pageid(pageid)
print(article["pages"][0]["extract"])