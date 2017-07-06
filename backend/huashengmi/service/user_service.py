# encoding: utf-8
from dao.user_dao import UserDao
class UserService(object):
    def __init__(self):
        self.dao = UserDao()

    def login(self,login_name,password):
        return self.dao.login(login_name,password)

    def logout(self,ID):
        return self.dao.logout(ID)

