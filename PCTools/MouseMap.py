import time
import threading
import keyboard  # 需要安装 keyboard 库
from pynput import mouse
import sys  # 导入 sys 模块以便退出程序

# 可调的长按阈值（秒）
LONG_PRESS_THRESHOLD = 0.15

# 全局变量
space_pressed_time = None  # 记录按下空格键的时间
space_long_press = False   # 标记是否为长按
long_press_timer = None    # 长按定时器
mouse_controller = mouse.Controller()  # 鼠标控制器实例

# 锁以同步访问全局变量
lock = threading.Lock()

def handle_long_press():
    """
    定时器回调函数，用于处理长按事件
    """
    global space_long_press
    with lock:
        space_long_press = True
        # 按下鼠标左键
        mouse_controller.press(mouse.Button.left)

def on_space_down(event):
    """
    空格键按下事件处理函数
    """
    global space_pressed_time, space_long_press, long_press_timer
    with lock:
        if space_pressed_time is None:
            space_pressed_time = time.time()
            space_long_press = False
            # 启动长按定时器
            long_press_timer = threading.Timer(LONG_PRESS_THRESHOLD, handle_long_press)
            long_press_timer.start()

def on_space_up(event):
    """
    空格键释放事件处理函数
    """
    global space_pressed_time, space_long_press, long_press_timer
    with lock:
        if space_pressed_time is not None:
            if not space_long_press:
                # 短按，发送一个空格
                keyboard.press_and_release('space')
                # 取消长按定时器
                if long_press_timer is not None:
                    long_press_timer.cancel()
                    long_press_timer = None
            else:
                # 长按，释放鼠标左键
                mouse_controller.release(mouse.Button.left)
        
            # 重置状态
            space_pressed_time = None
            space_long_press = False

def exit_script():
    """
    退出脚本的处理函数
    """
    # 取消所有键盘钩子
    keyboard.unhook_all()
    # 释放鼠标左键（如果正在长按）
    with lock:
        if space_long_press:
            mouse_controller.release(mouse.Button.left)
    sys.exit()

def main():
    """
    主函数，注册事件并保持运行
    """
    # 注册空格键按下和释放事件，设置 suppress=True 仅抑制空格键事件
    keyboard.on_press_key('space', on_space_down, suppress=True)
    keyboard.on_release_key('space', on_space_up, suppress=True)

    # 注册 Ctrl+Esc 快捷键以退出脚本
    keyboard.add_hotkey('ctrl+esc', exit_script)

    # 让主线程保持运行
    keyboard.wait()

if __name__ == "__main__":
    main()
