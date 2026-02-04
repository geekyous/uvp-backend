-- ============================================
-- 测试数据脚本
-- 用于模拟 device_resource、camera、tool_box_talk、toolboxtalk_camera_rela 表数据
-- ============================================

-- 清空相关表数据
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE toolboxtalk_camera_rela;
TRUNCATE TABLE camera;
TRUNCATE TABLE tool_box_talk;
TRUNCATE TABLE device_resource;
SET FOREIGN_KEY_CHECKS = 1;

-- ============================================
-- 1. device_resource 设备资源树形数据
-- ============================================

-- 1.1 根节点
INSERT INTO device_resource (id, text, dev_code, dev_type, pid, path, type, is_group, has_children, status, children_count, `order`, is_available)
VALUES
('root_001', '国网江苏省电力公司', 'ROOT_JIANGSU', '00', NULL, '/root_001', 0, 1, 1, 1, 3, 0, 1);

-- 1.2 区域节点
INSERT INTO device_resource (id, text, dev_code, dev_type, pid, path, type, is_group, has_children, status, children_count, `order`, is_available)
VALUES
('area_001', '南京供电公司', 'AREA_NANJING', '01', 'root_001', '/root_001/area_001', 1, 1, 1, 1, 2, 1, 1),
('area_002', '苏州供电公司', 'AREA_SUZHOU', '01', 'root_001', '/root_001/area_002', 1, 1, 1, 1, 1, 2, 1);

-- 1.3 项目节点
INSERT INTO device_resource (id, text, dev_code, dev_type, pid, path, type, is_group, has_children, status, children_count, `order`, is_available)
VALUES
('proj_001', '220kV变电站工程项目', 'PROJ_NJ_2024001', '02', 'area_001', '/root_001/area_001/proj_001', 2, 1, 1, 1, 5, 1, 1),
('proj_002', '500kV线路改造工程', 'PROJ_SZ_2024001', '02', 'area_002', '/root_001/area_002/proj_002', 2, 1, 1, 1, 3, 1, 1);

-- 1.4 布控球设备（摄像头类型，dev_type='11'表示监控摄像机）
INSERT INTO device_resource (id, text, dev_short_name, dev_code, dev_type, pid, path, type, is_group, has_children, status, `order`, is_available, lng, lat, dvr_code, gis_peer_code, audio)
VALUES
-- 南京项目的布控球
('camera_device_001', '1号施工现场东侧布控球', '1号东侧', 'CAM_NJ_2024001_01', '11', 'proj_001', '/root_001/area_001/proj_001/camera_device_001', 11, 0, 0, 1, 1, 1, 118.796877, 32.060255, 'DVR_NJ_001', 'GIS_NJ_001', 1),
('camera_device_002', '1号施工现场西侧布控球', '1号西侧', 'CAM_NJ_2024001_02', '11', 'proj_001', '/root_001/area_001/proj_001/camera_device_002', 11, 0, 0, 1, 2, 1, 118.795877, 32.060255, 'DVR_NJ_002', 'GIS_NJ_002', 1),
('camera_device_003', '2号施工现场南侧布控球', '2号南侧', 'CAM_NJ_2024001_03', '11', 'proj_001', '/root_001/area_001/proj_001/camera_device_003', 11, 0, 0, 1, 3, 1, 118.796877, 32.059255, 'DVR_NJ_003', 'GIS_NJ_003', 0),
('camera_device_004', '2号施工现场北侧布控球', '2号北侧', 'CAM_NJ_2024001_04', '11', 'proj_001', '/root_001/area_001/proj_001/camera_device_004', 11, 0, 0, 0, 4, 1, 118.796877, 32.061255, 'DVR_NJ_004', 'GIS_NJ_004', 1),
('camera_device_005', '材料堆场监控布控球', '材料堆场', 'CAM_NJ_2024001_05', '11', 'proj_001', '/root_001/area_001/proj_001/camera_device_005', 11, 0, 0, 1, 5, 1, 118.797877, 32.060255, 'DVR_NJ_005', 'GIS_NJ_005', 0),

