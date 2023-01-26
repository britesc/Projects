#!/usr/bin/env python3
# coding: utf-8

import os
import sys

from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

def main():
    try:
        app = QApplication(sys.argv)
        w = MainWindow(app)
        w.show()
                
    except:
        print(f"Unfortunately Projectionist has encountered an error and is unable to continue.")
    
    finally:
        sys.exit(app.exec())        


if __name__ == '__main__':
    main()
    
    