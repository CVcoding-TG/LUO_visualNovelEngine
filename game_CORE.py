import sys
import time
import multitasking
import tempfile
import os
import shutil
from pydub import AudioSegment
from pydub.playback import play
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UIdate import date
from playSound import voice_change,voice_stop,music_stop,music_change
import images.CreateUI.qt5.create_CA_rc
import images.CreateUI.qt5.create_CB_rc
import images.CreateUI.qt5.create_CC_rc
import images.CreateUI.qt5.create_CD_rc
import images.CreateUI.qt5.create_CE_rc
import images.CreateUI.qt5.create_CF_rc
import images.CreateUI.qt5.create_CG_rc
import images.CreateUI.qt5.create_CH_rc
import images.CreateUI.qt5.create_CI_rc

file_select =0#选中存档的编号

cnt = -1#计算schedule到哪了,因为进入card时要调用pb_start_CA-->cnt=-1,所以设置为-1



class Ui_Form(object):
    lb_background_CA = None
    global cnt
    def __init__(self):
        
        pass
    
    def nextCard(self):  # 用于切换下一个card
        
        global cnt
        print('nextCard')
        cnt+=1#推进进程
        
        if date["schedule"][cnt] == "B":
            self.frameB()
            
        elif date["schedule"][cnt] == "C":
            self.frameC()
            
        elif date["schedule"][cnt] == "D":
            self.frameD()

        elif date["schedule"][cnt] == "E":
            self.frameE()
            
        elif date["schedule"][cnt] == "F":
            self.frameF()
            
        elif date["schedule"][cnt] == "G":
            self.frameG()


    def setExit(self):# 用于set返回后让界面覆盖回原先的card
        
        print("setExit")
        
        if cnt == 0:
            self.frameA()
            
        elif date["schedule"][cnt] == "B":
            self.frameB()

        elif date["schedule"][cnt] == "C":
            self.frameC()

        elif date["schedule"][cnt] == "D":
            self.frameD()

        elif date["schedule"][cnt] == "E":
            self.frameE()

        elif date["schedule"][cnt] == "F":
            self.frameF()

        elif date["schedule"][cnt] == "G":
            self.frameG()
        
        
    def fileExit(self):# 用于file返回后让界面覆盖回原先的card
        
        print("fileExit")
        
        self.frameA()
        
        
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1020)
        
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 1922, 1022))
        
        
        #main总布局
        
        self.gridLayout_Main = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_Main.setObjectName(u"gridLayout_Main")
        self.gridLayout_Main.setContentsMargins(0, 0, 0, 0)
        
        
        #装下每一个卡片的stack widget
        
        self.sw_Main = QStackedWidget(self.gridLayoutWidget)
        self.sw_Main.setObjectName(u"sw_Main")
        
        
        #人物在左边的page
        
        self.page_CB = QWidget()
        self.page_CB.setObjectName(u"page_CB")
        
        
        #pageB的背景
        
        self.lb_background_CB = QLabel(self.page_CB)
        self.lb_background_CB.setObjectName(u"lb_background_CB")
        self.lb_background_CB.setGeometry(QRect(0, 0, 1920, 1020))
        self.lb_background_CB.setPixmap(QPixmap(u":/new/Create_B/lb_background_CB.png"))
        
        
        #pageB的人物
        
        self.lb_character_CB = QLabel(self.page_CB)
        self.lb_character_CB.setObjectName(u"lb_character_CB")
        self.lb_character_CB.setGeometry(QRect(40, 240, 540, 770))
        self.lb_character_CB.setPixmap(QPixmap(u":/new/Create_B/lb_character_CB.png"))
        
        
        #pageB的next按钮兼任对话框
        
        self.pb_next_CB = QPushButton(self.page_CB)
        self.pb_next_CB.setObjectName(u"pb_next_CB")
        self.pb_next_CB.setGeometry(QRect(190, 640, 1540, 330))
        self.pb_next_CB.setStyleSheet(u"background-color: rgba(255, 255, 255, 150);")
        self.pb_next_CB.clicked.connect(self.nextCard)
        
        
        #pageB的对话文本
        
        self.lb_text_CB = QLabel(self.page_CB)
        self.lb_text_CB.setObjectName(u"lb_text_CB")
        self.lb_text_CB.setGeometry(QRect(190, 640, 911, 161))
        self.lb_text_CB.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        
        #pageB的人物名称
        
        self.lb_name_CB = QLabel(self.page_CB)
        self.lb_name_CB.setObjectName(u"lb_name_CB")
        self.lb_name_CB.setGeometry(QRect(452, 586, 121, 41))
        self.lb_name_CB.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        
        #pageB的设置按钮
        
        self.pb_set_CB = QPushButton(self.page_CB)
        self.pb_set_CB.setObjectName(u"pb_set_CB")
        self.pb_set_CB.setGeometry(QRect(1850, 20, 40, 40))
        self.pb_set_CB.setStyleSheet(u"font: 700 15pt \"Terminal\";")
        self.pb_set_CB.clicked.connect(self.frameH)
        
        self.sw_Main.addWidget(self.page_CB)
        
        
        #开始界面的page
        
        self.page_CA = QWidget()
        self.page_CA.setObjectName(u"page_CA")


        # pageA的背景
        
        self.lb_background_CA = QLabel(self.page_CA)
        self.lb_background_CA.setObjectName(u"lb_background_CA")
        self.lb_background_CA.setGeometry(QRect(0, 0, 1920, 1020))
        self.lb_background_CA.setPixmap(QPixmap(u":/new/Create_A/lb_bakground_CA.jpg"))
        
        
        #pageA的标题
        
        self.lb_title_CA = QLabel(self.page_CA)
        self.lb_title_CA.setObjectName(u"lb_title_CA")
        self.lb_title_CA.setGeometry(QRect(70, 200, 651, 91))
        self.lb_title_CA.setStyleSheet(u"font: italic 100pt \"Monotype Corsiva\";")
        
        
        #pageA的版本
        
        self.lb_edition_CA = QLabel(self.page_CA)
        self.lb_edition_CA.setObjectName(u"lb_edition_CA")
        self.lb_edition_CA.setGeometry(QRect(130, 300, 271, 41))
        self.lb_edition_CA.setStyleSheet(u"font: 32pt \"Verdana\";")


        # pageA的开始按钮
        
        self.pb_start_CA = QPushButton(self.page_CA)
        self.pb_start_CA.setObjectName(u"pb_start_CA")
        self.pb_start_CA.setGeometry(QRect(220, 430, 281, 91))
        self.pb_start_CA.setStyleSheet(u"font: 36pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.pb_start_CA.setIconSize(QSize(281, 91))
        self.pb_start_CA.clicked.connect(self.nextCard)


        # pageA的游戏介绍文档
        
        self.pb_file_CA = QPushButton(self.page_CA)
        self.pb_file_CA.setObjectName(u"pb_file_CA")
        self.pb_file_CA.setGeometry(QRect(220, 560, 281, 91))
        self.pb_file_CA.setStyleSheet(u"font: 36pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.pb_file_CA.clicked.connect(self.frameI)


        # pageA的设置按钮
        
        self.pb_set_CA = QPushButton(self.page_CA)
        self.pb_set_CA.setObjectName(u"pb_set_CA")
        self.pb_set_CA.setGeometry(QRect(220, 690, 281, 91))
        self.pb_set_CA.setStyleSheet(u"font: 36pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.pb_set_CA.clicked.connect(self.frameH)
        
        self.sw_Main.addWidget(self.page_CA)


        # 人物在右边的page
        
        self.page_CC = QWidget()
        self.page_CC.setObjectName(u"page_CC")
        
        
        #pageC的背景
        
        self.lb_background_CC = QLabel(self.page_CC)
        self.lb_background_CC.setObjectName(u"lb_background_CC")
        self.lb_background_CC.setGeometry(QRect(0, 0, 1920, 1020))
        self.lb_background_CC.setPixmap(QPixmap(u":/new/Create_C/lb_background_CC.png"))


        # pageC的人物名称
        
        self.lb_name_CC = QLabel(self.page_CC)
        self.lb_name_CC.setObjectName(u"lb_name_CC")
        self.lb_name_CC.setGeometry(QRect(1347, 586, 121, 41))
        self.lb_name_CC.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")


        # pageC的人物
        
        self.lb_character_CC = QLabel(self.page_CC)
        self.lb_character_CC.setObjectName(u"lb_character_CC")
        self.lb_character_CC.setGeometry(QRect(1340, 240, 540, 770))
        self.lb_character_CC.setPixmap(QPixmap(u":/new/Create_C/lb_character_CC.png"))


        # pageC的next按钮兼任对话框
        
        self.pb_next_CC = QPushButton(self.page_CC)
        self.pb_next_CC.setObjectName(u"pb_next_CC")
        self.pb_next_CC.setGeometry(QRect(190, 640, 1540, 330))
        self.pb_next_CC.setStyleSheet(u"background-color: rgba(255, 255, 255, 150);")
        self.pb_next_CC.clicked.connect(self.nextCard)


        # pageC对话文本
        
        self.lb_text_CC = QLabel(self.page_CC)
        self.lb_text_CC.setObjectName(u"lb_text_CC")
        self.lb_text_CC.setGeometry(QRect(820, 640, 911, 161))
        self.lb_text_CC.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")


        # pageC的设置按钮
        
        self.pb_set_CC = QPushButton(self.page_CC)
        self.pb_set_CC.setObjectName(u"pb_set_CC")
        self.pb_set_CC.setGeometry(QRect(1850, 20, 40, 40))
        self.pb_set_CC.setStyleSheet(u"font: 700 15pt \"Terminal\";")
        self.pb_set_CC.clicked.connect(self.frameH)
        
        self.sw_Main.addWidget(self.page_CC)
        
        
        self.lb_background_CC.raise_()
        self.lb_character_CC.raise_()
        self.lb_name_CC.raise_()
        self.pb_next_CC.raise_()
        self.lb_text_CC.raise_()
        self.pb_set_CC.raise_()


        # 有一个按钮的page
        
        self.page_CD = QWidget()
        self.page_CD.setObjectName(u"page_CD")
        
        
        #pageD的背景
        
        self.lb_background_CD = QLabel(self.page_CD)
        self.lb_background_CD.setObjectName(u"lb_background_CD")
        self.lb_background_CD.setGeometry(QRect(0, 0, 1920, 1020))
        self.lb_background_CD.setPixmap(QPixmap(u":/new/Create_D/lb_background_CD.png"))
        
        
        #pageD的设置按钮
        
        self.pb_set_CD = QPushButton(self.page_CD)
        self.pb_set_CD.setObjectName(u"pb_set_CD")
        self.pb_set_CD.setGeometry(QRect(1850, 20, 40, 40))
        self.pb_set_CD.setStyleSheet(u"font: 700 15pt \"Terminal\";")
        self.pb_set_CD.clicked.connect(self.frameH)


        # pageD的第一个选择按钮
        
        self.pb_choiceI_CD = QPushButton(self.page_CD)
        self.pb_choiceI_CD.setObjectName(u"pb_choiceI_CD")
        self.pb_choiceI_CD.setGeometry(QRect(685, 440, 580, 141))
        self.pb_choiceI_CD.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);\n"
"font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        
        self.sw_Main.addWidget(self.page_CD)


        # 有两个选项的page
        
        
        self.page_CE = QWidget()
        self.page_CE.setObjectName(u"page_CE")


        # pageE的背景
        
        
        self.lb_background_CE = QLabel(self.page_CE)
        self.lb_background_CE.setObjectName(u"lb_background_CE")
        self.lb_background_CE.setGeometry(QRect(0, 0, 1920, 1020))
        self.lb_background_CE.setPixmap(QPixmap(u":/new/Create_E/lb_background_CE.png"))


        # pageE的设置按钮
        
        self.pb_set_CE = QPushButton(self.page_CE)
        self.pb_set_CE.setObjectName(u"pb_set_CE")
        self.pb_set_CE.setGeometry(QRect(1850, 20, 40, 40))
        self.pb_set_CE.setStyleSheet(u"font: 700 15pt \"Terminal\";")
        self.pb_set_CE.clicked.connect(self.frameH)


        # pageE的第一个选择按钮
        
        self.pb_choiceI_CE = QPushButton(self.page_CE)
        self.pb_choiceI_CE.setObjectName(u"pb_choiceI_CE")
        self.pb_choiceI_CE.setGeometry(QRect(685, 290, 580, 141))
        self.pb_choiceI_CE.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);\n"
"font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        
        # pageE的第二个选择按钮
        
        self.pb_choiceII_CE = QPushButton(self.page_CE)
        self.pb_choiceII_CE.setObjectName(u"pb_choiceII_CE")
        self.pb_choiceII_CE.setGeometry(QRect(685, 640, 580, 141))
        self.pb_choiceII_CE.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);\n"
