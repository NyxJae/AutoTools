"""
API和路径配置
"""
import os

# OpenAI API配置
API_KEY = "sk-JnjCG9WAhWqXqJLwX4PwZhXLmOZgYluOQnzQBvXOWXpmYE2R"
BASE_URL = "https://ai98.vip/v1"
MODEL_NAME = "claude-3-5-sonnet-20241022"

# 项目路径配置
PROJECT_ROOT = "d:/Personal/Documents/AutoTools"
DOC_ROOT = os.path.join(PROJECT_ROOT, "Docs")

# API请求配置
MAX_RETRIES = 3  # 最大重试次数
RETRY_DELAY = 2  # 重试等待时间(秒)
REQUEST_TIMEOUT = 60  # 请求超时时间(秒)
