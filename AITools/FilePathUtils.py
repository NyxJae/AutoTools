import os

class FilePathUtils:
    def __init__(self, project_root, file_extensions=None):
        self.project_root = os.path.normpath(project_root)
        self.file_extensions = file_extensions if file_extensions is not None else []

    def get_all_file_paths(self, paths):
        all_files = []
        for path in paths:
            full_path = os.path.join(self.project_root, os.path.normpath(path))
            if os.path.isfile(full_path) and self._has_valid_extension(full_path):
                all_files.append(os.path.abspath(full_path))
            else:
                for root, _, files in os.walk(full_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        if self._has_valid_extension(file_path):
                            all_files.append(os.path.normpath(file_path))
        return all_files

    def get_all_folder_paths(self, paths):
        all_folders = []
        for path in paths:
            full_path = os.path.join(self.project_root, os.path.normpath(path))
            if os.path.isdir(full_path):
                all_folders.append(full_path)  # 包含传入的文件夹
                for root, dirs, _ in os.walk(full_path):
                    for directory in dirs:
                        all_folders.append(os.path.normpath(os.path.join(root, directory)))
        return all_folders

    def _has_valid_extension(self, file_path):
        if not self.file_extensions:
            return True
        _, ext = os.path.splitext(file_path)
        return ext.lower() in self.file_extensions

if __name__ == "__main__":
    project_root = "d:/Personal/Documents/AutoTools"
    paths = ["AITools"]
    extensions = ['.py']
    # Example usage
    utils = FilePathUtils(project_root, extensions)
    file_paths = utils.get_all_file_paths(paths)
    folder_paths = utils.get_all_folder_paths(paths)
    print("文件路径:")
    for p in file_paths:
        print(p)
    print("文件夹路径:")
    for p in folder_paths:
        print(p)
