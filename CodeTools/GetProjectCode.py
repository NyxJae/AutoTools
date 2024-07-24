"""
指定一个文件夹url,为导出目录,用以存放一个json文件和最后生成的txt文件
如果导出目录不存在,则创建一个
json文件 名字为 ProjectCodeDic.json,存放的是代码文件名和代码文件的路径,如果已经存在则直接读取,不存在则创建,为了节约时间.
txt文件 名字为 ProjectCode.txt,存放的是所有代码文件的内容,每次重新生成,如果已经存在则覆盖
指定一个列表 名字为 ProjectCodeFolderList,内指定多个文件夹,为项目代码文件夹,用以从其中以及递归其子文件夹获取代码文件
指定一个列表 名字为 ProjectCodeList,内指定多个代码文件名,格式为 xxx.xx ,用以从项目代码文件夹中获取代码文件

每次运行时,会将中的代码文件的内容写入txt文件中,并将代码文件名和代码文件的路径写入json文件中
每次运行时,会先检查json文件中是否已经存在代码文件名和对应的代码文件的路径,如果存在则直接去指定路径获取代码文件内容
如果json中保存的路径名有问题,则会在所有项目代码文件夹中递归遍历,找到对应的代码文件,并将代码文件内容写入txt文件中,并将代码文件名和代码文件的路径写入json文件中
如果代码文件名不在json文件中,则会在所有项目代码文件夹中递归遍历,找到对应的代码文件,并将代码文件内容写入txt文件中,并将代码文件名和代码文件的路径写入json文件中
每次运行时,会先检查txt文件是否存在,若存在则删除,重新生成
txt中 用md格式组织内容,先写入代码文件名,再写入代码文件内容,格式是:
# 代码文件名
代码文件内容 用代码块包裹(三个反引号)并指定代码语言(创建一个字典,用以指定代码语言,包括CSharp,Java,Python,JavaScript,TypeScript,Html,Xml,Json,lua,proto)

在控制台显示个进度条,能直观看到进度,进度条只在一行上更新显示,不换行,显示的内容包括进度条(#-),当前处理的任务
若是在遍历文件夹时,显示的内容包括当前遍历的文件夹路径
若是在处理代码文件时,显示的内容包括当前处理的代码文件名
若是在读取json文件时,显示的内容包括当前读取的进度
若是在写入json文件时,显示的内容包括当前写入的进度
若是在写入txt文件时,显示的内容包括当前写入的进度

如果有报错,特别是代码文件没找到,只要出现任何错误都停止程序,并给出错误信息和建议修改方案

完成后打开导出目录

函数调用形如:process_files(export_url, project_code_folder_list, project_code_list)

在处理文件内容时，确保使用正确的编码格式（如UTF-8）。
"""

import os
import json
import time

# 定义代码语言字典
code_language_dict = {
    "cs": "csharp",
    "java": "java",
    "py": "python",
    "js": "javascript",
    "ts": "typescript",
    "html": "html",
    "xml": "xml",
    "json": "json",
    "lua": "lua",
    "proto": "proto"
}


