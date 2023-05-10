from aqt import mw
from aqt.qt import *
from PyQt5.QtWidgets import QFileDialog


def testFunction() -> None:
    dialog = QDialog()
    grid = QGridLayout()

    for i in range(1, 5):
        for j in range(1, 5):
            grid.addWidget(QPushButton("B" + str(i) + str(j)), i, j)

    dialog.setLayout(grid)
    dialog.setGeometry(100, 100, 200, 100)
    dialog.setWindowTitle("ImgToAnki")

    # Add a file dialog to choose a file
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(dialog, "Choose a file", "", "All Files (*)")
    if file_path:
        # Do something with the chosen file path
        print("Selected file:", file_path)

    dialog.exec()


action = QAction("ImgToAnki", mw)
qconnect(action.triggered, testFunction)
mw.form.menuTools.addAction(action)
