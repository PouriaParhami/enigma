import json

import write


# read the json files in settings folder.
def read_json_settings(file_name, plug_board, plug_board_panel, reflect_board,
                       reflect_board_panel, first_router_connections, first_router_right_panel, first_router_left_panel,
                       second_router_connections=None, second_router_right_panel=None, second_router_left_panel=None,
                       third_router_connections=None, third_router_right_panel=None, third_router_left_panel=None):
    """
    Each file contains the settings of all routers, reflex boards, and plugins.

    This function is responsible for reading and setting the data in the file for the relevant variables.

    :param file_name: name of the json file, name must be entered with out .json like: hello.json -> hello
    :param plug_board: must be a dictionary
    :param plug_board_panel: must be a list
    :param reflect_board:  must be a dictionary
    :param reflect_board_panel: must be a list
    :param first_router_connections: must be a dictionary
    :param first_router_right_panel: must be a list
    :param first_router_left_panel: must be a list
    :param second_router_connections: must be a dictionary
    :param second_router_right_panel: must be a list
    :param second_router_left_panel: must be a list
    :param third_router_connections: must be a dictionary
    :param third_router_right_panel: must be a list
    :param third_router_left_panel: must be a list
    :return: True if our work is done. false if we have problem.
    """
    if write.check_exists_router(file_name):
        with open(file_name + ".json", "r") as read_json:
            data = json.load(read_json)

        try:
            json_default_address = data[file_name]["routersAndBoards"]

            for x in locals().keys():
                try:
                    x.clean()
                except AttributeError:
                    continue

            alphabet = data[file_name]["alphabets"]
            plug_board.update(json_default_address["plugBoard"]["connections"])
            plug_board_panel.extend(json_default_address["plugBoard"]["alphabet"])

            reflect_board.update(json_default_address["reflectBoard"]["connections"])
            reflect_board_panel.extend(json_default_address["reflectBoard"]["alphabet"])

            first_router_connections.update(json_default_address["firstRouter"]["connections"])
            first_router_right_panel.extend(json_default_address["firstRouter"]["rightPanel"])
            first_router_left_panel.extend(json_default_address["firstRouter"]["leftPanel"])

            second_router_connections.update(json_default_address["secondRouter"]["connections"])
            second_router_right_panel.extend(json_default_address["secondRouter"]["rightPanel"])
            second_router_left_panel.extend(json_default_address["secondRouter"]["leftPanel"])

            third_router_connections.update(json_default_address["thirdRouter"]["connections"])
            third_router_right_panel.extend(json_default_address["thirdRouter"]["rightPanel"])
            third_router_left_panel.extend(json_default_address["thirdRouter"]["leftPanel"])

            return True
        except KeyError as key:
            print("The '{}' not exist.\nplease check the json file with keys you want.".format(key.args[0]))
            return False
    else:
        print("There is no such router. Please double-check the imported name or look at the Stings folder.")
        return False
