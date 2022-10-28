# 自动设置ppt背景
# 导入pyautogui
import pyautogui
# 导入time
import time

# 等待2秒
time.sleep(2)
# 无限循环
while True:
    # 鼠标去到屏幕中央
    pyautogui.moveTo(960, 540)
    # 点击鼠标右键
    pyautogui.click(button='right')
    # 等待0.1秒
    time.sleep(0.1)
    # 点击坐标(1040,250)
    pyautogui.click(1040, 250)
    # 等待0.1秒
    time.sleep(0.1)
    # 按下ctrl+a
    pyautogui.hotkey('ctrl', 'a')
    # 等待0.1秒
    time.sleep(0.1)
    # 按下删除键
    pyautogui.press('delete')
    # 按下下方向键
    pyautogui.press('down')
