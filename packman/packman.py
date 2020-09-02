from gui import mainwindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import sys
import psutil


class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        timer = QTimer(self)
        timer.timeout.connect(self.update_label)
        timer.start()
        self.backlog.setText(str(0))

        reg_ex = QRegExp("[0-9]+.?[0-9]{,2}")
        input_validator = QRegExpValidator(reg_ex, self.backlog)
        self.backlog.setValidator(input_validator)

    def update_label(self):
        # Make sure that we only use values that can be taken as numeric data
        try:
            backlog = float(self.backlog.text())
        except ValueError:
            backlog = 0

        data = psutil.net_io_counters().bytes_recv
        gb = round((data / 1024 ** 3) - backlog / 1024, 2)
        mb = round((data / 1024 ** 2) - backlog, 2)
        self.val_gb.setText(str(gb) + "GB")
        self.val_mb.setText(str(mb) + "MiB")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
