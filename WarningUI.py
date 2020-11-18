# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WarningDialog(object):
    def setupUi(self, WarningDialog):
        WarningDialog.setObjectName("WarningDialog")
        WarningDialog.resize(871, 637)
        self.horizontalLayout = QtWidgets.QHBoxLayout(WarningDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(WarningDialog)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(WarningDialog)
        QtCore.QMetaObject.connectSlotsByName(WarningDialog)

    def retranslateUi(self, WarningDialog):
        _translate = QtCore.QCoreApplication.translate
        WarningDialog.setWindowTitle(_translate("WarningDialog", "WARNING"))
        self.label.setText(_translate("WarningDialog", "WARNING\n"
"\n"
"Touch the screen if you don\'t want to go back to the main menu."))

