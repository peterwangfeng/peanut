# coding=utf-8
from flask import g
from flask_restful import fields
import json
import datetime
import decimal
from datetime import date
import time, hmac, base64, hashlib
from flask_httpauth import HTTPTokenAuth
from oracle_util import OracleUtil


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


class Factory(object):
    def __init__(self, db_type, module_name):
        self.type = db_type
        self.module_name = module_name

    def get_dao(self, path):
        module = __import__(path, {}, {}, ['a'])
        obj = getattr(module, self.type + self.module_name)()
        return obj


class Token(object):
    def generate_token(self, key, expire=3600):
        ts_str = str(time.time() + expire)
        ts_byte = ts_str.encode('utf-8')
        sha1_tshexstr = hmac.new(key.encode('utf-8'), ts_byte).hexdigest()
        token = ts_str + ':' + sha1_tshexstr
        b64_token = base64.urlsafe_b64encode(token.encode('utf-8'))
        return b64_token.decode('utf-8')

    def verify_token(self, key, token):
        token_str = base64.urlsafe_b64decode(token)
        token_list = token_str.split(':')
        if (len(token_list)) != 2:
            return False
        ts_str = token_list[0]
        if float(ts_str) < time.time():
            return False
        known_sha1_tsstr = token_list[1]
        sha1 = hmac.new(key.encode('utf-8'), ts_str.encode('utf-8'))
        calc_sha_tsstr = sha1.hexdigest()
        if calc_sha_tsstr != known_sha1_tsstr:
            return False
        return True

        # 验证token


class Verify(object):
    @staticmethod
    def validate_password(plain_password, encrypted_password):
        salt = encrypted_password[:16].decode('hex')
        # 获取盐
        sha_enc = hashlib.sha1()
        sha_enc.update(salt + plain_password)
        encrypted2 = sha_enc.digest()
        # 加盐计算sha1
        # print encrypted2.encode('hex')
        for i in range(1, 1024):
            # 计算1023次
            sha1_num_enc = hashlib.sha1()
            sha1_num_enc.update(encrypted2)
            encrypted2 = sha1_num_enc.digest()
        if encrypted_password[16:] == encrypted2.encode('hex'):
            return True
        else:
            return False


auth = HTTPTokenAuth(scheme='Token')


@auth.verify_token
def verify_token(token):
    cursor = OracleUtil.get_cursor()
    sql = "SELECT ID from OA.SYS_USER WHERE TOKEN = '%s'" % token
    result = OracleUtil.query_list_result(cursor, sql)
    if result:
        user_id = result[0]['ID']
    else:
        return False
    if user_id is not None and Token().verify_token(user_id, str(token)):
        g.user_id = user_id
        return True
    else:
        return False
