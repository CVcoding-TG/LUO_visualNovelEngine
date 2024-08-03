schedule_date = {
        "img_character":0,
        "img_background":0,
        "img_name":0,
        "txt_dialogue":0,
        "txt_pbI":0,
        "txt_pbII":0,
        "txt_pbIII":0,
        }
from game_CORE import nextSignal,pause#为了防止循环导入，放在数据后进行延迟导入
from game_CORE import Ui_Form
import time
while nextSignal==0:
    pause = 0#重置pause
    print('h')
    Ui_Form.frameA()
    try:
        schedule_date["img_character"] = 0
        schedule_date["img_background"] = 0
        schedule_date["img_name"] = 0
        schedule_date["txt_dialogue"] = 0
        schedule_date["txt_pbI"] = 0
        schedule_date["txt_pbII"] = 0
        schedule_date["txt_pbIII"] = 0
    except:
        print("bug")
    while pause != 0:
        print("鸭蛋")
        if pause == 2:
            break#当从setFFrame返回next依旧为0，就会跳出二层循环重新开始一层循环，还原原先的布局
        elif pause == 1:
            nextSignal = 1#当next=1时，就会跳出二层循环后到下一级循环
            break
while nextSignal==0:
    pause = 0#重置pause
    print('c')
    Ui_Form.frameA()
    schedule_date["img_character"] = 0
    schedule_date["img_background"] = 0
    schedule_date["img_name"] = 0
    schedule_date["txt_dialogue"] = 0
    schedule_date["txt_pbI"] = 0
    schedule_date["txt_pbII"] = 0
    schedule_date["txt_pbIII"] = 0
    while pause != 0:
        if pause == 2:
            break#当从setFFrame返回next依旧为0，就会跳出二层循环重新开始一层循环，还原原先的布局
        elif pause == 1:
            nextSignal = 1#当next=1时，就会跳出二层循环后到下一级循环
            break