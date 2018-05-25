/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50611
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50611
File Encoding         : 65001

Date: 2016-12-19 18:59:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for authorities
-- ----------------------------
DROP TABLE IF EXISTS `authorities`;
CREATE TABLE `authorities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `authority` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of authorities
-- ----------------------------
INSERT INTO `authorities` VALUES ('1', 'admin', 'ROLE_USER');
INSERT INTO `authorities` VALUES ('2', 'root', 'ROLE_USER');
INSERT INTO `authorities` VALUES ('3', 'test', 'ROLE_USER');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'admin', 'admin');
INSERT INTO `user` VALUES ('2', 'root', 'root');
INSERT INTO `user` VALUES ('15', 'MarK', '123456');
INSERT INTO `user` VALUES ('16', 'Fawofolo', '123456');
INSERT INTO `user` VALUES ('17', 'MarK', '123456');
INSERT INTO `user` VALUES ('18', 'Fawofolo', '123456');
INSERT INTO `user` VALUES ('19', 'MarK', '123456');
INSERT INTO `user` VALUES ('20', 'Fawofolo', '123456');
INSERT INTO `user` VALUES ('46', 'test', 'test');
