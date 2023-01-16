# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(240, 100)
        Widget.setMinimumSize(QSize(240, 100))
        Widget.setMaximumSize(QSize(240, 100))
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonAboutDiakog = QPushButton(Widget)
        self.buttonAboutDiakog.setObjectName(u"buttonAboutDiakog")
        self.buttonAboutDiakog.setMaximumSize(QSize(240, 100))
        self.buttonAboutDiakog.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.buttonAboutDiakog)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Parent", None))
        self.buttonAboutDiakog.setText(QCoreApplication.translate("Widget", u"About Dialog", None))
    # retranslateUi

