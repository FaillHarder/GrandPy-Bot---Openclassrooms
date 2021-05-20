import json
from wiki_api import WikiApi


mock_url_by_title = "mock_wiki_search_by_title.json"
mock_url_by_pageid = "mock_wiki_search_by_pageid.json"

with open(mock_url_by_title, encoding="utf-8") as json_file:
    mock_response_by_tile = json.load(json_file)

with open(mock_url_by_pageid, encoding="utf-8") as json_file:
    mock_response_by_pageid = json.load(json_file)


def test_method_request_get_by_title():
    result = WikiApi().parse_pageid(mock_response_by_tile)
    assert result == 164149



test_method_request_get_by_title()