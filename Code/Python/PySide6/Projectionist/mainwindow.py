from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox

from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        
        self.setWindowTitle("Projectionist Configuration")

        self.actionExit.triggered.connect(self.exit)
        self.actionSettings.triggered.connect(self.settings)
        self.actionLight.triggered.connect(self.light)
        self.actionDark.triggered.connect(self.dark)
        self.actionAuto.triggered.connect(self.auto)
        self.actionTheme.triggered.connect(self.theme)
        #self.actionAbout.triggered.connect(self.about)
        #self.actionAboutQt.triggered.connect(self.aboutQt)

    def exit(self):
        self.app.quit()
    def settings(self):
        pass
    def light(self):
        pass
    def dark(self):
        pass
    def auto(self):
        pass
    def theme(self):
        pass
    def about(self):
        QMessageBox.information(self,"Going pro!","QMainWindow,Qt Designer and Resources : Going pro!")
    def aboutQt(self):
        QApplication.aboutQt()    