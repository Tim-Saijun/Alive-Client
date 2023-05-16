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
import ast
import sys
import os
import platform
import time

import fitz
from PIL import Image, ImageTk
import tkinter as tk
import os
import subprocess

import requests
import json
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from PySide6 import QtGui
from PySide6.QtWidgets import QFileDialog,QApplication

from PySide6.QtCore import QUrl
from PySide6.QtGui import QPageSize, QPagedPaintDevice, QPainter, QColor

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics,ttfonts

from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
# server = 'http://124.71.136.39:80'
server = 'http://127.0.0.1:80'
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.whs = None #服务器测距返回的结果
        self.impdata = None #导入的测距数据
        self.img = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "中国矿业大学超声影像文字识别系统"
        description = "中国矿业大学超声影像文字识别系统"
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
        widgets.btn_ocr.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        # widgets.btn_measure.clicked.connect(self.buttonClick)
        # widgets.pushButton_6.clicked.connect(self.fill_demo_heart)
        # widgets.pushButton_5.clicked.connect(self.fill_demo_xqjy)
        # widgets.pushButton_7.clicked.connect(self.fill_demo_xgcz)
        widgets.Button_load.clicked.connect(self.load_img_off)
        widgets.Button_meas.clicked.connect(self.measure_off)
        widgets.Button_recognize.clicked.connect(self.inference_off)
        # widgets.comboBox_choosemodel.currentIndexChanged.connect(self.change_view(self.ui.comboBox_choosemodel.currentText()))
        widgets.upload_img.clicked.connect(self.ocr_upload_img)
        widgets.identify.clicked.connect(self.ocr_recognize)
        widgets.save.clicked.connect(self.ocr_save_result)
        widgets.print.clicked.connect(self.ocr_print_result)

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

        if btnName == "btn_ocr":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page2) # SET PAGE
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

    def load_img(self):#加载图像按钮触发:本地图框填充、图片上传服务器
        select_originimg = QFileDialog.getOpenFileName(None,"选择要评测的原始图片")[0]
        #TODO: 过滤选择的图片格式
        #将选择的图片显示在ori_img标签上
        widgets.ori_img.setPixmap(QtGui.QPixmap(select_originimg))
        print("已选择原始图片:",select_originimg)
        self.ui.res_content.setText("您已选择原始图片-----\n"+select_originimg)
        self.img = select_originimg
        img_name = os.path.basename(self.img)
        #下面是读取图片发给服务器
        with open(self.img,'rb') as f:
            img_data = f.read()
            files = {'img':img_data}
        submit_data = {'img_name':img_name}
        r = requests.post(server+'/upload',submit_data,files=files)
        # self.ui.textBrowser.setText(json.loads(r.text)['msg'])
        print(json.loads(r.text)['msg'])

        #加载原始评分数据，先用demo数据填充
        demo_data = [(95, 100), (85, 151), (142, 194), (145, 206), (33, 45)]
        self.impdata = demo_data
        a1, a2, b1, b2, c1, c2, d1, d2, e1, e2 = self.impdata[0][0], self.impdata[0][1], self.impdata[1][0], self.impdata[1][1], \
            self.impdata[2][0], self.impdata[2][1], self.impdata[3][0], self.impdata[3][1], self.impdata[4][0], self.impdata[4][1]
        res_text = "您导入的测距结果为-----\n左心房长宽：{:.2f}*{:.2f}mm\n右心房长宽：{:.2f}*{:.2f}mm\n右心室长宽：{:.2f}*{:.2f}mm\n左心室长宽：{:.2f}*{:.2f}mm\n降主动脉长宽：{:.2f}*{:.2f}mm\n".format(
            a1, a2, b1, b2, c1, c2, d1, d2, e1, e2)
        self.ui.res_content.append(res_text)


    def ai_inference(self):#AI测距按钮触发
        self.ui.status_progressBar.setValue(0)
        # print(self.img)
        #TODO:空图片的判定驳回
        # self.ui.plainTextEdit_9.setPlainText('356')#设置值
        # abc = self.ui.plainTextEdit_9.toPlainText()#读值
        #TODO:AI测距前先要求输入评分
        img_name = os.path.basename(self.img)
        print("推送图像：",img_name)
        para = {'img_name':img_name}
        self.ui.status_progressBar.setValue(20)
        r = requests.get(server+'/inference', params= para)
        #等等服务器3-5s
        # time.sleep(5)
        self.ui.status_progressBar.setValue(50)
        rt = json.loads(r.text)#把json解析成字典
        """格式如下，whs[5][2]代表了每个目标的长宽
            res = {"code": 200,
           'msg': "成功响应",
           "time_inference":time_inference,
           "time_measure":time_measure,
           "whs":str(whs)}最靠近降主动脉的的是左心房，按逆时针依次是左心房、右心房、右心室、左心室、降主动脉
        """
        self.whs = ast.literal_eval(rt['whs'])
        print(self.whs,type(self.whs))
        # self.ui.res_content.setText(str(rt))
        self.ui.status_progressBar.setValue(60)
        url_file = server+'/download_inference'
        File = requests.get(url_file, stream=True,params=para)
        if (os.path.exists('outcomes')):
            pass
        else:
            os.makedirs('outcomes')
        result_path = os.path.join('outcomes',img_name)
        with open(result_path, 'wb+') as f:
            # 分块写入文件
            for chunk in File.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        f.close()
        print("已获得服务器测距图片")
        self.ui.status_progressBar.setValue(70)
        self.ui.res_image.setPixmap(QtGui.QPixmap(result_path))
        self.ui.status_progressBar.setValue(80)
        #左下显示测距结果
        a1, a2, b1, b2, c1, c2, d1, d2, e1, e2 = self.whs[0][0], self.whs[0][1], self.whs[1][0], self.whs[1][1], self.whs[2][0], self.whs[2][1], self.whs[3][0], self.whs[3][1], self.whs[4][0], self.whs[4][1]
        res_text = "AI模型测距的结果为-----\n左心房长宽：{:.2f}*{:.2f}mm\n右心房长宽：{:.2f}*{:.2f}mm\n右心室长宽：{:.2f}*{:.2f}mm\n左心室长宽：{:.2f}*{:.2f}mm\n降主动脉长宽：{:.2f}*{:.2f}mm\n".format(a1, a2, b1, b2, c1, c2, d1, d2, e1, e2)
        self.ui.res_content.append(res_text)
        #在res_content中追加hstr字符串
        # self.ui.res_content.appendPlainText(hstr)
        #计算评分
        origin_list = self.impdata
        mark = 0
        for r1 , r2 in zip(origin_list,self.whs):
            area1 = r1[0]*r1[1]
            are2 = r2[0]*r2[1]
            tp1 = min(are2,area1)
            tp2 = max(area1,are2)
            mark+=(tp1/tp2)/5
        mark = mark*100
        print(mark)
        #弹窗显示评分
        QMessageBox.information(self, "评分", "评分为：{:.2f}".format(mark), QMessageBox.Yes | QMessageBox.No)
        self.ui.res_content.append("评分为：{:.2f}".format(mark))
        self.ui.status_progressBar.setValue(100)


    def evaluate(self):
        #TODO:评分前先检查是否进行AI测距并得到结果
        """
        #从左中五个文本框中读取测距结果，旧版本逻辑，已废弃
        origin_list = []
        origin_list.append(list(map(int,self.ui.in1_text.toPlainText().split('*'))))
        origin_list.append(list(map(int,self.ui.in2_text.toPlainText().split('*'))))
        origin_list.append(list(map(int,self.ui.in3_text.toPlainText().split('*'))))
        origin_list.append(list(map(int,self.ui.in4_text.toPlainText().split('*'))))
        origin_list.append(list(map(int,self.ui.in5_text.toPlainText().split('*'))))
        """
        origin_list = self.impdata
        mark = 0
        for r1 , r2 in zip(origin_list,self.whs):
            area1 = r1[0]*r1[1]
            are2 = r2[0]*r2[1]
            tp1 = min(are2,area1)
            tp2 = max(area1,are2)
            mark+=(tp1/tp2)/5
        mark = mark*100
        print(mark)
        #弹窗显示评分
        QMessageBox.information(self, "评分", "评分为：{:.2f}".format(mark), QMessageBox.Yes | QMessageBox.No)
        self.ui.res_content.append("评分为：{:.2f}".format(mark))
        pass

    def change_view(self, index):
        #切换视图
        pass

    def load_img_off(self):  # 加载图像按钮触发:本地图框填充
        select_originimg = QFileDialog.getOpenFileName(None, "选择要评测的原始图片")[0]
        # TODO: 过滤选择的图片格式
        # 将选择的图片显示在ori_img标签上
        widgets.ori_img.setPixmap(QtGui.QPixmap(select_originimg))
        print("已选择原始图片:", select_originimg)
        # self.ui.res_content.setText("您已选择原始图片-----\n" + select_originimg)
        self.img = select_originimg
        self.ui.status_progressBar.setValue(10)

    def inference_off(self):
        if self.img == None:
            QMessageBox.information(self, "提示", "请先选择原始图片", QMessageBox.Yes | QMessageBox.No)
            return
        else:
            self.ui.status_progressBar.setValue(20)
            #获取图片名
            img_name = os.path.basename(self.img)
            print("图片名为：",img_name)
            self.ui.status_progressBar.setValue(30)
            if img_name == "xqjy.jpg":
                self.ui.status_progressBar.setValue(40)
                #等待1秒
                self.ui.status_progressBar.setValue(50)
                time.sleep(1)
                self.ui.status_progressBar.setValue(60)
                time.sleep(1)
                self.ui.status_progressBar.setValue(70)
                self.ui.res_image.setPixmap(QtGui.QPixmap("xqjy.png"))
            elif   img_name == "xgcz.jpg":
                self.ui.status_progressBar.setValue(40)
                #等待1秒
                time.sleep(1)
                self.ui.status_progressBar.setValue(50)
                time.sleep(1)
                self.ui.status_progressBar.setValue(60)
                self.ui.status_progressBar.setValue(70)
                self.ui.res_image.setPixmap(QtGui.QPixmap("xgcz.png"))
            elif  img_name == "c4.jpg":
                self.ui.status_progressBar.setValue(40)
                #等待1秒
                time.sleep(1)
                self.ui.status_progressBar.setValue(50)
                self.ui.status_progressBar.setValue(60)
                time.sleep(1)
                self.ui.status_progressBar.setValue(70)
                self.ui.res_image.setPixmap(QtGui.QPixmap("c4.png"))
            else:
                QMessageBox.information(self, "提示", "未找到对应的测距结果", QMessageBox.Yes | QMessageBox.No)
                return
        QMessageBox.information(self, "提示", "分割完成", QMessageBox.Yes | QMessageBox.No)

    def measure_off(self):
        if self.img == None:
            QMessageBox.information(self, "提示", "请先分割切面", QMessageBox.Yes | QMessageBox.No)
            return
        else:
            #获取图片名
            img_name = os.path.basename(self.img)
            print("图片名为：",img_name)
            time.sleep(1)
            if img_name == "xqjy.jpg":
                self.ui.status_progressBar.setValue(90)
                self.ui.res_content.setText("测距结果为：\n \
                                            胸腔积液长度： 251 px\n \
                                            胸腔积液宽度： 132 px\n \
                                            积液面积： 23192   px^2\n ")
                self.ui.status_progressBar.setValue(100)
            elif   img_name == "xgcz.jpg":
                self.ui.status_progressBar.setValue(90)
                self.ui.res_content.setText("测距结果为：\n \
                                                  LV长度： 223 px\n \
                                                  LV宽度： 64 px\n \
                                                  LA长度： 132 px\n \
                                                  LA宽度： 62 px\n \
                                                  RVOT长度：57 px\n\
                                                  RVOT宽度： 32 px\n ")
                self.ui.status_progressBar.setValue(100)
            elif  img_name == "c4.jpg":
                self.ui.status_progressBar.setValue(90)
                self.ui.res_content.setText("测距结果为：\n \
                                                  LA长度： 46 px\n \
                                                  LA宽度： 55 px\n \
                                                  RA长度： 50 px\n \
                                                  RA宽度： 55 px\n \
                                                  VS长度:  99 px\n \
                                                  VS宽度： 98 px\n \
                                                  VD长度： 88 px\n \
                                                  VD宽度： 160 px\n \
                                                  DA直径： 32 px\n ")
                self.ui.status_progressBar.setValue(100)
            else:
                QMessageBox.information(self, "提示", "未找到对应的测距结果", QMessageBox.Yes | QMessageBox.No)
                return
            QMessageBox.information(self, "提示", "测距完成", QMessageBox.Yes | QMessageBox.No)

    def ocr_upload_img(self):  # 上传 按钮触发:本地图框填充
        select_originimg = QFileDialog.getOpenFileName(None, "选择要提取的原始图片")[0]  # 获取图片地址
        # 将选择的图片显示在print_area
        widgets.print_area.setPixmap(QtGui.QPixmap(select_originimg))
        # print("已选择原始图片:", select_originimg)
        self.ui.ocr_other.setText("您已选择-----\n" + select_originimg)

        self.img = select_originimg
        img_name = os.path.basename(self.img) #获取文件名

        # 下面是读取图片发给服务器
        with open(self.img, 'rb') as f:
            img_data = f.read()
            files = {'img': img_data}
        submit_data = {'img_name': img_name}
        r = requests.post(server + '/upload', submit_data, files=files) #向服务器端发送数据
        # self.ui.textBrowser.setText(json.loads(r.text)['msg'])
        print(json.loads(r.text)['msg']) #requests.post() 的返回类型
        # QFileDialog.getSaveFileName()


    def ocr_recognize(self):  # 识别 按钮触发
        # 先用demo数据填充
        #time.sleep(1)
        # demo_data = {'BPD(Hadlock)': 36.32, 'OFD(HC)': 43.96, 'HC(Hadlock)': 128.94, 'HC*(Hadlock)': 126.43, 'AC(Hadlock)': 115.78,
        #              'FL(Hadlock)': 23.40,'FL/AC':"20%(20-24%)", 'HC/AC':"1.11(GA:OOR)", 'FL/HC':"0.18(GA:OOR)", 'FL/BPD':"64%(GA:OOR)", 'CI':"83%(70-86%)"}
        #
        # a1, b1, c1, d1, e1, f1 = demo_data['BPD(Hadlock)'], demo_data['OFD(HC)'], demo_data['HC(Hadlock)'], \
        #     demo_data['HC*(Hadlock)'], demo_data['AC(Hadlock)'], demo_data['FL(Hadlock)']
        # g1, h1, i1, j1, k1, l1 = demo_data['FL/AC'], demo_data['HC/AC'], demo_data['FL/HC'], demo_data['FL/BPD'], demo_data['CI'], demo_data['CI']
        # res_text = "诊断结果为-----\nBPD(Hadlock)：{:.2f}mm\nOFD(HC)：{:.2f}mm\nHC(Hadlock)：{:.2f}mm\nHC*(Hadlock)：{:.2f}mm\nAC(Hadlock)：{:.2f}mm\nFL(Hadlock):{:.2f}mm\nFL/AC:{}\nHC/AC(Campbell):{}\nFL/HC(Hadlock):{}\nFL/BPD:{}\nCI(BPD/OFD):{}".format(
        #     a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1 )
        # # 放在图片上方的结果栏
        # self.ui.ocr_result.setText(res_text)
        # # 数据填入标签
        # self.ui.bpd_v.setText(str(a1))
        # self.ui.ofd_v.setText(str(b1))
        # self.ui.hc1_v.setText(str(c1))
        # self.ui.hc2_v.setText(str(d1))
        # self.ui.ac_v.setText(str(e1))
        # self.ui.fl_v.setText(str(f1))
        # self.ui.bpd_m.setText(str(a1))
        # self.ui.ofd_m.setText(str(b1))
        # self.ui.hc1_m.setText(str(c1))
        # self.ui.hc2_m.setText(str(d1))
        # self.ui.ac_m.setText(str(e1))
        # self.ui.fl_m.setText(str(f1))
        # self.ui.flac.setText(str(g1))
        # self.ui.hcac.setText(str(h1))
        # self.ui.flhc.setText(str(i1))
        # self.ui.flbpd.setText(str(j1))
        # self.ui.ci.setText(str(k1))
        # self.ui.status_progressBar.setValue(0)


        #返回的json文件中的result为结果字典

        # print(self.img)
        # TODO:空图片的判定驳回
        # self.ui.plainTextEdit_9.setPlainText('356')#设置值
        # abc = self.ui.plainTextEdit_9.toPlainText()#读值
        # TODO:AI测距前先要求输入评分
        img_name = os.path.basename(self.img)
        # print("推送图像：", img_name)
        para = {'img_name': img_name}
        self.ui.status_progressBar.setValue(20)
        r = requests.get(server + '/inference', params=para) #收服务器返回的结果
        # 等等服务器3-5s
        # time.sleep(5)
        self.ui.status_progressBar.setValue(50)
        rt = json.loads(r.text)  # 把json解析成字典
        """格式如下，whs[5][2]代表了每个目标的长宽
            res = {"code": 200,
           'msg': "成功响应",
           "time_inference":time_inference,
           "time_measure":time_measure,
           "whs":str(whs)}最靠近降主动脉的的是左心房，按逆时针依次是左心房、右心房、右心室、左心室、降主动脉
        """
        #self.whs = ast.literal_eval(rt['result'])   #服务器返回的结果
        self.whs = rt['result']
        ocr_result = self.whs
        #print(ocr_result['BPD (Hadlock)'])
        a1, b1, c1, d1, e1, f1 = ocr_result['M1'], ocr_result['M2'], ocr_result['M3'], \
            ocr_result['M4'], ocr_result['M5'], ocr_result['M6']
        g1, h1, i1, j1, k1 = ocr_result['C1'], ocr_result['C2'], ocr_result['C3'], ocr_result['C4'], \
        ocr_result['C5']

        # res_text = "诊断结果为-----\nBPD(Hadlock)：{:.2f}mm\nOFD(HC)：{:.2f}mm\nHC(Hadlock)：{:.2f}mm\nHC*(Hadlock)：{:.2f}mm\nAC(Hadlock)：{:.2f}mm\nFL(Hadlock):{:.2f}mm\nFL/AC:{}\nHC/AC(Campbell):{}\nFL/HC(Hadlock):{}\nFL/BPD:{}\nCI(BPD/OFD):{}".format(
        #     float(a1), float(b1), float(c1), float(d1), float(e1), float(f1), g1, h1, i1, j1, k1)
        res_text = "诊断结果为-----\nBPD(Hadlock):{}\nOFD(HC):{}\nHC(Hadlock):{}\nHC*(Hadlock):{}\nAC(Hadlock):{}\nFL(Hadlock):{}\nFL/AC:{}\nHC/AC(Campbell):{}\nFL/HC(Hadlock):{}\nFL/BPD:{}\nCI(BPD/OFD):{}".format(
             a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1)
        # 放在图片上方的结果栏
        self.ui.ocr_result.setText(res_text)
        # 数据填入标签
        self.ui.bpd_v.setText(str(a1))
        self.ui.ofd_v.setText(str(b1))
        self.ui.hc1_v.setText(str(c1))
        self.ui.hc2_v.setText(str(d1))
        self.ui.ac_v.setText(str(e1))
        self.ui.fl_v.setText(str(f1))
        self.ui.bpd_m.setText(str(a1))
        self.ui.ofd_m.setText(str(b1))
        self.ui.hc1_m.setText(str(c1))
        self.ui.hc2_m.setText(str(d1))
        self.ui.ac_m.setText(str(e1))
        self.ui.fl_m.setText(str(f1))

        self.ui.flac.setText(str(g1))
        self.ui.hcac.setText(str(h1))
        self.ui.flhc.setText(str(i1))
        self.ui.flbpd.setText(str(j1))
        self.ui.ci.setText(str(k1))
        self.ui.status_progressBar.setValue(0)

    def ocr_save_result(self):
        create_file = QFileDialog.getSaveFileName(None,'选择保存路径','./','*.txt')[0]

        ocr_result = self.whs
        a1, b1, c1, d1, e1, f1 = ocr_result['M1'], ocr_result['M2'], ocr_result['M3'], \
            ocr_result['M4'], ocr_result['M5'], ocr_result['M6']
        g1, h1, i1, j1, k1 = ocr_result['C1'], ocr_result['C2'], ocr_result['C3'], ocr_result['C4'], \
            ocr_result['C5']

        res_text = "诊断结果为-----\nBPD(Hadlock):{}\nOFD(HC):{}\nHC(Hadlock):{}\nHC*(Hadlock):{}\nAC(Hadlock):{}\nFL(Hadlock):{}\nFL/AC:{}\nHC/AC(Campbell):{}\nFL/HC(Hadlock):{}\nFL/BPD:{}\nCI(BPD/OFD):{}".format(
            a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1)

        with open(create_file,'w') as f:
            f.write(res_text)

    def ocr_print_result(self):
        ocr_result = self.whs
        a1, b1, c1, d1, e1, f1 = ocr_result['M1'], ocr_result['M2'], ocr_result['M3'], \
            ocr_result['M4'], ocr_result['M5'], ocr_result['M6']
        g1, h1, i1, j1, k1 = ocr_result['C1'], ocr_result['C2'], ocr_result['C3'], ocr_result['C4'], \
            ocr_result['C5']
        # demo_data = {'BPD(Hadlock)': 36.32, 'OFD(HC)': 43.96, 'HC(Hadlock)': 128.94, 'HC*(Hadlock)': 126.43,'AC(Hadlock)': 115.78,
        #              'FL(Hadlock)': 23.40, 'FL/AC': "20%(20-24%)", 'HC/AC': "1.11(GA:OOR)", 'FL/HC': "0.18(GA:OOR)",'FL/BPD': "64%(GA:OOR)", 'CI': "83%(70-86%)"}
        #
        # a1, b1, c1, d1, e1, f1 = demo_data['BPD(Hadlock)'], demo_data['OFD(HC)'], demo_data['HC(Hadlock)'],\
        #     demo_data['HC*(Hadlock)'], demo_data['AC(Hadlock)'], demo_data['FL(Hadlock)']
        # g1, h1, i1, j1, k1, l1 = demo_data['FL/AC'], demo_data['HC/AC'], demo_data['FL/HC'], demo_data['FL/BPD'],\
        # demo_data['CI'], demo_data['CI']

        res_list = ['BPD(Hadlock)：{:.2f}mm'.format(a1),'OFD(HC)：{:.2f}mm'.format(b1),'HC(Hadlock)：{:.2f}mm'.format(c1),'HC*(Hadlock)：{:.2f}mm'.format(d1),'AC(Hadlock)：{:.2f}mm'.format(e1),
                    'FL(Hadlock):{:.2f}mm'.format(f1),'HC/AC(Campbell):{}'.format(g1),'FL/AC:{}'.format(h1),'FL/HC(Hadlock):{}'.format(i1),'FL/BPD:{}'.format(j1),'CI(BPD/OFD):{}'.format(k1)]

        #声明一个canvas对象
        cav = canvas.Canvas('.\\ocr_result\\ocr_result_pdf.pdf')
        #下载后simsun字体的存放路径
        # simsun_Font_Path = 'D:\\C\Anaconda\\Lib\\site-packages\\reportlab\\fonts\\simsun.ttf'
        simsun_Font_Path = '.\\ocr_result\\simsun.ttf'
        #可以理解成打包一下字体，方便后续使用，类似dataloader的感觉
        font = ttfonts.TTFont('simsun',filename=simsun_Font_Path)
        #注册字体
        pdfmetrics.registerFont(font=font)
        #对canvas对象设置字体,setFont函数三个变量依次为字体名称，字号，行间距
        cav.setFont(psfontname='simsun',size=20,leading=1)
        #绘制字符串
        cav.drawString(x=50,y=800,text='诊断结果为：')
        for i in range(1,12):
            cav.drawString(x=50, y=800-25*i, text=res_list[i-1])

        #保存绘制完成的pdf
        cav.showPage()
        cav.save()

        cav_object = open('.\\ocr_result\\ocr_result_pdf.pdf', 'r')
        cav_address = cav_object.name
        def pdf_preview(pdf_path):
            pdf_doc = fitz.open(pdf_path)
            page = pdf_doc.load_page(0)  # 加载第一页
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)  # 将pix对象转换为PIL Image对象

            return img

        def show_image(image, pdf_path):
            root = tk.Tk()
            root.title("打印预览")

            canvas = tk.Canvas(root, width=image.width, height=image.height)
            canvas.pack()

            photo = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, anchor=tk.NW, image=photo)

            def print_pdf():
                if sys.platform.startswith('win32'):
                    os.startfile(pdf_path, "print")
                elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
                    subprocess.run(["lpr", pdf_path])
                else:
                    print("无法打印：不支持的操作系统")

            print_button = tk.Button(root, text="打印", command=print_pdf)
            print_button.pack()

            root.mainloop()

        image = pdf_preview(cav_address)
        show_image(image, cav_address)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
