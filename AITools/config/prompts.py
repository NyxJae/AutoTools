"""
文档生成提示词配置
"""

# 代码文件文档生成提示词
CODE_PROMPT = """
请分析以下代码文件，生成详细的文档说明。如果有现有文档，请分析后决定是否需要更新。
文档应包含：
1. 模块概述
2. 主要功能和类的说明
3. 关键方法的参数和返回值说明
4. 使用示例或注意事项
5. 依赖关系说明
请确保文档清晰易懂，并保持专业性。
"""

# 模块文档生成提示词
MODULE_PROMPT = """
请根据所有文档内容，生成一个完整的模块文档。如果有现有文档，请分析后决定是否需要更新。
文档应包含：
1. 模块的整体架构和目的
2. 各子模块或文件的关系和职责
3. 关键功能和接口说明
4. 模块级别的使用说明和注意事项
请确保文档结构清晰，突出模块的整体性和关联性。
"""
