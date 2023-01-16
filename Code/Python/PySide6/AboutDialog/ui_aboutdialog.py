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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import aboutdialog_rc

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(642, 400)
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelPicture = QLabel(AboutDialog)
        self.labelPicture.setObjectName(u"labelPicture")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(96)
        sizePolicy.setVerticalStretch(96)
        sizePolicy.setHeightForWidth(self.labelPicture.sizePolicy().hasHeightForWidth())
        self.labelPicture.setSizePolicy(sizePolicy)
        self.labelPicture.setMaximumSize(QSize(96, 96))
        self.labelPicture.setPixmap(QPixmap(u":/images/images/ProjectCreator.png"))
        self.labelPicture.setScaledContents(True)

        self.gridLayout.addWidget(self.labelPicture, 0, 0, 1, 1)

        self.labelPythonVersionBlurb = QLabel(AboutDialog)
        self.labelPythonVersionBlurb.setObjectName(u"labelPythonVersionBlurb")

        self.gridLayout.addWidget(self.labelPythonVersionBlurb, 1, 0, 1, 1)

        self.labelQtVersionBlurb = QLabel(AboutDialog)
        self.labelQtVersionBlurb.setObjectName(u"labelQtVersionBlurb")

        self.gridLayout.addWidget(self.labelQtVersionBlurb, 2, 0, 1, 1)

        self.labelAuthor = QLabel(AboutDialog)
        self.labelAuthor.setObjectName(u"labelAuthor")

        self.gridLayout.addWidget(self.labelAuthor, 3, 0, 1, 1)

        self.labelCopyright = QLabel(AboutDialog)
        self.labelCopyright.setObjectName(u"labelCopyright")

        self.gridLayout.addWidget(self.labelCopyright, 4, 0, 1, 1)

        self.labelQtVersion = QLabel(AboutDialog)
        self.labelQtVersion.setObjectName(u"labelQtVersion")

        self.gridLayout.addWidget(self.labelQtVersion, 2, 1, 1, 1)

        self.labelPythonVersion = QLabel(AboutDialog)
        self.labelPythonVersion.setObjectName(u"labelPythonVersion")

        self.gridLayout.addWidget(self.labelPythonVersion, 1, 1, 1, 1)

        self.labelTitle = QLabel(AboutDialog)
        self.labelTitle.setObjectName(u"labelTitle")

        self.gridLayout.addWidget(self.labelTitle, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayoutButtonClose = QHBoxLayout()
        self.horizontalLayoutButtonClose.setObjectName(u"horizontalLayoutButtonClose")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutButtonClose.addItem(self.horizontalSpacer)

        self.buttonClose = QPushButton(AboutDialog)
        self.buttonClose.setObjectName(u"buttonClose")
        icon = QIcon()
        icon.addFile(u":/buttons/Buttons/glassButtonClose.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonClose.setIcon(icon)

        self.horizontalLayoutButtonClose.addWidget(self.buttonClose)


        self.verticalLayout.addLayout(self.horizontalLayoutButtonClose)


        self.retranslateUi(AboutDialog)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"Dialog", None))
        self.labelPicture.setText("")
        self.labelPythonVersionBlurb.setText(QCoreApplication.translate("AboutDialog", u"This Appliation is written in Python Version: ", None))
        self.labelQtVersionBlurb.setText(QCoreApplication.translate("AboutDialog", u"This Application uses Pyside6 Version:", None))
        self.labelAuthor.setText(QCoreApplication.translate("AboutDialog", u"This Application was written by Julian Bourne.", None))
        self.labelCopyright.setText(QCoreApplication.translate("AboutDialog", u"Copyright \u00a9 Julian Bourne 2023 All Rights Reserved", None))
        self.labelQtVersion.setText(QCoreApplication.translate("AboutDialog", u"6.4.1", None))
        self.labelPythonVersion.setText(QCoreApplication.translate("AboutDialog", u"1.1.1.1", None))
        self.labelTitle.setText(QCoreApplication.translate("AboutDialog", u"<html><head/><body><p\n"
"                                    align=\"center\"><span style=\"\n"
"                                    font-size:20pt; font-weight:700;\">About\n"
"                                    Application</span></p></body></html>", None))
        self.buttonClose.setText(QCoreApplication.translate("AboutDialog", u"Close", None))
    # retranslateUi

