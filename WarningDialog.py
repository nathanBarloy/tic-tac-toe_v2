# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:10:11 2020

@author: Nathan Barloy
"""

from PyQt5.QtWidgets import QDialog

from WarningUI import Ui_WarningDialog


class WarningDialog(Ui_WarningDialog, QDialog):
    def __init__(self, app):
        super(WarningDialog, self).__init__()
        self.app = app
        self.setupUi(self)
    
    def mouseReleaseEvent(self, event):
        self.app.removeWarning()