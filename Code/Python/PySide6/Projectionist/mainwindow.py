from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox

from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        

        