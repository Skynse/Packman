# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'packman/gui/ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 505)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(674, 505))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(6, 6, 661, 431))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.data = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.data.setFont(font)
        self.data.setAlignment(QtCore.Qt.AlignCenter)
        self.data.setObjectName("data")
        self.verticalLayout.addWidget(self.data)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.val_gb = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.val_gb.setFont(font)
        self.val_gb.setText("")
        self.val_gb.setObjectName("val_gb")
        self.gridLayout.addWidget(self.val_gb, 1, 0, 2, 1)
        self.val_mb_up = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.val_mb_up.setFont(font)
        self.val_mb_up.setText("")
        self.val_mb_up.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.val_mb_up.setObjectName("val_mb_up")
        self.gridLayout.addWidget(self.val_mb_up, 3, 2, 1, 1)
        self.val_gb_up = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.val_gb_up.setFont(font)
        self.val_gb_up.setText("")
        self.val_gb_up.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.val_gb_up.setObjectName("val_gb_up")
        self.gridLayout.addWidget(self.val_gb_up, 1, 2, 1, 1)
        self.val_mb = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.val_mb.setFont(font)
        self.val_mb.setText("")
        self.val_mb.setObjectName("val_mb")
        self.gridLayout.addWidget(self.val_mb, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.backlog = QtWidgets.QLineEdit(self.layoutWidget)
        self.backlog.setObjectName("backlog")
        self.verticalLayout.addWidget(self.backlog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStatistics = QtWidgets.QAction(MainWindow)
        self.actionStatistics.setObjectName("actionStatistics")
        self.hide_action = QtWidgets.QAction(MainWindow)
        self.hide_action.setCheckable(True)
        self.hide_action.setObjectName("hide_action")
        self.menuFile.addAction(self.actionStatistics)
        self.menuFile.addAction(self.hide_action)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Packman"))
        self.data.setText(_translate("MainWindow", "Data Usage"))
        self.label.setText(_translate("MainWindow", "Download"))
        self.label_3.setText(_translate("MainWindow", "Upload"))
        self.label_2.setText(_translate("MainWindow", "Backlog level"))
        self.backlog.setWhatsThis(_translate("MainWindow", "size to subtract from data"))
        self.backlog.setPlaceholderText(_translate("MainWindow", "size"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionStatistics.setText(_translate("MainWindow", "Statistics"))
        self.hide_action.setText(_translate("MainWindow", "Minimize to tray"))
