# coding=utf-8
import sys

import logging
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from controller.controller import JiduSalary, DepartAndMonth, DepartAndCategory, YearSalary, Download
from config import BASE_URL
reload(sys)
sys.setdefaultencoding("utf-8")
logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='[%(asctime)s] [%(levelname)s] %(filename)s(%(funcName)s:%(lineno)d): %(message)s',
                    stream=sys.stdout)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)


#接口
api.add_resource(JiduSalary, BASE_URL + 'jidu_salary/')
api.add_resource(DepartAndMonth, BASE_URL + 'depart_month/')
api.add_resource(DepartAndCategory, BASE_URL + 'depart_categary/')
api.add_resource(YearSalary, BASE_URL + 'year_salary/')
api.add_resource(Download, BASE_URL + 'download/')

if __name__ == '__main__':
    logger.info('启动app')
    app.run(host="0.0.0.0", threaded=True, debug=True)
