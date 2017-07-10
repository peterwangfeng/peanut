# coding=utf-8
import sys

import logging
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from controller.controller import JiduSalary, DepartAndMonth, DepartAndCategory, YearSalary, Download, GetDepart
from config import BASE_URL
from controller.user_controller import UserLogin, UserLogout,OneAuthLogin

reload(sys)
sys.setdefaultencoding("utf-8")
logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='[%(asctime)s] [%(levelname)s] %(filename)s(%(funcName)s:%(lineno)d): %(message)s',
                    stream=sys.stdout)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)

# 接口
# 某年度4季度工资情况
api.add_resource(JiduSalary, BASE_URL + 'jidu_salary/')
# 各部门各月份工资情况
api.add_resource(DepartAndMonth, BASE_URL + 'depart_month/')
# 各部门各项绩效情况
api.add_resource(DepartAndCategory, BASE_URL + 'depart_category/')
# 员工全年工资绩效汇总
api.add_resource(YearSalary, BASE_URL + 'year_salary/')
# 导出为excel表格
api.add_resource(Download, BASE_URL + 'download/')
# 登陆
api.add_resource(UserLogin, BASE_URL + 'login/')
# 登出
api.add_resource(UserLogout, BASE_URL + 'logout/')
# 获取部门名称对应ID
api.add_resource(GetDepart, BASE_URL + 'get_depart/')
# 单点登陆接口
api.add_resource(OneAuthLogin, BASE_URL + 'one_auth_login/')

if __name__ == '__main__':
    logger.info('启动app')
    app.run(host="0.0.0.0", threaded=True, debug=True)
