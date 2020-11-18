# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuform.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1375, 1032)
        Form.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonPlay = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.buttonPlay.setFont(font)
        self.buttonPlay.setObjectName("buttonPlay")
        self.verticalLayout.addWidget(self.buttonPlay, 0, QtCore.Qt.AlignHCenter)
        self.buttonMenu = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.buttonMenu.setFont(font)
        self.buttonMenu.setObjectName("buttonMenu")
        self.verticalLayout.addWidget(self.buttonMenu, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Blablabla"))
        self.buttonPlay.setText(_translate("Form", "Play"))
        self.buttonMenu.setText(_translate("Form", "Back"))

