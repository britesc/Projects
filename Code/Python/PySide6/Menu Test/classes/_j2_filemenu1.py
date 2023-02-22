import sys
from PySide6.QtWidgets import (
    QWidgetAction,
    QMenuBar
)

class J2_FileMenu1(QMenuBar):

    def __init__(self, menubar):
        super().__init__()
        
        menu = menubar
        menu.clear()
        menuBarFile = menu.addMenu("&File")
        
        menuBarFileSub = menuBarFile.addMenu("&Exit")
        menuBarFileSub = menuBarFile.addMenu("&Exit")
        # menuBarFile.addAction(self.actionExit)
        

        


    def actionExit() -> None:
        sys.exit()

