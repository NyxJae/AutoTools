# AutoDoc 模块文档

## 1. 模块概述

`AutoDoc` 是一个自动化文档生成工具，旨在简化项目中文档的生成和管理。通过与 OpenAI 的集成，它可以自动生成代码文件和模块的详细文档，帮助开发者更高效地记录和理解项目。

## 2. 模块架构

### 2.1 模块关系

- **核心模块**
  - `AutoDoc`: 主入口模块，协调各个子模块进行文档生成。
  - `OpenAIConnection`: 提供与 OpenAI API 的连接功能。
  - `DocProcessor`: 负责文档生成的处理逻辑。
  - `FilePathUtils`: 提供文件路径的管理和过滤功能。
  - `Logger`: 提供统一的日志记录格式和计时功能。

- **配置模块**
  - `config`: 提供 API 和路径配置。
  - `filters`: 定义要排除的文件和目录。

### 2.2 依赖关系

- `AutoDoc` 调用 `OpenAIConnection` 进行文档生成。
- `DocProcessor` 使用 `FilePathUtils` 进行文件路径管理。
- `Logger` 负责所有模块的日志记录。

## 3. 关键功能和接口说明

### 3.1 `AutoDoc` 类

- **属性**
  - `api_key`: 用于 OpenAI API 的访问密钥。
  - `openai`: `OpenAIConnection`实例。
  - `processor`: `DocProcessor`实例。

- **方法**
  - `__init__(api_key)`: 初始化 API 连接和文档处理器。
  - `generate_docs(paths)`: 生成指定路径列表的文档。

### 3.2 `OpenAIConnection` 类

- **方法**
  - `_send_request(messages)`: 发送请求到 OpenAI API。
  - `generate_document(code, prompt)`: 生成文档内容。

### 3.3 `DocProcessor` 类

- **方法**
  - `generate_docs(paths)`: 处理路径并生成文档。
  - `_process_file(file_path)`: 处理代码文件。
  - `_process_folder(folder_path)`: 处理文件夹模块。

### 3.4 `FilePathUtils` 类

- **方法**
  - `get_all_file_paths(paths)`: 获取所有文件路径。
  - `get_all_folder_paths(paths)`: 获取所有文件夹路径。

### 3.5 `Logger` 和 `Timer` 类

- **方法**
  - `info(message)`: 输出普通信息。
  - `success(message)`: 输出成功信息。
  - `progress(current, total, message)`: 显示进度。
  - `__enter__`/`__exit__`: 计时上下文管理。

## 4. 使用说明

### 4.1 使用示例

```python
if __name__ == "__main__":
    auto_doc = AutoDoc(api_key="您的API密钥")
    paths_to_process = ["AITools"]
    auto_doc.generate_docs(paths_to_process)
```

### 4.2 注意事项

- 请确保在运行前配置正确的 OpenAI API 密钥。
- 确保路径列表中的路径有效。
- 参数 `code_prompt` 和 `module_prompt` 应根据项目需求调整。

## 5. 注意点

- 确保 API 密钥的安全性，避免泄露。
- 文档生成依赖于网络和 OpenAI 服务的可用性。
- 根据项目要求，自定义排除的目录和文件类型，避免误删除重要文件。

通过结合 OpenAI 强大的语言处理能力，`AutoDoc` 提供了一种自动化、高效的方式来管理项目文档，提升开发团队的协作和代码维护能力。