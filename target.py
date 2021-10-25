from typing import List

import random
def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters =[]
    letter_number = 0
    while letter_number<9:
        if letter_number%3 == 0:
            letters.append([])
        letters[-1].append(chr(random.randint(65,90)))
        letter_number+=1
    return letters

# print(generate_grid())

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
    word= word.lower()
    for ord_index in range (97,123):
        # check by letter ACS if it is in a word
        if chr(ord_index) in word:
            letters_list.append(((chr(ord_index), word.count(chr(ord_index)))))
    return letters_list
# print(list_of_letter_tuples('azAZ'))

def get_words(file_with_words: str, letters: List[str]):
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    # create list of tuples with letters and its number of occurrences
    grid_letters = list_of_letter_tuples(''.join(letters[0] + letters[1] + letters[2]))
    main_letter = letters[1][1]
    words_from_dictionary = []
    # open file with words and read it line by line
    with open (file_with_words, mode = 'r', encoding='utf-8') as dictionary:
        for word in dictionary:
            # read new word from the file
            current_word = word.read()
            # if word is too short or too long do not add it to the list, continue loop
            if len(current_word) < 4 or len(current_word) > 9 or main_letter not in current_word:
                continue

            # create list[tuple] with letters of the word from dict and its number of occurrences
            current_word_letters = list_of_letter_tuples(current_word)

            # check if it's possible to fold current word from dictionary by letters in grid
            startig_index_in_grid_letters, index_in_word = 0, 0
            correct_word = True  #default correct_word value
            while index_in_word < len(current_word_letters):
                letter_in = False # default letter_in value
                # check if current letter from a word is in grid
                for i in range(startig_index_in_grid_letters, len(grid_letters)):
                    if  current_word_letters[index_in_word][0] == grid_letters[i][0]:
                        # if it is in grid then check if its number of occurrences
                        # in the word is not more than in the grid and exit the loop
                        if current_word_letters[index_in_word][1] <= grid_letters[i][1]:
                            letter_in = True
                            startig_index_in_grid_letters = i+1
                        break
                # if current letter is not in grid exit the loop, do not add the word to list
                if not letter_in:
                    correct_word = False
                    break
                index_in_word += 1   # change letter in word_letter_list to next one
            if correct_word:
                words_from_dictionary.append(current_word)

    return words_from_dictionary


def rule_correctness_word(word, grid_letters):
    """
    (str, list) -> bool
    Check if word fits game roles.
    Word lenght in range [4,9].
    Word includes central letter
    All letters in the word are from grid board and itd
    number of occurrences in words is not more than in the grid board

    """
    word = ''
    central_letter = grid_letters[1][1]
    # if word is too short or too long do not add it to the list, continue loop
    if len(word) < 4 or len(word) > 9 or central_letter not in word:
        return False

    # create list[tuple] with letters of the word from dict and its number of occurrences
    current_word_letters = list_of_letter_tuples(word)

    # check if it's possible to fold word from dictionary by letters in grid
    startig_index_in_grid_letters, index_in_word = 0, 0
    correct_word = True  #default correct_word value
    while index_in_word < len(current_word_letters):
        letter_in = False # default letter_in value
        # check if current letter from a word is in grid
        for i in range(startig_index_in_grid_letters, len(grid_letters)):
            if  current_word_letters[index_in_word][0] == grid_letters[i][0]:
                # if it is in grid then check if its number of occurrences
                # in the word is not more than in the grid and exit the loop
                if current_word_letters[index_in_word][1] <= grid_letters[i][1]:
                    letter_in = True
                    startig_index_in_grid_letters = i+1
                break
        # if current letter is not in grid exit the loop, do not add the word to list
        if not letter_in:
            correct_word = False
            break
        index_in_word += 1   # change letter in word_letter_list to next one

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    list_of_player_worlds = []
    while True:
        player_world = input()
        if player_world == '^D':
            break
        list_of_player_worlds.append(player_world)
    return list_of_player_worlds


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    wrong_words = []
    main_letter = letters[1][1]
    for word in user_words:
        if not rule_correctness_word(word,letters):
            continue
        word = list_of_letter_tuples(user_words)


def results():
    pass
