from PyQt6.QtGui import QAction
from aqt import mw
from aqt.utils import getText

def createDeck():
    deckName = getText("Geben Sie den Namen des neuen Decks ein")[0]
    if deckName:
        did = mw.col.decks.id(deckName)
        mw.col.decks.select(did)

action = QAction("Neues Deck erstellen", mw)
action.triggered.connect(createDeck)
mw.form.menuTools.addAction(action)
