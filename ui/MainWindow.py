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
        MainWindow.resize(635, 535)
        MainWindow.setMinimumSize(QSize(549, 430))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(34, 162, 111, 16))
        self.checkBox_bbc = QCheckBox(self.centralwidget)
        self.checkBox_bbc.setObjectName(u"checkBox_bbc")
        self.checkBox_bbc.setGeometry(QRect(70, 204, 109, 19))
        self.checkBox_foxnews = QCheckBox(self.centralwidget)
        self.checkBox_foxnews.setObjectName(u"checkBox_foxnews")
        self.checkBox_foxnews.setGeometry(QRect(70, 282, 109, 19))
        self.checkBox_cnn = QCheckBox(self.centralwidget)
        self.checkBox_cnn.setObjectName(u"checkBox_cnn")
        self.checkBox_cnn.setGeometry(QRect(70, 230, 109, 19))
        self.checkBox_wsj = QCheckBox(self.centralwidget)
        self.checkBox_wsj.setObjectName(u"checkBox_wsj")
        self.checkBox_wsj.setGeometry(QRect(70, 256, 109, 19))
        self.checkBox_olympics_world = QCheckBox(self.centralwidget)
        self.checkBox_olympics_world.setObjectName(u"checkBox_olympics_world")
        self.checkBox_olympics_world.setGeometry(QRect(220, 204, 109, 19))
        self.checkBox_thehill = QCheckBox(self.centralwidget)
        self.checkBox_thehill.setObjectName(u"checkBox_thehill")
        self.checkBox_thehill.setGeometry(QRect(220, 256, 109, 19))
        self.checkBox_politico = QCheckBox(self.centralwidget)
        self.checkBox_politico.setObjectName(u"checkBox_politico")
        self.checkBox_politico.setGeometry(QRect(220, 282, 109, 19))
        self.checkBox_olympics_tokyo = QCheckBox(self.centralwidget)
        self.checkBox_olympics_tokyo.setObjectName(u"checkBox_olympics_tokyo")
        self.checkBox_olympics_tokyo.setGeometry(QRect(220, 230, 109, 19))
        self.start_date = QDateEdit(self.centralwidget)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setGeometry(QRect(73, 102, 110, 24))
        self.start_date.setDateTime(QDateTime(QDate(2021, 5, 1), QTime(0, 0, 0)))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(34, 90, 32, 49))
        self.end_date = QDateEdit(self.centralwidget)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setGeometry(QRect(213, 102, 110, 24))
        self.end_date.setDateTime(QDateTime(QDate(2021, 5, 2), QTime(0, 0, 0)))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 90, 16, 49))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(34, 35, 71, 39))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(105, 42, 308, 24))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(420, 40, 93, 28))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(34, 370, 571, 111))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(34, 330, 111, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 635, 26))
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
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Target Sites:", None))
        self.checkBox_bbc.setText(QCoreApplication.translate("MainWindow", u"BBC", None))
        self.checkBox_foxnews.setText(QCoreApplication.translate("MainWindow", u"FoxNews", None))
        self.checkBox_cnn.setText(QCoreApplication.translate("MainWindow", u"CNN", None))
        self.checkBox_wsj.setText(QCoreApplication.translate("MainWindow", u"WSJ", None))
        self.checkBox_olympics_world.setText(QCoreApplication.translate("MainWindow", u"\u4e16\u5965", None))
        self.checkBox_thehill.setText(QCoreApplication.translate("MainWindow", u"\u56fd\u4f1a\u5c71\u62a5", None))
        self.checkBox_politico.setText(QCoreApplication.translate("MainWindow", u"Politico", None))
        self.checkBox_olympics_tokyo.setText(QCoreApplication.translate("MainWindow", u"\u4e1c\u5965", None))
        self.start_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.end_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"KeyWords", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u51fa\u5173\u952e\u8bcd\uff0c\u5e76\u4ee5\u7a7a\u683c\u5206\u9694", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Display Info:", None))
    # retranslateUi

