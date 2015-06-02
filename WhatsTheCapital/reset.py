from PySide.QtCore import *
from PySide.QtGui import *

class Reset(QDialog):

    pButton = Signal(int)

    def __init__(self, parent):
        super(Reset, self).__init__(parent)
        self.resize(200, 100)
        self.setWindowTitle("Reset")

        self.label1 = QLabel("This will erase your answers, do you want to do this?")
        self.btnYes = QPushButton("Yes")
        self.btnNo = QPushButton("No")
        self.btnYes.clicked.connect(self.clickedYes)
        self.btnNo.clicked.connect(self.clickedNo)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.btnYes)
        layout.addWidget(self.btnNo)

        self.setLayout(layout)

    def clickedYes(self):
        self.pButton.emit(1)
        self.close()

    def clickedNo(self):
        self.pButton.emit(0)
        self.close()
