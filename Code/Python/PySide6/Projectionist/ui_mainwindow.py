# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QToolBar, QVBoxLayout, QWidget)
import splash_rc
import buttons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(620, 480)
        MainWindow.setMinimumSize(QSize(620, 480))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon = QIcon()
        icon.addFile(u":/buttons/buttons/glassButtonExit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/buttons/glassButtonConfigure.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon1)
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.actionAuto = QAction(MainWindow)
        self.actionAuto.setObjectName(u"actionAuto")
        self.actionTheme = QAction(MainWindow)
        self.actionTheme.setObjectName(u"actionTheme")
        icon2 = QIcon()
        icon2.addFile(u":/buttons/buttons/glassButtonTheme.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionTheme.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayoutMain = QVBoxLayout()
        self.verticalLayoutMain.setObjectName(u"verticalLayoutMain")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabInfo = QWidget()
        self.tabInfo.setObjectName(u"tabInfo")
        self.verticalLayout = QVBoxLayout(self.tabInfo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayoutInfoTab = QGridLayout()
        self.gridLayoutInfoTab.setObjectName(u"gridLayoutInfoTab")
        self.labelInfoTitle = QLabel(self.tabInfo)
        self.labelInfoTitle.setObjectName(u"labelInfoTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.labelInfoTitle.sizePolicy().hasHeightForWidth())
        self.labelInfoTitle.setSizePolicy(sizePolicy)
        self.labelInfoTitle.setAlignment(Qt.AlignCenter)

        self.gridLayoutInfoTab.addWidget(self.labelInfoTitle, 0, 0, 1, 1)

        self.labelInfoDetails = QLabel(self.tabInfo)
        self.labelInfoDetails.setObjectName(u"labelInfoDetails")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(99)
        sizePolicy1.setHeightForWidth(self.labelInfoDetails.sizePolicy().hasHeightForWidth())
        self.labelInfoDetails.setSizePolicy(sizePolicy1)
        self.labelInfoDetails.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.labelInfoDetails.setWordWrap(True)
        self.labelInfoDetails.setMargin(5)
        self.labelInfoDetails.setIndent(-4)

        self.gridLayoutInfoTab.addWidget(self.labelInfoDetails, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayoutInfoTab)

        self.tabWidget.addTab(self.tabInfo, "")
        self.tabConfiguration = QWidget()
        self.tabConfiguration.setObjectName(u"tabConfiguration")
        self.gridLayout = QGridLayout(self.tabConfiguration)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayoutConfigProjectFolder = QVBoxLayout()
        self.verticalLayoutConfigProjectFolder.setObjectName(u"verticalLayoutConfigProjectFolder")
        self.horizontalLayoutConfigProjectFolder = QHBoxLayout()
        self.horizontalLayoutConfigProjectFolder.setSpacing(10)
        self.horizontalLayoutConfigProjectFolder.setObjectName(u"horizontalLayoutConfigProjectFolder")
        self.horizontalLayoutConfigProjectFolder.setContentsMargins(10, -1, 10, -1)
        self.labelConfigProjectFolder = QLabel(self.tabConfiguration)
        self.labelConfigProjectFolder.setObjectName(u"labelConfigProjectFolder")

        self.horizontalLayoutConfigProjectFolder.addWidget(self.labelConfigProjectFolder)

        self.lineEditConfigProjectFolder = QLineEdit(self.tabConfiguration)
        self.lineEditConfigProjectFolder.setObjectName(u"lineEditConfigProjectFolder")

        self.horizontalLayoutConfigProjectFolder.addWidget(self.lineEditConfigProjectFolder)


        self.verticalLayoutConfigProjectFolder.addLayout(self.horizontalLayoutConfigProjectFolder)


        self.gridLayout.addLayout(self.verticalLayoutConfigProjectFolder, 4, 0, 1, 1)

        self.gridLayoutConfigTab = QGridLayout()
        self.gridLayoutConfigTab.setObjectName(u"gridLayoutConfigTab")
        self.labelConfigTitle = QLabel(self.tabConfiguration)
        self.labelConfigTitle.setObjectName(u"labelConfigTitle")
        self.labelConfigTitle.setAlignment(Qt.AlignCenter)

        self.gridLayoutConfigTab.addWidget(self.labelConfigTitle, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayoutConfigTab, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayoutConfigButtonLocate = QHBoxLayout()
        self.horizontalLayoutConfigButtonLocate.setObjectName(u"horizontalLayoutConfigButtonLocate")
        self.horizontalSpacerTabConfigLineEditProjectFolderLeft = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutConfigButtonLocate.addItem(self.horizontalSpacerTabConfigLineEditProjectFolderLeft)

        self.pushButtonProjectFolderLocate = QPushButton(self.tabConfiguration)
        self.pushButtonProjectFolderLocate.setObjectName(u"pushButtonProjectFolderLocate")

        self.horizontalLayoutConfigButtonLocate.addWidget(self.pushButtonProjectFolderLocate)

        self.horizontalSpacerTabConfigLineEditProjectFolderRight = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutConfigButtonLocate.addItem(self.horizontalSpacerTabConfigLineEditProjectFolderRight)


        self.verticalLayout_4.addLayout(self.horizontalLayoutConfigButtonLocate)


        self.gridLayout.addLayout(self.verticalLayout_4, 5, 0, 1, 1)

        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(4, 98)
        self.gridLayout.setRowStretch(5, 1)
        self.tabWidget.addTab(self.tabConfiguration, "")
        self.tabAction = QWidget()
        self.tabAction.setObjectName(u"tabAction")
        self.tabWidget.addTab(self.tabAction, "")

        self.verticalLayoutMain.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayoutMain)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 620, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTheme = QMenu(self.menuFile)
        self.menuTheme.setObjectName(u"menuTheme")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMinimumSize(QSize(0, 0))
        self.toolBar.setBaseSize(QSize(0, 48))
        self.toolBar.setIconSize(QSize(48, 48))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.menuTheme.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTheme.addAction(self.actionLight)
        self.menuTheme.addAction(self.actionDark)
        self.menuTheme.addAction(self.actionAuto)
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addAction(self.actionTheme)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Projectionist", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
#if QT_CONFIG(tooltip)
        self.actionExit.setToolTip(QCoreApplication.translate("MainWindow", u"Exit Projectionist", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionExit.setStatusTip(QCoreApplication.translate("MainWindow", u"Exit Projectionist", None))
#endif // QT_CONFIG(statustip)
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(statustip)
        self.actionSettings.setStatusTip(QCoreApplication.translate("MainWindow", u"Configure Projectionist", None))
#endif // QT_CONFIG(statustip)
        self.actionLight.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.actionAuto.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.actionTheme.setText(QCoreApplication.translate("MainWindow", u"&Theme", None))
#if QT_CONFIG(tooltip)
        self.actionTheme.setToolTip(QCoreApplication.translate("MainWindow", u"Change Theme", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionTheme.setStatusTip(QCoreApplication.translate("MainWindow", u"Change Application Theme", None))
#endif // QT_CONFIG(statustip)
        self.labelInfoTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Projectionist</span></h1></body></html>", None))
        self.labelInfoDetails.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Welcome to Projectionist.</span></h3><h4>In order to make use of this excellent application it is first necessary to configure it.</h4><h4>It may also be necessary to add applications to the OS $PATH Variable to ensure that they can be found and utilised correctly. This should be fairly easy to do.</h4><h4>Once you are ready to commence the configuration, please click on the Configuration Tab and follow the instructions.</h4><h4>This application has been set to operate in a minimum size of 640 x 520, but can operate just as well or better in large sizes, imcluding full screen.</h4><h5 align=\"center\">Copyright J2Casa 2023. All Rights Reserved</h5><p><br/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInfo), QCoreApplication.translate("MainWindow", u"Information", None))
        self.labelConfigProjectFolder.setText(QCoreApplication.translate("MainWindow", u"Project Folder:", None))
        self.lineEditConfigProjectFolder.setText(QCoreApplication.translate("MainWindow", u"          Please Enter Project Main Folder", None))
        self.labelConfigTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Configuration</span></h1></body></html>", None))
        self.pushButtonProjectFolderLocate.setText(QCoreApplication.translate("MainWindow", u"Locate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfiguration), QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAction), QCoreApplication.translate("MainWindow", u"Action", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

