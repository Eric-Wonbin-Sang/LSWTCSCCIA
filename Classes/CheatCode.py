
class CheatCode:

    def __init__(self, category, name, code):

        self.category = category
        self.name = name
        self.code = code

    def __str__(self):
        return "category: {}, name: {}, code: {}".format(
            self.category,
            self.name,
            self.code
        )