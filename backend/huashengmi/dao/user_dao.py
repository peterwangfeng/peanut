# -*- coding: utf-8 -*-

from utils.flask_util import Factory,Verfy,Token
from utils.oracle_util import OracleUtil

class UserDao(object):
    def __init__(self, db_type='Oracle'):
        self.type = db_type
        self.factory = Factory(self.type, self.__class__.__name__)
        self.path = 'dao.user_dao'

    def login(self,login_name,password):
        dao = self.factory.get_dao(self.path)
        return dao.login(login_name,password)

    def logout(self,ID):
        dao=self.factory.get_dao(self.path)
        return dao.logout(ID)

class OracleUserDao(object):

    def __init__(self):
        self.con=OracleUtil.get_connection()
        self.cursor=self.con.cursor()

    def login(self,login_name,plain_password):
        result = []
        sql="select ID,LOGIN_NAME,NAME,PASSWORD from OA.SYS_USER WHERE LOGIN_NAME = '%s'"%login_name
        self.cursor.execute(sql)
        result = OracleUtil.query_list_result(self.cursor,sql)
        try:
            if not result:
                #未查到则返回false
                return False,2001
            for user in result:
                encrypted_password=user.pop('PASSWORD')
                ID = user['ID']
                if Verfy.validatePassword(plain_password.encode('utf-8'),encrypted_password):
                    user_token=self.setToken(ID)
                    user['TOKEN']=user_token
                    return True,user
            return False,2002
        except Exception as e:
            return False,2002

    def setToken(self,ID):
        token=Token()
        user_token=token.generate_token(ID)
        sql = "UPDATE OA.SYS_USER SET TOKEN = '%s' WHERE ID = '%s'" % (user_token,ID)
        self.cursor.execute(sql)
        self.con.commit()
        return user_token

    def logout(self,ID):
        sql= "UPDATE OA.SYS_USER SET TOKEN = NULL WHERE ID = '%s'" % ID
        self.cursor.execute(sql)
        self.con.commit()
        return True







