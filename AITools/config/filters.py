"""
文件过滤配置
"""

# 配置要排除的目录
EXCLUDE_DIRS = {
    'test',          # 测试目录
    'tests',         # 测试目录
    'backup',        # 备份目录
    'temp',          # 临时文件目录
    'logs',          # 日志目录
    'build',         # 构建输出目录
    'dist',          # 分发目录
    '.pytest_cache',  # pytest缓存
    '__pycache__',   # Python字节码缓存
    '.git',          # Git目录
    '.idea',         # IDE配置
    'node_modules',  # Node.js依赖
    'venv',          # Python虚拟环境
    'env',           # Python虚拟环境
}

# 配置要排除的文件类型
EXCLUDE_EXTENSIONS = {
    # 编译和字节码文件
    '.pyc', '.pyo', '.pyd',  # Python
    '.class', '.jar',        # Java
    '.o', '.a', '.so',       # C/C++
    '.dll', '.exe',          # Windows
    
    # 临时文件
    '.tmp', '.temp',
    '.bak', '.backup',
    '.swp', '.swo',          # Vim
    
    # 日志文件
    '.log',
    
    # 系统文件
    '.DS_Store',             # macOS
    'Thumbs.db',             # Windows
    
    # 其他二进制文件
    '.zip', '.tar', '.gz', '.rar',
    '.png', '.jpg', '.jpeg', '.gif',
    '.pdf', '.doc', '.docx',
}
