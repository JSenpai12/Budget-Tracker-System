# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BudgetDesign.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(711, 513)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 711, 521))
        self.frame.setStyleSheet(u"background-color: #c0e7fb;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 551, 41))
        self.label.setStyleSheet(u"color: medium-gray;\n"
"font-size: 30px;\n"
"font-weight: bold;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 80, 641, 411))
        self.frame_2.setStyleSheet(u"background-color: #e5f5fd;\n"
"border-radius: 15px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.history_frame = QFrame(self.frame_2)
        self.history_frame.setObjectName(u"history_frame")
        self.history_frame.setGeometry(QRect(260, 20, 351, 371))
        self.history_frame.setStyleSheet(u"#history_frame {\n"
"    background-color: white;\n"
"    border: 1px solid #ccc;\n"
"    border-bottom: 2px solid #cfdde5; /* darker bottom edge to fake depth */\n"
"    border-right: 2px solid #cfdde5;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.history_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.history_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_8 = QLabel(self.history_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(120, 20, 111, 41))
        self.label_8.setStyleSheet(u"background-color: #cce5ff;\n"
"color: #226cbd;\n"
"border-radius: 4px;\n"
"font-weight: bold;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.history_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(250, 20, 91, 41))
        self.label_9.setStyleSheet(u"background-color: #cce5ff;\n"
"color: #226cbd;\n"
"border-radius: 4px;\n"
"font-weight: bold;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line = QFrame(self.history_frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 80, 348, 1))
        self.line.setStyleSheet(u"background-color: #ccc;")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.history_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 110, 348, 1))
        self.line_2.setStyleSheet(u"background-color: #ccc;")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_10 = QLabel(self.history_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 80, 141, 31))
        self.label_10.setStyleSheet(u"color: black;\n"
"font-weight: medium;\n"
"font-size: 15px;\n"
"background: transparent;\n"
"")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7 = QLabel(self.history_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 21, 91, 41))
        self.label_7.setStyleSheet(u"background-color: #cce5ff;\n"
"color: #226cbd;\n"
"border-radius: 4px;\n"
"font-weight: bold;")
        self.label_7.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setMargin(0)
        self.tableView = QTableView(self.history_frame)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(15, 121, 321, 231))
        self.tableView.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.add_budgetFrame = QFrame(self.frame_2)
        self.add_budgetFrame.setObjectName(u"add_budgetFrame")
        self.add_budgetFrame.setGeometry(QRect(20, 30, 221, 131))
        self.add_budgetFrame.setStyleSheet(u"#add_budgetFrame {\n"
"    background-color: white;\n"
"    border: 1px solid #ccc;\n"
"    border-bottom: 2px solid #cfdde5; /* darker bottom edge to fake depth */\n"
"    border-right: 2px solid #cfdde5;\n"
"    border-radius: 4px;\n"
"\n"
"}")
        self.add_budgetFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.add_budgetFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.add_budgetFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 95, 24))
        self.label_2.setStyleSheet(u"color: black;\n"
"font-weight: medium;\n"
"font-size: 18px;\n"
"background: transparent;\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit = QLineEdit(self.add_budgetFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 60, 161, 21))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 0.5px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"	background-color: white;\n"
"	color: black;\n"
"}\n"
"")
        self.label_3 = QLabel(self.add_budgetFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 40, 49, 16))
        self.label_3.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.pushButton = QPushButton(self.add_budgetFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 90, 161, 24))
        self.pushButton.setStyleSheet(u"background-color: #007bff;\n"
"color: white;\n"
"border-radius: 4px;\n"
"font-weight: bold;")
        self.expense_frame = QFrame(self.frame_2)
        self.expense_frame.setObjectName(u"expense_frame")
        self.expense_frame.setGeometry(QRect(20, 170, 221, 181))
        self.expense_frame.setStyleSheet(u"#expense_frame {\n"
"    background-color: white;\n"
"    border: 1px solid #ccc;\n"
"    border-bottom: 2px solid #cfdde5; /* darker bottom edge to fake depth */\n"
"    border-right: 2px solid #cfdde5;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.expense_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.expense_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.expense_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 110, 24))
        self.label_4.setStyleSheet(u"color: black;\n"
"font-weight: medium;\n"
"font-size: 18px;\n"
"background: transparent;\n"
"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.expense_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 40, 131, 16))
        self.label_5.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.lineEdit_2 = QLineEdit(self.expense_frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 60, 161, 21))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    border: 0.5px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"	background-color: white;\n"
"	color: black;\n"
"}\n"
"")
        self.label_6 = QLabel(self.expense_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 90, 131, 16))
        self.label_6.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.lineEdit_3 = QLineEdit(self.expense_frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 110, 161, 21))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    border: 0.5px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"	background-color: white;\n"
"	color: black;\n"
"}\n"
"")
        self.pushButton_2 = QPushButton(self.expense_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 140, 161, 24))
        self.pushButton_2.setStyleSheet(u"background-color: #007bff;\n"
"color: white;\n"
"border-radius: 4px;\n"
"font-weight: bold;")
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 360, 221, 24))
        self.pushButton_3.setStyleSheet(u"background-color: #d63746;\n"
"color: white;\n"
"border-radius: 4px;\n"
"font-weight: bold;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Budget Tracker System", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Total Expenses: 0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Budget Left: 0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Expense History:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Total Budet: 0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Add Budget", None))
        self.lineEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Budget:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add Budget", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Add Expense", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Expense Title:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Amount:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add Expenses", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Reset All", None))
    # retranslateUi

