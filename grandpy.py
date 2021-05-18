from parser_sentence import ParserSentence
from here_api import HereApi
from wiki_api import WikiApi

class Grandpy:

    def get_response(self, sentence):
        data = {}
        par = ParserSentence()
        user_message = par.clean(sentence)
        data_here_api = HereApi().get_request(user_message)
        if data_here_api == None:
            data = {
                "grandpy_address": "Désolé mon petit je n'ai pas compris ta demande"
                }
            return data
        else:
            data_wiki_api = WikiApi().get_description(user_message)
            data = {
                "grandpy_address": "Bien sûr mon poussin ! La voici : ",
                "address": data_here_api["address"],
                "grandpy_descript": "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? ",
                "descriptif": data_wiki_api,
                "lat": data_here_api["lat"],
                "lng": data_here_api["lng"]
            }
            return data



# sentence = "openclassrooms"
# response = Grandpy().get_response(sentence)
# print(response)
