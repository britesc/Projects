import qdarktheme

from PySide6.QtWidgets import QWidget, QTabWidget

from ui_tab2 import Ui_Tab2


class Tab2(QWidget, Ui_Tab2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        