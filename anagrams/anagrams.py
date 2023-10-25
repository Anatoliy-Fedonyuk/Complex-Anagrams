"""This file is the entry point application Complex Anagrams"""
from functools import lru_cache
from loguru import logger


logger.add('debug.log', format='{time} {level} {message}', level='DEBUG')
logger.info(f"[INFO] Start working application {__name__} !")


@lru_cache(maxsize=1024)
def get_anagram(text: str) -> str:
    """
    Function to create complex anagrams with use Lru cache and
    handling of all exceptions that arise
    :param text: string input
    :return: string
    """
    try:
        if not isinstance(text, str):
            logger.error("[ERROR] TypeError - only a string is expected.")
            raise TypeError('--Only a string can be used as input!--')
        if text == "":
            logger.error("[ERROR] ValueError - a string is empty.")
            raise ValueError('--Anagram do not make sense, string is empty--')
        words = text.split()
        if all(w.isdigit() for w in words):
            logger.error("[ERROR] ValueError - a string is empty.")
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
    except Exception as e:
        logger.error(f"[ERROR] Unexpected error occurred: {e}")
        raise # Re-raise the exception for further handling


if __name__ == '__main__':
    cases = [("abcd efgh", "dcba hgfe"),
             ('da1234SeD 4321', 'De1234Sad 4321')]
    for text, reversed_text in cases:
        assert get_anagram(text) == reversed_text
        print("Assertion - is True")
