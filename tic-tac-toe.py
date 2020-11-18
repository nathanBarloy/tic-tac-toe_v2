# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 08:32:27 2020

@author: Nathan Barloy
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QHBoxLayout, QDialog, QLabel
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import QCoreApplication, QTranslator, QTimer
from PyQt5.Qt import Qt

from MainMenu import MainWindow
from SubMenu import SubMenu
from Board import Board
from WarningDialog import WarningDialog

IDLE_TIME = 5000
WARNING_TIME = 3000

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tic-Tac-Toe')
        self.resize(2500,1400)
        
        self.currentTranslator = None
        self.stack = QStackedWidget(self)
        self.stackDict = {}
        
        # the different windows to show
        self._mainWindow = MainWindow(self)
        self._subMenu = SubMenu(self)
        self._board = Board(self)
        
        self.stack.addWidget(self._mainWindow)
        self.stackDict["main"] = 0
        self.stack.addWidget(self._subMenu)
        self.stackDict["sub"] = 1
        self.stack.addWidget(self._board)
        self.stackDict["board"] = 2
        
        # init the timer
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.showWarning)
        
        self.timerWarning = QTimer()
        self.timerWarning.setSingleShot(True)
        self.timerWarning.timeout.connect(self.expiredWarning)
        
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.stack)
        self.setLayout(hbox)

    def keyPressEvent(self, event):
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
    
    def mouseReleaseEvent(self, event):
        if self.stack.currentIndex() > 0:
            self.timer.start(IDLE_TIME)
    
    def display(self, name):
        index = self.stackDict[name]
        if index == 0:
            self.timer.stop()
        else:
            self.timer.start(IDLE_TIME)
        self.stack.setCurrentIndex(index)
    
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
    
    def showWarning(self):
        self.msg = WarningDialog(self)
        self.timerWarning.start(WARNING_TIME)
        self.msg.exec_()
        
    def removeWarning(self):
        self.msg.close()
        self.timerWarning.stop()
        self.timer.start(IDLE_TIME)
        
    def expiredWarning(self):
        self.msg.close()
        self.display('main')
        
            

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
        sys.exit()
        raise
