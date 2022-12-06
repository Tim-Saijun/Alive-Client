# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
        MainWindow.resize(1450, 874)
        MainWindow.setMinimumSize(QSize(1000, 700))
        icon = QIcon()
        icon.addFile(u":/png/\u533b\u7597\u670d\u52a1.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toodle = QFrame(self.frame_top)
        self.frame_toodle.setObjectName(u"frame_toodle")
        self.frame_toodle.setMinimumSize(QSize(80, 55))
        self.frame_toodle.setMaximumSize(QSize(80, 55))
        self.frame_toodle.setStyleSheet(u"background:rgb(0,143,150);")
        self.frame_toodle.setFrameShape(QFrame.NoFrame)
        self.frame_toodle.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toodle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toodle = QPushButton(self.frame_toodle)
        self.toodle.setObjectName(u"toodle")
        self.toodle.setMinimumSize(QSize(80, 55))
        self.toodle.setMaximumSize(QSize(80, 55))
        self.toodle.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,178,178);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/1x/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toodle.setIcon(icon1)
        self.toodle.setIconSize(QSize(22, 12))
        self.toodle.setFlat(True)

        self.horizontalLayout_3.addWidget(self.toodle)


        self.horizontalLayout.addWidget(self.frame_toodle)

        self.frame_top_east = QFrame(self.frame_top)
        self.frame_top_east.setObjectName(u"frame_top_east")
        self.frame_top_east.setMaximumSize(QSize(16777215, 55))
        self.frame_top_east.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_top_east.setFrameShape(QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_appname = QFrame(self.frame_top_east)
        self.frame_appname.setObjectName(u"frame_appname")
        self.frame_appname.setFrameShape(QFrame.NoFrame)
        self.frame_appname.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_appname)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lab_appname = QLabel(self.frame_appname)
        self.lab_appname.setObjectName(u"lab_appname")
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        font.setPointSize(24)
        self.lab_appname.setFont(font)
        self.lab_appname.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_10.addWidget(self.lab_appname)


        self.horizontalLayout_4.addWidget(self.frame_appname)

        self.frame_user = QFrame(self.frame_top_east)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lab_user = QLabel(self.frame_user)
        self.lab_user.setObjectName(u"lab_user")
        self.lab_user.setFont(font)
        self.lab_user.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_user.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lab_user)


        self.horizontalLayout_4.addWidget(self.frame_user)

        self.frame_person = QFrame(self.frame_top_east)
        self.frame_person.setObjectName(u"frame_person")
        self.frame_person.setMinimumSize(QSize(55, 55))
        self.frame_person.setMaximumSize(QSize(55, 55))
        self.frame_person.setFrameShape(QFrame.NoFrame)
        self.frame_person.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_person)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lab_person = QLabel(self.frame_person)
        self.lab_person.setObjectName(u"lab_person")
        self.lab_person.setMaximumSize(QSize(55, 55))
        self.lab_person.setPixmap(QPixmap(u"icons/1x/peple.png"))
        self.lab_person.setScaledContents(False)
        self.lab_person.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lab_person)


        self.horizontalLayout_4.addWidget(self.frame_person)


        self.horizontalLayout.addWidget(self.frame_top_east)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_west = QFrame(self.frame_bottom)
        self.frame_bottom_west.setObjectName(u"frame_bottom_west")
        self.frame_bottom_west.setMinimumSize(QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QSize(80, 16777215))
        self.frame_bottom_west.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_bottom_west.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_home = QFrame(self.frame_bottom_west)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setMinimumSize(QSize(80, 55))
        self.frame_home.setMaximumSize(QSize(160, 55))
        self.frame_home.setFrameShape(QFrame.NoFrame)
        self.frame_home.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bn_home = QPushButton(self.frame_home)
        self.bn_home.setObjectName(u"bn_home")
        self.bn_home.setMinimumSize(QSize(80, 60))
        self.bn_home.setMaximumSize(QSize(160, 55))
        self.bn_home.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/png/\u533b\u7597_\u533b\u7597\u5927\u5c4f .png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_home.setIcon(icon2)
        self.bn_home.setIconSize(QSize(48, 48))
        self.bn_home.setFlat(True)

        self.horizontalLayout_15.addWidget(self.bn_home)


        self.verticalLayout_3.addWidget(self.frame_home)

        self.frame_bug = QFrame(self.frame_bottom_west)
        self.frame_bug.setObjectName(u"frame_bug")
        self.frame_bug.setMinimumSize(QSize(80, 55))
        self.frame_bug.setMaximumSize(QSize(160, 55))
        self.frame_bug.setFrameShape(QFrame.NoFrame)
        self.frame_bug.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_bug)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.bn_bug = QPushButton(self.frame_bug)
        self.bn_bug.setObjectName(u"bn_bug")
        self.bn_bug.setMinimumSize(QSize(80, 60))
        self.bn_bug.setMaximumSize(QSize(160, 55))
        self.bn_bug.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/png/\u533b\u7597_\u533b\u7597\u6587\u6863 .png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_bug.setIcon(icon3)
        self.bn_bug.setIconSize(QSize(48, 48))
        self.bn_bug.setFlat(True)

        self.horizontalLayout_16.addWidget(self.bn_bug)


        self.verticalLayout_3.addWidget(self.frame_bug)

        self.frame_8 = QFrame(self.frame_bottom_west)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.frame_bottom_west)

        self.frame_bottom_east = QFrame(self.frame_bottom)
        self.frame_bottom_east.setObjectName(u"frame_bottom_east")
        self.frame_bottom_east.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_bottom_east)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:rgb(169, 169, 169)\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(800, 16777215))
        font1 = QFont()
        font1.setPointSize(16)
        self.frame_2.setFont(font1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.image_origin = QLabel(self.frame_2)
        self.image_origin.setObjectName(u"image_origin")
        self.image_origin.setMinimumSize(QSize(0, 0))
        self.image_origin.setMaximumSize(QSize(708, 400))
        self.image_origin.setPixmap(QPixmap(u":/bmp/E:/unet-nested-multiple-classification-master/\u5355\u955c\u5934/{2E7D14DF-89B8-4DA3-84E6-B5CCD6F197FB}.bmp"))
        self.image_origin.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.image_origin)

        self.image_result = QLabel(self.frame_2)
        self.image_result.setObjectName(u"image_result")
        self.image_result.setMinimumSize(QSize(0, 0))
        self.image_result.setMaximumSize(QSize(708, 400))
        self.image_result.setPixmap(QPixmap(u":/bmp/E:/unet-nested-multiple-classification-master/\u5355\u955c\u5934/{2E7D14DF-89B8-4DA3-84E6-B5CCD6F197FB}.bmp"))
        self.image_result.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.image_result)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 1)

        self.horizontalLayout_14.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(240, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.input_cluster = QFrame(self.frame_5)
        self.input_cluster.setObjectName(u"input_cluster")
        self.input_cluster.setStyleSheet(u"background-color:rgb(169, 169, 16)\n"
"#input_cluster{border:2px solid rgb(255,255,0)}")
        self.input_cluster.setFrameShape(QFrame.Panel)
        self.input_cluster.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.input_cluster)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.input_1 = QFrame(self.input_cluster)
        self.input_1.setObjectName(u"input_1")
        self.input_1.setMaximumSize(QSize(208, 64))
        self.input_1.setFrameShape(QFrame.StyledPanel)
        self.input_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.input_1)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_9 = QLabel(self.input_1)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_22.addWidget(self.label_9)

        self.plainTextEdit_6 = QPlainTextEdit(self.input_1)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setFont(font1)
        self.plainTextEdit_6.setFrameShape(QFrame.WinPanel)

        self.horizontalLayout_22.addWidget(self.plainTextEdit_6)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 1)

        self.verticalLayout_9.addWidget(self.input_1)

        self.input_2 = QFrame(self.input_cluster)
        self.input_2.setObjectName(u"input_2")
        self.input_2.setMaximumSize(QSize(208, 64))
        self.input_2.setFrameShape(QFrame.StyledPanel)
        self.input_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.input_2)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_12 = QLabel(self.input_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_25.addWidget(self.label_12)

        self.plainTextEdit_9 = QPlainTextEdit(self.input_2)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")
        self.plainTextEdit_9.setFont(font1)
        self.plainTextEdit_9.setFrameShape(QFrame.WinPanel)

        self.horizontalLayout_25.addWidget(self.plainTextEdit_9)

        self.horizontalLayout_25.setStretch(0, 1)
        self.horizontalLayout_25.setStretch(1, 1)

        self.verticalLayout_9.addWidget(self.input_2)

        self.input_3 = QFrame(self.input_cluster)
        self.input_3.setObjectName(u"input_3")
        self.input_3.setMaximumSize(QSize(208, 64))
        self.input_3.setFrameShape(QFrame.StyledPanel)
        self.input_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.input_3)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_10 = QLabel(self.input_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_23.addWidget(self.label_10)

        self.plainTextEdit_7 = QPlainTextEdit(self.input_3)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setKerning(True)
        self.plainTextEdit_7.setFont(font2)
        self.plainTextEdit_7.setFrameShape(QFrame.WinPanel)

        self.horizontalLayout_23.addWidget(self.plainTextEdit_7)

        self.horizontalLayout_23.setStretch(0, 1)
        self.horizontalLayout_23.setStretch(1, 1)

        self.verticalLayout_9.addWidget(self.input_3)

        self.input_4 = QFrame(self.input_cluster)
        self.input_4.setObjectName(u"input_4")
        self.input_4.setMaximumSize(QSize(208, 64))
        self.input_4.setFrameShape(QFrame.StyledPanel)
        self.input_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.input_4)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_11 = QLabel(self.input_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_24.addWidget(self.label_11)

        self.plainTextEdit_8 = QPlainTextEdit(self.input_4)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setFont(font1)
        self.plainTextEdit_8.setFrameShape(QFrame.WinPanel)
        self.plainTextEdit_8.setBackgroundVisible(False)
        self.plainTextEdit_8.setCenterOnScroll(False)

        self.horizontalLayout_24.addWidget(self.plainTextEdit_8)

        self.horizontalLayout_24.setStretch(0, 1)
        self.horizontalLayout_24.setStretch(1, 1)

        self.verticalLayout_9.addWidget(self.input_4)

        self.input_5 = QFrame(self.input_cluster)
        self.input_5.setObjectName(u"input_5")
        self.input_5.setMaximumSize(QSize(208, 64))
        self.input_5.setFrameShape(QFrame.StyledPanel)
        self.input_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.input_5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_13 = QLabel(self.input_5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_26.addWidget(self.label_13)

        self.plainTextEdit_10 = QPlainTextEdit(self.input_5)
        self.plainTextEdit_10.setObjectName(u"plainTextEdit_10")
        self.plainTextEdit_10.setFont(font1)
        self.plainTextEdit_10.setFrameShape(QFrame.WinPanel)

        self.horizontalLayout_26.addWidget(self.plainTextEdit_10)

        self.horizontalLayout_26.setStretch(0, 1)
        self.horizontalLayout_26.setStretch(1, 1)

        self.verticalLayout_9.addWidget(self.input_5)


        self.verticalLayout_8.addWidget(self.input_cluster)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_25 = QFrame(self.frame_9)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(10, 0, 180, 351))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.frame_25)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(0, 50, 200, 75))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.pushButton_loadimage = QPushButton(self.frame_14)
        self.pushButton_loadimage.setObjectName(u"pushButton_loadimage")
        self.pushButton_loadimage.setGeometry(QRect(10, 20, 161, 41))
        font3 = QFont()
        font3.setFamily(u"Adobe \u9ed1\u4f53 Std R")
        font3.setPointSize(20)
        self.pushButton_loadimage.setFont(font3)
        self.pushButton_loadimage.setFlat(False)
        self.frame_7 = QFrame(self.frame_25)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(-10, 130, 220, 89))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.comboBox = QComboBox(self.frame_7)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 27, 181, 41))
        font4 = QFont()
        font4.setPointSize(18)
        self.comboBox.setFont(font4)
        self.label = QLabel(self.frame_25)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 211, 51))
        font5 = QFont()
        font5.setPointSize(14)
        self.label.setFont(font5)
        self.pushButton_loadimage_2 = QPushButton(self.frame_25)
        self.pushButton_loadimage_2.setObjectName(u"pushButton_loadimage_2")
        self.pushButton_loadimage_2.setGeometry(QRect(10, 280, 161, 41))
        self.pushButton_loadimage_2.setFont(font3)
        self.pushButton_loadimage_2.setFlat(False)
        self.pushButton_confirm = QPushButton(self.frame_25)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")
        self.pushButton_confirm.setGeometry(QRect(10, 230, 161, 41))
        self.pushButton_confirm.setFont(font3)
        self.pushButton_confirm.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_confirm.setAutoDefault(True)
        self.pushButton_confirm.setFlat(False)

        self.verticalLayout_8.addWidget(self.frame_9)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 1)

        self.horizontalLayout_14.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(240, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.result_cluster = QFrame(self.frame_4)
        self.result_cluster.setObjectName(u"result_cluster")
        self.result_cluster.setFrameShape(QFrame.Panel)
        self.result_cluster.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.result_cluster)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_6 = QFrame(self.result_cluster)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.result_8 = QFrame(self.frame_6)
        self.result_8.setObjectName(u"result_8")
        self.result_8.setMaximumSize(QSize(208, 64))
        self.result_8.setFrameShape(QFrame.StyledPanel)
        self.result_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.result_8)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_21 = QLabel(self.result_8)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_34.addWidget(self.label_21)

        self.plainTextEdit_18 = QPlainTextEdit(self.result_8)
        self.plainTextEdit_18.setObjectName(u"plainTextEdit_18")
        self.plainTextEdit_18.setFont(font1)
        self.plainTextEdit_18.setFrameShape(QFrame.WinPanel)

        self.horizontalLayout_34.addWidget(self.plainTextEdit_18)

        self.horizontalLayout_34.setStretch(0, 1)
        self.horizontalLayout_34.setStretch(1, 1)

        self.verticalLayout_6.addWidget(self.result_8)

        self.result_7 = QFrame(self.frame_6)
        self.result_7.setObjectName(u"result_7")
        self.result_7.setMaximumSize(QSize(208, 64))
        self.result_7.setFrameShape(QFrame.StyledPanel)
        self.result_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.result_7)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_20 = QLabel(self.result_7)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_33.addWidget(self.label_20)

        self.plainTextEdit_17 = QPlainTextEdit(self.result_7)
        self.plainTextEdit_17.setObjectName(u"plainTextEdit_17")
        self.plainTextEdit_17.setFont(font1)
        self.plainTextEdit_17.setFrameShape(QFrame.WinPanel)

        self.horizontalLayout_33.addWidget(self.plainTextEdit_17)

        self.horizontalLayout_33.setStretch(0, 1)
        self.horizontalLayout_33.setStretch(1, 1)

        self.verticalLayout_6.addWidget(self.result_7)

        self.result_6 = QFrame(self.frame_6)
        self.result_6.setObjectName(u"result_6")
        self.result_6.setMaximumSize(QSize(208, 64))
        self.result_6.setFrameShape(QFrame.StyledPanel)
        self.result_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.result_6)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_19 = QLabel(self.result_6)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_32.addWidget(self.label_19)

        self.plainTextEdit_16 = QPlainTextEdit(self.result_6)
        self.plainTextEdit_16.setObjectName(u"plainTextEdit_16")
        self.plainTextEdit_16.setFont(font1)
        self.plainTextEdit_16.setFrameShape(QFrame.WinPanel)

        self.horizontalLayout_32.addWidget(self.plainTextEdit_16)

        self.horizontalLayout_32.setStretch(0, 1)
        self.horizontalLayout_32.setStretch(1, 1)

        self.verticalLayout_6.addWidget(self.result_6)

        self.result_10 = QFrame(self.frame_6)
        self.result_10.setObjectName(u"result_10")
        self.result_10.setMaximumSize(QSize(208, 64))
        self.result_10.setFrameShape(QFrame.StyledPanel)
        self.result_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.result_10)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_23 = QLabel(self.result_10)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_36.addWidget(self.label_23)

        self.plainTextEdit_20 = QPlainTextEdit(self.result_10)
        self.plainTextEdit_20.setObjectName(u"plainTextEdit_20")
        self.plainTextEdit_20.setFont(font1)
        self.plainTextEdit_20.setFrameShape(QFrame.WinPanel)

        self.horizontalLayout_36.addWidget(self.plainTextEdit_20)

        self.horizontalLayout_36.setStretch(0, 1)
        self.horizontalLayout_36.setStretch(1, 1)

        self.verticalLayout_6.addWidget(self.result_10)

        self.result_9 = QFrame(self.frame_6)
        self.result_9.setObjectName(u"result_9")
        self.result_9.setMaximumSize(QSize(208, 64))
        self.result_9.setFrameShape(QFrame.StyledPanel)
        self.result_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.result_9)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_22 = QLabel(self.result_9)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_35.addWidget(self.label_22)

        self.plainTextEdit_19 = QPlainTextEdit(self.result_9)
        self.plainTextEdit_19.setObjectName(u"plainTextEdit_19")
        self.plainTextEdit_19.setFont(font1)
        self.plainTextEdit_19.setFrameShape(QFrame.WinPanel)

        self.horizontalLayout_35.addWidget(self.plainTextEdit_19)

        self.horizontalLayout_35.setStretch(0, 1)
        self.horizontalLayout_35.setStretch(1, 1)

        self.verticalLayout_6.addWidget(self.result_9)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 1)
        self.verticalLayout_6.setStretch(3, 1)
        self.verticalLayout_6.setStretch(4, 1)

        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_10 = QFrame(self.result_cluster)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textBrowser = QTextBrowser(self.frame_10)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_10.addWidget(self.textBrowser)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)

        self.verticalLayout_11.addWidget(self.result_cluster)

        self.verticalLayout_11.setStretch(0, 5)

        self.horizontalLayout_14.addWidget(self.frame_4)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(240, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_13)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")
        font6 = QFont()
        font6.setFamily(u"Adobe \u5b8b\u4f53 Std L")
        font6.setPointSize(48)
        self.label_4.setFont(font6)

        self.verticalLayout_14.addWidget(self.label_4)


        self.verticalLayout_13.addWidget(self.frame_13)

        self.frame_30 = QFrame(self.frame_12)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frame_30)

        self.verticalLayout_13.setStretch(0, 5)
        self.verticalLayout_13.setStretch(1, 2)

        self.horizontalLayout_14.addWidget(self.frame_12)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.horizontalLayout_5.setStretch(0, 2)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_low = QFrame(self.frame_bottom_east)
        self.frame_low.setObjectName(u"frame_low")
        self.frame_low.setMinimumSize(QSize(0, 20))
        self.frame_low.setMaximumSize(QSize(16777215, 20))
        self.frame_low.setStyleSheet(u"")
        self.frame_low.setFrameShape(QFrame.NoFrame)
        self.frame_low.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_tab = QFrame(self.frame_low)
        self.frame_tab.setObjectName(u"frame_tab")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        self.frame_tab.setFont(font7)
        self.frame_tab.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_tab.setFrameShape(QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lab_tab = QLabel(self.frame_tab)
        self.lab_tab.setObjectName(u"lab_tab")
        font8 = QFont()
        font8.setFamily(u"Segoe UI Light")
        font8.setPointSize(10)
        self.lab_tab.setFont(font8)
        self.lab_tab.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_12.addWidget(self.lab_tab)


        self.horizontalLayout_11.addWidget(self.frame_tab)

        self.frame_drag = QFrame(self.frame_low)
        self.frame_drag.setObjectName(u"frame_drag")
        self.frame_drag.setMinimumSize(QSize(20, 20))
        self.frame_drag.setMaximumSize(QSize(20, 20))
        self.frame_drag.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_drag.setFrameShape(QFrame.NoFrame)
        self.frame_drag.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.frame_drag)


        self.verticalLayout_2.addWidget(self.frame_low)


        self.horizontalLayout_2.addWidget(self.frame_bottom_east)


        self.verticalLayout.addWidget(self.frame_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_confirm.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toodle.setText("")
        self.lab_appname.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lab_user.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">User8455</span></p></body></html>", None))
        self.lab_person.setText("")
