# -*- coding: utf-8 -*-
import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import multitasking
#import qrc转.img_stable_rc
sw_stack = None
lb_background_G = None
lb_tell_talk_left_G= None
lb_name_story_G = None
lb_human_F = None
#lb_tell_talk_left_G = None
###index###
index_human = 0
index_name = 0
index_tell = 0
index_background = 0
continue_count_next = 0
###index###
###button###
button_countA = 0
button_countB = 0
button_countC = 0
###button###
date_process = open('date/date_process.txt','r+',encoding = 'UTF-8')
game_process = date_process.read()#游戏的进程码
img_date ={'sister_left':[1,"新建项目.png",3],
           'sister_right':[1,2,3],
           'player_left':[1,2,3],
           'player_right':[1,2,3],
           'background':[1,2,3],
           'button':[1,2,3],
           'story':[1,2,3],
           'name':[1,2,3]
           }#Game轮子所用的图片素材库
text_date ={'sister':[1,2,3],
           'player':[1,2,3],
           'narrator': [1, 2, 3]
           }#Game轮子所用的文字素材库
back_date = ['B1','B2','B3','B4','B5','B6','B6/F1','B6/F1/B1','B6/F1/B1/H',
             'B6/F2/B1','B6/F2/B1/H',
             'B6/F3/B1','B6/F3/B1/H']
