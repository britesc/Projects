import qdarktheme

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import QSettings
from PySide6.QtWidgets import QFileDialog
from pathlib import Path

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.settings = QSettings()
        self.setupUi(self)
        self.app = app

        self.setWindowTitle("Projectionist Configuration")

        self.actionExit.triggered.connect(self.MWExit)
        self.actionSettings.triggered.connect(self.MWSettings)
        self.actionLight.triggered.connect(self.MWlight)
        self.actionDark.triggered.connect(self.MWdark)
        self.actionAuto.triggered.connect(self.MWauto)
        self.actionTheme.triggered.connect(self.theme)
        self.actionAbout.triggered.connect(self.MWAbout)
        self.actionAboutQt.triggered.connect(self.MWAboutQt)
        self.pushButtonPFLocate.clicked.connect(self.PFLocate)
        self.pushButtonPFSave.clicked.connect(self.dummy_function)
        self.pushButtonPFCancel.clicked.connect(self.PFSettings)
        self.lineEditPFConfig.textChanged.connect(self.dummy_function)

        self.MWSettings()

    def dummy_function(self) -> None:
        print("Dummy Function Called")

    def MWExit(self) -> None:
        self.app.quit()

    def MWSettings(self) -> None:

        vMWTheme = self.settings.value("Window/Theme", "auto")
        match vMWTheme:
            case "auto":
                self.MWauto()
            case "dark":
                self.MWdark()
            case "light":
                self.MWlight()
            case _:
                self.MWauto()
        self.PFSettings()

    def MWlight(self) -> None:
        qdarktheme.setup_theme("light")
        self.settings.setValue("Window/Theme", "light")

    def MWdark(self) -> None:
        qdarktheme.setup_theme("dark")
        self.settings.setValue("Window/Theme", "dark")

    def MWauto(self) -> None:
        qdarktheme.setup_theme("auto")
        self.settings.setValue("Window/Theme", "auto")

    def theme(self) -> None:
        vMWTheme = self.settings.value("Window/Theme", "auto")
        match vMWTheme:
            case "auto":
                self.MWdark()
            case "dark":
                self.MWlight()
            case "light":
                self.MWauto()
            case _:
                self.MWauto()

    def MWAbout(self) -> None:
        QMessageBox.information(self, "Rubbish!", " Rubbish!")

    def MWAboutQt(self) -> None:
        QApplication.aboutQt()

    def PFSettings(self) -> None:
        settings = QSettings()

        vProjectLocation = settings.value("Project/Folder", False)

        if vProjectLocation is not False:
            self.lineEditPFConfig.setText(vProjectLocation)
            self.pushButtonPFSave.setEnabled(True)
        else:
            self.lineEditPFConfig.setText("Please Enter Project Folder")
            self.pushButtonPFSave.setEnabled(False)

    def PFLocate(self) -> str:
        dir = QFileDialog.getExistingDirectory(self,
                                               "Choose Project Directory",
                                               "/home",
                                               QFileDialog.ShowDirsOnly |
                                               QFileDialog.DontResolveSymlinks)

        self.lineEditPFConfig.setText(dir)

    def PFChanged(self) -> None:
        vCheckPath = self.lineEditPFConfig.text()
        vRealPath = Path(vCheckPath).is_dir()
        if vRealPath is True:
            self.pushButtonPFSave.setEnabled(True)
            self.pushButtonPFCancel.setEnabled(True)
        else:
            self.pushButtonPFSave.setEnabled(False)
            self.pushButtonPFCancel.setEnabled(False)
