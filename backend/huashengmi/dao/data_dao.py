#coding: utf-8
from utils.oracle_util import OracleUtil
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
os.environ['nls_lang'] = 'AMERICAN_AMERICA.ZHS16GBK'

class DataDao(object):
    def __init__(self):
        pass

    @staticmethod
    def query_jidu_salary(years=['2017']):

        cursor = OracleUtil.get_cursor()
        year_str = ",".join(years)
        sql = """
            SELECT SUBSTR(MONTH,0,4) as YEAR,
            SUM(case when SUBSTR(MONTH,6,2) in ('01','02','03') then TO_Number(SALARY) else 0 end) AS season1,
            SUM(case when SUBSTR(MONTH,6,2) in ('04','05','06') then TO_Number(SALARY) else 0 end) AS season2,
            SUM(case when SUBSTR(MONTH,6,2) in ('07','08','09') then TO_Number(SALARY) else 0 end) AS season3,
            SUM(case when SUBSTR(MONTH,6,2) in ('10','11','12') then TO_Number(SALARY) else 0 end) AS season4
            FROM "PERFORMANCE_USER_SALARY"
            WHERE SUBSTR(MONTH,0,4) in (%s)
            GROUP BY SUBSTR(MONTH,0,4)
        """ % year_str
        result = OracleUtil.query_dict_result(cursor, sql)
        return result

    @staticmethod
    def query_depart_and_month(months=[], depart=[], year='2017'):
        cursor = OracleUtil.get_cursor()
        months_str = ",".join(months)
        depart_str = ",".join(("'" + month + "'") for month in months)
        sql = """
            SELECT SUBSTR(MONTH,6,2) as MONTH,
            b.OFFICE_ID,
            SUM(SALARY) AS total
            FROM "PERFORMANCE_USER_SALARY" a
            LEFT JOIN "PERFORMANCE_USER" b
            ON a.USER_ID = b.ID
            WHERE SUBSTR(MONTH,0,4) = %s
        """ % year
        if len(months) > 0:
            sql += """
            AND SUBSTR(MONTH,6,2) in (%s)
            """ % months_str
        if len(depart) > 0:
            sql += """
                AND OFFICE_ID in (%s)
                GROUP BY SUBSTR(MONTH,6,2), OFFICE_ID
            """ % depart_str
        else:
            sql += """
                GROUP BY SUBSTR(MONTH,6,2), OFFICE_ID
            """
        cursor.execute(sql)
        return [cursor.fetchall(), cursor.description]

    @staticmethod
    def query_depart_and_categary(year='2017', month='', depart=''):
        cursor = OracleUtil.get_cursor()
        sql = """
            SELECT b.OFFICE_ID,
            PROGRAMID,
            SUM(TO_Number(SALARY)) AS total
            FROM "PERFORMANCE_RESULT_SALARY" a
            LEFT JOIN "PERFORMANCE_USER" b
            ON a.USER_ID = b.ID
            LEFT JOIN "PERFORMANCE_PROGRAM" c 
            on PROGRAMID = c.ID
            WHERE OFFICE_ID = '%s'
            AND SUBSTR(MONTH,0,4) = %s
        """ % (depart, year)
        if len(month) > 0:
            sql += """
                AND SUBSTR(MONTH,6,2) = %s
            """ % month
        sql += """
            GROUP BY PROGRAMID, OFFICE_ID
        """
        cursor.execute(sql)
        return [cursor.fetchall(), cursor.description]

    @staticmethod
    def query_year_salary(year='2017'):
        cursor = OracleUtil.get_cursor()

        sql = """
            SELECT USER_ID, b.NAME, OFFICE_ID, PROGRAMID, 
            SUM(case when c.INCLUDE_WAY = 0 then TO_Number(SALARY) else TO_Number(SALARY)*(-1) end) 
            AS amount
            FROM "PERFORMANCE_RESULT_SALARY" a
            LEFT JOIN "PERFORMANCE_USER" b
            ON a.USER_ID = b.ID
            LEFT JOIN "PERFORMANCE_PROGRAM" c 
            on PROGRAMID = c.ID
            WHERE SUBSTR(MONTH,0,4) = %s
            GROUP BY SUBSTR(MONTH,0,4), USER_ID, PROGRAMID, b.NAME, OFFICE_ID
        """ % year

        cursor.execute(sql)
        result = cursor.fetchall()
        return [result, cursor.description]

    @staticmethod
    def query_depart_dict():
        cursor = OracleUtil.get_cursor()

        sql = """
            SELECT SHORT_NAME, ID, NAME FROM "SYS_OFFICE"
        """
        result = OracleUtil.query_dict_result(cursor, sql)
        return result

    @staticmethod
    def query_jixiao_dict():
        cursor = OracleUtil.get_cursor()

        sql = """
                    SELECT SHORT_NAME, ID, PROGRAM_NAME FROM "PERFORMANCE_PROGRAM"
                """
        result = OracleUtil.query_dict_result(cursor, sql)
        return result