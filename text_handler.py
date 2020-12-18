"""
Just some methods that I use in the program. They can be copy and pasted into the main .py file but
to keep it clean I opted to put them in their own dedicated file.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# Replace feature that will be added. Currently only for one word. Would like to have multiple words.
def replace_word(list, word, new_word):
    for i in range(len(list)):
        list[i] = list[i].replace(word, new_word)
    return list


"""Parameter Window"""


class ParamDialog(QWidget):
    def __init__(self, file, *args, **kwargs):
        super(ParamDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Parameters")

        doc = file
        toggle = False

        if doc.__contains__(":/"):
            doc = doc.replace("/", "\\\\")
            toggle = True
            print(doc)

        self.master_layout = QVBoxLayout()
        self.setLayout(self.master_layout)
        self.sub_layout = QHBoxLayout()
        self.form_layout = QFormLayout()

        self.master_layout.addLayout(self.form_layout)
        self.master_layout.addLayout(self.sub_layout)

        """File Path in Param Window"""
        self.directory_path = QLineEdit()
        self.directory_path.setPlaceholderText("No Directory Specified")
        self.directory_path.setReadOnly(True)
        self.directory_path.setText(doc)
        self.form_layout.addRow("Directory", self.directory_path)

        """File Contents in Param Window"""
        self.directory_contents = QLineEdit()
        self.directory_contents.setReadOnly(True)
        if toggle:
            self.f = open(doc)
            self.line = self.f.readline()
            self.f.close()
            self.directory_contents.setText(self.line)
        self.form_layout.addRow("Content", self.directory_contents)

        self.table = QTableWidget(1, 7)
        self.scrollbar = QScrollBar()
        self.scrollbar.setHidden(True)

        self.table.setVerticalScrollBar(self.scrollbar)
        if toggle:
            self.f = open(doc)
        self.table.resizeColumnsToContents()
        self.table.cellPressed.connect(self.cell_pressed)
        self.table.itemPressed.connect(self.item_something)

        self.h_header = QHeaderView(Qt.Horizontal)
        self.h_header.setHidden(False)
        self.table.setHorizontalHeader(self.h_header)
        self.v_header = QHeaderView(Qt.Vertical)
        self.v_header.setHidden(True)
        self.table.setVerticalHeader(self.v_header)

        self.sub_layout.addWidget(self.table, Qt.AlignTop)

        # self.diagnose_line = QLabel()
        # self.diagnose_line.setText("Yuh")
        #
        # self.slider = QSlider()
        # self.slider.setRange(0, 10)
        # self.slider.setOrientation(Qt.Horizontal)
        # self.slider.valueChanged.connect(lambda x: self.slider_value(x))
        #
        # self.master_layout.addWidget(self.diagnose_line)
        # self.master_layout.addWidget(self.slider)

    def transfer_param(self):
        print("Hey, listen! (transfer_param)")

    def cell_pressed(self):
        print("Cell Pressed")

    def item_something(self):
        print("item something")

    def slider_value(self, x):
        print(x)


class CWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(CWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Another Window")

        self.window_layout = QFormLayout()
        self.setLayout(self.window_layout)

        self.label = QLineEdit()
        self.window_layout.addRow("testing", self.label)

        # self.tab = QTabWidget()
        # self.window_layout.addWidget(self.tab, alignment=Qt.AlignLeft)
        # self.setLayout(self.window_layout)
