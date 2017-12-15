#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import time
import db_conn

# get db connection
db = db_conn.db
# use cursor
cursor = db.cursor()

# 获取命令行参数
#server_source = '10.73.129.187'
#db_source = 'test123'
server_source = sys.argv[1]
db_source = sys.argv[2]

try:
	# SQL 查询语句
	sql = "select id, server_source, port_source, user_source, password_source, db_source, table_source," \
		  "server_dest, port_dest, user_dest, password_dest, db_dest, table_dest, archive_condition " \
		  "from db_archive_info " \
		  "where server_source = '%s' and db_source = '%s' " % (server_source, db_source)

	# 执行SQL语句
	cursor.execute(sql)
	# 获取所有记录列表
	results = cursor.fetchall()

	for row in results:
		id = row[0]
		server_source = row[1]
		port_source = row[2]
		user_source = row[3]
		password_source = row[4]
		db_source = row[5]
		table_source = row[6]
		server_dest= row[7]
		port_dest = row[8]
		user_dest = row[9]
		password_dest = row[10]
		db_dest = row[11]
		table_dest = row[12]
		archive_condition = row[13]

		# 归档开始时间
		archive_starttime = time.strftime('%Y-%m-%d %H:%M:%S')

		# 生成pt-archive命令
		archive_cmd = "pt-archiver " \
					 "--source h='%s',P='%s',u='%s',p='%s',D='%s',t='%s' " \
					 "--dest h='%s',P='%s',u='%s',p='%s',D='%s',t='%s' " \
					 "--charset=UTF8 --where '%s' --progress 50000 --limit 10000 --txn-size 10000 " \
					 "--bulk-insert --bulk-delete --statistics --purge " % \
					 (server_source, port_source, user_source, password_source, db_source, table_source, \
		  			  server_dest, port_dest, user_dest, password_dest, db_dest, table_dest, \
					  archive_condition)
		#print archive_cmd

		# make a copy of original stdout route
		stdout_archive = sys.stdout
		# define the log file that receives your log info
		log_file = open("/software/python_script/db_archive_%s_%s.log"% (db_source, table_source), "w")
		# redirect print output to log file
		sys.stdout = log_file

		#archive_cmd = os.popen(pt_archive)
		with os.popen(archive_cmd) as c:
		#with open("db_archive1.log", "r") as c:
			archive_log = c.read()
			print archive_log

		# close log file
		log_file.close()
		# restore the output to initial pattern
		sys.stdout = stdout_archive

		# 定义归档相关变量
		inserted_qty = 0
		deleted_qty = 0
		# 归档结束时间
		archive_endtime = time.strftime('%Y-%m-%d %H:%M:%S')

		with open("/software/python_script/db_archive_%s_%s.log"% (db_source, table_source),"r") as f:
			for line in f:
				if 'INSERT' in line:
					i = line.index(" ")
					inserted_qty = line[i+1:]
				elif 'DELETE' in line:
					i = line.index(" ")
					deleted_qty = line[i+1:]

		#判断归档是否失败
		if inserted_qty == deleted_qty:
			archive_status = 'Y'
			archive_error = ''
		else:
			archive_status = 'N'
			archive_error = 'inserted_qty and deleted_qty are not equal'

		# insert sql
		sql_insert = "insert into db_archive_log(server_source, db_source, table_source, server_dest, " \
					 "db_dest, table_dest, archive_qty, archive_cmd, archive_log, archive_start, archive_end, " \
					 "archive_status, archive_error ) " \
					 "values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
					 (server_source, db_source, table_source, server_dest, \
						db_dest, table_dest, inserted_qty, db.escape_string(archive_cmd), archive_log, archive_starttime, archive_endtime, \
					 	archive_status, archive_error)
		# exec sql
		cursor.execute(sql_insert)
		# exec commit
		db.commit()

		if archive_status == 'Y':
			sql_update = "update db_archive_info " \
					 	 "set datetime_modified = '%s', last_archive_date = '%s', last_archive_qty = %s " \
					 	 "where id = %d" % \
					 	 (archive_starttime, archive_endtime, inserted_qty, id)
			cursor.execute(sql_update)
			# exec commit
			db.commit()

except  Exception, e:
	print str(Exception)
	print str(e)
