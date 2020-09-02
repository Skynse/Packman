from gui import mainwindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from tools.filter import to_gb, to_mb
import sys
import psutil


class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.setFixedSize(self.size())
        self.tray_icon.setIcon(
            self.style().standardIcon(QtWidgets.QStyle.SP_ComputerIcon)
        )

        tray_menu = QtWidgets.QMenu()

        show_action = QtWidgets.QAction("Show", self)
        quit_action = QtWidgets.QAction("Exit", self)
        hide = QtWidgets.QAction("Hide", self)

        show_action.triggered.connect(self.show)
        hide.triggered.connect(self.hide)
        quit_action.triggered.connect(self.quit)

        tray_menu.addAction(show_action)
        tray_menu.addAction(hide)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        timer = QTimer(self)
        timer.timeout.connect(self.update_label)
        timer.start()

        self.backlog.setText(str(0))

        reg_ex = QRegExp("[0-9]+.?[0-9]{,2}")
        input_validator = QRegExpValidator(reg_ex, self.backlog)
        self.backlog.setValidator(input_validator)

    def closeEvent(self, event):
        if self.hide_action.isChecked():
            event.ignore()
            self.hide()
            self.tray_icon.showMessage(
                    "Packman",
                    "Application was minimized to Tray",
                    QtWidgets.QSystemTrayIcon.Information,
                    2000
                )
        else:
            quit()

    def quit(self):
        self.close()
        sys.exit(0)

    def update_label(self):
        # Make sure that we only use values that can be taken as numeric data
        try:
            backlog = float(self.backlog.text())
        except ValueError:
            backlog = 0

        data = psutil.net_io_counters().bytes_recv
        data_up = psutil.net_io_counters().bytes_sent

        gb = round(to_gb(data) - backlog / 1024, 2)
        mb = round(to_mb(data) - backlog, 2)

        gb_up = to_gb(data_up)
        mb_up = to_mb(data_up)

        self.val_gb.setText(str(gb) + "GB")
        self.val_mb.setText(str(mb) + "MB")

        self.val_gb_up.setText(str(gb_up) + "GB")
        self.val_mb_up.setText(str(mb_up) + "MB")

        self.tray_icon.setToolTip(
            f"""Download:  {str(gb)} GB {str(mb)} MB
Upload:       {str(gb_up)} GB {str(mb_up)} MB""")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
