Python写的很多零零散散的小工具

现在要写一个脚本
在 "../AITools" 文件中写脚本

已创建以下工具类和模块：
1. **OpenAIConnector.py**: 用于与 OpenAI API 连接，发送请求并生成文档。
2. **FilePathUtils.py**: 提供路径工具，获取文件和文件夹路径，支持文件类型筛选。
3. **AutoDoc.py**: 初始化并测试 OpenAI 连接。


依据：
API_KEY = "sk-5WVwOmZqjuuhXiQZ5d4c8c1e1dB24fF4B59630C66fB91cFe"
BASE_URL = "https://35fast.aigcbest.top/v1"
MODEL_NAME = "gpt-4o-2024-08-06"
一个代码文件文档提示词:
一个代码模块(文件夹)文档提示词:
一个文档目录绝对路径:
一个项目根目录绝对路径:
需写文档的文件或文件夹相对路径列表:

需遍历列表中的文件和文件夹下的所有文件与递归子文件

让模型写代码文档 每次写文档时会先去对应路径下查找文档,如果已有,也将文档加到上下文中,看是否需要更新,如果没有文档就写一个新的文档

1. 文档以 "Doc_" 为前缀,参考的代码文件名加格式为后缀,格式是md(eg: 代码文件名:TempWorld.cs 代码文件名:Doc_TempWorld_cs.md)
2. 在文档文件夹地址下生成文档,路径结构和源代码路径一致(eg:代码文件项目路径:Root/src/world/TempWorld.cs   (Docs是文档文件夹)文档路径:Docs/Root/src/world/Doc_TempWorld_cs.md)
3. 当路径为文件夹时,将根据文件夹内(不包括子文件夹)的所有文档生成总的模块文档,根据文件夹名,以 Doc_model_fieldName.md 为名称

先对所有代码文件生成文档,用代码文件文档提示词
,然后在对所有文件夹生成文档,代码模块(文件夹)文档提示词
