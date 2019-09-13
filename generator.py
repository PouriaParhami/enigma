from random import randint

defaultAlphabetAndSymbols = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                             "Y", "Z", "<", ">", "{", "}", "[", "]", "(", ")", ",", ".",
                             ";", "?", "!", "-", "+", ":", "@", "#", "$", "%", "^", "&", "*", "=", " ", "_")

defaultAlphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                   "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                   "Y", "Z")

defaultAlphabetAndSymbolsAndNumbers = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                                       "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                                       "Y", "Z", "<", ">", "{", "}", "[", "]", "(", ")", ",", ".",
                                       ";", "?", "!", "-", "+", ":", "@", "#", "$", "%", "^", "&",
                                       "*", "=", " ", "_", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")


# create a list with random letters or symbols or both.
def make_random_list(tuple_alphabet):
    """
       The list is used to point to the left and right of each page of the router.

       This function is responsible for making lists random.

       @:param tuple_alphabet: The letters and symbols on this tuple give this function.
       :return random_list: A list of letters or symbols in random order.
    """
    alphabet_list = list(tuple_alphabet)
    random_list = []
    alphabet_list_len = len(alphabet_list)
    goal_number = alphabet_list_len

    while goal_number != 0:
        random_index = randint(0, alphabet_list_len - 1)

        if alphabet_list[random_index] != "no":
            random_list.append(alphabet_list[random_index])
            alphabet_list[random_index] = "no"
            goal_number -= 1

    return random_list


# create dict with random key and value for routers.
def make_random_relation_dict(tuple_alphabet):
    """
    The dictionary is used to illustrate the relationship between two router pages.

    This function is responsible for making dictionary random.

    In the relationship between the two router plates it doesn't matter who to connect to.
    It can even be attached to itself on the opposite screen.

    :param: tuple_alphabet: The letters and symbols on this tuple give this function.
    :return: random_dict: A dictionary with random key and value.
    """
    the_list = list(tuple_alphabet)
    random_dict = {}
    goal_number = len(the_list)
    random_list = make_random_list(the_list)

    for key in the_list:
        random_dict[key] = random_list[goal_number - 1]
        goal_number -= 1
    return random_dict


# create dict with random key and value for plug board.
def make_random_paired_connection_dict(tuple_alphabet):
    """
    The dictionary created to display the communication between the members of the plug board is used.

    In plug board Each character must be connected to another character correspondingly.
    It doesn't matter if a character is related to himself.

    :param tuple_alphabet: The letters and symbols on this tuple give this function.
    :return random_dict: A dictionary with random key and value.
    """

    the_list = list(tuple_alphabet)
    random_dict = {}
    random_list = make_random_list(the_list)

    for key in the_list:
        random_dict[key] = "no"

    for key, value in random_dict.items():

        while value == "no":
            index = randint(0, len(the_list) - 1)

            if random_list[index] != "no":
                value = random_list[index]
                random_dict[key] = value
                random_dict[value] = key
                random_list[index] = "no"

                if key in random_list:
                    random_list[random_list.index(key)] = "no"

    return random_dict


# create dict with random key and value for reflect board.
def make_reflect_board(tuple_alphabet):
    """
    The dictionary created to display the communication between the members of the reflect board is used.

    In reflect board Each character must be connected to another character correspondingly.
    And it's important that each character doesn't attach to itself.

    :param tuple_alphabet: The letters and symbols on this tuple give this function.
    :return random_dict: A dictionary with random key and value.
    """
    the_list = list(tuple_alphabet)
    random_dict = {}
    random_list = make_random_list(the_list)

    for key in random_list:
        random_dict[key] = "no"

    for key, value in random_dict.items():

        while value == "no":
            index = randint(0, len(random_list) - 1)
            if random_list[index] != "no" and random_list[index] != key:
                value = random_list[index]
                random_dict[key] = value
                random_dict[value] = key
                random_list[index] = "no"
                if key in random_list:
                    random_list[random_list.index(key)] = "no"

    return random_dict