def process_files(export_url, project_code_folder_list, project_code_list):
    """
    处理代码文件并将结果写入到json和txt文件中。

    此函数将遍历指定的代码文件列表，读取每个文件的内容，并将其写入到一个txt文件中。
    同时，函数还会将代码文件名和路径存储在一个json文件中，方便后续查找。

    Args:
        export_url (str): 导出目录路径。
        project_code_folder_list (list): 项目代码文件夹路径列表。
        project_code_list (list): 代码文件名列表。

    Raises:
        FileNotFoundError: 如果找不到指定的代码文件，则会引发此异常。
        Exception: 处理过程中出现任何其他错误，将引发此异常。
    """
    # 创建导出目录（如果不存在）
    os.makedirs(export_url, exist_ok=True)

    # 定义json文件路径
    json_file_path = os.path.join(export_url, "ProjectCodeDic.json")

    # 初始化代码文件字典
    project_code_dic = {}

    # 读取已有的代码文件字典（如果存在）
    if os.path.exists(json_file_path):
        show_progress_bar(f"正在读取json文件: {json_file_path}", 0)
        try:
            with open(json_file_path, "r", encoding="utf-8") as f:
                project_code_dic = json.load(f)
        except Exception as e:
            raise Exception(f"读取json文件出错: {e}") from e
        show_progress_bar(f"读取json文件完成: {json_file_path}", 1)

    # 定义txt文件路径
    txt_file_path = os.path.join(export_url, "ProjectCode.txt")

    # 删除已有的txt文件（如果存在）
    if os.path.exists(txt_file_path):
        os.remove(txt_file_path)

    # 处理代码文件列表
    total_files = len(project_code_list)
    for i, code_file_name in enumerate(project_code_list):
        show_progress_bar(f"正在处理代码文件: {code_file_name}", i / total_files)

        # 检查代码文件是否已存在于字典中
        if code_file_name in project_code_dic:
            # 从字典中获取代码文件路径
            code_file_path = project_code_dic[code_file_name]
        else:
            # 遍历项目代码文件夹，查找代码文件
            code_file_path = find_code_file(
                project_code_folder_list, code_file_name)
            if not code_file_path:
                raise FileNotFoundError(f"找不到代码文件: {code_file_name}")

        # 读取代码文件内容
        try:
            with open(code_file_path, "r", encoding="utf-8") as f:
                code_content = f.read()
        except Exception as e:
            raise Exception(f"读取代码文件出错: {e}") from e

        # 将代码文件名和路径写入字典
        project_code_dic[code_file_name] = code_file_path

        # 将代码文件内容写入txt文件
        write_to_txt(txt_file_path, code_file_name,
                     code_content, i, total_files)

    # 将代码文件字典写入json文件
    show_progress_bar("正在写入json文件...", 0)
    try:
        with open(json_file_path, "w", encoding="utf-8") as f:
            json.dump(project_code_dic, f, indent=4, ensure_ascii=False)
    except Exception as e:
        raise Exception(f"写入json文件出错: {e}") from e
    show_progress_bar("写入json文件完成", 1)

    show_progress_bar("处理完成", 1)
    # 打开导出目录
    os.startfile(export_url)


def find_code_file(folder_list, code_file_name):
    """
    递归遍历文件夹列表，查找指定的代码文件。

    Args:
        folder_list (list): 文件夹路径列表。
        code_file_name (str): 代码文件名。

    Returns:
        str: 代码文件路径，如果找到则返回路径，否则返回None。
    """
    for folder_path in folder_list:
        show_progress_bar(f"正在遍历文件夹: {folder_path}")
        for root, _, files in os.walk(folder_path):
            if code_file_name in files:
                return os.path.join(root, code_file_name)
    return None


def write_to_txt(txt_file_path, code_file_name, code_content, current_file, total_files):
    """
    将代码文件内容写入txt文件。

    Args:
        txt_file_path (str): txt文件路径。
        code_file_name (str): 代码文件名。
        code_content (str): 代码文件内容。
        current_file (int): 当前正在处理的文件索引。
        total_files (int): 总文件数量。
    """
    file_extension = code_file_name.split(".")[-1].lower()
    code_language = code_language_dict.get(file_extension, "")
    with open(txt_file_path, "a", encoding="utf-8") as f:
        f.write(f"# {code_file_name}\n")
        f.write(f"```{code_language}\n")
        f.write(code_content)
        f.write("\n```\n\n")
    show_progress_bar(f"正在写入txt文件: {code_file_name}",
                      (current_file + 1) / total_files)


def show_progress_bar(task_name, progress=0):
    """
    在控制台显示进度条。

    Args:
        task_name (str): 当前任务名称。
        progress (float, optional): 进度值 (0.0 - 1.0)。默认为 0。
    """
    bar_length = 20
    filled_length = int(bar_length * progress)
    bar = f"[{'#' * filled_length}{'-' * (bar_length - filled_length)}]"
    print(f"\r{bar} {task_name} {progress:.1%}", end=" "*50)
    if progress >= 1:
        print()