"font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        
        self.sw_Main.addWidget(self.page_CE)


        # 有三个选择按钮的page
        
        self.page_CF = QWidget()
        self.page_CF.setObjectName(u"page_CF")


        # pageF的背景
        
        self.lb_background_CF = QLabel(self.page_CF)
        self.lb_background_CF.setObjectName(u"lb_background_CF")
        self.lb_background_CF.setGeometry(QRect(0, 0, 1920, 1020))
        self.lb_background_CF.setPixmap(QPixmap(u":/new/Create_F/lb_background_CF.png"))


        # pageF的第一个选择按钮
        
        self.pb_choiceI_CF = QPushButton(self.page_CF)
        self.pb_choiceI_CF.setObjectName(u"pb_choiceI_CF")
        self.pb_choiceI_CF.setGeometry(QRect(685, 102, 580, 141))
        self.pb_choiceI_CF.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);\n"
"font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")


        # pageF的第二个选择按钮
        
        self.pb_choiceII_CF = QPushButton(self.page_CF)
        self.pb_choiceII_CF.setObjectName(u"pb_choiceII_CF")
        self.pb_choiceII_CF.setGeometry(QRect(685, 350, 580, 141))
        self.pb_choiceII_CF.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);\n"
"font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")


        # pageF的第三个选择按钮
        
        self.pb_choiceIII_CF = QPushButton(self.page_CF)
        self.pb_choiceIII_CF.setObjectName(u"pb_choiceIII_CF")
        self.pb_choiceIII_CF.setGeometry(QRect(685, 600, 580, 141))
        self.pb_choiceIII_CF.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);\n"
