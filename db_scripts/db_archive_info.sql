/*
Navicat MySQL Data Transfer

Source Server         : 02_pro_dbbackup_db
Source Server Version : 50621
Source Host           : localhost:3306
Source Database       : db_backup

Target Server Type    : MYSQL
Target Server Version : 50621
File Encoding         : 65001

Date: 2017-12-16 01:07:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for db_archive_info
-- ----------------------------
DROP TABLE IF EXISTS `db_archive_info`;
CREATE TABLE `db_archive_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '表id',
  `server_source` varchar(640) DEFAULT NULL COMMENT '源服务器',
  `port_source` varchar(64) DEFAULT NULL COMMENT '源服务器端口',
  `user_source` varchar(64) DEFAULT NULL COMMENT '源数据库用户',
  `password_source` varchar(128) DEFAULT NULL COMMENT '源数据库密码',
  `db_source` varchar(64) DEFAULT NULL COMMENT '源数据库schema',
  `table_source` varchar(128) DEFAULT NULL COMMENT '源数据库表',
  `server_dest` varchar(640) DEFAULT NULL COMMENT '目标服务器',
  `port_dest` varchar(64) DEFAULT NULL COMMENT '目标服务器端口',
  `user_dest` varchar(64) DEFAULT NULL COMMENT '目标数据库用户',
  `password_dest` varchar(128) DEFAULT NULL COMMENT '目标数据库密码',
  `db_dest` varchar(64) DEFAULT NULL COMMENT '目标数据库schema',
  `table_dest` varchar(128) DEFAULT NULL COMMENT '目标数据库表',
  `archive_condition` varchar(1000) DEFAULT NULL COMMENT '数据归档条件',
  `last_archive_date` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最近归档时间',
  `last_archive_qty` int(10) DEFAULT NULL COMMENT '最近归档数量',
  `state` varchar(255) DEFAULT 'A' COMMENT '数据行状态',
  `user_created` varchar(128) DEFAULT 'SYS' COMMENT '数据行创建人',
  `datetime_created` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '数据行创建时间',
  `user_modified` varchar(128) DEFAULT 'SYS' COMMENT '数据行修改人',
  `datetime_modified` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '数据行修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COMMENT='数据库归档基础信息表';
