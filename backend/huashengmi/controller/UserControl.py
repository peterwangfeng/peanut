# encoding: utf-8
from flask_restful import Resource,marshal_with
from service.user_service import UserService
from flask import request
from utils.flask_util import response
from utils.flask_util import auth

class UserLogin(Resource):
    def __init__(self):
        self.service=UserService()

    @marshal_with(response)
    def post(self):
        '''
        处理登陆请求，返回token和用户信息
        :return:
        '''
        data = request.json
        user_name=data['login_name']
        password=data['password']

        if user_name and password:
            result = self.service.login(user_name,password)
            if result[0] == True:
                return {'code': 100, 'msg': 'login is ok', 'data': {'user_name': result[1]['NAME'],
                                                       'token': result[1]['TOKEN'], 'user_id': result[1]['ID']}}
            if result[0] == False:
                return {'code': result[1], 'msg': "login false!"}
        else:
            return {'code': 2002, 'msg': "login false!"}

class UserLogout(Resource):
    def __init__(self):
        self.service=UserService()
    @marshal_with(response)
    @auth.login_required
    def post(self):
        '''处理注销请求，删除数据库存储的token'''
        data = request.json
        user_id = data['user_id']
        # user_id=request.form.get('user_id')
        result=self.service.logout(user_id)
        if result:
            return {'code': 100, 'msg': "logout success!"}
        else:
            return {'code':2001,'msg':"logout fail!"}