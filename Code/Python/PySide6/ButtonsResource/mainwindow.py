from PySide6.QtCore import Qt
from PySide6.QtGui import QClipboard
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox


from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        
        # File
        self.actionMenuSave.triggered.connect(self.save)
        self.actionMenuSaveAs.triggered.connect(self.saveas)
        self.actionMenuExit.triggered.connect(self.quit)
        
        #Edit
        self.actionMenuCopy.triggered.connect(self.copy)
        self.actionMenuCut.triggered.connect(self.cut)
        self.actionMenuPaste.triggered.connect(self.paste)
        self.actionMenuClear.triggered.connect(self.clear)
        self.actionMenuRedo.triggered.connect(self.redo)
        self.actionMenuUndo.triggered.connect(self.undo)
        self.actionMenuSelectAll.triggered.connect(self.selectall)
        
        #Settings
        self.actionMenuConfigure.triggered.connect(self.configure)
        
        
        #Window
        self.actionMenuMinimise.triggered.connect(self.minimise)
        self.actionMenuMaximise.triggered.connect(self.maximise)
        
        #Help
        self.actionMenuContextHelp.triggered.connect(self.contexthelp)
        self.actionMenuAbout.triggered.connect(self.about)
        self.actionMenuAboutQt.triggered.connect(self.qtabout)
        
        #My Musings
        
    #File    
    def save(self):
        pass

    def saveas(self):
        pass        
        
    def quit(self):
        self.app.quit()
    
    #Edit    
    def copy(self):
        self.__na
    
    def cut(self):
        pass
    
    def paste(self):
        pass
    
    def clear(self):
        pass
    
    def redo(self):
        pass
    
    def undo(self):
        pass
    
    def selectall(self):
        pass
            
            
    #Settings
    def configure(self):
        pass   
    
    #Window
    def minimise(self):
        pass
    
    def maximise(self):
        pass   
    
    #Help        
    def contexthelp(self):
        pass
    
    def about(self):
        self.aboutDialogBox()
    
    def qtabout(self):
        QApplication.aboutQt()    
    
    #My Musings
    def aboutDialogBox(self):
        QMessageBox.information(self,"Going pro!","QMainWindow,Qt Designer and Resources : Going pro!")


