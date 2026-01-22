create database uvp charset utf8mb4 collate utf8mb4_0900_bin;

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

-- 创建电压等级枚举表（可选）
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
