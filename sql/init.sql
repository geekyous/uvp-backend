create database uvp charset utf8mb4 collate utf8mb4_0900_bin;

CREATE TABLE `ps_single_project_info`
(
    `id`                          varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '主键',
    `build_unit_code`             varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '建设管理单位编码',
    `build_unit_name`             varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '建设管理单位名称',
    `area`                        varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci   DEFAULT NULL COMMENT '区域',
    `single_project_type`         varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '单项工程类型',
    `single_project_prer_type`    varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '单项工程预规类型',
    `single_project_details_type` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '单项工程明细类型',
    `safety_project_status`       varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '安全工程状态',
    `is_work`                     varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '是否在施',
    `is_stop`                     varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '是否停工',
    `scale`                       text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci COMMENT '项目规模',
    `voltage_level`               varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '电压等级',
    `constr_nature`               varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '建设性质',
    `project_num`                 varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '项目编号',
    `safety_code`                 varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '安全编码',
    `parent_name`                 varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '隶属大项工程名称',
    `prj_code`                    varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '隶属大项工程编码',
    `construction_line_length`    decimal(17, 3)                                                DEFAULT NULL COMMENT '建设线路长度',
    `constr_transformer_capacity` decimal(17, 3)                                                DEFAULT NULL COMMENT '建设变电容量',
    `production_line_length`      decimal(17, 3)                                                DEFAULT NULL COMMENT '投产线路长度',
    `prod_trans_capacity`         decimal(17, 3)                                                DEFAULT NULL COMMENT '投产变电容量',
    `name`                        varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '单项工程名称',
    `safety_director`             varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '安全总监(SM2密文)',
    `construction_organization`   varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '建设单位',
    `supervisor_organization`     varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '监理单位',
    `builder`                     varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '施工单位',
    `location_province`           varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '单项所在省编码，',
    `location_province_name`      varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '单项所在省名称',
    `location_municipality`       varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '单项所在市编码',
    `location_municipality_name`  varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '单项所在市名称，',
    `location_area`               varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '单项所在区/县编码，',
    `location_area_name`          varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '单项所在区/县名称',
    `planned_start_time`          date                                                          DEFAULT NULL COMMENT '计划开工时间',
    `actual_start_time`           date                                                          DEFAULT NULL COMMENT '实际开工时间',
    `planned_commissioning_time`  date                                                          DEFAULT NULL COMMENT '计划投产时间',
    `actual_commissioning_time`   date                                                          DEFAULT NULL COMMENT '实际投产时间',
    `planned_completion_time`     date                                                          DEFAULT NULL COMMENT '计划竣工时间',
    `actual_completion_time`      date                                                          DEFAULT NULL COMMENT '实际竣工时间',
    `week_plan_range`             varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '次周计划日期范围',
    `construction_status`         int                                                           DEFAULT NULL COMMENT '在建状态：默认0：0：施工；1：暂停；',
    `status_from_weekly`          int                                                           DEFAULT NULL COMMENT '工程状态',
    `basic_data`                  int                                                           DEFAULT '0' COMMENT '基础数据 1 基础数据 0 非基础数据',
    `sync_time`                   datetime                                                     NOT NULL COMMENT '数据同步时间',
    `sync_source`                 varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '数据同步来源',
    `session`                     varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '同步session',
    `created_by`                  varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '创建人',
    `created_at`                  datetime                                                     NOT NULL COMMENT '创建时间',
    `updated_by`                  varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '最近一次更新人',
    `updated_at`                  datetime                                                      DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最近一次更新时间',
    `ext_id`                      varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  DEFAULT NULL COMMENT '外部Id',
    `src_flag`                    varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '数据来源标记',
    `enable_modify_week_plan`     varchar(32)                                                   DEFAULT '1' COMMENT '是否可修改周计划项目规模',
    `remarks`                     text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci COMMENT '备注',
    PRIMARY KEY (`id`) USING BTREE,
    KEY `idx_safety_code` (`safety_code`) USING BTREE,
    KEY `idx_project_num` (`project_num`) USING BTREE,
    KEY `idx_name` (`name`) USING BTREE,
    KEY `idx_buc_bun_parentName_prjCode` (`build_unit_code`, `build_unit_name`, `parent_name`, `prj_code`) USING BTREE,
    KEY `idx_extId_voltageLevel` (`ext_id`, `voltage_level`) USING BTREE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci
  ROW_FORMAT = DYNAMIC COMMENT ='单项项目工程信息表';

-- ----------------------------
-- 认证信息表
-- ----------------------------
create table api_credential
(
    access_key varchar(64) primary key,
    secret_key varchar(128),
    app_name   varchar(128),
    status     tinyint,
    expire_at  datetime,
    created_at datetime
) engine innodb;

-- ----------------------------
-- 资源信息表
-- ----------------------------
-- 创建资源表
CREATE TABLE device_resource
(
    id             VARCHAR(64)  NOT NULL PRIMARY KEY COMMENT '资源ID',
    text           VARCHAR(255) NOT NULL COMMENT '资源名称',
    dev_short_name VARCHAR(100) COMMENT '设备简称',
    p_notes        TEXT COMMENT '备注信息',
    p_code         VARCHAR(100) COMMENT '父节点编码',
    url            VARCHAR(500) COMMENT '资源链接',
    open_type      INT                   DEFAULT 0 COMMENT '资源打开方式',
    pid            VARCHAR(50) COMMENT '父节点ID',
    path           VARCHAR(1000) COMMENT '资源路径',
    type           INT COMMENT '资源类型',
    is_group       INT          NOT NULL DEFAULT 0 COMMENT '是否为分组(1：分组，0：设备)',
    is_available   INT          NOT NULL DEFAULT 1 COMMENT '资源状态 1:有效；0:无效',
    `order`        INT          NOT NULL DEFAULT 0 COMMENT '展示顺序',
    has_children   BOOLEAN      NOT NULL DEFAULT FALSE COMMENT '是否有子节点 true:是；false:否',
    status         INT          NOT NULL DEFAULT 0 COMMENT '设备状态 0:不在线；1:在线；2:不可用',
    is_outernet    INT                   DEFAULT 0 COMMENT '是否外网 0:内网；1:外网',
    s_decode_tag   VARCHAR(10) COMMENT '设备解码标签 108:H265；100:H264；150:非标',
    dev_code       VARCHAR(100) NOT NULL COMMENT '设备编码',
    dev_type       VARCHAR(2)   NOT NULL COMMENT '设备类型',
    lng            DECIMAL(10, 6) COMMENT '经度位置',
    lat            DECIMAL(10, 6) COMMENT '纬度位置',
    children_count INT                   DEFAULT NULL DEFAULT 0 COMMENT '子节点数量',
    gis_peer_code  VARCHAR(100) COMMENT 'GIS侧标识设备的编码',
    sys_info_code  VARCHAR(100) COMMENT '设备所属前端编码',
    dvr_code       VARCHAR(100) COMMENT 'dvr编码',
    is_check       BOOLEAN               DEFAULT FALSE COMMENT '设备是否关联dvr true:是；false:否',
    font_type_code VARCHAR(2) COMMENT '电压等级',
    peer_id        VARCHAR(50) COMMENT '协议编码',
    audio          INT                   DEFAULT 0 COMMENT '是否包含音频，0：否，1：是',
    created_time   TIMESTAMP             DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_time   TIMESTAMP             DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    INDEX idx_pid (pid) COMMENT '父节点ID索引',
    INDEX idx_dev_code (dev_code) COMMENT '设备编码索引',
    INDEX idx_status (status) COMMENT '状态索引',
    INDEX idx_is_available (is_available) COMMENT '有效状态索引',
    INDEX idx_type (type) COMMENT '资源类型索引',
    INDEX idx_dev_type (dev_type) COMMENT '设备类型索引',
    INDEX idx_order (`order`) COMMENT '排序索引',
    INDEX idx_gis_peer_code (gis_peer_code) COMMENT 'GIS编码索引',
    INDEX idx_dvr_code (dvr_code) COMMENT 'DVR编码索引',
    INDEX idx_path (path(255)) COMMENT '路径索引（前缀索引）'
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4 COMMENT ='资源信息表';


CREATE TABLE `tool_box_talk`
(
    `id`                              varchar(32)  NOT NULL COMMENT '名称：主键id；',
    `off_online_flag`                 int(4)       NOT NULL COMMENT '离线标识：0-非离线，1-离线',
    `prj_name`                        varchar(255) NOT NULL COMMENT '名称：项目名称；',
    `prj_code`                        varchar(32)  NOT NULL COMMENT '名称：项目编码；',
    `ticket_id`                       varchar(32)  NOT NULL COMMENT '名称：作业票id；',
    `ticket_no`                       varchar(128) NOT NULL COMMENT '名称：作业票编号；',
    `re_assessment_risk_level`        int(4)                DEFAULT NULL COMMENT '	复测风险等级	包括：1；2；3；4；5	',
    `current_constr_headcount`        int(11)      NOT NULL COMMENT '名称：当日作业人数；',
    `construction_headcount`          int(8)                DEFAULT NULL COMMENT '	施工人数		',
    `work_start_time`                 datetime              DEFAULT NULL COMMENT '	作业开始时间		',
    `current_constr_date`             date         NOT NULL COMMENT '名称：施工时间；',
    `current_construction_status`     varchar(8)            DEFAULT NULL COMMENT '	当日施工状态	包括：01-作业中；02-暂停中；03-作业完工	',
    `work_overnight_flag`             int(4)                DEFAULT NULL COMMENT '	是否跨零点作业	包括：0-非跨零点；1-跨零点	',
    `tool_box_talk_address`           varchar(480)          DEFAULT NULL COMMENT '站班会地址',
    `tool_box_talk_longitude`         varchar(480)          DEFAULT NULL COMMENT '	站班会地理坐标-经度		',
    `tool_box_talk_Latitude`          varchar(480)          DEFAULT NULL COMMENT '	站班会地理坐标-纬度		',
    `mc_work_site_id`                 varchar(32)           DEFAULT NULL COMMENT '名称：距离站班会最近的作业部位ID；',
    `bidding_section_code`            varchar(32)           DEFAULT NULL COMMENT '	标段编码		',
    `bidding_section_name`            varchar(255)          DEFAULT NULL COMMENT '	标段名称		',
    `single_project_code`             varchar(32)           DEFAULT NULL COMMENT '	单项工程编码		',
    `single_project_name`             varchar(255)          DEFAULT NULL COMMENT '	单项工程名称		',
    `single_project_type`             int(4)                DEFAULT NULL COMMENT '	工程类型	包括：1-变电工程；2-线路工程；3-电缆工程	',
    `constr_unified_social_credit_id` varchar(18)           DEFAULT NULL COMMENT '	施工单位统一社会信用代码		',
    `construction_unit_name`          varchar(100)          DEFAULT NULL COMMENT '名称：施工单位名称；',
    `supervision_social_credit_code`  varchar(256)          DEFAULT NULL COMMENT '监理单位统一社会信用代码',
    `supervision_unit_name`           varchar(256)          DEFAULT NULL COMMENT '监理单位名称',
    `voltage_level`                   varchar(12)           DEFAULT NULL COMMENT '	电压等级		',
    `huv_flag`                        int(4)                DEFAULT '0' COMMENT '0:常规工程  1:特高压',
    `build_unit_code`                 varchar(32)           DEFAULT NULL COMMENT '名称：建设管理单位编码；',
    `province_code`                   varchar(32)           DEFAULT NULL COMMENT '名称：省公司编码；',
    `creater_id`                      varchar(32)  NOT NULL COMMENT '名称：创建人；',
    `create_time`                     datetime     NOT NULL COMMENT '名称：创建时间；',
    `updater_id`                      varchar(32)  NOT NULL COMMENT '名称：更新人；',
    `update_time`                     datetime     NOT NULL COMMENT '名称：更新时间；',
    `delete_flag`                     int(11)      NOT NULL DEFAULT '0' COMMENT '名称：删除状态；默认0，包括：0未删除，1已删除',
    PRIMARY KEY (`id`),
    KEY `daily_meeting_risk_level_reassessment_current_constr_date_index` (`re_assessment_risk_level`, `current_constr_date`),
    KEY `daily_meeting_statistics_index` (`single_project_code`, `single_project_name`, `prj_code`,
                                          `build_unit_code`) COMMENT '站班会统计分析索引',
    KEY `daily_meeting_count_index` (`re_assessment_risk_level`, `current_construction_status`,
                                     `current_constr_date`) COMMENT '站班会统计分析索引',
    KEY `tool_box_talk_current_constr_date_delete_flag_index` (`current_constr_date`, `delete_flag`),
    KEY `tool_box_talk_ticket_id_delete_flag_index` (`ticket_id`, `delete_flag`) COMMENT '作业票跳转站班会索引',
    KEY `tool_box_talk_bidding_section_code` (`bidding_section_code`),
    KEY `tool_box_talk_build_current_del_huv_index` (`build_unit_code`, `current_constr_date`, `delete_flag`, `huv_flag`) USING BTREE,
    KEY `tool_box_talk_ticket_id_index` (`ticket_id`) USING BTREE,
    KEY `tool_box_talk_current_del_huv_index` (`current_constr_date`, `delete_flag`, `huv_flag`, `province_code`,
                                               `build_unit_code`) USING BTREE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='名称：站班会；';



CREATE TABLE `camera`
(
    `id`            varchar(32) NOT NULL COMMENT '名称：主键id；',
    `camera_name`   varchar(64) DEFAULT NULL COMMENT '名称：布控球名称；',
    `camera_no`     varchar(64) NOT NULL COMMENT '名称：布控球编码；',
    `province_code` varchar(32) DEFAULT NULL COMMENT '名称：省公司编码；',
    `creater_id`    varchar(32) DEFAULT NULL COMMENT '名称：创建人；',
    `create_time`   datetime    DEFAULT NULL COMMENT '名称：创建时间；',
    `updater_id`    varchar(32) DEFAULT NULL COMMENT '名称：更新人；',
    `update_time`   datetime    DEFAULT NULL COMMENT '名称：更新时间；',
    `delete_flag`   int(11)     DEFAULT '0' COMMENT '名称：删除状态；默认0，包括：0未删除，1已删除',
    PRIMARY KEY (`id`),
    UNIQUE KEY `camera_no` (`camera_no`, `delete_flag`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='名称：布控球；';



CREATE TABLE `toolboxtalk_camera_rela`
(
    `id`               varchar(32) NOT NULL COMMENT '名称：主键id；',
    `camera_id`        varchar(32) NOT NULL COMMENT '名称：布控球id；',
    `tool_box_talk_id` varchar(32)          DEFAULT NULL COMMENT '名称：站班会id',
    `province_code`    varchar(32)          DEFAULT NULL COMMENT '名称：省公司编码；',
    `creater_id`       varchar(32) NOT NULL COMMENT '名称：创建人；',
    `create_time`      datetime    NOT NULL COMMENT '名称：创建时间；',
    `updater_id`       varchar(32) NOT NULL COMMENT '名称：更新人；',
    `update_time`      datetime    NOT NULL COMMENT '名称：更新时间；',
    `delete_flag`      int(11)     NOT NULL DEFAULT '0' COMMENT '名称：删除状态；默认0，包括：0未删除，1已删除',
    `sort_no`          int(4)      NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`),
    KEY `camera_id_index` (`camera_id`) USING BTREE,
    KEY `tool_box_talk_id_index` (`tool_box_talk_id`) USING BTREE,
    KEY `camer_rela_create_time_index` (`create_time`) USING BTREE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='名称：站班会布控球关联；';

-- 创建设备类型枚举表（可选，用于规范化设备类型）
CREATE TABLE device_type
(
    type_code   VARCHAR(2)  NOT NULL PRIMARY KEY COMMENT '设备类型编码',
    type_name   VARCHAR(50) NOT NULL COMMENT '设备类型名称',
    description VARCHAR(200) COMMENT '类型描述'
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4 COMMENT ='设备类型枚举表';

-- 插入设备类型数据
INSERT INTO device_type (type_code, type_name)
VALUES ('01', '智能网络高速球机'),
       ('02', '网络中速球机'),
       ('03', '网络固定摄像机'),
       ('04', '智能高速球机'),
       ('05', '中速球机'),
       ('06', '云台摄像机'),
       ('07', '固定摄像机'),
       ('08', '红外热成像摄像机'),
       ('09', '监拍装置'),
       ('10', '布控球'),
       ('11', '手持终端/单兵'),
       ('12', '智能安全帽'),
       ('13', '智能巡检机器人'),
       ('14', '无人机'),
       ('15', '移动采集设备'),
       ('16', '红外对射'),
       ('17', '红外双鉴'),
       ('18', '水浸探头'),
       ('19', '烟雾探测'),
       ('20', '温度探测'),
       ('21', '警笛'),
       ('22', '门禁控制器'),
       ('23', '电子围栏'),
       ('25', '震动监测'),
       ('26', '一键警报'),
       ('31', '温度传感器'),
       ('32', '湿度传感器'),
       ('33', 'SF6浓度监测设备'),
       ('41', '数据存储设备'),
       ('42', '射频增强设备'),
       ('43', '光端机'),
       ('44', '网络延伸器'),
       ('45', '交换机'),
       ('46', '防火墙'),
       ('51', '工控机/板卡DVR'),
       ('52', '嵌入式DVR/NVS'),
       ('53', 'IP Camera'),
       ('54', '综合接入设备'),
       ('55', '智能分析装置'),
       ('56', '人脸分析设备'),
       ('61', '灯光控制器'),
       ('62', '云镜控制器'),
       ('63', '告警控制器'),
       ('64', '视频切换控制器'),
       ('71', '赋值照明装置'),
       ('72', '时钟控制装置'),
       ('73', '视频解码设备'),
       ('74', '打印机'),
       ('75', '窗口采集设备'),
       ('76', '网口采集设备'),
       ('77', '综合接入装置');

-- 创建电压等级枚举表
CREATE TABLE voltage_level
(
    level_code VARCHAR(2)  NOT NULL PRIMARY KEY COMMENT '电压等级编码',
    level_name VARCHAR(50) NOT NULL COMMENT '电压等级名称'
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4 COMMENT ='电压等级枚举表';

-- 插入电压等级数据
INSERT INTO voltage_level (level_code, level_name)
VALUES ('01', '35KV及其以下'),
       ('02', '66KV'),
       ('03', '110KV'),
       ('04', '220V'),
       ('05', '330KV'),
       ('06', '500KV'),
       ('07', '750KV及其以上'),
       ('10', '其他');