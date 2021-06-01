from .api.here_api import HereApi
from .message_grandpy import (
    grandpy_error, grandpy_response,
    grandpy_story, grandpy_no_description
    )
from .parser.parser_sentence import ParserSentence
from .api.wiki_api import WikiApi
from config import HERE_API_KEY

from random import choice


class Grandpy:
    """
    Grandpy retrun response for frontend.

    ....

    Method
    ------
    get_response(sentence):
        Take as parameter a user_input from Front-end
        return a dictionary
    """
    def get_response(self, sentence):
        """
        Use ParserSentence() to clean user_input
        Use HereApi() to get address, lat and lng
        Use WikiApi() to get a description
        Use message_grandpy.py for choice random GrandPy message
        """
        user_message = ParserSentence().clean(sentence)
        data_here_api = HereApi().get_request(user_message)
        if not data_here_api:
            return {
                "grandpy_error": choice(grandpy_error)
                }
        else:
            data_wiki_api = WikiApi().get_description(user_message)
            if not data_wiki_api:
                return {
                    "grandpy_address": choice(grandpy_response),
                    "address": data_here_api["address"],
                    "grandpy_descript": "",
                    "descriptif": choice(grandpy_no_description),
                    "lat": data_here_api["lat"],
                    "lng": data_here_api["lng"],
                    "apikey": HERE_API_KEY
                }
            else:
                return {
                    "grandpy_address": choice(grandpy_response),
                    "address": data_here_api["address"],
                    "grandpy_descript": choice(grandpy_story),
                    "descriptif": data_wiki_api,
                    "lat": data_here_api["lat"],
                    "lng": data_here_api["lng"],
                    "apikey": HERE_API_KEY
                }
