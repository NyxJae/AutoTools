import os

# 定义一个函数，用于读取并合并.cs文件内容

# 初始化合并后的内容字符串
combined_content = ""
print("开始")


# 定义一个函数，用于读取并合并.cs文件内容
def combine_cs_files(folder_path):
    # 声明全局的合并内容字符串
    global combined_content
    # 遍历指定文件夹
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            # 检查文件扩展名是否为.cs
            if filename.lower().endswith(".cs"):
                # 构建完整的文件路径
                file_path = os.path.join(root, filename)
                # 清空控制台
                os.system('cls')
                # 打印日志,并让日志在同一行显示
                print("正在处理文件: " + file_path, end="\r")
                # 读取文件内容
                try:
                    with open(file_path, 'r', encoding="utf-8") as file:
                        content = file.read()
                        combined_content += content + "\n\n"

                except IOError as e:
                    # 打印错误信息
                    print(f"Error reading file {filename}: {e}")
                finally:
                    # 跳过当前循环，继续处理下一个文件
                    continue


# 定义一个函数，用于读取并合并.lua文件内容
def combine_lua_files(folder_path):
    # 声明全局的合并内容字符串
    global combined_content
    # 遍历指定文件夹
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            # 检查文件扩展名是否为.lua
            if filename.lower().endswith(".lua"):
                # 构建完整的文件路径
                file_path = os.path.join(root, filename)
                # 清除一行日志
                print(" " * 150, end="\r")
                # 打印日志,并让日志在同一行显示
                print("正在处理文件: " + file_path, end="\r")
                # 读取文件内容
                try:
                    with open(file_path, 'r', encoding="utf-8") as file:
                        content = file.read()
                        # 先添加文件名到合并内容字符串中
                        combined_content += f"-- {filename}\n"
                        # 如果第一行是注释，则去掉第一行
                        if content.startswith("--"):
                            content = content[content.find("\n") + 1:]
                        combined_content += content + "\n\n"
                except IOError as e:
                    # 打印错误信息
                    print(f"Error reading file {filename}: {e}")


# 定义一个函数，用于将合并后的内容写入指定的Markdown文件
def write_to_md_file(output_dir, output_file_name):
    # 声明全局的合并内容字符串
    global combined_content
    # 构建输出Markdown文件的完整路径
    output_file_path = os.path.join(output_dir, output_file_name)
    # 将合并后的内容写入指定的Markdown文件
    try:
        with open(output_file_path, 'w', encoding="utf-8") as md_file:
            md_file.write(combined_content)
        print(f"All files have been combined into {output_file_path}")
    except IOError as e:
        # 打印错误信息
        print(f"Error writing to file {output_file_path}: {e}")

    # 使用资源管理器打开输出文件夹
    os.startfile(output_dir)


# # 指定需要读取的文件夹路径
# folder_path = r"e:\UnityProject\XYFramework\pure"
# # 调用函数，读取并合并文件内容
# combine_cs_files(folder_path)

# # 指定需要读取的文件夹路径
# folder_path = r"e:\UnityProject\XYFramework\game"
# # 调用函数，读取并合并文件内容
# combine_cs_files(folder_path)

# # 指定需要读取的文件夹路径
# folder_path = r"e:\UnityProject\XYFramework\game.editor"
# # 调用函数，读取并合并文件内容
# combine_cs_files(folder_path)

# # 指定需要读取的文件夹路径
# folder_path = r"e:\UnityProject\XYFramework\LuaDll"
# # 调用函数，读取并合并文件内容
# combine_lua_files(folder_path)

# # 指定需要读取的文件夹路径
# folder_path = r"E:\UnityProject\Project_tcxy\Assets\ScriptAot"
# # 调用函数，读取并合并文件内容
# combine_cs_files(folder_path)
# # 指定需要读取的文件夹路径
# folder_path = r"E:\UnityProject\Project_tcxy\Assets\ScriptHotfix"
# # 调用函数，读取并合并文件内容
# combine_cs_files(folder_path)

# # 指定需要读取的文件夹路径
# folder_path = r"E:\UnityProject\Project_tcxy\Assets\Script\DLCsharp"
# # 调用函数，读取并合并文件内容
# combine_cs_files(folder_path)

# # 指定需要读取的文件夹路径
# folder_path = r"E:\UnityProject\Project_tcxy\Assets\Script\Lua"
# # 调用函数，读取并合并文件内容
# combine_lua_files(folder_path)
# # 指定需要读取的文件夹路径
# folder_path = r"E:\UnityProject\Project_tcxy\Assets\Res\Plua\view"
# # 调用函数，读取并合并文件内容
# combine_lua_files(folder_path)
# # 指定需要读取的文件夹路径
# folder_path = r"E:\UnityProject\Project_tcxy\Assets\Res\Plua\label"
# # 调用函数，读取并合并文件内容
# combine_lua_files(folder_path)#
# # 指定需要读取的文件夹路径
# folder_path = r"E:\UnityProject\TEngine-TEngine4.0.12\UnityProject\Assets\TEngine"
# # 调用函数，读取并合并文件内容
# combine_cs_files(folder_path)


# # 指定输出文件夹路径
# output_directory = r"D:\Personal\Documents\GetAllText"
# # 指定输出文件名
# output_file_name = "TEngine.md"

# # 指定需要读取的文件夹路径
folder_path = r"E:\UnityProject\XY\Assets\test\Editor\LinkerGenerator"
# 调用函数，读取并合并文件内容
combine_cs_files(folder_path)
# 指定输出文件夹路径
output_directory = r"D:\Personal\Documents\GetAllText"
# 指定输出文件名
output_file_name = "LinkerGenerator.md"

# 调用函数，将合并后的内容写入指定的Markdown文件
write_to_md_file(output_directory, output_file_name)
