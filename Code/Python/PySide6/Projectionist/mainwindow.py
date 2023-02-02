import qdarktheme

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QFileDialog
from pathlib import Path

from ui_mainwindow import Ui_MainWindow
from dialogs.aboutdialog import AboutDialog
from classes._j2_settings import J2_Settings as V2JS


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.setWindowTitle("Projectionist Configuration")

        self.actionExit.triggered.connect(self.MWExit)
        """ self.actionSettings.triggered.connect(self.MWSettings) """
        self.actionLight.triggered.connect(self.MWlight)
        self.actionDark.triggered.connect(self.MWdark)
        self.actionAuto.triggered.connect(self.MWauto)
        self.actionTheme.triggered.connect(self.MWTheme)
        self.actionAbout.triggered.connect(self.MWAbout)
        self.actionAboutQt.triggered.connect(self.MWAboutQt)
        self.pushButtonPFLocate.clicked.connect(self.PFLocate)
        self.pushButtonPFSave.clicked.connect(self.PFSave)
        self.pushButtonPFCancel.clicked.connect(self.PFCancel)
        self.lineEditPFConfig.textChanged.connect(self.PFChanged)

        self.aboutDialog = AboutDialog()

        """
            When the window is created we first have to
            ensure that the Theme is Set
            Next we have to make sure that Tab 0 is showing
            We use self.MWSettings() to senure all MainWindow Functionality is
            correct.
            Next we ensure Config Tab bittons are off.
            And that and Line Edit Content is displayed
            We use self.PFSettings() to ensure all Config Tabs functionality
            is set.
            If there is a change to the line edit, we need to check it is a
            valid Dir.
            If the tab is shown we await an action
            1. If Locate is pressed we go to self.PFLocate()
                Which opens a directory find and save dislog box
                and displays result in the lineEditPFConfig
            2. If there is any change to the lineEditPFConfig
                then self.PFChanged() is called.
            3. If self.PFChanged() is happy that line entry is a dir it
                will enable the save and canel buttons which calls
                self.PFSave() or self.PFCancel() as appropriate
            4. PFSave writes the value from lineEdit to the
                settings config file. Buttons are disabled again
            5. PFCancel retrieves the value from the settings file and
            reinserts it into the line Edit. Buttons are disabled again.
        """

        self.MWSettings()
        self.PFSettings()

    """ START OF MAINWINDOW CODE """

    def MWExit(self) -> None:
        self.app.quit()

    def MWSettings(self) -> None:
        vMWTheme = V2JS.getSetting(self, "Window/Theme", "auto")
        match vMWTheme:
            case "auto":
                self.MWauto()
            case "dark":
                self.MWdark()
            case "light":
                self.MWlight()
            case _:
                self.MWauto()
        self.tabWidget.setCurrentIndex(0)

    def MWlight(self) -> None:
        qdarktheme.setup_theme("light")
        V2JS.setSetting(self, "Window/Theme", "light")
        self.actionLight.setChecked(True)
        self.actionDark.setChecked(False)
        self.actionAuto.setChecked(False)

    def MWdark(self) -> None:
        qdarktheme.setup_theme("dark")
        V2JS.setSetting(self, "Window/Theme", "dark")
        self.actionLight.setChecked(False)
        self.actionDark.setChecked(True)
        self.actionAuto.setChecked(False)

    def MWauto(self) -> None:
        qdarktheme.setup_theme("auto")
        V2JS.setSetting(self, "Window/Theme", "auto")
        self.actionLight.setChecked(False)
        self.actionDark.setChecked(False)
        self.actionAuto.setChecked(True)

    def MWTheme(self) -> None:
        vMWTheme = V2JS.getSetting(self, "Window/Theme", "auto")
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
        '''QMessageBox.information(self, "Rubbish!", " Rubbish!")'''
        self.aboutDialog.exec()

    def MWAboutQt(self) -> None:
        QApplication.aboutQt()

    """ END OF MAINWINDOW CODE """

    """ START OF CONFIG TAB CODE """

    def PFSettings(self) -> None:
        self._tabConfigButtonsOff()
        vPFLocation = V2JS.getSetting(self, "Project/Folder", False)
        if vPFLocation:
            self.lineEditPFConfig.setText(vPFLocation)

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
            self._tabConfigButtonsOn()
        else:
            self._tabConfigButtonsOff()

    def PFSave(self) -> None:
        vCheckPath = self.lineEditPFConfig.text()
        V2JS.setSetting(self, "Project/Folder", vCheckPath)
        self._tabConfigButtonsOff()

    def PFCancel(self) -> None:
        vPFLocation = V2JS.getSetting(self, "Project/Folder", False)
        if vPFLocation:
            self.lineEditPFConfig.setText(vPFLocation)
        self._tabConfigButtonsOff()

    def _tabConfigButtonsOn(self) -> None:
        self.pushButtonPFSave.setEnabled(True)
        self.pushButtonPFCancel.setEnabled(True)

    def _tabConfigButtonsOff(self) -> None:
        self.pushButtonPFSave.setEnabled(False)
        self.pushButtonPFCancel.setEnabled(False)

    """ END OF CONFIG TAB CODE """
