#!/usr/bin/python
# -*- coding: UTF-8 -*-

import db_conn
from db_log import db_archive_monitor_log

# 获取日志
logger = db_archive_monitor_log.logger

# 获取数据库连接
db = db_conn.db
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 查询语句
# 需要归档的任务数量
sql_archive_summary = "select count(*) qty from db_archive_info"
# 归档失败的任务数量
sql_archive_results = "select count(*) qty from vw_db_archive_fail"

try:
    # 执行SQL语句
    cursor.execute(sql_archive_summary)
    # 获取所有记录列表
    results_archive_summary = cursor.fetchall()
    # 获取需要归档的任务数量
    for row in results_archive_summary:
        qty_archive_summary = row[0]
        #print qty_archive_summary

    # 执行SQL语句
    cursor.execute(sql_archive_results)
    # 获取所有记录列表
    results_archive_results = cursor.fetchall()
    # 获取归档失败的任务数量
    for row in results_archive_results:
        qty_archive_results = row[0]
        #print qty_archive_results

    # 判断是否归档成功
    if qty_archive_results == 0:
        logger.info("ok\n")
        logger.info("=========== DB归档汇总 ===========\n")
        logger.info("归档任务:" + str(qty_archive_summary))
        logger.info("归档失败:" + str(qty_archive_results))
        logger.info("\n=========== DB归档汇总 ===========")
    else:
        logger.info("false\n")
        logger.info("=========== DB归档汇总 ===========\n")
        logger.info("归档任务:" + str(qty_archive_summary))
        logger.info("归档失败:" + str(qty_archive_results))
        logger.info("归档失败详细信息")

        # 归档失败信息
        sql_select = "select id, substr(server_source,1,20) server_source, db_source, table_source from vw_db_archive_fail"

        # 执行SQL语句
        cursor.execute(sql_select)
        # 获取所有记录列表
        results = cursor.fetchall()

        for row in results:
            id = row[0]
            server_source = row[1]
            db_source = row[2]
            table_source = row[3]

            # 打印归档失败详细信息
            logger.info("[" + str(id) + "]   " + server_source + "  " + db_source + "  " + table_source )

        logger.info("\n=========== DB归档汇总 ===========")

except  Exception, e:
    print str(Exception)
    print str(e)

# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()
