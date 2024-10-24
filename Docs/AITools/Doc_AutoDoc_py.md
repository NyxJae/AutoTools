# AutoDoc 自动文档生成工具文档

## 1. 模块概述

`AutoDoc` 是一个自动文档生成工具的主入口模块。它集成了配置和核心处理模块，并提供一个简单的接口用于生成项目文档。

## 2. 主要功能和类说明

### AutoDoc 类

`AutoDoc` 为自动文档生成器的核心类，负责初始化和管理与 OpenAI 的连接以及文档处理的过程。

- **属性**
  - `api_key`: 用于访问 OpenAI API 的密钥。
  - `openai`: `OpenAIConnection`实例，用于与 OpenAI API进行通信。
  - `processor`: `DocProcessor`实例，负责文档生成的处理工作。

## 3. 关键方法的参数和返回值说明

### `__init__(self, api_key=None)`

- **参数**
  - `api_key` (str, 可选): OpenAI API 密钥，若不提供将使用默认设置中的 API 密钥。

- **行为**
  - 初始化 `OpenAIConnection` 并设置相关属性。
  - 初始化 `DocProcessor`，用于处理文档的生成。

### `generate_docs(self, paths)`

- **参数**
  - `paths` (list): 需要生成文档的路径列表。

- **行为**
  - 使用 `DocProcessor` 对提供的路径进行文档生成处理。

## 4. 使用示例或注意事项

### 示例

```python
if __name__ == "__main__":
    auto_doc = AutoDoc(api_key="您的API密钥")
    paths_to_process = ["AITools"]
    auto_doc.generate_docs(paths_to_process)
```

### 注意事项

- 确保在运行前已配置正确的 API 密钥和其他设置参数。
- 路径列表中的路径应指向有效的代码项目目录，以便正确生成文档。

## 5. 依赖关系说明

- **内部模块**
  - `core.OpenAIConnector`: 提供与 OpenAI API 的连接功能。
  - `core.processor`: 负责文档生成的处理逻辑。
  - `config`: 包含所有的配置设置和提示文本。

- 提供的 API 密钥和配置的 URL、模型名等参数需要在 `settings` 模块中定义。

此文档对现有代码进行了详细的解释和说明，帮助开发者快速理解并使用 `AutoDoc` 模块进行文档生成工作。