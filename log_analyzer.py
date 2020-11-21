import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        LEFT = Qt.AlignLeft

        master_layout = QHBoxLayout()

        sublayout = QVBoxLayout()
        master_layout.addLayout(sublayout)

        sublayout_2 = QVBoxLayout()
        master_layout.addLayout(sublayout_2)

        dsublayout = QFormLayout()
        sublayout_2.addLayout(dsublayout)

        self.group = QGroupBox()
        self.group.setFixedWidth(700)
        self.group_layout = QHBoxLayout()
        self.group.setLayout(self.group_layout)
        sublayout.addWidget(self.group, alignment=LEFT)

        self.file_line = QLineEdit()
        self.file_line.setFixedWidth(580)
        # self.file_line.setEditable(True)
        self.file_line.setPlaceholderText("Log File Location")
        # self.file_line.addItem("C:\\")
        self.group_layout.addWidget(self.file_line, alignment=LEFT)

        self.button = QPushButton("QFileDialog Object")
        self.button.clicked.connect(self.file_dialog)
        self.group_layout.addWidget(self.button, alignment=LEFT)

        self.label = QLabel("Waiting...")
        sublayout.addWidget(self.label, alignment=LEFT)

        self.frame = QTextEdit()
        self.frame.setFixedWidth(700)
        self.frame.setReadOnly(True)
        sublayout.addWidget(self.frame, alignment=LEFT)

        self.group_1 = QGroupBox()
        self.group_1.setStyleSheet("background-color: gray")

        self.parameter_l = QComboBox()
        self.parameter_l.setEditable(True)
        self.parameter_l.setPlaceholderText("Test")
        self.parameter_l.addItems(["[", "(", "{", "<", "\"", "\'"])

        self.parameter_r = QComboBox()
        self.parameter_r.setEditable(True)
        self.parameter_r.setPlaceholderText("Test 2")
        self.parameter_r.addItems(["]", ")", "}", ">", "\"", "\'"])

        dsublayout.layout().addRow('Left Parameter', self.parameter_l)
        dsublayout.layout().addRow('Right Parameter', self.parameter_r)

        dummy = QWidget()
        dummy.setLayout(master_layout)
        self.setCentralWidget(dummy)

    def file_dialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setNameFilters(["All Files (*)", "Text files (*.txt)", "Log Files (*.LOG), (*.log)"])
        dialog.selectNameFilter("All Files (*)")
        dialog.setDirectory("C:\\users\\isaac n. dominguez\\desktop")

        if dialog.exec_():
            filenames = dialog.selectedFiles()
            f = open(filenames[0], 'r')

            self.label.setStyleSheet("color: green")
            self.label.setText("Opened")

            self.file_line.setText(dialog.selectedFiles()[0])

            with f:
                data = f.read()
                self.frame.setText(data)
                # self.frame.insertPlainText(dialog.selectedFiles()[0])
                # self.frame.insertPlainText("\n")


app = QApplication(sys.argv)
window = MainWindow()
window.setMinimumSize(960, 540)
window.setWindowTitle("Demo")
window.show()
sys.exit(app.exec_())
