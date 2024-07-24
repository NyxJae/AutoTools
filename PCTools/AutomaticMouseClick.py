# 按下f7鼠标开始自动点击,按下f8停止自动点击
import pyautogui
import keyboard
import time
from threading import Thread

clicking = False

print('按下F7开始自动点击，按下F8停止自动点击')


def auto_click():
    print('自动点击开始')
    global clicking
    while clicking:
        pyautogui.click()
        time.sleep(0.01)


def start_click():
    global clicking
    clicking = True
    t = Thread(target=auto_click)  # 创建一个线程去执行auto_click函数
    t.start()  # 启动线程


def stop_click():
    print('自动点击结束,程序退出')
    global clicking
    clicking = False
    # 停止监听
    keyboard.unhook_all()


keyboard.add_hotkey('F7', lambda: (start_click()))
keyboard.add_hotkey('F8', lambda: (stop_click()))
keyboard.wait()
