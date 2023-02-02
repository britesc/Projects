#!/usr/bin/env python3
# coding: utf-8

from PySide6.QtWidgets import QDialog
from ui_aboutdialog import Ui_aboutDialog


class AboutDialog(QDialog, Ui_aboutDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("About Projectionist")

        self.pushButtonClose.clicked.connect(self.close)

    def close(self) -> None:
        self.reject()
