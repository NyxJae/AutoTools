'''
自动添加Logo和二维码
'''
# 导入GUI库
import tkinter as tk
# 导入filedialog库
from tkinter import filedialog
# 导入图片处理库
import cv2
# 导入numpy库
import numpy as np
# 导入shutil库
import shutil
# 导入os库
import os


# 创建窗口
window = tk.Tk()
# 设置窗口标题
window.title('自动添加Logo和二维码')
# 设置窗口大小
window.geometry('500x300')
# 设置窗口不可变
window.resizable(False, False)

# 创建一个"选择图片"按钮的函数


def select_image():
    # 选择图片
    global img_path
    img_path = filedialog.askopenfilenames(title='选择图片')


# 创建一个"选择Logo"按钮的函数
def select_logo():
    # 选择Logo
    global logo_path
    logo_path = filedialog.askopenfilename(title='选择Logo')
    # 复制Logo到此目录,文件名不变
    shutil.copy(logo_path, 'logo.png')

# 创建一个"选择二维码"按钮的函数


def select_qrcode():
    # 选择二维码
    global qrcode_path
    qrcode_path = filedialog.askopenfilename(title='选择二维码')
    # 复制二维码到此目录
    shutil.copy(qrcode_path, 'qrcode.png')

# 创建一个"添加Logo和二维码"按钮的函数


def add_logo_qrcode():
    # 添加Logo和二维码,将logo添加在右上角,二维码添加在左下角
    # 读取Logo,解决中文路径问题
    logo = cv2.imdecode(np.fromfile('logo.png', dtype=np.uint8), -1)
    # 读取二维码,解决中文路径问题
    qrcode = cv2.imdecode(np.fromfile('qrcode.png', dtype=np.uint8), -1)
    # 遍历图片
    for path in img_path:
        # 读取图片,解决中文路径问题
        img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)
        # 获取图片的高和宽
        h, w = img.shape[:2]
        # 获取Logo的高和宽
        h_logo, w_logo = logo.shape[:2]
        # 获取二维码的高和宽
        h_qrcode, w_qrcode = qrcode.shape[:2]
        # 将Logo等比例缩放到图片的1/5
        logo = cv2.resize(logo, (int(w / 5), int(h_logo * w / 5 / w_logo)))
        # 将二维码等比例缩放到图片的1/5
        qrcode = cv2.resize(
            qrcode, (int(w / 5), int(h_qrcode * w / 5 / w_qrcode)))
        # 获取Logo的高和宽
        h_logo, w_logo = logo.shape[:2]
        # 获取二维码的高和宽
        h_qrcode, w_qrcode = qrcode.shape[:2]
        # 将Logo添加到图片的左上角
        img[0:h_logo, 0:w_logo] = logo
        # 将二维码添加到图片的右下角
        img[h - h_qrcode:h, w - w_qrcode:w] = qrcode
        # 保存图片.解决中文路径问题
        cv2.imencode('.jpg', img)[1].tofile(path)


# 如果不存在logo.png文件
if os.path.exists('logo.png'):
    # 在第一行第一列创建"已有Logo,可不用添加"的标签
    tk.Label(window, text='已有Logo,可不用添加').grid(row=0, column=1)
# 如果不存在qrcode.png文件
if os.path.exists('qrcode.png'):
    # 在第一行第二列创建"已有二维码,可不用添加"的标签
    tk.Label(window, text='已有二维码,可不用添加').grid(row=0, column=2)

# 创建一个"选择图片们"的按钮
select_image_button = tk.Button(window, text='选择图片们', command=select_image)
# 放置按钮
select_image_button.place(x=50, y=50, width=100, height=50)
# 创建一个"选择Logo"的按钮
select_logo_button = tk.Button(window, text='选择Logo', command=select_logo)
# 放置按钮
select_logo_button.place(x=200, y=50, width=100, height=50)
# 创建一个"选择二维码"的按钮
select_qrcode_button = tk.Button(window, text='选择二维码', command=select_qrcode)
# 放置按钮
select_qrcode_button.place(x=350, y=50, width=100, height=50)
# 创建一个"添加Logo和二维码"的按钮
add_logo_qrcode_button = tk.Button(
    window, text='添加Logo和二维码', command=add_logo_qrcode)
# 放置按钮
add_logo_qrcode_button.place(x=50, y=150, width=400, height=50)


# 主循环
window.mainloop()


# 打包成exe
# pyinstaller -F add_logo_qrcode.py
