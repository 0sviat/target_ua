"""
TARGET UKTAINIAN VERSION GAME MODULE
"""
from typing import List
import random


def generate_grid() -> List[str]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. ['ч', 'щ', 'й', 'а', 'е']
    """
    letters = [ 'б', 'в', 'г', 'ґ', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т',\
     'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'й', 'а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я', 'ь']
    grid_letters = []
    while len(grid_letters) < 5 :
        new_letter = random.choice(letters)
        if new_letter not in new_letter:
            grid_letters.append(new_letter)
    return grid_letters


def list_of_letter_tuples(word):
    """
    str -> list(tuple(str,int))
    Create list of tuples with letter of the word  and its number of occurrences
    Letter will be displayed in alphabetic order in lower registor
    If there are other symbols in a word(1,2,%,&...) they will be omitted
    >>> list_of_letter_tuples('potato')
    [('a', 1), ('o', 2), ('p', 1), ('t', 2)]
    [('a', 1), ('e', 1), ('l', 1), ('p', 2)]
    >>> list_of_letters_tuples('PyThOn')
    [('h', 1), ('n', 1), ('o', 1), ('p', 1), ('t', 1), ('y', 1)]
    >>> list_of_letter_tuples('ERROR')
    [('e', 1), ('o', 1), ('r', 3)]
    """
    letters_list = []
    word = word.lower()
    for ord_index in range(97, 123):
        # check by letter ACS if it is in a word
        if chr(ord_index) in word:
            letters_list.append(((chr(ord_index), word.count(chr(ord_index)))))
    return letters_list
# print(list_of_letter_tuples('azAZ'))

def check_user_words(user_words, language_part, letters, dict_of_words):


def get_words(file_with_words: str, letters: List[str]):
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    words_from_dictionary = []
    # open file with words and read it line by line
    with open(file_with_words, mode='r', encoding='utf-8') as dictionary:
        for word in dictionary:
            # read new word from the file
            current_word = word.read()
            # if a word corresponds to the rules add it to the list
            if rule_correct_word(current_word,letters):
                words_from_dictionary.append(current_word)

    return words_from_dictionary


def rule_correct_word(word, letters):
    """
    (str, list) -> bool
    Check if word fits game rules:
    Starts with one of letters
    Word includes less then 6 words
    """


def results():
    """
    Return results of the game
    """
    letters = generate_grid()
