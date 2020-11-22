"""
Just some methods that I use in the program. They can be copy and pasted into the main .py file but
to keep it clean I opted to put them in their own dedicated file.
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


def replace_word(list, word, new_word):
    for i in range(len(list)):
        list[i] = list[i].replace(word, new_word)
    return list


class ParamDialog(QWidget):
    def __init__(self, *args, **kwargs):
        super(ParamDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Parameters")

        self.master_layout = QVBoxLayout()
        self.setLayout(self.master_layout)
        self.sub_layout = QHBoxLayout()
        self.master_layout.addLayout(self.sub_layout)

        self.param = QTextEdit()
        self.transfer_btn_right = QPushButton("->")
        self.transfer_btn_right.clicked.connect(self.transfer_param)
        self.final_param = QTextEdit()

        self.table = QTableWidget(2, 2)
        self.table.cellPressed.connect(self.cell_pressed)
        self.table.itemPressed.connect(self.item_something)
        self.header = QHeaderView(Qt.Horizontal)
        self.header.setHidden(True)
        self.table.setHorizontalHeader(self.header)

        self.sub_layout.addWidget(self.param)
        self.sub_layout.addWidget(self.transfer_btn_right)
        self.sub_layout.addWidget(self.final_param)
        self.sub_layout.addWidget(self.table)

    def transfer_param(self):
        print("Hey, listen! (transfer_param)")

    def cell_pressed(self):
        print("Cell Pressed")

    def item_something(self):
        print("item something")
