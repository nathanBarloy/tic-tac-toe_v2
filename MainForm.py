# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1056, 773)
        MainForm.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(MainForm)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitle = QtWidgets.QLabel(MainForm)
        font = QtGui.QFont()
        font.setPointSize(45)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.labelIntro = QtWidgets.QLabel(MainForm)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.labelIntro.setFont(font)
        self.labelIntro.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIntro.setObjectName("labelIntro")
        self.verticalLayout.addWidget(self.labelIntro)
        self.buttonStart = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStart.sizePolicy().hasHeightForWidth())
        self.buttonStart.setSizePolicy(sizePolicy)
        self.buttonStart.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.buttonStart.setFont(font)
        self.buttonStart.setObjectName("buttonStart")
        self.verticalLayout.addWidget(self.buttonStart, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonLu = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonLu.sizePolicy().hasHeightForWidth())
        self.buttonLu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.buttonLu.setFont(font)
        self.buttonLu.setObjectName("buttonLu")
        self.horizontalLayout.addWidget(self.buttonLu)
        self.buttonfr = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonfr.sizePolicy().hasHeightForWidth())
        self.buttonfr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.buttonfr.setFont(font)
        self.buttonfr.setObjectName("buttonfr")
        self.horizontalLayout.addWidget(self.buttonfr)
        self.buttonDe = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDe.sizePolicy().hasHeightForWidth())
        self.buttonDe.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.buttonDe.setFont(font)
        self.buttonDe.setObjectName("buttonDe")
        self.horizontalLayout.addWidget(self.buttonDe)
        self.buttonEn = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonEn.sizePolicy().hasHeightForWidth())
        self.buttonEn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.buttonEn.setFont(font)
        self.buttonEn.setObjectName("buttonEn")
        self.horizontalLayout.addWidget(self.buttonEn)
        self.buttonPt = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonPt.sizePolicy().hasHeightForWidth())
        self.buttonPt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.buttonPt.setFont(font)
        self.buttonPt.setObjectName("buttonPt")
        self.horizontalLayout.addWidget(self.buttonPt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Form"))
        self.labelTitle.setText(_translate("MainForm", "Tic-Tac-Toe"))
        self.labelIntro.setText(_translate("MainForm", "Introduction"))
        self.buttonStart.setText(_translate("MainForm", "Start"))
        self.buttonLu.setText(_translate("MainForm", "Luxemburgish"))
        self.buttonfr.setText(_translate("MainForm", "Français"))
        self.buttonDe.setText(_translate("MainForm", "Deutsch"))
        self.buttonEn.setText(_translate("MainForm", "English"))
        self.buttonPt.setText(_translate("MainForm", "Portugues"))