# 运行主函数
if __name__ == "__main__":
    # 导出目录
    export_url = r"d:\Personal\Documents\ProjectCode"
    # 项目代码文件夹
    project_code_folder_list = [
        r"e:\UnityProject\XY\Assets\Lua",
        r"e:\UnityProject\XY\Assets\Res\Plua",
        r"e:\UnityProject\XY\Assets\Script\ScriptHotfix",
        r"e:\UnityProject\XY\Assets\Script\ScriptAot",
        r"e:\UnityProject\XYFramework\LuaDll",
        r"e:\UnityProject\XYFramework\pure",
        r"e:\UnityProject\XYFramework\game",
        r"E:\UnityProject\XY\Assets\Res\Data\Proto"
    ]
    # 代码文件名列表
    project_code_list = [
        "GameStarter.cs",
        "GameActivity.cs",
        "UIRendererBase.cs",
        "MediatorCore.cs",
        "GameMediator.cs",
        "ChildControl.cs",
        "ChildSelector.cs",
        "UIItemPane.cs",
        "NativeManager.cs",
        "NativeMethod.cs",
        "NativeImpl_Android.cs",
        "NativeImpl_WebGL.cs",
        "PanelManager.cs",
        "GameManager.cs",
        "AppCenter.lua",
        "SceneData.lua",
        "Data.lua",
        "SceneManager.lua",
        "proxy_center.lua",
        "TypeDB.lua",
        "TypeClasses.lua",
        "database.lua",
        "user_info.lua",
        "info_base.lua",
        "util.lua",
        "vector.lua",
        "pipe_line.lua",
        "GameTicker.lua",
        "update_queue.lua",
        "tick_queue.lua",
        "await_delay.lua",
        "co_delay.lua",
        "socket_form.lua",
        "memory_gc.lua",
        "prompt_center.lua",
        "GameManager.lua",
        "TableProxy.lua",
        "Main.lua",
        "platform_initor.lua",
        "platform_manager.lua",
        "platform_type.lua",
        "login_proccess.lua",
        "platform_abstract.lua",
        "platform_localtest.lua",
        "ptask_login_info_test.lua",
        "native_form.lua",
        "ptask_login_info_ios.lua",
        "LoginServerMediator_Login.lua",
        "ptask_visit_http.lua",
        "ptask_login_info_test.lua",
        "ptask_select_server.lua",
        "server_status.lua",
        "enterphase_type.lua",
        "LoginServerMediator_SelectServer.lua",
        "LoginServerMediator_ServerList.lua",
        "ptask_start_tcp.lua",
        "global_prompt_tcpconnect.lua",
        "tcp_connect.lua",
        "ptask_start_game_single_hero.lua",
        "Proxy_GateResponse.lua",
        "main_panel_type.lua",
        "HomeMediator_Right.lua",
        "SubView_Home_Right_Open.lua",
        "HomeMediator_Top.lua",
        "GameToClientProto.proto",
        "Type_ChatChannel.lua",
        "Data_Chat.lua",
        "chat_enum.lua",
        "chat_channel_map.lua",
        "chat_channel_common.lua",
        "chat_channel_player.lua",
        "chat_player_view.lua",
        "Data_Friend.lua",
        "ChatMediator_Main.lua",
        "chathandler_request.lua",
        "GameToClientField.proto",
        "ClientToGameLevel.proto",
        "HomeMediator_Scene.lua",
        "fieldrunhandler_start.lua",
        "prompt_handler_fieldrun.lua",
        "FieldRunMediator_Prepare.lua",
        "fieldrunhandler_pause.lua",
        "fieldrunhandler_resume.lua",
        "FieldRunMediator_Main.lua",
        "native_form.lua",
        "native_method.lua",
    ]
    process_files(export_url, project_code_folder_list, project_code_list)