-- 苏州项目的布控球
('camera_device_006', '线路A段施工监控球', 'A段监控', 'CAM_SZ_2024001_01', '11', 'proj_002', '/root_001/area_002/proj_002/camera_device_006', 11, 0, 0, 1, 1, 1, 120.585316, 31.298886, 'DVR_SZ_001', 'GIS_SZ_001', 1),
('camera_device_007', '线路B段施工监控球', 'B段监控', 'CAM_SZ_2024001_02', '11', 'proj_002', '/root_001/area_002/proj_002/camera_device_007', 11, 0, 0, 1, 2, 1, 120.586316, 31.298886, 'DVR_SZ_002', 'GIS_SZ_002', 1),
('camera_device_008', '线路C段施工监控球', 'C段监控', 'CAM_SZ_2024001_03', '11', 'proj_002', '/root_001/area_002/proj_002/camera_device_008', 11, 0, 0, 1, 3, 1, 120.587316, 31.298886, 'DVR_SZ_003', 'GIS_SZ_003', 1);

-- ============================================
-- 2. camera 布控球表数据
-- ============================================

INSERT INTO camera (id, camera_name, camera_no, province_code, creater_id, create_time, updater_id, update_time, delete_flag)
VALUES
-- 南京项目的布控球（与 device_resource 对应）
('CAM_001', '1号施工现场东侧布控球', 'CAM_NJ_2024001_01', '32', 'admin', NOW(), 'admin', NOW(), 0),
('CAM_002', '1号施工现场西侧布控球', 'CAM_NJ_2024001_02', '32', 'admin', NOW(), 'admin', NOW(), 0),
('CAM_003', '2号施工现场南侧布控球', 'CAM_NJ_2024001_03', '32', 'admin', NOW(), 'admin', NOW(), 0),
('CAM_004', '2号施工现场北侧布控球', 'CAM_NJ_2024001_04', '32', 'admin', NOW(), 'admin', NOW(), 0),
('CAM_005', '材料堆场监控布控球', 'CAM_NJ_2024001_05', '32', 'admin', NOW(), 'admin', NOW(), 0),

-- 苏州项目的布控球（与 device_resource 对应）
('CAM_006', '线路A段施工监控球', 'CAM_SZ_2024001_01', '32', 'admin', NOW(), 'admin', NOW(), 0),
('CAM_007', '线路B段施工监控球', 'CAM_SZ_2024001_02', '32', 'admin', NOW(), 'admin', NOW(), 0),
('CAM_008', '线路C段施工监控球', 'CAM_SZ_2024001_03', '32', 'admin', NOW(), 'admin', NOW(), 0);

-- ============================================
-- 3. tool_box_talk 站班会业务数据
-- ============================================

INSERT INTO tool_box_talk (
    id,
    off_online_flag,
    prj_name,
    prj_code,
    ticket_id,
    ticket_no,
    re_assessment_risk_level,
    current_constr_headcount,
    construction_headcount,
    work_start_time,
    current_constr_date,
    current_construction_status,
    work_overnight_flag,
    tool_box_talk_address,
    tool_box_talk_longitude,
    tool_box_talk_latitude,
    bidding_section_code,
    bidding_section_name,
    single_project_code,
    single_project_name,
    single_project_type,
    constr_unified_social_credit_id,
    construction_unit_name,
    supervision_social_credit_code,
    supervision_unit_name,
    voltage_level,
    huv_flag,
    build_unit_code,
    province_code,
    creater_id,
    create_time,
    updater_id,
    update_time,
    delete_flag
)
VALUES
-- 站班会1：南京220kV变电站工程 - 高风险作业
(
    'TBT_001',
    0,
    '220kV龙潭变电站新建工程',
    'PROJ_NJ_2024001',
    'TICKET_001',
    'GD-NJ-2024-001',
    5,  -- 风险等级5（最高）
    25,
    25,
    '2024-02-04 08:00:00',
    '2024-02-04',
    '01',  -- 作业中
    0,
    '南京市栖霞区龙潭街道变电站施工现场',
    '118.796877',
    '32.060255',
    'BD_NJ_001',
    '变电工程第一标段',
    'SP_NJ_001',
    '220kV龙潭变电站',
    1,  -- 变电工程
    '91320000MA1234567A',
    '江苏省电力建设第一工程公司',
    '91320000MA7654321B',
    '江苏诚信工程监理有限公司',
    '220kV',
    0,  -- 常规工程
    'BUILD_32001',
    '32',
    'admin',
    NOW(),
    'admin',
    NOW(),
    0
),