#if QT_CONFIG(tooltip)
        self.bn_home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.bn_home.setText("")
#if QT_CONFIG(tooltip)
        self.bn_bug.setToolTip(QCoreApplication.translate("MainWindow", u"Bug", None))
#endif // QT_CONFIG(tooltip)
        self.bn_bug.setText("")
        self.image_origin.setText("")
        self.image_result.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\u5de6\u5fc3\u5ba4</span></p></body></html>", None))
        self.plainTextEdit_6.setPlainText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\u53f3\u5fc3\u5ba4</span></p></body></html>", None))
        self.plainTextEdit_9.setPlainText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\u5de6\u5fc3\u623f</span></p></body></html>", None))
        self.plainTextEdit_7.setPlainText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\u53f3\u5fc3\u623f</span></p></body></html>", None))
        self.plainTextEdit_8.setPlainText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u964d\u4e3b\u52a8\u8109</span></p></body></html>", None))
        self.plainTextEdit_10.setPlainText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_loadimage.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u56fe\u50cf", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9009\u9879A", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u9009\u9879B", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u9009\u9879C", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u65b9\u8f93\u5165\u6d4b\u8ddd\u4fe1\u606f", None))
        self.pushButton_loadimage_2.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u5206", None))
        self.pushButton_confirm.setText(QCoreApplication.translate("MainWindow", u"AI\u6d4b\u8ddd", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\u5de6\u5fc3\u5ba4</span></p></body></html>", None))
        self.plainTextEdit_18.setPlainText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\u53f3\u5fc3\u5ba4</span></p></body></html>", None))
        self.plainTextEdit_17.setPlainText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\u5de6\u5fc3\u623f</span></p></body></html>", None))
        self.plainTextEdit_16.setPlainText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\u53f3\u5fc3\u623f</span></p></body></html>", None))
        self.plainTextEdit_20.setPlainText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u964d\u4e3b\u52a8\u8109</span></p></body></html>", None))
        self.plainTextEdit_19.setPlainText(QCoreApplication.translate("MainWindow", u"14", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">\u663e\u793a\u8bc4\u5206\u7ed3\u679c</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u9884\u7559", None))
        self.lab_tab.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.frame_drag.setToolTip(QCoreApplication.translate("MainWindow", u"Drag", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

