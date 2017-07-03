# coding=utf-8


BASE_URL = '/huashengmi/v1/'
oracle_config = {'ID': 'oa', 'pwd' : 'oa', 'host' : '139.196.152.15:1521/orcl1'}



# 部门ID和简称对照dict
depart_dict = {
    #营销部
    '5ee2506d6b584e70a4267ba0e893aec3' : 'YXB',
    #抄收用电服务部
    '1c3df6a9f2654e65a0876ced537e9add' : 'CSYDFWB',
    #安全运检部
    'b5d1800d8a77463cac04522c8dac692a' : 'AQYJB',
    #电力调度中心
    '5917ff2cc86f4033aa8ee9a46c7dff80' : 'DLDDZX',
    #发展建设部
    '81cfe6feb056455ea75fbfe3309c4075' : 'FZJSB',
    #档案室
    'b798b037ff5a4c9da2aea546f143d9fc' : 'DAS',
    #输电工程分公司
    '1a0bb9f3916f4aa596b082c7fc2e1c83' : 'SDGCFGS',
    #物业分公司
    'e272604e0df940fba8a6a5421089df3f' : 'WYFGS',
    #设计分公司
    'd943566e6def4da485ef2fadc3788ac4' : 'SJFGS',
    #输配电运维分公司
    '38f51528044f459c891013c30e6600c0' : 'SPDYWFGS',
    #仪征恒邦实业有限公司
    'b144c48ac3bb4fb881be54e99331e85f' : 'YZHBSYYXGS',
    #生产单位
    'cf4c2c36b55441a7b7cacd80582b82e5' : 'SCDW',
    #管理部门
    '89db7c73ef494ad782dee55c9645f07b' : 'GLBM',
    #事务部
    '766fa018013d41ec96995de1010c5f7c' : 'SWB',
    #财务部
    'c05e6ef18704442e80ac134eb0635235' : 'CWB',
    #市场部
    '1b5527cdae1d4c419e9170ef61c5e9bf' : 'SCB',
    #工程部
    'ebb83e7cddb24b11912f7448b6467f48' : 'GCB',
    #综合服务分公司
    '188110fa13d14f5287d42bbaeb5c1d70' : 'ZHFWFGS',
    #器材分公司
    'b82410d91f6742a1b4250cc906073baf' : 'QCFGS',
    #电力工程服务分公司
    '709002de2d4342c79c32ee916fe3ba63' : 'DLGCFWFGS',
    #输配电工程分公司
    '0207d05722e8431d91c1e21bdfb9da54' : 'SPDGCFGS',
    #变电工程分公司
    '5d080393140a48368409159d03de5eff' : 'BDGCFGS',
    #城南用电服务部
    '6bb1c7d4a1bf4e78b3104e92a2437ed7' : 'CNYDFWB',
    #公司领导
    'f7873c0c3e6d4209becc49f5f1137e7e' : 'GSLD'
}