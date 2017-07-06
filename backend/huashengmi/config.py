# coding=utf-8


BASE_URL = '/huashengmi/v1/'
oracle_config = {'ID': 'oa', 'pwd': 'oa', 'host': '139.196.152.15:1521/orcl1'}

jixiao_sum_title = ['基本工资','补助', '加班', '奖励', '四险一金']

depart_short_name_dict = {
    # 营销部
    'YXB': {'ID': '5ee2506d6b584e70a4267ba0e893aec3', 'short_name': 'YXB', 'name': '营销部'},
    # 抄收用电服务部
    'CSYDFWB': {'ID': '1c3df6a9f2654e65a0876ced537e9add', 'short_name': 'CSYDFWB', 'name': '抄收用电服务部'},
    # 安全运检部
    'AQYJB': {'ID': 'b5d1800d8a77463cac04522c8dac692a', 'short_name': 'AQYJB', 'name': '安全运检部'},
    # 电力调度中心
    'DLDDZX': {'ID': '5917ff2cc86f4033aa8ee9a46c7dff80', 'short_name': 'DLDDZX', 'name': '电力调度中心'},
    # 发展建设部
    'FZJSB': {'ID': '81cfe6feb056455ea75fbfe3309c4075', 'short_name': 'FZJSB', 'name': '发展建设部'},
    # 档案室
    'DAS': {'ID': 'b798b037ff5a4c9da2aea546f143d9fc', 'short_name': 'DAS', 'name': '档案室'},
    # 输电工程分公司
    'SDGCFGS': {'ID': '1a0bb9f3916f4aa596b082c7fc2e1c83', 'short_name': 'SDGCFGS', 'name': '输电工程分公司'},
    # 物业分公司
    'WYFGS': {'ID': 'e272604e0df940fba8a6a5421089df3f', 'short_name': 'WYFGS', 'name': '物业分公司'},
    # 设计分公司
    'SJFGS': {'ID': 'd943566e6def4da485ef2fadc3788ac4', 'short_name': 'SJFGS', 'name': '设计分公司'},
    # 输配电运维分公司
    'SPDYWFGS': {'ID': '38f51528044f459c891013c30e6600c0', 'short_name': 'SPDYWFGS', 'name': '输配电运维分公司'},
    # 仪征恒邦实业有限公司
    'YZHBSYYXGS': {'ID': 'b144c48ac3bb4fb881be54e99331e85f', 'short_name': 'YZHBSYYXGS', 'name': '仪征恒邦实业有限公司'},
    # 生产单位
    'SCDW': {'ID': 'cf4c2c36b55441a7b7cacd80582b82e5', 'short_name': 'SCDW', 'name': '生产单位'},
    # 管理部门
    'GLBM': {'ID': '89db7c73ef494ad782dee55c9645f07b', 'short_name': 'GLBM', 'name': '管理部门'},
    # 事务部
    'SWB': {'ID': '766fa018013d41ec96995de1010c5f7c', 'short_name': 'SWB', 'name': '事务部'},
    # 财务部
    'CWB': {'ID': 'c05e6ef18704442e80ac134eb0635235', 'short_name': 'CWB', 'name': '财务部'},
    # 市场部
    'SCB': {'ID': '1b5527cdae1d4c419e9170ef61c5e9bf', 'short_name': 'SCB', 'name': '市场部'},
    # 工程部
    'GCB': {'ID': 'ebb83e7cddb24b11912f7448b6467f48', 'short_name': 'GCB', 'name': '工程部'},
    # 综合服务分公司
    'ZHFWFGS': {'ID': '188110fa13d14f5287d42bbaeb5c1d70', 'short_name': 'ZHFWFGS', 'name': '综合服务分公司'},
    # 器材分公司
    'QCFGS': {'ID': 'b82410d91f6742a1b4250cc906073baf', 'short_name': 'QCFGS', 'name': '生产单位'},
    # 电力工程服务分公司
    'DLGCFWFGS': {'ID': '709002de2d4342c79c32ee916fe3ba63', 'short_name': 'DLGCFWFGS', 'name': '电力工程服务分公司'},
    # 输配电工程分公司
    'SPDGCFGS': {'ID': '0207d05722e8431d91c1e21bdfb9da54', 'short_name': 'SPDGCFGS', 'name': '输配电工程分公司'},
    # 变电工程分公司
    'BDGCFGS': {'ID': '5d080393140a48368409159d03de5eff', 'short_name': 'BDGCFGS', 'name': '变电工程分公司'},
    # 城南用电服务部
    'CNYDFWB': {'ID': '6bb1c7d4a1bf4e78b3104e92a2437ed7', 'short_name': 'CNYDFWB', 'name': '城南用电服务部'},
    # 公司领导
    'GSLD': {'ID': 'f7873c0c3e6d4209becc49f5f1137e7e', 'short_name': 'GSLD', 'name': '公司领导'}
}

