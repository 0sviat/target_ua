"""
TARGET GAME MODULE
"""
import random

def generate_grid():
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters = []
    letter_number = 0
    while letter_number < 9:
        if letter_number % 3 == 0:
            letters.append([])
        letters[-1].append(chr(random.randint(97, 122)))
        letter_number += 1
    return letters


def list_of_letter_tuples(word):
    """
    str -> list(tuple(str,int))
    Create list of tuples with letter of the word  and its number of occurrences
    Letter will be displayed in alphabetic order in lower registor
    If there are other symbols in a word(1,2,%,&...) they will be omitted
    >>> list_of_letter_tuples('potato')
    [('a', 1), ('o', 2), ('p', 1), ('t', 2)]
    [('a', 1), ('e', 1), ('l', 1), ('p', 2)]
    >>> list_of_letter_tuples('PyThOn')
    [('h', 1), ('n', 1), ('o', 1), ('p', 1), ('t', 1), ('y', 1)]
    >>> list_of_letter_tuples('ERROR')
    [('e', 1), ('o', 1), ('r', 3)]
    """
    letters_list = []
    word = word.lower()
    for ord_index in range(97, 123):
        # check by letter ACS if it is in a word
        if chr(ord_index) in word:
            letters_list.append((chr(ord_index), word.count(chr(ord_index))))
    return letters_list


def rule_correctness_word(word, letters):
    """
    (str, list) -> bool
    Check if word fits game rules:
    Word length in range [4,9]
    Word includes central letter
    All letters in the word are from grid board and itd
    number of occurrences in words is not more than in the grid board
    """
    central_letter = letters[4]
    # if word is too short or too long or do not include central letter
    if len(word) < 4 or len(word) > 9 or central_letter not in word:
        return False
    # create list[tuples] with letters in alphabet order and their number of occurrences in grid
    grid_letters = list_of_letter_tuples(' '.join(letters))
    # create list[tuple] with letters in alphabet order and their number of occurrences in word
    word_letters = list_of_letter_tuples(word)

    starting_index_in_grid_letters, index_in_word = 0, 0
    # check letters in the word one by one
    while index_in_word < len(word_letters):
        # check if current letter from a word is in grid
        for i in range(starting_index_in_grid_letters, len(grid_letters) + 1):
            # if we have checked all letters from grid but there still are letters in word
            if i == len(grid_letters):
                return False
            if word_letters[index_in_word][0] == grid_letters[i][0]:
                # then check letter's number of occurrences in the word
                if word_letters[index_in_word][1] <= grid_letters[i][1]:
                    starting_index_in_grid_letters = i + 1
                    # change starting letter to next by the alphabets in grid letters
                    break
                return False
        index_in_word += 1  # change letter in word_letter_list to next one
    return True

def get_words(file_with_words: str, letters):
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    words_from_dictionary = []
    # open file with words and read it line by line
    with open(file_with_words, mode='r', encoding='utf-8') as dictionary:
        for word in dictionary:
            # read new word from the file with no symbol new line and in lower format
            current_word = word.strip().lower()
            # if a word corresponds to the rules add it to the list
            if rule_correctness_word(current_word, letters):
                words_from_dictionary.append(current_word)

    return words_from_dictionary

def get_user_words():
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    list_of_player_worlds = input().split()
    return list_of_player_worlds


def get_pure_user_words(user_words, letters, words_from_dict):
    """
    (list, list, list) -> list
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    wrong_words = []
    for word in user_words:
        if rule_correctness_word(word, letters) and (word not in words_from_dict):
            wrong_words.append(word)
    return wrong_words


def results():
    """
    Return results of the game
    """
    letters = generate_grid()
    letters = letters[0] + letters[1] + letters[2]
    right_words_number = 0
    dict_words = get_words('en', letters)
    user_words = get_user_words()
    wrong_words = get_pure_user_words(user_words, letters, dict_words)

    for one_user_word in user_words:
        if one_user_word in dict_words:
            right_words_number += 1
            dict_words.remove(one_user_word)

    print(right_words_number)
    print(dict_words)
    print(wrong_words)
    with open ('results.txt', 'w', encoding='utf-8') as result_text:
        result_text.write(str(right_words_number)+'\n')
        result_text.write('\n'.join(dict_words))
        result_text.write('\n'.join(wrong_words))
