/*
Navicat MySQL Data Transfer

Source Server         : 02_pro_dbbackup_db
Source Server Version : 50621
Source Host           : localhost:3306
Source Database       : db_backup

Target Server Type    : MYSQL
Target Server Version : 50621
File Encoding         : 65001

Date: 2017-12-16 01:07:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for db_archive_report_weekly
-- ----------------------------
DROP TABLE IF EXISTS `db_archive_report_weekly`;
CREATE TABLE `db_archive_report_weekly` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `archive_week` varchar(6) DEFAULT NULL COMMENT '归档周次',
  `archive_week_start` varchar(10) DEFAULT NULL COMMENT '归档周次-起',
  `archive_week_end` varchar(10) DEFAULT NULL COMMENT '归档周次-止',
  `server_source` varchar(640) DEFAULT NULL COMMENT '源服务器',
  `db_source` varchar(64) DEFAULT NULL COMMENT '源数据库schema',
  `table_source` varchar(128) DEFAULT NULL COMMENT '源数据库表',
  `archive_success_qty` int(4) DEFAULT NULL COMMENT '归档成功数量',
  `archive_fail_qty` int(4) DEFAULT NULL COMMENT '归档失败数量',
  `archive_sum_data` decimal(12,2) DEFAULT NULL COMMENT '总归档数据量',
  `archive_sum_minute` decimal(12,2) DEFAULT NULL COMMENT '总归档时长',
  `archive_avg_data` decimal(12,2) DEFAULT NULL COMMENT '平均归档数据量',
  `archive_avg_minute` decimal(12,2) DEFAULT NULL COMMENT '平均归档时长',
  `state` varchar(1) DEFAULT '1' COMMENT '可用状态',
  `user_created` varchar(32) DEFAULT 'sys' COMMENT '创建人',
  `datetime_created` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `user_modified` varchar(32) DEFAULT 'sys' COMMENT '修改人',
  `datetime_modified` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COMMENT='数据库归档报表-周报';
