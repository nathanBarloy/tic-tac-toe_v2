# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 08:32:27 2020

@author: Nathan Barloy
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import QCoreApplication, QTranslator
from PyQt5.Qt import Qt

from MainMenu import MainWindow
from SubMenu import SubMenu
from Board import Board


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget(self)
        self.setWindowTitle('Tic-Tac-Toe')
        self.currentTranslator = None
        self.stackDict = {}
        
        self._mainWindow = MainWindow(self)
        self._subMenu = SubMenu(self)
        self._board = Board(self)
        
        self.stack.addWidget(self._mainWindow)
        self.stackDict["main"] = 0
        self.stack.addWidget(self._subMenu)
        self.stackDict["sub"] = 1
        self.stack.addWidget(self._board)
        self.stackDict["board"] = 2
        
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.stack)
        self.setLayout(hbox)

    def keyPressEvent(self, event):
        print("cc")
        if event.key()==Qt.Key_Escape:
            self.close()
            QApplication.quit()
    
    """
    def paintEvent(self, event):# set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./data/images/background.jpg")#Change to the relative path of your own image
        painter.drawPixmap(self.rect(), pixmap)
    """
    
    def display(self, name):
        self.stack.setCurrentIndex(self.stackDict[name])
    
    def changeLanguage(self, lang):
        if self.currentTranslator is not None :
            QCoreApplication.removeTranslator(self.currentTranslator)
        if lang=='en':
            self.currentTranslator = None
        else:
            self.currentTranslator = QTranslator()
            self.currentTranslator.load('data/translations/mainform_'+lang)
            QCoreApplication.installTranslator(self.currentTranslator)
        for i in range(self.stack.count()):
            self.stack.widget(i).retranslateUi(self)
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        w = MyApp()
        #w.paintEngine()
        w.show()
        #w.showFullScreen()
        sys.exit(app.exec_())
    except Exception:
        w.close()
        QApplication.quit()
        raise
