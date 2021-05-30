# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(549, 438)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 50, 481, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(30, 110, 291, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.start_date = QDateEdit(self.horizontalLayoutWidget_2)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setDateTime(QDateTime(QDate(2021, 5, 1), QTime(0, 0, 0)))

        self.horizontalLayout_2.addWidget(self.start_date)

        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.end_date = QDateEdit(self.horizontalLayoutWidget_2)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setDateTime(QDateTime(QDate(2021, 5, 2), QTime(0, 0, 0)))

        self.horizontalLayout_2.addWidget(self.end_date)

        self.label_info = QLabel(self.centralwidget)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(30, 370, 481, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_info.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 190, 111, 16))
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(230, 230, 111, 99))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_olympics_world = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_olympics_world.setObjectName(u"checkBox_olympics_world")

        self.verticalLayout_2.addWidget(self.checkBox_olympics_world)

        self.checkBox_olympics_tokyo = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_olympics_tokyo.setObjectName(u"checkBox_olympics_tokyo")

        self.verticalLayout_2.addWidget(self.checkBox_olympics_tokyo)

        self.checkBox_thehill = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_thehill.setObjectName(u"checkBox_thehill")

        self.verticalLayout_2.addWidget(self.checkBox_thehill)

        self.checkBox_politico = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_politico.setObjectName(u"checkBox_politico")

        self.verticalLayout_2.addWidget(self.checkBox_politico)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 230, 111, 99))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_bbc = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_bbc.setObjectName(u"checkBox_bbc")

        self.verticalLayout.addWidget(self.checkBox_bbc)

        self.checkBox_cnn = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_cnn.setObjectName(u"checkBox_cnn")

        self.verticalLayout.addWidget(self.checkBox_cnn)

        self.checkBox_wsj = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_wsj.setObjectName(u"checkBox_wsj")

        self.verticalLayout.addWidget(self.checkBox_wsj)

        self.checkBox_foxnews = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_foxnews.setObjectName(u"checkBox_foxnews")

        self.verticalLayout.addWidget(self.checkBox_foxnews)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 549, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u65b0\u95fb\u901f\u9012", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"KeyWords", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u51fa\u5173\u952e\u8bcd\uff0c\u5e76\u4ee5\u7a7a\u683c\u5206\u9694", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.start_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.end_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.label_info.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Target Sites:", None))
        self.checkBox_olympics_world.setText(QCoreApplication.translate("MainWindow", u"\u4e16\u5965", None))
        self.checkBox_olympics_tokyo.setText(QCoreApplication.translate("MainWindow", u"\u4e1c\u5965", None))
        self.checkBox_thehill.setText(QCoreApplication.translate("MainWindow", u"\u56fd\u4f1a\u5c71\u62a5", None))
        self.checkBox_politico.setText(QCoreApplication.translate("MainWindow", u"Politico", None))
        self.checkBox_bbc.setText(QCoreApplication.translate("MainWindow", u"BBC", None))
        self.checkBox_cnn.setText(QCoreApplication.translate("MainWindow", u"CNN", None))
        self.checkBox_wsj.setText(QCoreApplication.translate("MainWindow", u"WSJ", None))
        self.checkBox_foxnews.setText(QCoreApplication.translate("MainWindow", u"Foxnews", None))
    # retranslateUi

