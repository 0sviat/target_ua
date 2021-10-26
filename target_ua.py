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

def get_words(file_with_words: str, letters: List[str]):
    """
    Reads the file f. Checks the words with rules (starts with symbol from setted letters
    and it contains less then 6 letters) Returns a list of words.
    """
    words_from_dictionary = []
    # open file with words and read it line by line
    with open(file_with_words, mode='r', encoding='utf-8') as dictionary:
        for line_word in dictionary:
            space_index = line_word.index(' ')
            if line_word[0] in letters and space_index < 6:
                # separate word from the line
                word = line_word[:space_index]
                # check language part of the word
                if line_word[space_index + 1: space_index + 3] in ['no','/n']:
                    part_of_speech = 'noun'
                elif line_word[space_index + 1: space_index + 3] in ['ve','/v']:
                    part_of_speech = 'verb'
                elif line_word[space_index + 1: space_index + 4] in [ 'adv']:
                    part_of_speech = 'adverb'
                elif line_word[space_index + 1: space_index + 4] in ['/ad', 'adj']:
                    part_of_speech = 'adjective'
                else:
                    # speech part is not beyong indicated go to next word
                    continue
                # add the word to a list
                words_from_dictionary.append((word,part_of_speech))
    return words_from_dictionary

print(get_words('base.lst',['a']))
print(get_words('base.lst',['а','б','в','г','д']))

def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    (str, list) -> bool
    Check if word fits game rules:
    Starts with one of letters
    Word includes less then 6 words
    """
    omitted_words = []
    player_correct_words =[]
    # delete from list with user words that do not start from one of stated letters
    for i in range(len(user_words)-1,-1,-1):
        if user_words[i][0] not in letters:
            user_words.pop(i)
    number_in_dict = len(dict_of_words)
    for j in range(number_in_dict):
        if dict_of_words[j][1] == language_part:
            if dict_of_words[i][0] in user_words:
                player_correct_words.append(dict_of_words[i][0])
            else:
                omitted_words.append(dict_of_words[i][0])
    return player_correct_words, omitted_words,


def results():
    """
    Return results of the game
    """
    letters = generate_grid()
