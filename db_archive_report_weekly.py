#!/usr/bin/python
# -*- coding: UTF-8 -*-

import db_conn
import os
import time
import smtp_config
from email.mime.text import MIMEText
from email.header import Header

def send_mail(mail_msg):
    # 调用send_mail函数
    mail_body = """
    <style type="text/css">
    table.gridtable {
    	font-family: verdana,arial,sans-serif;
    	font-size:11px;
    	color:#333333;
    	border-width: 1px;
    	border-color: #666666;
    	border-collapse: collapse;
    }
    table.gridtable th {
    	border-width: 1px;
    	padding: 8px;
    	border-style: solid;
    	border-color: #666666;
    	background-color: #dedede;
    }
    table.gridtable td {
    	border-width: 1px;
    	padding: 8px;
    	border-style: solid;
    	border-color: #666666;
    	background-color: #ffffff;
    }
    </style>

    <!-- Table goes in the document BODY -->
    <table class="gridtable">
    <tr>
    	<th>序号</th><th>归档周次</th><th>归档日期-起</th><th>归档日期-止</th>
    	<th>服务器</th><th>数据库</th><th>表名</th><th>归档成功</th><th>归档失败</th>
    	<th >总归档数据量(行)</th><th>总归档时长(分钟)</th><th>平均归档数据量(行)</th><th>平均归档时长(分钟)</th>
    </tr>
        """
    mail_body = mail_body + mail_msg + "</table>"
    message = MIMEText(mail_body, 'html', 'utf-8')
    subject = 'DB归档周报'
    message['Subject'] = Header(subject, 'utf-8')
    smtp_config.send_mail(message)
    return
#定义邮件体变量
mail_msg = ""

# 获取数据库连接
db = db_conn.db
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 查询语句
# 备份日报
sql_archive_report = "select cast((@i:= @i+1) as char) as id, archive_week, archive_week_start, archive_week_end, " \
                     "substr(server_source,1,15) server_source, db_source, table_source, archive_success_qty, archive_fail_qty, " \
                     "archive_sum_data, archive_sum_minute, archive_avg_data, archive_avg_minute " \
                        "from vw_db_archive_report_weekly t, (select @i:=0) as a"

try:
    # 执行SQL语句
    cursor.execute(sql_archive_report)
    # 获取所有记录列表
    results = cursor.fetchall()

    for row in results:
        id = str(row[0])
        archive_week = str(row[1])
        archive_week_start = str(row[2])
        archive_week_end = str(row[3])
        server_source = str(row[4])
        db_source = str(row[5])
        table_source = str(row[6])
        archive_success_qty = str(row[7])
        archive_fail_qty = str(row[8])
        archive_sum_data = str(row[9])
        archive_sum_minute = str(row[10])
        archive_avg_data = str(row[11])
        archive_avg_minute = str(row[12])

        # 生成邮件内容
        mail_msg_single = """ 
        <tr>
        	<td align="center">%s</td><td>%s</td><td>%s</td><td>%s</td>
        	<td>%s</td><td>%s</td><td>%s</td><td align="right">%s</td><td align="right">%s</td>
        	<td align="right">%s</td><td align="right">%s</td><td align="right">%s</td><td align="right">%s</td> 
        </tr> """ % \
        (id, archive_week, archive_week_start, archive_week_end, server_source, db_source, table_source,
        archive_success_qty, archive_fail_qty, archive_sum_data, archive_sum_minute, archive_avg_data, archive_avg_minute)

        mail_msg = mail_msg + mail_msg_single

        # SQL 插入语句
        sql_insert = "insert into db_archive_report_weekly(archive_week, archive_week_start, archive_week_end, server_source, db_source, "  \
			             "table_source, archive_success_qty, archive_fail_qty, archive_sum_data, archive_sum_minute, archive_avg_data, archive_avg_minute) " \
			             "values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
                         (archive_week, archive_week_start, archive_week_end, server_source, db_source,table_source, archive_success_qty, archive_fail_qty, archive_sum_data,
                         archive_sum_minute, archive_avg_data, archive_avg_minute)

        # 执行sql语句
        cursor.execute(sql_insert)
        # 提交到数据库执行
        db.commit()

    # 发送邮件
    send_mail(mail_msg)

except  Exception, e:
    print str(Exception)
    print str(e)

# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()
