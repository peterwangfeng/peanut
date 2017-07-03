# -*- coding: utf-8 -*-
import time
from service.oracle_service import OracleService


class DataDao(object):
    def __init__(self):
        pass

    @staticmethod
    def append_with_douhao(list):
        result = ""
        for a in list:
            result += "'" + str(a) + "',"
        return result[:-1]

    @staticmethod
    def query_jidu_salary(years=[str(time.localtime()[0])]):

        cursor = OracleService.get_cursor()
        year_str = ",".join(years)
        sql = """
            SELECT SUBSTR(MONTH,0,4) as YEAR,
            SUM(case when SUBSTR(MONTH,6,2) in ('01','02','03') then TO_Number(SALARY) else 0 end) AS season1,
            SUM(case when SUBSTR(MONTH,6,2) in ('04','05','06') then TO_Number(SALARY) else 0 end) AS season2,
            SUM(case when SUBSTR(MONTH,6,2) in ('07','08','09') then TO_Number(SALARY) else 0 end) AS season3,
            SUM(case when SUBSTR(MONTH,6,2) in ('10','11','12') then TO_Number(SALARY) else 0 end) AS season4
            FROM "PERFORMANCE_USER_SALARY_copy"
            WHERE SUBSTR(MONTH,0,4) in (%s)
            GROUP BY SUBSTR(MONTH,0,4)
        """ % year_str
        result = OracleService.query_list_result(cursor, sql)

        return result

    @staticmethod
    def query_depart_and_month(months=[], depart=[], year=str(time.localtime()[0])):
        cursor = OracleService.get_cursor()
        months_str = ",".join(months)
        depart_str = DataDao.append_with_douhao(depart)
        sql = """
            SELECT SUBSTR(MONTH,6,2) as MONTH,
            b.OFFICE_ID,
            SUM(SALARY) AS total
            FROM "PERFORMANCE_USER_SALARY_copy" a
            LEFT JOIN "PERFORMANCE_USER" b
            ON a.USER_ID = b.ID
            WHERE SUBSTR(MONTH,0,4) = %s
            AND SUBSTR(MONTH,6,2) in (%s)
        """ % (year, months_str)
        if len(depart) > 0:
            sql += """
                AND OFFICE_ID in (%s)
                GROUP BY SUBSTR(MONTH,6,2), OFFICE_ID
            """ % depart_str
        else:
            sql += """
                GROUP BY SUBSTR(MONTH,6,2), OFFICE_ID
            """
        result = OracleService.query_yangshi1_result(cursor, sql)

        return result

    @staticmethod
    def query_depart_and_categary(year=str(time.localtime()[0]), month='05'):
        cursor = OracleService.get_cursor()
        sql = """
            SELECT b.OFFICE_ID,
            PROGRAMID,
            SUM(SALARY) AS total
            FROM "PERFORMANCE_RESULT_SALARY_copy" a
            LEFT JOIN "PERFORMANCE_USER" b
            ON a.USER_ID = b.ID
            WHERE SUBSTR(MONTH,0,4) = %s
	        AND SUBSTR(MONTH,6,2) = %s
            GROUP BY PROGRAMID, OFFICE_ID
        """ % (year, month)
        result = OracleService.query_yangshi1_result(cursor, sql)
        return result

    @staticmethod
    def query_year_salary(year=str(time.localtime()[0])):
        cursor = OracleService.get_cursor()
        sql = """
            SELECT PROGRAM_NAME, USER_ID, b.NAME, c.NAME, SUM(SALARY) AS amount
            FROM "PERFORMANCE_RESULT_SALARY_copy" a
            LEFT JOIN "PERFORMANCE_USER" b
            ON a.USER_ID = b.ID
	        LEFT JOIN "SYS_OFFICE" c
	        ON b.OFFICE_ID = c.ID
	        LEFT JOIN "PERFORMANCE_PROGRAM" d
            ON PROGRAMID = d.ID
            WHERE SUBSTR(MONTH,0,4) = %s
            GROUP BY SUBSTR(MONTH,0,4), USER_ID, b.NAME, PROGRAM_NAME, c.NAME
        """ % year
        cursor.execute(sql)
        sql_result = cursor.fetchall()

        return sql_result

dao = DataDao()
#print dao.query_depart_and_month(['05','06'],['5ee2506d6b584e70a4267ba0e893aec3','b5d1800d8a77463cac04522c8dac692a'])
#print dao.query_depart_and_categary('2017', '05')
#print dao.query_year_salary(2017)

