from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox
from PyQt6.QtCore import QSettings, QCoreApplication

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
        self.actionAbout.triggered.connect(self.about)
        self.actionAboutQt.triggered.connect(self.aboutQt)
        self.pushButtonProjectFolderLocate.clicked.connect(self.ProjectFolderLocate)
        self.pushButtonProjectFolderSave.clicked.connect(self.dummy_function)
        self.pushButtonProjectFolderCancel.clicked.connect(self.dummy_function)
        
    def dummy_function(self):
        print(f"Dummy Function Called")
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
    def ProjectFolderLocate(self):
        pass
    
    def projectfoldercancel(self):
        self.projectlolderlineedit(self)
        
    
    def projectlolderlineedit(self):
        settings = QSettings()
        
        vProjectLocation = settings.value("Project/Folder", False)
        
        if vProjectLocation != False:
           self.projectlolderlineedit.setText(vProjectLocation)
           self.pushButtonProjectFolderSave.setEnabled(True)
        else:
           self.projectlolderlineedit.setText("          Please Enter Project Main Folder")
           self.pushButtonProjectFolderSave.setEnabled(False)    
                       
        
        