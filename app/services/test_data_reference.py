"""
测试数据参考配置

根据实际生产数据来生成更贴近真实的测试数据
"""
import random

# ============================================
# 站班会参考数据 (jj_class_meetting)
# ============================================

CLASS_MEETING_REFERENCES = {
    "project_type_codes": {
        "变电工程": "1",
        "线路工程": "2",
        "电缆工程": "3"
    },
    "construction_status_codes": {
        "撤回": "01",
        "驳回": "02",
        "提交审核中": "03",
        "待执行": "04",
        "执行中": "05",
        "已结束": "06",
        "作废": "07",
        "删除": "08"
    },
    "risk_levels": {
        2: "低风险",
        3: "中风险",
        4: "高风险",
        5: "特高风险"
    },
    "audit_hierarchy": {
        "班组": "01",
        "施工": "02",
        "监理": "03"
    },
    "issue_type": {
        "审核签发": "01",
        "自动签发": "02"
    },
    "priority": {
        "高": "01",
        "中": "02"
    },
    "sample_projects": [
        {
            "prj_name": "埇桥～萧砀Ⅱ回500千伏线路工程",
            "prj_code": "S100009",
            "single_project_code": "S100009",
            "single_project_name": "埇桥～萧砀500千伏线路工程",
            "single_project_type": "线路工程",
            "location_province": "34",
            "location_municipality_name": "宿州市",
            "location_area_name": "萧砀县",
            "voltage_level": "500KV",
            "huv_flag": 1,
            "build_unit_code": "AC05001",
            "build_unit_name": "宿州萧砀500kV输变电工程",
            "builder": "安徽电力工程监理有限公司",
            "supervisor_organization": "AC05001"
        },
        {
            "prj_name": "刘尧-屏山π入濉河变电站110kV线路工程",
            "prj_code": "1612Q021001",
            "single_project_code": "1612Q021001",
            "single_project_name": "刘尧-屏山π入濉河变电站110kV线路工程",
            "single_project_type": "变电工程",
            "location_province": "37",
            "location_municipality_name": "宿州市",
            "location_area_name": "刘尧县",
            "voltage_level": "110KV",
            "huv_flag": 0,
            "build_unit_code": "12Z0",
            "build_unit_name": "宿州刘尧-屏山110kV线路工程",
            "builder": "宿州供电公司",
            "supervisor_organization": "12Z0"
        },
        {
            "prj_name": "SZ-B3-1712G420001Y0101",
            "prj_code": "SZ-B3-1712G420001Y0101",
            "single_project_code": "SZ-B3-1712G420001Y0101",
            "single_project_name": "SZ-B3-1712G420001Y0101",
            "single_project_type": "变电工程",
            "location_province": "32",
            "location_municipality_name": "苏州市",
            "location_area_name": "吴江区",
            "voltage_level": "220V",  # 注意：这是220V不是220KV
            "huv_flag": 0,
            "build_unit_code": "AC01101",
            "build_unit_name": "苏州吴江220kV输变电工程",
            "builder": "SZ-B3",
            "supervisor_organization": "AC01101"
        }
    ],
    "sample_bidding_sections": [
        {
            "code": "1171528657",
            "name": "埇桥区支河镇031县道"
        },
        {
            "code": "33.883657",
            "name": "刘尧-屏山π入濉河变电站110kV线路工程"
        }
    ]
}

# ============================================
# 作业票参考数据 (jj_ticket)
# ============================================

TICKET_REFERENCES = {
    "ticket_types": {
        "A": "A票",
        "B": "B票"
    },
    "team_samples": [
        {
            "team_id": "22qocw9jonpxd4qy7wx075",
            "team_name": "线路组塔架线-张林4班"
        },
        {
            "team_id": "2912e346a69a438ca91606d2637",
            "team_name": "刘尧-屏山π入濉河变电站110kV线路工程"
        }
    ]
}

# ============================================
# 设备资源参考数据 (JSON 格式)
# ============================================

DEVICE_RESOURCE_REFERENCES = {
    "dev_types": {
        "布控球": "10",
        "网络固定摄像机": "03",
        "其他": "00"
    },
    "dev_status": {
        "在线": "1",
        "离线": "0",
        "不可用": "2"
    },
    "is_available": {
        "有效": "1",
        "无效": "0"
    },
    "sample_camera": {
        "text": "基建施工现场-基建作业-1977号球机",
        "dev_short_name": "基建作业-1977",
        "p_code": "123590000002060001",
        "dev_code": "123590000003101924",
        "dev_type": "10",  # 布控球
        "url": None,
        "open_type": 0,
        "pid": "43b1504d5cd34f9a8de76340b3092ec4",
        "path": "基建施工现场/基建施工现场/基建施工现场-基建作业-1977号球机",
        "type": 0,
        "is_group": 0,
        "is_available": 1,
        "order": None,
        "has_children": False,
        "status": 0,  # 离线
        "is_outernet": 1,
        "s_decode_tag": "100",  # H264
        "lng": None,
        "lat": None,
        "children_count": 0,
        "online_count": 0,
        "gis_peer_code": None,
        "sys_info_code": "120091818601000000",
        "dvr_code": None,
        "is_check": False,
        "self_data": False,
        "socre": "0",
        "font_type_code": "10",
        "coordinate": None,
        "use_status": None,
        "check": False,
        "tower_id": None,
        "plat_code": "120090000000000000",
        "resource_attr": None,
        "resource_type": None,
        "protocol_type": "5",
        "audio": 0
    }
}

