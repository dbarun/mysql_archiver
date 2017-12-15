create view vw_db_archive_report_weekly as
-- 计算前一周的数据库归档情况
select  concat(year(min(archive_start)),week(min(archive_start))) archive_week, -- 归档周次
				date_format(min(archive_start),'%Y-%m-%d') archive_week_start, -- 归档时间起
				date_format(max(archive_start),'%Y-%m-%d') archive_week_end, -- 归档时间止
				server_source, -- 服务器ip/域名
				db_source, -- 数据库schema
				table_source, -- 表名
			 ifnull(sum(case archive_status when 'Y' then 1 end),0) archive_success_qty, -- 归档成功任务
		   ifnull(sum(case archive_status when 'N' then 1 end),0) archive_fail_qty, -- 归档失败任务
			 ifnull(sum(case archive_status when 'Y' then archive_qty end),0) archive_sum_data, -- 总归档数据量
			 ifnull(round(sum(case archive_status when 'Y' then timestampdiff(SECOND, archive_start, archive_end) end)/60,2),0) archive_sum_minute, -- 总归档时长
			 ifnull(round(sum(case archive_status when 'Y' then archive_qty end) / sum(case archive_status when 'Y' then 1 end),0),0) archive_avg_data, -- 平均归档数据量(归档数据量/归档成功任务)
			 ifnull(round(ifnull(round(sum(case archive_status when 'Y' then timestampdiff(SECOND, archive_start, archive_end) end)/60,2),0) 
       / ifnull(sum(case archive_status when 'Y' then 1 end),0),2),0) archive_avg_minute -- 平均归档时长(总归档时长/归档成功任务)
  from db_archive_log
  where week(archive_start) = week(date_add(curdate(), interval - 7 day))
  group by server_source, db_source, table_source 