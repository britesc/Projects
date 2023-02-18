import qdarktheme

from PySide6.QtWidgets import QMainWindow, QTabWidget

from ui_mainwindow import Ui_MainWindow
from tab1 import Tab1 
from tab2 import Tab2


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.setWindowTitle("Tab Test")
        
        taba1 = Tab1()
        self.tabWidget.addTab(taba1, "Information")

        taba2 = Tab2()
        self.tabWidget.addTab(taba2, "Naturism")
