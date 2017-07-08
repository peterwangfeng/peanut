# coding=utf-8


BASE_URL = '/huashengmi/v1/'
oracle_config = {'ID': 'oa', 'pwd': 'oa', 'host': '139.196.152.15:1521/orcl1'}

jixiao_sum_title = ['基本工资', '补助', '加班', '奖励', '四险一金']


# 各项绩效工资排布顺序
jixiao_name_list = ['JBGZ1', 'NXGZ', 'JSGZ', 'JXGZ', 'JNGZ', 'JBGZ2', 'CSJBF1', 'CSJBF2',
                    'JRJBF', 'CQ', 'BZ', 'GWBT', 'DHF', 'YCF', 'SGBZ1', 'SGBZ2', 'GLBZ',
                    'JTBZ', 'WWBZ', 'ZBCJGCBZ', 'MBGLJ', 'DDZYF', 'XLXSWH', 'XLXSJXF',
                    'XLWHSJF', 'SBXSJXF', 'XCGZFZRAQYGWBT', 'JL', 'FL', 'KHJ', 'SJKHJ',
                    'AQYZKH', 'YDKHJ', 'JDKPJJDZXJ', 'JDZXJ', 'JBYLBX1', 'JBYLBX2',
                    'SYBX', 'ZFGJJ', 'DBJZ']
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

    WEB_LOGIN = 1

    ONE_AUTH_LOGIN = 2