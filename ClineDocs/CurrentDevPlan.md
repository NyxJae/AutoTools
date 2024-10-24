# 当前开发计划

## 1. 参考文档与源码分析
### 1.1 核心文件
- AITools/AutoDoc.py: 主入口文件
- AITools/config/settings.py: 配置文件，定义文档生成路径
- AITools/core/processor.py: 文档生成核心逻辑

### 1.2 当前实现分析
- 文档生成路径由 settings.py 中的 DOC_ROOT 控制
- 文档生成逻辑在 processor.py 中的 DocProcessor 类实现
- AutoDoc.py 作为入口文件调用 DocProcessor

## 2. 优化策略与计划
### 2.1 路径生成逻辑修改
1. 修改 settings.py：
   - 移除固定的 DOC_ROOT 配置
   - 添加新的配置项 DOC_SUFFIX="_docs" 用于生成文档目录名

2. 修改 processor.py：
   - 重构 get_doc_path() 方法，使其在源代码目录旁生成文档
   - 添加目录存在检查和创建逻辑
   - 优化错误处理

3. 修改 AutoDoc.py：
   - 更新文档路径的处理逻辑
   - 增加文档生成位置的日志输出

### 2.2 具体修改步骤
1. settings.py 修改
2. processor.py 重构
3. AutoDoc.py 更新
4. 测试验证

## 3. 测试计划
- 对不同层级的目录进行测试
- 验证文档是否正确生成在源码目录旁
- 测试错误处理机制
