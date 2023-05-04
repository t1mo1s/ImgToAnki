class Card:
    def __init__(self, lang1, lang2):
        self.lang1 = lang1
        self.lang2 = lang2

    def getLang1(self):
        return self.lang1

    def getLang2(self):
        return self.lang2

    def __str__(self):
        return "Word 1: {}, Word 2: {}".format(self.lang1, self.lang2)