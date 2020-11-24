from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Initialization(QMainWindow):
    def __init__(self, program_name, program_version, *args, **kwargs):
        super(Initialization, self).__init__(*args, **kwargs)
        self.program_name = program_name
        self.program_version = program_version
        self.setWindowTitle(f'{program_name} Installer')
        self.setMaximumSize(640, 480)
        self.setMinimumSize(640, 480)
        self.setStyleSheet("QLabel {font: 30pt Microsoft Sans Serif}")
        welcome_large_label = QLabel(f'{program_name} Installer')
        welcome_large_label.setAlignment(Qt.AlignTop)
        self.setCentralWidget(welcome_large_label)
