from PySide.QtCore import *
from PySide.QtGui import *


class Submit(QDialog):

    def __init__(self, parent, nme):
        super(Submit, self).__init__(parent)
        self.resize(200, 100)
        self.setWindowTitle("Results")

        self.label1 = QLabel(nme)
        self.btn = QPushButton("Close")
        self.btn.clicked.connect(self.btnClose)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def btnClose(self):
        self.close()