from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *




def testFunction() -> None:
    # create a new dialog window
    dialog = QDialog(mw)
    dialog.setWindowTitle("Custom Dialog")
    dialog.setFixedSize(900, 700)

    # create a new grid layout
    gridLayout = QGridLayout()

    # add widgets to the grid layout
    label1 = QLabel("Label 1")
    label2 = QLabel("Label 2")
    label3 = QLabel("Label 3")
    lineEdit1 = QLineEdit()
    lineEdit1.setMaximumHeight(mw.g)
    lineEdit2 = QLineEdit()
    lineEdit3 = QLineEdit()

    gridLayout.addWidget(label1, 0, 0)
    gridLayout.addWidget(lineEdit1, 0, 1)
    gridLayout.addWidget(label2, 1, 0)
    gridLayout.addWidget(lineEdit2, 1, 1)
    gridLayout.addWidget(label3, 2, 0)
    gridLayout.addWidget(lineEdit3, 2, 1)

    # customize the grid layout
    gridLayout.setSpacing(10)
    gridLayout.setColumnStretch(0, 1)
    gridLayout.setColumnStretch(1, 2)
    gridLayout.setRowStretch(0, 1)
    gridLayout.setRowStretch(1, 2)
    gridLayout.setRowStretch(2, 3)

    # set the border of the widget to black
    for i in range(gridLayout.count()):
        widget = gridLayout.itemAt(i).widget()
        widget.setStyleSheet("border: 1px solid black;")

    # set the layout of the dialog window to the grid layout
    dialog.setLayout(gridLayout)

    # show the dialog window
    dialog.exec_()


action = QAction("test", mw)
qconnect(action.triggered, testFunction)
mw.form.menuTools.addAction(action)