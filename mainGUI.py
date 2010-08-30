# import sys
# from PyQt4.QtGui import QApplication
# from window import Window

#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    window = Window()
#    window.show()
#    sys.exit(app.exec_())
import sys
from PyQt4 import QtGui
from ui_window import Ui_MainWindow

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())