-- 站班会2：南京220kV变电站工程 - 中风险作业
(
    'TBT_002',
    0,
    '220kV龙潭变电站新建工程',
    'PROJ_NJ_2024001',
    'TICKET_002',
    'GD-NJ-2024-002',
    3,  -- 风险等级3（中）
    18,
    18,
    '2024-02-04 09:00:00',
    '2024-02-04',
    '01',  -- 作业中
    0,
    '南京市栖霞区龙潭街道变电站材料区',
    '118.797877',
    '32.060255',
    'BD_NJ_001',
    '变电工程第一标段',
    'SP_NJ_002',
    '220kV配电装置安装',
    1,  -- 变电工程
    '91320000MA1234567A',
    '江苏省电力建设第一工程公司',
    '91320000MA7654321B',
    '江苏诚信工程监理有限公司',
    '220kV',
    0,  -- 常规工程
    'BUILD_32001',
    '32',
    'admin',
    NOW(),
    'admin',
    NOW(),
    0
),

-- 站班会3：苏州500kV线路改造工程 - 特高压工程
(
    'TBT_003',
    0,
    '500kV吴江-昆山输电线路改造工程',
    'PROJ_SZ_2024001',
    'TICKET_003',
    'GD-SZ-2024-001',
    4,  -- 风险等级4
    32,
    30,
    '2024-02-04 07:30:00',
    '2024-02-04',
    '01',  -- 作业中
    0,
    '苏州市吴江区盛泽镇500kV线路走廊',
    '120.585316',
    '31.298886',
    'BD_SZ_001',
    '线路工程第一标段',
    'SP_SZ_001',
    '500kV吴江-昆山A段线路',
    2,  -- 线路工程
    '91320500MA8765432C',
    '江苏苏电输变电工程有限公司',
    '91320500MA5678901D',
    '苏州电力工程监理公司',
    '500kV',
    1,  -- 特高压工程
    'BUILD_32005',
    '32',
    'admin',
    NOW(),
    'admin',
    NOW(),
    0
),

-- 站班会4：苏州500kV线路工程 - 已完工
(
    'TBT_004',
    0,
    '500kV吴江-昆山输电线路改造工程',
    'PROJ_SZ_2024001',
    'TICKET_004',
    'GD-SZ-2024-002',
    2,  -- 风险等级2（低）
    15,
    15,
    '2024-02-03 08:00:00',
    '2024-02-03',
    '03',  -- 作业完工
    0,
    '苏州市吴江区盛泽镇500kV线路B段',
    '120.586316',
    '31.298886',
    'BD_SZ_001',
    '线路工程第一标段',
    'SP_SZ_002',
    '500kV吴江-昆山B段线路',
    2,  -- 线路工程
    '91320500MA8765432C',
    '江苏苏电输变电工程有限公司',
    '91320500MA5678901D',
    '苏州电力工程监理公司',
    '500kV',
    1,  -- 特高压工程
    'BUILD_32005',
    '32',
    'admin',
    NOW(),
    'admin',
    NOW(),
    0
);

