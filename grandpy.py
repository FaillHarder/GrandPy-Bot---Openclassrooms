from here_api import HereApi
from message_grandpy import grandpy_error, grandpy_response, grandpy_story
from parser_sentence import ParserSentence
from wiki_api import WikiApi

from random import choice


class Grandpy:

    def get_response(self, sentence):
        data = {}
        par = ParserSentence()
        user_message = par.clean(sentence)
        data_here_api = HereApi().get_request(user_message)
        if data_here_api == None:
            data = {
                "grandpy_error": choice(grandpy_error)
                }
            return data
        else:
            data_wiki_api = WikiApi().get_description(user_message)
            data = {
                "grandpy_address": choice(grandpy_response),
                "address": data_here_api["address"],
                "grandpy_descript": choice(grandpy_story),
                "descriptif": data_wiki_api,
                "lat": data_here_api["lat"],
                "lng": data_here_api["lng"]
            }
            return data
