# Created by: PyCharm
# Date: 9/12/2019
# Author: Pouria Parhami
# Project Name: enigma


import generator
import read
import write

plugBoard = {}
plugBoardP = []

firstRouter = {}
firstRouterR = []
firstRouterL = []

secondRouter = {}
secondRouterR = []
secondRouterL = []

thirdRouter = {}
thirdRouterR = []
thirdRouterL = []

reflectBoard = {}
reflectBoardP = []


# from plug board to reflect board
def step_forward(position, panel_r, panel_l, connection_map):
    """

    When each character is read from the input, this function is sounded until it reaches the reflect board.
    This function specifies that at each step I have to go through the index of each page
    Of the routers to reach the reflect board.

    :param position: Position of the char in the list.
    :param panel_r: The list that represents the right side of the router
    :param panel_l: The list that represents the left side of the router
    :param connection_map: A dictionary showing which characters are attached to each character on the screen

    :return: Index of the char in left side of router
    """
    holder1 = panel_r[position]
    holder2 = connection_map[holder1]
    holder3 = panel_l.index(holder2)
    return holder3


# from reflect board to plug board.
def step_backward(position, panel_l, panel_r, connection_map):
    """
    This function sounds as the character moves from the reflex board to the plug.
    Its similar to the previous one, but vice versa

    :param position: Position of the char in the list.
    :param panel_r: The list that represents the right side of the router
    :param panel_l: The list that represents the left side of the router
    :param connection_map: A dictionary showing which characters are attached to each character on the screen

    :return: Index of the char in left side of router
    """
    holder1 = panel_l[position]
    holder3 = ""
    for key, value in connection_map.items():
        if value == holder1:
            holder3 = key
            break
    holder4 = panel_r.index(holder3)
    return [holder4, holder3]


# shift right one list.
def shift_right_panel(panel):
    last_value = panel.pop(-1)
    panel.insert(0, last_value)


# shift left one list.
def shift_left_panel(panel):
    first_value = panel.pop(0)
    panel.append(first_value)


# Sugar code.
def shift_right_router(panel_r, panel_l):
    shift_right_panel(panel_r)
    shift_right_panel(panel_l)


# sugar code.
def shift_left_router(panel_r, panel_l):
    shift_left_panel(panel_r)
    shift_left_panel(panel_l)


# If the router has a full round, it will move the next router
def check_for_rotate_routers(counter, goal, pr, pl, the_counter):
    if counter == goal:
        counter = 0
        shift_right_router(pr, pl)
        the_counter += 1


# just helper function for developer test.
def print_some_settings():
    print("---plug bard")
    print(plugBoard)
    print(plugBoardP)
    print("--first routers")
    print(firstRouter)
    print(firstRouterR)
    print(firstRouterL)
    print("--second routers")
    print(secondRouter)
    print(secondRouterR)
    print(secondRouterL)
    print("--third routers")
    print(thirdRouter)
    print(thirdRouterR)
    print(thirdRouterL)
    print("--ref routers")
    print(reflectBoard)
    print(reflectBoardP
          )


# Create json file (router setting) with name that user want.
def create_user_router():
    while True:
        router_name = input("Enter the router name:\n>> ")
        alphabet = input("Enter the alphabet you want to use.\n"
                         "1- just english alphabet\n"
                         "2- english alphabet and symbols\n"
                         "3- english alphabet and symbols and numbers")

        # If the user sends a letter instead of a number, show an error message.
        try:
            if int(alphabet) not in range(1, 4):
                print("please enter number in range 1 to 3")
                continue
            else:
                if int(alphabet) == 1:
                    write.create_user_settings(router_name,
                                               generator.make_random_list(generator.defaultAlphabet))
                elif int(alphabet) == 2:
                    write.create_user_settings(router_name,
                                               generator.make_random_list(
                                                   generator.defaultAlphabetAndSymbols))
                else:
                    write.create_user_settings(
                        router_name,
                        generator.make_random_list(generator.defaultAlphabetAndSymbolsAndNumbers))

            # At the end, if json file is create and exist set the variables and show success message.
            if write.check_exists_router(router_name):
                print("Router Create Successfully.")

                # Read json file and set the variables.
                read.read_json_settings(router_name, plugBoard, plugBoardP, reflectBoard,
                                        reflectBoardP,
                                        firstRouter,
                                        firstRouterR, firstRouterL, secondRouter, secondRouterR,
                                        secondRouterL,
                                        thirdRouter,
                                        thirdRouterR, thirdRouterL)
            else:
                print("Can't create router.")
                continue

            break

        except ValueError:
            print("Please Enter Number Between 1 to 4.")
            continue


