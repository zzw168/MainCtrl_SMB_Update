# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SMB_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 450)
        MainWindow.setMinimumSize(QSize(300, 450))
        MainWindow.setMaximumSize(QSize(300, 450))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(680, 16777215))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setMaximumSize(QSize(280, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(278, 435))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.textBrowser = QTextBrowser(self.frame_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setReadOnly(False)

        self.gridLayout_4.addWidget(self.textBrowser, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 260))
        self.groupBox.setMaximumSize(QSize(16777215, 260))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(10)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_share_name = QLineEdit(self.groupBox)
        self.lineEdit_share_name.setObjectName(u"lineEdit_share_name")

        self.gridLayout_3.addWidget(self.lineEdit_share_name, 1, 1, 1, 1)

        self.lineEdit_remote_path = QLineEdit(self.groupBox)
        self.lineEdit_remote_path.setObjectName(u"lineEdit_remote_path")

        self.gridLayout_3.addWidget(self.lineEdit_remote_path, 4, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_password = QLineEdit(self.groupBox)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.gridLayout_3.addWidget(self.lineEdit_password, 3, 1, 1, 1)

        self.lineEdit_username = QLineEdit(self.groupBox)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.gridLayout_3.addWidget(self.lineEdit_username, 2, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.lineEdit_remote_host = QLineEdit(self.groupBox)
        self.lineEdit_remote_host.setObjectName(u"lineEdit_remote_host")

        self.gridLayout_3.addWidget(self.lineEdit_remote_host, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)

        self.lineEdit_local_path = QLineEdit(self.groupBox)
        self.lineEdit_local_path.setObjectName(u"lineEdit_local_path")

        self.gridLayout_3.addWidget(self.lineEdit_local_path, 5, 1, 1, 1)

        self.pushButton_update = QPushButton(self.groupBox)
        self.pushButton_update.setObjectName(u"pushButton_update")

        self.gridLayout_3.addWidget(self.pushButton_update, 7, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e2d\u63a7\u5347\u7ea7\u5668", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5347\u7ea7\u8bbe\u7f6e", None))
        self.lineEdit_share_name.setText("")
        self.lineEdit_remote_path.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5171\u4eab\u76ee\u5f55\u540d\u79f0\uff1a", None))
        self.lineEdit_username.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939\u8def\u5f84\uff1a", None))
        self.lineEdit_remote_host.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8fdc\u7a0b\u4e3b\u673a\u5730\u5740\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.lineEdit_local_path.setText("")
        self.pushButton_update.setText(QCoreApplication.translate("MainWindow", u"\u5347\u7ea7\u5e76\u542f\u52a8", None))
    # retranslateUi

