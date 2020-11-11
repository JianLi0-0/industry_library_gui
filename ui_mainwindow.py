# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_Chinese.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
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
        MainWindow.resize(1030, 692)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_10 = QGridLayout(self.tab_1)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBox_12 = QGroupBox(self.tab_1)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.video_label = QLabel(self.groupBox_12)
        self.video_label.setObjectName(u"video_label")
        self.video_label.setMinimumSize(QSize(700, 400))
        self.video_label.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.video_label)

        self.connect_camera_button = QPushButton(self.groupBox_12)
        self.connect_camera_button.setObjectName(u"connect_camera_button")

        self.verticalLayout_5.addWidget(self.connect_camera_button)


        self.gridLayout_10.addWidget(self.groupBox_12, 0, 0, 3, 1)

        self.groupBox_11 = QGroupBox(self.tab_1)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(260, 80))
        self.groupBox_11.setMaximumSize(QSize(260, 70))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.plainTextEdit_6 = QPlainTextEdit(self.groupBox_11)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setMinimumSize(QSize(0, 28))
        self.plainTextEdit_6.setMaximumSize(QSize(16777215, 28))

        self.horizontalLayout_3.addWidget(self.plainTextEdit_6)

        self.pushButton_13 = QPushButton(self.groupBox_11)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_3.addWidget(self.pushButton_13)


        self.gridLayout_10.addWidget(self.groupBox_11, 1, 1, 1, 1)

        self.splitter_3 = QSplitter(self.tab_1)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.groupBox_9 = QGroupBox(self.splitter_3)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMaximumSize(QSize(16777215, 220))
        self.gridLayout_8 = QGridLayout(self.groupBox_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.object_info_TextEdit = QPlainTextEdit(self.groupBox_9)
        self.object_info_TextEdit.setObjectName(u"object_info_TextEdit")
        self.object_info_TextEdit.setMinimumSize(QSize(0, 100))
        self.object_info_TextEdit.setMaximumSize(QSize(16777215, 120))

        self.gridLayout_8.addWidget(self.object_info_TextEdit, 1, 0, 1, 2)

        self.object_comboBox = QComboBox(self.groupBox_9)
        self.object_comboBox.addItem("")
        self.object_comboBox.addItem("")
        self.object_comboBox.setObjectName(u"object_comboBox")

        self.gridLayout_8.addWidget(self.object_comboBox, 2, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 2)

        self.label_8 = QLabel(self.groupBox_9)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_8.addWidget(self.label_8, 2, 0, 1, 1)

        self.splitter_3.addWidget(self.groupBox_9)
        self.groupBox_10 = QGroupBox(self.splitter_3)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_9 = QGridLayout(self.groupBox_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.grasp_button = QPushButton(self.groupBox_10)
        self.grasp_button.setObjectName(u"grasp_button")

        self.gridLayout_9.addWidget(self.grasp_button, 6, 0, 1, 2)

        self.move2home_button = QPushButton(self.groupBox_10)
        self.move2home_button.setObjectName(u"move2home_button")

        self.gridLayout_9.addWidget(self.move2home_button, 4, 0, 1, 2)

        self.place_button = QPushButton(self.groupBox_10)
        self.place_button.setObjectName(u"place_button")

        self.gridLayout_9.addWidget(self.place_button, 7, 0, 1, 2)

        self.label_9 = QLabel(self.groupBox_10)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)

        self.place_pt_comboBox = QComboBox(self.groupBox_10)
        self.place_pt_comboBox.addItem("")
        self.place_pt_comboBox.addItem("")
        self.place_pt_comboBox.addItem("")
        self.place_pt_comboBox.setObjectName(u"place_pt_comboBox")

        self.gridLayout_9.addWidget(self.place_pt_comboBox, 0, 1, 1, 1)

        self.splitter_3.addWidget(self.groupBox_10)
        self.emergency_stop_button = QPushButton(self.splitter_3)
        self.emergency_stop_button.setObjectName(u"emergency_stop_button")
        self.emergency_stop_button.setMinimumSize(QSize(0, 60))
        self.splitter_3.addWidget(self.emergency_stop_button)

        self.gridLayout_10.addWidget(self.splitter_3, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_7 = QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_8 = QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.video_label_2 = QLabel(self.groupBox_8)
        self.video_label_2.setObjectName(u"video_label_2")
        self.video_label_2.setMinimumSize(QSize(700, 400))
        self.video_label_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.video_label_2)

        self.connect_camera_button_2 = QPushButton(self.groupBox_8)
        self.connect_camera_button_2.setObjectName(u"connect_camera_button_2")

        self.verticalLayout_2.addWidget(self.connect_camera_button_2)


        self.gridLayout_7.addWidget(self.groupBox_8, 0, 0, 3, 1)

        self.groupBox_7 = QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(260, 80))
        self.groupBox_7.setMaximumSize(QSize(260, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.plainTextEdit_4 = QPlainTextEdit(self.groupBox_7)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setMinimumSize(QSize(0, 28))
        self.plainTextEdit_4.setMaximumSize(QSize(16777215, 28))

        self.horizontalLayout_2.addWidget(self.plainTextEdit_4)

        self.pushButton_9 = QPushButton(self.groupBox_7)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_2.addWidget(self.pushButton_9)


        self.gridLayout_7.addWidget(self.groupBox_7, 1, 1, 1, 1)

        self.splitter_2 = QSplitter(self.tab_2)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.groupBox_5 = QGroupBox(self.splitter_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(16777215, 220))
        self.formLayout = QFormLayout(self.groupBox_5)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.plainTextEdit_3 = QPlainTextEdit(self.groupBox_5)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.plainTextEdit_3)

        self.select_place_pt_Button_2 = QPushButton(self.groupBox_5)
        self.select_place_pt_Button_2.setObjectName(u"select_place_pt_Button_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.select_place_pt_Button_2)

        self.select_object_Button_2 = QPushButton(self.groupBox_5)
        self.select_object_Button_2.setObjectName(u"select_object_Button_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.select_object_Button_2)

        self.pushButton_10 = QPushButton(self.groupBox_5)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.pushButton_10)

        self.splitter_2.addWidget(self.groupBox_5)
        self.groupBox_6 = QGroupBox(self.splitter_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.formLayout_2 = QFormLayout(self.groupBox_6)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 0))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.plainTextEdit_7 = QPlainTextEdit(self.groupBox_6)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setMaximumSize(QSize(16777215, 28))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.plainTextEdit_7)

        self.label_3 = QLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.plainTextEdit_5 = QPlainTextEdit(self.groupBox_6)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setMaximumSize(QSize(16777215, 25))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.plainTextEdit_5)

        self.label_6 = QLabel(self.groupBox_6)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.plainTextEdit_9 = QPlainTextEdit(self.groupBox_6)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")
        self.plainTextEdit_9.setMaximumSize(QSize(16777215, 25))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.plainTextEdit_9)

        self.label_5 = QLabel(self.groupBox_6)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.plainTextEdit_8 = QPlainTextEdit(self.groupBox_6)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setMaximumSize(QSize(16777215, 25))

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.plainTextEdit_8)

        self.confirm_button = QPushButton(self.groupBox_6)
        self.confirm_button.setObjectName(u"confirm_button")

        self.formLayout_2.setWidget(4, QFormLayout.SpanningRole, self.confirm_button)

        self.splitter_2.addWidget(self.groupBox_6)
        self.emergency_stop_button_2 = QPushButton(self.splitter_2)
        self.emergency_stop_button_2.setObjectName(u"emergency_stop_button_2")
        self.emergency_stop_button_2.setMinimumSize(QSize(0, 60))
        self.splitter_2.addWidget(self.emergency_stop_button_2)

        self.gridLayout_7.addWidget(self.splitter_2, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1030, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u9891", None))
        self.video_label.setText("")
        self.connect_camera_button.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u6444\u50cf\u5934", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u6807\u5b9a\u6587\u4ef6\u8def\u5f84", None))
        self.plainTextEdit_6.setPlainText(QCoreApplication.translate("MainWindow", u"./desktop/calib.txt", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u6837\u54c1\u68c0\u6d4b\u53ca\u5339\u914d", None))
        self.object_info_TextEdit.setPlainText("")
        self.object_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6837\u54c11", None))
        self.object_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6837\u54c12", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6837\u54c1\u4fe1\u606f", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6837\u54c1", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u63a7\u5236", None))
        self.grasp_button.setText(QCoreApplication.translate("MainWindow", u"\u6293\u53d6\u6837\u54c1", None))
        self.move2home_button.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u52a8\u81f3home\u4f4d\u7f6e", None))
        self.place_button.setText(QCoreApplication.translate("MainWindow", u"\u653e\u7f6e\u6837\u54c1", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u653e\u7f6e\u70b9", None))
        self.place_pt_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u653e\u7f6e\u70b91", None))
        self.place_pt_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u653e\u7f6e\u70b92", None))
        self.place_pt_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u653e\u7f6e\u70b93", None))

        self.emergency_stop_button.setText(QCoreApplication.translate("MainWindow", u"\u7d27\u6025\u505c\u6b62", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u5206\u62e3", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u9891", None))
        self.video_label_2.setText("")
        self.connect_camera_button_2.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u6444\u50cf\u5934", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u6807\u5b9a\u6587\u4ef6\u8def\u5f84", None))
        self.plainTextEdit_4.setPlainText(QCoreApplication.translate("MainWindow", u"./desktop/calib.txt", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u4ea4\u4e92\u751f\u6210\u6253\u78e8\u8def\u5f84", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u4fe1\u606f", None))
        self.select_place_pt_Button_2.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u8def\u5f84", None))
        self.select_object_Button_2.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u8def\u5f84", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u9884\u89c8", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u63a7\u5236", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u60ef\u6027", None))
        self.plainTextEdit_7.setPlainText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u963b\u5c3c", None))
        self.plainTextEdit_5.setPlainText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u538b\u529b", None))
        self.plainTextEdit_9.setPlainText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6", None))
        self.plainTextEdit_8.setPlainText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.confirm_button.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c\u8def\u5f84", None))
        self.emergency_stop_button_2.setText(QCoreApplication.translate("MainWindow", u"\u7d27\u6025\u505c\u6b62", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6253\u78e8", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u6807\u5b9a", None))
    # retranslateUi

