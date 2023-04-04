# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)
from . resources_rc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1640, 960)
        MainWindow.setMinimumSize(QSize(1640, 960))
        MainWindow.setMaximumSize(QSize(1640, 960))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.styleSheet.setFont(font1)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	\n"
"}\n"
"\n"
"#pagesContainer #new_page #corearea,\n"
"#leftarea,\n"
"#resultarea,\n"
"#resultarea_2{\n"
"	border: 6px solid #fefefe;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* ////////////////////////////////////"
                        "/////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: #efefef;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	\n"
"}\n"
"#topLogo {\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 14px solid #fdfdfd;\n"
"	background-color: #fdfdfd;\n"
"	text-align: left;\n"
"	padding-left: 46px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-posit"
                        "ion: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: #0068ff;\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_menu.png);\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, "
                        "249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu"
                        " .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	\n"
"}\n"
"#contentBottom{\n"
"	\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton {  border: none;  border-radius: 5px; }\n"
"\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar {\n"
"	border-top:1px solid grey;\n"
" }\n"
"#bottomBar QLabel { font-size: 11px; ; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	borde"
                        "r-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: #0068ff;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-styl"
                        "e: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #fdfdfd;\n"
"	border-radius: 3px;\n"
"	border: 1px solid #000000;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"}\n"
"QLineEdit:focus {\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////"
                        "//////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 1px solid #0068ff;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: transparent;\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:#0068ff;\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 20px;\n"
"	border-top-"
                        "right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: #0068ff;\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background:transparent;\n"
"     height: 20px;\n"
"	borde"
                        "r-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid grey;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #fdfdfd;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid #0068ff;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    bac"
                        "kground: 3px solid #0068ff;\n"
"	border: 3px solid #0068ff;	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid grey;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #fdfdfd;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid #0068ff;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid #0068ff;\n"
"	border: 3px solid #0068ff;	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid #fefefe;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: #0068ff;"
                        "\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: #0068ff;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color:#fdfdfd;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: #0068ff;\n"
"    border: none;\n"
""
                        "    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"  \n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color:#fdfdfd;\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: #0068ff;\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color:"
                        " rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer #new_page QPushButton {\n"
