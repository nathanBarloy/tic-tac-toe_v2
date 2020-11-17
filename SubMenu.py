# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:28:25 2020

@author: Nathan Barloy
"""

from PyQt5.QtWidgets import QWidget

from MenuForm import Ui_Form


class SubMenu(Ui_Form, QWidget):
    def __init__(self, app):
        super(SubMenu, self).__init__()
        self.app = app
        self.setupUi(self)
        self.connectButtons()
        
    def connectButtons(self):
        self.buttonMenu.clicked.connect(lambda: self.app.display('main'))
        self.buttonPlay.clicked.connect(lambda: self.app.display('board'))