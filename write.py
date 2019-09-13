import json
import os

import generator

# It holds the address of the main directory of the program.
CURRENT_PATH = os.getcwd()


# Creates the basic structure of the json file
def make_json_alphabet_structure(file_name, alphabet):
    """
    Creates the basic structure of the json file.
    This file has all the settings of the router, plug board and the reflect board.
    :param file_name: Name of the json file 'router name'
    :param alphabet: The letters and symbols that we want to create with the router and so on
    :return: A json structure.
    """
    setting_json = {
        file_name: {
            "alphabets": alphabet,
            "routersAndBoards": {
                "reflectBoard": {
                    "connections": generator.make_reflect_board(alphabet),
                    "alphabet": generator.make_random_list(alphabet)},

                "plugBoard": {
                    "connections": generator.make_random_relation_dict(
                        generator.make_random_list(alphabet)),
                    "alphabet": generator.make_random_list(alphabet)},

                "firstRouter": {
                    "connections":
                        generator.make_random_relation_dict(
                            generator.make_random_list(alphabet)),
                    "rightPanel": generator.make_random_list(alphabet),
                    "leftPanel": generator.make_random_list(alphabet)
                },
                "secondRouter": {
                    "connections":
                        generator.make_random_relation_dict(
                            generator.make_random_list(alphabet)),
                    "rightPanel": generator.make_random_list(alphabet),
                    "leftPanel": generator.make_random_list(alphabet),
                },
                "thirdRouter": {
                    "connections":
                        generator.make_random_relation_dict(
                            generator.make_random_list(alphabet)),
                    "rightPanel": generator.make_random_list(alphabet),
                    "leftPanel": generator.make_random_list(alphabet),
                }

            },

        }

    }

    return setting_json


# Creates the Json file physically
def make_json_random_setting_structure(file_name, alphabet):
    """
    Creates the Json file physically

    :param file_name: Name of the json file 'router name'
    :param alphabet: The letters and symbols that we want to create with the router and so on
    :return:
    """
    setting_json = make_json_alphabet_structure(file_name, alphabet)

    with open(file_name + ".json", "w") as file_json:
        json.dump(setting_json, file_json)


# create settings folder
def create_dir():
    """
    Creates the settings file.
    This file contains all json files that represent the settings of routers, plug board,
    Reflect board and relation between roters pages.

    :return:
    """
    os.chdir(CURRENT_PATH)

    try:
        os.chdir("settings")

    except FileNotFoundError:
        os.mkdir("settings")
        os.chdir("settings")
        print("file is not exist and i create it.")


# first time the program run we make some setting for user to test the program.
def create_default_settings():
    create_dir()
    if not os.path.isfile(os.getcwd() + "" + "\\default_alphabet.json"):

        make_json_random_setting_structure(
            "default_alphabet",
            generator.defaultAlphabet)

        print("df alpha not exist and i create it.")

    if not os.path.isfile(os.getcwd() + "\\default_alphabet_symbols.json"):

        make_json_random_setting_structure(
            "default_alphabet_symbols",
            generator.defaultAlphabetAndSymbols)

        print("df alpha symbols not exist and i create.")

    if not os.path.isfile(os.getcwd() + "\\default_alphabet_symbols_numbers.json"):
        make_json_random_setting_structure(
            "default_alphabet_symbols_numbers",
            generator.defaultAlphabetAndSymbolsAndNumbers)

        print("df alpha symbols numbers not exist and i create it.")


def create_random_settings():
    """
    When a user wants to make a random setting,
    This function creates these settings by the name of random stings.

    :return:
    """
    create_dir()
    make_json_random_setting_structure("random_alphabet", generator.make_random_list(generator.defaultAlphabet))
    make_json_random_setting_structure("random_alphabet_symbols",
                                       generator.make_random_list(generator.defaultAlphabetAndSymbols))
    make_json_random_setting_structure("random_alphabet_symbols_numbers",
                                       generator.make_random_list(generator.defaultAlphabetAndSymbolsAndNumbers))


# Makes settings that the user specifies its name.
def create_user_settings(setting_name, alphabet):
    create_dir()
    make_json_random_setting_structure(setting_name, alphabet)


# Check if the json file exist on setting folder or not.
def check_exists_router(router_name):
    """
    Check if the json file exist on setting folder or not.

    :param router_name: name of the json file.
    :return: True if exist, false if not exist.
    """
    try:
        os.chdir(CURRENT_PATH)
        if os.path.isdir("settings"):
            os.chdir("settings")
            if os.path.isfile(router_name + ".json"):
                return True
    except FileNotFoundError:
        return False

    return False


# show all json files.
def give_me_files():
    """
    Show all json files is settings folder.

    :return: list of files.
    """
    path = CURRENT_PATH + "\\settings"

    files = []

    for r, d, f in os.walk(path):
        for file in f:
            if '.json' in file:
                files.append(file)

    return files
