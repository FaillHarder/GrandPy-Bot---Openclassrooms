from stop_word import stop_word
import re



class Parser:
    def __init__(self):
        self.sentence = None


    def remove_uppercase(self, sentence):
        return sentence.lower()


    def remove_punctuation(self, sentence):
        sentence = sentence.replace("'", " ")
        sentence = sentence.replace("-", " ")
        sentence = re.sub(r'[^\w\s]','',sentence)
        return sentence

    def remove_extra_space(self, sentence):
        sentence.replace("  ", " ")
        return sentence

    def extract_word(self, sentence):
        stop_word_list = stop_word
        sentence_list = sentence.split()
        sentence_list = [
            word for word in sentence_list if word not in stop_word_list
            ]
        return sentence_list


    def clean(self, sentence):
        sentence = self.remove_uppercase(sentence)
        sentence = self.remove_punctuation(sentence)
        sentence = self.remove_extra_space(sentence)
        sentence = self.extract_word(sentence)
        return sentence
