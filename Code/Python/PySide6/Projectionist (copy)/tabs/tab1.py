import qdarktheme

from PySide6.QtWidgets import QWidget, QTabWidget

from ui_tab1 import Ui_Tab1


class Tab1(QWidget, Ui_Tab1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        