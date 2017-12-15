create view vw_db_archive_fail as 
-- 汇总前一天执行失败的归档任务
select * from db_archive_info
where concat(server_source, db_source, table_source) not in 
(
  select concat(server_source, db_source, table_source) from db_archive_log
where datetime_created >= curdate()
and archive_status = 'Y'
)
order by id 