"	background-color: #fdfdfd;\n"
"	border: 5px solid #fdfdfd;\n"
"	border-radius: 25px;	\n"
"	font: 12pt \u9ed1\u4f53;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0068ff;\n"
"	color:#fdfdfd;\n"
"}\n"
"#pagesContainer QPushButton{\n"
"	border: 4px solid #fdfdfd;\n"
"	border-radius: 15px;	\n"
"	background-color: #fdfdfd;\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.topLogo.setStyleSheet(u"")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftApp.setFont(font2)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleLeftDescription.setFont(font3)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftApp.raise_()
        self.titleLeftDescription.raise_()
        self.topLogo.raise_()

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font1)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setAutoFillBackground(False)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/5.png);")
        icon = QIcon()
        iconThemeName = u"accessories-calculator"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/icons/images/icons/icon1.png", QSize(), QIcon.Normal, QIcon.Off)

        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font1)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setAutoFillBackground(False)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/4.png);")
        icon1 = QIcon()
        iconThemeName = u"accessories-character-map"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u":/icons/images/icons/icon5.png", QSize(), QIcon.Normal, QIcon.Off)

        self.btn_widgets.setIcon(icon1)

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font1)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/3.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_ocr = QPushButton(self.topMenu)
        self.btn_ocr.setObjectName(u"btn_ocr")
        sizePolicy.setHeightForWidth(self.btn_ocr.sizePolicy().hasHeightForWidth())
        self.btn_ocr.setSizePolicy(sizePolicy)
        self.btn_ocr.setMinimumSize(QSize(0, 45))
        self.btn_ocr.setFont(font1)
        self.btn_ocr.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ocr.setLayoutDirection(Qt.LeftToRight)
        self.btn_ocr.setStyleSheet(u"background-image: url(:/icons/images/icons/1.png);")

        self.verticalLayout_8.addWidget(self.btn_ocr)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font1)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/2.png)")

        self.verticalLayout_8.addWidget(self.btn_save)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font1)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon2)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font1)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font1)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font1)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font1)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon3)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon4)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon5)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setStyleSheet(u"")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon6)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 4, 1, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font1)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: #fdfdfd;")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1157, 222))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color:#fdfdfd;")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 3, 3, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setStyleSheet(u"color:#000000;")
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.new_page.setStyleSheet(u"QFrame{\n"
"	background-color:#fdfdfd;\n"
"	border-radius:12px;\n"
"}\n"
"QTextBrowser{\n"
"	background-color:#efefef;\n"
"	border:none;\n"
"	border-radius:12px;\n"
"	padding:4px 6px;\n"
"}\n"
"*{\n"
"	font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"}")
        self.layoutWidget = QWidget(self.new_page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 21, 1531, 821))
        self.horizontalLayout_29 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.leftarea = QFrame(self.layoutWidget)
        self.leftarea.setObjectName(u"leftarea")
        self.leftarea.setStyleSheet(u"")
        self.leftarea.setFrameShape(QFrame.StyledPanel)
        self.leftarea.setFrameShadow(QFrame.Raised)
        self.left_title = QLabel(self.leftarea)
        self.left_title.setObjectName(u"left_title")
        self.left_title.setGeometry(QRect(60, 10, 121, 41))
        font6 = QFont()
        font6.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setItalic(False)
        self.left_title.setFont(font6)
        self.left_title.setStyleSheet(u"")
        self.res_image = QLabel(self.leftarea)
        self.res_image.setObjectName(u"res_image")
        self.res_image.setGeometry(QRect(100, 60, 731, 571))
        self.res_image.setStyleSheet(u"")
        self.res_image.setScaledContents(True)
        self.res_image.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.leftarea)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 41, 41))
        self.label_3.setPixmap(QPixmap(u"images/icons/judge.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.leftarea)

        self.corearea = QFrame(self.layoutWidget)
        self.corearea.setObjectName(u"corearea")
        self.corearea.setStyleSheet(u"")
        self.corearea.setFrameShape(QFrame.StyledPanel)
        self.corearea.setFrameShadow(QFrame.Raised)
        self.corearea_cors = QFrame(self.corearea)
        self.corearea_cors.setObjectName(u"corearea_cors")
        self.corearea_cors.setGeometry(QRect(30, 10, 871, 91))
        font7 = QFont()
        font7.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setItalic(False)
        self.corearea_cors.setFont(font7)
        self.corearea_cors.setStyleSheet(u"QPushButton{\n"
"	background-color:#0068ff;\n"
"	font-weight:700;\n"
"	font-size:24px;\n"
"	color:#fdfdfd;\n"
"	border:3px solid #0068ff;\n"
"	border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#0068ff;\n"
"	color:#fdfdfd;\n"
"}")
        self.corearea_cors.setFrameShape(QFrame.StyledPanel)
        self.corearea_cors.setFrameShadow(QFrame.Raised)
        self.Button_load = QPushButton(self.corearea_cors)
        self.Button_load.setObjectName(u"Button_load")
        self.Button_load.setGeometry(QRect(50, 20, 230, 60))
        font8 = QFont()
        font8.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font8.setBold(True)
        font8.setItalic(False)
        self.Button_load.setFont(font8)
        self.Button_load.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_load.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"images/icons/upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_load.setIcon(icon7)
        self.Button_load.setIconSize(QSize(30, 30))
        self.Button_meas = QPushButton(self.corearea_cors)
        self.Button_meas.setObjectName(u"Button_meas")
        self.Button_meas.setGeometry(QRect(590, 20, 230, 60))
        self.Button_meas.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_meas.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"images/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_meas.setIcon(icon8)
        self.Button_meas.setIconSize(QSize(30, 30))
        self.Button_recognize = QPushButton(self.corearea_cors)
        self.Button_recognize.setObjectName(u"Button_recognize")
        self.Button_recognize.setGeometry(QRect(320, 20, 230, 60))
        self.Button_recognize.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_recognize.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u"images/icons/view.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_recognize.setIcon(icon9)
        self.Button_recognize.setIconSize(QSize(30, 30))
        self.status_progressBar = QProgressBar(self.corearea)
        self.status_progressBar.setObjectName(u"status_progressBar")
        self.status_progressBar.setGeometry(QRect(30, 110, 871, 6))
        self.status_progressBar.setValue(24)
        self.status_progressBar.setTextVisible(False)

        self.verticalLayout_37.addWidget(self.corearea)

        self.verticalLayout_37.setStretch(0, 10)
        self.verticalLayout_37.setStretch(1, 2)

        self.horizontalLayout_29.addLayout(self.verticalLayout_37)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.resultarea = QFrame(self.layoutWidget)
        self.resultarea.setObjectName(u"resultarea")
        self.resultarea.setFont(font7)
        self.resultarea.setStyleSheet(u"")
        self.resultarea.setFrameShape(QFrame.StyledPanel)
        self.resultarea.setFrameShadow(QFrame.Raised)
        self.res_title = QLabel(self.resultarea)
        self.res_title.setObjectName(u"res_title")
        self.res_title.setGeometry(QRect(60, 10, 111, 41))
        font9 = QFont()
        font9.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font9.setPointSize(18)
        font9.setBold(False)
        font9.setItalic(False)
        self.res_title.setFont(font9)
        self.res_title.setStyleSheet(u"")
        self.res_title.setFrameShadow(QFrame.Raised)
        self.res_content = QTextBrowser(self.resultarea)
        self.res_content.setObjectName(u"res_content")
        self.res_content.setGeometry(QRect(15, 55, 565, 291))
        self.res_content.setFont(font6)
        self.res_content.setStyleSheet(u"")
        self.res_content.setReadOnly(True)
        self.label_27 = QLabel(self.resultarea)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 10, 41, 41))
        self.label_27.setPixmap(QPixmap(u"images/icons/result.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.resultarea)

        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.ori_img = QLabel(self.frame)
        self.ori_img.setObjectName(u"ori_img")
        self.ori_img.setGeometry(QRect(60, 60, 481, 331))
        self.ori_img.setScaledContents(True)
        self.ori_img.setAlignment(Qt.AlignCenter)
        self.label_55 = QLabel(self.frame)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(10, 10, 41, 41))
        self.label_55.setPixmap(QPixmap(u"images/icons/otherinfo.png"))
        self.label_55.setScaledContents(True)
        self.label_55.setAlignment(Qt.AlignCenter)
        self.res_title_2 = QLabel(self.frame)
        self.res_title_2.setObjectName(u"res_title_2")
        self.res_title_2.setGeometry(QRect(60, 11, 111, 41))
        self.res_title_2.setFont(font9)
        self.res_title_2.setStyleSheet(u"")
        self.res_title_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_38.addWidget(self.frame)

        self.verticalLayout_38.setStretch(0, 5)
        self.verticalLayout_38.setStretch(1, 6)

        self.horizontalLayout_29.addLayout(self.verticalLayout_38)

        self.horizontalLayout_29.setStretch(0, 25)
        self.horizontalLayout_29.setStretch(1, 16)
        self.stackedWidget.addWidget(self.new_page)
        self.new_page2 = QWidget()
        self.new_page2.setObjectName(u"new_page2")
        self.new_page2.setStyleSheet(u"#patience,\n"
"#res,\n"
"#tables_upload{\n"
"	border-radius:12px;\n"
"	background-color:#fdfdfd;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#0068ff;\n"
"}\n"
"#change:hover{\n"
"	background-color:#fdfdfd;\n"
"}\n"
"QTableWidget{\n"
"	border:none;\n"
"}\n"
"#upload #clue{\n"
"	margin: 0px 15px;\n"
"}\n"
"#patience #info QLineEdit{\n"
"	border:none;\n"
"	font-size: 18px;\n"
"}\n"
"#tables_upload #tables #table_1 QLabel{\n"
"	border:1px solid grey;\n"
"}\n"
"QPushButton{\n"
"	font-weight:700;\n"
"	font-size:18px;\n"
"	border:none;\n"
"	border-radius:9px;	\n"
"	margin-left:4px;\n"
" 	margin-right:4px;\n"
"}\n"
"QComboBox{\n"
"	background-color:#fdfdfd;\n"
"	border:1px solid grey;\n"
"	margin-right:10px;\n"
"}\n"
"QComboBox:hover{\n"
"	background-color:#0068ff;\n"
"	border:1px solid grey;\n"
"}\n"
"QComboBox::drop-down {\n"
"	border-left-color: transparent;\n"
"}\n"
"QTextBrowser{\n"
"	background-color:#efefef;\n"
"	border:none;\n"
"	border-radius:12px;\n"
" 	margin-left:4px;\n"
"}\n"
"*{font-family:\u5fae\u8f6f"
                        "\u96c5\u9ed1;}")
        self.layoutWidget1 = QWidget(self.new_page2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 20, 1531, 821))
        self.orc = QHBoxLayout(self.layoutWidget1)
        self.orc.setSpacing(10)
        self.orc.setObjectName(u"orc")
        self.orc.setContentsMargins(0, 0, 0, 0)
        self.patience = QFrame(self.layoutWidget1)
        self.patience.setObjectName(u"patience")
        self.patience.setFrameShape(QFrame.StyledPanel)
        self.patience.setFrameShadow(QFrame.Raised)
        self.layoutWidget2 = QWidget(self.patience)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(9, 10, 361, 801))
        self.verticalLayout_23 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.info = QFrame(self.layoutWidget2)
        self.info.setObjectName(u"info")
        self.info.setFrameShape(QFrame.StyledPanel)
        self.info.setFrameShadow(QFrame.Raised)
        self.layoutWidget3 = QWidget(self.info)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 50, 331, 28))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.name = QLabel(self.layoutWidget3)
        self.name.setObjectName(u"name")

        self.horizontalLayout_10.addWidget(self.name)

        self.name_info = QLineEdit(self.layoutWidget3)
        self.name_info.setObjectName(u"name_info")
        self.name_info.setFrame(True)
        self.name_info.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.name_info)

        self.layoutWidget4 = QWidget(self.info)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 140, 331, 28))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.phone = QLabel(self.layoutWidget4)
        self.phone.setObjectName(u"phone")

        self.horizontalLayout_13.addWidget(self.phone)

        self.phone_info = QLineEdit(self.layoutWidget4)
        self.phone_info.setObjectName(u"phone_info")
        self.phone_info.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.phone_info)

        self.layoutWidget5 = QWidget(self.info)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 110, 331, 28))
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.age = QLabel(self.layoutWidget5)
        self.age.setObjectName(u"age")

        self.horizontalLayout_14.addWidget(self.age)

        self.age_info = QLineEdit(self.layoutWidget5)
        self.age_info.setObjectName(u"age_info")
        self.age_info.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.age_info)

        self.layoutWidget6 = QWidget(self.info)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(10, 80, 331, 28))
        self.horizontalLayout_15 = QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.sex = QLabel(self.layoutWidget6)
        self.sex.setObjectName(u"sex")

        self.horizontalLayout_15.addWidget(self.sex)

        self.sex_info = QLineEdit(self.layoutWidget6)
        self.sex_info.setObjectName(u"sex_info")
        self.sex_info.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.sex_info)

        self.title_patience = QLabel(self.info)
        self.title_patience.setObjectName(u"title_patience")
        self.title_patience.setGeometry(QRect(40, 9, 92, 31))
        self.icon_patience = QLabel(self.info)
        self.icon_patience.setObjectName(u"icon_patience")
        self.icon_patience.setGeometry(QRect(0, 8, 30, 30))
        self.icon_patience.setPixmap(QPixmap(u"images/icons/patienceinfo.png"))
        self.icon_patience.setScaledContents(True)
        self.icon_patience.setAlignment(Qt.AlignCenter)
        self.change = QPushButton(self.info)
        self.change.setObjectName(u"change")
        self.change.setGeometry(QRect(325, 10, 30, 30))
        self.change.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u"images/icons/change.png", QSize(), QIcon.Normal, QIcon.Off)
        self.change.setIcon(icon10)
        self.change.setIconSize(QSize(25, 25))

        self.verticalLayout_23.addWidget(self.info)

        self.otherinfo = QFrame(self.layoutWidget2)
        self.otherinfo.setObjectName(u"otherinfo")
        self.otherinfo.setFrameShape(QFrame.StyledPanel)
        self.otherinfo.setFrameShadow(QFrame.Raised)
        self.icon_other = QLabel(self.otherinfo)
        self.icon_other.setObjectName(u"icon_other")
        self.icon_other.setGeometry(QRect(0, 5, 30, 30))
        self.icon_other.setPixmap(QPixmap(u"images/icons/otherinfo.png"))
        self.icon_other.setScaledContents(True)
        self.icon_other.setAlignment(Qt.AlignCenter)
        self.title_other = QLabel(self.otherinfo)
        self.title_other.setObjectName(u"title_other")
        self.title_other.setGeometry(QRect(40, 6, 92, 31))
        self.layoutWidget7 = QWidget(self.otherinfo)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(-4, 41, 361, 551))
        self.verticalLayout_36 = QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(3, 0, 0, 0)
        self.otherinfomation = QTextBrowser(self.layoutWidget7)
        self.otherinfomation.setObjectName(u"otherinfomation")
        self.otherinfomation.setStyleSheet(u"margin-top:4px;")

        self.verticalLayout_36.addWidget(self.otherinfomation)

        self.add_info = QPushButton(self.layoutWidget7)
        self.add_info.setObjectName(u"add_info")
        self.add_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_info.setStyleSheet(u"margin-right:0;")

        self.verticalLayout_36.addWidget(self.add_info)


        self.verticalLayout_23.addWidget(self.otherinfo)

        self.verticalLayout_23.setStretch(0, 1)
        self.verticalLayout_23.setStretch(1, 3)

        self.orc.addWidget(self.patience)

        self.tables_upload = QFrame(self.layoutWidget1)
        self.tables_upload.setObjectName(u"tables_upload")
        self.tables_upload.setFrameShape(QFrame.StyledPanel)
        self.tables_upload.setFrameShadow(QFrame.Raised)
        self.layoutWidget8 = QWidget(self.tables_upload)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(0, 0, 601, 821))
        self.verticalLayout_20 = QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.tables = QFrame(self.layoutWidget8)
        self.tables.setObjectName(u"tables")
        self.tables.setStyleSheet(u"")
        self.tables.setFrameShape(QFrame.StyledPanel)
        self.tables.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.tables)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 69, 31))
        self.table_2 = QFrame(self.tables)
        self.table_2.setObjectName(u"table_2")
        self.table_2.setGeometry(QRect(10, 100, 581, 221))
        self.verticalLayout_28 = QVBoxLayout(self.table_2)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_23 = QLabel(self.table_2)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_21.addWidget(self.label_23)

        self.label_22 = QLabel(self.table_2)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_21.addWidget(self.label_22)

        self.label_21 = QLabel(self.table_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_21)

        self.label_20 = QLabel(self.table_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_20)

        self.horizontalLayout_21.setStretch(0, 3)
        self.horizontalLayout_21.setStretch(1, 1)
        self.horizontalLayout_21.setStretch(2, 2)
        self.horizontalLayout_21.setStretch(3, 2)

        self.verticalLayout_28.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_4 = QLabel(self.table_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_24.addWidget(self.label_4)

        self.label_6 = QLabel(self.table_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_24.addWidget(self.label_6)

        self.label_5 = QLabel(self.table_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_24.addWidget(self.label_5)

        self.label_8 = QLabel(self.table_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_24.addWidget(self.label_8)

        self.label_7 = QLabel(self.table_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_24.addWidget(self.label_7)

        self.label_53 = QLabel(self.table_2)
        self.label_53.setObjectName(u"label_53")

        self.verticalLayout_24.addWidget(self.label_53)


        self.horizontalLayout_20.addLayout(self.verticalLayout_24)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.bpd = QCheckBox(self.table_2)
        self.bpd.setObjectName(u"bpd")
        self.bpd.setCursor(QCursor(Qt.PointingHandCursor))
        self.bpd.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_26.addWidget(self.bpd)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer)

        self.hc1 = QCheckBox(self.table_2)
        self.hc1.setObjectName(u"hc1")
        self.hc1.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_26.addWidget(self.hc1)

        self.hc2 = QCheckBox(self.table_2)
        self.hc2.setObjectName(u"hc2")
        self.hc2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_26.addWidget(self.hc2)

        self.ac = QCheckBox(self.table_2)
        self.ac.setObjectName(u"ac")
        self.ac.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_26.addWidget(self.ac)

        self.fl = QCheckBox(self.table_2)
        self.fl.setObjectName(u"fl")
        self.fl.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_26.addWidget(self.fl)

        self.verticalLayout_26.setStretch(0, 1)
        self.verticalLayout_26.setStretch(1, 1)
        self.verticalLayout_26.setStretch(2, 1)
        self.verticalLayout_26.setStretch(3, 1)
        self.verticalLayout_26.setStretch(4, 1)
        self.verticalLayout_26.setStretch(5, 1)

        self.horizontalLayout_20.addLayout(self.verticalLayout_26)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.bpd_v = QLabel(self.table_2)
        self.bpd_v.setObjectName(u"bpd_v")
        self.bpd_v.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.bpd_v)

        self.ofd_v = QLabel(self.table_2)
        self.ofd_v.setObjectName(u"ofd_v")
        self.ofd_v.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.ofd_v)

        self.hc1_v = QLabel(self.table_2)
        self.hc1_v.setObjectName(u"hc1_v")
        self.hc1_v.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.hc1_v)

        self.hc2_v = QLabel(self.table_2)
        self.hc2_v.setObjectName(u"hc2_v")
        self.hc2_v.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.hc2_v)

        self.ac_v = QLabel(self.table_2)
        self.ac_v.setObjectName(u"ac_v")
        self.ac_v.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.ac_v)

        self.fl_v = QLabel(self.table_2)
        self.fl_v.setObjectName(u"fl_v")
        self.fl_v.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.fl_v)


        self.horizontalLayout_20.addLayout(self.verticalLayout_25)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.bpd_m = QLabel(self.table_2)
        self.bpd_m.setObjectName(u"bpd_m")
        self.bpd_m.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.bpd_m)

        self.ofd_m = QLabel(self.table_2)
        self.ofd_m.setObjectName(u"ofd_m")
        self.ofd_m.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.ofd_m)

        self.hc1_m = QLabel(self.table_2)
        self.hc1_m.setObjectName(u"hc1_m")
        self.hc1_m.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.hc1_m)

        self.hc2_m = QLabel(self.table_2)
        self.hc2_m.setObjectName(u"hc2_m")
        self.hc2_m.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.hc2_m)

        self.ac_m = QLabel(self.table_2)
        self.ac_m.setObjectName(u"ac_m")
        self.ac_m.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.ac_m)

        self.fl_m = QLabel(self.table_2)
        self.fl_m.setObjectName(u"fl_m")
        self.fl_m.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.fl_m)


        self.horizontalLayout_20.addLayout(self.verticalLayout_27)

        self.horizontalLayout_20.setStretch(0, 3)
        self.horizontalLayout_20.setStretch(1, 1)
        self.horizontalLayout_20.setStretch(2, 2)
        self.horizontalLayout_20.setStretch(3, 2)

        self.verticalLayout_28.addLayout(self.horizontalLayout_20)

        self.table_3 = QFrame(self.tables)
        self.table_3.setObjectName(u"table_3")
        self.table_3.setGeometry(QRect(10, 330, 581, 231))
        self.verticalLayout_29 = QVBoxLayout(self.table_3)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_26 = QLabel(self.table_3)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_23.addWidget(self.label_26)


        self.verticalLayout_29.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_28 = QLabel(self.table_3)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_31.addWidget(self.label_28)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_3)

        self.label_29 = QLabel(self.table_3)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_31.addWidget(self.label_29)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_2)

        self.label_30 = QLabel(self.table_3)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_31.addWidget(self.label_30)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_6)

        self.label_31 = QLabel(self.table_3)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_31.addWidget(self.label_31)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_8)

        self.label_32 = QLabel(self.table_3)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_31.addWidget(self.label_32)


        self.horizontalLayout_22.addLayout(self.verticalLayout_31)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.flac = QLabel(self.table_3)
        self.flac.setObjectName(u"flac")
        self.flac.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.flac)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_4)

        self.hcac = QLabel(self.table_3)
        self.hcac.setObjectName(u"hcac")
        self.hcac.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.hcac)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_5)

        self.flhc = QLabel(self.table_3)
        self.flhc.setObjectName(u"flhc")
        self.flhc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.flhc)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_7)

        self.flbpd = QLabel(self.table_3)
        self.flbpd.setObjectName(u"flbpd")
        self.flbpd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.flbpd)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_9)

        self.ci = QLabel(self.table_3)
        self.ci.setObjectName(u"ci")
        self.ci.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.ci)


        self.horizontalLayout_22.addLayout(self.verticalLayout_32)

        self.horizontalLayout_22.setStretch(0, 3)
        self.horizontalLayout_22.setStretch(1, 5)

        self.verticalLayout_29.addLayout(self.horizontalLayout_22)

        self.title_tables = QLabel(self.tables)
        self.title_tables.setObjectName(u"title_tables")
        self.title_tables.setGeometry(QRect(50, 18, 92, 31))
        self.icon_tables = QLabel(self.tables)
        self.icon_tables.setObjectName(u"icon_tables")
        self.icon_tables.setGeometry(QRect(10, 18, 30, 30))
        self.icon_tables.setPixmap(QPixmap(u"images/icons/judge.png"))
        self.icon_tables.setScaledContents(True)
        self.icon_tables.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.tables)

        self.upload = QFrame(self.layoutWidget8)
        self.upload.setObjectName(u"upload")
        self.upload.setStyleSheet(u"")
        self.upload.setFrameShape(QFrame.StyledPanel)
        self.upload.setFrameShadow(QFrame.Raised)
        self.title_upload = QLabel(self.upload)
        self.title_upload.setObjectName(u"title_upload")
        self.title_upload.setGeometry(QRect(50, 2, 92, 31))
        self.icon_upload = QLabel(self.upload)
        self.icon_upload.setObjectName(u"icon_upload")
        self.icon_upload.setGeometry(QRect(10, 2, 30, 30))
        self.icon_upload.setStyleSheet(u"")
        self.icon_upload.setPixmap(QPixmap(u"images/icons/template.png"))
        self.icon_upload.setScaledContents(True)
        self.icon_upload.setAlignment(Qt.AlignCenter)
        self.template_input = QComboBox(self.upload)
        self.template_input.setObjectName(u"template_input")
        self.template_input.setGeometry(QRect(390, 0, 211, 34))
        self.template_input.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_2 = QLabel(self.upload)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(313, 1, 68, 31))
        self.layoutWidget9 = QWidget(self.upload)
        self.layoutWidget9.setObjectName(u"layoutWidget9")
        self.layoutWidget9.setGeometry(QRect(0, 40, 601, 153))
        self.verticalLayout_21 = QVBoxLayout(self.layoutWidget9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(3, 2, 0, 9)
        self.clue = QTextBrowser(self.layoutWidget9)
        self.clue.setObjectName(u"clue")
        self.clue.setStyleSheet(u"margin-left:9px;margin-right:10px;")

        self.verticalLayout_21.addWidget(self.clue)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.upload_img = QPushButton(self.layoutWidget9)
        self.upload_img.setObjectName(u"upload_img")
        self.upload_img.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.upload_img)

        self.identify = QPushButton(self.layoutWidget9)
        self.identify.setObjectName(u"identify")
        self.identify.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.identify)

        self.save = QPushButton(self.layoutWidget9)
        self.save.setObjectName(u"save")
        self.save.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.save)

        self.print = QPushButton(self.layoutWidget9)
        self.print.setObjectName(u"print")
        self.print.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.print)


        self.verticalLayout_21.addLayout(self.horizontalLayout_17)


        self.verticalLayout_20.addWidget(self.upload)

        self.verticalLayout_20.setStretch(0, 200)
        self.verticalLayout_20.setStretch(1, 63)

        self.orc.addWidget(self.tables_upload)

        self.res = QFrame(self.layoutWidget1)
        self.res.setObjectName(u"res")
        self.res.setFrameShape(QFrame.StyledPanel)
        self.res.setFrameShadow(QFrame.Raised)
        self.title_res = QLabel(self.res)
        self.title_res.setObjectName(u"title_res")
        self.title_res.setGeometry(QRect(49, 20, 92, 31))
        self.icon_res = QLabel(self.res)
        self.icon_res.setObjectName(u"icon_res")
        self.icon_res.setGeometry(QRect(9, 21, 30, 30))
        self.icon_res.setPixmap(QPixmap(u"images/icons/result.png"))
        self.icon_res.setScaledContents(True)
        self.icon_res.setAlignment(Qt.AlignCenter)
        self.layoutWidget10 = QWidget(self.res)
        self.layoutWidget10.setObjectName(u"layoutWidget10")
        self.layoutWidget10.setGeometry(QRect(8, 59, 511, 751))
        self.verticalLayout_22 = QVBoxLayout(self.layoutWidget10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 2)
        self.result = QTextBrowser(self.layoutWidget10)
        self.result.setObjectName(u"result")
        self.result.setStyleSheet(u"margin-right:2px;")

        self.verticalLayout_22.addWidget(self.result)

        self.print_area = QLabel(self.layoutWidget10)
        self.print_area.setObjectName(u"print_area")
        self.print_area.setScaledContents(True)
        self.print_area.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.print_area)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.print_browser = QPushButton(self.layoutWidget10)
        self.print_browser.setObjectName(u"print_browser")
        self.print_browser.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_18.addWidget(self.print_browser)

        self.exit = QPushButton(self.layoutWidget10)
        self.exit.setObjectName(u"exit")
        self.exit.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_18.addWidget(self.exit)

        self.horizontalLayout_18.setStretch(0, 3)
        self.horizontalLayout_18.setStretch(1, 1)

        self.verticalLayout_22.addLayout(self.horizontalLayout_18)

        self.verticalLayout_22.setStretch(0, 3)
        self.verticalLayout_22.setStretch(1, 4)

        self.orc.addWidget(self.res)

        self.orc.setStretch(0, 5)
        self.orc.setStretch(1, 8)
        self.orc.setStretch(2, 7)
        self.stackedWidget.addWidget(self.new_page2)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font1)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font1)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font1)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setBold(False)
        font10.setItalic(False)
        self.creditsLabel.setFont(font10)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u5168\u6808\u8d85\u58f0\u5f71\u50cf\u8bca\u65ad\u7cfb\u7edf", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u56fd\u77ff\u4e1a\u5927\u5b66\u5f00\u53d1", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u9996\u9875", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u4e2d\u5fc3", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"AI\u6d4b\u8ddd", None))
        self.btn_ocr.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"\u5de6\u83dc\u5355", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#ffffff;\">An interface created using Python and PySide (sup"
                        "port for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe "
                        "UI'; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u5f90\u5dde\u5e02\u7b2c\u4e00\u4eba\u6c11\u533b\u9662", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u5728\u8fd9\u8f93\u5165\u6587\u4ef6\u8def\u5f84", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"2022\u5e7412\u6708", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u67e5\u8be2", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6a21\u578bA", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u7acb\u5373\u6d4b\u8ddd", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4\u7f16\u53f7", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u6d4b\u8ddd\u4fe1\u606f", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"AI\u6d4b\u8ddd\u4fe1\u606f", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u5206", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.left_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#0068ff;\">\u5206\u5272\u7ed3\u679c</span></p></body></html>", None))
        self.res_image.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u5206\u5272\u7ed3\u679c</span></p></body></html>", None))
        self.label_3.setText("")
        self.Button_load.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u6570\u636e", None))
        self.Button_meas.setText(QCoreApplication.translate("MainWindow", u"\u667a\u80fd\u6d4b\u8ddd", None))
        self.Button_recognize.setText(QCoreApplication.translate("MainWindow", u"\u5206\u5272\u5207\u9762", None))
        self.res_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#0068ff;\">\u6d4b\u8ddd\u4fe1\u606f</span></p></body></html>", None))
        self.res_content.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">\u6682\u65e0\u6d4b\u8ddd\u4fe1\u606f</span></p></body></html>", None))
        self.label_27.setText("")
        self.ori_img.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u539f\u59cb\u6570\u636e</span></p></body></html>", None))
        self.label_55.setText("")
        self.res_title_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#0068ff;\">\u539f\u59cb\u56fe\u7247</span></p></body></html>", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">\u59d3\u540d\uff1a</span></p></body></html>", None))
        self.name_info.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u660e", None))
        self.phone.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">\u7535\u8bdd\uff1a</span></p></body></html>", None))
        self.phone_info.setText(QCoreApplication.translate("MainWindow", u"17462534980", None))
        self.age.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">\u5e74\u9f84\uff1a</span></p></body></html>", None))
        self.age_info.setText(QCoreApplication.translate("MainWindow", u"46", None))
        self.sex.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">\u6027\u522b\uff1a</span></p></body></html>", None))
        self.sex_info.setText(QCoreApplication.translate("MainWindow", u"\u5973", None))
        self.title_patience.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#0068ff;\">\u60a3\u8005\u4fe1\u606f</span></p></body></html>", None))
        self.icon_patience.setText("")
        self.change.setText("")
        self.icon_other.setText("")
        self.title_other.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#0068ff;\">\u5176\u4ed6\u4fe1\u606f</span></p></body></html>", None))
        self.add_info.setText(QCoreApplication.translate("MainWindow", u"\u8865\u5145\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">\u8bca\u65ad\u63cf\u8ff0</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">2D Measurements</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">AUA</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Value</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">m</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"BPD(Hadlock)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"OFD(HC)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"HC(Hadlock)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"HC*(Hadlock)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"AC(Hadlock)", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"FL(Hadlock)", None))
        self.bpd.setText("")
        self.hc1.setText("")
        self.hc2.setText("")
        self.ac.setText("")
        self.fl.setText("")
        self.bpd_v.setText(QCoreApplication.translate("MainWindow", u"32.55mm", None))
        self.ofd_v.setText(QCoreApplication.translate("MainWindow", u"32.55mm", None))
        self.hc1_v.setText(QCoreApplication.translate("MainWindow", u"32.55mm", None))
        self.hc2_v.setText(QCoreApplication.translate("MainWindow", u"31.55mm", None))
        self.ac_v.setText(QCoreApplication.translate("MainWindow", u"32.55mm", None))
        self.fl_v.setText(QCoreApplication.translate("MainWindow", u"32.55mm", None))
        self.bpd_m.setText(QCoreApplication.translate("MainWindow", u"32.55", None))
        self.ofd_m.setText(QCoreApplication.translate("MainWindow", u"32.55", None))
        self.hc1_m.setText(QCoreApplication.translate("MainWindow", u"42.44", None))
        self.hc2_m.setText(QCoreApplication.translate("MainWindow", u"32.55", None))
        self.ac_m.setText(QCoreApplication.translate("MainWindow", u"32.55", None))
        self.fl_m.setText(QCoreApplication.translate("MainWindow", u"32.55", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">2D Calculation</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"FL/AC", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"HC/AC(Campbell)", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"FL/HC(Hadlock)", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"FL/BPD", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"CI(BPD/OFD)", None))
        self.flac.setText(QCoreApplication.translate("MainWindow", u"19%(20-24%)", None))
        self.hcac.setText(QCoreApplication.translate("MainWindow", u"1.09(GA:OOR)", None))
        self.flhc.setText(QCoreApplication.translate("MainWindow", u"0.17(GA:OOR)", None))
        self.flbpd.setText(QCoreApplication.translate("MainWindow", u"65%(GA:OOR)", None))
        self.ci.setText(QCoreApplication.translate("MainWindow", u"74%(70-86%)", None))
        self.title_tables.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#0068ff;\">\u8bca\u65ad\u7ed3\u679c</span></p></body></html>", None))
        self.icon_tables.setText("")
        self.title_upload.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#0068ff;\">\u8bca\u65ad\u63d0\u793a</span></p></body></html>", None))
        self.icon_upload.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">\u5bfc\u5165\u6a21\u677f</span></p></body></html>", None))
        self.upload_img.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20", None))
        self.identify.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.print.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5370", None))
        self.title_res.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#0068ff;\">\u751f\u6210\u7ed3\u679c</span></p></body></html>", None))
        self.icon_res.setText("")
        self.print_area.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8\u533a\u57df", None))
        self.print_browser.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5370\u9884\u89c8", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: \u4e2d\u56fd\u77ff\u4e1a\u5927\u5b66", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v2.0.2", None))
    # retranslateUi

