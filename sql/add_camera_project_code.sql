-- 添加 single_project_code 字段到 camera 表
ALTER TABLE `camera` ADD COLUMN `single_project_code` varchar(64) DEFAULT NULL COMMENT '名称：项目编码；' AFTER `province_code`;

-- 验证字段是否添加成功
DESCRIBE camera;