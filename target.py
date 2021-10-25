from typing import List


import random
def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters =[]
    for i in range(3):
        letters.append([])
        for j in range(3):
            letters[-1].append(chr(random.randint(65,90)))
    print(letters)

generate_grid()





def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    pass



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
    pass


def results():
    pass
