# -*- coding: utf-8 -*-
import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from FlowChartNode import *
from FlowChartArea import *
import multitasking
from images import A0_Demo_rc, B1_Demo_rc, C2_Demo_rc, D3_Demo_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1440, 835)
        self.gridLayoutWidget = QWidget()
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 1440, 860))
        
        self.sw_main = QStackedWidget(Form)
        self.sw_main.setObjectName(u"sw_main")
        self.sw_main.setGeometry(QRect(0, 0, 1440, 860))
        # 用于切换客户端各个预设布局的stackwidget（布局层次仅次于Form，排第二）
        
        self.page_main_A = QWidget()
        self.page_main_A.setObjectName(u"page_main_A")
        # userA布局对应的的page
        
        self.page_main_A = QWidget()
        self.page_main_A.setObjectName(u"page_main_A")
        self.sw_main.addWidget(self.page_main_A)
        # userA的布局
        
        self.page_main_B = QWidget()
        self.page_main_B.setObjectName(u"page_main_B")
        self.sw_main.addWidget(self.page_main_B)
        # userB布局对应的page
        
        ###########################################################################(BBBBBBBBBBBBBBBBBBBBBBBBBBBB)#####################################################
        self.gridLayout_B = QGridLayout(self.page_main_B)
        self.gridLayout_B.setObjectName(u"gridLayout_B")
        self.gridLayout_B.setContentsMargins(0, 0, 0, 0)  # 0, 0, 1440, 860
        # 父类为page_main_B，是包裹整个B_ui界面的主体布局
        
        self.widget_B = QWidget(self.gridLayoutWidget)
        self.widget_B.setObjectName(u"widget_B")
        # 父类为gridLayout_B，包裹整个B_ui界面，用于各控件能够自由的放置位置
        
        self.lb_background_B = QLabel(self.widget_B)
        self.lb_background_B.setObjectName(u"lb_background_B")
        self.lb_background_B.setGeometry(QRect(0, 0, 1440, 900))
        self.lb_background_B.setPixmap(QPixmap(u":/old/B1(create)/lb_background_B.jpg"))
        
        self.lb_above_background_B = QLabel(self.widget_B)
        self.lb_above_background_B.setObjectName(u"lb_above_background_B")
        self.lb_above_background_B.setGeometry(QRect(-7, 1, 401, 111))  # 0, 0, 1440, 860
        self.lb_above_background_B.setStyleSheet(u"\n"
                                                 "background-color: rgb(0, 10, 13);")
        self.lb_above_background_B.raise_()
        # self.lb_above_background_B.setScaledContents(True)
        '预留功能切换背景图片'  # 父类为widget_B背景版，左上布局背景
        
        self.gridLayoutWidget_2 = QWidget(self.widget_B)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 391, 111))  #
        
        self.gridLayout_above_B = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_above_B.setObjectName(u"gridLayout_above_B")
        self.gridLayout_above_B.setContentsMargins(0, 0, 0, 0)  #
        
        self.widget_above_B = QWidget(self.gridLayoutWidget_2)
        self.widget_above_B.setObjectName(u"widget_above_B")
        # 包裹左上角的小部件的布局
        
        self.pb_above_exit_B = QPushButton(self.widget_above_B)
        self.pb_above_exit_B.setObjectName(u"pb_exit_B")
        self.pb_above_exit_B.setGeometry(QRect(270, 10, 101, 41))
        self.pb_above_exit_B.setStyleSheet(u"background-color: rgb(54, 0, 129);\n"
                                           "font: 75 18pt \"Constantia\";\n"
                                           "color: rgb(255, 255, 255);")
        self.pb_above_exit_B.setIconSize(QSize(101, 41))
        self.pb_above_exit_B.raise_()
        # 左上角布局中的小控件，用于退出create界面
        
        # icon = QIcon()
        # icon.addFile(u"../image/B1/above/pb_exit_B.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.pb_above_exit_B.setIcon(icon)
        # self.pb_above_exit_B.setIconSize(QSize(169, 40))
        # pb_exit_B的图片素材
        
        self.lcd_above_time_B = QLCDNumber(self.widget_above_B)
        self.lcd_above_time_B.setObjectName(u"lcd_time_B")
        self.lcd_above_time_B.setEnabled(True)
        self.lcd_above_time_B.setGeometry(QRect(180, 50, 81, 41))
        self.lcd_above_time_B.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcd_above_time_B.raise_()
        # 数字晶体显示器，用于展示user的工作时间
        
        self.lb_above_mode_B = QLabel(self.widget_above_B)
        self.lb_above_mode_B.setObjectName(u"lb_above_mode_B")
        self.lb_above_mode_B.setGeometry(QRect(10, 10, 161, 31))
        self.lb_above_mode_B.setStyleSheet(u"background-color: rgb(23, 22, 27);\n"
                                           "font: 75 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "")
        self.lb_above_mode_B.raise_()
        # 当前创作模式的label
        
        self.cb_above_mode_B = QComboBox(self.widget_above_B)
        self.cb_above_mode_B.setObjectName(u"cb_mode_B")
        self.cb_above_mode_B.setGeometry(QRect(180, 20, 81, 22))
        self.cb_above_mode_B.raise_()
        # 当前创作模式的下拉框
        
        self.lb_above_timeRemind_B = QLabel(self.widget_above_B)
        self.lb_above_timeRemind_B.setObjectName(u"lb_above_timeRemind_B")
        self.lb_above_timeRemind_B.setGeometry(QRect(10, 52, 161, 41))
        self.lb_above_timeRemind_B.setStyleSheet(u"background-color: rgb(23, 22, 27);\n"
                                                 "font: 75 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
                                                 "color: rgb(255, 255, 255);\n"
                                                 "")
        self.lb_above_timeRemind_B.raise_()
        # 已工作时间的label
        
        self.gridLayout_above_B.addWidget(self.widget_above_B, 1, 0, 1, 1)
        
        "注：有两种创作模式："
        "1.流程图模式：show布局中会显示可编辑的流程图，attribute布局会显示流程图节点的具体信息"
        "2.布局开发模式：show布局中会显示布局的预览（不可互动），attribute布局会显示各个控件的具体信息，目前可以改变图片素材"
        
        self.gridLayoutWidget_3 = QWidget(self.widget_B)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 720, 1441, 151))  # 0, 100, 891, 631
        
        self.gridLayout_show_B = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_show_B.setObjectName(u"gridLayout_show_B")
        self.gridLayout_show_B.setContentsMargins(0, 0, 0, 0)
        # 左边中间的布局，用于展示流程图和创作布局预览
        
        self.sw_show_B = QStackedWidget(self.gridLayoutWidget_3)
        self.sw_show_B.setObjectName(u"sw_show_B")
        # 用于切换两种模式时，布局中的内容
        
        self.page_show1_B = QWidget()
        self.page_show1_B.setObjectName(u"page_show1_B")
        # 用于展示预设布局
        
        "命名内涵："
        "page:例子page_showWidgetA_B，show代表这是show布局内的内容，Widget代表其类型是widget，A代表其预设布局的编号，_B是引擎UI的布局编号"
        "控件：例子pb_showRestA_B，pb代表其类型为pushbutton，show代表其是show布局的内容，Rest代表其功能描述（描述的每个单词开头大写）,_B是引擎UI的布局编号"
        "waring！！！切勿将预设布局和UI布局弄混"
        '*预设布局指游戏创作的预先设置好的创作模板的各个UI文件内容，UI布局指的是引擎的UI部分的各个UI文件内容'
        
        # 每个大写字母代表一个stack内嵌套的每张卡片的小布局的编号
        # 界面码：
        #       zero-A(main_game)----游戏的初始界面
        #       one-B(talk_left)----人物在左边的情况
        #       two-C(talk_right)----人物在右边的情况
        #       three-D(change_one)----选择界面，有一个选项
        #       four-E(change_two)----选择界面，有两个选项
        #       five-F(change_three)----选择界面，有三个选项
        #       six-G(talk_story)----动画或旁白进程，没有人物
        #       seven-H(game_end)----游戏结束（未完待续），开发者致谢表
        # waring:1.*_talk_left_*等命名是因为第一代时的命名问题，没有特殊含义
        #       2.__（双下划杠）只是编写是的疏漏，没有特殊含义
        ################本编号同样适用于UI文件和game类和Xmind##############
        
        #####################################################Probject##############################################
        #####################################################Probject##############################################
        #####################################################Probject##############################################
        
        self.sw_showProbject_B = QStackedWidget(self.page_show1_B)
        self.sw_showProbject_B.setObjectName(u"sw_showProbject_B")
        self.sw_showProbject_B.setGeometry(QRect(0, 0, 891, 631))
        # 父类是self.page_show1_B，属于page_show1_B，用于切换各个预设界面的预览
        
        '·······································page_show1_B········································'
        '·······································page_show1_B········································'
        '·······································page_show1_B········································'
        ##########################################page_showWidgetA_B##################################
        ##########################################page_showWidgetA_B##################################
        ##########################################page_showWidgetA_B##################################
        
        self.page_showWidgetA_B = QWidget()
        self.page_showWidgetA_B.setObjectName(u"page_showWidgetA_B")
        # A布局预览
        
        self.lb_showBackgroundA_B = QLabel(self.page_showWidgetA_B)
        self.lb_showBackgroundA_B.setObjectName(u"lb_showBackgroundA_B")
        self.lb_showBackgroundA_B.setGeometry(QRect(3, 1, 881, 621))
        # A布局内的背景
        
        self.lb_showTitleA_B = QLabel(self.page_showWidgetA_B)
        self.lb_showTitleA_B.setObjectName(u"lb_showTitleA_B")
        self.lb_showTitleA_B.setGeometry(QRect(440, 40, 391, 111))
        # A布局内的游戏标题
        
        self.pb_showStartA_B = QPushButton(self.page_showWidgetA_B)
        self.pb_showStartA_B.setObjectName(u"pb_showStartA_B")
        self.pb_showStartA_B.setGeometry(QRect(560, 170, 201, 91))
        # A布局内的开始按钮
        
        self.pb_showStoryA_B = QPushButton(self.page_showWidgetA_B)
        self.pb_showStoryA_B.setObjectName(u"pb_showStoryA_B")
        self.pb_showStoryA_B.setGeometry(QRect(560, 270, 201, 91))
        # A布局内的故事成就按钮
        
        self.pb_showRestA_B = QPushButton(self.page_showWidgetA_B)
        self.pb_showRestA_B.setObjectName(u"pb_showRestA_B")
        self.pb_showRestA_B.setGeometry(QRect(560, 370, 201, 91))
        # A布局内的退出按钮
        
        self.pb_showSetA_B = QPushButton(self.page_showWidgetA_B)
        self.pb_showSetA_B.setObjectName(u"pb_showSetA_B")
        self.pb_showSetA_B.setGeometry(QRect(560, 470, 201, 91))
        # A布局内的设置按钮
        
        self.lb_showHumanLeftA_B = QLabel(self.page_showWidgetA_B)
        self.lb_showHumanLeftA_B.setObjectName(u"lb_showHumanLeftA_B")
        self.lb_showHumanLeftA_B.setGeometry(QRect(30, 100, 301, 501))
        # A布局内的人物（在左边）
        
        self.sw_showProbject_B.addWidget(self.page_showWidgetA_B)
        
        ##########################################page_showWidgetB_B##################################
        ##########################################page_showWidgetB_B##################################
        ##########################################page_showWidgetB_B##################################
        
        self.page_showWidgetB_B = QWidget()
        self.page_showWidgetB_B.setObjectName(u"page_showWidgetB_B")
        # B布局预览
        
        self.pb_showNextB_B = QPushButton(self.page_showWidgetB_B)
        self.pb_showNextB_B.setObjectName(u"pb_nextB_B")
        self.pb_showNextB_B.setGeometry(QRect(750, 560, 75, 23))
        # B布局内的切换下一个节点（布局）
        
        self.lb_showBackgroundB_B = QLabel(self.page_showWidgetB_B)
        self.lb_showBackgroundB_B.setObjectName(u"lb_showBackgroundB_B")
        self.lb_showBackgroundB_B.setGeometry(QRect(3, 1, 881, 621))
        # B布局内的背景
        
        self.lb_showHuamnLeftB_B = QLabel(self.page_showWidgetB_B)
        self.lb_showHuamnLeftB_B.setObjectName(u"lb_showHuamnLeftB_B")
        self.lb_showHuamnLeftB_B.setGeometry(QRect(13, 111, 261, 501))
        # B布局内的人物（在左边）
        
        self.lb_showTellB_B = QLabel(self.page_showWidgetB_B)
        self.lb_showTellB_B.setObjectName(u"lb_showTellB_B")
        self.lb_showTellB_B.setGeometry(QRect(313, 381, 531, 211))
        # B布局内的对话框
        
        self.lb_showNameB_B = QLabel(self.page_showWidgetB_B)
        self.lb_showNameB_B.setObjectName(u"lb_showNameB_B")
        self.lb_showNameB_B.setGeometry(QRect(310, 310, 181, 51))
        # B布局内的名称框
        
        self.sw_showProbject_B.addWidget(self.page_showWidgetB_B)
        
        self.lb_showTellB_B.raise_()
        self.lb_showBackgroundB_B.raise_()
        self.pb_showNextB_B.raise_()
        self.lb_showHuamnLeftB_B.raise_()
        self.lb_showNameB_B.raise_()
        
        ##########################################page_showWidgetC_B##################################
        ##########################################page_showWidgetC_B##################################
        ##########################################page_showWidgetC_B##################################
        
        self.page_showWidgetC_B = QWidget()
        self.page_showWidgetC_B.setObjectName(u"page_showWidgetC_B")
        # C布局预览
        
        self.pb_showNextC_B = QPushButton(self.page_showWidgetC_B)
        self.pb_showNextC_B.setObjectName(u"pb_showNextC_B")
        self.pb_showNextC_B.setGeometry(QRect(460, 550, 75, 23))
        # C布局内的切换下一个节点（布局）
        
        self.lb_showBackgroundC_B = QLabel(self.page_showWidgetC_B)
        self.lb_showBackgroundC_B.setObjectName(u"lb_showBackgroundC_B")
        self.lb_showBackgroundC_B.setGeometry(QRect(3, 1, 881, 621))
        # C布局内的背景
        
        self.lb_showTellC_B = QLabel(self.page_showWidgetC_B)
        self.lb_showTellC_B.setObjectName(u"lb_showTellC_B")
        self.lb_showTellC_B.setGeometry(QRect(10, 410, 541, 191))
        # C布局内的对话框
        
        self.lb_showNameC_B = QLabel(self.page_showWidgetC_B)
        self.lb_showNameC_B.setObjectName(u"lb_showNameC_B")
        self.lb_showNameC_B.setGeometry(QRect(10, 330, 171, 51))
        # C布局内的名称框
        
        self.lb_showHumanRightC_B = QLabel(self.page_showWidgetC_B)
        self.lb_showHumanRightC_B.setObjectName(u"lb_showHumanRightC_B")
        self.lb_showHumanRightC_B.setGeometry(QRect(583, 71, 301, 551))
        # C布局内的人物（在右边）
        
        self.sw_showProbject_B.addWidget(self.page_showWidgetC_B)
        
        self.lb_showBackgroundC_B.raise_()
        self.lb_showTellC_B.raise_()
        self.pb_showNextC_B.raise_()
        self.lb_showNameC_B.raise_()
        self.lb_showHumanRightC_B.raise_()
        ##########################################page_showWidgetD_B##################################
        ##########################################page_showWidgetD_B##################################
        ##########################################page_showWidgetD_B##################################
        self.page_showWidgetD_B = QWidget()
        self.page_showWidgetD_B.setObjectName(u"page_showWidgetD_B")
        # D布局预览
        
        self.lb_showBackgroundD_B = QLabel(self.page_showWidgetD_B)
        self.lb_showBackgroundD_B.setObjectName(u"lb_showBackgroundD_B")
        self.lb_showBackgroundD_B.setGeometry(QRect(3, 1, 881, 621))
        # D布局内的背景
        
        self.lb_showHumanLeftD_B = QLabel(self.page_showWidgetD_B)
        self.lb_showHumanLeftD_B.setObjectName(u"lb_showHumanLeftD_B")
        self.lb_showHumanLeftD_B.setGeometry(QRect(3, 101, 321, 521))
        # D布局内的人物（在左边）
        
        self.lb_showTellD_B = QLabel(self.page_showWidgetD_B)
        self.lb_showTellD_B.setObjectName(u"lb_showTellD_B")
        self.lb_showTellD_B.setGeometry(QRect(343, 381, 531, 231))
        # D布局内的对话框
        
        self.lb_showNameD_B = QLabel(self.page_showWidgetD_B)
        self.lb_showNameD_B.setObjectName(u"lb_showNameD_B")
        self.lb_showNameD_B.setGeometry(QRect(340, 320, 181, 51))
        # D布局内的名称框
        
        self.lb_showChangeD_B = QLabel(self.page_showWidgetD_B)
        self.lb_showChangeD_B.setObjectName(u"lb_showChangeD_B")
        self.lb_showChangeD_B.setGeometry(QRect(553, 190, 71, 20))
        # D布局内的“选择”二字
        
        self.pb_showChangeAD_B = QPushButton(self.page_showWidgetD_B)
        self.pb_showChangeAD_B.setObjectName(u"pb_showChangeAD_B")
        self.pb_showChangeAD_B.setGeometry(QRect(640, 220, 75, 23))
        # D布局内的A选项
        
        self.sw_showProbject_B.addWidget(self.page_showWidgetD_B)
        
        ##########################################page_showWidgetB_B##################################
        ##########################################page_showWidgetB_B##################################
        ##########################################page_showWidgetB_B##################################
        
        self.page_showWidgetE_B = QWidget()
        self.page_showWidgetE_B.setObjectName(u"page_showWidgetE_B")
        # E布局预览
        
        self.pb_showChangeAE_B = QPushButton(self.page_showWidgetE_B)
        self.pb_showChangeAE_B.setObjectName(u"pb_showChangeAE_B")
        self.pb_showChangeAE_B.setGeometry(QRect(640, 220, 75, 23))
        # E布局内的A选项
        
        self.lb_showTellE_B = QLabel(self.page_showWidgetE_B)
        self.lb_showTellE_B.setObjectName(u"lb_showTellE_B")
        self.lb_showTellE_B.setGeometry(QRect(343, 381, 531, 231))
        # E布局内的对话框
        
        self.lb_showChangeE_B = QLabel(self.page_showWidgetE_B)
        self.lb_showChangeE_B.setObjectName(u"lb_showChangeE_B")
        self.lb_showChangeE_B.setGeometry(QRect(553, 190, 71, 20))
        # E布局内的“选择”二字
        
        self.lb_showBackgroundE_B = QLabel(self.page_showWidgetE_B)
        self.lb_showBackgroundE_B.setObjectName(u"lb_showBackgroundE_B")
        self.lb_showBackgroundE_B.setGeometry(QRect(3, 1, 881, 621))
        # E布局内的背景
        
        self.lb_showNameE_B = QLabel(self.page_showWidgetE_B)
        self.lb_showNameE_B.setObjectName(u"lb_showNameE_B")
        self.lb_showNameE_B.setGeometry(QRect(340, 320, 181, 51))
        # E布局内的名称框
        
        self.lb_showHumanLeftE_B = QLabel(self.page_showWidgetE_B)
        self.lb_showHumanLeftE_B.setObjectName(u"lb_showHumanLeftE_B")
        self.lb_showHumanLeftE_B.setGeometry(QRect(3, 101, 321, 521))
        # E布局内的人物（在左边）
        
        self.pb_showChangeBE_B = QPushButton(self.page_showWidgetE_B)
        self.pb_showChangeBE_B.setObjectName(u"pb_showChangeBE_B")
        self.pb_showChangeBE_B.setGeometry(QRect(640, 250, 75, 23))
        # E布局内的B选项
        
        self.sw_showProbject_B.addWidget(self.page_showWidgetE_B)
        
        ##########################################page_showWidgetF_B##################################
        ##########################################page_showWidgetF_B##################################
        ##########################################page_showWidgetF_B##################################
        
        self.page_showWidgetF_B = QWidget()
        self.page_showWidgetF_B.setObjectName(u"page_showWidgetF_B")
        # F布局预览
        
        self.lb_showTellF_B = QLabel(self.page_showWidgetF_B)
        self.lb_showTellF_B.setObjectName(u"lb_showTellF_B")
        self.lb_showTellF_B.setGeometry(QRect(340, 380, 531, 231))
        # F布局内的对话框
        
        self.pb_showChangeBF_B = QPushButton(self.page_showWidgetF_B)
        self.pb_showChangeBF_B.setObjectName(u"pb_showChangeBF_B")
        self.pb_showChangeBF_B.setGeometry(QRect(637, 249, 75, 23))
        # F布局内的B选项
        
        self.lb_showChangeF_B = QLabel(self.page_showWidgetF_B)
        self.lb_showChangeF_B.setObjectName(u"lb_showChangeF_B")
        self.lb_showChangeF_B.setGeometry(QRect(550, 189, 71, 20))
        # F布局内的“选择”二字
        
        self.lb_showBackgroundF_B = QLabel(self.page_showWidgetF_B)
        self.lb_showBackgroundF_B.setObjectName(u"lb_showBackgroundF_B")
        self.lb_showBackgroundF_B.setGeometry(QRect(0, 0, 881, 621))
        # F布局内的背景
        
        self.lb_showNameF_B = QLabel(self.page_showWidgetF_B)
        self.lb_showNameF_B.setObjectName(u"lb_showNameF_B")
        self.lb_showNameF_B.setGeometry(QRect(337, 319, 181, 51))
        # F布局内的名称框
        
        self.pb_showChangeAF_B = QPushButton(self.page_showWidgetF_B)
        self.pb_showChangeAF_B.setObjectName(u"pb_showChangeAF_B")
        self.pb_showChangeAF_B.setGeometry(QRect(637, 219, 75, 23))
        # F布局内的A选项
        
        self.lb_showHumanLeftF_B = QLabel(self.page_showWidgetF_B)
        self.lb_showHumanLeftF_B.setObjectName(u"lb_showHumanLeftF_B")
        self.lb_showHumanLeftF_B.setGeometry(QRect(0, 100, 321, 521))
        # F布局内的人物（在左边）
        
        self.pb_showChangeCF_B = QPushButton(self.page_showWidgetF_B)
        self.pb_showChangeCF_B.setObjectName(u"pb_showChangeCF_B")
        self.pb_showChangeCF_B.setGeometry(QRect(637, 280, 75, 23))
        # F布局内的C选项
        
        self.sw_showProbject_B.addWidget(self.page_showWidgetF_B)
        
        self.lb_showBackgroundF_B.raise_()
        self.lb_showTellF_B.raise_()
        self.pb_showChangeBF_B.raise_()
        self.lb_showChangeF_B.raise_()
        self.lb_showNameF_B.raise_()
        self.pb_showChangeAF_B.raise_()
        self.lb_showHumanLeftF_B.raise_()
        self.pb_showChangeCF_B.raise_()
        
        ##########################################page_showWidgetG_B##################################
        ##########################################page_showWidgetG_B##################################
        ##########################################page_showWidgetG_B##################################
        
        self.page_showWidgetG_B = QWidget()
        self.page_showWidgetG_B.setObjectName(u"page_showWidgetG_B")
        # G布局预览
        
        self.lb_showBackgroundG_B = QLabel(self.page_showWidgetG_B)
        self.lb_showBackgroundG_B.setObjectName(u"lb_showBackgroundG_B")
        self.lb_showBackgroundG_B.setGeometry(QRect(3, 1, 881, 621))
        # G布局内的人物（在左边）
        
        self.lb_showTellG_B = QLabel(self.page_showWidgetG_B)
        self.lb_showTellG_B.setObjectName(u"lb_showTellG_B")
        self.lb_showTellG_B.setGeometry(QRect(190, 400, 551, 181))
        # G布局内的对话框
        
        self.pb_showNextG_B = QPushButton(self.page_showWidgetG_B)
        self.pb_showNextG_B.setObjectName(u"pb_showNextG_B")
        self.pb_showNextG_B.setGeometry(QRect(630, 540, 75, 23))
        # G布局内的切换下一个节点（布局）
        
        self.lb_showNameG_B = QLabel(self.page_showWidgetG_B)
        self.lb_showNameG_B.setObjectName(u"lb_showNameG_B")
        self.lb_showNameG_B.setGeometry(QRect(183, 330, 141, 41))
        # G布局内的名称框
        
        self.sw_showProbject_B.addWidget(self.page_showWidgetG_B)
        
        ##########################################page_showWidgetH_B##################################
        ##########################################page_showWidgetH_B##################################
        ##########################################page_showWidgetH_B##################################
        
        self.page_showWidgetH_B = QWidget()
        self.page_showWidgetH_B.setObjectName(u"page_showWidgetH_B")
        # H布局预览
        
        self.lb_showBackgroundH_B = QLabel(self.page_showWidgetH_B)
        self.lb_showBackgroundH_B.setObjectName(u"lb_showBackgroundH_B")
        self.lb_showBackgroundH_B.setGeometry(QRect(3, 1, 881, 621))
        # H布局内的背景
        
        self.pb_showExitH_B = QPushButton(self.page_showWidgetH_B)
        self.pb_showExitH_B.setObjectName(u"pb_showExitH_B")
        self.pb_showExitH_B.setGeometry(QRect(360, 510, 221, 71))
        # H布局内的退出按钮
        
        self.sw_showProbject_B.addWidget(self.page_showWidgetH_B)
        
        self.sw_show_B.addWidget(self.page_show1_B)
        '·······································page_show1_B········································'
        '·······································page_show1_B········································'
        '·······································page_show1_B········································'
        
        '·······································page_show2_B········································'
        '·······································page_show2_B········································'
        '·······································page_show2_B········································'
        
        self.page_show2_B = QWidget()
        self.page_show2_B.setObjectName(u"page_show2_B")
        # 用于展示流程图的page
        self.sw_show_B.addWidget(self.page_show2_B)
        
        '·······································page_show2_B········································'
        '·······································page_show2_B········································'
        '·······································page_show2_B········································'
        
        self.gridLayout_show_B.addWidget(self.sw_show_B, 0, 0, 1, 1)
        
        #####################################################attribute##############################################
        #####################################################attribute##############################################
        #####################################################attribute##############################################
        
        self.gridLayoutWidget_4 = QWidget(self.widget_B)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(890, 0, 561, 731))
        
        self.gridLayout_attribute_B = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_attribute_B.setObjectName(u"gridLayout_attribute_B")
        self.gridLayout_attribute_B.setContentsMargins(0, 0, 0, 0)
        # 最右边的布局，用于包裹属性编辑的部分
        
        self.sw_attribute_B = QStackedWidget(self.gridLayoutWidget_4)
        self.sw_attribute_B.setObjectName(u"sw_attribute_B")
        # 用于切换流程图和布局开发模式的编辑内容
        
        self.page_attribute_flow_B = QWidget()
        self.page_attribute_flow_B.setObjectName(u"page_attribute_flow_B")
        # 用于存放布局开发模式的内容
        
        self.lb_attribute_flow_background_B = QLabel(self.page_attribute_flow_B)
        self.lb_attribute_flow_background_B.setObjectName(u"lb_attribute_flow_background_B")
        self.lb_attribute_flow_background_B.setGeometry(QRect(0, 0, 560, 730))  # 0, 0, 560, 720
        self.lb_attribute_flow_background_B.setStyleSheet(u"background-color:rgb(20, 20, 24);\n"
                                                          "font: 75 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
                                                          "color:rgb(45, 43, 53);")
        # 背景
        
        # self.lb_attributeBox0_B = QLabel(self.page_attribute_flow_B)
        # self.lb_attributeBox0_B.setObjectName(u"lb_attributeBox0_B")
        # self.lb_attributeBox0_B.setGeometry(QRect(0, 0, 551, 731))
        # sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.lb_attributeBox0_B.sizePolicy().hasHeightForWidth())
        # self.lb_attributeBox0_B.setSizePolicy(sizePolicy)
        # self.lb_attributeBox0_B.setPixmap(QPixmap(u"../image/B1/attribute/lb_attributeBox0_B.png"))
        # 背景，相当于分割各个部分的框
        
        self.lb_attribute_flow_titleFlowI_B = QLabel(self.page_attribute_flow_B)
        self.lb_attribute_flow_titleFlowI_B.setObjectName(u"lb_attribute_flow_titleFlowI_B")
        self.lb_attribute_flow_titleFlowI_B.setGeometry(QRect(0, 0, 201, 51))
        self.lb_attribute_flow_titleFlowI_B.setStyleSheet(u"background-color:rgb(20, 20, 24);\n"
                                                          "font: 75 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
                                                          "color:rgb(255, 255, 255);")
        # 标题文本：窗口属性
        
        # self.lb_attributeWindowSaw_B = QLabel(self.page_attribute_flow_B)
        # self.lb_attributeWindowSaw_B.setObjectName(u"lb_attributeWindowSaw_B")
        # self.lb_attributeWindowSaw_B.setGeometry(QRect(50, 160, 321, 31))
        # self.lb_attributeWindowSaw_B.setStyleSheet(u"font: 75 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 第二框里的“编号布局展示”的提示字
        
        self.lb_attribute_flow_mapII_B = QLabel(self.page_attribute_flow_B)
        self.lb_attribute_flow_mapII_B.setObjectName(u"lb_attribute_flow_mapII_B")
        self.lb_attribute_flow_mapII_B.setGeometry(QRect(90, 240, 371, 171))
        self.lb_attribute_flow_mapII_B.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                                     "font: 87 48pt \"Arial Black\";\n"
                                                     "")
        # 编号布局展示的图片，素材由上传上传(窗性模板展示：)
        
        self.lb_attribute_flow_titleFlowII_B = QLabel(self.page_attribute_flow_B)
        self.lb_attribute_flow_titleFlowII_B.setObjectName(u"lb_attribute_flow_titleFlowII_B")
        self.lb_attribute_flow_titleFlowII_B.setGeometry(QRect(0, 170, 201, 51))
        self.lb_attribute_flow_titleFlowII_B.setStyleSheet(u"background-color:rgb(20, 20, 24);\n"
                                                           "font: 75 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
                                                           "color:rgb(255, 255, 255);")
        # 文本：窗性模板展示
        
        self.lb_attribute_flow_nameI_B = QLabel(self.page_attribute_flow_B)
        self.lb_attribute_flow_nameI_B.setObjectName(u"lb_attribute_flow_nameI_B")
        self.lb_attribute_flow_nameI_B.setGeometry(QRect(50, 90, 201, 31))
        self.lb_attribute_flow_nameI_B.setStyleSheet(u"font: 18pt \"\u5b8b\u4f53\";color:rgb(255, 255, 255);")
        # 文本：窗口名称（注释）
        
        self.le_attribute_flow_nameI_B = QLineEdit(self.page_attribute_flow_B)
        self.le_attribute_flow_nameI_B.setObjectName(u"le_attribute_flow_nameI_B")
        self.le_attribute_flow_nameI_B.setGeometry(QRect(270, 100, 113, 20))
        # 输入框：窗口名称（注释）
        
        self.lb_attribute_flow_mapIII_B = QLabel(self.page_attribute_flow_B)
        self.lb_attribute_flow_mapIII_B.setObjectName(u"lb_attribute_flow_mapIII_B")
        self.lb_attribute_flow_mapIII_B.setGeometry(QRect(90, 530, 371, 171))
        self.lb_attribute_flow_mapIII_B.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                                      "font: 87 48pt \"Arial Black\";\n"
                                                      "")
        # 窗性流程图缩略展示图(该节点的具体内容，由user上传)
        
        self.lb_attribute_flow_numI_B = QLabel(self.page_attribute_flow_B)
        self.lb_attribute_flow_numI_B.setObjectName(u"lb_attribute_flow_numI_B")
        self.lb_attribute_flow_numI_B.setGeometry(QRect(260, 60, 111, 31))
        self.lb_attribute_flow_numI_B.setStyleSheet(u"font: 18pt \"\u5b8b\u4f53\";color:rgb(255, 255, 255);")
        # 文本：窗口编号
        
        self.lb_attribute_flow_titleFlowIII_B = QLabel(self.page_attribute_flow_B)
        self.lb_attribute_flow_titleFlowIII_B.setObjectName(u"lb_attribute_flow_titleFlowIII_B")
        self.lb_attribute_flow_titleFlowIII_B.setGeometry(QRect(0, 470, 301, 51))
        self.lb_attribute_flow_titleFlowIII_B.setStyleSheet(u"background-color:rgb(20, 20, 24);\n"
                                                            "font: 75 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
                                                            "color:rgb(255, 255, 255);")
        # 窗性流程图缩略展示图：文本
        
        self.cb_attribute_flowI_B = QComboBox(self.page_attribute_flow_B)
        self.cb_attribute_flowI_B.setObjectName(u"cb_attribute_flow_B")
        self.cb_attribute_flowI_B.setGeometry(QRect(160, 68, 69, 22))
        # 下拉框：窗口类型
        
        self.lb_attribute_flow_typeI_B = QLabel(self.page_attribute_flow_B)
        self.lb_attribute_flow_typeI_B.setObjectName(u"lb_attribute_flow_typeI_B")
        self.lb_attribute_flow_typeI_B.setGeometry(QRect(50, 60, 111, 31))
        self.lb_attribute_flow_typeI_B.setStyleSheet(u"font: 18pt \"\u5b8b\u4f53\";\n"
                                                     "color:rgb(255, 255, 255);")
        # 文本：窗口类型
        
        self.pb_attribute_flow_updataI_B = QPushButton(self.page_attribute_flow_B)
        self.pb_attribute_flow_updataI_B.setObjectName(u"pb_attribute_flow_updataI_B")
        self.pb_attribute_flow_updataI_B.setGeometry(QRect(320, 480, 111, 31))
        self.pb_attribute_flow_updataI_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 上传窗性流程图缩略展示图的按钮
        
        self.widget_attribute_B = QWidget(self.page_attribute_flow_B)
        self.widget_attribute_B.setObjectName(u"widget_attribute_B")
        self.widget_attribute_B.setGeometry(QRect(-1, -1, 561, 731))
        # 存放布局开发模式的内容的widget
        
        self.sw_attributeSet_B = QStackedWidget(self.widget_attribute_B)
        self.sw_attributeSet_B.setObjectName(u"sw_attributeSet_B")
        self.sw_attributeSet_B.setGeometry(QRect(-7, 111, 885, 610))  # 60, 420, 441, 261
        # 用于存放各个预设控件的属性信息的控件
        
        self.lb_chart_B = QLabel(self.widget_B)
        self.lb_chart_B.setObjectName(u"lb_chart_B")
        self.lb_chart_B.setGeometry(QRect(-7, 111, 896, 620))  # 885, 610
        self.lb_chart_B.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lb_chart_B.stackUnder(self.sw_attributeSet_B)
        # 左侧图表widget的空白背景
        
        self.page_A = QWidget()
        self.page_A.setObjectName(u"page_A")
        # 包含A预设布局的内容
        
        self.sa_attributeSetA_B = QScrollArea(self.page_A)
        self.sa_attributeSetA_B.setObjectName(u"sa_attributeSetA_B")
        self.sa_attributeSetA_B.setGeometry(QRect(-7, 111, 885, 610))  # 0, 0, 441, 261
        self.sa_attributeSetA_B.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.sa_attributeSetA_B.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sa_attributeSetA_B.setWidgetResizable(True)
        # 最下面的框内包裹的滑动条布局，内含A布局的控件及属性内容
        
        self.SaWidgetContents_attributeSetA_B = QWidget()
        self.SaWidgetContents_attributeSetA_B.setObjectName(u"SaWidgetContents_attributeSetA_B")
        self.SaWidgetContents_attributeSetA_B.setGeometry(QRect(0, 0, 431, 399))
        self.SaWidgetContents_attributeSetA_B.setMinimumSize(QSize(431, 399))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.SaWidgetContents_attributeSetA_B.setPalette(palette)
        # sa_attributeSetA_B自动生成的Qgridlayout
        
        self.gridLayout_9 = QGridLayout(self.SaWidgetContents_attributeSetA_B)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        
        self.grid_attributeSetA_B = QGridLayout()
        self.grid_attributeSetA_B.setObjectName(u"grid_attributeSetA_B")
        # 为了使SaWidgetContents_attributeSetA_B的内部控件挤压，使滑动条可使用
        
        self.pb_attributeSetSignA_B = QLabel(self.SaWidgetContents_attributeSetA_B)
        self.pb_attributeSetSignA_B.setObjectName(u"pb_attributeSetSignA_B")
        self.pb_attributeSetSignA_B.setPixmap(QPixmap(u"../image/B1/attribute/pb_attributeSign_B.png"))
        # 各个属性的标志总和成的一张图片在A中
        
        self.grid_attributeSetA_B.addWidget(self.pb_attributeSetSignA_B, 0, 0, 1, 1)
        
        "attribute命名解析："
        #         "例子：lb_attributeNum0A2_B，0代表其在各个属性内的编号，A代表他对应的预设布局，2代表在A的控件中他的编号"
        #         "0:编号； 1.控件名称； 2.控件类型； 3.图片素材； 4.功能描述"
        #         # *********************************************************************attributeA*************************************************************************#
        #         # *********************************************************************attributeA*************************************************************************#
        #         # *********************************************************************attributeA*************************************************************************#
        #
        self.widget_attributeSetA2_B = QWidget(self.SaWidgetContents_attributeSetA_B)
        self.widget_attributeSetA2_B.setObjectName(u"widget_attributeSetA2_B")
        self.widget_attributeSetA2_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为2）
        
        self.lb_attributeNum0A2_B = QLabel(self.widget_attributeSetA2_B)
        self.lb_attributeNum0A2_B.setObjectName(u"lb_attributeNum0A2_B")
        self.lb_attributeNum0A2_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0A2_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为2）,内的编号label
        
        self.lb_attribute1A2_B = QLabel(self.widget_attributeSetA2_B)
        self.lb_attribute1A2_B.setObjectName(u"lb_attribute1A2_B")
        self.lb_attribute1A2_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1A2_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为5）,内的控件名称label
        
        self.lb_attribute2A2_B = QLabel(self.widget_attributeSetA2_B)
        self.lb_attribute2A2_B.setObjectName(u"lb_attribute2A2_B")
        self.lb_attribute2A2_B.setGeometry(QRect(160, 10, 54, 12))
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为2）,内的控件类型label
        
        self.pb_attribute3A2_B = QPushButton(self.widget_attributeSetA2_B)
        self.pb_attribute3A2_B.setObjectName(u"pb_attribute3A2_B")
        self.pb_attribute3A2_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3A2_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为2）,内的图片素材Pushbutton
        
        self.lb_attribute4A2_B = QLabel(self.widget_attributeSetA2_B)
        self.lb_attribute4A2_B.setObjectName(u"lb_attribute4A2_B")
        self.lb_attribute4A2_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4A2_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为2）,内的功能描述label
        
        self.grid_attributeSetA_B.addWidget(self.widget_attributeSetA2_B, 3, 0, 1, 1)
        
        self.widget_attributeSetA0_B = QWidget(self.SaWidgetContents_attributeSetA_B)
        self.widget_attributeSetA0_B.setObjectName(u"widget_attributeSetA0_B")
        self.widget_attributeSetA0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为0）
        
        self.lb_attributeNum0A0_B = QLabel(self.widget_attributeSetA0_B)
        self.lb_attributeNum0A0_B.setObjectName(u"lb_attributeNum0A0_B")
        self.lb_attributeNum0A0_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0A0_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为0）,内的编号label
        
        self.lb_attribute1A0_B = QLabel(self.widget_attributeSetA0_B)
        self.lb_attribute1A0_B.setObjectName(u"lb_attribute1A0_B")
        self.lb_attribute1A0_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1A0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为0）,内的控件名称label
        
        self.lb_attribute2A0_B = QLabel(self.widget_attributeSetA0_B)
        self.lb_attribute2A0_B.setObjectName(u"lb_attribute2A0_B")
        self.lb_attribute2A0_B.setGeometry(QRect(160, 10, 54, 12))
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为0）,内的控件类型label
        
        self.pb_attribute3A0_B = QPushButton(self.widget_attributeSetA0_B)
        self.pb_attribute3A0_B.setObjectName(u"pb_attribute3A0_B")
        self.pb_attribute3A0_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3A0_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为0）,内的图片素材PushButton
        
        self.lb_attribute4A0_B = QLabel(self.widget_attributeSetA0_B)
        self.lb_attribute4A0_B.setObjectName(u"lb_attribute4A0_B")
        self.lb_attribute4A0_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4A0_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为0）,内的功能描述label
        
        self.grid_attributeSetA_B.addWidget(self.widget_attributeSetA0_B, 1, 0, 1, 1)
        
        self.widget_attributeSetA1_B = QWidget(self.SaWidgetContents_attributeSetA_B)
        self.widget_attributeSetA1_B.setObjectName(u"widget_attributeSetA1_B")
        self.widget_attributeSetA1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为1）
        
        self.lb_attributeNum0A1_B = QLabel(self.widget_attributeSetA1_B)
        self.lb_attributeNum0A1_B.setObjectName(u"lb_attributeNum0A1_B")
        self.lb_attributeNum0A1_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0A1_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为1）,内的编号label
        
        self.lb_attribute1A1_B = QLabel(self.widget_attributeSetA1_B)
        self.lb_attribute1A1_B.setObjectName(u"lb_attribute1A1_B")
        self.lb_attribute1A1_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1A1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为1）,内的控件名称label
        
        self.lb_attribute2A1_B = QLabel(self.widget_attributeSetA1_B)
        self.lb_attribute2A1_B.setObjectName(u"lb_attribute2A1_B")
        self.lb_attribute2A1_B.setGeometry(QRect(160, 10, 54, 12))
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为1）,内的控件类型label
        
        self.pb_attribute3A1_B = QPushButton(self.widget_attributeSetA1_B)
        self.pb_attribute3A1_B.setObjectName(u"pb_attribute3A1_B")
        self.pb_attribute3A1_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3A1_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为1）,内的图片素材PushButton
        
        self.lb_attribute4A1_B = QLabel(self.widget_attributeSetA1_B)
        self.lb_attribute4A1_B.setObjectName(u"lb_attribute4A1_B")
        self.lb_attribute4A1_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4A1_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为1）,内的功能描述label
        
        self.grid_attributeSetA_B.addWidget(self.widget_attributeSetA1_B, 2, 0, 1, 1)
        
        self.widget_attributeSetA5_B = QWidget(self.SaWidgetContents_attributeSetA_B)
        self.widget_attributeSetA5_B.setObjectName(u"widget_attributeSetA5_B")
        self.widget_attributeSetA5_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为5）
        
        self.lb_attributeNum0A5_B = QLabel(self.widget_attributeSetA5_B)
        self.lb_attributeNum0A5_B.setObjectName(u"lb_attributeNum0A5_B")
        self.lb_attributeNum0A5_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0A5_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为5）,内的编号label
        
        self.lb_attribute1A5_B = QLabel(self.widget_attributeSetA5_B)
        self.lb_attribute1A5_B.setObjectName(u"lb_attribute1A5_B")
        self.lb_attribute1A5_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1A5_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为5）,内的控件名称label
        
        self.pb_attribute3A5_B = QPushButton(self.widget_attributeSetA5_B)
        self.pb_attribute3A5_B.setObjectName(u"pb_attribute3A5_B")
        self.pb_attribute3A5_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3A5_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为5）,内的图片素材PushButton
        
        self.lb_attribute4A5_B = QLabel(self.widget_attributeSetA5_B)
        self.lb_attribute4A5_B.setObjectName(u"lb_attribute4A5_B")
        self.lb_attribute4A5_B.setGeometry(QRect(320, 0, 81, 31))
        self.lb_attribute4A5_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为5）,内的功能描述label
        
        self.lb_attribute2A5_B = QLabel(self.widget_attributeSetA5_B)
        self.lb_attribute2A5_B.setObjectName(u"lb_attribute2A5_B")
        self.lb_attribute2A5_B.setGeometry(QRect(160, 0, 61, 41))
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为5）,内的控件类型label
        
        self.grid_attributeSetA_B.addWidget(self.widget_attributeSetA5_B, 6, 0, 1, 1)
        
        self.widget_attributeSetA3_B = QWidget(self.SaWidgetContents_attributeSetA_B)
        self.widget_attributeSetA3_B.setObjectName(u"widget_attributeSetA3_B")
        self.widget_attributeSetA3_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为3）
        
        self.lb_attributeNum0A3_B = QLabel(self.widget_attributeSetA3_B)
        self.lb_attributeNum0A3_B.setObjectName(u"lb_attributeNum0A3_B")
        self.lb_attributeNum0A3_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0A3_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为3）,内的编号label
        
        self.lb_attribute1A3_B = QLabel(self.widget_attributeSetA3_B)
        self.lb_attribute1A3_B.setObjectName(u"lb_attribute1A3_B")
        self.lb_attribute1A3_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1A3_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为3）,内的控件名称label
        
        self.lb_attribute2A3_B = QLabel(self.widget_attributeSetA3_B)
        self.lb_attribute2A3_B.setObjectName(u"lb_attribute2A3_B")
        self.lb_attribute2A3_B.setGeometry(QRect(160, 0, 61, 41))
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为3）,内的控件类型label
        
        self.pb_attribute3A3_B = QPushButton(self.widget_attributeSetA3_B)
        self.pb_attribute3A3_B.setObjectName(u"pb_attribute3A3_B")
        self.pb_attribute3A3_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3A3_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为3）,内的图片素材PushButton
        
        self.lb_attribute4A3_B = QLabel(self.widget_attributeSetA3_B)
        self.lb_attribute4A3_B.setObjectName(u"lb_attribute4A3_B")
        self.lb_attribute4A3_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4A3_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为3）,内的功能描述label
        
        self.grid_attributeSetA_B.addWidget(self.widget_attributeSetA3_B, 4, 0, 1, 1)
        
        self.widget_attributeSetA4_B = QWidget(self.SaWidgetContents_attributeSetA_B)
        self.widget_attributeSetA4_B.setObjectName(u"widget_attributeSetA4_B")
        self.widget_attributeSetA4_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为4）
        
        self.lb_attributeNum0A4_B = QLabel(self.widget_attributeSetA4_B)
        self.lb_attributeNum0A4_B.setObjectName(u"lb_attributeNum0A4_B")
        self.lb_attributeNum0A4_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0A4_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为4）,内的编号label
        
        self.lb_attribute1A4_B = QLabel(self.widget_attributeSetA4_B)
        self.lb_attribute1A4_B.setObjectName(u"lb_attribute1A4_B")
        self.lb_attribute1A4_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1A4_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为4）,内的控件名称label
        
        self.pb_attribute3A4_B = QPushButton(self.widget_attributeSetA4_B)
        self.pb_attribute3A4_B.setObjectName(u"pb_attribute3A4_B")
        self.pb_attribute3A4_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3A4_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为4）,内的图片素材PushButton
        
        self.lb_attribute4A4_B = QLabel(self.widget_attributeSetA4_B)
        self.lb_attribute4A4_B.setObjectName(u"lb_attribute4A4_B")
        self.lb_attribute4A4_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4A4_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为4）,内的功能描述label
        
        self.lb_attribute2A4_B = QLabel(self.widget_attributeSetA4_B)
        self.lb_attribute2A4_B.setObjectName(u"lb_attribute2A4_B")
        self.lb_attribute2A4_B.setGeometry(QRect(160, 0, 61, 41))
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为4）,内的控件名称label
        
        self.grid_attributeSetA_B.addWidget(self.widget_attributeSetA4_B, 5, 0, 1, 1)
        
        self.widget_attributeSetA6_B = QWidget(self.SaWidgetContents_attributeSetA_B)
        self.widget_attributeSetA6_B.setObjectName(u"widget_attributeSetA6_B")
        self.widget_attributeSetA6_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为6）
        
        self.lb_attributeNum0A6_B = QLabel(self.widget_attributeSetA6_B)
        self.lb_attributeNum0A6_B.setObjectName(u"lb_attributeNum0A6_B")
        self.lb_attributeNum0A6_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0A6_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为6）,内的编号label
        
        self.lb_attribute1A6_B = QLabel(self.widget_attributeSetA6_B)
        self.lb_attribute1A6_B.setObjectName(u"lb_attribute1A6_B")
        self.lb_attribute1A6_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1A6_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为6）,内的控件名称label
        
        self.pb_attribute3A6_B = QPushButton(self.widget_attributeSetA6_B)
        self.pb_attribute3A6_B.setObjectName(u"pb_attribute3A6_B")
        self.pb_attribute3A6_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3A6_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为6）,内的图片素材PushButton
        
        self.lb_attribute4A6_B = QLabel(self.widget_attributeSetA6_B)
        self.lb_attribute4A6_B.setObjectName(u"lb_attribute4A6_B")
        self.lb_attribute4A6_B.setGeometry(QRect(330, 0, 61, 31))
        self.lb_attribute4A6_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为6）,内的功能描述label
        
        self.lb_attribute2A6_B = QLabel(self.widget_attributeSetA6_B)
        self.lb_attribute2A6_B.setObjectName(u"lb_attribute2A6_B")
        self.lb_attribute2A6_B.setGeometry(QRect(160, 0, 61, 41))
        # 包裹每个控件的各个属性控件的布局（在所有A布局控件中索引为6）,内的控件类型label
        
        self.grid_attributeSetA_B.addWidget(self.widget_attributeSetA6_B, 7, 0, 1, 1)
        self.gridLayout_9.addLayout(self.grid_attributeSetA_B, 1, 0, 1, 1)
        self.sa_attributeSetA_B.setWidget(self.SaWidgetContents_attributeSetA_B)
        self.sw_attributeSet_B.addWidget(self.page_A)
        # *********************************************************************attributeB*************************************************************************#
        # *********************************************************************attributeB*************************************************************************#
        # *********************************************************************attributeB*************************************************************************#
        
        self.page_B = QWidget()
        self.page_B.setObjectName(u"page_B")
        # 包含B预设布局的内容
        
        self.sa_attributeSetB_B = QScrollArea(self.page_B)
        self.sa_attributeSetB_B.setObjectName(u"sa_attributeSetB_B")
        self.sa_attributeSetB_B.setGeometry(QRect(0, 0, 441, 261))
        self.sa_attributeSetB_B.setMinimumSize(QSize(0, 0))
        self.sa_attributeSetB_B.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.sa_attributeSetB_B.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sa_attributeSetB_B.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.sa_attributeSetB_B.setWidgetResizable(True)
        # 最下面的框内包裹的滑动条布局，内含B布局的控件及属性内容
        
        self.SaWidgetContents_attributeSetB_B = QWidget()
        self.SaWidgetContents_attributeSetB_B.setObjectName(u"SaWidgetContents_attributeSetB_B")
        self.SaWidgetContents_attributeSetB_B.setGeometry(QRect(0, 0, 431, 259))
        self.SaWidgetContents_attributeSetB_B.setMinimumSize(QSize(0, 0))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.SaWidgetContents_attributeSetB_B.setPalette(palette1)
        # sa_attributeSetB_B自动生成的Qgridlayout
        
        self.gridLayout_10 = QGridLayout(self.SaWidgetContents_attributeSetB_B)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        
        self.grid_attributeSetB_B = QGridLayout()
        self.grid_attributeSetB_B.setObjectName(u"grid_attributeSetB_B")
        # 为了使SaWidgetContents_attributeSetB_B的内部控件挤压，使滑动条可使用
        
        self.widget_attributeSetB3_B = QWidget(self.SaWidgetContents_attributeSetB_B)
        self.widget_attributeSetB3_B.setObjectName(u"widget_attributeSetB3")
        self.widget_attributeSetB3_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有B布局控件中索引为3）
        
        self.lb_attributeNum0B3_B = QLabel(self.widget_attributeSetB3_B)
        self.lb_attributeNum0B3_B.setObjectName(u"lb_attributeNum0B3_B")
        self.lb_attributeNum0B3_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0B3_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        # 包裹每个控件的各个属性控件的布局（在所有B布局控件中索引为3）,内的编号label
        
        self.lb_attribute1B3_B = QLabel(self.widget_attributeSetB3_B)
        self.lb_attribute1B3_B.setObjectName(u"lb_attribute1B3_B")
        self.lb_attribute1B3_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1B3_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        # 包裹每个控件的各个属性控件的布局（在所有B布局控件中索引为3）,内的控件名称label
        
        self.lb_attribute2B3_B = QLabel(self.widget_attributeSetB3_B)
        self.lb_attribute2B3_B.setObjectName(u"lb_attribute2B3_B")
        self.lb_attribute2B3_B.setGeometry(QRect(160, 0, 61, 41))
        # 包裹每个控件的各个属性控件的布局（在所有B布局控件中索引为3）,内的控件类型label
        
        self.pb_attribute3B3_B = QPushButton(self.widget_attributeSetB3_B)
        self.pb_attribute3B3_B.setObjectName(u"pb_attribute3B3_B")
        self.pb_attribute3B3_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3B3_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有B布局控件中索引为3）,内的图片素材Pushbutton
        
        self.lb_attribute4B3_B = QLabel(self.widget_attributeSetB3_B)
        self.lb_attribute4B3_B.setObjectName(u"lb_attribute4B3_B")
        self.lb_attribute4B3_B.setGeometry(QRect(330, 0, 61, 31))
        self.lb_attribute4B3_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 包裹每个控件的各个属性控件的布局（在所有B布局控件中索引为4）,内的功能描述label
        
        self.grid_attributeSetB_B.addWidget(self.widget_attributeSetB3_B, 4, 0, 1, 1)
        
        self.pb_attributeSetSignB_B = QLabel(self.SaWidgetContents_attributeSetB_B)
        self.pb_attributeSetSignB_B.setObjectName(u"pb_attributeSetSignB_B")
        self.pb_attributeSetSignB_B.setPixmap(QPixmap(u"../image/B1/attribute/pb_attributeSign_B.png"))
        # 各个属性的标志总和成的一张图片在B中
        self.grid_attributeSetB_B.addWidget(self.pb_attributeSetSignB_B, 0, 0, 1, 1)
        
        "PS :本人很懒，剩下内容请根据命名规则读懂控件的对应功能（上面的地方已给出）"
        
        self.widget_attributeSetB2_B = QWidget(self.SaWidgetContents_attributeSetB_B)
        self.widget_attributeSetB2_B.setObjectName(u"widget_attributeSetB2_B")
        self.widget_attributeSetB2_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0B2_B = QLabel(self.widget_attributeSetB2_B)
        self.lb_attributeNum0B2_B.setObjectName(u"lb_attributeNum0B2_B")
        self.lb_attributeNum0B2_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0B2_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1B2_B = QLabel(self.widget_attributeSetB2_B)
        self.lb_attribute1B2_B.setObjectName(u"lb_attribute1B2_B")
        self.lb_attribute1B2_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1B2_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2B2_B = QLabel(self.widget_attributeSetB2_B)
        self.lb_attribute2B2_B.setObjectName(u"lb_attribute2B2_B")
        self.lb_attribute2B2_B.setGeometry(QRect(160, 10, 54, 12))
        self.pb_attribute3B2_B = QPushButton(self.widget_attributeSetB2_B)
        self.pb_attribute3B2_B.setObjectName(u"pb_attribute3B2_B")
        self.pb_attribute3B2_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3B2_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4B2_B = QLabel(self.widget_attributeSetB2_B)
        self.lb_attribute4B2_B.setObjectName(u"lb_attribute4B2_B")
        self.lb_attribute4B2_B.setGeometry(QRect(320, 0, 81, 31))
        self.lb_attribute4B2_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetB_B.addWidget(self.widget_attributeSetB2_B, 3, 0, 1, 1)
        
        self.widget_attributeSetB1_B = QWidget(self.SaWidgetContents_attributeSetB_B)
        self.widget_attributeSetB1_B.setObjectName(u"widget_attributeSetB1_B")
        self.widget_attributeSetB1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0B1_B = QLabel(self.widget_attributeSetB1_B)
        self.lb_attributeNum0B1_B.setObjectName(u"lb_attributeNum0B1_B")
        self.lb_attributeNum0B1_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0B1_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1B1_B = QLabel(self.widget_attributeSetB1_B)
        self.lb_attribute1B1_B.setObjectName(u"lb_attribute1B1_B")
        self.lb_attribute1B1_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1B1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2B1_B = QLabel(self.widget_attributeSetB1_B)
        self.lb_attribute2B1_B.setObjectName(u"lb_attribute2B1_B")
        self.lb_attribute2B1_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3B1_B = QPushButton(self.widget_attributeSetB1_B)
        self.pb_attribute3B1_B.setObjectName(u"pb_attribute3B1_B")
        self.pb_attribute3B1_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3B1_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4B1_B = QLabel(self.widget_attributeSetB1_B)
        self.lb_attribute4B1_B.setObjectName(u"lb_attribute4B1_B")
        self.lb_attribute4B1_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4B1_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetB_B.addWidget(self.widget_attributeSetB1_B, 2, 0, 1, 1)
        
        self.widget_attributeSetB0_B = QWidget(self.SaWidgetContents_attributeSetB_B)
        self.widget_attributeSetB0_B.setObjectName(u"widget_attributeSetB0_B")
        self.widget_attributeSetB0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0B0_B = QLabel(self.widget_attributeSetB0_B)
        self.lb_attributeNum0B0_B.setObjectName(u"lb_attributeNum0B0_B")
        self.lb_attributeNum0B0_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0B0_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1B0_B = QLabel(self.widget_attributeSetB0_B)
        self.lb_attribute1B0_B.setObjectName(u"lb_attribute1B0_B")
        self.lb_attribute1B0_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1B0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2B0_B = QLabel(self.widget_attributeSetB0_B)
        self.lb_attribute2B0_B.setObjectName(u"lb_attribute2B0_B")
        self.lb_attribute2B0_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3B0_B = QPushButton(self.widget_attributeSetB0_B)
        self.pb_attribute3B0_B.setObjectName(u"pb_attribute3B0_B")
        self.pb_attribute3B0_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3B0_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4B0_B = QLabel(self.widget_attributeSetB0_B)
        self.lb_attribute4B0_B.setObjectName(u"lb_attribute4B0_B")
        self.lb_attribute4B0_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4B0_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetB_B.addWidget(self.widget_attributeSetB0_B, 1, 0, 1, 1)
        
        self.gridLayout_10.addLayout(self.grid_attributeSetB_B, 1, 0, 1, 1)
        
        self.sa_attributeSetB_B.setWidget(self.SaWidgetContents_attributeSetB_B)
        
        self.sw_attributeSet_B.addWidget(self.page_B)
        
        # *********************************************************************attributeC*************************************************************************#
        # *********************************************************************attributeC*************************************************************************#
        # *********************************************************************attributeC*************************************************************************#
        
        self.page_C = QWidget()
        self.page_C.setObjectName(u"page_C")
        
        self.sa_attributeSetC_B = QScrollArea(self.page_C)
        self.sa_attributeSetC_B.setObjectName(u"sa_attributeSetC_B")
        self.sa_attributeSetC_B.setGeometry(QRect(0, 0, 441, 261))
        self.sa_attributeSetC_B.setMinimumSize(QSize(0, 0))
        self.sa_attributeSetC_B.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.sa_attributeSetC_B.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sa_attributeSetC_B.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.sa_attributeSetC_B.setWidgetResizable(True)
        self.SaWidgetContents_attributeSetC_B = QWidget()
        self.SaWidgetContents_attributeSetC_B.setObjectName(u"SaWidgetContents_attributeSetC_B")
        self.SaWidgetContents_attributeSetC_B.setGeometry(QRect(0, 0, 431, 259))
        self.SaWidgetContents_attributeSetC_B.setMinimumSize(QSize(0, 0))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.SaWidgetContents_attributeSetC_B.setPalette(palette2)
        
        self.gridLayout_11 = QGridLayout(self.SaWidgetContents_attributeSetC_B)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        
        self.grid_attributeSetC_B = QGridLayout()
        self.grid_attributeSetC_B.setObjectName(u"grid_attributeSetC_B")
        
        self.widget_attributeSetC3 = QWidget(self.SaWidgetContents_attributeSetC_B)
        self.widget_attributeSetC3.setObjectName(u"widget_attributeSetC3")
        self.widget_attributeSetC3.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0C3_B = QLabel(self.widget_attributeSetC3)
        self.lb_attributeNum0C3_B.setObjectName(u"lb_attributeNum0C3_B")
        self.lb_attributeNum0C3_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0C3_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1C3_B = QLabel(self.widget_attributeSetC3)
        self.lb_attribute1C3_B.setObjectName(u"lb_attribute1C3_B")
        self.lb_attribute1C3_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1C3_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2C3_B = QLabel(self.widget_attributeSetC3)
        self.lb_attribute2C3_B.setObjectName(u"lb_attribute2C3_B")
        self.lb_attribute2C3_B.setGeometry(QRect(160, 0, 61, 41))
        
        self.pb_attribute3C3_B = QPushButton(self.widget_attributeSetC3)
        self.pb_attribute3C3_B.setObjectName(u"pb_attribute3C3_B")
        self.pb_attribute3C3_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3C3_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4C3_B = QLabel(self.widget_attributeSetC3)
        self.lb_attribute4C3_B.setObjectName(u"lb_attribute4C3_B")
        self.lb_attribute4C3_B.setGeometry(QRect(330, 0, 61, 31))
        self.lb_attribute4C3_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetC_B.addWidget(self.widget_attributeSetC3, 4, 0, 1, 1)
        
        self.pb_attributeSetSignC_B = QLabel(self.SaWidgetContents_attributeSetC_B)
        self.pb_attributeSetSignC_B.setObjectName(u"pb_attributeSetSignC_B")
        self.pb_attributeSetSignC_B.setPixmap(QPixmap(u"../image/B1/attribute/pb_attributeSign_B.png"))
        
        self.grid_attributeSetC_B.addWidget(self.pb_attributeSetSignC_B, 0, 0, 1, 1)
        
        self.widget_attributeSetC2_B = QWidget(self.SaWidgetContents_attributeSetC_B)
        self.widget_attributeSetC2_B.setObjectName(u"widget_attributeSetC2_B")
        self.widget_attributeSetC2_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0C2_B = QLabel(self.widget_attributeSetC2_B)
        self.lb_attributeNum0C2_B.setObjectName(u"lb_attributeNum0C2_B")
        self.lb_attributeNum0C2_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0C2_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1C2_B = QLabel(self.widget_attributeSetC2_B)
        self.lb_attribute1C2_B.setObjectName(u"lb_attribute1C2_B")
        self.lb_attribute1C2_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1C2_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2C2_B = QLabel(self.widget_attributeSetC2_B)
        self.lb_attribute2C2_B.setObjectName(u"lb_attribute2C2_B")
        self.lb_attribute2C2_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3C2_B = QPushButton(self.widget_attributeSetC2_B)
        self.pb_attribute3C2_B.setObjectName(u"pb_attribute3C2_B")
        self.pb_attribute3C2_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3C2_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4C2_B = QLabel(self.widget_attributeSetC2_B)
        self.lb_attribute4C2_B.setObjectName(u"lb_attribute4C2_B")
        self.lb_attribute4C2_B.setGeometry(QRect(320, 0, 81, 31))
        self.lb_attribute4C2_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetC_B.addWidget(self.widget_attributeSetC2_B, 3, 0, 1, 1)
        
        self.widget_attributeSetC1_B = QWidget(self.SaWidgetContents_attributeSetC_B)
        self.widget_attributeSetC1_B.setObjectName(u"widget_attributeSetC1_B")
        self.widget_attributeSetC1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0C1_B = QLabel(self.widget_attributeSetC1_B)
        self.lb_attributeNum0C1_B.setObjectName(u"lb_attributeNum0C1_B")
        self.lb_attributeNum0C1_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0C1_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1C1_B = QLabel(self.widget_attributeSetC1_B)
        self.lb_attribute1C1_B.setObjectName(u"lb_attribute1C1_B")
        self.lb_attribute1C1_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1C1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2C1_B = QLabel(self.widget_attributeSetC1_B)
        self.lb_attribute2C1_B.setObjectName(u"lb_attribute2C1_B")
        self.lb_attribute2C1_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3C1_B = QPushButton(self.widget_attributeSetC1_B)
        self.pb_attribute3C1_B.setObjectName(u"pb_attribute3C1_B")
        self.pb_attribute3C1_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3C1_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4C1_B = QLabel(self.widget_attributeSetC1_B)
        self.lb_attribute4C1_B.setObjectName(u"lb_attribute4C1_B")
        self.lb_attribute4C1_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4C1_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetC_B.addWidget(self.widget_attributeSetC1_B, 2, 0, 1, 1)
        
        self.widget_attributeSetC0_B = QWidget(self.SaWidgetContents_attributeSetC_B)
        self.widget_attributeSetC0_B.setObjectName(u"widget_attributeSetC0_B")
        self.widget_attributeSetC0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0C0_B = QLabel(self.widget_attributeSetC0_B)
        self.lb_attributeNum0C0_B.setObjectName(u"lb_attributeNum0C0_B")
        self.lb_attributeNum0C0_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0C0_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1C0_B = QLabel(self.widget_attributeSetC0_B)
        self.lb_attribute1C0_B.setObjectName(u"lb_attribute1C0_B")
        self.lb_attribute1C0_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1C0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2C0_B = QLabel(self.widget_attributeSetC0_B)
        self.lb_attribute2C0_B.setObjectName(u"lb_attribute2C0_B")
        self.lb_attribute2C0_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3C0_B = QPushButton(self.widget_attributeSetC0_B)
        self.pb_attribute3C0_B.setObjectName(u"pb_attribute3C0_B")
        self.pb_attribute3C0_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3C0_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4C0_B = QLabel(self.widget_attributeSetC0_B)
        self.lb_attribute4C0_B.setObjectName(u"lb_attribute4C0_B")
        self.lb_attribute4C0_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4C0_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetC_B.addWidget(self.widget_attributeSetC0_B, 1, 0, 1, 1)
        
        self.gridLayout_11.addLayout(self.grid_attributeSetC_B, 1, 0, 1, 1)
        
        self.sa_attributeSetC_B.setWidget(self.SaWidgetContents_attributeSetC_B)
        
        self.sw_attributeSet_B.addWidget(self.page_C)
        
        self.page_D = QWidget()
        self.page_D.setObjectName(u"page_D")
        
        # *********************************************************************attributeD*************************************************************************#
        # *********************************************************************attributeD*************************************************************************#
        # *********************************************************************attributeD*************************************************************************#
        
        self.sa_attributeSetD_B = QScrollArea(self.page_D)
        self.sa_attributeSetD_B.setObjectName(u"sa_attributeSetD_B")
        self.sa_attributeSetD_B.setGeometry(QRect(0, 0, 441, 261))
        self.sa_attributeSetD_B.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.sa_attributeSetD_B.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sa_attributeSetD_B.setWidgetResizable(True)
        
        self.SaWidgetContents_attributeSetD_B = QWidget()
        self.SaWidgetContents_attributeSetD_B.setObjectName(u"SaWidgetContents_attributeSetD_B")
        self.SaWidgetContents_attributeSetD_B.setGeometry(QRect(0, 0, 431, 399))
        self.SaWidgetContents_attributeSetD_B.setMinimumSize(QSize(431, 399))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.SaWidgetContents_attributeSetD_B.setPalette(palette3)
        
        self.gridLayout_12 = QGridLayout(self.SaWidgetContents_attributeSetD_B)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        
        self.grid_attributeSetD_B = QGridLayout()
        self.grid_attributeSetD_B.setObjectName(u"grid_attributeSetD_B")
        
        self.widget_attributeSetD3_B = QWidget(self.SaWidgetContents_attributeSetD_B)
        self.widget_attributeSetD3_B.setObjectName(u"widget_attributeSetD3_B")
        self.widget_attributeSetD3_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0D3_B = QLabel(self.widget_attributeSetD3_B)
        self.lb_attributeNum0D3_B.setObjectName(u"lb_attributeNum0D3_B")
        self.lb_attributeNum0D3_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0D3_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1D3_B = QLabel(self.widget_attributeSetD3_B)
        self.lb_attribute1D3_B.setObjectName(u"lb_attribute1D3_B")
        self.lb_attribute1D3_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1D3_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2D3_B = QLabel(self.widget_attributeSetD3_B)
        self.lb_attribute2D3_B.setObjectName(u"lb_attribute2D3_B")
        self.lb_attribute2D3_B.setGeometry(QRect(160, 0, 61, 41))
        
        self.pb_attribute3D3_B = QPushButton(self.widget_attributeSetD3_B)
        self.pb_attribute3D3_B.setObjectName(u"pb_attribute3D3_B")
        self.pb_attribute3D3_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3D3_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4D3_B = QLabel(self.widget_attributeSetD3_B)
        self.lb_attribute4D3_B.setObjectName(u"lb_attribute4D3_B")
        self.lb_attribute4D3_B.setGeometry(QRect(320, 0, 81, 31))
        self.lb_attribute4D3_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetD_B.addWidget(self.widget_attributeSetD3_B, 4, 0, 1, 1)
        
        self.widget_attributeSetD0_B = QWidget(self.SaWidgetContents_attributeSetD_B)
        self.widget_attributeSetD0_B.setObjectName(u"widget_attributeSetD0_B")
        self.widget_attributeSetD0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0D0_B = QLabel(self.widget_attributeSetD0_B)
        self.lb_attributeNum0D0_B.setObjectName(u"lb_attributeNum0D0_B")
        self.lb_attributeNum0D0_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0D0_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1D0_B = QLabel(self.widget_attributeSetD0_B)
        self.lb_attribute1D0_B.setObjectName(u"lb_attribute1D0_B")
        self.lb_attribute1D0_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1D0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2D0_B = QLabel(self.widget_attributeSetD0_B)
        self.lb_attribute2D0_B.setObjectName(u"lb_attribute2D0_B")
        self.lb_attribute2D0_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3D0_B = QPushButton(self.widget_attributeSetD0_B)
        self.pb_attribute3D0_B.setObjectName(u"pb_attribute3D0_B")
        self.pb_attribute3D0_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3D0_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4D0_B = QLabel(self.widget_attributeSetD0_B)
        self.lb_attribute4D0_B.setObjectName(u"lb_attribute4D0_B")
        self.lb_attribute4D0_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4D0_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetD_B.addWidget(self.widget_attributeSetD0_B, 1, 0, 1, 1)
        
        self.pb_attributeSetSignD_B = QLabel(self.SaWidgetContents_attributeSetD_B)
        self.pb_attributeSetSignD_B.setObjectName(u"pb_attributeSetSignD_B")
        self.pb_attributeSetSignD_B.setPixmap(QPixmap(u"../image/B1/attribute/pb_attributeSign_B.png"))
        
        self.grid_attributeSetD_B.addWidget(self.pb_attributeSetSignD_B, 0, 0, 1, 1)
        
        self.widget_attributeSetD2_B = QWidget(self.SaWidgetContents_attributeSetD_B)
        self.widget_attributeSetD2_B.setObjectName(u"widget_attributeSetD2_B")
        self.widget_attributeSetD2_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0D2_B = QLabel(self.widget_attributeSetD2_B)
        self.lb_attributeNum0D2_B.setObjectName(u"lb_attributeNum0D2_B")
        self.lb_attributeNum0D2_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0D2_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1D2_B = QLabel(self.widget_attributeSetD2_B)
        self.lb_attribute1D2_B.setObjectName(u"lb_attribute1D2_B")
        self.lb_attribute1D2_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1D2_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2D2_B = QLabel(self.widget_attributeSetD2_B)
        self.lb_attribute2D2_B.setObjectName(u"lb_attribute2D2_B")
        self.lb_attribute2D2_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3D2_B = QPushButton(self.widget_attributeSetD2_B)
        self.pb_attribute3D2_B.setObjectName(u"pb_attribute3D2_B")
        self.pb_attribute3D2_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3D2_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4D2_B = QLabel(self.widget_attributeSetD2_B)
        self.lb_attribute4D2_B.setObjectName(u"lb_attribute4D2_B")
        self.lb_attribute4D2_B.setGeometry(QRect(310, 0, 101, 31))
        self.lb_attribute4D2_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetD_B.addWidget(self.widget_attributeSetD2_B, 3, 0, 1, 1)
        
        self.widget_attributeSetD1_B = QWidget(self.SaWidgetContents_attributeSetD_B)
        self.widget_attributeSetD1_B.setObjectName(u"widget_attributeSetD1_B")
        self.widget_attributeSetD1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0D1_B = QLabel(self.widget_attributeSetD1_B)
        self.lb_attributeNum0D1_B.setObjectName(u"lb_attributeNum0D1_B")
        self.lb_attributeNum0D1_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0D1_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1D1_B = QLabel(self.widget_attributeSetD1_B)
        self.lb_attribute1D1_B.setObjectName(u"lb_attribute1D1_B")
        self.lb_attribute1D1_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1D1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2D1_B = QLabel(self.widget_attributeSetD1_B)
        self.lb_attribute2D1_B.setObjectName(u"lb_attribute2D1_B")
        self.lb_attribute2D1_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3D1_B = QPushButton(self.widget_attributeSetD1_B)
        self.pb_attribute3D1_B.setObjectName(u"pb_attribute3D1_B")
        self.pb_attribute3D1_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3D1_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4D1_B = QLabel(self.widget_attributeSetD1_B)
        self.lb_attribute4D1_B.setObjectName(u"lb_attribute4D1_B")
        self.lb_attribute4D1_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4D1_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetD_B.addWidget(self.widget_attributeSetD1_B, 2, 0, 1, 1)
        
        self.widget_attributeSetD5_B = QWidget(self.SaWidgetContents_attributeSetD_B)
        self.widget_attributeSetD5_B.setObjectName(u"widget_attributeSetD5_B")
        self.widget_attributeSetD5_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0D5_B = QLabel(self.widget_attributeSetD5_B)
        self.lb_attributeNum0D5_B.setObjectName(u"lb_attributeNum0D5_B")
        self.lb_attributeNum0D5_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0D5_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1D5_B = QLabel(self.widget_attributeSetD5_B)
        self.lb_attribute1D5_B.setObjectName(u"lb_attribute1D5_B")
        self.lb_attribute1D5_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1D5_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.pb_attribute3D5_B = QPushButton(self.widget_attributeSetD5_B)
        self.pb_attribute3D5_B.setObjectName(u"pb_attribute3D5_B")
        self.pb_attribute3D5_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3D5_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4D5_B = QLabel(self.widget_attributeSetD5_B)
        self.lb_attribute4D5_B.setObjectName(u"lb_attribute4D5_B")
        self.lb_attribute4D5_B.setGeometry(QRect(340, 0, 51, 31))
        self.lb_attribute4D5_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute2D5_B = QLabel(self.widget_attributeSetD5_B)
        self.lb_attribute2D5_B.setObjectName(u"lb_attribute2D5_B")
        self.lb_attribute2D5_B.setGeometry(QRect(160, 0, 61, 41))
        
        self.grid_attributeSetD_B.addWidget(self.widget_attributeSetD5_B, 6, 0, 1, 1)
        
        self.widget_attributeSetD4_B = QWidget(self.SaWidgetContents_attributeSetD_B)
        self.widget_attributeSetD4_B.setObjectName(u"widget_attributeSetD4_B")
        self.widget_attributeSetD4_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0D4_B = QLabel(self.widget_attributeSetD4_B)
        self.lb_attributeNum0D4_B.setObjectName(u"lb_attributeNum0D4_B")
        self.lb_attributeNum0D4_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0D4_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1D4_B = QLabel(self.widget_attributeSetD4_B)
        self.lb_attribute1D4_B.setObjectName(u"lb_attribute1D4_B")
        self.lb_attribute1D4_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1D4_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.pb_attribute3D4_B = QPushButton(self.widget_attributeSetD4_B)
        self.pb_attribute3D4_B.setObjectName(u"pb_attribute3D4_B")
        self.pb_attribute3D4_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3D4_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4D4_B = QLabel(self.widget_attributeSetD4_B)
        self.lb_attribute4D4_B.setObjectName(u"lb_attribute4D4_B")
        self.lb_attribute4D4_B.setGeometry(QRect(330, 0, 61, 31))
        self.lb_attribute4D4_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute2D4_B = QLabel(self.widget_attributeSetD4_B)
        self.lb_attribute2D4_B.setObjectName(u"lb_attribute2D4_B")
        self.lb_attribute2D4_B.setGeometry(QRect(160, 0, 61, 41))
        
        self.grid_attributeSetD_B.addWidget(self.widget_attributeSetD4_B, 5, 0, 1, 1)
        
        self.gridLayout_12.addLayout(self.grid_attributeSetD_B, 1, 0, 1, 1)
        
        self.sa_attributeSetD_B.setWidget(self.SaWidgetContents_attributeSetD_B)
        
        self.sw_attributeSet_B.addWidget(self.page_D)
        
        # *********************************************************************attributeE*************************************************************************#
        # *********************************************************************attributeE*************************************************************************#
        # *********************************************************************attributeE*************************************************************************#
        
        self.page_E = QWidget()
        self.page_E.setObjectName(u"page_E")
        
        self.sa_attributeSetE_B = QScrollArea(self.page_E)
        self.sa_attributeSetE_B.setObjectName(u"sa_attributeSetE_B")
        self.sa_attributeSetE_B.setGeometry(QRect(0, 0, 441, 261))
        self.sa_attributeSetE_B.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.sa_attributeSetE_B.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sa_attributeSetE_B.setWidgetResizable(True)
        self.SaWidgetContents_attributeSetE_B = QWidget()
        self.SaWidgetContents_attributeSetE_B.setObjectName(u"SaWidgetContents_attributeSetE_B")
        self.SaWidgetContents_attributeSetE_B.setGeometry(QRect(0, 0, 431, 399))
        self.SaWidgetContents_attributeSetE_B.setMinimumSize(QSize(431, 399))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.SaWidgetContents_attributeSetE_B.setPalette(palette4)
        
        self.gridLayout_13 = QGridLayout(self.SaWidgetContents_attributeSetE_B)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        
        self.grid_attributeSetE_B = QGridLayout()
        self.grid_attributeSetE_B.setObjectName(u"grid_attributeSetE_B")
        self.widget_attributeSetE2_B = QWidget(self.SaWidgetContents_attributeSetE_B)
        self.widget_attributeSetE2_B.setObjectName(u"widget_attributeSetE2_B")
        self.widget_attributeSetE2_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0E2_B = QLabel(self.widget_attributeSetE2_B)
        self.lb_attributeNum0E2_B.setObjectName(u"lb_attributeNum0E2_B")
        self.lb_attributeNum0E2_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0E2_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1E2_B = QLabel(self.widget_attributeSetE2_B)
        self.lb_attribute1E2_B.setObjectName(u"lb_attribute1E2_B")
        self.lb_attribute1E2_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1E2_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2E2_B = QLabel(self.widget_attributeSetE2_B)
        self.lb_attribute2E2_B.setObjectName(u"lb_attribute2E2_B")
        self.lb_attribute2E2_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3E2_B = QPushButton(self.widget_attributeSetE2_B)
        self.pb_attribute3E2_B.setObjectName(u"pb_attribute3E2_B")
        self.pb_attribute3E2_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3E2_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4E2_B = QLabel(self.widget_attributeSetE2_B)
        self.lb_attribute4E2_B.setObjectName(u"lb_attribute4E2_B")
        self.lb_attribute4E2_B.setGeometry(QRect(320, 0, 81, 31))
        self.lb_attribute4E2_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetE_B.addWidget(self.widget_attributeSetE2_B, 3, 0, 1, 1)
        
        self.widget_attributeSetE4_B = QWidget(self.SaWidgetContents_attributeSetE_B)
        self.widget_attributeSetE4_B.setObjectName(u"widget_attributeSetE4_B")
        self.widget_attributeSetE4_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0E4_B = QLabel(self.widget_attributeSetE4_B)
        self.lb_attributeNum0E4_B.setObjectName(u"lb_attributeNum0E4_B")
        self.lb_attributeNum0E4_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0E4_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1E4_B = QLabel(self.widget_attributeSetE4_B)
        self.lb_attribute1E4_B.setObjectName(u"lb_attribute1E4_B")
        self.lb_attribute1E4_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1E4_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.pb_attribute3E4_B = QPushButton(self.widget_attributeSetE4_B)
        self.pb_attribute3E4_B.setObjectName(u"pb_attribute3E4_B")
        self.pb_attribute3E4_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3E4_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4E4_B = QLabel(self.widget_attributeSetE4_B)
        self.lb_attribute4E4_B.setObjectName(u"lb_attribute4E4_B")
        self.lb_attribute4E4_B.setGeometry(QRect(310, 0, 91, 31))
        self.lb_attribute4E4_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute2E4_B = QLabel(self.widget_attributeSetE4_B)
        self.lb_attribute2E4_B.setObjectName(u"lb_attribute2E4_B")
        self.lb_attribute2E4_B.setGeometry(QRect(160, 0, 61, 41))
        
        self.grid_attributeSetE_B.addWidget(self.widget_attributeSetE4_B, 5, 0, 1, 1)
        
        self.widget_attributeSetE1_B = QWidget(self.SaWidgetContents_attributeSetE_B)
        self.widget_attributeSetE1_B.setObjectName(u"widget_attributeSetE1_B")
        self.widget_attributeSetE1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0E1_B = QLabel(self.widget_attributeSetE1_B)
        self.lb_attributeNum0E1_B.setObjectName(u"lb_attributeNum0E1_B")
        self.lb_attributeNum0E1_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0E1_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1E1_B = QLabel(self.widget_attributeSetE1_B)
        self.lb_attribute1E1_B.setObjectName(u"lb_attribute1E1_B")
        self.lb_attribute1E1_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1E1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2E1_B = QLabel(self.widget_attributeSetE1_B)
        self.lb_attribute2E1_B.setObjectName(u"lb_attribute2E1_B")
        self.lb_attribute2E1_B.setGeometry(QRect(160, 10, 54, 12))
        self.pb_attribute3E1_B = QPushButton(self.widget_attributeSetE1_B)
        self.pb_attribute3E1_B.setObjectName(u"pb_attribute3E1_B")
        self.pb_attribute3E1_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3E1_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4E1_B = QLabel(self.widget_attributeSetE1_B)
        self.lb_attribute4E1_B.setObjectName(u"lb_attribute4E1_B")
        self.lb_attribute4E1_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4E1_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetE_B.addWidget(self.widget_attributeSetE1_B, 2, 0, 1, 1)
        
        self.widget_attributeSetE5_B = QWidget(self.SaWidgetContents_attributeSetE_B)
        self.widget_attributeSetE5_B.setObjectName(u"widget_attributeSetE5_B")
        self.widget_attributeSetE5_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0E5_B = QLabel(self.widget_attributeSetE5_B)
        self.lb_attributeNum0E5_B.setObjectName(u"lb_attributeNum0E5_B")
        self.lb_attributeNum0E5_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0E5_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1E5_B = QLabel(self.widget_attributeSetE5_B)
        self.lb_attribute1E5_B.setObjectName(u"lb_attribute1E5_B")
        self.lb_attribute1E5_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1E5_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.pb_attribute3E5_B = QPushButton(self.widget_attributeSetE5_B)
        self.pb_attribute3E5_B.setObjectName(u"pb_attribute3E5_B")
        self.pb_attribute3E5_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3E5_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4E5_B = QLabel(self.widget_attributeSetE5_B)
        self.lb_attribute4E5_B.setObjectName(u"lb_attribute4E5_B")
        self.lb_attribute4E5_B.setGeometry(QRect(330, 0, 51, 31))
        self.lb_attribute4E5_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute2E5_B = QLabel(self.widget_attributeSetE5_B)
        self.lb_attribute2E5_B.setObjectName(u"lb_attribute2E5_B")
        self.lb_attribute2E5_B.setGeometry(QRect(160, 0, 61, 41))
        
        self.grid_attributeSetE_B.addWidget(self.widget_attributeSetE5_B, 6, 0, 1, 1)
        
        self.widget_attributeSetE3_B = QWidget(self.SaWidgetContents_attributeSetE_B)
        self.widget_attributeSetE3_B.setObjectName(u"widget_attributeSetE3_B")
        self.widget_attributeSetE3_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0E3_B = QLabel(self.widget_attributeSetE3_B)
        self.lb_attributeNum0E3_B.setObjectName(u"lb_attributeNum0E3_B")
        self.lb_attributeNum0E3_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0E3_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1E3_B = QLabel(self.widget_attributeSetE3_B)
        self.lb_attribute1E3_B.setObjectName(u"lb_attribute1E3_B")
        self.lb_attribute1E3_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1E3_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2E3_B = QLabel(self.widget_attributeSetE3_B)
        self.lb_attribute2E3_B.setObjectName(u"lb_attribute2E3_B")
        self.lb_attribute2E3_B.setGeometry(QRect(160, 0, 61, 41))
        
        self.pb_attribute3E3_B = QPushButton(self.widget_attributeSetE3_B)
        self.pb_attribute3E3_B.setObjectName(u"pb_attribute3E3_B")
        self.pb_attribute3E3_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3E3_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4E3_B = QLabel(self.widget_attributeSetE3_B)
        self.lb_attribute4E3_B.setObjectName(u"lb_attribute4E3_B")
        self.lb_attribute4E3_B.setGeometry(QRect(330, 0, 61, 31))
        self.lb_attribute4E3_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetE_B.addWidget(self.widget_attributeSetE3_B, 4, 0, 1, 1)
        
        self.pb_attributeSetSignE_B = QLabel(self.SaWidgetContents_attributeSetE_B)
        self.pb_attributeSetSignE_B.setObjectName(u"pb_attributeSetSignE_B")
        self.pb_attributeSetSignE_B.setPixmap(QPixmap(u"../image/B1/attribute/pb_attributeSign_B.png"))
        
        self.grid_attributeSetE_B.addWidget(self.pb_attributeSetSignE_B, 0, 0, 1, 1)
        
        self.widget_attributeSetE0_B = QWidget(self.SaWidgetContents_attributeSetE_B)
        self.widget_attributeSetE0_B.setObjectName(u"widget_attributeSetE0_B")
        self.widget_attributeSetE0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0E0_B = QLabel(self.widget_attributeSetE0_B)
        self.lb_attributeNum0E0_B.setObjectName(u"lb_attributeNum0E0_B")
        self.lb_attributeNum0E0_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0E0_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1E0_B = QLabel(self.widget_attributeSetE0_B)
        self.lb_attribute1E0_B.setObjectName(u"lb_attribute1E0_B")
        self.lb_attribute1E0_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1E0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2E0_B = QLabel(self.widget_attributeSetE0_B)
        self.lb_attribute2E0_B.setObjectName(u"lb_attribute2E0_B")
        self.lb_attribute2E0_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3E0_B = QPushButton(self.widget_attributeSetE0_B)
        self.pb_attribute3E0_B.setObjectName(u"pb_attribute3E0_B")
        self.pb_attribute3E0_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3E0_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4E0_B = QLabel(self.widget_attributeSetE0_B)
        self.lb_attribute4E0_B.setObjectName(u"lb_attribute4E0_B")
        self.lb_attribute4E0_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4E0_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetE_B.addWidget(self.widget_attributeSetE0_B, 1, 0, 1, 1)
        
        self.widget_attributeSetE6_B = QWidget(self.SaWidgetContents_attributeSetE_B)
        self.widget_attributeSetE6_B.setObjectName(u"widget_attributeSetE6_B")
        self.widget_attributeSetE6_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0E6_B = QLabel(self.widget_attributeSetE6_B)
        self.lb_attributeNum0E6_B.setObjectName(u"lb_attributeNum0E6_B")
        self.lb_attributeNum0E6_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0E6_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1E6_B = QLabel(self.widget_attributeSetE6_B)
        self.lb_attribute1E6_B.setObjectName(u"lb_attribute1E6_B")
        self.lb_attribute1E6_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1E6_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.pb_attribute3E6_B = QPushButton(self.widget_attributeSetE6_B)
        self.pb_attribute3E6_B.setObjectName(u"pb_attribute3E6_B")
        self.pb_attribute3E6_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3E6_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4E6_B = QLabel(self.widget_attributeSetE6_B)
        self.lb_attribute4E6_B.setObjectName(u"lb_attribute4E6_B")
        self.lb_attribute4E6_B.setGeometry(QRect(330, 0, 51, 31))
        self.lb_attribute4E6_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute2E6_B = QLabel(self.widget_attributeSetE6_B)
        self.lb_attribute2E6_B.setObjectName(u"lb_attribute2E6_B")
        self.lb_attribute2E6_B.setGeometry(QRect(160, 0, 61, 41))
        
        self.grid_attributeSetE_B.addWidget(self.widget_attributeSetE6_B, 7, 0, 1, 1)
        
        self.gridLayout_13.addLayout(self.grid_attributeSetE_B, 1, 0, 1, 1)
        
        self.sa_attributeSetE_B.setWidget(self.SaWidgetContents_attributeSetE_B)
        
        self.sw_attributeSet_B.addWidget(self.page_E)
        
        # *********************************************************************attributeF*************************************************************************#
        # *********************************************************************attributeF*************************************************************************#
        # *********************************************************************attributeF*************************************************************************#
        
        self.page_F = QWidget()
        self.page_F.setObjectName(u"page_F")
        
        self.sa_attributeSetF_B = QScrollArea(self.page_F)
        self.sa_attributeSetF_B.setObjectName(u"sa_attributeSetF_B")
        self.sa_attributeSetF_B.setGeometry(QRect(0, 0, 441, 261))
        self.sa_attributeSetF_B.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.sa_attributeSetF_B.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sa_attributeSetF_B.setWidgetResizable(True)
        self.SaWidgetContents_attributeSetF_B = QWidget()
        self.SaWidgetContents_attributeSetF_B.setObjectName(u"SaWidgetContents_attributeSetF_B")
        self.SaWidgetContents_attributeSetF_B.setGeometry(QRect(0, 0, 431, 399))
        self.SaWidgetContents_attributeSetF_B.setMinimumSize(QSize(431, 399))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.SaWidgetContents_attributeSetF_B.setPalette(palette5)
        
        self.gridLayout_14 = QGridLayout(self.SaWidgetContents_attributeSetF_B)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        
        self.grid_attributeSetF_B = QGridLayout()
        self.grid_attributeSetF_B.setObjectName(u"grid_attributeSetF_B")
        
        self.widget_attributeSeF2_B = QWidget(self.SaWidgetContents_attributeSetF_B)
        self.widget_attributeSeF2_B.setObjectName(u"widget_attributeSeF2_B")
        self.widget_attributeSeF2_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0F2_B = QLabel(self.widget_attributeSeF2_B)
        self.lb_attributeNum0F2_B.setObjectName(u"lb_attributeNum0F2_B")
        self.lb_attributeNum0F2_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0F2_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1F2_B = QLabel(self.widget_attributeSeF2_B)
        self.lb_attribute1F2_B.setObjectName(u"lb_attribute1F2_B")
        self.lb_attribute1F2_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1F2_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2F2_B = QLabel(self.widget_attributeSeF2_B)
        self.lb_attribute2F2_B.setObjectName(u"lb_attribute2F2_B")
        self.lb_attribute2F2_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3F2_B = QPushButton(self.widget_attributeSeF2_B)
        self.pb_attribute3F2_B.setObjectName(u"pb_attribute3F2_B")
        self.pb_attribute3F2_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3F2_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4F2_B = QLabel(self.widget_attributeSeF2_B)
        self.lb_attribute4F2_B.setObjectName(u"lb_attribute4F2_B")
        self.lb_attribute4F2_B.setGeometry(QRect(320, 0, 81, 31))
        self.lb_attribute4F2_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetF_B.addWidget(self.widget_attributeSeF2_B, 3, 0, 1, 1)
        
        self.widget_attributeSetF4_B = QWidget(self.SaWidgetContents_attributeSetF_B)
        self.widget_attributeSetF4_B.setObjectName(u"widget_attributeSetF4_B")
        self.widget_attributeSetF4_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0F4_B = QLabel(self.widget_attributeSetF4_B)
        self.lb_attributeNum0F4_B.setObjectName(u"lb_attributeNum0F4_B")
        self.lb_attributeNum0F4_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0F4_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1F4_B = QLabel(self.widget_attributeSetF4_B)
        self.lb_attribute1F4_B.setObjectName(u"lb_attribute1F4_B")
        self.lb_attribute1F4_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1F4_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.pb_attribute3F4_B = QPushButton(self.widget_attributeSetF4_B)
        self.pb_attribute3F4_B.setObjectName(u"pb_attribute3F4_B")
        self.pb_attribute3F4_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3F4_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4F4_B = QLabel(self.widget_attributeSetF4_B)
        self.lb_attribute4F4_B.setObjectName(u"lb_attribute4F4_B")
        self.lb_attribute4F4_B.setGeometry(QRect(310, 0, 91, 31))
        self.lb_attribute4F4_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute2F4_B = QLabel(self.widget_attributeSetF4_B)
        self.lb_attribute2F4_B.setObjectName(u"lb_attribute2F4_B")
        self.lb_attribute2F4_B.setGeometry(QRect(160, 0, 61, 41))
        
        self.grid_attributeSetF_B.addWidget(self.widget_attributeSetF4_B, 5, 0, 1, 1)
        
        self.widget_attributeSetF1_B = QWidget(self.SaWidgetContents_attributeSetF_B)
        self.widget_attributeSetF1_B.setObjectName(u"widget_attributeSetF1_B")
        self.widget_attributeSetF1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0F1_B = QLabel(self.widget_attributeSetF1_B)
        self.lb_attributeNum0F1_B.setObjectName(u"lb_attributeNum0F1_B")
        self.lb_attributeNum0F1_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0F1_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1F1_B = QLabel(self.widget_attributeSetF1_B)
        self.lb_attribute1F1_B.setObjectName(u"lb_attribute1F1_B")
        self.lb_attribute1F1_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1F1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2F1_B = QLabel(self.widget_attributeSetF1_B)
        self.lb_attribute2F1_B.setObjectName(u"lb_attribute2F1_B")
        self.lb_attribute2F1_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3F1_B = QPushButton(self.widget_attributeSetF1_B)
        self.pb_attribute3F1_B.setObjectName(u"pb_attribute3F1_B")
        self.pb_attribute3F1_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3F1_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4F1_B = QLabel(self.widget_attributeSetF1_B)
        self.lb_attribute4F1_B.setObjectName(u"lb_attribute4F1_B")
        self.lb_attribute4F1_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4F1_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetF_B.addWidget(self.widget_attributeSetF1_B, 2, 0, 1, 1)
        
        self.widget_attributeSetF5_B = QWidget(self.SaWidgetContents_attributeSetF_B)
        self.widget_attributeSetF5_B.setObjectName(u"widget_attributeSetF5_B")
        self.widget_attributeSetF5_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0F5_B = QLabel(self.widget_attributeSetF5_B)
        self.lb_attributeNum0F5_B.setObjectName(u"lb_attributeNum0F5_B")
        self.lb_attributeNum0F5_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0F5_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1F5_B = QLabel(self.widget_attributeSetF5_B)
        self.lb_attribute1F5_B.setObjectName(u"lb_attribute1F5_B")
        self.lb_attribute1F5_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1F5_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.pb_attribute3F5_B = QPushButton(self.widget_attributeSetF5_B)
        self.pb_attribute3F5_B.setObjectName(u"pb_attribute3F5_B")
        self.pb_attribute3F5_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3F5_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4F5_B = QLabel(self.widget_attributeSetF5_B)
        self.lb_attribute4F5_B.setObjectName(u"lb_attribute4F5_B")
        self.lb_attribute4F5_B.setGeometry(QRect(330, 0, 51, 31))
        self.lb_attribute4F5_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute2F5_B = QLabel(self.widget_attributeSetF5_B)
        self.lb_attribute2F5_B.setObjectName(u"lb_attribute2F5_B")
        self.lb_attribute2F5_B.setGeometry(QRect(160, 0, 61, 41))
        
        self.grid_attributeSetF_B.addWidget(self.widget_attributeSetF5_B, 6, 0, 1, 1)
        
        self.widget_attributeSetF3_B = QWidget(self.SaWidgetContents_attributeSetF_B)
        self.widget_attributeSetF3_B.setObjectName(u"widget_attributeSetF3_B")
        self.widget_attributeSetF3_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0F3_B = QLabel(self.widget_attributeSetF3_B)
        self.lb_attributeNum0F3_B.setObjectName(u"lb_attributeNum0F3_B")
        self.lb_attributeNum0F3_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0F3_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1F3_B = QLabel(self.widget_attributeSetF3_B)
        self.lb_attribute1F3_B.setObjectName(u"lb_attribute1F3_B")
        self.lb_attribute1F3_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1F3_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2F3_B = QLabel(self.widget_attributeSetF3_B)
        self.lb_attribute2F3_B.setObjectName(u"lb_attribute2F3_B")
        self.lb_attribute2F3_B.setGeometry(QRect(160, 0, 61, 41))
        
        self.pb_attribute3F3_B = QPushButton(self.widget_attributeSetF3_B)
        self.pb_attribute3F3_B.setObjectName(u"pb_attribute3F3_B")
        self.pb_attribute3F3_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3F3_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4F3_B = QLabel(self.widget_attributeSetF3_B)
        self.lb_attribute4F3_B.setObjectName(u"lb_attribute4F3_B")
        self.lb_attribute4F3_B.setGeometry(QRect(330, 0, 61, 31))
        self.lb_attribute4F3_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetF_B.addWidget(self.widget_attributeSetF3_B, 4, 0, 1, 1)
        
        self.widget_attributeSetF7_B = QWidget(self.SaWidgetContents_attributeSetF_B)
        self.widget_attributeSetF7_B.setObjectName(u"widget_attributeSetF7_B")
        self.widget_attributeSetF7_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0F7_B = QLabel(self.widget_attributeSetF7_B)
        self.lb_attributeNum0F7_B.setObjectName(u"lb_attributeNum0F7_B")
        self.lb_attributeNum0F7_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0F7_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1F7_B = QLabel(self.widget_attributeSetF7_B)
        self.lb_attribute1F7_B.setObjectName(u"lb_attribute1F7_B")
        self.lb_attribute1F7_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1F7_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2F7_B = QLabel(self.widget_attributeSetF7_B)
        self.lb_attribute2F7_B.setObjectName(u"lb_attribute2F7_B_2")
        self.lb_attribute2F7_B.setGeometry(QRect(160, 0, 61, 31))
        
        self.lb_attribute3F7_B = QPushButton(self.widget_attributeSetF7_B)
        self.lb_attribute3F7_B.setObjectName(u"lb_attribute3F7_B")
        self.lb_attribute3F7_B.setGeometry(QRect(240, 0, 71, 31))
        self.lb_attribute3F7_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4F7_B = QLabel(self.widget_attributeSetF7_B)
        self.lb_attribute4F7_B.setObjectName(u"lb_attribute4F7_B")
        self.lb_attribute4F7_B.setGeometry(QRect(330, 0, 61, 31))
        self.lb_attribute4F7_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetF_B.addWidget(self.widget_attributeSetF7_B, 8, 0, 1, 1)
        
        self.pb_attributeSetSignF_B = QLabel(self.SaWidgetContents_attributeSetF_B)
        self.pb_attributeSetSignF_B.setObjectName(u"pb_attributeSetSignF_B")
        self.pb_attributeSetSignF_B.setPixmap(QPixmap(u"../image/B1/attribute/pb_attributeSign_B.png"))
        
        self.grid_attributeSetF_B.addWidget(self.pb_attributeSetSignF_B, 0, 0, 1, 1)
        
        self.widget_attributeSetF0_B = QWidget(self.SaWidgetContents_attributeSetF_B)
        self.widget_attributeSetF0_B.setObjectName(u"widget_attributeSetF0_B")
        self.widget_attributeSetF0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0F0_B = QLabel(self.widget_attributeSetF0_B)
        self.lb_attributeNum0F0_B.setObjectName(u"lb_attributeNum0F0_B")
        self.lb_attributeNum0F0_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0F0_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1F0_B = QLabel(self.widget_attributeSetF0_B)
        self.lb_attribute1F0_B.setObjectName(u"lb_attribute1F0_B")
        self.lb_attribute1F0_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1F0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2F0_B = QLabel(self.widget_attributeSetF0_B)
        self.lb_attribute2F0_B.setObjectName(u"lb_attribute2F0_B")
        self.lb_attribute2F0_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3F0_B = QPushButton(self.widget_attributeSetF0_B)
        self.pb_attribute3F0_B.setObjectName(u"pb_attribute3F0_B")
        self.pb_attribute3F0_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3F0_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4F0_B = QLabel(self.widget_attributeSetF0_B)
        self.lb_attribute4F0_B.setObjectName(u"lb_attribute4F0_B")
        self.lb_attribute4F0_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4F0_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetF_B.addWidget(self.widget_attributeSetF0_B, 1, 0, 1, 1)
        
        self.widget_attributeSetF6_B = QWidget(self.SaWidgetContents_attributeSetF_B)
        self.widget_attributeSetF6_B.setObjectName(u"widget_attributeSetF6_B")
        self.widget_attributeSetF6_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0F6_B = QLabel(self.widget_attributeSetF6_B)
        self.lb_attributeNum0F6_B.setObjectName(u"lb_attributeNum0F6_B")
        self.lb_attributeNum0F6_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0F6_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1F6_B = QLabel(self.widget_attributeSetF6_B)
        self.lb_attribute1F6_B.setObjectName(u"lb_attribute1F6_B")
        self.lb_attribute1F6_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1F6_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.pb_attribute3F6_B = QPushButton(self.widget_attributeSetF6_B)
        self.pb_attribute3F6_B.setObjectName(u"pb_attribute3F6_B")
        self.pb_attribute3F6_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3F6_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4F6_B = QLabel(self.widget_attributeSetF6_B)
        self.lb_attribute4F6_B.setObjectName(u"lb_attribute4F6_B")
        self.lb_attribute4F6_B.setGeometry(QRect(330, 0, 51, 31))
        self.lb_attribute4F6_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute2F6_B = QLabel(self.widget_attributeSetF6_B)
        self.lb_attribute2F6_B.setObjectName(u"lb_attribute2F6_B")
        self.lb_attribute2F6_B.setGeometry(QRect(160, 0, 61, 41))
        
        self.grid_attributeSetF_B.addWidget(self.widget_attributeSetF6_B, 7, 0, 1, 1)
        
        self.gridLayout_14.addLayout(self.grid_attributeSetF_B, 1, 0, 1, 1)
        
        self.sa_attributeSetF_B.setWidget(self.SaWidgetContents_attributeSetF_B)
        
        self.sw_attributeSet_B.addWidget(self.page_F)
        
        # *********************************************************************attributeG*************************************************************************#
        # *********************************************************************attributeG*************************************************************************#
        # *********************************************************************attributeG*************************************************************************#
        
        self.page_G = QWidget()
        self.page_G.setObjectName(u"page_G")
        
        self.sa_attributeSetG_B = QScrollArea(self.page_G)
        self.sa_attributeSetG_B.setObjectName(u"sa_attributeSetG_B")
        self.sa_attributeSetG_B.setGeometry(QRect(0, 0, 441, 261))
        self.sa_attributeSetG_B.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.sa_attributeSetG_B.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sa_attributeSetG_B.setWidgetResizable(True)
        
        self.SaWidgetContents_attributeSetG_B = QWidget()
        self.SaWidgetContents_attributeSetG_B.setObjectName(u"SaWidgetContents_attributeSetG_B")
        self.SaWidgetContents_attributeSetG_B.setGeometry(QRect(0, 0, 431, 259))
        self.SaWidgetContents_attributeSetG_B.setMinimumSize(QSize(431, 200))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.SaWidgetContents_attributeSetG_B.setPalette(palette6)
        
        self.gridLayout_15 = QGridLayout(self.SaWidgetContents_attributeSetG_B)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        
        self.grid_attributeSetG_B = QGridLayout()
        self.grid_attributeSetG_B.setObjectName(u"grid_attributeSetG_B")
        
        self.widget_attributeSetG1_B = QWidget(self.SaWidgetContents_attributeSetG_B)
        self.widget_attributeSetG1_B.setObjectName(u"widget_attributeSetG1_B")
        self.widget_attributeSetG1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0G1_B = QLabel(self.widget_attributeSetG1_B)
        self.lb_attributeNum0G1_B.setObjectName(u"lb_attributeNum0G1_B")
        self.lb_attributeNum0G1_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0G1_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1G1_B = QLabel(self.widget_attributeSetG1_B)
        self.lb_attribute1G1_B.setObjectName(u"lb_attribute1G1_B")
        self.lb_attribute1G1_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1G1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2G1_B = QLabel(self.widget_attributeSetG1_B)
        self.lb_attribute2G1_B.setObjectName(u"lb_attribute2G1_B")
        self.lb_attribute2G1_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3G1_B = QPushButton(self.widget_attributeSetG1_B)
        self.pb_attribute3G1_B.setObjectName(u"pb_attribute3G1_B")
        self.pb_attribute3G1_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3G1_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4G1_B = QLabel(self.widget_attributeSetG1_B)
        self.lb_attribute4G1_B.setObjectName(u"lb_attribute4G1_B")
        self.lb_attribute4G1_B.setGeometry(QRect(320, 0, 81, 31))
        self.lb_attribute4G1_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetG_B.addWidget(self.widget_attributeSetG1_B, 2, 0, 1, 1)
        
        self.widget_attributeSetG2_B = QWidget(self.SaWidgetContents_attributeSetG_B)
        self.widget_attributeSetG2_B.setObjectName(u"widget_attributeSetG2_B")
        self.widget_attributeSetG2_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0G3_B = QLabel(self.widget_attributeSetG2_B)
        self.lb_attributeNum0G3_B.setObjectName(u"lb_attributeNum0G3_B")
        self.lb_attributeNum0G3_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0G3_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1G3_B = QLabel(self.widget_attributeSetG2_B)
        self.lb_attribute1G3_B.setObjectName(u"lb_attribute1G3_B")
        self.lb_attribute1G3_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1G3_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2G3_B = QLabel(self.widget_attributeSetG2_B)
        self.lb_attribute2G3_B.setObjectName(u"lb_attribute2G3_B")
        self.lb_attribute2G3_B.setGeometry(QRect(160, 0, 61, 41))
        
        self.pb_attribute3G3_B = QPushButton(self.widget_attributeSetG2_B)
        self.pb_attribute3G3_B.setObjectName(u"pb_attribute3G3_B")
        self.pb_attribute3G3_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3G3_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4G3_B = QLabel(self.widget_attributeSetG2_B)
        self.lb_attribute4G3_B.setObjectName(u"lb_attribute4G3_B")
        self.lb_attribute4G3_B.setGeometry(QRect(330, 0, 61, 31))
        self.lb_attribute4G3_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetG_B.addWidget(self.widget_attributeSetG2_B, 3, 0, 1, 1)
        
        self.pb_attributeSetSignG_B = QLabel(self.SaWidgetContents_attributeSetG_B)
        self.pb_attributeSetSignG_B.setObjectName(u"pb_attributeSetSignG_B")
        self.pb_attributeSetSignG_B.setPixmap(QPixmap(u"../image/B1/attribute/pb_attributeSign_B.png"))
        
        self.grid_attributeSetG_B.addWidget(self.pb_attributeSetSignG_B, 0, 0, 1, 1)
        
        self.widget_attributeSetG0_B = QWidget(self.SaWidgetContents_attributeSetG_B)
        self.widget_attributeSetG0_B.setObjectName(u"widget_attributeSetG0_B")
        self.widget_attributeSetG0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0G0_B = QLabel(self.widget_attributeSetG0_B)
        self.lb_attributeNum0G0_B.setObjectName(u"lb_attributeNum0G0_B")
        self.lb_attributeNum0G0_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0G0_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1G0_B = QLabel(self.widget_attributeSetG0_B)
        self.lb_attribute1G0_B.setObjectName(u"lb_attribute1G0_B")
        self.lb_attribute1G0_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1G0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2G0_B = QLabel(self.widget_attributeSetG0_B)
        self.lb_attribute2G0_B.setObjectName(u"lb_attribute2G0_B")
        self.lb_attribute2G0_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3G0_B = QPushButton(self.widget_attributeSetG0_B)
        self.pb_attribute3G0_B.setObjectName(u"pb_attribute3G0_B")
        self.pb_attribute3G0_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3G0_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4G0_B = QLabel(self.widget_attributeSetG0_B)
        self.lb_attribute4G0_B.setObjectName(u"lb_attribute4G0_B")
        self.lb_attribute4G0_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4G0_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetG_B.addWidget(self.widget_attributeSetG0_B, 1, 0, 1, 1)
        
        self.gridLayout_15.addLayout(self.grid_attributeSetG_B, 1, 0, 1, 1)
        
        self.sa_attributeSetG_B.setWidget(self.SaWidgetContents_attributeSetG_B)
        
        self.sw_attributeSet_B.addWidget(self.page_G)
        
        # *********************************************************************attributeH*************************************************************************#
        # *********************************************************************attributeH*************************************************************************#
        # *********************************************************************attributeH*************************************************************************#
        
        self.page_H = QWidget()
        self.page_H.setObjectName(u"page_H")
        
        self.sa_attributeSetH_B = QScrollArea(self.page_H)
        self.sa_attributeSetH_B.setObjectName(u"sa_attributeSetH_B")
        self.sa_attributeSetH_B.setGeometry(QRect(0, 0, 441, 261))
        self.sa_attributeSetH_B.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.sa_attributeSetH_B.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sa_attributeSetH_B.setWidgetResizable(True)
        
        self.SaWidgetContents_attributeSetH_B = QWidget()
        self.SaWidgetContents_attributeSetH_B.setObjectName(u"SaWidgetContents_attributeSetH_B")
        self.SaWidgetContents_attributeSetH_B.setGeometry(QRect(0, 0, 431, 259))
        self.SaWidgetContents_attributeSetH_B.setMinimumSize(QSize(431, 100))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.SaWidgetContents_attributeSetH_B.setPalette(palette7)
        
        self.gridLayout_16 = QGridLayout(self.SaWidgetContents_attributeSetH_B)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        
        self.grid_attributeSetH_B = QGridLayout()
        self.grid_attributeSetH_B.setObjectName(u"grid_attributeSetH_B")
        
        self.widget_attributeSetH1_B = QWidget(self.SaWidgetContents_attributeSetH_B)
        self.widget_attributeSetH1_B.setObjectName(u"widget_attributeSetH1_B")
        self.widget_attributeSetH1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0H1_B = QLabel(self.widget_attributeSetH1_B)
        self.lb_attributeNum0H1_B.setObjectName(u"lb_attributeNum0H1_B")
        self.lb_attributeNum0H1_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0H1_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1H1_B = QLabel(self.widget_attributeSetH1_B)
        self.lb_attribute1H1_B.setObjectName(u"lb_attribute1H1_B")
        self.lb_attribute1H1_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1H1_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2H1_B = QLabel(self.widget_attributeSetH1_B)
        self.lb_attribute2H1_B.setObjectName(u"lb_attribute2H1_B")
        self.lb_attribute2H1_B.setGeometry(QRect(153, 10, 61, 31))
        
        self.pb_attribute3H1_B = QPushButton(self.widget_attributeSetH1_B)
        self.pb_attribute3H1_B.setObjectName(u"pb_attribute3H1_B")
        self.pb_attribute3H1_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3H1_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4H1_B = QLabel(self.widget_attributeSetH1_B)
        self.lb_attribute4H1_B.setObjectName(u"lb_attribute4H1_B")
        self.lb_attribute4H1_B.setGeometry(QRect(320, 0, 81, 31))
        self.lb_attribute4H1_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetH_B.addWidget(self.widget_attributeSetH1_B, 2, 0, 1, 1)
        
        self.pb_attributeSetSignH_B = QLabel(self.SaWidgetContents_attributeSetH_B)
        self.pb_attributeSetSignH_B.setObjectName(u"pb_attributeSetSignH_B")
        self.pb_attributeSetSignH_B.setPixmap(QPixmap(u"../image/B1/attribute/pb_attributeSign_B.png"))
        
        self.grid_attributeSetH_B.addWidget(self.pb_attributeSetSignH_B, 0, 0, 1, 1)
        
        self.widget_attributeSetH0_B = QWidget(self.SaWidgetContents_attributeSetH_B)
        self.widget_attributeSetH0_B.setObjectName(u"widget_attributeSetH0_B")
        self.widget_attributeSetH0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attributeNum0H0_B = QLabel(self.widget_attributeSetH0_B)
        self.lb_attributeNum0H0_B.setObjectName(u"lb_attributeNum0H0_B")
        self.lb_attributeNum0H0_B.setGeometry(QRect(10, 0, 21, 31))
        self.lb_attributeNum0H0_B.setStyleSheet(u"font: 75 18pt \"\u5b8b\u4f53\";")
        
        self.lb_attribute1H0_B = QLabel(self.widget_attributeSetH0_B)
        self.lb_attribute1H0_B.setObjectName(u"lb_attribute1H0_B")
        self.lb_attribute1H0_B.setGeometry(QRect(70, 0, 61, 31))
        self.lb_attribute1H0_B.setStyleSheet(u"font: 75 10pt \"Aharoni\";")
        
        self.lb_attribute2H0_B = QLabel(self.widget_attributeSetH0_B)
        self.lb_attribute2H0_B.setObjectName(u"lb_attribute2H0_B")
        self.lb_attribute2H0_B.setGeometry(QRect(160, 10, 54, 12))
        
        self.pb_attribute3H0_B = QPushButton(self.widget_attributeSetH0_B)
        self.pb_attribute3H0_B.setObjectName(u"pb_attribute3H0_B")
        self.pb_attribute3H0_B.setGeometry(QRect(240, 0, 71, 31))
        self.pb_attribute3H0_B.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_attribute4H0_B = QLabel(self.widget_attributeSetH0_B)
        self.lb_attribute4H0_B.setObjectName(u"lb_attribute4H0_B")
        self.lb_attribute4H0_B.setGeometry(QRect(340, 0, 41, 31))
        self.lb_attribute4H0_B.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.grid_attributeSetH_B.addWidget(self.widget_attributeSetH0_B, 1, 0, 1, 1)
        
        self.gridLayout_16.addLayout(self.grid_attributeSetH_B, 1, 0, 1, 1)
        
        self.sa_attributeSetH_B.setWidget(self.SaWidgetContents_attributeSetH_B)
        
        self.sw_attributeSet_B.addWidget(self.page_H)
        
        self.sw_attribute_B.addWidget(self.page_attribute_flow_B)
        
        #####################################################Attribute##############################################
        #####################################################Attribute##############################################
        #####################################################Attribute##############################################
        
        self.page_attribute_edit_B = QWidget()
        self.page_attribute_edit_B.setObjectName(u"page_attribute_edit_B")
        # 用于存放流程图模式的内容
        
        self.lb_attribute_edit_background_B = QLabel(self.page_attribute_edit_B)
        self.lb_attribute_edit_background_B.setObjectName(u"lb_attribute_edit_background_B")
        self.lb_attribute_edit_background_B.setGeometry(QRect(0, 0, 560, 730))  # 0, 0, 560, 720
        self.lb_attribute_edit_background_B.setStyleSheet(u"background-color: rgb(45, 43, 53);")
        # 背景，相当于分割各个部分的框
        
        self.lb_attribute_edit_titleFlowI_B = QLabel(self.page_attribute_edit_B)
        self.lb_attribute_edit_titleFlowI_B.setObjectName(u"lb_attribute_edit_titleFlowI_B")
        self.lb_attribute_edit_titleFlowI_B.setGeometry(QRect(0, 0, 201, 51))
        self.lb_attribute_edit_titleFlowI_B.setStyleSheet(u"background-color:rgb(20, 20, 24);\n"
                                                          "font: 75 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
                                                          "color:rgb(255, 255, 255);")
        # "窗口属性："label
        
        self.lb_attribute_edit_titleFlowII_B = QLabel(self.page_attribute_edit_B)
        self.lb_attribute_edit_titleFlowII_B.setObjectName(u"lb_attribute_edit_titleFlowII_B")
        self.lb_attribute_edit_titleFlowII_B.setGeometry(QRect(0, 160, 201, 51))
        self.lb_attribute_edit_titleFlowII_B.setStyleSheet(u"background-color:rgb(20, 20, 24);\n"
                                                           "font: 75 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
                                                           "color:rgb(255, 255, 255);")
        # 控件参数label
        # self.lb_windowSignal_B = QLabel(self.page_attribute_edit_B)
        # self.lb_windowSignal_B.setObjectName(u"lb_windowSignal_B")
        # self.lb_windowSignal_B.setGeometry(QRect(70, 140, 131, 21))
        # self.lb_windowSignal_B.setStyleSheet(u"font: 75 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # "编号布局示意："label
        "被lb_chart代替，具体内容以后再编写"
        
        # self.pb_mapUp_B = QPushButton(self.page_attribute_edit_B)
        # self.pb_mapUp_B.setObjectName(u"pb_mapUp_B")
        # self.pb_mapUp_B.setGeometry(QRect(360, 130, 91, 31))
        # self.pb_mapUp_B.setStyleSheet(u"font: 75 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # "图片上传"按钮
        
        # self.lb_attributeMap11_B = QLabel(self.page_attribute_edit_B)
        # self.lb_attributeMap11_B.setObjectName(u"lb_attributeMap11_B")
        # self.lb_attributeMap11_B.setGeometry(QRect(60, 170, 431, 211))
        # self.lb_attributeMap11_B.setMaximumSize(QSize(16777214, 16777215))
        # self.lb_attributeMap11_B.setPixmap(QPixmap(u"../image/B1/attribute/lb_attributeMap11_B.png"))
        # 编号布局示意的图片，11表示按索引排位page_attribute2_B索引应为1，而这是page_attribute2_B里的第一个pixmap，所以编号11
        
        # self.lb_windowShow_B = QLabel(self.page_attribute_edit_B)
        # self.lb_windowShow_B.setObjectName(u"lb_windowShow_B")
        # self.lb_windowShow_B.setGeometry(QRect(80, 430, 91, 21))
        # self.lb_windowShow_B.setStyleSheet(u"font: 75 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # “布局展示：”label
        
        # self.lb_attributeMap12_B = QLabel(self.page_attribute_edit_B)
        # self.lb_attributeMap12_B.setObjectName(u"lb_attributeMap12_B")
        # self.lb_attributeMap12_B.setGeometry(QRect(60, 470, 431, 211))
        # self.lb_attributeMap12_B.setMaximumSize(QSize(16777214, 16777215))
        # self.lb_attributeMap12_B.setPixmap(QPixmap(u"../image/B1/attribute/lb_attributeMap11_B.png"))
        # 编号布局示意的图片，12表示按索引排位page_attribute2_B索引应为1，而这是page_attribute2_B里的第二个pixmap，所以编号12
        
        self.le_attribute_edit_nameI_B = QLineEdit(self.page_attribute_edit_B)
        self.le_attribute_edit_nameI_B.setObjectName(u"le_attribute_edit_nameI_B")
        self.le_attribute_edit_nameI_B.setGeometry(QRect(270, 100, 113, 20))
        # 输入框：窗口名称（注释）
        
        self.lb_attribute_edit_nameI_B = QLabel(self.page_attribute_edit_B)
        self.lb_attribute_edit_nameI_B.setObjectName(u"lb_attribute_edit_nameI_B")
        self.lb_attribute_edit_nameI_B.setGeometry(QRect(50, 90, 201, 31))
        self.lb_attribute_edit_nameI_B.setStyleSheet(u"font: 18pt \"\u5b8b\u4f53\";color:rgb(255, 255, 255);")
        # “窗口名称（注释）：”label
        
        self.lb_attribute_edit_numI_B = QLabel(self.page_attribute_edit_B)
        self.lb_attribute_edit_numI_B.setObjectName(u"lb_attribute_edit_numI_B")
        self.lb_attribute_edit_numI_B.setGeometry(QRect(260, 60, 111, 31))
        self.lb_attribute_edit_numI_B.setStyleSheet(u"font: 18pt \"\u5b8b\u4f53\";color:rgb(255, 255, 255);")
        # "窗口编号："
        
        self.cb_attribute_editI_B = QComboBox(self.page_attribute_edit_B)
        self.cb_attribute_editI_B.setObjectName(u"cb_attribute_editI_B")
        self.cb_attribute_editI_B.setGeometry(QRect(160, 65, 69, 22))
        # "窗口类型："的下拉框
        
        self.lb_attribute_edit_typeI_B = QLabel(self.page_attribute_edit_B)
        self.lb_attribute_edit_typeI_B.setObjectName(u"lb_attribute_edit_typeI_B")
        self.lb_attribute_edit_typeI_B.setGeometry(QRect(50, 60, 111, 31))
        self.lb_attribute_edit_typeI_B.setStyleSheet(u"font: 18pt \"\u5b8b\u4f53\";\n"
                                                     "color:rgb(255, 255, 255);")
        # 窗口类型的label
        
        self.sw_attribute_edit_II_B = QStackedWidget(self.page_attribute_edit_B)
        self.sw_attribute_edit_II_B.setObjectName(u"sw_attribute_edit_II_B")
        self.sw_attribute_edit_II_B.setGeometry(QRect(0, 210, 561, 511))
        
        self.page_attribute_edit_II1_B = QWidget()
        self.page_attribute_edit_II1_B.setObjectName(u"page_attribute_edit_II1_B")
        
        self.sw_attribute_edit_II_B.addWidget(self.page_attribute_edit_II1_B)
        
        self.page_attribute_edit_II2_B = QWidget()
        self.page_attribute_edit_II2_B.setObjectName(u"page_attribute_edit_II2_B")
        
        self.sw_attribute_edit_II_B.addWidget(self.page_attribute_edit_II2_B)
        # 右侧的控件参数部分
        
        self.sw_attribute_B.addWidget(self.page_attribute_edit_B)
        
        self.gridLayout_attribute_B.addWidget(self.sw_attribute_B, 0, 0, 1, 1)
        
        self.gridLayout_B.addWidget(self.widget_B, 0, 0, 1, 1)
        
        #####################################################introduce##############################################
        #####################################################introduce##############################################
        #####################################################introduce##############################################
        
        self.gridLayoutWidget_5 = QWidget(Form)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 730, 1441, 111))
        
        self.gridLayout_introduce_B = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_introduce_B.setObjectName(u"gridLayout_introduce_B")
        self.gridLayout_introduce_B.setContentsMargins(0, 0, 0, 0)
        # 底边的布局，用于展示email，爱发电，B站等制作组信息
        
        self.widget_introduce_B = QWidget(self.gridLayoutWidget_5)
        self.widget_introduce_B.setObjectName(u"widget_introduce_B")
        # 被gridLayout_introduce_B包裹，用于内部控件的摆放自由
        
        self.lb_introduce_background_B = QLabel(self.widget_introduce_B)
        self.lb_introduce_background_B.setObjectName(u"lb_introduce_background_B")
        self.lb_introduce_background_B.setGeometry(QRect(0, 0, 1441, 151))
        self.lb_introduce_background_B.setStyleSheet(u"background-color: rgb(23, 22, 27);")
        # 背景板
        
        self.lb_introduce_studio_B = QLabel(self.widget_introduce_B)
        self.lb_introduce_studio_B.setObjectName(u"lb_introduce_studio_B")
        self.lb_introduce_studio_B.setGeometry(QRect(1190, 70, 231, 31))
        self.lb_introduce_studio_B.setStyleSheet(
            u"font: 75 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";color:rgb(102, 181, 220);")
        # 工作室名称
        
        self.lb_introduce_Maker_B = QLabel(self.widget_introduce_B)
        self.lb_introduce_Maker_B.setObjectName(u"lb_introduce_Maker_B")
        self.lb_introduce_Maker_B.setGeometry(QRect(0, 0, 181, 31))
        self.lb_introduce_Maker_B.setStyleSheet(u"font: 75 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";color:rgb(102, 181, 220);")
        # 制作者名称
        
        self.lb_introduce_biliURL_B = QLabel(self.widget_introduce_B)
        self.lb_introduce_biliURL_B.setObjectName(u"lb_introduce_biliURL_B")
        self.lb_introduce_biliURL_B.setGeometry(QRect(12, 70, 821, 31))
        self.lb_introduce_biliURL_B.setStyleSheet(u"font: 75 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
                                                  "color: rgb(87, 69, 186);")
        # bilibili官号链接
        
        self.lb_introduce_email_B = QLabel(self.widget_introduce_B)
        self.lb_introduce_email_B.setObjectName(u"lb_introduce_email_B")
        self.lb_introduce_email_B.setGeometry(QRect(12, 35, 281, 31))
        self.lb_introduce_email_B.setStyleSheet(
            u"font: 75 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n""color: rgb(87, 69, 186);")
        # 邮箱号码
        
        self.gridLayout_introduce_B.addWidget(self.widget_introduce_B, 0, 0, 1, 1)
        
        self.sw_show_B.setCurrentIndex(0)
        # self.sw_attribute_B.setCurrentWidget(self.lb_attribute_flow_mapII_B)
        self.sw_attribute_B.setCurrentIndex(0)
        self.sw_attributeSet_B.setCurrentIndex(3)
        
        ###########################################################################(BBBBBBBBBBBBBBBBBBBBBBBBBBBB)#####################################################
        
        ###########################################################################(AAAAAAAAAAAAAAAAAAAAAAAAAAAA)#####################################################
        self.gridLayoutWidget_6 = QWidget(self.page_main_A)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget_6.setGeometry(QRect(0, 0, 1441, 861))
        
        self.gridLayout_A = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_A.setObjectName(u"gridLayout_A")
        self.gridLayout_A.setContentsMargins(0, 0, 0, 0)
        # 包裹整个A0（welcome）窗口的grid布局
        
        self.widget_A = QWidget(self.gridLayoutWidget_6)
        self.widget_A.setObjectName(u"widget_A")
        # 包裹整个A0（welcome）窗口的widget布局，为了使控件位置摆放自由
        
        self.lb_trademark_A = QLabel(self.widget_A)
        self.lb_trademark_A.setObjectName(u"lb_trademark_A")
        self.lb_trademark_A.setGeometry(QRect(1050, 510, 401, 401))
        self.lb_trademark_A.setPixmap(QPixmap(u":/old/A0(welcome)/lb_trademark_A.png"))
        self.lb_trademark_A.setScaledContents(True)
        # TG工作室的标志
        
        self.lb_background_A = QLabel(self.widget_A)
        self.lb_background_A.setObjectName(u"lb_background_A")
        self.lb_background_A.setGeometry(QRect(0, 0, 1440, 900))
        self.lb_background_A.setPixmap(
            QPixmap(u"../images/A0(welcome)/lb_background_A.png"))
        self.lb_background_A.setScaledContents(True)
        # 背景
        
        self.lb_note1_A = QLabel(self.widget_A)
        self.lb_note1_A.setObjectName(u"lb_note1_A")
        self.lb_note1_A.setGeometry(QRect(1320, 800, 91, 31))
        self.lb_note1_A.setPixmap(QPixmap(u":/old/A0(welcome)/lb_note1_A.png"))
        # "made by"的label
        
        self.lb_title_A = QLabel(self.widget_A)
        self.lb_title_A.setObjectName(u"lb_title_A")
        self.lb_title_A.setGeometry(QRect(60, 20, 491, 161))
        self.lb_title_A.setPixmap(QPixmap(u":/old/A0(welcome)/lb_title_A.png"))
        # 标题
        
        self.pb_create_A = QPushButton(self.widget_A)
        self.pb_create_A.setObjectName(u"pb_create_A")
        self.pb_create_A.setGeometry(QRect(180, 250, 191, 81))
        icon = QIcon()
        icon.addFile(u":/old/A0(welcome)/pb_create_A.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_create_A.setIcon(icon)
        self.pb_create_A.setIconSize(QSize(191, 81))
        # 创作按钮
        
        self.pb_dictionary_A = QPushButton(self.widget_A)
        self.pb_dictionary_A.setObjectName(u"pb_dictionary_A")
        self.pb_dictionary_A.setGeometry(QRect(180, 350, 191, 81))
        icon1 = QIcon()
        icon1.addFile(u":/old/A0(welcome)/pb_dictionary_A.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_dictionary_A.setIcon(icon1)
        self.pb_dictionary_A.setIconSize(QSize(191, 81))
        # 文档按钮
        
        self.pb_about_A = QPushButton(self.widget_A)
        self.pb_about_A.setObjectName(u"pb_about_A")
        self.pb_about_A.setGeometry(QRect(180, 450, 191, 81))
        icon2 = QIcon()
        icon2.addFile(u":/old/A0(welcome)/pb_about_A.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_about_A.setIcon(icon2)
        self.pb_about_A.setIconSize(QSize(191, 81))
        # 关于按钮
        "PS:*这里icon和UI生成的有出入"
        
        self.pb_set_A = QPushButton(self.widget_A)
        self.pb_set_A.setObjectName(u"pb_set_A")
        self.pb_set_A.setGeometry(QRect(180, 550, 191, 81))
        icon3 = QIcon()
        icon3.addFile(u":/old/A0(welcome)/pb_set_A.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_set_A.setIcon(icon3)
        self.pb_set_A.setIconSize(QSize(191, 81))
        # 设置按钮
        
        self.lb_background_A.raise_()
        self.lb_trademark_A.raise_()
        self.lb_title_A.raise_()
        self.lb_note1_A.raise_()
        self.pb_create_A.raise_()
        self.pb_dictionary_A.raise_()
        self.pb_about_A.raise_()
        self.pb_set_A.raise_()
        
        self.gridLayout_A.addWidget(self.widget_A, 0, 0, 1, 1)
        self.sw_main.addWidget(self.page_main_A)
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
    
    
    ###########################################################################(AAAAAAAAAAAAAAAAAAAAAAAAAAAA)#####################################################
    
    def retranslateUi(self, Form):
        ###########################################################################(AAAAAAAAAAAAAAAAAAAAAAAAAAAA)#####################################################
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lb_above_timeRemind_B.setText(
            QCoreApplication.translate("Form", u"  \u5df2\u5de5\u4f5c\u65f6\u95f4\uff1a", None))
        self.pb_above_exit_B.setText(QCoreApplication.translate("Form", u"EXIT", None))
        self.lb_above_mode_B.setText(QCoreApplication.translate("Form", u"  \u5f53\u524d\u6a21\u5f0f\uff1a", None))
        # self.lb_above_timeRemind_B.setText("")
        self.lb_background_B.setText("")
        self.lb_showBackgroundA_B.setText("")
        self.lb_showTitleA_B.setText("")
        self.pb_showStartA_B.setText("")
        self.pb_showStoryA_B.setText("")
        self.pb_showRestA_B.setText("")
        self.pb_showSetA_B.setText("")
        self.lb_showHumanLeftA_B.setText("")
        self.pb_showNextB_B.setText(QCoreApplication.translate("Form", u"next", None))
        self.lb_showBackgroundB_B.setText("")
        self.lb_showHuamnLeftB_B.setText("")
        self.lb_showTellB_B.setText("")
        self.lb_showNameB_B.setText("")
        self.pb_showNextC_B.setText(QCoreApplication.translate("Form", u"next", None))
        self.lb_showBackgroundC_B.setText("")
        self.lb_showTellC_B.setText("")
        self.lb_showNameC_B.setText("")
        self.lb_showHumanRightC_B.setText("")
        self.lb_showBackgroundD_B.setText("")
        self.lb_showHumanLeftD_B.setText("")
        self.lb_showTellD_B.setText("")
        self.lb_showNameD_B.setText("")
        self.lb_showChangeD_B.setText("")
        self.pb_showChangeAD_B.setText("")
        self.pb_showChangeAE_B.setText("")
        self.lb_showTellE_B.setText("")
        self.lb_showChangeE_B.setText("")
        self.lb_showBackgroundE_B.setText("")
        self.lb_showNameE_B.setText("")
        self.lb_showHumanLeftE_B.setText("")
        self.pb_showChangeBE_B.setText("")
        self.lb_showTellF_B.setText("")
        self.pb_showChangeBF_B.setText("")
        self.lb_showChangeF_B.setText("")
        self.lb_showBackgroundF_B.setText("")
        self.lb_showNameF_B.setText("")
        self.pb_showChangeAF_B.setText("")
        self.lb_showHumanLeftF_B.setText("")
        self.pb_showChangeCF_B.setText("")
        self.lb_showBackgroundG_B.setText("")
        self.lb_showTellG_B.setText("")
        self.pb_showNextG_B.setText("")
        self.lb_showNameG_B.setText("")
        self.lb_showBackgroundH_B.setText("")
        self.pb_showExitH_B.setText("")
        self.lb_attribute_flow_background_B.setText("")
        # self.lb_attributeBox0_B.setText("")
        # self.lb_attribute_flow_titleFlowI_B.setText(
        #    QCoreApplication.translate("Form", u"\u7a97\u53e3\u7f16\u53f7\uff1aA0      \u98ce\u683c\uff1aB1", None))
        # self.lb_attributeWindowSaw_B.setText(
        #    QCoreApplication.translate("Form", u"\u7f16\u53f7\u5e03\u5c40\u5c55\u793a\uff1a", None))
        self.lb_attribute_flow_mapII_B.setText(QCoreApplication.translate("Form", u"     MAP", None))
        self.lb_attribute_flow_titleFlowIII_B.setText(
            QCoreApplication.translate("Form", u"\u7a97\u6027\u6d41\u7a0b\u56fe\u7f29\u7565\u5c55\u793a\u56fe\uff1a",
                                       None))
        self.lb_attribute_flow_titleFlowII_B.setText(
            QCoreApplication.translate("Form", u"\u7a97\u6027\u6a21\u677f\u5c55\u793a\uff1a", None))
        self.lb_attribute_flow_nameI_B.setText(
            QCoreApplication.translate("Form", u"\u7a97\u53e3\u540d\u79f0\uff08\u6ce8\u91ca\uff09\uff1a", None))
        self.lb_attribute_flow_typeI_B.setText(
            QCoreApplication.translate("Form", u"\u7a97\u53e3\u7c7b\u578b\uff1a", None))
        self.lb_attribute_flow_titleFlowI_B.setText(
            QCoreApplication.translate("Form", u"\u7a97\u53e3\u5c5e\u6027\uff1a", None))
        self.lb_attribute_flow_numI_B.setText(
            QCoreApplication.translate("Form", u"\u7a97\u53e3\u7f16\u53f7\uff1a", None))
        self.pb_attributeSetSignA_B.setText("")
        self.lb_chart_B.setText("")
        self.lb_attributeNum0A2_B.setText(QCoreApplication.translate("Form", u"3.", None))
        self.lb_attribute1A2_B.setText(QCoreApplication.translate("Form", u"lb_title_\n"
                                                                          "A", None))
        self.lb_attribute2A2_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3A2_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4A2_B.setText(QCoreApplication.translate("Form", u"\u6807\u9898", None))
        self.lb_attributeNum0A0_B.setText(QCoreApplication.translate("Form", u"1.", None))
        self.lb_attribute1A0_B.setText(QCoreApplication.translate("Form", u"lb_back\n"
                                                                          "groud_A", None))
        self.lb_attribute2A0_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3A0_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4A0_B.setText(QCoreApplication.translate("Form", u"\u80cc\u666f", None))
        self.lb_attributeNum0A1_B.setText(QCoreApplication.translate("Form", u"2.", None))
        self.lb_attribute1A1_B.setText(QCoreApplication.translate("Form", u"lb_huam\n"
                                                                          "n_left_A", None))
        self.lb_attribute2A1_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3A1_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4A1_B.setText(QCoreApplication.translate("Form", u"\u4eba\u7269", None))
        self.lb_attributeNum0A5_B.setText(QCoreApplication.translate("Form", u"6.", None))
        self.lb_attribute1A5_B.setText(QCoreApplication.translate("Form", u"pb_start_\n"
                                                                          "A", None))
        self.pb_attribute3A5_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4A5_B.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u6e38\u620f", None))
        self.lb_attribute2A5_B.setText(QCoreApplication.translate("Form", u"QPushBu\n"
                                                                          "tton", None))
        self.lb_attributeNum0A3_B.setText(QCoreApplication.translate("Form", u"4.", None))
        self.lb_attribute1A3_B.setText(QCoreApplication.translate("Form", u"pb_rest_\n"
                                                                          "A", None))
        self.lb_attribute2A3_B.setText(QCoreApplication.translate("Form", u"QPushBu\n"
                                                                          "tton", None))
        self.pb_attribute3A3_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4A3_B.setText(QCoreApplication.translate("Form", u"\u5b58\u6863", None))
        self.lb_attributeNum0A4_B.setText(QCoreApplication.translate("Form", u"5.", None))
        self.lb_attribute1A4_B.setText(QCoreApplication.translate("Form", u"pb_set_A", None))
        self.pb_attribute3A4_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4A4_B.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.lb_attribute2A4_B.setText(QCoreApplication.translate("Form", u"QPushBu\n"
                                                                          "tton", None))
        self.lb_attributeNum0A6_B.setText(QCoreApplication.translate("Form", u"7.", None))
        self.lb_attribute1A6_B.setText(QCoreApplication.translate("Form", u"pb_story\n"
                                                                          "_A", None))
        self.pb_attribute3A6_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4A6_B.setText(QCoreApplication.translate("Form", u"\u8fdb\u7a0b\u6811", None))
        self.lb_attribute2A6_B.setText(QCoreApplication.translate("Form", u"QPushBu\n"
                                                                          "tton", None))
        self.lb_attributeNum0B3_B.setText(QCoreApplication.translate("Form", u"4.", None))
        self.lb_attribute1B3_B.setText(QCoreApplication.translate("Form", u"lb_tell_B", None))
        self.lb_attribute2B3_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3B3_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4B3_B.setText(QCoreApplication.translate("Form", u"\u5bf9\u8bdd\u6846", None))
        self.pb_attributeSetSignB_B.setText("")
        self.lb_attributeNum0B2_B.setText(QCoreApplication.translate("Form", u"3.", None))
        self.lb_attribute1B2_B.setText(QCoreApplication.translate("Form", u"lb_name\n"
                                                                          "_B", None))
        self.lb_attribute2B2_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3B2_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4B2_B.setText(QCoreApplication.translate("Form", u"\u4eba\u7269\u540d\u79f0", None))
        self.lb_attributeNum0B1_B.setText(QCoreApplication.translate("Form", u"2.", None))
        self.lb_attribute1B1_B.setText(QCoreApplication.translate("Form", u"lb_huam\n"
                                                                          "n_left_B", None))
        self.lb_attribute2B1_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3B1_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4B1_B.setText(QCoreApplication.translate("Form", u"\u4eba\u7269", None))
        self.lb_attributeNum0B0_B.setText(QCoreApplication.translate("Form", u"1.", None))
        self.lb_attribute1B0_B.setText(QCoreApplication.translate("Form", u"lb_back\n"
                                                                          "groud_B", None))
        self.lb_attribute2B0_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3B0_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4B0_B.setText(QCoreApplication.translate("Form", u"\u80cc\u666f", None))
        self.lb_attributeNum0C3_B.setText(QCoreApplication.translate("Form", u"4.", None))
        self.lb_attribute1C3_B.setText(QCoreApplication.translate("Form", u"lb_tell_C", None))
        self.lb_attribute2C3_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3C3_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4C3_B.setText(QCoreApplication.translate("Form", u"\u5bf9\u8bdd\u6846", None))
        self.pb_attributeSetSignC_B.setText("")
        self.lb_attributeNum0C2_B.setText(QCoreApplication.translate("Form", u"3.", None))
        self.lb_attribute1C2_B.setText(QCoreApplication.translate("Form", u"lb_name\n"
                                                                          "_C", None))
        self.lb_attribute2C2_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3C2_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4C2_B.setText(QCoreApplication.translate("Form", u"\u4eba\u7269\u540d\u79f0", None))
        self.lb_attributeNum0C1_B.setText(QCoreApplication.translate("Form", u"2.", None))
        self.lb_attribute1C1_B.setText(QCoreApplication.translate("Form", u"lb_huam\n"
                                                                          "n_left_C", None))
        self.lb_attribute2C1_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3C1_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4C1_B.setText(QCoreApplication.translate("Form", u"\u4eba\u7269", None))
        self.lb_attributeNum0C0_B.setText(QCoreApplication.translate("Form", u"1.", None))
        self.lb_attribute1C0_B.setText(QCoreApplication.translate("Form", u"lb_back\n"
                                                                          "groud_C", None))
        self.lb_attribute2C0_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3C0_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4C0_B.setText(QCoreApplication.translate("Form", u"\u80cc\u666f", None))
        self.lb_attributeNum0D3_B.setText(QCoreApplication.translate("Form", u"4.", None))
        self.lb_attribute1D3_B.setText(QCoreApplication.translate("Form", u"lb_name\n"
                                                                          "_D", None))
        self.lb_attribute2D3_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3D3_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4D3_B.setText(QCoreApplication.translate("Form", u"\u4eba\u7269\u540d\u79f0", None))
        self.lb_attributeNum0D0_B.setText(QCoreApplication.translate("Form", u"1.", None))
        self.lb_attribute1D0_B.setText(QCoreApplication.translate("Form", u"lb_back\n"
                                                                          "groud_D", None))
        self.lb_attribute2D0_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3D0_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4D0_B.setText(QCoreApplication.translate("Form", u"\u80cc\u666f", None))
        self.pb_attributeSetSignD_B.setText("")
        self.lb_attributeNum0D2_B.setText(QCoreApplication.translate("Form", u"3.", None))
        self.lb_attribute1D2_B.setText(QCoreApplication.translate("Form", u"lb_chang\n"
                                                                          "e_D", None))
        self.lb_attribute2D2_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3D2_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4D2_B.setText(QCoreApplication.translate("Form", u"'\u9009\u62e9'\u4e8c\u5b57", None))
        self.lb_attributeNum0D1_B.setText(QCoreApplication.translate("Form", u"2.", None))
        self.lb_attribute1D1_B.setText(QCoreApplication.translate("Form", u"lb_huam\n"
                                                                          "n_left_D", None))
        self.lb_attribute2D1_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3D1_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4D1_B.setText(QCoreApplication.translate("Form", u"\u4eba\u7269", None))
        self.lb_attributeNum0D5_B.setText(QCoreApplication.translate("Form", u"6.", None))
        self.lb_attribute1D5_B.setText(QCoreApplication.translate("Form", u"pb_chang\n"
                                                                          "e_A_D", None))
        self.pb_attribute3D5_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4D5_B.setText(QCoreApplication.translate("Form", u"\u9009\u9879A", None))
        self.lb_attribute2D5_B.setText(QCoreApplication.translate("Form", u"QPushBu\n"
                                                                          "tton", None))
        self.lb_attributeNum0D4_B.setText(QCoreApplication.translate("Form", u"5.", None))
        self.lb_attribute1D4_B.setText(QCoreApplication.translate("Form", u"lb_tell_D", None))
        self.pb_attribute3D4_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4D4_B.setText(QCoreApplication.translate("Form", u"\u5bf9\u8bdd\u6846", None))
        self.lb_attribute2D4_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.lb_attributeNum0E2_B.setText(QCoreApplication.translate("Form", u"3.", None))
        self.lb_attribute1E2_B.setText(QCoreApplication.translate("Form", u"lb_name_\n"
                                                                          "E", None))
        self.lb_attribute2E2_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3E2_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4E2_B.setText(QCoreApplication.translate("Form", u"\u4eba\u7269\u540d\u79f0", None))
        self.lb_attributeNum0E4_B.setText(QCoreApplication.translate("Form", u"5.", None))
        self.lb_attribute1E4_B.setText(QCoreApplication.translate("Form", u"lb_chang\n"
                                                                          "e_E", None))
        self.pb_attribute3E4_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4E4_B.setText(QCoreApplication.translate("Form", u"'\u9009\u62e9'\u4e8c\u5b57", None))
        self.lb_attribute2E4_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.lb_attributeNum0E1_B.setText(QCoreApplication.translate("Form", u"2.", None))
        self.lb_attribute1E1_B.setText(QCoreApplication.translate("Form", u"lb_huam\n"
                                                                          "n_left_E", None))
        self.lb_attribute2E1_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3E1_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4E1_B.setText(QCoreApplication.translate("Form", u"\u4eba\u7269", None))
        self.lb_attributeNum0E5_B.setText(QCoreApplication.translate("Form", u"6.", None))
        self.lb_attribute1E5_B.setText(QCoreApplication.translate("Form", u"pb_chang\n"
                                                                          "e_A_E", None))
        self.pb_attribute3E5_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4E5_B.setText(QCoreApplication.translate("Form", u"A\u9009\u9879", None))
        self.lb_attribute2E5_B.setText(QCoreApplication.translate("Form", u"QPushBu\n"
                                                                          "tton", None))
        self.lb_attributeNum0E3_B.setText(QCoreApplication.translate("Form", u"4.", None))
        self.lb_attribute1E3_B.setText(QCoreApplication.translate("Form", u"lb_tell_\n"
                                                                          "E", None))
        self.lb_attribute2E3_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3E3_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4E3_B.setText(QCoreApplication.translate("Form", u"\u5bf9\u8bdd\u6846", None))
        self.pb_attributeSetSignE_B.setText("")
        self.lb_attributeNum0E0_B.setText(QCoreApplication.translate("Form", u"1.", None))
        self.lb_attribute1E0_B.setText(QCoreApplication.translate("Form", u"lb_back\n"
                                                                          "groud_E", None))
        self.lb_attribute2E0_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3E0_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4E0_B.setText(QCoreApplication.translate("Form", u"\u80cc\u666f", None))
        self.lb_attributeNum0E6_B.setText(QCoreApplication.translate("Form", u"7.", None))
        self.lb_attribute1E6_B.setText(QCoreApplication.translate("Form", u"pb_chang\n"
                                                                          "e_B_E", None))
        self.pb_attribute3E6_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4E6_B.setText(QCoreApplication.translate("Form", u"B\u9009\u9879", None))
        self.lb_attribute2E6_B.setText(QCoreApplication.translate("Form", u"QPushBu\n"
                                                                          "tton", None))
        self.lb_attributeNum0F2_B.setText(QCoreApplication.translate("Form", u"3.", None))
        self.lb_attribute1F2_B.setText(QCoreApplication.translate("Form", u"lb_name_\n"
                                                                          "F", None))
        self.lb_attribute2F2_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3F2_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4F2_B.setText(QCoreApplication.translate("Form", u"\u4eba\u7269\u540d\u79f0", None))
        self.lb_attributeNum0F4_B.setText(QCoreApplication.translate("Form", u"5.", None))
        self.lb_attribute1F4_B.setText(QCoreApplication.translate("Form", u"lb_chang\n"
                                                                          "e_F", None))
        self.pb_attribute3F4_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4F4_B.setText(QCoreApplication.translate("Form", u"'\u9009\u62e9'\u4e8c\u5b57", None))
        self.lb_attribute2F4_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.lb_attributeNum0F1_B.setText(QCoreApplication.translate("Form", u"2.", None))
        self.lb_attribute1F1_B.setText(QCoreApplication.translate("Form", u"lb_huam\n"
                                                                          "n_left_F", None))
        self.lb_attribute2F1_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3F1_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4F1_B.setText(QCoreApplication.translate("Form", u"\u4eba\u7269", None))
        self.lb_attributeNum0F5_B.setText(QCoreApplication.translate("Form", u"6.", None))
        self.lb_attribute1F5_B.setText(QCoreApplication.translate("Form", u"pb_chang\n"
                                                                          "e_A_F", None))
        self.pb_attribute3F5_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4F5_B.setText(QCoreApplication.translate("Form", u"A\u9009\u9879", None))
        self.lb_attribute2F5_B.setText(QCoreApplication.translate("Form", u"QPushBu\n"
                                                                          "tton", None))
        self.lb_attributeNum0F3_B.setText(QCoreApplication.translate("Form", u"4.", None))
        self.lb_attribute1F3_B.setText(QCoreApplication.translate("Form", u"lb_tell_\n"
                                                                          "F", None))
        self.lb_attribute2F3_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3F3_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4F3_B.setText(QCoreApplication.translate("Form", u"\u5bf9\u8bdd\u6846", None))
        self.lb_attributeNum0F7_B.setText(QCoreApplication.translate("Form", u"8.", None))
        self.lb_attribute1F7_B.setText(QCoreApplication.translate("Form", u"pb_chang\n"
                                                                          "e_C_F", None))
        self.lb_attribute2F7_B.setText(QCoreApplication.translate("Form", u"QPushBu\n"
                                                                          "tton", None))
        self.lb_attribute3F7_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4F7_B.setText(QCoreApplication.translate("Form", u"C\u9009\u9879", None))
        self.pb_attributeSetSignF_B.setText("")
        self.lb_attributeNum0F0_B.setText(QCoreApplication.translate("Form", u"1.", None))
        self.lb_attribute1F0_B.setText(QCoreApplication.translate("Form", u"lb_back\n"
                                                                          "groud_F", None))
        self.lb_attribute2F0_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3F0_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4F0_B.setText(QCoreApplication.translate("Form", u"\u80cc\u666f", None))
        self.lb_attributeNum0F6_B.setText(QCoreApplication.translate("Form", u"7.", None))
        self.lb_attribute1F6_B.setText(QCoreApplication.translate("Form", u"pb_chang\n"
                                                                          "e_B_F", None))
        self.pb_attribute3F6_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4F6_B.setText(QCoreApplication.translate("Form", u"B\u9009\u9879", None))
        self.lb_attribute2F6_B.setText(QCoreApplication.translate("Form", u"QPushBu\n"
                                                                          "tton", None))
        self.lb_attributeNum0G1_B.setText(QCoreApplication.translate("Form", u"2.", None))
        self.lb_attribute1G1_B.setText(QCoreApplication.translate("Form", u"lb_name_\n"
                                                                          "G", None))
        self.lb_attribute2G1_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3G1_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4G1_B.setText(QCoreApplication.translate("Form", u"\u4eba\u7269\u540d\u79f0", None))
        self.lb_attributeNum0G3_B.setText(QCoreApplication.translate("Form", u"3.", None))
        self.lb_attribute1G3_B.setText(QCoreApplication.translate("Form", u"lb_tell_\n"
                                                                          "G", None))
        self.lb_attribute2G3_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3G3_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4G3_B.setText(QCoreApplication.translate("Form", u"\u5bf9\u8bdd\u6846", None))
        self.pb_attributeSetSignG_B.setText("")
        self.lb_attributeNum0G0_B.setText(QCoreApplication.translate("Form", u"1.", None))
        self.lb_attribute1G0_B.setText(QCoreApplication.translate("Form", u"lb_back\n"
                                                                          "groud_G", None))
        self.lb_attribute2G0_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3G0_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4G0_B.setText(QCoreApplication.translate("Form", u"\u80cc\u666f", None))
        self.lb_attributeNum0H1_B.setText(QCoreApplication.translate("Form", u"2.", None))
        self.lb_attribute1H1_B.setText(QCoreApplication.translate("Form", u"pb_exit_\n"
                                                                          "H", None))
        self.lb_attribute2H1_B.setText(QCoreApplication.translate("Form", u"QpushBu\n"
                                                                          "tton", None))
        self.pb_attribute3H1_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4H1_B.setText(QCoreApplication.translate("Form", u"\u9000\u51fa\u6309\u94ae", None))
        self.pb_attributeSetSignH_B.setText("")
        self.lb_attributeNum0H0_B.setText(QCoreApplication.translate("Form", u"1.", None))
        self.lb_attribute1H0_B.setText(QCoreApplication.translate("Form", u"lb_back\n"
                                                                          "groud_H", None))
        self.lb_attribute2H0_B.setText(QCoreApplication.translate("Form", u"Qlabel", None))
        self.pb_attribute3H0_B.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.lb_attribute4H0_B.setText(QCoreApplication.translate("Form", u"\u80cc\u666f", None))
        self.lb_attribute_edit_background_B.setText("")
        self.pb_attribute_flow_updataI_B.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u4e0a\u4f20", None))
        self.lb_attribute_edit_titleFlowI_B.setText(
            QCoreApplication.translate("Form", u"\u7a97\u53e3\u5c5e\u6027\uff1a", None))
        # self.lb_windowSignal_B.setText(
        #    QCoreApplication.translate("Form", u"\u7f16\u53f7\u5e03\u5c40\u793a\u610f\uff1a", None))
        # self.pb_mapUp_B.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u4e0a\u4f20", None))
        # self.lb_attributeMap11_B.setText("")
        # self.lb_windowShow_B.setText(QCoreApplication.translate("Form", u"\u5e03\u5c40\u5c55\u793a\uff1a", None))
        # self.lb_attributeMap12_B.setText("")
        self.le_attribute_edit_nameI_B.setText("")
        self.lb_attribute_edit_titleFlowII_B.setText(
            QCoreApplication.translate("Form", u"\u63a7\u4ef6\u53c2\u6570\uff1a", None))
        self.lb_attribute_edit_nameI_B.setText(
            QCoreApplication.translate("Form", u"\u7a97\u53e3\u540d\u79f0\uff08\u6ce8\u91ca\uff09\uff1a", None))
        self.lb_attribute_edit_numI_B.setText(
            QCoreApplication.translate("Form", u"\u7a97\u53e3\u7f16\u53f7\uff1a", None))
        self.lb_attribute_edit_typeI_B.setText(
            QCoreApplication.translate("Form", u"\u7a97\u53e3\u7c7b\u578b\uff1a", None))
        self.lb_attribute_flow_mapIII_B.setText(QCoreApplication.translate("Form", u"     MAP", None))
        self.lb_introduce_background_B.setText("")
        self.lb_introduce_Maker_B.setText(QCoreApplication.translate("Form", u"  Maker:CVcoding", None))
        self.lb_introduce_biliURL_B.setText(QCoreApplication.translate("Form",
                                                                       u"<html><head/><body><p>Bilibili:<span style=\" color:#ffffff;\"/><a href=\"https://space.bilibili.com/1100670294?spm_id_from=333.337.search-card.all.click\"><span style=\" text-decoration: underline; color:#ffffff;\">https://space.bilibili.com/1100670294?spm_id_from=333.337.search-card.all.click</span></a></p></body></html>",
                                                                       None))
        self.lb_introduce_studio_B.setText(QCoreApplication.translate("Form", u"Powered by TG-studio", None))
        # self.lb_introduceBiliURL_B.setText(QCoreApplication.translate("<a href='https://space.bilibili.com/1100670294?spm_id_from=333.337.search-card.all.click'>https://space.bilibili.com/1100670294?spm_id_from=333.337.search-card.all.click</a>"))
        # self.lb_introduceBiliURL_B.setOpenExternalLinks(True)
        
        self.lb_introduce_email_B.setText(QCoreApplication.translate("Form",
                                                                     u"<html><head/><body><p>  e-mail:<span style=\" color:#ffffff;\">CVcoding@proton.me</span></p></body></html>",
                                                                     None))
        
        ###########################################################################(AAAAAAAAAAAAAAAAAAAAAAAAAAAA)#####################################################
        ###########################################################################(BBBBBBBBBBBBBBBBBBBBBBBBBBBB)#####################################################
        self.lb_trademark_A.setText("")
        self.lb_background_A.setText("")
        self.lb_note1_A.setText("")
        self.lb_title_A.setText("")
        self.pb_create_A.setText("")
        self.pb_dictionary_A.setText("")
        self.pb_about_A.setText("")
        self.pb_set_A.setText("")
###########################################################################(BBBBBBBBBBBBBBBBBBBBBBBBBBBB)#####################################################

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")  # 设置窗口风格
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_Form()  # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程