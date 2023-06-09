from aqt import mw
from aqt.qt import *
from PyQt5.QtWidgets import QFileDialog
from .ui_dialog import UiDialog


def testFunction() -> None:
    dialog = QDialog()
    grid = QGridLayout()

    for i in range(1, 5):
        for j in range(1, 5):
            grid.addWidget(QPushButton("B" + str(i) + str(j)), i, j, 2)

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

def show_dialog():
    # Create an instance of QDialog
    dialog = QDialog()

    # Create an instance of Ui_Dialog
    ui = UiDialog()
    ui.setupUi(dialog)

    # Show the dialog
    dialog.show()
    dialog.exec()



def setup_dialog_action():
    action = QAction("ImgToAnki", mw)
    qconnect(action.triggered, show_dialog)
    mw.form.menuTools.addAction(action)


setup_dialog_action()
