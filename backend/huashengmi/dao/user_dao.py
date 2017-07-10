# -*- coding: utf-8 -*-

from utils.flask_util import Factory, Verify, Token
from utils.oracle_util import OracleUtil
from config import StatusCode


# class UserDao(object):
#     def __init__(self, db_type='Oracle'):
#         self.type = db_type
#         self.factory = Factory(self.type, self.__class__.__name__)
#         self.path = 'dao.user_dao'
#
#     def login(self,login_name,password):
#         dao = self.factory.get_dao(self.path)
#         return dao.login(login_name,password)
#
#     def logout(self,ID):
#         dao=self.factory.get_dao(self.path)
#         return dao.logout(ID)

class UserDao(object):
    def __init__(self):
        self.con = OracleUtil.get_connection()
        self.cursor = self.con.cursor()

    def login(self, login_name, plain_password):
        result = []
        sql = "select ID,LOGIN_NAME,NAME,PASSWORD from OA.SYS_USER WHERE LOGIN_NAME = '%s'" % login_name
        self.cursor.execute(sql)
        result = OracleUtil.query_list_result(self.cursor, sql)
        try:
            if not result:
                # 未查到则返回false
                return False, StatusCode.LOGIN_FAIL_USER_NOT_FOUND
            for user in result:
                encrypted_password = user.pop('PASSWORD')
                ID = user['ID']
                if Verify.validate_password(plain_password.encode('utf-8'), encrypted_password):
                    user_token = self.setToken(ID)
                    user['TOKEN'] = user_token
                    return True, user
            return False, StatusCode.LOGIN_FAIL_PASSWORD_ERROR
        except Exception as e:
            return False, StatusCode.LOGIN_FAIL_PASSWORD_ERROR

    def setToken(self, user_id):
        token = Token()
        user_token = token.generate_token(user_id)
        sql = "UPDATE OA.SYS_USER SET TOKEN = '%s' WHERE ID = '%s'" % (user_token, user_id)
        self.cursor.execute(sql)
        self.con.commit()
        return user_token

    def logout(self, user_id):
        sql = "UPDATE OA.SYS_USER SET TOKEN = NULL WHERE ID = '%s'" % user_id
        self.cursor.execute(sql)
        self.con.commit()
        return True

    def one_auth_login(self,login_name,enc_password):
        sql = "select ID,LOGIN_NAME,NAME,PASSWORD from OA.SYS_USER WHERE LOGIN_NAME = '%s'" % login_name
        self.cursor.execute(sql)
        result = OracleUtil.query_list_result(self.cursor, sql)
        try:
            if not result:
                # 未查到则返回false
                return False, StatusCode.LOGIN_FAIL_USER_NOT_FOUND
            for user in result:
                db_password = user['PASSWORD']
                user_id = user['ID']
                if Verify.one_auth_verify(enc_password,db_password):
                    user_token = self.setToken(user_id)
                    user['TOKEN'] = user_token
                    return True, user
            return False, StatusCode.LOGIN_FAIL_PASSWORD_ERROR
        except Exception as e:
            return False, StatusCode.LOGIN_FAIL_PASSWORD_ERROR


if __name__ == '__main__':
    login_name=u'swb'
    enc_password=u'cd04cb32656cf74938e22bd9722fead3af6d532a'
    b=UserDao().one_auth_login(login_name,enc_password)