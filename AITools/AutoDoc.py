"""
自动文档生成工具主入口
集成配置和核心处理模块，提供简单的接口
"""
from .OpenAIConnector import OpenAIConnection
from .config import settings, prompts
from .core.processor import DocProcessor


class AutoDoc:
    def __init__(self, api_key=None):
        """
        初始化自动文档生成器
        :param api_key: OpenAI API密钥，如果不提供则使用settings中的默认值
        """
        # 使用提供的API密钥或默认值
        self.api_key = api_key or settings.API_KEY
        
        # 初始化OpenAI连接
        self.openai = OpenAIConnection(
            self.api_key,
            settings.BASE_URL,
            settings.MODEL_NAME
        )
        
        # 初始化文档处理器
        self.processor = DocProcessor(
            self.openai,
            settings.DOC_ROOT,
            settings.PROJECT_ROOT,
            prompts.CODE_PROMPT,
            prompts.MODULE_PROMPT
        )

    def generate_docs(self, paths):
        """
        生成文档
        :param paths: 需要生成文档的路径列表
        """
        self.processor.generate_docs(paths)


if __name__ == "__main__":
    # 使用示例
    auto_doc = AutoDoc()
    
    # 指定要处理的路径列表
    paths_to_process = ["AITools"]
    
    # 生成文档
    auto_doc.generate_docs(paths_to_process)
