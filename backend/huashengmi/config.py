# coding=utf-8


BASE_URL = '/huashengmi/v1/'
oracle_config = {'ID': 'oa', 'pwd': 'oa', 'host': '139.196.152.15:1521/orcl1'}

jixiao_sum_title = ['基本工资', '补助', '加班', '奖励', '四险一金']

depart_short_name_dict = {
    # 营销部
    'YXB': {'ID': '', 'SHORT_NAME': 'YXB', 'NAME': '营销部'},
    # 抄收用电服务部
    'CSYDFWB': {'ID': '', 'SHORT_NAME': 'CSYDFWB', 'NAME': '抄收用电服务部'},
    # 安全运检部
    'AQYJB': {'ID': '', 'SHORT_NAME': 'AQYJB', 'NAME': '安全运检部'},
    # 电力调度中心
    'DLDDZX': {'ID': '', 'SHORT_NAME': 'DLDDZX', 'NAME': '电力调度中心'},
    # 发展建设部
    'FZJSB': {'ID': '', 'SHORT_NAME': 'FZJSB', 'NAME': '发展建设部'},
    # 档案室
    'DAS': {'ID': '', 'SHORT_NAME': 'DAS', 'NAME': '档案室'},
    # 输电工程分公司
    'SDGCFGS': {'ID': '', 'SHORT_NAME': 'SDGCFGS', 'NAME': '输电工程分公司'},
    # 物业分公司
    'WYFGS': {'ID': '', 'SHORT_NAME': 'WYFGS', 'NAME': '物业分公司'},
    # 设计分公司
    'SJFGS': {'ID': '', 'SHORT_NAME': 'SJFGS', 'NAME': '设计分公司'},
    # 输配电运维分公司
    'SPDYWFGS': {'ID': '', 'SHORT_NAME': 'SPDYWFGS', 'NAME': '输配电运维分公司'},
    # 仪征恒邦实业有限公司
    'YZHBSYYXGS': {'ID': '', 'SHORT_NAME': 'YZHBSYYXGS', 'NAME': '仪征恒邦实业有限公司'},
    # 生产单位
    'SCDW': {'ID': '', 'SHORT_NAME': 'SCDW', 'NAME': '生产单位'},
    # 管理部门
    'GLBM': {'ID': '', 'SHORT_NAME': 'GLBM', 'NAME': '管理部门'},
    # 事务部
    'SWB': {'ID': '', 'SHORT_NAME': 'SWB', 'NAME': '事务部'},
    # 财务部
    'CWB': {'ID': '', 'SHORT_NAME': 'CWB', 'NAME': '财务部'},
    # 市场部
    'SCB': {'ID': '', 'SHORT_NAME': 'SCB', 'NAME': '市场部'},
    # 工程部
    'GCB': {'ID': '', 'SHORT_NAME': 'GCB', 'NAME': '工程部'},
    # 综合服务分公司
    'ZHFWFGS': {'ID': '', 'SHORT_NAME': 'ZHFWFGS', 'NAME': '综合服务分公司'},
    # 器材分公司
    'QCFGS': {'ID': '', 'SHORT_NAME': 'QCFGS', 'NAME': '生产单位'},
    # 电力工程服务分公司
    'DLGCFWFGS': {'ID': '', 'SHORT_NAME': 'DLGCFWFGS', 'NAME': '电力工程服务分公司'},
    # 输配电工程分公司
    'SPDGCFGS': {'ID': '', 'SHORT_NAME': 'SPDGCFGS', 'NAME': '输配电工程分公司'},
    # 变电工程分公司
    'BDGCFGS': {'ID': '', 'SHORT_NAME': 'BDGCFGS', 'NAME': '变电工程分公司'},
    # 城南用电服务部
    'CNYDFWB': {'ID': '', 'SHORT_NAME': 'CNYDFWB', 'NAME': '城南用电服务部'},
    # 公司领导
    'GSLD': {'ID': '', 'SHORT_NAME': 'GSLD', 'NAME': '公司领导'}
}

# 各项绩效工资排布顺序
jixiao_name_list = ['基本工资', '年限工资', '技术工资', '绩效工资', '技能工资', '加班工资', '超时加班费1', '超时加班费2',
                    '节日加班费', '出勤', '补助', '岗位补贴', '电话费', '夜餐费', '施工补助1', '施工补助2', '公里补助',
                    '交通补助', '慰问补助', '装表采集工程补助', '目标管理奖', '带电作业费', '线路巡视维护', '线路巡视检修费',
                    '线路巡视设计费', '设备巡视检修费', '现场工作负责人安全员岗位补贴', '奖励', '福利', '考核奖', '设计考核奖',
                    '安全优质考核', '月度考核奖', '季度考评及季度专项奖', '季度专项奖', '基本养老保险', '基本医疗保险',
                    '失业保险', '住房公积金', '大病救助']