# Set a router to use.
def set_routers():
    while True:

        # If the user sends a letter instead of a number, show an error message.
        try:

            s1 = input("1-default_alphabet\n"
                       "2-default_alphabet_and_symbols\n"
                       "3-default_alphabet_symbols_and_numbers\n"
                       "4-create new router\n"
                       "5-enter name of the router\n>> ")

            if int(s1) not in range(1, 6):
                print("Please enter number between 1 to 5")
                continue

            if int(s1) == 1:

                # Read json file and set the variables.
                read.read_json_settings("default_alphabet", plugBoard, plugBoardP, reflectBoard, reflectBoardP,
                                        firstRouter,
                                        firstRouterR, firstRouterL, secondRouter, secondRouterR, secondRouterL,
                                        thirdRouter,
                                        thirdRouterR, thirdRouterL)
            elif int(s1) == 2:
                # Read json file and set the variables.
                read.read_json_settings("default_alphabet_symbols", plugBoard, plugBoardP, reflectBoard, reflectBoardP,
                                        firstRouter,
                                        firstRouterR, firstRouterL, secondRouter, secondRouterR, secondRouterL,
                                        thirdRouter,
                                        thirdRouterR, thirdRouterL)
            elif int(s1) == 3:

                # Read json file and set the variables.
                read.read_json_settings("default_alphabet_symbols_numbers", plugBoard, plugBoardP, reflectBoard,
                                        reflectBoardP, firstRouter,
                                        firstRouterR, firstRouterL, secondRouter, secondRouterR, secondRouterL,
                                        thirdRouter,
                                        thirdRouterR, thirdRouterL)
            elif int(s1) == 4:
                print("------------------------------------------")

                create_user_router()

            elif int(s1) == 5:

                name = input("Enter name of the router: ")

                # Read json file and set the variables.
                result = read.read_json_settings(name, plugBoard, plugBoardP, reflectBoard,
                                                 reflectBoardP,
                                                 firstRouter,
                                                 firstRouterR, firstRouterL, secondRouter, secondRouterR,
                                                 secondRouterL,
                                                 thirdRouter,
                                                 thirdRouterR, thirdRouterL)
                if result:

                    print("Router find and we setup it.")

                else:
                    continue

                break

            break

        except ValueError:
            print("Please Enter Number Between 1 to 5.")
            continue


# if user want rotate routers before start this function handel it.
def tuning_routers_by_user():
    while True:
        rotate = input("Rotate router:\n"
                       "1- don't want to rotate them.\n"
                       "2- rotate router one.\n"
                       "3- rotate router two.\n"
                       "4- rotate router three.\n"
                       ">> ")

        # If the user sends a letter instead of a number, show an error message.
        try:
            int_rotate = int(rotate)
        except ValueError:
            print("Please Enter Number Between 1 to 4.")
            continue

        if int_rotate == 1:
            break

        # if user send number bigger than our range, that is not problem.
        elif int_rotate == 2:
            number = input("enter number between 1 to " + str(len(firstRouterR)))

            # If the user sends a letter instead of a number, show an error message.
            try:
                number = int(number)
            except ValueError:
                print("please enter number.")
                continue

            for x in range(number):
                shift_right_router(firstRouterR, firstRouterL)
            continue

        elif int_rotate == 3:
            number = input("enter number between 1 to " + str(len(secondRouterR)))

            # If the user sends a letter instead of a number, show an error message.
            try:
                number = int(number)
            except ValueError:
                print("please enter number.")
                continue

            for x in range(number):
                shift_right_router(secondRouterR, secondRouterL)
            continue

        elif int_rotate == 4:
            number = input("enter number between 1 to " + str(len(thirdRouterR)))

            # If the user sends a letter instead of a number, show an error message.
            try:
                number = int(number)
            except ValueError:
                print("please enter number.")
                continue

            for x in range(number):
                shift_right_router(thirdRouterR, thirdRouterL)
            continue


