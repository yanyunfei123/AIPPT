# app/utils/logger.py

import logging
import os
from logging.handlers import TimedRotatingFileHandler

# 日志目录
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# 日志文件基础名（不包含时间）
log_file_base = os.path.join(log_dir, "aippt")

# 创建 logger 对象
logger = logging.getLogger("AIPPT")
logger.setLevel(logging.INFO)

# 控制台日志
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s"))
logger.addHandler(console_handler)

# 文件日志（按天切割，每天生成一个）
file_handler = TimedRotatingFileHandler(
    filename=log_file_base,
    when="midnight",         # 每天 0 点新建文件
    interval=1,
    backupCount=14,          # 保留最近 14 天日志，可改
    encoding='utf-8',
    utc=False
)

# 设置日志文件名格式为：aippt_2025-07-02.log
file_handler.suffix = "%Y-%m-%d.log"
file_handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s"))
logger.addHandler(file_handler)