# ============================================
# 数据生成规则
# ============================================

DATA_GENERATION_RULES = {
    # ID生成规则
    "id_prefixes": {
        "tool_box_talk": "TBT",
        "ticket": "TICKET",
        "camera": "CAM",
        "device_resource": "DEV",
        "relation": "RELA"
    },

    # 编号生成规则
    "ticket_no_format": "{project_code}-{index:03d}",
    "camera_code_format": "{project_code}_{index:02d}",
    "device_code_format": "123590000003{index:06d}",
    "dev_code_format2": "12359000000{random}",

    # 日期时间生成
    "use_current_date": True,  # 使用当前日期
    "planned_days_offset": {  # 计划日期偏移天数
        "start": -1,  # 计划开始时间比当前早1天
        "end": 7     # 计划结束时间比当前晚7天
    },
    "working_hours": {
        "default": 8,  # 默认工作时长8小时
        "short": 6,
        "long": 10
    },

    # 风险等级分配
    "risk_level_assignment": {
        "default": 3,  # 默认中风险
        "based_on_workers": {
            "<10": 2,      # 少于10人：低风险
            "10-20": 3,     # 10-20人：中风险
            "20-30": 4,     # 20-30人：高风险
            ">30": 5       # 超过30人：特高风险
        }
    },

    # 施工人数分配
    "worker_count_ranges": [14, 15, 18, 20, 25, 30],

    # 布控球数量
    "cameras_per_project": {
        "min": 3,
        "max": 8
    },

    # 站班会与布控球关联
    "cameras_per_talk": {
        "min": 2,
        "max": 5
    },

    # 站班会数量
    "talks_per_project": {
        "min": 1,
        "max": 2
    }
}

# ============================================
# 工程名称模板
# ============================================

PROJECT_NAME_TEMPLATES = {
    "变电站": "{bidding_section_name}{voltage}变电站",
    "线路工程": "{bidding_section_name}{voltage}线路工程",
    "电缆工程": "{bidding_section_name}{voltage}电缆工程"
}

# ============================================
# 工作班组名称模板
# ============================================

TEAM_NAME_TEMPLATES = [
    "线路组塔架线{index}班",
    "变电站{index}班",
    "电缆敷设{index}班",
    "变电安装{index}班",
    "调试{index}班"
]

# ============================================
# 常用位置数据（用于生成经纬度）
# 根据建设管理单位名称匹配坐标
# ============================================

LOCATION_REFERENCES = {
    "安徽省": {
        "province_code": "34",
        "municipalities": {
            "宿州市": {
                "code": "3404",
                "areas": {
                    "萧砀县": {
                        "lng": "116.9345",
                        "lat": "34.399877"
                    },
                    "刘尧县": {
                        "lng": "115.974778",
                        "lat": "34.054367"
                    }
                }
            }
        }
    },
    "江苏省": {
        "province_code": "32",
        "municipalities": {
            "南京市": {
                "code": "3201",
                "areas": {
                    "栖霞区": {
                        "lng": "118.796877",
                        "lat": "32.060255"
                    },
                    "浦口区": {
                        "lng": "118.678877",
                        "lat": "32.092877"
                    }
                }
            },
            "苏州市": {
                "code": "3205",
                "areas": {
                    "吴江区": {
                        "lng": "120.585316",
                        "lat": "31.298886"
                    },
                    "相城区": {
                        "lng": "120.623877",
                        "lat": "31.317877"
                    }
                }
            }
        }
    }
}

# 根据建设管理单位名称映射坐标
BUILD_UNIT_LOCATION_MAP = {
    # 安徽省
    "宿州萧砀500kV输变电工程": ("116.9345", "34.399877"),  # 萧砀县
    "宿州刘尧-屏山110kV线路工程": ("115.974778", "34.054367"),  # 刘尧县
    "合肥供电公司": ("117.22", "31.82"),  # 合肥市
    "马鞍山供电公司": ("117.28", "31.73"),  # 马鞍山
    "芜湖供电公司": ("118.38", "31.35"),  # 芜湖
    "安庆供电公司": ("117.05", "30.53"),  # 安庆
    "淮南供电公司": ("116.98", "32.65"),  # 淮南
    "宣城供电公司": ("118.75", "30.95"),  # 宣城
    "阜阳供电公司": ("115.82", "32.64"),  # 阜阳
    "铜陵供电公司": ("117.79", "31.12"),  # 铜陵
    "蚌埠供电公司": ("117.39", "32.93"),  # 蚌埠
    "滁州供电公司": ("118.30", "32.31"),  # 滁州
    "六安供电公司": ("116.50", "31.75"),  # 六安
    "淮北供电公司": ("116.96", "33.53"),  # 淮北
    "宿州供电公司": ("116.97", "33.68"),  # 宿州
    "池州供电公司": ("117.49", "30.57"),  # 池州
    "黄山供电公司": ("118.19", "29.72"),  # 黄山
    "亳州供电公司": ("115.78", "33.86"),  # 亳州
    # 江苏省
    "苏州吴江220kV输变电工程": ("120.585316", "31.298886"),  # 吴江区
    "南京栖霞变电站": ("118.796877", "32.060255"),  # 栖霞区
    "南京浦口变电站": ("118.678877", "32.092877"),  # 浦口区
    "苏州相城变电站": ("120.623877", "31.317877"),  # 相城区
}

