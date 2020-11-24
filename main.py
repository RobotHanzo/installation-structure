import sys

from PyQt5.QtWidgets import *
from initialization import Initialization

app = QApplication(sys.argv)
window = Initialization('Test thing', '0.0.0.0')
window.show()
sys.exit(app.exec_())
