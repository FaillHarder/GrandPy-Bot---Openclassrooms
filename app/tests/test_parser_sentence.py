from typing import Sequence
from parser_sentence import ParserSentence
import re


def test_method_remove_uppercase():
    result = ParserSentence().remove_uppercase("SALUT")
    assert result == "salut"

def test_method_remove_punctuation():
    sentence = "salut! est-ce que ça va' ?"
    result = ParserSentence().remove_punctuation(sentence)
    assert result == "salut est ce que ça va  "

def test_method_extract_word():
    sentence = "salut grandpy ou se trouve le parc des princes"
    result = ParserSentence().extract_word(sentence)
    assert result == "parc des princes"

def test_method_clean():
    sentence = "Salut GrandPy! Ou se trouve le Parc des Princes ?"
    result = ParserSentence().clean(sentence)
    assert result == "parc des princes"

    
    