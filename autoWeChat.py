from tkinter import N
import pyautogui
import time
import random
import xlrd  # xlrd==1.2.0
import pyperclip

# pip 安装 requirements.txt
# pip install -r requirements.txt


# 第一次使用使用get_xy.py获取坐标！！！！

# 读取utf-8编码的xy.txt文件
with open('xy.txt', 'r', encoding='utf-8') as f:
    # 读取文件内容
    xy = f.read()
    # 将字符串转成字典
    xy = eval(xy)
    # 获取wps图标坐标
    WPS_XY = xy['WPS图标坐标']
    # 获取微信图标坐标
    WECHAT_XY = xy['微信图标坐标']
    # 获取搜索框坐标
    SEARCH_XY = xy['搜索框坐标']
    # 获取发送文件坐标
    SEND_FILE_XY = xy['发送文件坐标']


# 鼠标点击excel图标，防止忘记保存
pyautogui.click(WPS_XY)
# 保存快捷键
pyautogui.hotkey('ctrl', 's')
# 等待1秒
time.sleep(1)
# 读取 excel 文件
workbook = xlrd.open_workbook('群发改名字.xls')
# 点击微信坐标
pyautogui.click(WECHAT_XY)


def auto_wechat(page, begin, end, img=None, send=0):
    '''
    微信群发改名字
    :param page: 页数
    param begin: 开始行
    param end: 结束行
    param img: 文件列表，绝对路径字符串,前添加r,防止转义
    param send: 是否发送,0是打草稿,1是发送
    '''
    # 获取指定工作表
    sheet = workbook.sheet_by_index(page-1)

    # 从表格的第三行开始循环
    for i in range(begin-1, end):

        # 读取工作表中的第i行第一列的数据k
        name = sheet.cell(i, 2).value
        print(name)
        # 复制 name 的内容
        pyperclip.copy(name)
        time.sleep(1)
        # 定位到搜索框
        pyautogui.click(SEARCH_XY)
        # 粘贴 name 到搜索框
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        # 点击回车
        pyautogui.press('enter')
        # 提前发送
        if send == 1:
            # 随机等待1.0-5.0秒
            time.sleep(random.uniform(1.0, 5.0))
            # 点击回车
            pyautogui.press('enter')
            # 跳到下次循环
            continue
        # 读取工作表中的第i行第三列的数据
        content = sheet.cell(i, 4).value
        # 复制 content 的内容
        pyperclip.copy(content)
        time.sleep(1)
        # 粘贴 content 到发送框
        pyautogui.hotkey('ctrl', 'v')
        # 如果有图片，且类型是列表
        if isinstance(img, list):
            # 遍历图片列表
            for j in img:
                # 点击发送文件
                pyautogui.click(SEND_FILE_XY)
                # 等待1秒
                time.sleep(1)
                # 粘贴图片路径
                pyperclip.copy(j)
                # 等待1秒
                time.sleep(1)
                # 粘贴图片路径
                pyautogui.hotkey('ctrl', 'v')
                # 等待1秒
                time.sleep(1)
                # 回车
                pyautogui.press('enter')


auto_wechat(5, 3, 26, img=[r'C:\Users\admin\Desktop\AutoTools\教程视频.mp4',
            r'C:\Users\admin\Desktop\AutoTools\教程图片.jpg', r'C:\Users\admin\Desktop\AutoTools\二维码.jpg'], send=0)
