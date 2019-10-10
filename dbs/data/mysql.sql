--
-- Current Database: `lims_project`
--

USE `lims_project`;

-- 实验室
TRUNCATE TABLE `laboratory`;
INSERT INTO `laboratory` VALUES (1, '实验室1', '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `laboratory` VALUES (2, '实验室2', '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');

-- 部门
TRUNCATE TABLE `department`;
INSERT INTO `department` VALUES (1, '实验室1-部门1', 1, '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `department` VALUES (2, '实验室1-部门2', 1, '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `department` VALUES (3, '实验室2-部门1', 2, '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `department` VALUES (4, '实验室2-部门2', 2, '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');

-- 单位
TRUNCATE TABLE `company`;
INSERT INTO `company` VALUES (1, '单位名称工商局1', '', '', '', '', '', 1, '', 0, 0, NULL, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `company` VALUES (2, '单位名称工商局2', '', '', '', '', '', 1, '', 0, 0, NULL, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `company` VALUES (3, '单位名称客户1', '', '', '', '', '', 2, '', 0, 0, NULL, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `company` VALUES (4, '单位名称客户2', '', '', '', '', '', 2, '', 0, 0, NULL, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');

-- 联系人
TRUNCATE TABLE `contact`;
INSERT INTO `contact` VALUES (1, 1, '小李', '', '', '', '', 0, 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `contact` VALUES (2, 1, '小王', '', '', '', '', 0, 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `contact` VALUES (3, 2, '小张', '', '', '', '', 0, 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `contact` VALUES (4, 2, '小明', '', '', '', '', 0, 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');

-- 等级
TRUNCATE TABLE `grade`;
INSERT INTO `grade` VALUES (1, 'A级', '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `grade` VALUES (2, 'B级', '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `grade` VALUES (3, 'C级', '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `grade` VALUES (4, 'D级', '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');

-- 标准
TRUNCATE TABLE `standard`;
INSERT INTO `standard` VALUES (1, 'GB-2016', '标准1', '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `standard` VALUES (2, 'GB-2017', '标准2', '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `standard` VALUES (3, 'GB-2018', '标准3', '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `standard` VALUES (4, 'GB-2019', '标准4', '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');

-- 方法
TRUNCATE TABLE `manner`;
INSERT INTO `manner` VALUES (1, 'GB-2016', '标准1', '', '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `manner` VALUES (2, 'GB-2017', '标准2', '', '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `manner` VALUES (3, 'GB-2018', '标准3', '', '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `manner` VALUES (4, 'GB-2019', '标准4', '', '', 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');

-- 标准方法关系
TRUNCATE TABLE `map_standard_manner`;
INSERT INTO `map_standard_manner` VALUES (1, 1, 1, 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `map_standard_manner` VALUES (2, 1, 3, 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `map_standard_manner` VALUES (3, 2, 1, 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
INSERT INTO `map_standard_manner` VALUES (4, 2, 4, 0, NULL, '2018-03-14 10:00:00', '2018-03-14 10:00:00');
