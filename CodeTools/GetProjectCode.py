import os
import json

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
    "proto": "proto",
    "md": "markdown",
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
        show_progress_bar(f"读取json文件: {json_file_path}", 0)
        try:
            with open(json_file_path, "r", encoding="utf-8") as f:
                project_code_dic = json.load(f)
        except Exception as e:
            raise Exception(f"读取json文件出错: {e}") from e
        show_progress_bar(f"读取json文件完成: {json_file_path}", 1)

    # 定义txt文件路径
    txt_file_path = os.path.join(export_url, ".AllCode.txt")

    # 删除已有的txt文件（如果存在）
    if os.path.exists(txt_file_path):
        os.remove(txt_file_path)

    # 写入目录部分
    write_directory(txt_file_path, project_code_list)

    # 处理代码文件列表
    total_files = len(project_code_list)
    for i, code_file_name in enumerate(project_code_list):
        show_progress_bar(f"处理代码文件: {code_file_name}", i / total_files)

        # 检查代码文件是否已存在于字典中
        code_file_path = project_code_dic.get(code_file_name)

        if code_file_path and os.path.exists(code_file_path):
            # 如果字典中路径存在且有效
            pass
        else:
            # 尝试在项目代码文件夹中查找代码文件
            code_file_path = find_code_file(
                project_code_folder_list, code_file_name)
            if not code_file_path:
                raise FileNotFoundError(f"找不到代码文件: {code_file_name}")

            # 更新字典中的路径
            project_code_dic[code_file_name] = code_file_path

        # 读取代码文件内容
        try:
            with open(code_file_path, "r", encoding="utf-8") as f:
                code_content = f.read()
        except Exception as e:
            raise Exception(f"读取代码文件出错: {e}") from e

        # 将代码文件内容写入txt文件
        write_code_to_txt(txt_file_path, code_file_name,
                          code_content, i, total_files)

    # 将代码文件字典写入json文件
    show_progress_bar("写入json文件...", 0)
    try:
        with open(json_file_path, "w", encoding="utf-8") as f:
            json.dump(project_code_dic, f, indent=4, ensure_ascii=False)
    except Exception as e:
        raise Exception(f"写入json文件出错: {e}") from e
    show_progress_bar("写入json文件完成", 1)

    show_progress_bar("处理完成", 1)
    # 打开导出目录
    # os.startfile(export_url)


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


def write_directory(txt_file_path, project_code_list):
    """
    将代码文件名列表写入txt文件，作为目录部分。

    Args:
        txt_file_path (str): txt文件路径。
        project_code_list (list): 代码文件名列表。
    """
    with open(txt_file_path, "a", encoding="utf-8") as f:
        f.write("# 文件目录\n")
        for code_file_name in project_code_list:
            f.write(f"- {code_file_name}\n")
        f.write("\n")  # 添加一个空行以分隔目录和代码内容


def write_code_to_txt(txt_file_path, code_file_name, code_content, current_file, total_files):
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

# 对字符串list去重


def list_unique(lst):
    """
    对字符串列表进行去重。

    Args:
        list (list): 字符串列表。

    Returns:
        list: 去重后的字符串列表。
    """
    # 使用集合去重
    return list(set(lst))


# 运行主函数
if __name__ == "__main__":
    # 导出目录
    export_url = r"e:\UnityProject\XY\ProjectCode"
    # 项目代码文件夹
    project_code_folder_list = [
        r"e:\UnityProject\XY\Assets\Lua",
        r"e:\UnityProject\XY\Assets\Res\Plua",
        r"e:\UnityProject\XY\Assets\Script\ScriptHotfix",
        r"e:\UnityProject\XY\Assets\Script\ScriptAot",
        r"e:\UnityProject\XY\XYFramework\LuaDll",
        r"e:\UnityProject\XY\XYFramework\pure",
        r"e:\UnityProject\XY\XYFramework\game",
        r"E:\UnityProject\XY\XY\Assets\Res\Data\Proto",
        r"D:\Personal\Documents\Obsidian\NyxJaeCodeDoc\XY",
        r"E:\UnityProject\XY\Assets\Res\Data\Source\Lang",
    ]
    # 代码文件名列表
    project_code_list = [
        # region 文件命名规则
        "_004_文件命名规则.md",
        # endregion

        # region 界面Mediator 相关
        "LuaGrid.readme",
        "mediator.readme",
        "Mediator.lua",
        "MailMediator_Main.lua",
        "RankMediator_main.lua",
        "HomeMediator_Mid.lua",
        "HomeMediator_Top.lua",
        "FriendMediator_Main.lua",
        # endregion

        # region 用户和信息处理
        "user_info.lua",
        "share_info.lua",
        "info_base.lua",
        # endregion

        # region 数据相关
        "database.lua",
        "datasheet.lua",
        "typetable.lua",
        "TypeDB.lua",
        "Data.lua",
        # "TypeClasses.lua",
        # "DataClasses.lua"
        "Type_FieldRun.lua",
        "Data_Character.lua",
        "Data_FieldRunControl.lua",
        "tvo_wrapper_BodyPosition.lua",
        "Type_BodyPosition.lua",
        # endregion

        # region 逻辑管理
        "logic_manager.lua",
        "fashionhandler_slot.lua",
        "update_queue.lua",
        "fieldrunhandler_start.lua",
        # endregion

        # region 网络和通信
        # "SocketMethod.lua",
        "socket_form.lua",
        # endregion

        # region worker 后台任务
        "clientworker.lua",
        "clientworker_bd.lua",
        # endregion

        # region 工具
        # "CSNamespace.lua",
        "LogManager.lua",
        "Logger.lua",
        "xnumber.lua",
        "xlang.lua",
        "xstring.lua",
        "xtime.lua",
        "xcommon.lua",
        "hash_id.lua",
        "string_utils.lua",
        "thing_tools.lua",
        "thing_tools_cost.lua",
        "thing_tools_bag.lua",
        "thing_tools_userobject.lua",
        "tick_queue.lua",
        # endregion

        # region 背包
        "bag_container.lua",
        "bag_children.lua",
        "bag_datadriver.lua",
        "bag_manager.lua",
        "bag_view.lua",
        # endregion

        # region prompt提示系统
        "prompt_center.lua",
        "prompt_handler_fieldrun.lua",
        # endregion

        # region 红点系统
        "redpoint_fieldrun.lua",
        "redpoint_manager.lua",
        "manager_abstract.lua",
        # endregion

        # region 属性和对象管理
        "render_group.lua",
        "property_group.lua",
        "thing_group.lua",
        "property_tools.lua",
        # endregion
    ]

    # 对代码文件名列表去重后调用主函数
    process_files(export_url, project_code_folder_list,
                  list_unique(project_code_list))