"font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")


        # pageF的设置按钮
        
        self.pb_set_CF = QPushButton(self.page_CF)
        self.pb_set_CF.setObjectName(u"pb_set_CF")
        self.pb_set_CF.setGeometry(QRect(20, 40, 40, 40))
        self.pb_set_CF.setStyleSheet(u"font: 700 15pt \"Terminal\";")
        self.pb_set_CF.clicked.connect(self.frameH)
        
        
        self.sw_Main.addWidget(self.page_CF)
        
        
        #只有对话的按钮的page
        
        self.page_CG = QWidget()
        self.page_CG.setObjectName(u"page_CG")


        # pageG的背景
        
        self.lb_background_CG = QLabel(self.page_CG)
        self.lb_background_CG.setObjectName(u"lb_background_CG")
        self.lb_background_CG.setGeometry(QRect(0, 0, 1920, 1020))
        self.lb_background_CG.setPixmap(QPixmap(u":/new/Create_G/lb_background_CG.png"))


        # pageG的设置按钮
        
        self.pb_set_CG = QPushButton(self.page_CG)
        self.pb_set_CG.setObjectName(u"pb_set_CG")
        self.pb_set_CG.setGeometry(QRect(1850, 40, 40, 40))
        self.pb_set_CG.setStyleSheet(u"font: 700 15pt \"Terminal\";")
        self.pb_set_CG.clicked.connect(self.frameH)


        # pageG的人物名称
        
        self.lb_name_CG = QLabel(self.page_CG)
        self.lb_name_CG.setObjectName(u"lb_name_CG")
        self.lb_name_CG.setGeometry(QRect(190, 586, 121, 41))
        self.lb_name_CG.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")


        # pageG的next按钮兼任对话框
        
        self.pb_next_CG = QPushButton(self.page_CG)
        self.pb_next_CG.setObjectName(u"pb_next_CG")
        self.pb_next_CG.setGeometry(QRect(190, 640, 1540, 330))
        self.pb_next_CG.setStyleSheet(u"background-color: rgba(255, 255, 255, 150);")
        self.pb_next_CG.clicked.connect(self.nextCard)
        
        
        # pageG的对话文本
        
        self.lb_text_CG = QLabel(self.page_CG)
        self.lb_text_CG.setObjectName(u"lb_text_CG")
        self.lb_text_CG.setGeometry(QRect(190, 640, 911, 161))
        self.lb_text_CG.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        
        self.sw_Main.addWidget(self.page_CG)
        
        
        #设置的page
        
        self.page_CH = QWidget()
        self.page_CH.setObjectName(u"page_CH")


        # pageH的背景
        
        self.lb_background_CH = QLabel(self.page_CH)
        self.lb_background_CH.setObjectName(u"lb_background_CH")
        self.lb_background_CH.setGeometry(QRect(0, 0, 1920, 1020))
        self.lb_background_CH.setPixmap(QPixmap(u":/new/Create_H/lb_background_CH.png"))


        # pageH的设置标题
        
        self.lb_title_CH = QLabel(self.page_CH)
        self.lb_title_CH.setObjectName(u"lb_title_CH")
        self.lb_title_CH.setGeometry(QRect(852, 25, 241, 71))
        self.lb_title_CH.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"font: 700 36pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(255, 255, 255);")


        # pageH的音效widget
        
        self.widget_audio_CH = QWidget(self.page_CH)
        self.widget_audio_CH.setObjectName(u"widget_audio_CH")
        self.widget_audio_CH.setGeometry(QRect(620, 130, 730, 230))


        # pageHaudio的背景
        
        self.lb_audioBackground_CH = QLabel(self.widget_audio_CH)
        self.lb_audioBackground_CH.setObjectName(u"lb_audioBackground_CH")
        self.lb_audioBackground_CH.setGeometry(QRect(0, 0, 731, 231))
        self.lb_audioBackground_CH.setStyleSheet(u"background-color: rgb(121, 121, 121);\n"
"")


        # pageHaudio的背景音乐大小文本
        
        self.lb_music_CH = QLabel(self.widget_audio_CH)
        self.lb_music_CH.setObjectName(u"lb_music_CH")
        self.lb_music_CH.setGeometry(QRect(21, 81, 91, 21))
        self.lb_music_CH.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")


        # pageHaudio的背景音乐跳动条
        
        self.hsd_music_CH = QSlider(self.widget_audio_CH)
        self.hsd_music_CH.setObjectName(u"hsd_music_CH")
        self.hsd_music_CH.setGeometry(QRect(111, 81, 611, 22))
        self.hsd_music_CH.setOrientation(Qt.Horizontal)


        # pageHaudio的音效标题
        
        self.lb_audio_CH = QLabel(self.widget_audio_CH)
        self.lb_audio_CH.setObjectName(u"lb_audio_CH")
        self.lb_audio_CH.setGeometry(QRect(0, 0, 191, 61))
        self.lb_audio_CH.setStyleSheet(u"font: italic 24pt \"Monotype Corsiva\";\n"
"background-color: rgb(255, 255, 255);")


        # pageHaudio的语音文本
        
        self.lb_voice_CH = QLabel(self.widget_audio_CH)
        self.lb_voice_CH.setObjectName(u"lb_voice_CH")
        self.lb_voice_CH.setGeometry(QRect(21, 121, 91, 21))
        self.lb_voice_CH.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")


        # pageHaudio的语音拖动条
        
        self.hsd_voice_CH = QSlider(self.widget_audio_CH)
        self.hsd_voice_CH.setObjectName(u"hsd_voice_CH")
        self.hsd_voice_CH.setGeometry(QRect(111, 121, 611, 22))
        self.hsd_voice_CH.setOrientation(Qt.Horizontal)


        # pageHaudio的的背景音乐的模糊装饰条
        
        self.lb_music_blur_CH = QLabel(self.widget_audio_CH)
        self.lb_music_blur_CH.setObjectName(u"lb_music_blur_CH")
        self.lb_music_blur_CH.setGeometry(QRect(21, 81, 701, 21))
        self.lb_music_blur_CH.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);")


        # pageHaudio的语音的模糊装饰条
        
        self.lb_voice_blur_CH = QLabel(self.widget_audio_CH)
        self.lb_voice_blur_CH.setObjectName(u"lb_voice_blur_CH")
        self.lb_voice_blur_CH.setGeometry(QRect(21, 121, 701, 21))
        self.lb_voice_blur_CH.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);")


        # pageHaudio的点击音效文本
        
        self.lb_clickSound_CH = QLabel(self.widget_audio_CH)
        self.lb_clickSound_CH.setObjectName(u"lb_clickSound_CH")
        self.lb_clickSound_CH.setGeometry(QRect(21, 160, 91, 21))
        self.lb_clickSound_CH.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")


        # pageHaudio的点击音效开关
        
        self.rb_clickSound_CH = QRadioButton(self.widget_audio_CH)
        self.rb_clickSound_CH.setObjectName(u"rb_clickSound_CH")
        self.rb_clickSound_CH.setGeometry(QRect(120, 160, 95, 20))


        # pageHaudio点击音效的模糊装饰条
        
        self.lb_clickSound_blur_CH = QLabel(self.widget_audio_CH)
        self.lb_clickSound_blur_CH.setObjectName(u"lb_clickSound_blur_CH")
        self.lb_clickSound_blur_CH.setGeometry(QRect(20, 160, 701, 21))
        self.lb_clickSound_blur_CH.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);")
        
        
        self.lb_audioBackground_CH.raise_()
        self.lb_clickSound_blur_CH.raise_()
        self.lb_voice_blur_CH.raise_()
        self.lb_music_blur_CH.raise_()
        self.lb_music_CH.raise_()
        self.hsd_music_CH.raise_()
        self.lb_audio_CH.raise_()
        self.lb_voice_CH.raise_()
        self.hsd_voice_CH.raise_()
        self.lb_clickSound_CH.raise_()
        self.rb_clickSound_CH.raise_()


        # pageH的存档数据的widget
        
        self.widget_date_CH = QWidget(self.page_CH)
        self.widget_date_CH.setObjectName(u"widget_date_CH")
        self.widget_date_CH.setGeometry(QRect(620, 400, 731, 451))


        # pageHdate的背景
        
        self.lb_dateBackground_CH = QLabel(self.widget_date_CH)
        self.lb_dateBackground_CH.setObjectName(u"lb_dateBackground_CH")
        self.lb_dateBackground_CH.setGeometry(QRect(2, -5, 731, 461))
        self.lb_dateBackground_CH.setStyleSheet(u"background-color: rgb(121, 121, 121);\n"
"")
        
        
        # pageHdate的DATE：文本
        
        self.lb_saveDate_CH = QLabel(self.widget_date_CH)
        self.lb_saveDate_CH.setObjectName(u"lb_saveDate_CH")
        self.lb_saveDate_CH.setGeometry(QRect(0, 0, 191, 61))
        self.lb_saveDate_CH.setStyleSheet(u"font: italic 24pt \"Monotype Corsiva\";\n"
"background-color: rgb(255, 255, 255);")


        # pageHdate的1号存档按钮
        
        self.pb_date1_CH = QPushButton(self.widget_date_CH)
        self.pb_date1_CH.setObjectName(u"pb_date1_CH")
        self.pb_date1_CH.setGeometry(QRect(80, 100, 171, 81))
        self.pb_date1_CH.clicked.connect(FileDate.file_one)
        
        
        # pageHdate的2号存档按钮
        
        self.pb_date2_CH = QPushButton(self.widget_date_CH)
        self.pb_date2_CH.setObjectName(u"pb_date2_CH")
        self.pb_date2_CH.setGeometry(QRect(280, 100, 171, 81))
        self.pb_date2_CH.clicked.connect(FileDate.file_two)


        # pageHdate的3号存档按钮
        
        self.pb_date3_CH = QPushButton(self.widget_date_CH)
        self.pb_date3_CH.setObjectName(u"pb_date3_CH")
        self.pb_date3_CH.setGeometry(QRect(480, 100, 171, 81))
        self.pb_date3_CH.clicked.connect(FileDate.file_three)


        # pageHdate的4号存档按钮
        
        self.pb_date4_CH = QPushButton(self.widget_date_CH)
        self.pb_date4_CH.setObjectName(u"pb_date4_CH")
        self.pb_date4_CH.setGeometry(QRect(80, 200, 171, 81))
        self.pb_date4_CH.clicked.connect(FileDate.file_four)


        # pageHdate的5号存档按钮
        
        self.pb_date5_CH = QPushButton(self.widget_date_CH)
        self.pb_date5_CH.setObjectName(u"pb_date5_CH")
        self.pb_date5_CH.setGeometry(QRect(280, 200, 171, 81))
        self.pb_date5_CH.clicked.connect(FileDate.file_five)


        # pageHdate的6号存档按钮
        
        self.pb_date6_CH = QPushButton(self.widget_date_CH)
        self.pb_date6_CH.setObjectName(u"pb_date6_CH")
        self.pb_date6_CH.setGeometry(QRect(480, 200, 171, 81))
        self.pb_date6_CH.clicked.connect(FileDate.file_six)


        # pageHdate的7号存档按钮
        
        self.pb_date7_CH = QPushButton(self.widget_date_CH)
        self.pb_date7_CH.setObjectName(u"pb_date7_CH")
        self.pb_date7_CH.setGeometry(QRect(80, 300, 171, 81))
        self.pb_date7_CH.clicked.connect(FileDate.file_seven)


        # pageHdate的8号存档按钮
        
        self.pb_date8_CH = QPushButton(self.widget_date_CH)
        self.pb_date8_CH.setObjectName(u"pb_date8_CH")
        self.pb_date8_CH.setGeometry(QRect(280, 300, 171, 81))
        self.pb_date8_CH.clicked.connect(FileDate.file_eight)


        # pageHdate的9号存档按钮
        
        self.pb_date9_CH = QPushButton(self.widget_date_CH)
        self.pb_date9_CH.setObjectName(u"pb_date9_CH")
        self.pb_date9_CH.setGeometry(QRect(480, 300, 171, 81))
        self.pb_date9_CH.clicked.connect(FileDate.file_nine)


        # pageHdate的存档按钮
        
        self.pb_saveDate_CH = QPushButton(self.widget_date_CH)
        self.pb_saveDate_CH.setObjectName(u"pb_saveDate_CH")
        self.pb_saveDate_CH.setGeometry(QRect(224, 23, 91, 31))
        self.pb_saveDate_CH.clicked.connect(file_save)


        # pageHdate的读档按钮
        
        self.pb_readDate_CH = QPushButton(self.widget_date_CH)
        self.pb_readDate_CH.setObjectName(u"pb_readDate_CH")
        self.pb_readDate_CH.setGeometry(QRect(330, 23, 91, 31))
        self.pb_readDate_CH.clicked.connect(file_read)


        # pageHdate的注释文本
        
        self.lb_ps_CH = QLabel(self.widget_date_CH)
        self.lb_ps_CH.setObjectName(u"lb_ps_CH")
        self.lb_ps_CH.setGeometry(QRect(430, 30, 271, 21))
        self.lb_ps_CH.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")


        # pageH的退出按钮
        
        self.pb_exit_CH = QPushButton(self.page_CH)
        self.pb_exit_CH.setObjectName(u"pb_exit_CH")
        self.pb_exit_CH.setGeometry(QRect(1700, 920, 181, 71))
        self.pb_exit_CH.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.pb_exit_CH.clicked.connect(self.setExit)
        
        
        self.sw_Main.addWidget(self.page_CH)

        #介绍故事内容（人物，地点，结局）的page
        
        self.page_CI = QWidget()
        self.page_CI.setObjectName(u"page_CI")
        
        
        # pageI的背景
        
        self.lb_bakcground_CI = QLabel(self.page_CI)
        self.lb_bakcground_CI.setObjectName(u"lb_bakcground_CI")
        self.lb_bakcground_CI.setGeometry(QRect(-1, -1, 1920, 1021))
        self.lb_bakcground_CI.setPixmap(QPixmap(u":/new/Create_I/lb_background_CI.png"))


        # pageI的左侧选项收纳框
        
        self.tb_box_CI = QToolBox(self.page_CI)
        self.tb_box_CI.setObjectName(u"tb_box_CI")
        self.tb_box_CI.setGeometry(QRect(0, 0, 500, 1021))
        self.tb_box_CI.setStyleSheet(u"")


        # pageI的左侧收纳框的第一个框（人物介绍）
        
        self.page_BoxI_CI = QWidget()
        self.page_BoxI_CI.setObjectName(u"page_BoxI_CI")
        self.page_BoxI_CI.setGeometry(QRect(0, 0, 500, 931))
        self.page_BoxI_CI.setMinimumSize(QSize(271, 0))
        
        
        # pageI的左侧收纳框的第一个框的第2个选项
        
        self.pb_BoxI1_CI = QPushButton(self.page_BoxI_CI)
        self.pb_BoxI1_CI.setObjectName(u"pb_BoxI1_CI")
        self.pb_BoxI1_CI.setGeometry(QRect(20, 190, 460, 120))
        self.pb_BoxI1_CI.setStyleSheet(u"background-color: rgba(124, 178, 224, 150);\n"
                                       "font: 24pt \"Microsoft YaHei UI\";")
        
        
        # pageI的左侧收纳框的第一个框的第3个选项
        
        self.pb_BoxI2_CI = QPushButton(self.page_BoxI_CI)
        self.pb_BoxI2_CI.setObjectName(u"pb_BoxI2_CI")
        self.pb_BoxI2_CI.setGeometry(QRect(20, 350, 460, 120))
        self.pb_BoxI2_CI.setStyleSheet(u"background-color: rgba(124, 178, 224, 150);\n"
                                       "font: 24pt \"Microsoft YaHei UI\";")
        
        
        # pageI的左侧收纳框的第一个框的第4个选项
        
        self.pb_BoxI3_CI = QPushButton(self.page_BoxI_CI)
        self.pb_BoxI3_CI.setObjectName(u"pb_BoxI3_CI")
        self.pb_BoxI3_CI.setGeometry(QRect(20, 510, 460, 120))
        self.pb_BoxI3_CI.setStyleSheet(u"background-color: rgba(124, 178, 224, 150);\n"
                                       "font: 24pt \"Microsoft YaHei UI\";")
        
        # pageI的左侧收纳框的第一个框的第0个选项
        
        self.pb_BoxI0_CI = QPushButton(self.page_BoxI_CI)
        self.pb_BoxI0_CI.setObjectName(u"pb_BoxI0_CI")
        self.pb_BoxI0_CI.setGeometry(QRect(20, 30, 460, 120))
        self.pb_BoxI0_CI.setStyleSheet(u"background-color: rgba(124, 178, 224, 150);\n"
                                       "font: 24pt \"Microsoft YaHei UI\";")
        
        
        # pageI的左侧收纳框的第一个框的背景
        self.lb_background_BoxI_CI = QLabel(self.page_BoxI_CI)
        self.lb_background_BoxI_CI.setObjectName(u"lb_background_BoxI_CI")
        self.lb_background_BoxI_CI.setGeometry(QRect(0, -35, 500, 1021))
        self.lb_background_BoxI_CI.setPixmap(QPixmap(u":/new/Create_I/lb_background_Box_CI.jpg"))
        
        
        self.tb_box_CI.addItem(self.page_BoxI_CI, u"\u4eba\u7269")
        
        self.lb_background_BoxI_CI.raise_()
        
        self.pb_BoxI1_CI.raise_()
        self.pb_BoxI2_CI.raise_()
        self.pb_BoxI3_CI.raise_()
        self.pb_BoxI0_CI.raise_()
        
        
        # pageI的左侧收纳框的第二个框（地点）
        
        self.page_BoxII_CI = QWidget()
        self.page_BoxII_CI.setObjectName(u"page_BoxII_CI")
        self.page_BoxII_CI.setGeometry(QRect(0, 0, 500, 931))

        
        # pageI的左侧收纳框的第二个框的第1个选项
        
        self.pb_BoxII0_CI = QPushButton(self.page_BoxII_CI)
        self.pb_BoxII0_CI.setObjectName(u"pb_BoxII0_CI")
        self.pb_BoxII0_CI.setGeometry(QRect(20, 30, 460, 120))
        self.pb_BoxII0_CI.setStyleSheet(u"background-color: rgba(124, 178, 224, 150);\n"
                                        "font: 24pt \"Microsoft YaHei UI\";")
        
        
        # pageI的左侧收纳框的第二个框的第2个选项
        
        self.pb_BoxII1_CI = QPushButton(self.page_BoxII_CI)
        self.pb_BoxII1_CI.setObjectName(u"pb_BoxII1_CI")
        self.pb_BoxII1_CI.setGeometry(QRect(20, 190, 460, 120))
        self.pb_BoxII1_CI.setStyleSheet(u"background-color: rgba(124, 178, 224, 150);\n"
                                        "font: 24pt \"Microsoft YaHei UI\";")
        
        
        # pageI的左侧收纳框的第二个框的第3个选项
        
        self.pb_BoxII2_CI = QPushButton(self.page_BoxII_CI)
        self.pb_BoxII2_CI.setObjectName(u"pb_BoxII2_CI")
        self.pb_BoxII2_CI.setGeometry(QRect(20, 350, 460, 120))
        self.pb_BoxII2_CI.setStyleSheet(u"background-color: rgba(124, 178, 224, 150);\n"
                                        "font: 24pt \"Microsoft YaHei UI\";")
        
        
        # pageI的左侧收纳框的第二个框的背景
        
        self.lb_background_BoxII_CI = QLabel(self.page_BoxII_CI)
        self.lb_background_BoxII_CI.setObjectName(u"lb_background_BoxII_CI")
        self.lb_background_BoxII_CI.setGeometry(QRect(0, -60, 500, 1011))
        self.lb_background_BoxII_CI.setPixmap(QPixmap(u":/new/Create_I/lb_background_Box_CI.jpg"))
        
        
        self.tb_box_CI.addItem(self.page_BoxII_CI, u"\u5730\u70b9")
        
        self.lb_background_BoxII_CI.raise_()
        self.pb_BoxII0_CI.raise_()
        self.pb_BoxII1_CI.raise_()
        self.pb_BoxII2_CI.raise_()
        
        
        # pageI的左侧收纳框的第三个框（结局）
        
        self.page_BoxIII_CI = QWidget()
        self.page_BoxIII_CI.setObjectName(u"page_BoxIII_CI")
        self.page_BoxIII_CI.setGeometry(QRect(0, 0, 500, 931))
        
        
        # pageI的左侧收纳框的第三个框的第1个选项
        
        self.pb_BoxIII0_CI = QPushButton(self.page_BoxIII_CI)
        self.pb_BoxIII0_CI.setObjectName(u"pb_BoxIII0_CI")
        self.pb_BoxIII0_CI.setGeometry(QRect(20, 30, 460, 120))
        self.pb_BoxIII0_CI.setStyleSheet(u"background-color: rgba(124, 178, 224, 150);\n"
                                         "font: 24pt \"Microsoft YaHei UI\";")
        
        
        # pageI的左侧收纳框的第三个框的第2个选项
        
        self.pb_BoxIII1_CI = QPushButton(self.page_BoxIII_CI)
        self.pb_BoxIII1_CI.setObjectName(u"pb_BoxIII1_CI")
        self.pb_BoxIII1_CI.setGeometry(QRect(20, 190, 460, 120))
        self.pb_BoxIII1_CI.setStyleSheet(u"background-color: rgba(124, 178, 224, 150);\n"
                                         "font: 24pt \"Microsoft YaHei UI\";")
        
        
        # pageI的左侧收纳框的第三个框的第3个选项
        
        self.pb_BoxIII2_CI = QPushButton(self.page_BoxIII_CI)
        self.pb_BoxIII2_CI.setObjectName(u"pb_BoxIII2_CI")
        self.pb_BoxIII2_CI.setGeometry(QRect(20, 350, 460, 120))
        self.pb_BoxIII2_CI.setStyleSheet(u"background-color: rgba(124, 178, 224, 150);\n"
                                         "font: 24pt \"Microsoft YaHei UI\";")
        
        
        # pageI的左侧收纳框的第三个框的背景
        
        self.lb_background_BoxIII_CI = QLabel(self.page_BoxIII_CI)
        self.lb_background_BoxIII_CI.setObjectName(u"lb_background_BoxIII_CI")
        self.lb_background_BoxIII_CI.setGeometry(QRect(0, -90, 500, 1021))
        self.lb_background_BoxIII_CI.setPixmap(QPixmap(u":/new/Create_I/lb_background_Box_CI.jpg"))
        
        
        # pageI的左侧收纳框的第三个框的第4个选项
        
        self.pb_BoxIII3_CI = QPushButton(self.page_BoxIII_CI)
        self.pb_BoxIII3_CI.setObjectName(u"pb_BoxIII3_CI")
        self.pb_BoxIII3_CI.setGeometry(QRect(20, 510, 460, 120))
        self.pb_BoxIII3_CI.setStyleSheet(u"background-color: rgba(124, 178, 224, 150);\n"
                                         "font: 24pt \"Microsoft YaHei UI\";")
        
        
        self.tb_box_CI.addItem(self.page_BoxIII_CI, u"\u7ed3\u5c40")
    
        self.lb_background_BoxIII_CI.raise_()
        
        self.pb_BoxIII0_CI.raise_()
        self.pb_BoxIII1_CI.raise_()
        self.pb_BoxIII2_CI.raise_()
        self.pb_BoxIII3_CI.raise_()
        
        
        # pageI的左侧收纳框的后方填充背景
        
        self.lb_backgroundLine_CI = QLabel(self.page_CI)
        self.lb_backgroundLine_CI.setObjectName(u"lb_backgroundLine_CI")
        self.lb_backgroundLine_CI.setGeometry(QRect(0, 0, 500, 1020))
        self.lb_backgroundLine_CI.setStyleSheet(u"background-color: rgb(27, 89, 138);")
        
        
        # pageI的右方控件左上出的装饰小框
        
        self.lb_boder_CI = QLabel(self.page_CI)
        self.lb_boder_CI.setObjectName(u"lb_boder_CI")
        self.lb_boder_CI.setGeometry(QRect(500, 0, 800, 90))
        self.lb_boder_CI.setStyleSheet(u"")
        self.lb_boder_CI.setPixmap(QPixmap(u":/new/Create_I/lb_boder_CI.png"))
        
        
        # pageI的右方控件中的展示图片
        
        self.lb_map_CI = QLabel(self.page_CI)
        self.lb_map_CI.setObjectName(u"lb_map_CI")
        self.lb_map_CI.setGeometry(QRect(510, 110, 861, 461))
        self.lb_map_CI.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lb_map_CI.setPixmap(QPixmap(u":/new/Create_I/lb_map_CI.jpg"))
        
        
        # pageI的右方控件中的展示文本
        
        self.lb_text_CI = QLabel(self.page_CI)
        self.lb_text_CI.setObjectName(u"lb_text_CI")
        self.lb_text_CI.setGeometry(QRect(510, 600, 1381, 391))
        self.lb_text_CI.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                      "font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        
        # pageI的右方控件中的退出按钮
        
        self.pb_exit_CI = QPushButton(self.page_CI)
        self.pb_exit_CI.setObjectName(u"pb_exit_CI")
        self.pb_exit_CI.setGeometry(QRect(1670, 870, 181, 71))
        self.pb_exit_CI.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
                                      "font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.pb_exit_CI.clicked.connect(self.fileExit)
        
        self.sw_Main.addWidget(self.page_CI)

        self.lb_bakcground_CI.raise_()
        self.lb_backgroundLine_CI.raise_()
        self.tb_box_CI.raise_()
        self.lb_map_CI.raise_()
        self.lb_boder_CI.raise_()
        self.lb_text_CI.raise_()
        self.pb_exit_CI.raise_()
        self.gridLayout_Main.addWidget(self.sw_Main, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
        self.sw_Main.setCurrentIndex(1)#初始化start界面
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        
        self.lb_background_CB.setText("")
        
        self.lb_character_CB.setText("")
        
        self.pb_next_CB.setText("")
        
        self.lb_text_CB.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u4eba\u6709\u4e09\u5927\u6b32\u671b\uff0c\u98df\u6b32\uff0cX\u6b32\uff0c\u7761\u7720\u6b32\u3002</p><p>\u5728\u8fd9\u4e09\u5927\u6b32\u671b\u5f53\u4e2d\uff0c\u56e0\u4e3a\u98df\u6b32\u662f\u6ee1\u8db3\u4eba\u7c7b\u751f\u5b58\u9700\u6c42\u7684\u6b32\u671b\uff0c\u6240\u4ee5\u6ee1\u8db3\u98df\u6b32\u7684\u884c\u4e3a\u5728\u8fd9\u4e09\u8005\u4e2d\u4f18\u5148\u662f\u7b2c\u4e00\u4f4d\u7684\u3002</p><p>\u5982\u679c\u5728\u8fdb\u98df\u4e2d\u5403\u4e0b\u4e86\u7f8e\u5473\u7684\u98df\u7269\uff0c\u4e5f\u80fd\u4f7f\u4eba\u7c7b\u65e0\u6bd4\u6109\u5feb\u3002</p><p>\u800c\u5728\u73b0\u5b9e\u751f\u6d3b\u4e2d\uff0c\u800c\u5728\u73b0\u5b9e\u751f\u6d3b\u4e2d\uff0c\u53ea\u5bf9\u4e8e\u8fd9\u79cd\u5feb\u611f\u7684\u6267\u7740\u8ffd\u6c42\u7684\u4eba\uff0c\u6211\u4eec\u901a\u5e38\u628a\u8fd9\u79cd\u4eba\u79f0\u4e3a\u7f8e\u98df\u5bb6\u3002</p></body></html>", None))
        
        self.lb_name_CB.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6211\uff1a</p></body></html>", None))
        
        self.pb_set_CB.setText(QCoreApplication.translate("Form", u"...", None))
        
        self.lb_background_CA.setText("")
        
        self.lb_title_CA.setText(QCoreApplication.translate("Form", u"Sweet Dream", None))
        
        self.lb_edition_CA.setText(QCoreApplication.translate("Form", u"DEMO:0.0.1", None))
       
        self.pb_start_CA.setText(QCoreApplication.translate("Form", u"Start", None))
        
        self.pb_file_CA.setText(QCoreApplication.translate("Form", u"File", None))
        
        self.pb_set_CA.setText(QCoreApplication.translate("Form", u"Set", None))
       
        self.lb_background_CC.setText("")
        
        self.lb_name_CC.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6211\uff1a</p></body></html>", None))
        
        self.lb_character_CC.setText("")
        
        self.pb_next_CC.setText("")
        
        self.lb_text_CC.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u4eba\u6709\u4e09\u5927\u6b32\u671b\uff0c\u98df\u6b32\uff0cX\u6b32\uff0c\u7761\u7720\u6b32\u3002</p><p align=\"right\">\u5728\u8fd9\u4e09\u5927\u6b32\u671b\u5f53\u4e2d\uff0c\u56e0\u4e3a\u98df\u6b32\u662f\u6ee1\u8db3\u4eba\u7c7b\u751f\u5b58\u9700\u6c42\u7684\u6b32\u671b\uff0c\u6240\u4ee5\u6ee1\u8db3\u98df\u6b32\u7684\u884c\u4e3a\u5728\u8fd9\u4e09\u8005\u4e2d\u4f18\u5148\u662f\u7b2c\u4e00\u4f4d\u7684\u3002</p><p align=\"right\">\u5982\u679c\u5728\u8fdb\u98df\u4e2d\u5403\u4e0b\u4e86\u7f8e\u5473\u7684\u98df\u7269\uff0c\u4e5f\u80fd\u4f7f\u4eba\u7c7b\u65e0\u6bd4\u6109\u5feb\u3002</p><p align=\"right\">\u800c\u5728\u73b0\u5b9e\u751f\u6d3b\u4e2d\uff0c\u800c\u5728\u73b0\u5b9e\u751f\u6d3b\u4e2d\uff0c\u53ea\u5bf9\u4e8e\u8fd9\u79cd\u5feb\u611f\u7684\u6267\u7740\u8ffd\u6c42\u7684\u4eba\uff0c\u6211\u4eec\u901a\u5e38\u628a\u8fd9\u79cd\u4eba\u79f0\u4e3a\u7f8e\u98df\u5bb6\u3002</p></body></html>", None))
        
        self.pb_set_CC.setText(QCoreApplication.translate("Form", u"...", None))
        
        self.lb_background_CD.setText("")
        
        self.pb_set_CD.setText(QCoreApplication.translate("Form", u"...", None))
        
        self.pb_choiceI_CD.setText(QCoreApplication.translate("Form", u"\u9e2d\u86cb\u6478\u9e2d\u86cb\uff0c\u7261\u86ce\u6478\u7261\u86ce", None))
        
        self.lb_background_CE.setText("")
        
        self.pb_set_CE.setText(QCoreApplication.translate("Form", u"...", None))
        
        self.pb_choiceI_CE.setText(QCoreApplication.translate("Form", u"\u5567\u5567\u5567\uff0c\u8fd9\u9762\u76f8\u4e0d\u592a\u597d\uff0c\u6211\u770b\u662f\u6ca1\u620f\u4e86", None))
        
        self.pb_choiceII_CE.setText(QCoreApplication.translate("Form", u"\u8fd9\u4f4d\u662f\u4eba\u4e2d\u4e4b\u9f99\uff0c\u751f\u6765\u5c31\u662f\u8981\u505a\u4eba\u4e0a\u4eba\u7684", None))
        
        self.lb_background_CF.setText("")
        
        self.pb_choiceI_CF.setText(QCoreApplication.translate("Form", u"\u5567\u5567\u5567\uff0c\u8fd9\u9762\u76f8\u4e0d\u592a\u597d\uff0c\u6211\u770b\u662f\u6ca1\u620f\u4e86", None))
        
        self.pb_choiceII_CF.setText(QCoreApplication.translate("Form", u"\u8fd9\u4f4d\u662f\u4eba\u4e2d\u4e4b\u9f99\uff0c\u751f\u6765\u5c31\u662f\u8981\u505a\u4eba\u4e0a\u4eba\u7684", None))
        
        self.pb_choiceIII_CF.setText(QCoreApplication.translate("Form", u"\u8fd9\u9762\u76f8\u771f\u662f\u5929\u795e\u4e0b\u51e1......\u5c06\u6765\u80af\u5b9a\u662f\u8981\u505a\n"
"\u7687\u5e1d\u7684", None))
        
        self.pb_set_CF.setText(QCoreApplication.translate("Form", u"...", None))
        
        self.lb_background_CG.setText("")
        
        self.pb_set_CG.setText(QCoreApplication.translate("Form", u"...", None))
        
        self.lb_name_CG.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6211\uff1a</p></body></html>", None))
        
        self.pb_next_CG.setText("")
        
        self.lb_text_CG.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u4eba\u6709\u4e09\u5927\u6b32\u671b\uff0c\u98df\u6b32\uff0cX\u6b32\uff0c\u7761\u7720\u6b32\u3002</p><p>\u5728\u8fd9\u4e09\u5927\u6b32\u671b\u5f53\u4e2d\uff0c\u56e0\u4e3a\u98df\u6b32\u662f\u6ee1\u8db3\u4eba\u7c7b\u751f\u5b58\u9700\u6c42\u7684\u6b32\u671b\uff0c\u6240\u4ee5\u6ee1\u8db3\u98df\u6b32\u7684\u884c\u4e3a\u5728\u8fd9\u4e09\u8005\u4e2d\u4f18\u5148\u662f\u7b2c\u4e00\u4f4d\u7684\u3002</p><p>\u5982\u679c\u5728\u8fdb\u98df\u4e2d\u5403\u4e0b\u4e86\u7f8e\u5473\u7684\u98df\u7269\uff0c\u4e5f\u80fd\u4f7f\u4eba\u7c7b\u65e0\u6bd4\u6109\u5feb\u3002</p><p>\u800c\u5728\u73b0\u5b9e\u751f\u6d3b\u4e2d\uff0c\u800c\u5728\u73b0\u5b9e\u751f\u6d3b\u4e2d\uff0c\u53ea\u5bf9\u4e8e\u8fd9\u79cd\u5feb\u611f\u7684\u6267\u7740\u8ffd\u6c42\u7684\u4eba\uff0c\u6211\u4eec\u901a\u5e38\u628a\u8fd9\u79cd\u4eba\u79f0\u4e3a\u7f8e\u98df\u5bb6\u3002</p></body></html>", None))
        
        self.lb_background_CH.setText("")
        
        self.lb_title_CH.setText(QCoreApplication.translate("Form", u"     \u8bbe\u7f6e", None))
        
        self.lb_audioBackground_CH.setText("")
        
        self.lb_music_CH.setText(QCoreApplication.translate("Form", u"\u80cc\u666f\u97f3\u4e50\uff1a", None))
        
        self.lb_audio_CH.setText(QCoreApplication.translate("Form", u"AUDIO\uff1a", None))
        
        self.lb_voice_CH.setText(QCoreApplication.translate("Form", u"\u8bed\u97f3\uff1a", None))
        
        self.lb_music_blur_CH.setText("")
        
        self.lb_voice_blur_CH.setText("")
        
        self.lb_clickSound_CH.setText(QCoreApplication.translate("Form", u"\u70b9\u51fb\u97f3\u6548\uff1a", None))
        
        self.rb_clickSound_CH.setText(QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        
        self.lb_clickSound_blur_CH.setText("")
        
        self.lb_dateBackground_CH.setText("")
        
        self.lb_saveDate_CH.setText(QCoreApplication.translate("Form", u"DATE\uff1a", None))
        
        self.pb_date1_CH.setText(QCoreApplication.translate("Form", u"\u5b58\u68631\uff08\u65e5\u671f\uff09", None))
        
        self.pb_date2_CH.setText(QCoreApplication.translate("Form", u"\u5b58\u68632\uff08\u65e5\u671f\uff09", None))
        
        self.pb_date3_CH.setText(QCoreApplication.translate("Form", u"\u5b58\u68633\uff08\u65e5\u671f\uff09", None))
        
        self.pb_date4_CH.setText(QCoreApplication.translate("Form", u"\u5b58\u68634\uff08\u65e5\u671f\uff09", None))
        
        self.pb_date5_CH.setText(QCoreApplication.translate("Form", u"\u5b58\u68635\uff08\u65e5\u671f\uff09", None))
        
        self.pb_date6_CH.setText(QCoreApplication.translate("Form", u"\u5b58\u68636\uff08\u65e5\u671f\uff09", None))
        
        self.pb_date7_CH.setText(QCoreApplication.translate("Form", u"\u5b58\u68637\uff08\u65e5\u671f\uff09", None))
        
        self.pb_date8_CH.setText(QCoreApplication.translate("Form", u"\u5b58\u68638\uff08\u65e5\u671f\uff09", None))
        
        self.pb_date9_CH.setText(QCoreApplication.translate("Form", u"\u5b58\u68639\uff08\u65e5\u671f\uff09", None))
        
        self.pb_saveDate_CH.setText(QCoreApplication.translate("Form", u"\u5b58\u6863", None))
        
        self.pb_readDate_CH.setText(QCoreApplication.translate("Form", u"\u8bfb\u6863", None))
        
        self.lb_ps_CH.setText(QCoreApplication.translate("Form", u"PS\uff1a\u70b9\u51fb\u6863\u6848\u540e\u9009\u62e9\u5b58\u6863/\u8bfb\u6863", None))
        
        self.pb_exit_CH.setText(QCoreApplication.translate("Form", u"EXIT", None))
        
        self.lb_bakcground_CI.setText("")
        
        self.pb_BoxI1_CI.setText(QCoreApplication.translate("Form", u"\u6df3\u5e73\u533b\u751f", None))
        
        self.pb_BoxI2_CI.setText(QCoreApplication.translate("Form", u"god", None))
        
        self.pb_BoxI3_CI.setText(QCoreApplication.translate("Form", u"\u98df\u96ea\u6c49", None))
        
        self.pb_BoxI0_CI.setText(QCoreApplication.translate("Form", u"\u7530\u6240\u6d69\u4e8c", None))
        
        self.lb_background_BoxI_CI.setText("")
        
        self.tb_box_CI.setItemText(self.tb_box_CI.indexOf(self.page_BoxI_CI), QCoreApplication.translate("Form", u"\u4eba\u7269", None))
        
        self.pb_BoxII0_CI.setText(QCoreApplication.translate("Form", u"\u7ea2\u9b54\u9986", None))
        
        self.pb_BoxII1_CI.setText(QCoreApplication.translate("Form", u"\u65e0\u8d44\u683c\u533b\u9662", None))
        
        self.pb_BoxII2_CI.setText(QCoreApplication.translate("Form", u"\u91ce\u517d\u5e9c\u90b8", None))
        
        self.lb_background_BoxII_CI.setText("")
        
        self.tb_box_CI.setItemText(self.tb_box_CI.indexOf(self.page_BoxII_CI), QCoreApplication.translate("Form", u"\u5730\u70b9", None))
        
        self.pb_BoxIII0_CI.setText(QCoreApplication.translate("Form", u"\uff1f", None))
        
        self.pb_BoxIII1_CI.setText(QCoreApplication.translate("Form", u"\uff1f", None))
        
        self.pb_BoxIII2_CI.setText(QCoreApplication.translate("Form", u"\uff1f", None))
        
        self.lb_background_BoxIII_CI.setText("")
        
        self.pb_BoxIII3_CI.setText(QCoreApplication.translate("Form", u"\uff1f", None))
        
        self.tb_box_CI.setItemText(self.tb_box_CI.indexOf(self.page_BoxIII_CI), QCoreApplication.translate("Form", u"\u7ed3\u5c40", None))
        
        self.lb_backgroundLine_CI.setText("")
        
        self.lb_boder_CI.setText("")
        
        self.lb_map_CI.setText("")
        
        self.lb_text_CI.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-family:'Microsoft YaHei','Arial','Helvetica','sans-serif'; font-size:18px; color:#111111; background-color:#ffffff;\">\u7530\u6240\u6d69\u4e8c\uff081919\u5e748\u670810\u65e5\u20142034\u5e741\u670824\u65e5\uff09\uff0c</span><span style=\" font-family:'Microsoft YaHei','Arial','Helvetica','sans-serif'; font-size:18px; font-weight:700; color:#111111; background-color:rgba(16,110,190,0.176471);\">\u4e0b\u5317\u6cfd\u6cbc\u6c14</span></p><p><span style=\" font-family:'Microsoft YaHei','Arial','Helvetica','sans-serif'; font-size:18px; font-weight:700; color:#111111; background-color:rgba(16,110,190,0.176471);\">\u7814\u7a76\u6240\u9ad8\u7ea7\u5de5\u7a0b\u5e08\uff0c\u4f5c\u5bb6\uff0c\u97f3\u4e50\u5bb6</span><span style=\" font-family:'Microsoft YaHei','Arial','Helvetica','sans-serif'; font-size:18px; color:#111111; background-color:#ffffff;\">\u3002 \u4ed6\u51fa\u751f\u4e8e1919\u5e748\u670810</span></p><p><span style=\" font-family:'Microsoft YaHei','Arial','Helvetica','sans-"
                        "serif'; font-size:18px; color:#111111; background-color:#ffffff;\">\u65e5\uff0c\u901d\u4e16\u4e8e2034\u5e741\u670824\u65e5\u3002 \u4ed6\u6bd5\u4e1a\u4e8e\u4e0b\u5317\u6cfd\u5927\u5b66\uff0c\u6295\u8eab\u4e8e\u4e0b</span></p><p><span style=\" font-family:'Microsoft YaHei','Arial','Helvetica','sans-serif'; font-size:18px; color:#111111; background-color:#ffffff;\">\u5317\u6cfd\u5730\u533a\u7684\u6cbc\u6c14\u7530\u4e8b\u4e1a\uff0c\u66fe\u5e26\u98861145\u4eba\u5f00\u53d1\u4e0b\u5317\u6cfd\u5730\u533a\u7b2c14\u53f7</span></p><p><span style=\" font-family:'Microsoft YaHei','Arial','Helvetica','sans-serif'; font-size:18px; color:#111111; background-color:#ffffff;\">\u6cbc\u6c14\u7530\u5e76\u53d6\u5f97\u91cd\u5927\u79d1\u7814\u6210\u679c\u3002</span></p></body></html>", None))
        
        self.pb_exit_CI.setText(QCoreApplication.translate("Form", u"EXIT", None))
        
    # retranslateUi
    
    ###########################################function_card###########################################
    def frameA(self):#开始界面
        
        print("frameA")
        
        self.lb_background_CA.setPixmap(QPixmap(date["img_background"][cnt]))
        
        #self.lb_edition_CA.setStyleSheet(date["img_background"])
        #self.pb_start_CA.setStyleSheet(u"font: 36pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        #self.pb_file_CA.setStyleSheet(u"font: 36pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        #self.pb_set_CA.setStyleSheet(u"font: 36pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        voice_stop()
        voice_change(cnt,initialize=None)
        music_stop()
        music_change(cnt,initialize=None)
        
        self.sw_Main.setCurrentIndex(1)
        
        
    def frameB(self):#人物在左边的情况
        
        print("frameB")
        
        self.lb_background_CB.setPixmap(QPixmap(date["img_background"][cnt]))
        self.lb_character_CB.setPixmap(QPixmap(date["img_character"][cnt]))
        
        #self.pb_next_CB.setStyleSheet(u"background-color: rgba(255, 255, 255, 150);")
        #self.lb_text_CB.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        #self.lb_name_CB.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
        #                              "font: 700 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
       # self.pb_set_CB.setStyleSheet(u"font: 700 15pt \"Terminal\";")
        
        voice_stop()
        voice_change(cnt,initialize=None)
        
        if date["music"][cnt] != None:
            music_stop()
            music_change(cnt,initialize=None)
        
        self.sw_Main.setCurrentIndex(0)#因为designer编辑的时候先编辑了B,所以他的indedx对应也是0


    def frameC(self):#人物在右边的情况
        
        print("frameC")
        
        self.lb_background_CC.setPixmap(QPixmap(date["img_background"][cnt]))
        
        #self.lb_name_CC.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
        #                              "font: 700 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        
        self.lb_character_CC.setPixmap(QPixmap(date["img_character"][cnt]))
        
        #self.pb_next_CC.setStyleSheet(u"background-color: rgba(255, 255, 255, 150);")
        #self.lb_text_CC.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        #self.pb_set_CC.setStyleSheet(u"font: 700 15pt \"Terminal\";")
        
        voice_stop()
        voice_change(cnt,initialize=None)
        if date["music"][cnt] != None:
                music_stop()
                music_change(cnt,initialize=None)
            
        self.sw_Main.setCurrentIndex(2)


    def frameD(self):#一个选项
        
        print("frameD")

        self.lb_background_CD.setPixmap(QPixmap(date["img_background"][cnt]))
        
        #self.pb_set_CD.setStyleSheet(u"font: 700 15pt \"Terminal\";")
        #self.pb_choiceI_CD.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);\n"
        #                                 "font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        voice_stop()
        voice_change(cnt,initialize=None)
        if date["music"][cnt] != None:
                music_stop()
                music_change(cnt,initialize=None)

        self.sw_Main.setCurrentIndex(3)


    def frameE(self):#两个选项
        
        print("frameE")
        
        self.lb_background_CE.setPixmap(QPixmap(date["img_background"][cnt]))
        
        #self.pb_set_CE.setStyleSheet(u"font: 700 15pt \"Terminal\";")
        #self.pb_choiceI_CE.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);\n"
        #                                 "font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        #self.pb_choiceII_CE.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);\n"
        #                                  "font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        voice_stop()
        voice_change(cnt,initialize=None)
        if date["music"][cnt] != None:
                music_stop()
                music_change(cnt,initialize=None)

        self.sw_Main.setCurrentIndex(4)


    def frameF(self):#三个选项
        
        print("frameF")
        
        self.lb_background_CF.setPixmap(QPixmap(date["img_background"][cnt]))
        
        #self.pb_choiceI_CF.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);\n"
        #                                 "font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        #self.pb_choiceII_CF.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);\n"
        #                                  "font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        #self.pb_choiceIII_CF.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);\n"
        #                                   "font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        voice_stop()
        voice_change(cnt,initialize=None)
        if date["music"][cnt] != None:
                music_stop()
                music_change(cnt,initialize=None)

        self.sw_Main.setCurrentIndex(5)


    def frameG(self):#只有对话的过场
        
        print("frameG")
        
        self.lb_background_CG.setPixmap(QPixmap(date["img_background"][cnt]))
        
        #self.lb_name_CG.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
        #                              "font: 700 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        #self.pb_next_CG.setStyleSheet(u"background-color: rgba(255, 255, 255, 150);")
        #self.lb_text_CG.setStyleSheet(u"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        voice_stop()
        voice_change(cnt,initialize=None)
        if date["music"][cnt] != None:
                music_stop()
                music_change(cnt,initialize=None)

        self.sw_Main.setCurrentIndex(6)
    
    
    #@multitasking
    def frameH(self):#设置界面<-pb_set
        
        print("frameH")

        voice_stop()
        voice_change(cnt,initialize=None)
        music_stop()
        music_change(cnt,initialize=None)

        self.sw_Main.setCurrentIndex(7)
        
        
    def frameI(self):#文档界面<-pb_file
        
        voice_stop()
        voice_change(cnt,initialize=None)
        music_stop()
        music_change(cnt,initialize=None)

        self.sw_Main.setCurrentIndex(8)

