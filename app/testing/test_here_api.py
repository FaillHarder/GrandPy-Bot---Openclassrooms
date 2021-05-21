from ..grandpybot.api.here_api import HereApi
import json

mock_here_api = "app/testing/mock_resources/mock_here_api.json"

with open(mock_here_api, encoding="utf-8") as json_file:
    mock_response_here_api = json.load(json_file)


def test_method_request_here_api():
    result = HereApi().parse_address_lat_lng(mock_response_here_api)
    assert result == {
                "address": "Avenue du Piton de la Fournaise",
                "lat": -20.88334,
                "lng": 55.44244
                }
