from .stop_word import stop_word
import re


class ParserSentence:
    """
    Class for cleaning up sentences
    ...
    Attribute
    ---------
    sentence : str
        user_input from front-end

    Methods
    ---------
    remove_uppercase(sentence):
    remove_punctuation(sentence):
    extract_word(sentence):
    clean(sentence):
    """

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
        """
        Method to extract unnecessary words in the sentence
        take as parameter a sentence
        use a stop_word.py
        """
        index_list = []
        stop_word_list = stop_word
        sentence_list = sentence.split()
        sentence_list_substitute = [
            word for word in sentence_list if word not in stop_word_list
            ]
        for word in sentence_list_substitute:
            if word in sentence_list:
                # get the indexes of the remaining words
                index_list.append(sentence_list.index(word))
        if len(index_list) >= 1:
            first_index = index_list[0]
            last_index = index_list[-1]
            # get the all words from the sentence_list
            # using first and last index from index_list
            sentence_clear = " ".join(sentence_list[first_index:last_index+1])
            return sentence_clear
        else:
            return None

    def clean(self, sentence):
        sentence = self.remove_uppercase(sentence)
        sentence = self.remove_punctuation(sentence)
        sentence = self.extract_word(sentence)
        return sentence
