import cardreader
from card import Card
import ankiConnect
from menu import showMenu

userChoice = showMenu()

while userChoice != 0:
    if userChoice == 1:
        fileName = input("Enter the filename, it must be in the source folder:")
        # read card and check validity
        cardreader.onlyReadAndShowList(fileName)
        # show menu from start
        userChoice = showMenu()
    if userChoice == 2:
        fileName = input("Enter the filename, it must be an absolute path:")
        deckName = input("Now enter the deckname in which the cards should be added into:")
        # read card and produce list
        cards = cardreader.readingTxt(fileName)
        # add cards to anki
        for card in cards:
            ankiConnect.addNote(deckName, card.getLang1(), card.getLang2())
        # show menu from start
        userChoice = showMenu()