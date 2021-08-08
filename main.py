import keyboard
import json

from Classes import CodeTerminal

from General import Constants


def get_start_signal(letter="p"):
    while True:
        try:
            if keyboard.is_pressed(letter):  # if key 'q' is pressed
                return True
        except:
            break


def get_front_space_count(some_str):
    counter = 0
    for letter in some_str:
        if letter == " ":
            counter += 1
        else:
            break
    return counter


def get_all_cheats_dict():
    all_cheats_dict = json.load(open(Constants.cheat_codes_json))

    # for cheats_category in all_cheats_dict:
    #     print(cheats_category)
    #     for key, value in all_cheats_dict[cheats_category].items():
    #         print("\t{}: {}".format(key, value))

    return all_cheats_dict


def main():

    code_terminal = CodeTerminal.CodeTerminal()

    # print(code_terminal)
    # for code_module in code_terminal.code_module_list:
    #     for character in code_module.character_order:
    #         code_module.move_up()
    #         print(code_terminal)

    all_cheats_dict = get_all_cheats_dict()
    for cheats_category in all_cheats_dict:
        print(cheats_category)
        for key, value in all_cheats_dict[cheats_category].items():
            print("\t{}: {} -> {}".format(key, value, code_terminal.get_change_list_for_code(value)))


main()
