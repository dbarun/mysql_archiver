/*
Navicat MySQL Data Transfer

Source Server         : 02_pro_dbbackup_db
Source Server Version : 50621
Source Host           : localhost:3306
Source Database       : db_backup

Target Server Type    : MYSQL
Target Server Version : 50621
File Encoding         : 65001

Date: 2017-12-16 01:07:33
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for db_archive_log
-- ----------------------------
DROP TABLE IF EXISTS `db_archive_log`;
CREATE TABLE `db_archive_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '表id',
  `server_source` varchar(640) DEFAULT NULL COMMENT '源服务器',
  `db_source` varchar(64) DEFAULT NULL COMMENT '源数据库schema',
  `table_source` varchar(128) DEFAULT NULL COMMENT '源数据库表',
  `server_dest` varchar(640) DEFAULT NULL COMMENT '目标服务器',
  `db_dest` varchar(64) DEFAULT NULL COMMENT '目标数据库schema',
  `table_dest` varchar(128) DEFAULT NULL COMMENT '目标数据库表',
  `archive_qty` int(10) DEFAULT NULL COMMENT '归档数量',
  `archive_cmd` varchar(5000) DEFAULT NULL COMMENT '导出SQL脚本',
  `archive_log` varchar(5000) DEFAULT NULL COMMENT '归档日志',
  `archive_start` timestamp NULL DEFAULT NULL COMMENT '归档开始时间',
  `archive_end` timestamp NULL DEFAULT NULL COMMENT '归档结束时间',
  `archive_status` varchar(2) DEFAULT NULL COMMENT '归档状态',
  `archive_error` varchar(5000) DEFAULT NULL COMMENT '导出错误信息',
  `state` varchar(255) DEFAULT 'A' COMMENT '数据行状态',
  `user_created` varchar(128) DEFAULT 'SYS' COMMENT '数据行创建人',
  `datetime_created` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '数据行创建时间',
  `user_modified` varchar(128) DEFAULT 'SYS' COMMENT '数据行修改人',
  `datetime_modified` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '数据行修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=193 DEFAULT CHARSET=utf8 COMMENT='数据库归档执行日志表';
