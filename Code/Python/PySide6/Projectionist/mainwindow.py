
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import QSettings
from PySide6.QtWidgets import QFileDialog
from pathlib import Path

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
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
        self.pushButtonProjectFolderLocate.clicked.connect(self.PFLocate)
        self.pushButtonProjectFolderSave.clicked.connect(self.dummy_function)
        self.pushButtonProjectFolderCancel.clicked.connect(self.dummy_function)
        self.lineEditConfigProjectFolder.textChanged(self.PFChanged)

    def dummy_function(self) -> None:
        print("Dummy Function Called")

    def exit(self) -> None:
        self.app.quit()

    def settings(self) -> None:
        pass

    def light(self) -> None:
        pass

    def dark(self) -> None:
        pass

    def auto(self) -> None:
        pass

    def theme(self) -> None:
        pass

    def about(self) -> None:
        QMessageBox.information(self, "Rubbish!", " Rubbish!")

    def aboutQt(self) -> None:
        QApplication.aboutQt()

    def PFCancel(self) -> None:
        self.projectlolderlineedit(self)

    def projectlolderlineedit(self) -> None:
        settings = QSettings()

        vProjectLocation = settings.value("Project/Folder", False)

        if vProjectLocation is not False:
            self.projectlolderlineedit.setText(vProjectLocation)
            self.pushButtonProjectFolderSave.setEnabled(True)
        else:
            self.projectlolderlineedit.setText("Please Enter Project Folder")
            self.pushButtonProjectFolderSave.setEnabled(False)

    def PFLocate(self) -> str:
        dir = QFileDialog.getExistingDirectory(self,
                                               "Choose Project Directory",
                                               "/home",
                                               QFileDialog.ShowDirsOnly |
                                               QFileDialog.DontResolveSymlinks)

        self.lineEditConfigProjectFolder.setText(dir)

    def PFChanged(self) -> None:
        # if the line edit text is equal to a folder
        # enable the save pushbutton
        # enable the cancel pushbutton
        vCheckPath = self.lineEditConfigProjectFolder.text()
        vRealPath = Path(vCheckPath).is_dir()
        if vRealPath is True:
            self.pushButtonProjectFolderSave.setEnabled(True)
            self.pushButtonProjectFolderCancel.setEnabled(True)
        else:
            self.pushButtonProjectFolderSave.setEnabled(False)
            self.pushButtonProjectFolderCancel.setEnabled(False)
