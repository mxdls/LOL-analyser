/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50709
Source Host           : localhost:3306
Source Database       : lol

Target Server Type    : MYSQL
Target Server Version : 50709
File Encoding         : 65001

Date: 2017-07-26 11:47:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for battle
-- ----------------------------
DROP TABLE IF EXISTS `battle`;
CREATE TABLE `battle` (
  `battleId` varchar(20) NOT NULL,
  `type` int(11) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`battleId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for battledetail
-- ----------------------------
DROP TABLE IF EXISTS `battledetail`;
CREATE TABLE `battledetail` (
  `battleId` varchar(20) NOT NULL,
  `userId` varchar(20) NOT NULL,
  `win` int(11) DEFAULT NULL,
  `heroId` int(11) DEFAULT NULL,
  PRIMARY KEY (`battleId`,`userId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for hero
-- ----------------------------
DROP TABLE IF EXISTS `hero`;
CREATE TABLE `hero` (
  `heroId` int(11) NOT NULL,
  `displayName` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`heroId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `userId` varchar(20) NOT NULL,
  `userName` varchar(255) DEFAULT NULL,
  `zonepy` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `t` int(11) DEFAULT NULL,
  `r` int(11) DEFAULT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;