# 各项绩效工资排布顺序
jixiao_name_list = ['基本工资', '年限工资', '技术工资', '绩效工资', '技能工资', '加班工资', '超时加班费1', '超时加班费2',
                    '节日加班费', '出勤', '补助', '岗位补贴', '电话费', '夜餐费', '施工补助1', '施工补助2', '公里补助',
                    '交通补助', '慰问补助', '装表采集工程补助', '目标管理费', '带电作业费', '线路巡视维护', '线路巡视检修费',
                    '线路巡视设计费', '设备巡视检修费', '现场工作负责人安全员岗位补贴', '奖励', '福利', '考核奖', '设计考核奖',
                    '安全优质考核', '月度考核奖', '季度考评及季度专项奖', '季度专项奖', '基本养老保险', '基本医疗保险',
                    '失业保险', '住房公积金', '大病救助']

jixiao_short_name_dict = {
    # 施工补助
    'SGBZ1': {'ID': 'c96271255cb94427a883a28fbe70b434', 'short_name': 'SGBZ1', 'name': '施工补助1', 'category': 2},
    # 公里补助
    'GLBZ': {'ID': '39001dc32760480f80ea9239381990b4', 'short_name': 'GLBZ', 'name': '公里补助', 'category': 2},
    # 岗位补贴
    'GWBT': {'ID': 'ca02ab49fe43476d92678a41e51b6e1f', 'short_name': 'GWBT', 'name': '岗位补贴', 'category': 2},
    # 线路巡视维护
    'LXXSWH': {'ID': '19598fe99b9342a39e47acfa25098988', 'short_name': 'LXXSWH', 'name': '线路巡视维护', 'category': 2},
    # 线路巡视检修费
    'LXXSJXF': {'ID': 'b7b18e3f889c4defb7c194184613861c', 'short_name': 'LXXSJXF', 'name': '线路巡视检修费', 'category': 2},
    # 线路巡视设计费
    'LXXSSJF': {'ID': 'a6eed2f9152e4237a05a39736ae93477', 'short_name': 'LXXSSJF', 'name': '线路巡视设计费', 'category': 2},
    # 季度考评及季度专项奖
    'JDKPJJDZXJ': {'ID': 'd8cfec44e70448a38c82a67abfd7d51b', 'short_name': 'JDKPJJDZXJ', 'name': '季度考评及季度专项奖', 'category': 4},
    # 慰问补助
    'WWBZ': {'ID': '758457f6611c46a899de18259a5306b3', 'short_name': 'WWBZ', 'name': '慰问补助', 'category': 2},
    # 基本工资
    'JBGZ1': {'ID': '4bb28e2ac35440d8a2f23ff8c7bc8b23', 'short_name': 'JBGZ1', 'name': '基本工资', 'category': 1},
    # 绩效工资
    'JXGZ': {'ID': '2c8b53e2999542f3b287e032eec0381b', 'short_name': 'JXGZ', 'name': '绩效工资', 'category': 1},
    # 年限工资
    'NXGZ': {'ID': 'eb4ef46b9cf1485e8b579f820be64e4f', 'short_name': 'NXGZ', 'name': '年限工资', 'category': 1},
    # 技能工资
    'JNGZ': {'ID': '941c11258e5246aaa90ce88e86d21971', 'short_name': 'JNGZ', 'name': '技能工资', 'category': 1},
    # 加班工资
    'JBGZ2': {'ID': '1b97e305164241a79b280048cdecbcaa', 'short_name': 'JBGZ2', 'name': '加班工资', 'category': 3},
    # 月度考核奖
    'YDKHJ': {'ID': '72fd61561d9a43ad876b1ea33b684879', 'short_name': 'YDKHJ', 'name': '月度考核奖', 'category': 4},
    # 考核奖
    'KHJ': {'ID': '3afde600232a426b911304af45a755d2', 'short_name': 'KHJ', 'name': '考核奖', 'category': 4},
    # 补助
    'BZ': {'ID': 'de3d42a85c3443a0ae5cc0029103cf81', 'short_name': 'BZ', 'name': '补助', 'category': 2},
    # 基本养老保险
    'JBYLBX1': {'ID': '4047ab3e894243f4a345341b2eacab4c', 'short_name': 'JBYLBX1', 'name': '基本养老保险', 'category': 5},
    # 基本医疗保险
    'JBYLBX2': {'ID': '89d732c0eed64a6eb0b4bc903d16cf0c', 'short_name': 'JBYLBX2', 'name': '基本医疗保险', 'category': 5},
    # 大病救助
    'DBJZ': {'ID': 'a20e3222c5dc47da81e86c251cc080b1', 'short_name': 'DBJZ', 'name': '大病救助', 'category': 5},
    # 失业保险
    'SYBX': {'ID': '8611efa354414b3ca1c7122279b71d58', 'short_name': 'SYBX', 'name': '失业保险', 'category': 5},
    # 住房公积金
    'ZFGJJ': {'ID': '16166307bd334efc810c755bce9bacc0', 'short_name': 'ZFGJJ', 'name': '住房公积金', 'category': 5},
    # 福利
    'FL': {'ID': '30204c16263f41668eeae10957b99c82', 'short_name': 'FL', 'name': '福利', 'category': 4},
    # 交通补助
    'JTBZ': {'ID': 'dadb70dbde824670b23a1417b465caa7', 'short_name': 'JTBZ', 'name': '交通补助', 'category': 2},
    # 设备巡视检修费
    'SBXSJXF': {'ID': 'fdfd0ae36f184cd18cf1db82eaa4e1e9', 'short_name': 'SBXSJXF', 'name': '设备巡视检修费', 'category': 2},
    # 超时加班费
    'CSJBF1': {'ID': '40812a9c36c847aca69f3b94f23d1af8', 'short_name': 'CSJBF1', 'name': '超时加班费1', 'category': 3},
    # 超时加班费
    'CSJBF2': {'ID': 'd7d79fe7c45e4127add643aecdf1aae4', 'short_name': 'CSJBF2', 'name': '超时加班费2', 'category': 3},
    # 季度专项奖
    'JDZXJ': {'ID': 'c676863d98cf4512a5d03d1f8893094a', 'short_name': 'JDZXJ', 'name': '季度专项奖', 'category': 4},
    # 施工补助
    'SGBZ2': {'ID': '414c05bae6344bd5accb1a20d7c616ab', 'short_name': 'SGBZ2', 'name': '施工补助2', 'category': 2},
    # 奖励
    'JL': {'ID': '8160d68bef514c88aae18393cfec838d', 'short_name': 'JL', 'name': '奖励', 'category': 4},
    # 夜餐费
    'YCF': {'ID': '5760e4cc3acc455597ace45d063a235e', 'short_name': 'YCF', 'name': '夜餐费', 'category': 2},
    # 带电作业费
    'DDZYF': {'ID': '34d37e92f82445a6820976dee5bfca87', 'short_name': 'DDZYF', 'name': '带电作业费', 'category': 2},
    # 节日加班费
    'JRJBF': {'ID': '6ab60b43c1d44dcc80e1aed38181b7c9', 'short_name': 'JRJBF', 'name': '节日加班费', 'category': 3},
    # 安全优质考核
    'AQYZKH': {'ID': '028acf684e9740d19f0e6e1f790369c8', 'short_name': 'AQYZKH', 'name': '安全优质考核', 'category': 4},
    # 出勤
    'CQ': {'ID': '2db8a405fb4f47f38e015d08564d2e39', 'short_name': 'CQ', 'name': '出勤', 'category': 2},
    # 电话费
    'DHF': {'ID': '209a07e109be45718d261eaf8d4d40b7', 'short_name': 'DHF', 'name': '电话费', 'category': 2},
    # 目标管理费
    'MBGLJ': {'ID': '3725b6de29de4b8095d86dec016f1e49', 'short_name': 'MBGLJ', 'name': '目标管理费', 'category': 2},
    # 现场工作负责人安全员岗位补贴
    'XCGZFZRAQYGWBT': {'ID': '368743cc1aed483da54639c00d095709', 'short_name': 'XCGZFZRAQYGWBT', 'name': '现场工作负责人安全员岗位补贴', 'category': 2},
    # 装表采集工程补助
    'ZBCJGCBZ': {'ID': '47fbe05afa8e42d3bcc19a70160424c1', 'short_name': 'ZBCJGCBZ', 'name': '装表采集工程补助', 'category': 2},
    # 技术工资
    'JSGZ': {'ID': '3024dcc3df96496086a17dfbcebb0a1d', 'short_name': 'JSGZ', 'name': '技术工资', 'category': 1},
    # 设计考核奖
    'SJKHJ': {'ID': 'eeb640bb6cda4627b8eed8df99a95422', 'short_name': 'SJKHJ', 'name': '设计考核奖', 'category': 4}
}