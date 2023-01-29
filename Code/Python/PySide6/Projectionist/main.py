#!/usr/bin/env python3
# coding: utf-8


import sys

from PySide6.QtWidgets import QApplication, QSplashScreen
from PyQt6.QtCore import QSettings, QCoreApplication
from PySide6.QtGui import QPixmap

from mainwindow import MainWindow
from classes import j2_utilities as vJ2

global vProjectLocation
global vDatabaseLocation


def main():
    try:
        QCoreApplication.setOrganizationName("J2Casa")
        QCoreApplication.setApplicationName("Projectionist")
        settings = QSettings()

        vProjectLocation = settings.value("Project/Folder", False)
        vDatabaseLocation = settings.value("Database/Folder", False)

        if vProjectLocation is False:
            print(f"vProjectLocation = {vProjectLocation}")
            settings.setValue("Project/Folder", "")
        if vDatabaseLocation is False:
            print(f"vDatabaseLocation = {vDatabaseLocation}")
            settings.setValue("Database/Folder", "")

        app = QApplication(sys.argv)
        pixmap = QPixmap(":images/images/splash.png")
        splash = QSplashScreen(pixmap)
        splash.show()
        looper = 5
        j2s = vJ2.J2_Utilities
        while looper > 0:
            j2s.j2Sleep(1)

            app.processEvents()
            looper = looper - 1

        app.processEvents()

        w = MainWindow(app)
        w.show()
        splash.finish(w)

    except Exception:
        print("Unfortunately Projectionist has encountered an error \
            and is unable to continue.")

    finally:
        sys.exit(app.exec())


if __name__ == '__main__':
    main()
