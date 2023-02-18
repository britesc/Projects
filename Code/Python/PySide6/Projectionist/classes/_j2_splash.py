#!/usr/bin/env python3
# coding: utf-8

from PySide6.QtWidgets import QSplashScreen
from PySide6.QtGui import QPixmap
from classes._j2_utilities import J2_Utilities


class J2_Splash:
    """ A Class for the Splash Screen """

    def __init__(self, app) -> None:
        """ The __init__ Function """
        super().__init__()
        self.app = app
        pixmap = QPixmap(":images/images/splash.png")
        self.splash = QSplashScreen(pixmap)
        self.vJ2U = J2_Utilities()

    def __str__(self) -> str:
        """ The __str__ Function """
        return "J2 Utilities"

    def __repr__(self) -> str:
        """ The __repr__ Function """
        return "J2_Utilities"

    def getVersion(self) -> str:
        """ The Version String of this Class """
        vVersion = "1.0.0"
        return vVersion

    def show(self, duration) -> None:
        """ Show the Splash Screen """
        self.duration = duration
        self.splash.show()

        while self.duration > 0:
            self.vJ2U.j2Sleep(1)

            self.app.processEvents()
            self.duration = self.duration - 1

    def hide(self, window) -> None:
        """ Hide the Splash Screen """
        self.app.processEvents()
        self.window = window
        self.splash.finish(window)