# the main function
def run_enigma():
    print("Hello, Welcome to enigma.")
    print("For exit of program just type exit().")
    print("For reset the routers to encrypt type encrypt()")
    print("For set router again type reset()")
    print("For see all routers settings type show()")
    print("You can use this keys when see this message: 'Enter your message:' ")
    print("--------------------------------------")
    print("Please set your routers first.")
    print("We create 3 different package for routers,")
    print("if you dont want to use them select number '4', else chose one of them.")

    # Creates a folder and, if any, enters it.
    write.create_default_settings()

    dont_support_char = ""
    final_string = ""

    first_router_counter = 0
    second_router_counter = 0
    third_router_counter = 0

    '''
    The first step is to determine whether the user wants to use the default router, 
    Or the router that he has previously built or wants to build.  
    This function is designed to perform these tasks.
    '''
    set_routers()

    # The second step is for the user to set up the routers.
    tuning_routers_by_user()

    # ------------------------------- get message and encrypt it --------------------------------
    while True:

        input_str = input("Enter your message:")

        if input_str == "exit()":
            break

        if input_str == "show()":

            files = write.give_me_files()

            print("--------------------------")
            for file in files:
                print(file)
            print("---------------------------")

            continue

        if input_str == "encrypt()":

            for a in range(first_router_counter):
                shift_left_router(firstRouterR, firstRouterL)

            print()
            for b in range(second_router_counter):
                shift_left_router(secondRouterR, secondRouterL)

            for c in range(third_router_counter):
                shift_left_router(thirdRouterR, thirdRouterL)

            print("Routers is ready for encrypt.")
            first_router_counter = 0
            second_router_counter = 0
            third_router_counter = 0
            continue

        if input_str == "reset()":

            plugBoardP.clear()
            plugBoard.clear()
            firstRouterL.clear()
            firstRouterR.clear()
            firstRouter.clear()
            secondRouterL.clear()
            secondRouter.clear()
            secondRouterR.clear()
            thirdRouterL.clear()
            thirdRouterR.clear()
            thirdRouter.clear()
            reflectBoardP.clear()
            reflectBoard.clear()

            first_router_counter = 0
            second_router_counter = 0
            third_router_counter = 0

            dont_support_char = ""
            final_string = ""

            set_routers()
            tuning_routers_by_user()

        else:

            input_str = input_str.upper()
            input_list = [*input_str]

            counter = 0
            print("message before encrypt:", input_str)
            for x in input_str:

                # If the alphabet dont support some characters, we keep them in to the 'dont_support_char'
                try:
                    holder = plugBoard[x]
                    holder = plugBoardP.index(holder)

                    shift_right_router(firstRouterR, firstRouterL)
                    first_router_counter += 1

                    check_for_rotate_routers(first_router_counter, len(firstRouterR), secondRouterR, secondRouterL,
                                             second_router_counter)
                    check_for_rotate_routers(second_router_counter, len(secondRouterR), thirdRouterR, thirdRouterL,
                                             third_router_counter)
                    # The path that the character takes from the plug board to the reflect board.
                    po = step_forward(holder, firstRouterR, firstRouterL, firstRouter)
                    holder = step_forward(po, secondRouterR, secondRouterL, secondRouter)
                    po = step_forward(holder, thirdRouterR, thirdRouterL, thirdRouter)
                    holder = step_forward(po, reflectBoardP, reflectBoardP, reflectBoard)

                    # The path that the character takes from the reflect board to the plug board.
                    po = step_backward(holder, thirdRouterL, thirdRouterR, thirdRouter)
                    holder = step_backward(po[0], secondRouterL, secondRouterR, secondRouter)
                    po = step_backward(holder[0], firstRouterL, firstRouterR, firstRouter)
                    holder = step_backward(po[0], plugBoardP, plugBoardP, plugBoard)

                    input_list[counter] = holder[1]
                    counter += 1

                except KeyError:
                    dont_support_char += x + "\n"

                    # In this case the character can be considered and continued or
                    # Just the same character without changing
                    input_list[counter] = x
                    counter += 1

            # Preparing characters to join together and display at the output
            for n in input_list:
                final_string += n

            print("encrypt is:", final_string)
            final_string = ""

            if dont_support_char != "":
                print("we dont support this chars:", dont_support_char)
                dont_support_char = ""


run_enigma()