# excel配置
conf_of_excel = {
    'title': {
        "name": "年度收支汇总表",
        "children": None
    },

    'header': [
        {
            "name": "序号",
            "children": None,
        },
        {
            "name": "部门",
            "children": None
        },
        {
            "name": "姓名",
            "children": None
        },
        {
            "name": "基本工资",
            "children": ["基本工资", "年限工资", "技术工资", "绩效工资", "技能工资"]
        },
        {
            "name": "加班",
            "children": ["加班工资", "超时加班费1", "超时加班费2", "节日加班费"]
        },
        {
            "name": "补助",
            "children": ["出勤", "补助", "岗位补贴", "电话费",
                         "夜餐费", "施工补助1", "施工补助2", "公里补助",
                         "交通补助", "慰问补助", "装表采集工程补助", "目标管理费",
                         "带电作业费", "线路巡视维护", "线路巡视检修费", "线路巡视设计费",
                         "设备巡视检修费", "现场工作负责人安全员岗位补贴"]
        },
        {
            "name": "奖励",
            "children": ["奖励", "福利", "考核奖", "设计考核奖",
                         "安全优质考核", "月度考核奖", "季度考评及季度专项奖", "季度专项奖"]
        },
        {
            "name": "应发合计",
            "children": None
        },
        {
            "name": "四险一金",
            "children": ["扣养老", "扣医保", "扣失业", "扣公积金", "大病救助"]
        },
        {
            "name": "实发工资",
            "children": None
        },
    ]
}

