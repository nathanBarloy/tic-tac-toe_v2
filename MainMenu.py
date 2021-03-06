# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:17:24 2020

@author: Nathan Barloy
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

from MainForm import Ui_MainForm


class MainWindow(Ui_MainForm, QWidget):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.app = app
        self.setupUi(self)
        self.setupButtons()
        self.connectButtons()
        
    def setupButtons(self):
        self.buttonFr.setIcon(QIcon('data/images/francais.png'))
        
    def connectButtons(self):
        self.buttonFr.clicked.connect(lambda: self.app.changeLanguage('fr'))
        self.buttonEn.clicked.connect(lambda: self.app.changeLanguage('en'))
        self.buttonStart.clicked.connect(lambda: self.app.display('sub'))
        