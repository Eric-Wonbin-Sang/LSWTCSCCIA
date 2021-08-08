
class CodeModule:

    character_order = "abcdefghijklmnopqrstuvwxyz0123456789".upper()

    def __init__(self):

        self.curr_index = 0

    def get_value(self):
        return self.character_order[self.curr_index]

    def move_up(self, count=1):
        for _ in range(count):
            self.curr_index = (self.curr_index + 1) % len(self.character_order)

    def move_down(self, count=1):
        for _ in range(count):
            self.curr_index = (self.curr_index - 1) % len(self.character_order)

    def get_up_index_delta_for_code(self, code):
        count = 0
        for i in range(len(self.character_order)):
            if self.get_value() == code:
                self.move_down(count)
                return count
            self.move_up()
            count += 1

    def get_down_index_delta_for_code(self, code):
        count = 0
        for i in range(len(self.character_order)):
            if self.get_value() == code:
                self.move_up(count)
                return count
            self.move_down()
            count -= 1

    def get_best_index_delta_for_code(self, code):
        up_index_delta_for_code = self.get_up_index_delta_for_code(code)
        down_index_delta_for_code = self.get_down_index_delta_for_code(code)

        return up_index_delta_for_code if up_index_delta_for_code < abs(down_index_delta_for_code) \
            else down_index_delta_for_code
