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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Tab2(object):
    def setupUi(self, Tab2):
        if not Tab2.objectName():
            Tab2.setObjectName(u"Tab2")
        Tab2.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(Tab2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelHello = QLabel(Tab2)
        self.labelHello.setObjectName(u"labelHello")

        self.verticalLayout.addWidget(self.labelHello, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Tab2)

        QMetaObject.connectSlotsByName(Tab2)
    # setupUi

    def retranslateUi(self, Tab2):
        Tab2.setWindowTitle(QCoreApplication.translate("Tab2", u"Tab", None))
#if QT_CONFIG(tooltip)
        Tab2.setToolTip(QCoreApplication.translate("Tab2", u"Tab Tool Tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Tab2.setStatusTip(QCoreApplication.translate("Tab2", u"Tab Status Tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Tab2.setWhatsThis(QCoreApplication.translate("Tab2", u"Tab Whats This", None))
#endif // QT_CONFIG(whatsthis)
        self.labelHello.setText(QCoreApplication.translate("Tab2", u"HELLO AGAIN", None))
    # retranslateUi

