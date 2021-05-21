from .stop_word import stop_word
import re


class ParserSentence:

    def __init__(self):
        self.sentence = None

    def remove_uppercase(self, sentence):
        return sentence.lower()

    def remove_punctuation(self, sentence):
        sentence = sentence.replace("'", " ")
        sentence = sentence.replace("-", " ")
        sentence = re.sub(r'[^\w\s]', '', sentence)
        return sentence

    def extract_word(self, sentence):
        liste_index = []
        stop_word_list = stop_word
        sentence_list = sentence.split()
        sentence_list_substitute = [
            word for word in sentence_list if word not in stop_word_list
            ]
        for word in sentence_list_substitute:
            if word in sentence_list:
                liste_index.append(sentence_list.index(word))
        if len(liste_index) >= 1:
            first_index = liste_index[0]
            last_index = liste_index[-1]
            sentence_clear = " ".join(sentence_list[first_index:last_index+1])
            return sentence_clear
        else:
            return None

    def clean(self, sentence):
        sentence = self.remove_uppercase(sentence)
        sentence = self.remove_punctuation(sentence)
        sentence = self.extract_word(sentence)
        return sentence
