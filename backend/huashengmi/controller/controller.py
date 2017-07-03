# coding=utf-8
from flask_restful import Resource,marshal_with
from service.data_service import DataService
from flask import request
from utils.flask_util import response, CJsonEncoder
import json
import time


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
        result = self.service.jidu_salary_service(years)[0]
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
        month = args['month']
        year = str(time.localtime()[0])
        if 'year' in args.keys():
            year = args['year']
        result = self.service.depart_and_categary_service(year, month)
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
        if 'year' in args.keys():
            year = args['year']
        result = self.service.year_salary(year)
        return {'data': json.loads(json.dumps(result, cls=CJsonEncoder))}