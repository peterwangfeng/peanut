#coding=utf-8
import cx_Oracle
import config as config


class OracleUtil(object):

    def __init__(self):
        pass

    @staticmethod
    def get_cursor():
        ID = config.oracle_config['ID']
        pwd = config.oracle_config['pwd']
        host = config.oracle_config['host']
        connection = cx_Oracle.connect(ID, pwd, host)
        return connection.cursor()

    #list形式
    @staticmethod
    def query_list_result(cursor, sql):
        u"""执行SQL查询语言，以字典列表形式返回结果。

                    例1 ::
                        query_dict_result('SELECT id, alias FROM game')

                        返回如下结果：

                        [{'id' : 1, 'name' : '已结案件数'...},
                         {'id' : 2, 'name' : '未结案件数'...},
                         {'id' : 3, 'name' : '新收案件数'...},
                        ]

                    **参数：**
                        * sql (str): SQL语句。

                    **返回：**
                        * 字典列表。字典的键是数据库中的id。
                          不存在数据时，返回空字典。
                    """
        cursor.execute(sql)
        sql_result = cursor.fetchall()
        keys = [row[0] for row in cursor.description]
        dictlist_result = [dict(zip(keys, [x for x in row])) for row in sql_result]
        return dictlist_result

    #dict形式
    @staticmethod
    def query_dict_result(cursor, sql):
        u"""执行SQL查询语言，以字典字典形式返回结果。

            例1 ::

                query_dict_result('SELECT id, name... FROM INDEX_INFO')

                返回如下结果：

                {1 : {'id' : 1, 'name' : '已结案件数'...},
                 2 : {'id' : 2, 'name' : '未结案件数'...},
                 3 : {'id' : 3, 'name' : '新收案件数'...},
                }

            **参数：**
                * sql (str): SQL语句。

            **返回：**
                * 字典字典。外部字典的键查询结果的第一列，内部字典的键是数据库中的列名。
                  不存在数据时，返回空字典。
            """
        cursor.execute(sql)
        sql_result = cursor.fetchall()
        keys = [row[0] for row in cursor.description]
        dictdict_result = dict([(str(row[0]), dict(zip(keys, row))) for row in sql_result])
        return dictdict_result
