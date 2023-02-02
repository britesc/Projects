# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutdialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import splash_rc
import buttons_rc

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        if not aboutDialog.objectName():
            aboutDialog.setObjectName(u"aboutDialog")
        aboutDialog.resize(400, 300)
        aboutDialog.setMinimumSize(QSize(400, 300))
        aboutDialog.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u":/images/images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        aboutDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(aboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelDialogTitle = QLabel(aboutDialog)
        self.labelDialogTitle.setObjectName(u"labelDialogTitle")
        self.labelDialogTitle.setMaximumSize(QSize(16777215, 48))
        self.labelDialogTitle.setLayoutDirection(Qt.LeftToRight)
        self.labelDialogTitle.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.labelDialogTitle)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.iconImage = QLabel(aboutDialog)
        self.iconImage.setObjectName(u"iconImage")
        self.iconImage.setMaximumSize(QSize(96, 96))
        self.iconImage.setPixmap(QPixmap(u":/images/images/icon.png"))
        self.iconImage.setScaledContents(True)
        self.iconImage.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.iconImage)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelVersion = QLabel(aboutDialog)
        self.labelVersion.setObjectName(u"labelVersion")
        self.labelVersion.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelVersion)

        self.labelCreated = QLabel(aboutDialog)
        self.labelCreated.setObjectName(u"labelCreated")
        self.labelCreated.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelCreated)

        self.label = QLabel(aboutDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_4 = QLabel(aboutDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButtonClose = QPushButton(aboutDialog)
        self.pushButtonClose.setObjectName(u"pushButtonClose")
        icon1 = QIcon()
        icon1.addFile(u":/glass/buttons/glassButtonClose.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonClose.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.pushButtonClose)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(aboutDialog)

        QMetaObject.connectSlotsByName(aboutDialog)
    # setupUi

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(QCoreApplication.translate("aboutDialog", u"About...", None))
        self.labelDialogTitle.setText(QCoreApplication.translate("aboutDialog", u"<html><head/><body><h2 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700;\">About Projectionist</span></h2></body></html>", None))
        self.iconImage.setText("")
        self.labelVersion.setText(QCoreApplication.translate("aboutDialog", u"Version:", None))
        self.labelCreated.setText(QCoreApplication.translate("aboutDialog", u"Created: 02 February 2023 11:30:00", None))
        self.label.setText(QCoreApplication.translate("aboutDialog", u"<html><head/><body><h6 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:360;\">Copyright JTB 2023 All Rights Reserved</span></h6></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("aboutDialog", u"Prohectionist is a tool to assist in the Creation and Setup of various computer language projects.\n"
"Including:\n"
"Python, C, C++, Kotlin and Php amongst others.\n"
"\n"
"It was created by Julian Bourne for Personal Use.", None))
        self.pushButtonClose.setText(QCoreApplication.translate("aboutDialog", u"&Close", None))
    # retranslateUi

