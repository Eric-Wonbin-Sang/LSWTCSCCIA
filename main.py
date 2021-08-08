import keyboard

from Classes import CodeTerminal, CheatsFile

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


def get_code_to_delta_list_dict(code_terminal, cheat_code_list):
    curr_terminal_code_to_delta_list_dict = {}
    for cheat_code in cheat_code_list:
        curr_terminal_code_to_delta_list_dict[cheat_code] = code_terminal.get_delta_list_for_code(cheat_code.code)
    return curr_terminal_code_to_delta_list_dict


def get_fastest_code_for_input(code_terminal, cheat_code_list):
    code_to_delta_list_dict = get_code_to_delta_list_dict(code_terminal, cheat_code_list)
    for cheat_code, delta_list in code_to_delta_list_dict.items():
        code_to_delta_list_dict[cheat_code] = sum([abs(x) for x in delta_list])
    return min(code_to_delta_list_dict, key=code_to_delta_list_dict.get)


def main():

    code_terminal = CodeTerminal.CodeTerminal()
    cheats_file = CheatsFile.CheatsFile()

    # all_cheats_dict = cheats_file.all_cheats_dict
    # for cheats_category in all_cheats_dict:
    #     print(cheats_category)
    #     for key, value in all_cheats_dict[cheats_category].items():
    #         # print("\t{}".format(code_terminal))
    #         print("\t{}: {} -> {}".format(key, value, code_terminal.get_delta_list_for_code(value)))
    #         # break

    curr_cheat_code_list = cheats_file.cheat_code_list
    for _ in range(len(cheats_file.cheat_code_list)):
        print(code_terminal)
        print(get_fastest_code_for_input(code_terminal, curr_cheat_code_list))


main()
