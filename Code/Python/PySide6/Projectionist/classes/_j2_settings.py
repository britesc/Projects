#!/usr/bin/env python3
# coding: utf-8
from PyQt6.QtCore import QSettings, QCoreApplication


class J2_Settings:
    """ A Class for Settings """

    def __init__(self, OrgName, AppName) -> None:
        super().__init__()
        self.OrgName = OrgName
        self.AppName = AppName
        QCoreApplication.setOrganizationName(OrgName)
        QCoreApplication.setApplicationName(AppName)
        self.settings = QSettings()

    def __str__(self) -> str:
        """ The __str__ Function """
        return "J2_Settings"

    def __repr__(self) -> str:
        """ The __repr__ Function """
        return "J2_Settings"

    def getVersion(self) -> str:
        """ The Version String of this Class """
        vVersion = "1.0.0"
        return vVersion

    def setDefaults(self) -> None:
        """ Set the defaults for settings """
        vTemp1 = self.settings.value("Window/Theme", False)
        if vTemp1 is False:
            self.settings.setValue("Window/Theme", "auto")

        vTemp1 = self.settings.value("Project/Folder", False)
        if vTemp1 is False:
            self.settings.setValue("Project/Folder", "")

        vTemp1 = self.settings.value("Database/Folder", False)
        if vTemp1 is False:
            self.settings.setValue("Database/Folder", "Naturism")

    def setSetting(self, Context, Value) -> None:
        """ Set the Setting """
        self.Context = Context
        self.Value = Value
        self.settings.setValue(self.Context, self.Value)

    def getSetting(self, Context, Default) -> str:
        """ Get the Setting """
        self.Context = Context
        self.Default = Default
        vTemp1 = self.settings.value(Context, Default)
        if vTemp1 is False:
            vTemp1 = ""
        return vTemp1
