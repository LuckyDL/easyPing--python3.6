# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyPing.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_MyPing(object):
    def setupUi(self, MyPing):
        MyPing.setObjectName("MyPing")
        MyPing.setWindowIcon(QtGui.QIcon("ping.ico"))
        # MyPing.resize(660, 385)
        MyPing.setMaximumSize(QtCore.QSize(660, 425))
        MyPing.setMinimumSize(QtCore.QSize(660, 425))
        self.groupBox = QtWidgets.QGroupBox(MyPing)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 470, 50))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 20, 441, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startIP = QtWidgets.QLineEdit(self.widget)
        self.startIP.setText("192.168.0.0")
        self.startIP.selectAll()
        self.startIP.setObjectName("startIP")
        self.horizontalLayout.addWidget(self.startIP)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.endIP = QtWidgets.QLineEdit(self.widget)
        self.endIP.setObjectName("endIP")
        self.horizontalLayout.addWidget(self.endIP)
        self.pingButton = QtWidgets.QPushButton(self.widget)
        self.pingButton.setObjectName("pingButton")
        self.horizontalLayout.addWidget(self.pingButton)
        self.widget1 = QtWidgets.QWidget(MyPing)
        self.widget1.setGeometry(QtCore.QRect(10, 70, 630, 345))
        self.widget1.setObjectName("widget1")
        self.gridlayout = QtWidgets.QGridLayout(self.widget1)
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setObjectName("gridlayout")
        self.gridlayout.setSpacing(7)

        self.label_list = []
        list_index = 0
        for i in range(1, 17):
            for j in range(1, 17):
                label = QtWidgets.QLabel(self.widget1)
                label.setMinimumSize(QtCore.QSize(32, 15))
                label.setStyleSheet("background-color: rgb(203, 203, 203);")
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setText(QtCore.QCoreApplication.translate("MyPing", str(list_index)))
                self.label_list.append(label)
                self.gridlayout.addWidget(label, i-1, j-1, 1, 1)
                list_index += 1
        self.retranslateUi(MyPing)
        QtCore.QMetaObject.connectSlotsByName(MyPing)

    def retranslateUi(self, MyPing):
        _translate = QtCore.QCoreApplication.translate
        MyPing.setWindowTitle(_translate("MyPing", "MyPing"))
        self.groupBox.setTitle(_translate("MyPing", "Set IP Range"))
        self.label_2.setText(_translate("MyPing", "——"))
        self.pingButton.setText(_translate("MyPing", "Ping"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyPing = QtWidgets.QWidget()
    ui = Ui_MyPing()
    ui.setupUi(MyPing)
    MyPing.show()
    sys.exit(app.exec_())
