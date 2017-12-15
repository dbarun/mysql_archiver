#!/usr/bin/python
# -*- coding: UTF-8 -*-
#执行备份
import os
import time
import logging

# 创建一个logger
logger = logging.getLogger('simpleExample')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
log_name = r"F:\databackup\00_infrastructure\00_log\02_db_archive\db_archive_monitor.log"

fh = logging.FileHandler(os.path.join(os.getcwd(),log_name),'w')
fh.setLevel(logging.DEBUG)

# 定义handler的输出格式
#formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(message)s')
fh.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