-- ============================================
-- 4. toolboxtalk_camera_rela 站班会与布控球关联数据
-- ============================================

INSERT INTO toolboxtalk_camera_rela (
    id,
    camera_id,
    tool_box_talk_id,
    province_code,
    creater_id,
    create_time,
    updater_id,
    update_time,
    delete_flag,
    sort_no
)
VALUES
-- 站班会1（TBT_001）关联3个布控球
('RELA_001', 'CAM_001', 'TBT_001', '32', 'admin', NOW(), 'admin', NOW(), 0, 1),
('RELA_002', 'CAM_002', 'TBT_001', '32', 'admin', NOW(), 'admin', NOW(), 0, 2),
('RELA_003', 'CAM_003', 'TBT_001', '32', 'admin', NOW(), 'admin', NOW(), 0, 3),

-- 站班会2（TBT_002）关联2个布控球
('RELA_004', 'CAM_004', 'TBT_002', '32', 'admin', NOW(), 'admin', NOW(), 0, 1),
('RELA_005', 'CAM_005', 'TBT_002', '32', 'admin', NOW(), 'admin', NOW(), 0, 2),

-- 站班会3（TBT_003）关联3个布控球
('RELA_006', 'CAM_006', 'TBT_003', '32', 'admin', NOW(), 'admin', NOW(), 0, 1),
('RELA_007', 'CAM_007', 'TBT_003', '32', 'admin', NOW(), 'admin', NOW(), 0, 2),
('RELA_008', 'CAM_008', 'TBT_003', '32', 'admin', NOW(), 'admin', NOW(), 0, 3),

-- 站班会4（TBT_004）关联2个布控球
('RELA_009', 'CAM_007', 'TBT_004', '32', 'admin', NOW(), 'admin', NOW(), 0, 1),
('RELA_010', 'CAM_008', 'TBT_004', '32', 'admin', NOW(), 'admin', NOW(), 0, 2);

-- ============================================
-- 数据验证查询
-- ============================================

-- 查看设备资源树结构
SELECT
    id,
    text,
    dev_code,
    dev_type,
    pid,
    CONCAT(REPEAT('  ', LENGTH(path) - LENGTH(REPLACE(path, '/', '')) - 1), text) AS tree_view
FROM device_resource
ORDER BY path;

-- 查看布控球列表及其在 device_resource 中的对应关系
SELECT
    c.id AS camera_id,
    c.camera_name,
    c.camera_no,
    dr.text AS device_name,
    dr.dev_code,
    dr.status AS device_status
FROM camera c
LEFT JOIN device_resource dr ON c.camera_no = dr.dev_code
ORDER BY c.id;

-- 查看站班会及其关联的布控球数量
SELECT
    t.id,
    t.prj_name,
    t.ticket_no,
    t.re_assessment_risk_level AS risk_level,
    t.current_constr_date,
    t.current_construction_status AS status,
    COUNT(r.id) AS camera_count
FROM tool_box_talk t
LEFT JOIN toolboxtalk_camera_rela r ON t.id = r.tool_box_talk_id AND r.delete_flag = 0
WHERE t.delete_flag = 0
GROUP BY t.id
ORDER BY t.create_time DESC;

-- 查看站班会与布控球的详细关联关系
SELECT
    t.id AS talk_id,
    t.ticket_no,
    t.prj_name,
    c.camera_name,
    c.camera_no,
    r.sort_no,
    dr.status AS camera_status
FROM tool_box_talk t
INNER JOIN toolboxtalk_camera_rela r ON t.id = r.tool_box_talk_id AND r.delete_flag = 0
INNER JOIN camera c ON r.camera_id = c.id AND c.delete_flag = 0
LEFT JOIN device_resource dr ON c.camera_no = dr.dev_code
WHERE t.delete_flag = 0
ORDER BY t.id, r.sort_no;

-- ============================================
-- 完成
-- ============================================
