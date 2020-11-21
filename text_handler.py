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

#
# given = "uiib frzw sy bwedkej lqne ii wive qser gqu cl e gqieylvp"
#
# dic = {
#     "a": 0,
#     "b": 1,
#     "c": 2,
#     "d": 3,
#     "e": 4,
#     "f": 5,
#     "g": 6,
#     "h": 7,
#     "i": 8,
#     "j": 9,
#     "k": 10,
#     "l": 11,
#     'm': 12,
#     'n': 13,
#     'o': 14,
#     'p': 15,
#     'q': 16,
#     'r': 17,
#     's': 18,
#     't': 19,
#     'u': 20,
#     'v': 21,
#     'w': 22,
#     'x': 23,
#     'y': 24,
#     'z': 25,
# }
# dic2 = {
#     0: 'a',
#     1: 'b',
#     2: 'c',
#     3: 'd',
#     4: 'e',
#     5: 'f',
#     6: 'g',
#     7: 'h',
#     8: 'i',
#     9: 'j',
#     10: 'k',
#     11: 'l',
#     12: 'm',
#     13: 'n',
#     14: 'o',
#     15: 'p',
#     16: 'q',
#     17: 'r',
#     18: 's',
#     19: 't',
#     20: 'u',
#     21: 'v',
#     22: 'w',
#     23: 'x',
#     24: 'y',
#     25: 'z',
# }
#
# x = 0
# y = 1
#
# for i in range(len(given)):
#     if given[i] == ' ':
#         pass
#         # sys.stdout.write('_ ')
#     else:
#         buff = dic[given[i]]
#         if buff > 0\
#                 :
#             buff = buff - 1
#             sys.stdout.write(dic2[buff])
#
#             # sys.stdout.write(str(buff))
#             sys.stdout.write(' ')
#         elif buff <= 0:
#             buff =- 1
#             buff =+ 26
#             sys.stdout.write(dic2[buff])
#             sys.stdout.write(' ')
#
# shifter = 0