jixiao_short_name_dict = {
    # 施工补助
    'SGBZ1': {'ID': '', 'SHORT_NAME': 'SGBZ1', 'PROGRAM_NAME': '施工补助1', 'category': 2},
    # 公里补助
    'GLBZ': {'ID': '', 'SHORT_NAME': 'GLBZ', 'PROGRAM_NAME': '公里补助', 'category': 2},
    # 岗位补贴
    'GWBT': {'ID': '', 'SHORT_NAME': 'GWBT', 'PROGRAM_NAME': '岗位补贴', 'category': 2},
    # 线路巡视维护
    'XLXSWH': {'ID': '', 'SHORT_NAME': 'XLXSWH', 'PROGRAM_NAME': '线路巡视维护', 'category': 2},
    # 线路巡视检修费
    'XLXSJXF': {'ID': '', 'SHORT_NAME': 'XLXSJXF', 'PROGRAM_NAME': '线路巡视检修费', 'category': 2},
    # 线路维护设计费
    'XLWHSJF': {'ID': '', 'SHORT_NAME': 'XLWHSJF', 'PROGRAM_NAME': '线路巡视设计费', 'category': 2},
    # 季度考评及季度专项奖
    'JDKPJJDZXJ': {'ID': '', 'SHORT_NAME': 'JDKPJJDZXJ', 'PROGRAM_NAME': '季度考评及季度专项奖', 'category': 4},
    # 慰问补助
    'WWBZ': {'ID': '', 'SHORT_NAME': 'WWBZ', 'PROGRAM_NAME': '慰问补助', 'category': 2},
    # 基本工资
    'JBGZ1': {'ID': '', 'SHORT_NAME': 'JBGZ1', 'PROGRAM_NAME': '基本工资', 'category': 1},
    # 绩效工资
    'JXGZ': {'ID': '', 'SHORT_NAME': 'JXGZ', 'PROGRAM_NAME': '绩效工资', 'category': 1},
    # 年限工资
    'NXGZ': {'ID': '', 'SHORT_NAME': 'NXGZ', 'PROGRAM_NAME': '年限工资', 'category': 1},
    # 技能工资
    'JNGZ': {'ID': '', 'SHORT_NAME': 'JNGZ', 'PROGRAM_NAME': '技能工资', 'category': 1},
    # 加班工资
    'JBGZ2': {'ID': '', 'SHORT_NAME': 'JBGZ2', 'PROGRAM_NAME': '加班工资', 'category': 3},
    # 月度考核奖
    'YDKHJ': {'ID': '', 'SHORT_NAME': 'YDKHJ', 'PROGRAM_NAME': '月度考核奖', 'category': 4},
    # 考核奖
    'KHJ': {'ID': '', 'SHORT_NAME': 'KHJ', 'PROGRAM_NAME': '考核奖', 'category': 4},
    # 补助
    'BZ': {'ID': '', 'SHORT_NAME': 'BZ', 'PROGRAM_NAME': '补助', 'category': 2},
    # 基本养老保险
    'JBYLBX1': {'ID': '', 'SHORT_NAME': 'JBYLBX1', 'PROGRAM_NAME': '基本养老保险', 'category': 5},
    # 基本医疗保险
    'JBYLBX2': {'ID': '', 'SHORT_NAME': 'JBYLBX2', 'PROGRAM_NAME': '基本医疗保险', 'category': 5},
    # 大病救助
    'DBJZ': {'ID': '', 'SHORT_NAME': 'DBJZ', 'PROGRAM_NAME': '大病救助', 'category': 5},
    # 失业保险
    'SYBX': {'ID': '', 'SHORT_NAME': 'SYBX', 'PROGRAM_NAME': '失业保险', 'category': 5},
    # 住房公积金
    'ZFGJJ': {'ID': '', 'SHORT_NAME': 'ZFGJJ', 'PROGRAM_NAME': '住房公积金', 'category': 5},
    # 福利
    'FL': {'ID': '', 'SHORT_NAME': 'FL', 'PROGRAM_NAME': '福利', 'category': 4},
    # 交通补助
    'JTBZ': {'ID': '', 'SHORT_NAME': 'JTBZ', 'PROGRAM_NAME': '交通补助', 'category': 2},
    # 设备巡视检修费
    'SBXSJXF': {'ID': '', 'SHORT_NAME': 'SBXSJXF', 'PROGRAM_NAME': '设备巡视检修费', 'category': 2},
    # 超时加班费
    'CSJBF1': {'ID': '', 'SHORT_NAME': 'CSJBF1', 'PROGRAM_NAME': '超时加班费1', 'category': 3},
    # 超时加班费
    'CSJBF2': {'ID': '', 'SHORT_NAME': 'CSJBF2', 'PROGRAM_NAME': '超时加班费2', 'category': 3},
    # 季度专项奖
    'JDZXJ': {'ID': '', 'SHORT_NAME': 'JDZXJ', 'PROGRAM_NAME': '季度专项奖', 'category': 4},
    # 施工补助
    'SGBZ2': {'ID': '', 'SHORT_NAME': 'SGBZ2', 'PROGRAM_NAME': '施工补助2', 'category': 2},
    # 奖励
    'JL': {'ID': '', 'SHORT_NAME': 'JL', 'PROGRAM_NAME': '奖励', 'category': 4},
    # 夜餐费
    'YCF': {'ID': '', 'SHORT_NAME': 'YCF', 'PROGRAM_NAME': '夜餐费', 'category': 2},
    # 带电作业费
    'DDZYF': {'ID': '', 'SHORT_NAME': 'DDZYF', 'PROGRAM_NAME': '带电作业费', 'category': 2},
    # 节日加班费
    'JRJBF': {'ID': '', 'SHORT_NAME': 'JRJBF', 'PROGRAM_NAME': '节日加班费', 'category': 3},
    # 安全优质考核
    'AQYZKH': {'ID': '', 'SHORT_NAME': 'AQYZKH', 'PROGRAM_NAME': '安全优质考核', 'category': 4},
    # 出勤
    'CQ': {'ID': '', 'SHORT_NAME': 'CQ', 'PROGRAM_NAME': '出勤', 'category': 2},
    # 电话费
    'DHF': {'ID': '', 'SHORT_NAME': 'DHF', 'PROGRAM_NAME': '电话费', 'category': 2},
    # 目标管理奖
    'MBGLJ': {'ID': '', 'SHORT_NAME': 'MBGLJ', 'PROGRAM_NAME': '目标管理奖', 'category': 2},
    # 现场工作负责人安全员岗位补贴
    'XCGZFZRAQYGWBT': {'ID': '', 'SHORT_NAME': 'XCGZFZRAQYGWBT', 'PROGRAM_NAME': '现场工作负责人安全员岗位补贴', 'category': 2},
    # 装表采集工程补助
    'ZBCJGCBZ': {'ID': '', 'SHORT_NAME': 'ZBCJGCBZ', 'PROGRAM_NAME': '装表采集工程补助', 'category': 2},
    # 技术工资
    'JSGZ': {'ID': '', 'SHORT_NAME': 'JSGZ', 'PROGRAM_NAME': '技术工资', 'category': 1},
    # 设计考核奖
    'SJKHJ': {'ID': '', 'SHORT_NAME': 'SJKHJ', 'PROGRAM_NAME': '设计考核奖', 'category': 4}
}


class StatusCode(object):
    '''
    状态码设置
    '''
    DEFAULT = 100

    LOGIN_SUCCESS = 100

    LOGIN_FAIL_USER_NOT_FOUND = 2001

    LOGIN_FAIL_PASSWORD_ERROR = 2002

    LOGIN_FAIL_PARAMETER_ERROR = 2002

    LOGOUT_SUCCESS = 100

    LOGOUT_FAIL = 2001

    RESOURCE_NOT_FOUND = 404
