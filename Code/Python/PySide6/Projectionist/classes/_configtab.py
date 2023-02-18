#!/usr/bin/env python3
# coding: utf-8

from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QFileDialog
from ui_mainwindow import Ui_MainWindow
from classes._j2_settings import J2_Settings as V4JS
from pathlib import Path


class J2_ConfigTab:

    def __init__(self) -> None:
        super().__init__()
        self.MyWin = QMainWindow(Ui_MainWindow)
        

    def __str__(self) -> str:
        """ The __str__ Function """
        return "J2_ConfigTab"

    def __repr__(self) -> str:
        """ The __repr__ Function """
        return "J2_ConfigTab"

    def getVersion(self) -> str:
        """ The Version String of this Class """
        vVersion = "1.0.0"
        return vVersion

    def isPFValid() -> bool:
        """ Is the Project Folder Valid """
        vTemp1 = V4JS.value("Project/Folder", False)
        vRealPath = Path(vTemp1).is_dir()
        if vRealPath:
            return True
        else:
            return False

    def setPFLineEdit(self) -> None:
        """ Set the Project Folder into the lineEdit """
        vTemp1 = V4JS.value("Project/Folder", False)
        if vTemp1:
            self.MyWin    lineEditPFConfig.setText(vTemp1)