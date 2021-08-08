import json

from Classes import CheatCode

from General import Constants


class CheatsFile:

    def __init__(self):

        self.cheat_codes_json = Constants.cheat_codes_json

        self.all_cheats_dict = self.get_all_cheats_dict()
        self.cheat_code_list = self.get_cheat_code_list()

    def get_all_cheats_dict(self):
        return json.load(open(self.cheat_codes_json))

    def get_all_cheats_dict_str(self):
        ret_str = ""
        for i, cheats_category in enumerate(self.all_cheats_dict):
            if i != 0:
                ret_str += "\n"
            ret_str += cheats_category
            for key, value in self.all_cheats_dict[cheats_category].items():
                ret_str += "\n\t{}: {}".format(key, value)
        return ret_str

    def get_cheat_code_list(self):
        cheat_code_list = []
        for cheats_category in self.all_cheats_dict:
            for key, value in self.all_cheats_dict[cheats_category].items():
                cheat_code_list.append(
                    CheatCode.CheatCode(
                        cheats_category,
                        key,
                        value
                    )
                )
        return cheat_code_list
