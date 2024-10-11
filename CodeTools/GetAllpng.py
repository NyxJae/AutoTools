# region 导入模块
import os
import shutil

# endregion

# region 定义函数

# 定义一个函数，用于将png文件名前加上其父文件夹的父文件夹名,以_分隔,避免重名
# 参数1: 此文件的完整路径
# 返回值: 新文件的文件名


def rename_file(file_path):
    # 获取文件名
    file_name = os.path.basename(file_path)
    if '切图' == os.path.basename(
            os.path.dirname(file_path)):
        # 获取文件所在文件夹的父文件夹名
        parent_folder_name = os.path.basename(
            os.path.dirname(os.path.dirname(os.path.dirname(file_path))))
    else:
        # 获取文件所在文件夹的父文件夹名
        parent_folder_name = os.path.basename(
            os.path.dirname(file_path))
    # 构建新文件名
    new_file_name = parent_folder_name + "_" + file_name
    return new_file_name

# 定义一个函数，用于获取指定目录下的所有png文件,改名后复制到指定目录


def get_all_png_files(src_folder, dest_folder):
    # 如果目标目录不存在，则创建目标目录
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    # 统计总文件数
    total_files = sum([len(files) for r, d, files in os.walk(
        src_folder) if any(f.lower().endswith(".png") for f in files)])
    processed_files = 0
    # 遍历指定文件夹
    for root, dirs, files in os.walk(src_folder):
        for filename in files:
            # 检查文件扩展名是否为.png
            if filename.lower().endswith(".png"):
                # 构建完整的文件路径
                file_path = os.path.join(root, filename)
                # 清空控制台
                os.system('cls')
                # 打印进度信息
                processed_files += 1
                progress = f"处理文件 {processed_files}/{total_files}: " + file_path
                print(progress, end="\r")
                # 改名后复制到指定目录
                try:
                    # 改名
                    new_file_name = rename_file(file_path)
                    new_file_path = os.path.join(dest_folder, new_file_name)
                    # 复制到指定目录
                    shutil.copy(file_path, new_file_path)
                except IOError as e:
                    # 打印错误信息
                    print(f"Error reading file {filename}: {e}")
                finally:
                    # 跳过当前循环，继续处理下一个文件
                    continue
    print("\n处理完成")

# endregion

# region 调用函数


# 指定源目录
src_folder = r"E:\UnityProject\Resource\XYArts\ui"
# 指定目标目录
dest_folder = r"E:\UnityProject\Resource\XYArts\texture"

# 清理目标目录内的所有文件与文件夹,目标目录不要删除
if os.path.exists(dest_folder):
    for item in os.listdir(dest_folder):
        item_path = os.path.join(dest_folder, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

# 调用函数
get_all_png_files(src_folder, dest_folder)

# endregion
