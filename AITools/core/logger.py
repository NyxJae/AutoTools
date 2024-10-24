"""
日志输出工具
提供统一的日志格式和输出函数
"""
import time

class Logger:
    @staticmethod
    def info(message):
        """普通信息输出"""
        print(message)
    
    @staticmethod
    def success(message):
        """成功信息输出"""
        print(f"[√] {message}")
    
    @staticmethod
    def warning(message):
        """警告信息输出"""
        print(f"[!] {message}")
    
    @staticmethod
    def error(message):
        """错误信息输出"""
        print(f"[×] {message}")
    
    @staticmethod
    def progress(current, total, message):
        """进度信息输出"""
        print(f"\n--- {message} ({current}/{total})")
    
    @staticmethod
    def section(message):
        """段落标题输出"""
        print(f"\n=== {message} ===")
    
    @staticmethod
    def step(step_num, total_steps, message):
        """步骤信息输出"""
        print(f"\n[{step_num}/{total_steps}] {message}")

class Timer:
    def __init__(self, description="操作"):
        """
        初始化计时器
        :param description: 操作描述
        """
        self.description = description
        self.start_time = None
    
    def __enter__(self):
        """开始计时"""
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """结束计时并输出耗时"""
        end_time = time.time()
        duration = end_time - self.start_time
        print(f"{self.description}耗时: {duration:.2f}秒")