class Ui_MainWindow(QMainWindow):
    global icon1, icon2, icon3
    global lb_backgroud_A, lb_title_A, lb_huamn_left_A, pb_start_A, pb_set_A, pb_save_A, lb_huamn_B, \
        lb_background_B, lb_tell__B, lb_name_B, lb_background_C, lb_human_C, lb_name_C, tell_talk_right_C, \
        lb_tell_D, lb_huamn_left_D, lb_name_D, lb_backgroud_D, lb_background_E, lb_name_E, lb_tell_E, lb_huamn_E, \
        lb_backgroud_F, lb_human_F, lb_name_talk_left_F, lb_tell_talk_left_F, lb_background_G, lb_tell_talk_left_G, \
        lb_name_story_G
    def __init__(self,count):
        #super().__init__()
        super(Ui_MainWindow, self).__init__()
        self.count = count
        self.setupUi(self)
        self.retranslateUi(self)
        #self.lb_name_story_G =lb_name_story_G
        #self.change_widget(self)
    def setupUi(self, MainWindow):
        global icon1, icon2, icon3
        global lb_backgroud_A, lb_title_A, lb_huamn_left_A, pb_start_A, pb_set_A, pb_save_A, lb_huamn_B, \
            lb_background_B, lb_tell__B, lb_name_B, lb_background_C, lb_human_C, lb_name_C, tell_talk_right_C, \
            lb_tell_D, lb_huamn_left_D, lb_name_D, lb_backgroud_D, lb_background_E, lb_name_E, lb_tell_E, lb_huamn_E, \
            lb_backgroud_F, lb_human_F, lb_name_talk_left_F, lb_tell_talk_left_F, lb_background_G, lb_tell_talk_left_G, \
            lb_name_story_G

        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1183, 704)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 1181, 671))


        #每个大写字母代表一个stack内嵌套的每张卡片的小布局的编号
        #界面码：
        #       zero-A(main_game)----游戏的初始界面
        #       one-B(talk_left)----人物在左边的情况
        #       two-C(talk_right)----人物在右边的情况
        #       three-D(change_one)----选择界面，有一个选项
        #       four-E(change_two)----选择界面，有两个选项
        #       five-F(change_three)----选择界面，有三个选项
        #       six-G(talk_story)----动画或旁白进程，没有人物
        #       seven-H(game_end)----游戏结束（未完待续），开发者致谢表
        #waring:1.*_talk_left_*等命名是因为第一代时的命名问题，没有特殊含义
        #       2.__（双下划杠）只是编写是的疏漏，没有特殊含义
        ################本编号同样适用于UI文件和game类和Xmind##############

        ############################zero##############################(main_game)
        self.grid_main_A = QGridLayout(self.gridLayoutWidget)
        self.grid_main_A.setObjectName(u"grid_main_A")
        self.grid_main_A.setContentsMargins(0, 0, 0, 0)#第一层布局，相对布局

        self.widget_A = QWidget(self.gridLayoutWidget)
        self.widget_A.setObjectName(u"widget_A")
        #嵌套至stack的子布局#

        self.pb_story_A = QPushButton(self.widget_A)
        self.pb_story_A.setObjectName(u"pb_story_A")
        self.pb_story_A.setGeometry(QRect(770, 340, 261, 91))
        icon = QIcon()
        icon.addFile(u":/\u65b0\u524d\u7f00/pb_story.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_story_A.setIcon(icon)
        self.pb_story_A.setIconSize(QSize(261, 91))
        self.pb_story_A.clicked.connect(Game_function.game_story)
        #剧情进程或者成就界面

        self.lb_backgroud_A = QLabel(self.widget_A)
        self.lb_backgroud_A.setObjectName(u"lb_backgroud_A")
        self.lb_backgroud_A.setGeometry(QRect(0, 0, 1181, 671))
        self.lb_backgroud_A.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background1.jpg"))
        #背景

        self.pb_save_A = QPushButton(self.widget_A)
        self.pb_save_A.setObjectName(u"pb_save_A")
        self.pb_save_A.setGeometry(QRect(770, 440, 261, 91))
        icon4 = QIcon()
        icon4.addFile(u":/\u65b0\u524d\u7f00/pb_save.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_save_A.setIcon(icon4)
        self.pb_save_A.setIconSize(QSize(261, 91))
        self.pb_save_A.clicked.connect(Game_function.game_save)
        #打开存档按钮

        icon1 = QIcon()
        icon1.addFile(u":/\u65b0\u524d\u7f00/pb_save.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_save_A.setIcon(icon1)
        self.lb_title_A = QLabel(self.widget_A)
        self.lb_title_A.setObjectName(u"lb_title_A")
        self.lb_title_A.setGeometry(QRect(500, 0, 651, 171))
        self.lb_title_A.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/title.jpg"))
        #机械之心的标题

        self.lb_huamn_left_A = QLabel(self.widget_A)
        self.lb_huamn_left_A.setObjectName(u"lb_huamn_left_A")
        self.lb_huamn_left_A.setGeometry(QRect(-30, 80, 501, 781))
        self.lb_huamn_left_A.setPixmap(QPixmap(
            u":/\u65b0\u524d\u7f00/sisiter2.png"))
        #人物图片，在左边的情况

        self.pb_set_A = QPushButton(self.widget_A)
        self.pb_set_A.setObjectName(u"pb_set_A")
        self.pb_set_A.setGeometry(QRect(770, 540, 261, 91))
        icon2 = QIcon()
        icon2.addFile(u":/\u65b0\u524d\u7f00/pb_set.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_set_A.setIcon(icon2)
        self.pb_set_A.setIconSize(QSize(261, 91))
        self.pb_set_A.clicked.connect(Game_function.game_set)
        #退出游戏保存数据，开发者信息

        self.pb_start_A = QPushButton(self.widget_A)
        self.pb_start_A.setObjectName(u"pb_start_A")
        self.pb_start_A.setGeometry(QRect(770, 240, 261, 91))
        icon3 = QIcon()
        icon3.addFile(u":/\u65b0\u524d\u7f00/pb_start.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_start_A.setIcon(icon3)
        self.pb_start_A.setIconSize(QSize(261, 91))
        self.pb_start_A.clicked.connect(Game_function.game_start)#绑定槽函数-开始游戏
        #游戏的开始按钮#

        self.lb_backgroud_A.raise_()
        self.pb_save_A.raise_()
        self.lb_title_A.raise_()
        self.lb_huamn_left_A.raise_()
        self.pb_set_A.raise_()
        self.pb_start_A.raise_()
        self.pb_story_A.raise_()
        #self.grid_main_A.addWidget(self.widget_A, 0, 0, 1, 1)

        ################zero#####################################################
        ###################################one###################################(talk_left)

        #self.grid_B = QGridLayout(self.gridLayoutWidget)
        #self.grid_B.setObjectName(u"grid_B")
        #self.grid_B.setContentsMargins(0, 0, 0, 0)
        self.widget_B = QWidget(self.gridLayoutWidget)
        self.widget_B.setObjectName(u"widget_B")
        # 第三层嵌套，负责stack的卡片切换

        self.lb_huamn_B = QLabel(self.widget_B)
        self.lb_huamn_B.setObjectName(u"lb_huamn_B")
        self.lb_huamn_B.setGeometry(QRect(-30, 100, 501, 781))
        self.lb_huamn_B.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/sisiter2.png"))
        #人物在左边的情况

        self.lb_background_B = QLabel(self.widget_B)
        self.lb_background_B.setObjectName(u"lb_background_B")
        self.lb_background_B.setGeometry(QRect(0, 0, 1181, 671))
        self.lb_background_B.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background1.jpg"))
        #背景

        self.pb_next_B = QPushButton(self.widget_B)
        self.pb_next_B.setObjectName(u"pb_next_B")
        self.pb_next_B.setGeometry(QRect(970, 610, 75, 23))
        self.pb_next_B.clicked.connect(Game_patch.game_next)
        #切换下一部分的按钮

        self.lb_tell__B = QLabel(self.widget_B)
        self.lb_tell__B.setObjectName(u"lb_tell__B")
        self.lb_tell__B.setGeometry(QRect(470, 480, 631, 191))
        self.lb_tell__B.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/talk1.jpg"))
        #角色的对话---双下划杠只是打多了，没有其他意思

        self.lb_name_B = QLabel(self.widget_B)
        self.lb_name_B.setObjectName(u"lb_name_B")
        self.lb_name_B.setGeometry(QRect(470, 380, 281, 81))
        self.lb_name_B.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/name2.jpg"))
        self.lb_name_B.setMargin(0)
        self.lb_name_B.setIndent(6)
        self.lb_name_B.setOpenExternalLinks(False)
        #角色的名称栏

        self.lb_background_B.raise_()
        self.lb_tell__B.raise_()
        self.lb_huamn_B.raise_()
        self.lb_name_B.raise_()

        #self.grid_B.addWidget(self.widget_B, 0, 0, 1, 1)
        #######################one#####################
        #######################two#####################(talk_right)
        #self.grid_C = QGridLayout(self.gridLayoutWidget)
        #self.grid_C.setObjectName(u"grid_C")
        #self.grid_C.setContentsMargins(0, 0, 0, 0)
        self.widget_C = QWidget(self.gridLayoutWidget)
        self.widget_C.setObjectName(u"widget_C")
        # 第三层布局，负责stack的卡片切换

        self.lb_human_C = QLabel(self.widget_C)
        self.lb_human_C.setObjectName(u"lb_human_C")
        self.lb_human_C.setGeometry(QRect(700, 10, 481, 811))
        self.lb_human_C.setPixmap(QPixmap(u"../image/\u59b9\u59b9/sisiter1.png"))
        #人物在右边的情况

        self.lb_background_C = QLabel(self.widget_C)
        self.lb_background_C.setObjectName(u"lb_background_C")
        self.lb_background_C.setGeometry(QRect(0, 0, 1181, 671))
        self.lb_background_C.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background1.jpg"))
        # 背景

        self.lb_name_C = QLabel(self.widget_C)
        self.lb_name_C.setObjectName(u"lb_name_C")
        self.lb_name_C.setGeometry(QRect(380, 340, 301, 111))
        self.lb_name_C.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/name2.jpg"))
        self.lb_name_C.setMargin(0)
        self.lb_name_C.setIndent(6)
        self.lb_name_C.setOpenExternalLinks(False)
        #角色名称栏

        self.pb_next_C = QPushButton(self.widget_C)
        self.pb_next_C.setObjectName(u"pb_next_C")
        self.pb_next_C.setGeometry(QRect(700, 570, 75, 23))
        self.pb_next_C.clicked.connect(Game_patch.game_next)
        #切换下一部分的按钮

        self.tell_talk_right_C = QLabel(self.widget_C)
        self.tell_talk_right_C.setObjectName(u"tell_talk_right_C")
        self.tell_talk_right_C.setGeometry(QRect(40, 460, 661, 191))
        self.tell_talk_right_C.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/talk1.jpg"))
        #对话框，命名talk_right是第一代的命名不当

        self.lb_background_C.raise_()
        self.lb_human_C.raise_()
        self.lb_name_C.raise_()
        self.tell_talk_right_C.raise_()
        self.pb_next_B.raise_()

        #self.grid_C.addWidget(self.widget_C, 0, 0, 1, 1)

        #######################two#####################
        ########################three###################(change_one)

        #self.grid_change_D = QGridLayout(self.gridLayoutWidget)
        #self.grid_change_D.setObjectName(u"grid_change_D")
        #self.grid_change_D.setContentsMargins(0, 0, 0, 0)
        self.widget_D = QWidget(self.gridLayoutWidget)
        self.widget_D.setObjectName(u"widget_D")
        # 第三层布局，负责stack的卡片切换

        self.lb_change_D = QLabel(self.widget_D)
        self.lb_change_D.setObjectName(u"lb_change_D")
        self.lb_change_D.setGeometry(QRect(850, 250, 54, 12))
        #选项旁边的两个字选择

        self.lb_tell_D = QLabel(self.widget_D)
        self.lb_tell_D.setObjectName(u"lb_tell_D")
        self.lb_tell_D.setGeometry(QRect(480, 460, 631, 191))
        self.lb_tell_D.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/talk1.jpg"))
        #对话

        self.lb_huamn_left_D = QLabel(self.widget_D)
        self.lb_huamn_left_D.setObjectName(u"lb_huamn_left_D")
        self.lb_huamn_left_D.setGeometry(QRect(-20, 80, 501, 781))
        self.lb_huamn_left_D.setPixmap(QPixmap(
            u":/\u65b0\u524d\u7f00/sisiter2.png"))
        # 人物在左边的情况

        self.lb_name_D = QLabel(self.widget_D)
        self.lb_name_D.setObjectName(u"lb_name_D")
        self.lb_name_D.setGeometry(QRect(480, 360, 281, 81))
        self.lb_name_D.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/name2.jpg"))
        self.lb_name_D.setMargin(0)
        self.lb_name_D.setIndent(6)
        self.lb_name_D.setOpenExternalLinks(False)
        #名称栏

        self.pb_change_A_D = QPushButton(self.widget_D)
        self.pb_change_A_D.setObjectName(u"pb_change_A_D")
        self.pb_change_A_D.setGeometry(QRect(890, 270, 75, 23))
        self.pb_change_A_D.clicked.connect(Game_patch.game_A)
        #A选项

        self.lb_backgroud_D = QLabel(self.widget_D)
        self.lb_backgroud_D.setObjectName(u"lb_backgroud_D")
        self.lb_backgroud_D.setGeometry(QRect(0, 0, 1181, 671))
        self.lb_backgroud_D.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background1.jpg"))
        self.lb_backgroud_D.raise_()
        #背景

        self.lb_change_D.raise_()
        self.lb_tell_D.raise_()
        self.lb_huamn_left_D.raise_()
        self.lb_name_D.raise_()
        self.pb_change_A_D.raise_()

        #self.grid_change_D.addWidget(self.widget_D, 0, 0, 1, 1)

        #######################three###################
        #######################four####################(change_two)

        #self.grid_change_E = QGridLayout(self.gridLayoutWidget)
        #self.grid_change_E.setObjectName(u"grid_change_E")
        #self.grid_change_E.setContentsMargins(0, 0, 0, 0)
        self.widget_E = QWidget(self.gridLayoutWidget)
        self.widget_E.setObjectName(u"widget_E")
        # 第三层布局，负责stack的卡片切换

        self.lb_background_E = QLabel(self.widget_E)
        self.lb_background_E.setObjectName(u"lb_background_E")
        self.lb_background_E.setGeometry(QRect(0, 0, 1181, 671))
        self.lb_background_E.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background1.jpg"))
        #背景

        self.pb_change_B_E = QPushButton(self.widget_E)
        self.pb_change_B_E.setObjectName(u"pb_change_B_E")
        self.pb_change_B_E.setGeometry(QRect(850, 290, 75, 23))
        self.pb_change_B_E.clicked.connect(Game_patch.game_B)
        #B选项

        self.lb_name_E = QLabel(self.widget_E)
        self.lb_name_E.setObjectName(u"lb_name_E")
        self.lb_name_E.setGeometry(QRect(440, 350, 281, 81))
        self.lb_name_E.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/name2.jpg"))
        self.lb_name_E.setMargin(0)
        self.lb_name_E.setIndent(6)
        self.lb_name_E.setOpenExternalLinks(False)
        #名称栏

        self.pb_change_A_E = QPushButton(self.widget_E)
        self.pb_change_A_E.setObjectName(u"pb_change_A_E")
        self.pb_change_A_E.setGeometry(QRect(850, 260, 75, 23))
        self.pb_change_A_E.clicked.connect(Game_patch.game_A)
        #A选项

        self.lb_tell_E = QLabel(self.widget_E)
        self.lb_tell_E.setObjectName(u"lb_tell_E")
        self.lb_tell_E.setGeometry(QRect(440, 450, 631, 191))
        self.lb_tell_E.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/talk1.jpg"))
        #对话

        self.lb_huamn_E = QLabel(self.widget_E)
        self.lb_huamn_E.setObjectName(u"lb_huamn_E")
        self.lb_huamn_E.setGeometry(QRect(-60, 70, 501, 781))
        self.lb_huamn_E.setPixmap(QPixmap(
            u":/\u65b0\u524d\u7f00/sisiter2.png"))
        #人物在左边的情况

        self.lb_change_E = QLabel(self.widget_E)
        self.lb_change_E.setObjectName(u"lb_change_E")
        self.lb_change_E.setGeometry(QRect(810, 240, 54, 12))
        #选择那两个字


        #self.grid_change_E.addWidget(self.widget_E, 0, 0, 1, 1)

        #######################four####################
        #######################five####################(change_three)

        #self.grid_change_F = QGridLayout(self.gridLayoutWidget)
        #self.grid_change_F.setObjectName(u"grid_change_F")
        #self.grid_change_F.setContentsMargins(0, 0, 0, 0)
        self.widget_F = QWidget(self.gridLayoutWidget)
        self.widget_F.setObjectName(u"widget_F")
        # 第三层布局，负责stack的卡片切换

        self.pb_change_C_F = QPushButton(self.widget_F)
        self.pb_change_C_F.setObjectName(u"pb_change_C")
        self.pb_change_C_F.setGeometry(QRect(880, 310, 75, 23))
        self.pb_change_C_F.clicked.connect(Game_patch.game_C)
        #C选项

        lb_backgroud_F = QLabel(self.widget_F)
        lb_backgroud_F.setObjectName(u"lb_backgroud_F")
        lb_backgroud_F.setGeometry(QRect(0, 0, 1181, 671))
        lb_backgroud_F.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background1.jpg"))
        #self.lb_backgroud_F.raise_()
        #背景

        self.pb_change_A_F = QPushButton(self.widget_F)
        self.pb_change_A_F.setObjectName(u"pb_change_A_F")
        self.pb_change_A_F.setGeometry(QRect(880, 250, 75, 23))
        self.pb_change_A_F.clicked.connect(Game_patch.game_A)
        #A选项
        global lb_human_F
        lb_human_F = QLabel(self.widget_F)
        lb_human_F.setObjectName(u"lb_human_F")
        lb_human_F.setGeometry(QRect(-30, 60, 501, 781))
        lb_human_F.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/sisiter2.png"))
        # 人物在左边

        self.pb_change_B_F = QPushButton(self.widget_F)
        self.pb_change_B_F.setObjectName(u"pb_change_B_F")
        self.pb_change_B_F.setGeometry(QRect(880, 280, 75, 23))
        self.pb_change_B_F.clicked.connect(Game_patch.game_B)
        #B选项

        self.lb_change_F = QLabel(self.widget_F)
        self.lb_change_F.setObjectName(u"lb_change_F")
        self.lb_change_F.setGeometry(QRect(840, 230, 54, 12))
        #选择那两个字

        lb_name_talk_left_F = QLabel(self.widget_F)
        lb_name_talk_left_F.setObjectName(u"lb_name_talk_left_F")
        lb_name_talk_left_F.setGeometry(QRect(470, 340, 281, 81))
        lb_name_talk_left_F.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/name2.jpg"))
        lb_name_talk_left_F.setMargin(0)
        lb_name_talk_left_F.setIndent(6)
        lb_name_talk_left_F.setOpenExternalLinks(False)
        #名称栏

        lb_tell_talk_left_F = QLabel(self.widget_F)
        lb_tell_talk_left_F.setObjectName(u"lb_tell_talk_left_F")
        lb_tell_talk_left_F.setGeometry(QRect(470, 440, 631, 191))
        lb_tell_talk_left_F.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/talk1.jpg"))
        #对话

        lb_backgroud_F.raise_()
        self.pb_change_A_F.raise_()
        lb_human_F.raise_()
        self.pb_change_B_F.raise_()
        self.lb_change_F.raise_()
        lb_name_talk_left_F.raise_()
        lb_tell_talk_left_F.raise_()
        self.pb_change_C_F.raise_()
        #self.grid_change_F.addWidget(self.widget_F, 0, 0, 1, 1)

        #######################five####################
        #######################six#####################(talk_story)

        #self.grid_G = QGridLayout(self.gridLayoutWidget)
        #self.grid_G.setObjectName(u"grid_G")
        #self.grid_G.setContentsMargins(0, 0, 0, 0)
        self.widget_G = QWidget(self.gridLayoutWidget)
        self.widget_G.setObjectName(u"widget_G")
        # 第三层布局，负责stack的卡片切换
        global lb_background_G
        lb_background_G = QLabel(self.widget_G)
        lb_background_G.setObjectName(u"lb_background_G")
        lb_background_G.setGeometry(QRect(0, 0, 1181, 671))
        lb_background_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background1.jpg"))
        #背景
        global lb_tell_talk_left_G
        lb_tell_talk_left_G = QLabel(self.widget_G)
        lb_tell_talk_left_G.setObjectName(u"lb_tell_talk_left_G")
        lb_tell_talk_left_G.setGeometry(QRect(290, 420, 631, 191))
        lb_tell_talk_left_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/talk1.jpg"))
        #对话

        self.pb_next_G = QPushButton(self.widget_G)
        self.pb_next_G.setObjectName(u"pb_next_G")
        self.pb_next_G.setGeometry(QRect(980, 570, 75, 23))
        self.pb_next_G.clicked.connect(Game_patch.game_next)
        #切换下一个部分的按钮

        global lb_name_story_G
        lb_name_story_G = QLabel(self.widget_G)
        lb_name_story_G.setObjectName(u"lb_name_story_G")
        lb_name_story_G.setGeometry(QRect(300, 320, 281, 81))
        lb_name_story_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/name2.jpg"))
        lb_name_story_G.setMargin(0)
        lb_name_story_G.setIndent(6)
        lb_name_story_G.setOpenExternalLinks(False)
        #名称栏

        ##self.grid_G.addWidget(self.widget_G, 0, 0, 1, 1)
        #######################six#####################
        #######################seven###################(end)
        #self.grid_H = QGridLayout(self.gridLayoutWidget)
        #self.grid_H.setObjectName(u"grid_H")
        #self.grid_H.setContentsMargins(0, 0, 0, 0)
        self.widget_H = QWidget(self.gridLayoutWidget)
        self.widget_H.setObjectName(u"widget_H")
        self.lb_background_H = QLabel(self.widget_H)
        self.lb_background_H.setObjectName(u"lb_background_H")
        self.lb_background_H.setGeometry(QRect(170, -90, 851, 781))
        self.lb_background_H.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background.jpg"))
        self.pb_exit_H = QPushButton(self.widget_H)
        self.pb_exit_H.setObjectName(u"pb_exit_H")
        self.pb_exit_H.setGeometry(QRect(520, 530, 181, 61))
        icon = QIcon()
        icon.addFile(u":/\u65b0\u524d\u7f00/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_exit_H.setIcon(icon)
        self.pb_exit_H.setIconSize(QSize(181, 61))
        self.pb_exit_H.setAutoRepeatDelay(300)

        #self.grid_H.addWidget(self.widget_H, 0, 0, 1, 1)
        #######################seven###################(end)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1183, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u673a\u68b0\u4e4b\u5fc3", None))
        ###############A########################
        self.pb_story_A.setText("")
        self.lb_backgroud_A.setText("")
        self.pb_save_A.setText("")
        self.lb_title_A.setText("")
        self.lb_huamn_left_A.setText("")
        self.pb_set_A.setText("")
        self.pb_start_A.setText("")
        ##################A####################

        ##################B####################
        self.lb_huamn_B.setText("")
        self.lb_background_B.setText("")
        self.lb_tell__B.setText("")
        self.lb_name_B.setText("")
        self.pb_next_B.setText(QCoreApplication.translate("MainWindow", u">next", None))
        ###################B##################

        ###################C##################
        self.lb_human_C.setText("")
        self.lb_background_C.setText("")
        self.lb_name_C.setText("")
        self.tell_talk_right_C.setText("")
        self.pb_next_C.setText(QCoreApplication.translate("MainWindow", u">next", None))
        ##################C###################

        ##################D###################
        self.lb_change_D.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\uff1a", None))
        self.lb_tell_D.setText("")
        self.lb_huamn_left_D.setText("")
        self.lb_name_D.setText("")
        self.pb_change_A_D.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.lb_backgroud_D.setText("")
        #################D###################

        #################E###################
        self.lb_background_E.setText("")
        self.pb_change_B_E.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lb_name_E.setText("")
        self.pb_change_A_E.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.lb_tell_E.setText("")
        self.lb_huamn_E.setText("")
        self.lb_change_E.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\uff1a", None))
        ################E##################

        ################F##################
        self.pb_change_C_F.setText(QCoreApplication.translate("MainWindow", u"C", None))
        lb_backgroud_F.setText("")
        self.pb_change_A_F.setText(QCoreApplication.translate("MainWindow", u"A", None))
        lb_human_F.setText("")
        self.pb_change_B_F.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lb_change_F.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\uff1a", None))
        lb_name_talk_left_F.setText("")
        lb_tell_talk_left_F.setText("")
        #################F#################

        #################G#################
        lb_background_G.setText("")
        lb_tell_talk_left_G.setText("")
        lb_name_story_G.setText("")
        self.pb_next_G.setText(QCoreApplication.translate("MainWindow", u">next", None))
        #################G#################

        #################H#################
        self.lb_background_H.setText("感谢游玩，未完待续")
        self.pb_exit_H.setText("退出")
        #################H#################
        #global sw_stack
        global sw_stack
        sw_stack = QStackedWidget()
        self.grid_main_A.addWidget(sw_stack)
        sw_stack.addWidget(self.widget_A)
        sw_stack.addWidget(self.widget_B)
        sw_stack.addWidget(self.widget_C)
        sw_stack.addWidget(self.widget_D)
        sw_stack.addWidget(self.widget_E)
        sw_stack.addWidget(self.widget_F)
        sw_stack.addWidget(self.widget_G)
        sw_stack.addWidget(self.widget_H)

        #self.setLayout(self.grid_main_A)#相对布局
        #把所用的小模块的布局添加进stack
    @classmethod
    def change_widget(self,count):#设置当前可见的选项卡索引i为输入值
        print('5')
        global sw_stack
        sw_stack.setCurrentIndex(count)
        Ui_MainWindow.change_widget(self, count=0)
        # retranslateUi

class Game_card(object):
    #卡片式切换，调用写好的布局，切换素材来达到对话游戏的效果，实际就是个轮子
    #sw_stack = None
    #sw_stack = None
    global icon1, icon2, icon3,img_date,text_date
    global lb_backgroud_A,lb_title_A,lb_huamn_left_A,pb_start_A,pb_set_A,pb_save_A,lb_huamn_B,\
        lb_background_B,lb_tell__B,lb_name_B,lb_background_C,lb_human_C,lb_name_C,tell_talk_right_C,\
        lb_tell_D,lb_huamn_left_D,lb_name_D,lb_backgroud_D,lb_background_E,lb_name_E,lb_tell_E,lb_huamn_E,\
        lb_backgroud_F,lb_human_F,lb_name_talk_left_F,lb_tell_talk_left_F,lb_background_G,lb_tell_talk_left_G,\
        lb_name_story_G
    def __init__(self,game_process):
        self.game_process = game_process
        #self.lb_name_story_G = lb_name_story_G
        #self.lb_background_G = lb_background_G
        #self.lb_tell_talk_left_G =lb_tell_talk_left_G
        self.main_game(self)
        self.talk_left(self)
        self.talk_right(self)
        self.change_one(self)
        self.change_two(self)
        self.change_three(self)

    @classmethod
    def main_game(self):
        global sw_stack
        sw_stack.setCurrentIndex(0)
        #Ui_MainWindow.change_widget(self, count=0)
        self.lb_backgroud_A.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background1.jpg"))
        self.lb_title_A.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/title.jpg"))
        self.lb_huamn_left_A.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/sisiter2.png"))
        self.pb_start_A.setIcon(icon3)
        self.pb_set_A.setIcon(icon2)
        self.pb_save_A.setIcon(icon1)

    @classmethod
    def talk_left(self,game_process):
        global sw_stack
        sw_stack.setCurrentIndex(1)
        #Ui_MainWindow.change_widget(self, count=1)
        if game_process == 'A1':
            self.lb_huamn_B.setPixmap(QPixmap(img_date['sister_left'][1]))
            self.lb_background_B.setPixmap(QPixmap(img_date['sister_left'][1]))
            self.lb_tell__B.setPixmap(QPixmap(img_date['sister_left'][1]))
            self.lb_name_B.setPixmap(QPixmap(img_date['sister_left'][1]))

    @classmethod
    def talk_right(self,game_process):
        global sw_stack
        sw_stack.setCurrentIndex(2)
        #Ui_MainWindow.change_widget(self, count=2)
        if game_process == 'B1':
            self.lb_human_C.setPixmap(QPixmap(img_date['sister_left'][1]))
            self.lb_background_C.setPixmap(QPixmap(img_date['sister_left'][1]))
            self.lb_name_C.setPixmap(QPixmap(img_date['sister_left'][1]))
            self.tell_talk_right_C.setPixmap(QPixmap(img_date['sister_left'][1]))

    @classmethod
    def change_one(self,game_process):
        global sw_stack
        sw_stack.setCurrentIndex(3)
        #Ui_MainWindow.change_widget(self, count=3)
        if game_process == 'B1':
            self.lb_tell_D.setPixmap(QPixmap(img_date['sister_left'][1]))
            self.lb_huamn_left_D.setPixmap(QPixmap(img_date['sister_left'][1]))
            self.lb_name_D.setPixmap(QPixmap(img_date['sister_left'][1]))
            self.lb_backgroud_D.setPixmap(QPixmap(img_date['sister_left'][1]))

    @classmethod
    def change_two(self,game_process):
        global sw_stack
        sw_stack.setCurrentIndex(4)
        #Ui_MainWindow.change_widget(self, count=4)
        if game_process == 'B1':
            self.lb_background_E.setPixmap(QPixmap(img_date['sister_left'][1]))
            self.lb_name_E.setPixmap(QPixmap(img_date['sister_left'][1]))
            self.lb_tell_E.setPixmap(QPixmap(img_date['sister_left'][1]))
            self.lb_huamn_E.setPixmap(QPixmap(
                img_date['sister'][1]))

    @classmethod
    def change_three(self,game_process):
        global sw_stack,lb_backgroud_F,lb_human_F
        sw_stack.setCurrentIndex(5)
        #Ui_MainWindow.change_widget(self, count=5)
        if game_process == 'B6/F1':
            lb_backgroud_F.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background3.jpg"))
            lb_human_F.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/player1.png"))
            lb_name_talk_left_F.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/name2.jpg"))
            lb_tell_talk_left_F.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/talk7.jpg"))

    @classmethod
    def talk_story(self,game_process):
        print('5')
        #time.sleep(3)
        global sw_stack,lb_tell_talk_left_G,lb_name_story_G
        sw_stack.setCurrentIndex(6)
        #time.sleep(3)

        print(game_process)
        #Ui_MainWindow.change_widget(self, count=6)
        print('6')
        if game_process == 'B1':
            lb_background_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background1.jpg"))
            lb_tell_talk_left_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/talk1.jpg"))
            lb_name_story_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/name2.jpg"))

            #lb_huamn_G.setPixmap(QPixmap(img_date['sister_left'][1]))
            print('ok')

        elif game_process == 'B2':
            lb_background_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background1.jpg"))
            lb_tell_talk_left_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/talk2.jpg"))
            lb_name_story_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/name2.jpg"))

        elif game_process == 'B3':
            lb_background_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background1.jpg"))
            lb_tell_talk_left_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/talk3.jpg"))
            lb_name_story_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/name2.jpg"))

        elif game_process == 'B4':
            lb_background_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background2.jpg"))
            lb_tell_talk_left_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/talk4.jpg"))
            lb_name_story_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/name2.jpg"))

        elif game_process == 'B5':
            lb_background_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background3.jpg"))
            lb_tell_talk_left_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/talk5.jpg"))
            lb_name_story_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/name2.jpg"))

        elif game_process == 'B6':
            lb_background_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/background3.jpg"))
            lb_tell_talk_left_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/talk6.jpg"))
            lb_name_story_G.setPixmap(QPixmap(u":/\u65b0\u524d\u7f00/name2.jpg"))

    @classmethod
    def game_end(self):
        global sw_stack
        sw_stack.setCurrentIndex(7)
        #Ui_MainWindow.change_widget(self, count=7)

class Game_patch(object):
    #包含一些比较散的函数，不能包含为一类，用于处理或完成一些比较麻烦的小需求和优化
    #@classmethod
    #def main_save(self):
    #    self.MainWindow = QtWidgets.QMainWindow()
    #    ui = Ui_MainWindow(count=0)  # 创建PyQt设计的窗体对象
    #    ui.setupUi(self.MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    #    self.MainWindow.show()
    @classmethod
    def game_A(self):
        #用于判断按钮A是否按下
        global button_countA
        button_countA = 1
        print('A')

    @classmethod
    def game_B(self):
        # 用于判断按钮B是否按下
        global button_countB
        button_countB = 1
        print('B')

    @classmethod
    def game_C(self):
        # 用于判断按钮C是否按下
        global button_countC
        button_countC = 1

    @classmethod
    def game_next(self):#用于判断next按钮是否按下
        global continue_count_next
        continue_count_next = 1
        print('next')

    @classmethod
    def game_wait(self):#窗口的生命周期维持
        "Erorr:废弃的函数"
        count = 0
        global attribute
        global continue_count_next,button_countA,button_countB,button_countC
        if attribute == 'next':
            while continue_count_next == 1:
                count+=1
            continue_count_next =0

        else:
            while button_countA == 1 or button_countB == 1 or button_countC == 1:
                count+=1
            button_countA = 0
            button_countB = 0
            button_countB = 0

    @classmethod
    def game_back(self):
        #用于处理进程码在游戏新开始进入game_start的if会向下一部分导致的问题。
        global back_date,game_process
        count=0
        for w in back_date:
            if w == game_process:
                game_process = back_date[count-1]
            count += 1


    @classmethod
    def game_process_count(self):#判断此时的进程码对应的各个控件的素材的index
        global game_process,index_name,index_tell,index_human,index_background
        if game_process == 'B1':
            index_human = 0
            index_name = 0
            index_tell = 0
            index_background = 0

        elif game_process == 'B2':
            game_process = 'B1'
            index_human = 0
            index_name = 0
            index_tell = 0
            index_background = 0

        elif game_process == 'B3':
            game_process = 'B2'
            index_human = 0
            index_name = 0
            index_tell = 0
            index_background = 4

        elif game_process == 'B4':
            game_process = 'B3'
            index_human = 0
            index_name = 0
            index_tell = 0
            index_background = 0

        elif game_process == 'B5':
            game_process = 'B4'
            index_human = 0
            index_name = 0
            index_tell = 0
            index_background = 0

        elif game_process == 'B6':
            game_process = 'B5'
            index_human = 0
            index_name = 0
            index_tell = 0
            index_background = 0
        elif game_process == 'B6/F1':
            game_process = 'B6'
            index_human = 0
            index_name = 0
            index_tell = 0
            index_background = 0
        elif game_process == 'B6/F1/B1':
            game_process = 'B6/F1'
            index_human = 0
            index_name = 0
            index_tell = 0
            index_background = 0
        elif game_process == 'B6/F1/B1/H':
            index_human = 0
            index_name = 0
            index_tell = 0
            index_background = 0
        elif game_process == 'B6/F2/B1':
            game_process = 'B6/F1'
            index_human = 0
            index_name = 0
            index_tell = 0
            index_background = 0
        elif game_process == 'B6/F2/B1/H':
            index_human = 0
            index_name = 0
            index_tell = 0
            index_background = 0
        elif game_process == 'B6/F3/B1':
            game_process = 'B6/F1'
            index_human = 0
            index_name = 0
            index_tell = 0
            index_background = 0
        elif game_process == 'B6/F3/B1/H':
            index_human = 0
            index_name = 0
            index_tell = 0
            index_background = 0


class Game_function(object):
    def __init__(self,game_process):
        self.game_process = game_process
        #self.game_start(self)
        #self.game_save(self)
        #self.game_story(self)
        #self.game_set(self)

    "进程码："
    "1.由界面码的ABCDEFG和数字为一个小节。"
    "2.用/号分割."
    "3.数字为选择的选项或者游戏该小部分的对话步数等，堆积起来成为进程码"

    #开始界面的那几个功能
    @multitasking.task
    def game_start(self):
        #1.识别进程码
        #2.调用对应函数
        '原理：1.设置judgement为0'
        '     2.if,elif 判断游戏进程，进入该进程步骤，将judgement设置为1'
        '     3.if or 有两个判断量，一个就是进程码，另一个是judgement,如果其为1，就可以正常进行游戏进程'
        'waring:ABCDG这些类型通过单个if就可以判断，EF需要if的下一级内层if判断，先用切片判断界面码，下级if再进行判断数字'
        '优化建议：3.10switch语句'
        judgement = 0#用于判断进程码的识别是否完成，0为否，1为完成
        global continue_count_next,button_countA,button_countB,button_countC
        global game_process
        global attribute
        print(game_process)
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
        if game_process == 'B1' or judgement == 1:
            #2089年，你‘出生’了

            judgement = 1
            #print('1')
            print('2')
            Game_card.talk_story(game_process = game_process)
            attribute = 'A'
            #Game_patch.game_wait(self)
            count = 0
            while continue_count_next == 0:
                pass
            continue_count_next = 0
            print('next1')

            game_process = 'B2'


        if game_process== 'B2' or judgement == 1:
            #你的父亲是一家科技公司STC的高级科学家
            print('next2')

            judgement = 1
            #print(2)
            Game_card.talk_story(game_process = game_process)
            while continue_count_next == 0:
                pass
            continue_count_next = 0
            print('3')
            game_process = 'B3'


        if game_process == 'B3' or judgement == 1:
            #造出了你，世界上第一个ＡＩ仿生人，作为他女儿的16岁礼物

            judgement = 1
            Game_card.talk_story(game_process = game_process)
            while continue_count_next == 0:
                pass
            continue_count_next = 0
            game_process = 'B4'

        if game_process == 'B4' or judgement == 1:
            #1年后，在一场车祸中，只有女儿活了下来

            judgement = 1
            Game_card.talk_story(game_process = game_process)
            print('B5test')
            while continue_count_next == 0:
                pass
            continue_count_next = 0
            game_process = 'B5'

        if game_process == 'B5' or judgement == 1:
            #你便隐藏身份去打工，赚钱供主人妹妹继续上学

            judgement = 1
            Game_card.talk_story(game_process = game_process)
            while continue_count_next == 0:
                pass
            continue_count_next = 0
            game_process = 'B6'

        if game_process == 'B6' or judgement == 1:
            #电视：ＳＴＣ公司最新发布会，具有自我意识的机器人，已经被发明，有部分机器人已经逃离了实验室，
            # 国家安全委员会发表称，已经接管了其工厂，在逃机器人全部被最高级通缉，你也会被此波及

            judgement = 1
            Game_card.talk_story(game_process = game_process)
            while continue_count_next == 0:
                pass
            continue_count_next = 0
            game_process = 'B6/F1'
        #print(game_process)

        if game_process == 'B6/F1' or judgement == 1:

            #你决定(B6/F)

            judgement = 1
            print('1')
            Game_card.change_three(game_process=game_process)
            while button_countA == 0 and button_countB == 0 and button_countC == 0:
                pass
            game_process = 'B6/F1'
            #continue_count_next = 0
            if button_countA == 1 and judgement == 1:
                'Error:以后在说写不完'
                #逃离(B6/F1)
                button_countA = 0
                #print('a')

                judgement = 1
                #Game_card.talk_story(game_process = game_process)#下面的三个选项有时间再做
                #while continue_count_next == 0:
                #    pass
                game_process = 'B6/F1/B1/H'
                if game_process == 'B6/F1/B1/H' or judgement == 1:
                    #game_process = 'B6/F1/B1/H'
                    judgement = 1
                    Game_card.game_end()

            elif button_countB == 1 and judgement == 1:
                print('b')
                #隐藏，伺机行动(B6/F2)
                button_countB = 0

                judgement = 1
                #Game_card.talk_story(game_process=game_process)
                game_process = 'B6/F2/B1/H'
                #while continue_count_next == 0:
                #    pass
                if game_process == 'B6/F2/B1/H' or judgement == 1:
                    #game_process = 'B6/F2/B1/H'
                    judgement = 1
                    Game_card.game_end()

            elif button_countC == 1 and judgement == 1:
                button_countC = 0
                print('c')

                judgement = 1
                #Game_card.talk_story(game_process=game_process)
                game_process = 'B6/F3/B1/H'
                #while continue_count_next == 0:
                #    pass
                #投案自首，爷不玩了(B6/F3/B1)
                if game_process == 'B6/F3/B1/H' or judgement == 1:
                    #game_process = 'B6/F3/B1/H'
                    judgement = 1
                    Game_card.game_end()

#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################

    def game_save(self):
        #1.用户选择存档
        #2.调用本地数据，调用game_start函数
        QMessageBox.information(MainWindow,"机械之心-提示：","敬请期待",QMessageBox.Yes,QMessageBox.Yes)

    def game_story(self):
        #1.游戏成就
        #2.游戏进程
        QMessageBox.information(MainWindow, "机械之心-提示：", "敬请期待", QMessageBox.Yes, QMessageBox.Yes)

    def game_set(self):
        #1.退出，保存数据
        #2.创作者信息
        QMessageBox.information(MainWindow, "机械之心-提示：", "敬请期待", QMessageBox.Yes, QMessageBox.Yes)

# 主方法，程序从此处启动PyQt设计的窗体

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")  # 设置窗口风格
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_MainWindow(count = 0)  # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    #Game_patch.main_save()
    add_open = 1  # 是
    #var = ui.Demo(MainWindow)
    # var.initUI()
    #var.setGeometry(600, 100, 100, 100)
    #var.show()
    #demo = Ui_MainWindow.Demo()
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
date_process.close()
date_process = open('date/date_process.txt','w+',encoding = 'UTF-8')
date_process.write(game_process)#game_process
date_process.close()