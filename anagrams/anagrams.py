"""This file is the entry point application Complex Anagrams"""
from functools import lru_cache
from loguru import logger


@lru_cache(maxsize=1024)
def get_anagram(text: str) -> str:
    """
    Function to create complex anagrams with use Lru cache and
    handling of all exceptions that arise
    :param text: string input
    :return: string
    """
    if not isinstance(text, str):
        raise TypeError('--Only a string can be used as input!--')
    if text == "":
        raise ValueError('--Anagram do not make sense, string empty--')
    words = text.split()
    if all(w.isdigit() for w in words):
        raise ValueError('--Anagram do not make sense in your string only digits--')
    reversed_w = []
    for word in words:
        no_letter = [(i, ch) for i, ch in enumerate(word) if not ch.isalpha()]
        word = "".join(ch for ch in word if ch.isalpha())
        revers = word[::-1]
        for i, ch in no_letter:
            revers = f'{revers[:i]}{ch}{revers[i:]}'
        reversed_w.append(revers)
    return ' '.join(reversed_w)


if __name__ == '__main__':
    cases = [("abcd efgh", "dcba hgfe"),
             ('da1234SeD 4321', 'De1234Sad 4321')]
    for text, reversed_text in cases:
        assert get_anagram(text) == reversed_text
        print("Assertion - is True")
