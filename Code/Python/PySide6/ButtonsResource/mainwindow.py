from PySide6.QtCore import Qt
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
        
        
        #Window
        
        
        #Help
        
        
    #File    
    def save(self):
        pass

    def saveas(self):
        pass        
        
    def quit(self):
        self.app.quit()
    
    #Edit    
    def copy(self):
        pass
    
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
    
    
    #Window
    
    
    #Help        