###########################################function_card###########################################

class FileDate(object):#判断user选中了那个存档文件，将预选变量file_select的值设置
    
    
    def file_one(self):
        
        global file_select
        print("file_1")
        file_select = 1
        
        
    def file_two(self):
        
        global file_select
        print("file_2")
        file_select = 2
    
    
    def file_three(self):
        
        global file_select
        print("file_3")
        file_select = 3
        
        
    def file_four(self):
        
        global file_select
        print("file_4")
        file_select = 4
        
        
    def file_five(self):
        
        global file_select
        print("file_5")
        file_select = 5
        
        
    def file_six(self):
        
        global file_select
        print("file_6")
        file_select = 6
        
        
    def file_seven(self):
        
        global file_select
        print("file_7")
        file_select = 7
        
        
    def file_eight(self):
        
        global file_select
        print("file_8")
        file_select = 8
        
        
    def file_nine(self):
        
        global file_select
        print("file_9")
        file_select = 9

    def fileINT_toStr(self):  # 读取文件的时候，把file_select的值转为str来确认读写文件的文件名
        
        global file_select
        if file_select == 1:
            return "one"
        
        elif file_select == 2:
            return "two"
        
        elif file_select == 3:
            return "three"
        
        elif file_select == 4:
            return "four"
        
        elif file_select == 5:
            return "five"
        
        elif file_select == 6:
            return "six"
        
        elif file_select == 7:
            return "seven"
        elif file_select == 8:
            return "eight"
        
        elif file_select == 9:
            return "nine"
###########################################File_date##############################################


def file_save():#存档
    
    print("file_save")
    ans = FileDate.fileINT_toStr(file_select)
    file = open("saveFile/File_"+ans,"w",encoding = 'UTF-8')
    file.write(str(cnt))
    file.close()

def file_read():#读档

    print("file_read")
    ans = FileDate.fileINT_toStr(file_select)
    file = open("saveFile/File_" +ans, "r",encoding = 'UTF-8')
    cnt = int(file.read())
    file.close()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")  # 设置窗口风格
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_Form()  # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
