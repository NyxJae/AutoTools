# 日志输出工具模块

## 模块概述

该模块提供了一组用于输出格式化日志信息的工具，以及一个用于测量代码执行时间的计时器类。通过这些工具，用户可以在控制台上输出具有一致格式的普通信息、成功提示、警告、错误信息、进度信息、段落标题和步骤信息。

## 主要功能和类的说明

### Logger 类

- **info(message)**: 输出普通信息。

- **success(message)**: 输出成功信息，前缀为 `[√]`。

- **warning(message)**: 输出警告信息，前缀为 `[!]`。

- **error(message)**: 输出错误信息，前缀为 `[×]`。

- **progress(current, total, message)**: 输出进度信息，显示当前进度和总进度。

- **section(message)**: 输出段落标题，格式化为 `=== message ===`。

- **step(step_num, total_steps, message)**: 输出步骤信息，显示当前步骤和总步骤数。

### Timer 类

用于测量代码块的执行时间，适合使用上下文管理器来控制计时的开始和结束。

- **`__init__(description="操作")`**: 初始化计时器，可以传入一个描述字符串。
  
- **`__enter__()`**: 开始计时。

- **`__exit__(exc_type, exc_val, exc_tb)`**: 结束计时并输出耗时。

## 关键方法的参数和返回值说明

### Logger 类

- **info, success, warning, error**:
  - 参数: `message` (str) - 要输出的日志信息。
  - 返回值: 无返回值。

- **progress**:
  - 参数: 
    - `current` (int) - 当前进度。
    - `total` (int) - 总进度。
    - `message` (str) - 进度信息。
  - 返回值: 无返回值。

- **section**:
  - 参数: `message` (str) - 段落标题内容。
  - 返回值: 无返回值。

- **step**:
  - 参数: 
    - `step_num` (int) - 当前步骤号。
    - `total_steps` (int) - 总步骤数。
    - `message` (str) - 步骤信息。
  - 返回值: 无返回值。

### Timer 类

- **`__init__`**
  - 参数: `description` (str) - 操作描述，默认为“操作”。
  - 返回值: 无返回值。

- **`__enter__`**
  - 参数: 无。
  - 返回值: 返回计时实例自身。

- **`__exit__`**
  - 参数: 
    - `exc_type`, `exc_val`, `exc_tb` - 异常类型、异常值、异常堆栈。
  - 返回值: 无返回值（默认行为）。

## 使用示例或注意事项

### Logger 使用示例

```python
Logger.info("这是一条普通信息")
Logger.success("操作成功")
Logger.warning("注意事项")
Logger.error("出错了")
Logger.progress(3, 10, "处理进度")
Logger.section("新的内容块")
Logger.step(2, 5, "第二步进行中")
```

### Timer 使用示例

```python
with Timer("复杂计算"):
    # 代码块
    result = complex_calculation()
```

## 依赖关系说明

- 该模块依赖于 Python 内置的 `time` 模块，用于实现 `Timer` 类的计时功能。无其他外部依赖。