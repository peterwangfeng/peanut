# coding=utf-8
from flask import g
from flask_restful import fields
import time, base64, hmac
from flask_httpauth import HTTPTokenAuth
import json
import datetime
import decimal
from datetime import date
from service.oracle_service import OracleService

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, decimal.Decimal):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


response = {
    'code': fields.Integer(default=100),
    'msg': fields.String(default='请求成功'),
    'data': fields.Raw(default={})
}