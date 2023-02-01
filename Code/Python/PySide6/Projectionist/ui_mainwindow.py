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
        icon = QIcon()
        icon.addFile(u":/images/images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(False)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon()
        icon1.addFile(u":/glass/buttons/glassButtonExit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.actionLight.setCheckable(True)
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.actionDark.setCheckable(True)
        self.actionAuto = QAction(MainWindow)
        self.actionAuto.setObjectName(u"actionAuto")
        self.actionAuto.setCheckable(True)
        self.actionTheme = QAction(MainWindow)
        self.actionTheme.setObjectName(u"actionTheme")
        icon2 = QIcon()
        icon2.addFile(u":/glass/buttons/glassButtonTheme.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionTheme.setIcon(icon2)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon3 = QIcon()
        icon3.addFile(u":/glass/buttons/glassButtonAbout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon3)
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        icon4 = QIcon()
        icon4.addFile(u":/glass/buttons/glassButtonQt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAboutQt.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayoutMain = QVBoxLayout()
        self.verticalLayoutMain.setObjectName(u"verticalLayoutMain")
        self.verticalLayoutMain.setContentsMargins(0, -1, -1, -1)
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
        self.verticalLayoutPFConfig = QVBoxLayout()
        self.verticalLayoutPFConfig.setObjectName(u"verticalLayoutPFConfig")
        self.horizontalLayoutPFConfig = QHBoxLayout()
        self.horizontalLayoutPFConfig.setSpacing(10)
        self.horizontalLayoutPFConfig.setObjectName(u"horizontalLayoutPFConfig")
        self.horizontalLayoutPFConfig.setContentsMargins(10, -1, 10, -1)
        self.labelPFConfig = QLabel(self.tabConfiguration)
        self.labelPFConfig.setObjectName(u"labelPFConfig")
        self.labelPFConfig.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayoutPFConfig.addWidget(self.labelPFConfig)

        self.lineEditPFConfig = QLineEdit(self.tabConfiguration)
        self.lineEditPFConfig.setObjectName(u"lineEditPFConfig")
        self.lineEditPFConfig.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayoutPFConfig.addWidget(self.lineEditPFConfig, 0, Qt.AlignTop)


        self.verticalLayoutPFConfig.addLayout(self.horizontalLayoutPFConfig)


        self.gridLayout.addLayout(self.verticalLayoutPFConfig, 4, 0, 1, 1)

        self.vertitcalLayoutgridLayoutConfigTabButtonLocate = QVBoxLayout()
        self.vertitcalLayoutgridLayoutConfigTabButtonLocate.setObjectName(u"vertitcalLayoutgridLayoutConfigTabButtonLocate")
        self.horizontalLayoutConfigButtonLocate = QHBoxLayout()
        self.horizontalLayoutConfigButtonLocate.setObjectName(u"horizontalLayoutConfigButtonLocate")
        self.horizontalSpacerTabConfigLineEditPFLeft = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutConfigButtonLocate.addItem(self.horizontalSpacerTabConfigLineEditPFLeft)

        self.pushButtonPFLocate = QPushButton(self.tabConfiguration)
        self.pushButtonPFLocate.setObjectName(u"pushButtonPFLocate")
        icon5 = QIcon()
        icon5.addFile(u":/glass/buttons/glassButtonFind.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPFLocate.setIcon(icon5)

        self.horizontalLayoutConfigButtonLocate.addWidget(self.pushButtonPFLocate)

        self.pushButtonPFSave = QPushButton(self.tabConfiguration)
        self.pushButtonPFSave.setObjectName(u"pushButtonPFSave")
        self.pushButtonPFSave.setEnabled(False)
        icon6 = QIcon()
        icon6.addFile(u":/glass/buttons/glassButtonSave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPFSave.setIcon(icon6)

        self.horizontalLayoutConfigButtonLocate.addWidget(self.pushButtonPFSave)

        self.pushButtonPFCancel = QPushButton(self.tabConfiguration)
        self.pushButtonPFCancel.setObjectName(u"pushButtonPFCancel")
        self.pushButtonPFCancel.setEnabled(False)
        icon7 = QIcon()
        icon7.addFile(u":/glass/buttons/glassButtonCancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPFCancel.setIcon(icon7)

        self.horizontalLayoutConfigButtonLocate.addWidget(self.pushButtonPFCancel)

        self.horizontalLayoutConfigButtonLocate.setStretch(0, 97)
        self.horizontalLayoutConfigButtonLocate.setStretch(1, 1)
        self.horizontalLayoutConfigButtonLocate.setStretch(2, 1)
        self.horizontalLayoutConfigButtonLocate.setStretch(3, 1)

        self.vertitcalLayoutgridLayoutConfigTabButtonLocate.addLayout(self.horizontalLayoutConfigButtonLocate)


        self.gridLayout.addLayout(self.vertitcalLayoutgridLayoutConfigTabButtonLocate, 5, 0, 1, 1)

        self.gridLayoutConfigTab = QGridLayout()
        self.gridLayoutConfigTab.setObjectName(u"gridLayoutConfigTab")
        self.labelConfigTitle = QLabel(self.tabConfiguration)
        self.labelConfigTitle.setObjectName(u"labelConfigTitle")
        self.labelConfigTitle.setAlignment(Qt.AlignCenter)

        self.gridLayoutConfigTab.addWidget(self.labelConfigTitle, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayoutConfigTab, 0, 0, 1, 1)

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
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMinimumSize(QSize(0, 0))
        self.toolBar.setBaseSize(QSize(0, 48))
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(Qt.BottomToolBarArea|Qt.TopToolBarArea)
        self.toolBar.setIconSize(QSize(48, 48))
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
#if QT_CONFIG(shortcut)
        self.labelPFConfig.setBuddy(self.lineEditPFConfig)
#endif // QT_CONFIG(shortcut)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuTheme.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTheme.addAction(self.actionLight)
        self.menuTheme.addAction(self.actionDark)
        self.menuTheme.addAction(self.actionAuto)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.toolBar.addAction(self.actionExit)
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
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"Abot Qt", None))
        self.labelInfoTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Projectionist</span></h1></body></html>", None))
        self.labelInfoDetails.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Welcome to Projectionist.</span></h3><h4>In order to make use of this excellent application it is first necessary to configure it.</h4><h4>It may also be necessary to add applications to the OS $PATH Variable to ensure that they can be found and utilised correctly. This should be fairly easy to do.</h4><h4>Once you are ready to commence the configuration, please click on the Configuration Tab and follow the instructions.</h4><h4>This application has been set to operate in a minimum size of 640 x 520, but can operate just as well or better in large sizes, imcluding full screen.</h4><h5 align=\"center\">Copyright J2Casa 2023. All Rights Reserved</h5><p><br/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInfo), QCoreApplication.translate("MainWindow", u"Information", None))
        self.labelPFConfig.setText(QCoreApplication.translate("MainWindow", u"Project Folder:", None))
        self.lineEditPFConfig.setText("")
        self.lineEditPFConfig.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please Enter Project Main Folder", None))
#if QT_CONFIG(statustip)
        self.pushButtonPFLocate.setStatusTip(QCoreApplication.translate("MainWindow", u"Locate Project Folder", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonPFLocate.setText(QCoreApplication.translate("MainWindow", u"Locate", None))
#if QT_CONFIG(statustip)
        self.pushButtonPFSave.setStatusTip(QCoreApplication.translate("MainWindow", u"Save Location of Project Folder", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonPFSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(statustip)
        self.pushButtonPFCancel.setStatusTip(QCoreApplication.translate("MainWindow", u"Discard Changes", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonPFCancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.labelConfigTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Configuration</span></h1></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfiguration), QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAction), QCoreApplication.translate("MainWindow", u"Action", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

