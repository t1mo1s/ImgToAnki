from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *




def testFunction() -> None:
    dialog = QDialog()
    grid = QGridLayout()

    for i in range(1, 5):
        for j in range(1, 5):
            grid.addWidget(QPushButton("B" + str(i) + str(j)), i, j, 2)

    dialog.setLayout(grid)
    dialog.setGeometry(100, 100, 200, 100)
    dialog.setWindowTitle("ImgToAnki")
    dialog.exec_()


action = QAction("ImgToAnki", mw)
qconnect(action.triggered, testFunction)
mw.form.menuTools.addAction(action)