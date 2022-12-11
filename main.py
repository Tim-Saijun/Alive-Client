# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from PySide6 import QtGui

from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "全栈式超声影像诊断系统"
        description = "开发中"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        # widgets.btn_measure.clicked.connect(self.buttonClick)
        widgets.pushButton_6.clicked.connect(self.fill_demo_heart)
        widgets.pushButton_5.clicked.connect(self.fill_demo_xqjy)
        widgets.pushButton_7.clicked.connect(self.fill_demo_xgcz)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            print("Save BTN clicked!")

        if btnName == "btn_measure":
            widgets.stackedWidget.setCurrentWidget(widgets.measure) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def fill_demo_heart(self):
        # FILL label and label_2 with demo picture from file
        # ///////////////////////////////////////////////////////////////
        widgets.label.setPixmap(QtGui.QPixmap("images/images/demo/demo/心脏测距/1.bmp"))
        widgets.label_2.setPixmap(QtGui.QPixmap("images/images/demo/demo/心脏测距/1_result.bmp"))
        #fill textBrowser with demo text
        widgets.textBrowser.setText("模型A的测距结果：\
                                                            左心房轴距：47 55\
                                                            右心房轴距：50 55\
                                                            左心室轴距：99 98\
                                                            右心室轴距：88 160\
                                                            降主动脉： 30 32\
                                                            与您的测距匹配程度为97%")

    def fill_demo_xqjy(self):
        # FILL label and label_2 with demo picture from file
        # ///////////////////////////////////////////////////////////////
        widgets.label.setPixmap(QtGui.QPixmap("images/images/demo/demo/胸腔积液/1400003.jpg"))
        widgets.label_2.setPixmap(QtGui.QPixmap("images/images/demo/demo/胸腔积液/1400003_result.jpg"))
        #fill textBrowser with demo text
        widgets.textBrowser.setText("模型A的测距结果：\
                                                            主轴距：58 mm\
                                                            偏轴距：32 mm\
                                                            与您的测距匹配程度为87%")
        widgets.textEdit_2.setText("46")
        widgets.textEdit_3.setText("27")
        widgets.textEdit_4.setText(" ")
        widgets.textEdit_5.setText(" ")
        widgets.textEdit_6.setText(" ")
        #将label_8的文字改为“主轴距”
        widgets.label_8.setText("主轴距：")
        widgets.label_9.setText("偏轴距：")
        widgets.label_10.setText(" ")
        widgets.label_11.setText(" ")
        widgets.label_12.setText(" ")

    def fill_demo_xgcz(self):
            # FILL label and label_2 with demo picture from file
            # ///////////////////////////////////////////////////////////////
            widgets.label.setPixmap(QtGui.QPixmap("images/images/demo/demo/胸骨长轴/47800001.jpg"))
            widgets.label_2.setPixmap(QtGui.QPixmap("images/images/demo/demo/胸骨长轴/Inked47800001_LI_re.jpg"))
            # fill textBrowser with demo text
            widgets.textBrowser.setText("模型A的测距结果：\
                                                                RV轴距：21 mm\
                                                                LV轴距：27 mm\
                                                                AO轴距:  30 mm\
                                                                LA轴距:  26 mm\
                                                                DA轴距:  25 mm\
                                                                与您的测距匹配程度为92%")
            #将texEdit_2的文字改为“21”
            widgets.textEdit_2.setText("21")
            widgets.textEdit_3.setText("27")
            widgets.textEdit_4.setText("22")
            widgets.textEdit_5.setText("26")
            widgets.textEdit_6.setText("25")
            # 将label_8的文字改为“主轴距”
            widgets.label_8.setText("RV轴距：")
            widgets.label_9.setText("LV轴距：")
            widgets.label_10.setText("AO轴距：")
            widgets.label_11.setText("LA轴距：")
            widgets.label_12.setText("DAO轴距：")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
