from card import Card


def readingTxt(filename):
    cards = []
    #try:
    file = open(filename, encoding="utf_8")
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        words = line.split("\t")
        card = Card(words[0], words[1])
        print(card)
        cards.append(card)
    #except:
    #   print("Failed to read the txt, maybe wrong path.")

    return cards


def onlyReadAndShowList(filename):
    fails = []
    cards = []
    try:
        file = open(filename)
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue
            words = line.split("\t")
            if len(words) != 2:
                fails.append(line)
            else:
                cards.append(Card(words[0], words[1]))
    except:
        print("Failed to read the txt, maybe wrong path.")
        return

    if len(fails) == 0:
        print("The file is arranged correctly.")
    else:
        print("The file is not arranged correctly, the following lines are not correct:")
        [print(fail) for fail in fails]