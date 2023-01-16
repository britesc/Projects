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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(462, 293)
        self.horizontalLayout = QHBoxLayout(AboutDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayoutOKButton = QHBoxLayout()
        self.horizontalLayoutOKButton.setObjectName(u"horizontalLayoutOKButton")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutOKButton.addItem(self.horizontalSpacer)

        self.buttonDialogOK = QPushButton(AboutDialog)
        self.buttonDialogOK.setObjectName(u"buttonDialogOK")

        self.horizontalLayoutOKButton.addWidget(self.buttonDialogOK)


        self.horizontalLayout.addLayout(self.horizontalLayoutOKButton)


        self.retranslateUi(AboutDialog)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"Dialog", None))
        self.buttonDialogOK.setText(QCoreApplication.translate("AboutDialog", u"Ok", None))
    # retranslateUi

