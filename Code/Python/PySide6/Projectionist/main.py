#!/usr/bin/env python3
# coding: utf-8


import sys
import time

from PySide6.QtWidgets import QApplication, QSplashScreen 
from PyQt6.QtCore import QSettings, QCoreApplication
from PySide6.QtGui import QPixmap

from mainwindow import MainWindow

import splash_rc

global vProjectLocation
global vDatabaseLocation

def main():
    try:
        QCoreApplication.setOrganizationName("J2Casa") 
        QCoreApplication.setApplicationName("Projectionist")
        settings = QSettings()
        
        vProjectLocation = settings.value("Project/Folder", False)
        vDatabaseLocation = settings.value("Database/Folder", False)
        
        if vProjectLocation == False:
            print(f"vProjectLocation = {vProjectLocation}")
            settings.setValue("Project/Folder", "")
        if vDatabaseLocation == False:
            print(f"vDatabaseLocation = {vDatabaseLocation}")
            settings.setValue("Database/Folder", "")
            
        app = QApplication(sys.argv)
        pixmap = QPixmap(":images/images/splash.png")
        splash = QSplashScreen(pixmap)
        splash.show()
        looper = 5
        while looper > 0:
            time.sleep(1)
            app.processEvents()
            looper = looper -1

        app.processEvents()
        
        w = MainWindow(app)
        w.show()
        splash.finish(w)
                
    except:
        print(f"Unfortunately Projectionist has encountered an error and is unable to continue.")
    
    finally:
        sys.exit(app.exec())        


if __name__ == '__main__':
    main()
    
    