# encoding: utf-8
from flask_restful import Resource, marshal_with
from service.user_service import UserService
from flask import request
from utils.flask_util import response
from utils.flask_util import auth
from config import StatusCode, BASE_URL


class UserLogin(Resource):
    def __init__(self):
        self.service = UserService()

    # 登陆请求
    @marshal_with(response)
    def post(self):
        '''
        返回登陆状态码，登陆成功则返回用户信息
        :return: dict
        '''
        data = request.json
        try:
            user_name = data['login_name']
            password = data['password']
        except Exception as e:
            print e
            return {'code': StatusCode.LOGIN_FAIL_PARAMETER_ERROR}

        if user_name and password:
            result = self.service.login(user_name, password)
            if result and result[0] is True:
                if 'type' not in data.keys() \
                        or int(data['type']) == StatusCode.WEB_LOGIN:
                    return {'code': StatusCode.LOGIN_SUCCESS, 'data': {'user_name': result[1]['NAME'],
                                                                       'token': result[1]['TOKEN'],
                                                                       'user_id': result[1]['ID']}}
                elif 'type' in data.keys() \
                        and int(data['type']) == StatusCode.ONE_AUTH_LOGIN:
                    return {'code': StatusCode.LOGIN_SUCCESS,
                            'data': {
                                'user_name': result[1]['NAME'],
                                'token': result[1]['TOKEN'],
                                'user_id': result[1]['ID'],
                                'redirect_url': '/head/first'
                            }}
                else:
                    return {'code': StatusCode.LOGIN_FAIL_PARAMETER_ERROR}
            else:
                return {'code': result[1]}
        else:
            return {'code': StatusCode.LOGIN_FAIL_PASSWORD_ERROR}


class UserLogout(Resource):
    def __init__(self):
        self.service = UserService()

    @marshal_with(response)
    @auth.login_required
    def post(self):
        '''处理注销请求，删除数据库存储的token'''
        data = request.json
        user_id = data['user_id']
        # user_id=request.form.get('user_id')
        result = self.service.logout(user_id)
        if result:
            return {'code': StatusCode.LOGOUT_SUCCESS}
        else:
            return {'code': StatusCode.LOGOUT_FAIL}
