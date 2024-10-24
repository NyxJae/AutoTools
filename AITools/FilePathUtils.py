import os

class FilePathUtils:
    def __init__(self, project_root, exclude_dirs=None, exclude_extensions=None):
        """
        初始化项目根目录和文件过滤配置
        :param project_root: 项目根目录
        :param exclude_dirs: 要排除的目录列表，默认排除常见的系统和缓存目录
        :param exclude_extensions: 要排除的文件扩展名列表，如['.pyc', '.pyo']
        """
        self.project_root = os.path.normpath(project_root)
        
        # 合并默认排除目录和用户自定义排除目录
        default_exclude_dirs = {'__pycache__', 'node_modules', '.git', '.idea', 'venv'}
        self.exclude_dirs = default_exclude_dirs.union(set(exclude_dirs or []))
        
        # 合并默认排除扩展名和用户自定义排除扩展名
        default_exclude_extensions = {'.pyc', '.pyo', '.pyd', '.so', '.dll', '.class'}
        self.exclude_extensions = default_exclude_extensions.union(
            {ext.lower() for ext in (exclude_extensions or [])}
        )

    def get_all_file_paths(self, paths):
        """
        获取所有符合条件的文件路径
        :param paths: 路径列表
        :return: 符合条件的文件路径列表
        """
        all_files = []
        for path in paths:
            full_path = os.path.join(self.project_root, os.path.normpath(path))
            if os.path.isfile(full_path) and not self._should_exclude_file(full_path):
                all_files.append(os.path.abspath(full_path))
            else:
                for root, dirs, files in os.walk(full_path):
                    # 过滤掉不需要处理的目录
                    dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
                    
                    for file in files:
                        file_path = os.path.join(root, file)
                        if not self._should_exclude_file(file_path):
                            all_files.append(os.path.normpath(file_path))
        return all_files

    def get_all_folder_paths(self, paths):
        """
        获取所有需要处理的文件夹路径
        :param paths: 路径列表
        :return: 文件夹路径列表
        """
        all_folders = []
        for path in paths:
            full_path = os.path.join(self.project_root, os.path.normpath(path))
            if os.path.isdir(full_path) and os.path.basename(full_path) not in self.exclude_dirs:
                all_folders.append(full_path)  # 包含传入的文件夹
                for root, dirs, _ in os.walk(full_path):
                    # 过滤掉不需要处理的目录
                    dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
                    
                    for directory in dirs:
                        dir_path = os.path.normpath(os.path.join(root, directory))
                        if os.path.basename(dir_path) not in self.exclude_dirs:
                            all_folders.append(dir_path)
        return all_folders

    def _should_exclude_file(self, file_path):
        """
        检查文件是否应该被排除
        :param file_path: 文件路径
        :return: 布尔值，是否应该排除
        """
        _, ext = os.path.splitext(file_path)
        return ext.lower() in self.exclude_extensions

if __name__ == "__main__":
    # 测试代码
    project_root = "d:/Personal/Documents/AutoTools"
    paths = ["AITools"]
    exclude_dirs = ["test", "backup"]  # 额外排除的目录
    exclude_extensions = [".log", ".tmp"]  # 额外排除的文件类型
    
    print("\n=== 文件路径工具测试 ===")
    print(f"项目根目录: {project_root}")
    print(f"待处理路径: {paths}")
    print(f"排除目录: {exclude_dirs}")
    print(f"排除文件类型: {exclude_extensions}")
    
    # 实例化工具类并获取文件和文件夹路径
    utils = FilePathUtils(project_root, exclude_dirs, exclude_extensions)
    file_paths = utils.get_all_file_paths(paths)
    folder_paths = utils.get_all_folder_paths(paths)
    
    print("\n发现的文件:")
    for p in file_paths:
        print(f"- {p}")
        
    print("\n发现的文件夹:")
    for p in folder_paths:
        print(f"- {p}")
    
    print("\n=== 测试完成 ===")
