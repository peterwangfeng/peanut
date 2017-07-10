# coding=utf-8
from flask_restful import Resource, marshal_with
from service.data_service import DataService
from service.excel_service import XlsCreater
from flask import request, make_response
from utils.flask_util import response, CJsonEncoder, auth
from utils.oracle_util import OracleUtil
import json
import time
import tablib
from config import conf_of_excel


class Download(Resource):
    def __init__(self):
        self.service = DataService()

    # 导出excel
    def get(self):
        """
        导出年度工资excel表格
        :param year: string 不支持_hb类指标
        :return: excel文件
        """
        args = request.args.to_dict()
        year = str(time.localtime()[0])
        if args.has_key('year'):
            year = args['year']
        month = ''
        if args.has_key('month'):
            month = args['month']
        result = self.service.year_salary_for_download(year, month)
        headers = conf_of_excel
        rows = tuple(result[1])
        xls_creator = XlsCreater()
        data = xls_creator.insert_data(headers, rows)
        resp = make_response(data)
        if len(month) == 0:
            para = "attachment; filename=%s.xls" % year
        else:
            para = "attachment; filename=%s%s.xls" % (year, month)
        resp.headers["Content-Disposition"] = para
        return resp


class JiduSalary(Resource):
    def __init__(self):
        self.service = DataService()

    # 数据接口请求
    @auth.login_required
    @marshal_with(response)
    def get(self):
        """
        返回各季度总工资情况
        :param years: string 不支持_hb类指标
        :return: dict : {}
        """
        args = request.args.to_dict()
        years = args['years'].split(',')
        result = self.service.jidu_salary_service(years)
        return {'data': json.loads(json.dumps(result, cls=CJsonEncoder))}


class DepartAndMonth(Resource):
    def __init__(self):
        self.service = DataService()

    # 数据接口请求
    @auth.login_required
    @marshal_with(response)
    def get(self):
        """
        返回各部门各月份工资情况
        :param months，depart，year: string 不支持_hb类指标
        :return: {} 对象
        """
        args = request.args.to_dict()
        months = []
        if args.has_key('months'):
            months = args['months'].split(',')
        depart = []
        if args.has_key('depart'):
            depart = args['depart'].split(',')
        year = OracleUtil.getYear()
        if args.has_key('year'):
            year = args['year']
        result = self.service.depart_and_month_service(months, depart, year)
        return {'data': json.loads(json.dumps(result, cls=CJsonEncoder))}


class DepartAndCategory(Resource):
    def __init__(self):
        self.service = DataService()

    # 数据接口请求
    @auth.login_required
    @marshal_with(response)
    def get(self):
        """
        返回单月各部门各项工资情况
        :param year，month: string 不支持_hb类指标
        :return: {} 对象
        """
        args = request.args.to_dict()
        month = ''
        if args.has_key('month'):
            month = args['month']
        year = OracleUtil.getYear()
        if args.has_key('year'):
            year = args['year']
        depart = args['depart']
        result = self.service.depart_and_categary_service(year, month, depart)
        return {'data': json.loads(json.dumps(result, cls=CJsonEncoder))}


class YearSalary(Resource):
    def __init__(self):
        self.service = DataService()

    # 数据接口请求
    @auth.login_required
    @marshal_with(response)
    def get(self):
        """
        返回员工年度工资汇总
        :param year: string 不支持_hb类指标
        :return: {} 对象
        """
        args = request.args.to_dict()
        year = OracleUtil.getYear()
        cur_page = 1
        if args.has_key('cur_page'):
            cur_page = int(args['cur_page'])
        page_size = 10
        if args.has_key('page_size'):
            page_size = int(args['page_size'])
        if args.has_key('year'):
            year = args['year']
        month = ''
        if args.has_key('month'):
            month = args['month']
        result = self.service.year_salary(year, month, cur_page, page_size)
        return {'data': json.loads(json.dumps(result, cls=CJsonEncoder))}


class GetDepart(Resource):
    def __init__(self):
        self.service = DataService()

    # 数据接口请求
    @auth.login_required
    @marshal_with(response)
    def get(self):
        """
        返回部门名称表
        :return: [] 对象
        """
        result = self.service.get_depart()
        return {'data': json.loads(json.dumps(result, cls=CJsonEncoder))}
