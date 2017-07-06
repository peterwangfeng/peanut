# coding=utf-8
from flask_restful import Resource,marshal_with
from service.data_service import DataService
from flask import request, make_response
from utils.flask_util import response, CJsonEncoder
import json
import time
import tablib


class Download(Resource):

    def __init__(self):
        self.service = DataService()

    #导出excel
    def get(self):
        """
        导出年度工资excel表格
        :param year: string 不支持_hb类指标
        :return: excel文件
        """
        args = request.args.to_dict()
        year = str(time.localtime()[0])
        if 'year' in args.keys():
            year = args['year']
        result = self.service.year_salary_for_download(year)
        headers = tuple(result[0])
        rows = tuple(result[1])
        data = tablib.Dataset(*rows, headers=headers)

        resp = make_response(data.xlsx)
        para = "attachment; filename=%s.xlsx" % year
        resp.headers["Content-Disposition"] = para
        return resp



class JiduSalary(Resource):

    def __init__(self):
        self.service = DataService()

    #数据接口请求
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

    #数据接口请求
    @marshal_with(response)
    def get(self):
        """
        返回各部门各月份工资情况
        :param months，depart，year: string 不支持_hb类指标
        :return: {} 对象
        """
        args = request.args.to_dict()
        months = []
        if 'months' in args.keys():
            months = args['months'].split(',')
        depart = []
        if 'depart' in args.keys():
            depart = args['depart'].split(',')
        year = str(time.localtime()[0])
        if 'year' in args.keys():
            year = args['year']
        result = self.service.depart_and_month_service(months, depart, year)
        return {'data': json.loads(json.dumps(result, cls=CJsonEncoder))}


class DepartAndCategory(Resource):

    def __init__(self):
        self.service = DataService()

    #数据接口请求
    @marshal_with(response)
    def get(self):
        """
        返回单月各部门各项工资情况
        :param year，month: string 不支持_hb类指标
        :return: {} 对象
        """
        args = request.args.to_dict()
        month = ''
        if 'month' in args.keys():
            month = args['month']
        year = str(time.localtime()[0])
        if 'year' in args.keys():
            year = args['year']
        depart = args['depart']
        result = self.service.depart_and_categary_service(year, month, depart)
        return {'data': json.loads(json.dumps(result, cls=CJsonEncoder))}


class YearSalary(Resource):

    def __init__(self):
        self.service = DataService()

    #数据接口请求
    @marshal_with(response)
    def get(self):
        """
        返回员工年度工资汇总
        :param year: string 不支持_hb类指标
        :return: {} 对象
        """
        args = request.args.to_dict()
        year = str(time.localtime()[0])
        cur_page = 1
        if 'cur_page' in args.keys():
            cur_page = int(args['cur_page'])
        page_size = 10
        if 'page_size' in args.keys():
            page_size = int(args['page_size'])
        if 'year' in args.keys():
            year = args['year']
        result = self.service.year_salary(year, cur_page, page_size)
        return {'data': json.loads(json.dumps(result, cls=CJsonEncoder))}