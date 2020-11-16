# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:17:24 2020

@author: Nathan Barloy
"""

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import QCoreApplication, QTranslator
from PyQt5.Qt import Qt

from MainForm import Ui_MainForm


class MainWindow(Ui_MainForm, QWidget):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.app = app
        self.setupUi(self)
        self.currentTranslator = None
        self.setWindowTitle('Tic-Tac-Toe')
        self.connectButtons()
    
    def changeLanguage(self, lang):
        if self.currentTranslator is not None :
            QCoreApplication.removeTranslator(self.currentTranslator)
        if lang=='en':
            self.currentTranslator = None
        else:
            self.currentTranslator = QTranslator()
            self.currentTranslator.load('data/translations/mainform_'+lang)
            QCoreApplication.installTranslator(self.currentTranslator)
        self.retranslateUi(self)
        
    def connectButtons(self):
        self.buttonFr.clicked.connect(lambda: self.changeLanguage('fr'))
        self.buttonEn.clicked.connect(lambda: self.changeLanguage('en'))
        self.buttonStart.clicked.connect(lambda: self.app.display('sub'))
        