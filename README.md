# Complex Anagrams


### This is a small program for creating Complex Anagrams from individual strings and entire text fragments.

#### The algorithm for creating anagrams in the program is as follows - all digital and special characters will remain exactly in their positions, where they were! And all letter characters in a separate word change their position index in the word to the opposite. That is, if the letter was the first in the word (without taking into account non-letter characters), then after the anagram it will become the last, if it was the second letter in the word, it will become the penultimate, etc.

#### The program may be useful, for example, to students for educational purposes. The program is written in Python 3.11, lru_cache from the functools library is used to optimize the algorithm, the functionality of the program is tested using the unittest test-framework, all dependencies are stored in requirements.txt
