# 导入pynput
from pynput import mouse


'''获取坐标，运行后
1.点击任务栏WPS图标
2.点击任务栏微信图标
3.点击搜索框输入“文件助手”后 回车,
4.点击发送文件图标后会自动结束脚本并保存坐标'''

# 定义一个前缀列表
prefix = ['发送文件坐标', '搜索框坐标', '微信图标坐标', 'WPS图标坐标']
# 定义一个坐标字典
xy = {}
# 打开鼠标事件监听
with mouse.Events() as events:
    # 读取鼠标事件
    for event in events:
        # 如果是鼠标按下事件
        if isinstance(event, mouse.Events.Click):
            # 如果是按下左键事件
            if event.button == mouse.Button.left and event.pressed:
                # 字典添加键值对
                xy[prefix.pop()] = (int(event.x), int(event.y))
                # 如果提示前缀列表为空
                if not prefix:
                    # 将坐标字典保存在UTF-8的txt文件中
                    with open('xy.txt', 'w', encoding='utf-8') as f:
                        f.write(str(xy))
                    # 退出循环
                    break
            # 如果是按下右键
            elif event.button == mouse.Button.right:
                # 退出循环
                break
