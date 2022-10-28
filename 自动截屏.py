import pyautogui
import time

# 等待1秒
time.sleep(3)
# 无限循环
while True:
    # 等待2秒
    time.sleep(2)
    # 截屏快捷键 command+shift+5
    pyautogui.hotkey('command', 'shift', '5')
    # 等待1秒
    time.sleep(0.5)
    # 回车
    pyautogui.press('enter')
    # 等待0.5秒
    time.sleep(0.5)
    # 鼠标去到(1887,1045)
    pyautogui.moveTo(1790, 1045)
    # 鼠标点击并滑动
    pyautogui.dragTo(1887, 1045, 0.5, button='left')
    # 等待1秒
    time.sleep(1)
    # 鼠标点击
    pyautogui.click(1887, 1045)
