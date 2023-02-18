#!/usr/bin/env python3
# coding: utf-8

import sys
import qdarktheme
import traceback

from PySide6.QtWidgets import QApplication, QSplashScreen
from PySide6.QtGui import QPixmap

from mainwindow import MainWindow
from classes._j2_utilities import J2_Utilities
from classes._j2_settings import J2_Settings


def main():
    try:
        app = QApplication(sys.argv)
        pixmap = QPixmap(":images/images/splash.png")

        vJ2S = J2_Settings("J2Casa", "Projectionist")
        vJ2S.setDefaults()
        vJ2U = J2_Utilities()

        splash = QSplashScreen(pixmap)
        splash.show()
        looper = 5

        while looper > 0:
            vJ2U.j2Sleep(1)

            app.processEvents()
            looper = looper - 1

        app.processEvents()
        qdarktheme.setup_theme()
        w = MainWindow(app)
        w.show()
        splash.finish(w)

    except Exception as err:
        print("Unfortunately Projectionist has encountered an error \
and is unable to continue.")
        print(f"Exception {err=}, {type(err)=}")
        traceback.print_exc()
        traceback.print_exception()

    finally:
        sys.exit(app.exec())


if __name__ == '__main__':
    main()
