/*
 Navicat Premium Dump SQL

 Source Server         : 666
 Source Server Type    : MySQL
 Source Server Version : 80037 (8.0.37)
 Source Host           : localhost:3306
 Source Schema         : 体育馆管理

 Target Server Type    : MySQL
 Target Server Version : 80037 (8.0.37)
 File Encoding         : 65001

 Date: 11/07/2024 23:03:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admine_table
-- ----------------------------
DROP TABLE IF EXISTS `admine_table`;
CREATE TABLE `admine_table`  (
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `admin_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `admin_usr` bigint NOT NULL,
  `admin_pass` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`admin_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admine_table
-- ----------------------------
INSERT INTO `admine_table` VALUES (1, '安', 1, '1');
INSERT INTO `admine_table` VALUES (2, '王', 2, '2');
INSERT INTO `admine_table` VALUES (3, '陈', 3, '3');

-- ----------------------------
-- Table structure for borrow_table
-- ----------------------------
DROP TABLE IF EXISTS `borrow_table`;
CREATE TABLE `borrow_table`  (
  `borrow_id` int NOT NULL AUTO_INCREMENT,
  `phone_number` bigint NOT NULL,
  `tool_id` int NOT NULL,
  PRIMARY KEY (`borrow_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 27 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of borrow_table
-- ----------------------------
INSERT INTO `borrow_table` VALUES (1, 15932979418, 5);
INSERT INTO `borrow_table` VALUES (2, 15932979418, 4);
INSERT INTO `borrow_table` VALUES (22, 11111111111, 1);
INSERT INTO `borrow_table` VALUES (23, 0, 1);
INSERT INTO `borrow_table` VALUES (24, 0, 1);
INSERT INTO `borrow_table` VALUES (25, 12345678910, 5);
INSERT INTO `borrow_table` VALUES (26, 12345678911, 1);

-- ----------------------------
-- Table structure for place_table
-- ----------------------------
DROP TABLE IF EXISTS `place_table`;
CREATE TABLE `place_table`  (
  `place_id` int NOT NULL AUTO_INCREMENT,
  `open_solution` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `place_name` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `safe` date NOT NULL,
  PRIMARY KEY (`place_id` DESC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of place_table
-- ----------------------------
INSERT INTO `place_table` VALUES (6, '', '乒乓球场2', '2026-01-01');
INSERT INTO `place_table` VALUES (5, '', '乒乓球场1', '2026-03-01');
INSERT INTO `place_table` VALUES (4, '', '羽毛球场2', '2025-03-04');
INSERT INTO `place_table` VALUES (3, '', '羽毛球场1', '2025-01-15');
INSERT INTO `place_table` VALUES (2, '不开放', '篮球场2', '2025-02-12');
INSERT INTO `place_table` VALUES (1, '开放', '篮球场1', '2025-08-13');

-- ----------------------------
-- Table structure for time_table
-- ----------------------------
DROP TABLE IF EXISTS `time_table`;
CREATE TABLE `time_table`  (
  `time_id` int NOT NULL AUTO_INCREMENT,
  `place_id` int NOT NULL,
  `start_time` int NOT NULL,
  `end_time` int NOT NULL,
  `use_time` int NOT NULL,
  `user_phone` bigint NOT NULL,
  PRIMARY KEY (`time_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 61 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of time_table
-- ----------------------------
INSERT INTO `time_table` VALUES (46, 7, 8, 9, 20240708, 15932979418);
INSERT INTO `time_table` VALUES (47, 7, 8, 18, 20240709, 15932979418);
INSERT INTO `time_table` VALUES (48, 8, 8, 18, 20240709, 15932979418);
INSERT INTO `time_table` VALUES (49, 9, 8, 18, 20240709, 15932979418);
INSERT INTO `time_table` VALUES (50, 7, 8, 18, 20240710, 15932979418);
INSERT INTO `time_table` VALUES (51, 8, 8, 18, 20240710, 15932979418);
INSERT INTO `time_table` VALUES (52, 9, 8, 18, 20240710, 15932979418);
INSERT INTO `time_table` VALUES (53, 4, 8, 9, 20240708, 11111111111);
INSERT INTO `time_table` VALUES (54, 4, 12, 14, 20240708, 11111111111);
INSERT INTO `time_table` VALUES (55, 7, 9, 10, 20240708, 12345678910);
INSERT INTO `time_table` VALUES (56, 2, 8, 9, 20240708, 12345678911);
INSERT INTO `time_table` VALUES (57, 2, 8, 9, 20240709, 12345678911);
INSERT INTO `time_table` VALUES (58, 4, 8, 18, 20240709, 12345678911);
INSERT INTO `time_table` VALUES (59, 5, 8, 18, 20240709, 12345678911);
INSERT INTO `time_table` VALUES (60, 6, 8, 18, 20240709, 12345678911);

-- ----------------------------
-- Table structure for tools_table
-- ----------------------------
DROP TABLE IF EXISTS `tools_table`;
CREATE TABLE `tools_table`  (
  `tool_id` int NOT NULL AUTO_INCREMENT,
  `tool_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `yes_number` int NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`tool_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of tools_table
-- ----------------------------
INSERT INTO `tools_table` VALUES (1, '篮球', 1490, 10);
INSERT INTO `tools_table` VALUES (2, '足球', 1500, 10);
INSERT INTO `tools_table` VALUES (3, '乒乓球', 1000, 2);
INSERT INTO `tools_table` VALUES (4, '羽毛球', 990, 2);
INSERT INTO `tools_table` VALUES (5, '乒乓球拍', 496, 5);
INSERT INTO `tools_table` VALUES (6, '羽毛球拍', 500, 5);
INSERT INTO `tools_table` VALUES (7, '珍珠球', 800, 4);
INSERT INTO `tools_table` VALUES (8, '铅球', 200, 5);
INSERT INTO `tools_table` VALUES (9, '排球', 800, 10);

-- ----------------------------
-- Table structure for usr_table
-- ----------------------------
DROP TABLE IF EXISTS `usr_table`;
CREATE TABLE `usr_table`  (
  `phone_number` bigint NOT NULL,
  `white` int NOT NULL,
  `black` int NOT NULL,
  `vip` int NOT NULL,
  `usr_pass` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_equipment_reserved` int NOT NULL DEFAULT 0,
  PRIMARY KEY (`phone_number`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of usr_table
-- ----------------------------
INSERT INTO `usr_table` VALUES (0, 0, 0, 0, 'MA==', 0);
INSERT INTO `usr_table` VALUES (8, 60, 0, 1, 'MTIzNA==', 0);
INSERT INTO `usr_table` VALUES (123, 0, 5, 0, 'MTIzNDU2', 0);
INSERT INTO `usr_table` VALUES (11111111111, 2, 0, 0, 'MQ==', 0);
INSERT INTO `usr_table` VALUES (12345678910, 1, 0, 0, 'MQ==', 0);
INSERT INTO `usr_table` VALUES (12345678911, 32, 0, 0, 'MTIz', 0);
INSERT INTO `usr_table` VALUES (15932979418, 61, 0, 1, 'MTAyNA==', 0);

-- ----------------------------
-- Table structure for worker_table
-- ----------------------------
DROP TABLE IF EXISTS `worker_table`;
CREATE TABLE `worker_table`  (
  `worker_id` int NOT NULL,
  `admin_id` int NOT NULL,
  `worker_date` date NOT NULL,
  PRIMARY KEY (`worker_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of worker_table
-- ----------------------------
INSERT INTO `worker_table` VALUES (1, 1, '2024-07-14');
INSERT INTO `worker_table` VALUES (2, 2, '2024-07-13');
INSERT INTO `worker_table` VALUES (3, 3, '2024-07-12');

SET FOREIGN_KEY_CHECKS = 1;
