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
CREATE TABLE resource
(
    id             VARCHAR(32) PRIMARY KEY COMMENT '资源ID',
    text           VARCHAR(255) NOT NULL COMMENT '资源名称',
    pid            VARCHAR(32)  NULL COMMENT '父节点ID',
    path           VARCHAR(1024) COMMENT '资源完整路径',
    type           INT COMMENT '资源类型（预留）',
    is_group       TINYINT      NOT NULL COMMENT '是否分组 1=分组 0=设备',
    is_available   TINYINT      NOT NULL COMMENT '是否有效 1=有效 0=无效',
    status         TINYINT COMMENT '设备状态 0=离线 1=在线 2=不可用',
    dev_type       VARCHAR(4) COMMENT '设备类型',
    dev_code       VARCHAR(64) COMMENT '设备编码',
    protocol_type  INT COMMENT '协议类型 0:I1 1:非标 2:企标2014 3:企标2020 4:国标2016',
    s_decode_tag   VARCHAR(8) COMMENT '解码标签 100:H264 108:H265',
    is_outernet    TINYINT COMMENT '是否外网 0=内网 1=外网',
    order_num      INT          NOT NULL DEFAULT 0 COMMENT '展示顺序',
    lng            DECIMAL(10, 6) COMMENT '经度',
    lat            DECIMAL(10, 6) COMMENT '纬度',
    sys_info_code  VARCHAR(64) COMMENT '前端编码',
    dvr_code       VARCHAR(64) COMMENT 'DVR编码',
    gis_peer_code  VARCHAR(64) COMMENT 'GIS侧设备编码',
    font_type_code VARCHAR(4) COMMENT '电压等级',
    peer_id        VARCHAR(64) COMMENT '协议编码',
    audio          TINYINT COMMENT '是否包含音频 0=否 1=是',
    p_notes        VARCHAR(512) COMMENT '备注信息',
    p_code         VARCHAR(64) COMMENT '父节点编码',
    url            VARCHAR(512) COMMENT '资源URL',
    open_type      INT COMMENT '资源打开方式',
    create_time    TIMESTAMP             DEFAULT CURRENT_TIMESTAMP,
    update_time    TIMESTAMP             DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_pid (pid),
    INDEX idx_dev_type (dev_type),
    INDEX idx_status (status),
    INDEX idx_protocol_type (protocol_type)
) COMMENT ='资源树节点表';
