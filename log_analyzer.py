import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qdarkstyle

from text_handler import ParamDialog, CWindow


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.w = None
        self.me = None

        LEFT = Qt.AlignLeft

        master_layout = QHBoxLayout()

        sublayout = QVBoxLayout()
        master_layout.addLayout(sublayout)

        sublayout_2 = QVBoxLayout()
        master_layout.addLayout(sublayout_2)

        self.group = QGroupBox("File Location")
        self.group.setFixedWidth(700)
        self.group_layout = QHBoxLayout()
        self.group.setLayout(self.group_layout)
        sublayout.addWidget(self.group, alignment=LEFT)

        """File Line"""
        self.file_line = QLineEdit()
        self.file_line.setFixedWidth(580)
        # self.file_line.setEditable(True)
        self.file_line.setPlaceholderText("Directory Path")
        # self.file_line.addItem("C:\\")
        self.group_layout.addWidget(self.file_line, alignment=LEFT)
        self.file_line.returnPressed.connect(self.read_file)

        """File Button"""
        self.button = QPushButton("Open File")
        self.button.clicked.connect(self.file_dialog)
        self.group_layout.addWidget(self.button, alignment=LEFT)

        self.label = QLabel("Waiting...")
        self.label.setStyleSheet("color: lightGray;"
                                 "background-color: rgb(128,0,0);"
                                 "border-radius: 5px")
        sublayout.addWidget(self.label, alignment=LEFT)

        # self.btn = QPushButton("Window")
        # sublayout.addWidget(self.btn)
        # self.btn.clicked.connect(self.file_opened)

        self.frame = QPlainTextEdit()
        # self.frame.setStyleSheet("background-color: lightGray")
        # self.frame.setFixedWidth(700)
        self.frame.setReadOnly(True)
        # sublayout.addWidget(self.frame, alignment=LEFT)

        self.tab = QTabWidget()
        self.tab.setTabPosition(QTabWidget.North)
        self.tab.setFixedWidth(700)
        sublayout.addWidget(self.tab, alignment=LEFT)

        """File Attributes"""
        self.file_attributes = QGroupBox("File Attributes")
        self.file_attributes.setFixedHeight(60)
        fa_layout = QGridLayout()
        self.file_attributes.setLayout(fa_layout)

        self.file_rows_label = QLabel("Rows:")
        self.file_rows_label.setFixedWidth(29)

        self.file_rows_line = QLineEdit()
        # self.file_rows_line.setFixedWidth(50)

        self.file_cols_label = QLabel("Columns:")
        self.file_cols_label.setFixedWidth(45)

        self.file_cols_line = QLineEdit()
        self.file_cols_line.setMaxLength(4)
        self.file_cols_line.returnPressed.connect(self.col_num_given)
        # self.file_cols_line.setFixedWidth(50)

        fa_layout.addWidget(self.file_rows_label, 0, 0)
        fa_layout.addWidget(self.file_rows_line, 0, 1)
        fa_layout.addWidget(self.file_cols_label, 0, 2)
        fa_layout.addWidget(self.file_cols_line, 0, 3)

        sublayout_2.addWidget(self.file_attributes, Qt.AlignCenter)

        """Parameters"""
        self.parameters = QGroupBox("Parameters")
        param_layout = QVBoxLayout()
        self.parameters.setLayout(param_layout)

        self.param_button = QPushButton("Enter Parameters")
        param_layout.addWidget(self.param_button)
        self.param_button.clicked.connect(self.parameters_dialog)

        sublayout_2.addWidget(self.parameters)

        """Menu Bar"""
        menubar = QMenuBar()
        menu_file = menubar.addMenu("&File")
        menu_edit = menubar.addMenu("&Edit")

        replace = menu_edit.addAction("Replace")
        replace.setShortcut("Ctrl+R")
        replace.triggered.connect(lambda x: (self.hey_listen(x)))

        self.setMenuBar(menubar)

        dummy = QWidget(self)
        dummy.setLayout(master_layout)
        self.setCentralWidget(dummy)

    def file_dialog(self):
        dialog = QFileDialog()
        dialog.setNameFilters(["Text files (*.txt)", "Log Files (*.LOG), (*.log)"])
        dialog.selectNameFilter("Text files (*.txt)")

        if dialog.exec_():
            filenames = dialog.selectedFiles()
            f = open(filenames[0], 'r')

            self.label.setStyleSheet("color: lightGray;"
                                     "background-color: rgb(17,102,0);"
                                     "border-radius: 5px")
            self.label.setText("Opened")

            self.file_line.setText(dialog.selectedFiles()[0])

            with f:
                contents = f.read()
                self.frame.setPlainText(contents)
                self.tab.addTab(self.frame, f.name)
                # self.frame.insertPlainText(dialog.selectedFiles()[0])
                # self.frame.insertPlainText("\n")

            f.close()
            f = open(filenames[0])
            self.file_rows_line.setText(str(len(f.readlines())))

    def read_file(self):
        f = open(self.file_line.text())
        self.label.setStyleSheet("color: lightGray;"
                                 "background-color: rgb(17,102,0);"
                                 "border-radius: 5px;")
        self.label.setText("Opened")

        with f:
            data = f.read()
            self.frame.setPlainText(data)
            # self.frame.insertPlainText(dialog.selectedFiles()[0])
            # self.frame.insertPlainText("\n")

    def file_opened(self):
        if self.me is None:
            self.me = CWindow()
            self.me.show()
        else:
            self.me.close()
            self.me = None

    def col_num_given(self):
        print(self.file_cols_line.text())

    def hey_listen(self, x):
        print("Hey, listen!")
        # Open toolbar (replace options)

    def parameters_dialog(self):
        if self.w is None:
            self.w = ParamDialog(self.file_line.text())
            self.w.show()
        else:
            self.w = None


app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

window = MainWindow()
window.setFixedSize(960, 540)
window.setWindowTitle("Log Analyzer")
window.show()
sys.exit(app.exec_())
