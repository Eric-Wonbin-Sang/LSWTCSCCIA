from Classes import CodeModule

from General import Constants


class CodeTerminal:

    def __init__(self):

        self.code_module_length = Constants.code_module_length
        self.code_module_list = self.get_code_module_list()

    def get_code_module_list(self):
        return [
            CodeModule.CodeModule() for _ in range(self.code_module_length)
        ]

    def get_code_module(self, index):
        return self.code_module_list[index]

    def get_delta_list_for_code(self, code):
        delta_list = []
        for code_module, code_letter in zip(self.code_module_list, code):
            delta_list.append(code_module.get_best_index_delta_for_code(code_letter))
        self.change_with_delta_list([x * -1 for x in delta_list])
        return delta_list

    def change_with_delta_list(self, delta_list):
        for code_module, delta in zip(self.code_module_list, delta_list):
            if delta > 0:
                code_module.move_up(delta)
            elif delta < 0:
                code_module.move_down(abs(delta))

    def __str__(self):
        ret_str = "Curr: |"
        for i, code_module in enumerate(self.code_module_list):
            ret_str += "{}|".format(code_module.get_value())
        return ret_str
