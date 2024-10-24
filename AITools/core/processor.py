"""
文档处理核心逻辑
包含文件和文件夹的文档生成处理
"""
import os
from ..OpenAIConnector import OpenAIConnection
from .logger import Logger, Timer
from ..FilePathUtils import FilePathUtils
from ..config.filters import EXCLUDE_DIRS, EXCLUDE_EXTENSIONS

class DocProcessor:
    def __init__(self, openai_conn: OpenAIConnection, doc_root: str, project_root: str, 
                 code_prompt: str, module_prompt: str):
        """
        初始化文档处理器
        :param openai_conn: OpenAI连接实例
        :param doc_root: 文档根目录
        :param project_root: 项目根目录
        :param code_prompt: 代码文件文档提示词
        :param module_prompt: 模块文档提示词
        """
        self.openai = openai_conn
        self.doc_root = doc_root
        self.project_root = project_root
        self.code_prompt = code_prompt
        self.module_prompt = module_prompt
        self.logger = Logger()
        
        # 使用filters.py中的配置初始化文件路径工具
        self.file_utils = FilePathUtils(
            project_root=project_root,
            exclude_dirs=EXCLUDE_DIRS,
            exclude_extensions=EXCLUDE_EXTENSIONS
        )

    def generate_docs(self, paths):
        """
        生成文档
        :param paths: 需要生成文档的路径列表
        """
        with Timer("文档生成"):
            self.logger.section("开始生成文档")
            self.logger.info(f"待处理路径: {paths}")

            # 使用FilePathUtils获取所有文件和文件夹路径
            self.logger.step(1, 3, "扫描文件和文件夹...")
            file_paths = self.file_utils.get_all_file_paths(paths)
            folder_paths = self.file_utils.get_all_folder_paths(paths)
            self.logger.info(f"找到 {len(file_paths)} 个文件, {len(folder_paths)} 个文件夹")

            # 处理所有代码文件
            self.logger.step(2, 3, "处理代码文件...")
            for i, file_path in enumerate(file_paths, 1):
                try:
                    self.logger.progress(i, len(file_paths), f"处理文件: {file_path}")
                    self._process_file(file_path)
                    self.logger.success(f"文件处理完成: {file_path}")
                except Exception as e:
                    self.logger.error(f"处理文件失败 {file_path}: {str(e)}")

            # 处理所有文件夹
            self.logger.step(3, 3, "处理文件夹...")
            for i, folder_path in enumerate(folder_paths, 1):
                try:
                    self.logger.progress(i, len(folder_paths), f"处理文件夹: {folder_path}")
                    self._process_folder(folder_path)
                    self.logger.success(f"文件夹处理完成: {folder_path}")
                except Exception as e:
                    self.logger.error(f"处理文件夹失败 {folder_path}: {str(e)}")

            self.logger.section("文档生成完成")
            self.logger.info(f"成功处理 {len(file_paths)} 个文件和 {len(folder_paths)} 个文件夹")
            self.logger.info(f"文档已保存到: {self.doc_root}\n")

    def _process_file(self, file_path):
        """
        处理单个代码文件
        :param file_path: 代码文件路径
        """
        # 生成文档路径
        rel_path = os.path.relpath(file_path, self.project_root)
        doc_name = f"Doc_{os.path.basename(file_path).replace('.', '_')}.md"
        doc_path = os.path.join(self.doc_root, os.path.dirname(rel_path), doc_name)

        self.logger.info(f"[读取文件] {file_path}")
        
        # 创建文档目录
        os.makedirs(os.path.dirname(doc_path), exist_ok=True)

        # 读取代码文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            code_content = f.read()
        self.logger.success("成功读取源代码")

        # 检查是否存在现有文档
        existing_doc = ""
        if os.path.exists(doc_path):
            with open(doc_path, 'r', encoding='utf-8') as f:
                existing_doc = f.read()
            self.logger.warning("发现现有文档，将分析是否需要更新")

        # 准备提示词
        context = f"""
现有文档内容(如果为空则代表无现有文档):
{existing_doc}

源代码内容:
{code_content}
"""
        # 生成文档
        doc_content = self.openai.generate_document(context, self.code_prompt)

        # 写入文档
        self.logger.info(f"[保存文档] {doc_path}")
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)
        self.logger.success("文档已保存")

    def _process_folder(self, folder_path):
        """
        处理文件夹，生成模块文档
        :param folder_path: 文件夹路径
        """
        # 生成文档路径
        rel_path = os.path.relpath(folder_path, self.project_root)
        doc_name = f"Doc_module_{os.path.basename(folder_path)}.md"
        doc_path = os.path.join(self.doc_root, rel_path, doc_name)

        self.logger.info(f"[处理文件夹] {folder_path}")
        
        # 创建文档目录
        os.makedirs(os.path.dirname(doc_path), exist_ok=True)

        # 收集文件夹内所有文档内容
        docs_content = []
        doc_folder_path = os.path.join(self.doc_root, rel_path)
        if os.path.exists(doc_folder_path):
            self.logger.info("[收集文档] 正在收集文件夹内的现有文档...")
            for file in os.listdir(doc_folder_path):
                if file.startswith("Doc_") and file != doc_name:
                    try:
                        file_path = os.path.join(doc_folder_path, file)
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        docs_content.append(content)
                        self.logger.success(f"成功读取文档: {file}")
                    except Exception as e:
                        self.logger.error(f"读取文档失败 {file}: {str(e)}")

        # 检查是否存在现有模块文档
        existing_doc = ""
        if os.path.exists(doc_path):
            with open(doc_path, 'r', encoding='utf-8') as f:
                existing_doc = f.read()
            self.logger.warning("发现现有模块文档，将分析是否需要更新")

        # 准备提示词
        context = f"""
现有模块文档内容(如果为空则代表无现有文档):
{existing_doc}

文件夹内所有文档内容:
{''.join(docs_content)}
"""
        # 生成文档
        doc_content = self.openai.generate_document(context, self.module_prompt)

        # 写入文档
        self.logger.info(f"[保存文档] {doc_path}")
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)
        self.logger.success("模块文档已保存")
