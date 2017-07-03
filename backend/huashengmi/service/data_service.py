from dao.data_dao import DataDao
import time


class DataService(object):

    def __init__(self):
        self.dao = DataDao()

    def jidu_salary_service(self, years):
        return self.dao.query_jidu_salary(years)

    def depart_and_month_service(self, months=[], depart=[], year=str(time.localtime()[0])):
        return self.dao.query_depart_and_month(months, depart, year)

    def depart_and_categary_service(self, year=str(time.localtime()[0]), month='01'):
        return self.dao.query_depart_and_categary(year, month)

    def year_salary(self, year=str(time.localtime()[0])):
        return self.dao.query_year_salary(year)