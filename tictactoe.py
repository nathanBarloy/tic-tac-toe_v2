# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:17:24 2020

@author: Nathan Barloy
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import QCoreApplication, QTranslator
from PyQt5.Qt import Qt

from MainForm import Ui_MainForm


class MainWindow(Ui_MainForm, QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.currentTranslator = None
        self.setWindowTitle('Tic-Tac-Toe')
        self.connectButtons()
    
    """
    def paintEvent(self, event):# set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./data/background1.jpg")#Change to the relative path of your own image
        painter.drawPixmap(self.rect(), pixmap)
    """
    
    def keyPressEvent(self, event):
        print("cc")
        if event.key()==Qt.Key_Escape:
            self.close()
            QApplication.quit()
    
    def changeLanguage(self, lang):
        if self.currentTranslator is not None :
            QCoreApplication.removeTranslator(self.currentTranslator)
        if lang=='fr':
            self.currentTranslator = None
        else:
            self.currentTranslator = QTranslator()
            self.currentTranslator.load('firsttest-'+lang)
            QCoreApplication.installTranslator(self.currentTranslator)
        self.retranslateUi(self)
    
    def connectButtons(self):
        """
        self.buttonFr.clicked.connect(lambda: self.changeLanguage('fr'))
        self.buttonEn.clicked.connect(lambda: self.changeLanguage('en'))
        """
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    #w.paintEngine()
    w.show()
    sys.exit(app.exec_())