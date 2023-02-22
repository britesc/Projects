from PySide6.QtWidgets import (
    QMainWindow
)
from ui_mainwindow import Ui_MainWindow
from classes._j2_filemenu1 import J2_FileMenu1


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        menubar = self.menubar

        self.setWindowTitle("Menu Test")
            
        vJ2M = J2_FileMenu1(menubar)
     
        

        
        
