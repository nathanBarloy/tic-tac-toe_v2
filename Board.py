# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 08:49:42 2020

@author: Nathan Barloy
"""

from PyQt5.QtWidgets import QWidget

from BoardUI import Ui_Board


class Board(Ui_Board, QWidget):
    def __init__(self, app):
        super(Board, self).__init__()
        self.app = app
        self.setupUi(self)
        self.connectButtons()
        
    def connectButtons(self):
        self.buttonBack.clicked.connect(lambda: self.app.display('sub'))