# 合肥地区单位列表（用于判断是否使用合肥坐标）
HEFEI_BUILD_UNITS = [
    "马鞍山供电公司", "芜湖供电公司", "安庆供电公司", "淮南供电公司", "宣城供电公司",
    "阜阳供电公司", "铜陵供电公司", "蚌埠供电公司", "滁州供电公司", "六安供电公司",
    "淮北供电公司", "宿州供电公司", "池州供电公司", "黄山供电公司", "亳州供电公司",
    "建设分公司"  # 建设分公司也是合肥地区的
]

# ============================================
# 辅助函数
# ============================================

def get_location_coords(province_code: str, municipal_name: str, area_name: str, build_unit_name: str = "") -> tuple:
    """根据省市县或建设管理单位名称获取经纬度

    优先通过 build_unit_name 匹配，如果找不到则按省市县查找
    对于合肥地区单位，使用合肥中心坐标
    """
    # 1. 优先通过建设管理单位名称匹配
    if build_unit_name and build_unit_name in BUILD_UNIT_LOCATION_MAP:
        return BUILD_UNIT_LOCATION_MAP[build_unit_name]

    # 2. 检查是否是合肥地区单位（使用合肥中心坐标）
    if build_unit_name and build_unit_name in HEFEI_BUILD_UNITS:
        # 合肥市中心坐标（约）
        # 在合肥中心附近随机偏移（约 0.05 度，约 5km 范围内）
        hefei_base_lng = 117.22
        hefei_base_lat = 31.82
        lng_offset = random.uniform(-0.05, 0.05)
        lat_offset = random.uniform(-0.05, 0.05)
        return (str(hefei_base_lng + lng_offset), str(hefei_base_lat + lat_offset))

    # 3. 按省市县查找（回退逻辑）
    try:
        province = LOCATION_REFERENCES.get(province_code, {})
        municipality = province.get("municipalities", {}).get(municipal_name, {})
        area = municipality.get("areas", {}).get(area_name, {})
        return area.get("lng"), area.get("lat")
    except:
        return None, None


def format_ticket_no(project_code: str, index: int) -> str:
    """格式化作业票编号"""
    return DATA_GENERATION_RULES["ticket_no_format"].format(
        project_code=project_code,
        index=index
    )


def generate_team_name(index: int, project_type: str) -> str:
    """生成班组名称"""
    template_index = index % len(TEAM_NAME_TEMPLATES)
    template = TEAM_NAME_TEMPLATES[template_index]

    type_names = {
        "1": "变电站",
        "2": "线路",
        "3": "电缆"
    }

    type_name_cn = type_names.get(project_type, "")
    if "变电站" in template:
        template = template.replace("变电站", "")
        template = f"{type_name_cn}{index}"
    elif "线路" in template and "线路组" in template:
        pass  # 保持原模板
    elif "电缆" in template and "电缆敷设" in template:
        template = template.replace("电缆敷设", "")
        template = f"{type_name_cn}{index}"
    else:
        template = template.replace("线路工程", "").replace("变电站", "").replace("电缆工程", "")
        template = f"{type_name_cn}{index}"

    return template.format(index=index)


def assign_risk_level(worker_count: int, huv_flag: int = 0) -> int:
    """根据施工人数分配风险等级"""
    rules = DATA_GENERATION_RULES["risk_level_assignment"]["based_on_workers"]

    for threshold, level in sorted(rules.items(), key=lambda x: x[0], reverse=True):
        if isinstance(threshold, str):
            # 解析范围字符串
            if threshold.startswith("<"):
                # "<10" → worker_count < 10
                limit = int(threshold[1:])
                if worker_count < limit:
                    return level
            elif threshold.startswith(">"):
                # ">30" → worker_count > 30
                limit = int(threshold[1:])
                if worker_count > limit:
                    return level
            elif "-" in threshold:
                # "10-20" → 10 <= worker_count <= 20
                min_val, max_val = threshold.split("-")
                if int(min_val) <= worker_count <= int(max_val):
                    return level
        elif worker_count <= threshold:
            return level

    return DATA_GENERATION_RULES["risk_level_assignment"]["default"]
