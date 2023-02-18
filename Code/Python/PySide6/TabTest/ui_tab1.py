# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab1.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Tab1(object):
    def setupUi(self, Tab1):
        if not Tab1.objectName():
            Tab1.setObjectName(u"Tab1")
        Tab1.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(Tab1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelHello = QLabel(Tab1)
        self.labelHello.setObjectName(u"labelHello")

        self.verticalLayout.addWidget(self.labelHello, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Tab1)

        QMetaObject.connectSlotsByName(Tab1)
    # setupUi

    def retranslateUi(self, Tab1):
        Tab1.setWindowTitle(QCoreApplication.translate("Tab1", u"Tab", None))
#if QT_CONFIG(tooltip)
        Tab1.setToolTip(QCoreApplication.translate("Tab1", u"Tab Tool Tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Tab1.setStatusTip(QCoreApplication.translate("Tab1", u"Tab Status Tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Tab1.setWhatsThis(QCoreApplication.translate("Tab1", u"Tab Whats This", None))
#endif // QT_CONFIG(whatsthis)
        self.labelHello.setText(QCoreApplication.translate("Tab1", u"HELLO", None))
    # retranslateUi

