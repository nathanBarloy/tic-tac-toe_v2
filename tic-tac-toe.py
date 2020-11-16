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


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget(self)
        self.stackDict = {}
        
        self._mainWindow = MainWindow(self)
        self._subMenu = SubMenu(self)
        
        self.stack.addWidget(self._mainWindow)
        self.stackDict["main"] = 0
        self.stack.addWidget(self._subMenu)
        self.stackDict["sub"] = 1
        
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
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyApp()
    #w.paintEngine()
    w.show()
    #w.showFullScreen()
    sys.exit(app.exec_())