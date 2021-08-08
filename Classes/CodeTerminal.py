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

    def get_change_list_for_code(self, code):
        pass

    def __str__(self):
        ret_str = "Curr: |"
        for i, code_module in enumerate(self.code_module_list):
            ret_str += "{}|".format(code_module.get_value())
        return ret_str
