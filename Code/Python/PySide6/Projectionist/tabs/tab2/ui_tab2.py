# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab2.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import buttons_rc

class Ui_Tab2(object):
    def setupUi(self, Tab2):
        if not Tab2.objectName():
            Tab2.setObjectName(u"Tab2")
        Tab2.resize(536, 350)
        self.gridLayout_2 = QGridLayout(Tab2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.verticalLayout1_Title = QVBoxLayout()
        self.verticalLayout1_Title.setObjectName(u"verticalLayout1_Title")
        self.labelConfigTitle = QLabel(Tab2)
        self.labelConfigTitle.setObjectName(u"labelConfigTitle")
        self.labelConfigTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout1_Title.addWidget(self.labelConfigTitle)


        self.gridLayout_2.addLayout(self.verticalLayout1_Title, 0, 0, 1, 1)

        self.verticalLayout2_PF = QVBoxLayout()
        self.verticalLayout2_PF.setObjectName(u"verticalLayout2_PF")
        self.horizontalLayoutPFConfig = QHBoxLayout()
        self.horizontalLayoutPFConfig.setSpacing(10)
        self.horizontalLayoutPFConfig.setObjectName(u"horizontalLayoutPFConfig")
        self.horizontalLayoutPFConfig.setContentsMargins(10, -1, 10, -1)
        self.labelPFConfig = QLabel(Tab2)
        self.labelPFConfig.setObjectName(u"labelPFConfig")
        self.labelPFConfig.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayoutPFConfig.addWidget(self.labelPFConfig)

        self.lineEditPFConfig = QLineEdit(Tab2)
        self.lineEditPFConfig.setObjectName(u"lineEditPFConfig")
        self.lineEditPFConfig.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayoutPFConfig.addWidget(self.lineEditPFConfig, 0, Qt.AlignTop)


        self.verticalLayout2_PF.addLayout(self.horizontalLayoutPFConfig)

        self.horizontalLayoutPFButtons = QHBoxLayout()
        self.horizontalLayoutPFButtons.setObjectName(u"horizontalLayoutPFButtons")
        self.horizontalSpacerTabConfigLineEditPFLeft = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutPFButtons.addItem(self.horizontalSpacerTabConfigLineEditPFLeft)

        self.pushButtonPFLocate = QPushButton(Tab2)
        self.pushButtonPFLocate.setObjectName(u"pushButtonPFLocate")
        icon = QIcon()
        icon.addFile(u":/glass/buttons/glassButtonFind.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPFLocate.setIcon(icon)

        self.horizontalLayoutPFButtons.addWidget(self.pushButtonPFLocate)

        self.pushButtonPFSave = QPushButton(Tab2)
        self.pushButtonPFSave.setObjectName(u"pushButtonPFSave")
        self.pushButtonPFSave.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/glass/buttons/glassButtonSave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPFSave.setIcon(icon1)

        self.horizontalLayoutPFButtons.addWidget(self.pushButtonPFSave)

        self.pushButtonPFCancel = QPushButton(Tab2)
        self.pushButtonPFCancel.setObjectName(u"pushButtonPFCancel")
        self.pushButtonPFCancel.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/glass/buttons/glassButtonCancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPFCancel.setIcon(icon2)

        self.horizontalLayoutPFButtons.addWidget(self.pushButtonPFCancel)


        self.verticalLayout2_PF.addLayout(self.horizontalLayoutPFButtons)


        self.gridLayout_2.addLayout(self.verticalLayout2_PF, 1, 0, 1, 1)

        self.verticalLayout3_Spare = QVBoxLayout()
        self.verticalLayout3_Spare.setObjectName(u"verticalLayout3_Spare")

        self.gridLayout_2.addLayout(self.verticalLayout3_Spare, 2, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.labelPFConfig.setBuddy(self.lineEditPFConfig)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Tab2)

        QMetaObject.connectSlotsByName(Tab2)
    # setupUi

    def retranslateUi(self, Tab2):
        Tab2.setWindowTitle(QCoreApplication.translate("Tab2", u"Configuration", None))
#if QT_CONFIG(tooltip)
        Tab2.setToolTip(QCoreApplication.translate("Tab2", u"Tab Tool Tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Tab2.setStatusTip(QCoreApplication.translate("Tab2", u"Tab Status Tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Tab2.setWhatsThis(QCoreApplication.translate("Tab2", u"Tab Whats This", None))
#endif // QT_CONFIG(whatsthis)
        self.labelConfigTitle.setText(QCoreApplication.translate("Tab2", u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Configuration</span></h1></body></html>", None))
        self.labelPFConfig.setText(QCoreApplication.translate("Tab2", u"Project Folder:", None))
        self.lineEditPFConfig.setText("")
        self.lineEditPFConfig.setPlaceholderText(QCoreApplication.translate("Tab2", u"Please Enter Project Main Folder", None))
#if QT_CONFIG(statustip)
        self.pushButtonPFLocate.setStatusTip(QCoreApplication.translate("Tab2", u"Locate Project Folder", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonPFLocate.setText(QCoreApplication.translate("Tab2", u"Locate", None))
#if QT_CONFIG(statustip)
        self.pushButtonPFSave.setStatusTip(QCoreApplication.translate("Tab2", u"Save Location of Project Folder", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonPFSave.setText(QCoreApplication.translate("Tab2", u"Save", None))
#if QT_CONFIG(statustip)
        self.pushButtonPFCancel.setStatusTip(QCoreApplication.translate("Tab2", u"Discard Changes", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonPFCancel.setText(QCoreApplication.translate("Tab2", u"Cancel", None))
    # retranslateUi

