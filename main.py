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
import requests
import json
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from PySide6 import QtGui

from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
server = 'http://127.0.0.1:5000'
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
        title = "全栈式超声影像诊断系统"
        description = "超声影像诊断系统"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        self.ui.res_content.clear()
        self.ui.res_content_2.clear()
        self.ui.creditsLabel.clear()

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
        # widgets.pushButton_6.clicked.connect(self.fill_demo_heart)
        # widgets.pushButton_5.clicked.connect(self.fill_demo_xqjy)
        # widgets.pushButton_7.clicked.connect(self.fill_demo_xgcz)
        widgets.Button_load.clicked.connect(self.load_img)
        widgets.Button_meas.clicked.connect(self.ai_inference)
        widgets.Button_recognize.clicked.connect(self.evaluate)
        widgets.comboBox_choosemodel.currentIndexChanged.connect(self.change_view(self.ui.comboBox_choosemodel.currentText()))

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
        print(json.loads(r.text)['msg'])  #判断服务器是否收到图片

        #加载原始评分数据，先用demo数据填充
        demo_data = [(95, 100), (85, 151), (142, 194), (145, 206), (33, 45)]
        self.impdata = demo_data
        a1, a2, b1, b2, c1, c2, d1, d2, e1, e2 = self.impdata[0][0], self.impdata[0][1], self.impdata[1][0], self.impdata[1][1], \
            self.impdata[2][0], self.impdata[2][1], self.impdata[3][0], self.impdata[3][1], self.impdata[4][0], self.impdata[4][1]
        res_text = "您导入的测距结果为-----\n左心房长宽：{:.2f}*{:.2f}mm\n右心房长宽：{:.2f}*{:.2f}mm\n右心室长宽：{:.2f}*{:.2f}mm\n左心室长宽：{:.2f}*{:.2f}mm\n降主动脉长宽：{:.2f}*{:.2f}mm\n".format(
            a1, a2, b1, b2, c1, c2, d1, d2, e1, e2)
        self.ui.res_content.append(res_text)


    def ai_inference(self):#AI测距按钮触发
        self.ui.status_progressBar.setValue(0)   #设置进度条的值
        # print(self.img)
        #TODO:空图片的判定驳回
        # self.ui.plainTextEdit_9.setPlainText('356')#设置值
        # abc = self.ui.plainTextEdit_9.toPlainText()#读值
        #TODO:AI测距前先要求输入评分
        img_name = os.path.basename(self.img)
        print("推送图像：",img_name)
        para = {'img_name':img_name}
        self.ui.status_progressBar.setValue(20)
        r = requests.get(server+'/inference', params=para)
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
        self.whs = ast.literal_eval(rt['whs'])  #变回最初的列表形式
        # self.whs = rt['whs']
        print(self.whs,type(self.whs))
        # self.ui.res_content.setText(str(rt))
        self.ui.status_progressBar.setValue(60)
        # https://www.cnblogs.com/yuanyongqiang/p/12609860.html 对stream参数的介绍
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
        self.ui.res_image.setPixmap(QtGui.QPixmap(result_path))  #显示分割后的图片
        self.ui.status_progressBar.setValue(80)

        demo_data = [(95, 100), (85, 151), (142, 194), (145, 206), (33, 45)]
        self.impdata = demo_data
        a1, a2, b1, b2, c1, c2, d1, d2, e1, e2 = self.impdata[0][0], self.impdata[0][1], self.impdata[1][0], \
        self.impdata[1][1], \
            self.impdata[2][0], self.impdata[2][1], self.impdata[3][0], self.impdata[3][1], self.impdata[4][0], \
        self.impdata[4][1]
        res_text = "您导入的测距结果为-----\n左心房长宽：{:.2f}*{:.2f}mm\n右心房长宽：{:.2f}*{:.2f}mm\n右心室长宽：{:.2f}*{:.2f}mm\n左心室长宽：{:.2f}*{:.2f}mm\n降主动脉长宽：{:.2f}*{:.2f}mm\n".format(
            a1, a2, b1, b2, c1, c2, d1, d2, e1, e2)
        self.ui.res_content.append(res_text)

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
        # origin_list = self.impdata
        # mark = 0
        # for r1 , r2 in zip(origin_list,self.whs):
        #     area1 = r1[0]*r1[1]
        #     are2 = r2[0]*r2[1]
        #     tp1 = min(are2,area1)
        #     tp2 = max(area1,are2)
        #     mark+=(tp1/tp2)/5
        # mark = mark*100
        # print(mark)
        # #弹窗显示评分
        # QMessageBox.information(self, "评分", "评分为：{:.2f}".format(mark), QMessageBox.Yes | QMessageBox.No)
        # self.ui.res_content.append("评分为：{:.2f}".format(mark))
        # pass

        widgets.res_content_2.setText("模型识别到的部位有：\n左心房\n右心房\n左心室\n右心室\n降主动脉\n与标准切面匹配程度为100%")
        img_name = os.path.basename(self.img)
        para = {'img_name': img_name}
        url_file = server + '/download_inference_nomerge'
        File = requests.get(url_file, stream=True, params=para)
        if (os.path.exists('outcome_s')):
            pass
        else:
            os.makedirs('outcome_s')
        result_path = os.path.join('outcome_s',img_name)
        with open(result_path, 'wb+') as f:
            # 分块写入文件
            for chunk in File.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        f.close()
        self.ui.res_image_2.setPixmap(QtGui.QPixmap(result_path))

    def change_view(self, index):
        #切换视图
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
