
class CodeModule:

    character_order = "abcdefghijklmnopqrstuvwxyz0123456789".upper()

    def __init__(self):

        self.curr_index = 0

    def get_value(self):
        return self.character_order[self.curr_index]

    def move_up(self):
        self.curr_index = (self.curr_index + 1) % len(self.character_order)

    def move_down(self):
        self.curr_index = (self.curr_index - 1) % len(self.character_order)
