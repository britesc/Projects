#!/usr/bin/env python3
# coding: utf-8


from PySide6.QtWidgets import QDialog
from dialogs.ui_aboutdialog import Ui_aboutDialog

_ProjectionistVersionMajor = "0"
_ProjectionistVersionMinor = "0"
_ProjectionistVersionBuild = "0"
_ProjectionistVersionCompile = "1000"
_ProjectionistVersion = f"{_ProjectionistVersionMajor}.{_ProjectionistVersionMinor}.{_ProjectionistVersionBuild}.{_ProjectionistVersionCompile}"


class AboutDialog(QDialog, Ui_aboutDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("About Projectionist")
        vTemp1 = f"Version: {_ProjectionistVersion}"
        self.labelVersion.setText(vTemp1)

        self.pushButtonClose.clicked.connect(self.close)

    def close(self) -> None:
        self.reject()
