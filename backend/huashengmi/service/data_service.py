# -*- coding: utf-8 -*-
from dao.data_dao import DataDao
import config
import time


class DataService(object):

    def __init__(self):
        self.dao = DataDao()

    def jidu_salary_service(self, years):
        sql_result = self.dao.query_jidu_salary(years)
        #将数据库获取的数据按照接口标准重新组织
        seasons = ['SEASON1', 'SEASON2', 'SEASON3', 'SEASON4']
        if len(years) > 1:
            year_name = [year + '年' for year in years]
            return_result = {'category': {'years': year_name, 'seasons': ['第一季度', '第二季度', '第三季度', '第四季度']},
                             'dimen': ['season', 'year', 'index']}
            series = []
            i = 0
            for season in seasons:
                series.append([])
                for year in years:
                    if year in sql_result.keys():
                        series[i].append(round(sql_result[year][season] / 10000, 5))
                    else:
                        series[i].append(0)
                i += 1
            return_result['series'] = series
            return return_result
        else:
            series = []
            dict = sql_result.values()[0]
            sum = 0
            for season in seasons:
                series.append([dict[season], 0])
                sum += dict[season]
            for index in series:
                index[1] = sum / 4
            return_result = {'category' : ['实际工资', '预算工资'],
                             'series' : series}
            return return_result

    def depart_and_month_service(self, months=[], depart=[], year=str(time.localtime()[0])):
        return_result = self.dao.query_depart_and_month(months, depart, year)
        # 将数据库获取的数据按照接口标准重新组织
        sql_result = DataService.query_yangshi1_result(return_result[0], return_result[1])
        if len(months) > 0:
            depart_ID_list = [value['ID'] for key,value in config.depart_short_name_dict.items()]
            depart_dict = dict([(value['ID'], value['short_name']) for key, value in config.depart_short_name_dict.items()])
            depart_name_dict = dict([(value['ID'], value['name']) for key, value in config.depart_short_name_dict.items()])
            series = []
            depart_name_list = []
            depart_shortname_list = []
            for id in depart_ID_list:
                depart_shortname_list.append(depart_dict[id])
                depart_name_list.append(depart_name_dict[id])
            i = 0
            for sn in depart_shortname_list:
                series.append([])
                for month in months:
                    if month in sql_result.keys() and sn in sql_result[month].keys():
                        series[i].append(round(sql_result[month][sn] / 10000, 5))
                    else:
                        series[i].append(0)
                i += 1
            months_name = [year + '年' + month + '月' for month in months]
            return_result = {'category' : {'month' : months_name, 'depart' : depart_name_list},
                             'series' : series,
                             'dimen' : ['depart', 'month', 'index']}
            return return_result
        else:
            for key, value in sql_result.items():
                sum = 0
                for key2, value2 in value.items():
                    if key2 != 'MONTH':
                        sum += value2
                    else:
                        value[key2] = year + '年' + value2 + '月'
                value['SUM'] = round(sum,2)
            return sql_result

    def depart_and_categary_service(self, year=str(time.localtime()[0]), month='01', depart=''):
        return_result = self.dao.query_depart_and_categary(year, month, depart)
        # 将数据库获取的数据按照接口标准重新组织
        sql_result = DataService.query_yangshi1_result(return_result[0], return_result[1])
        depart_name_dict = {}
        for key, value in config.depart_short_name_dict.items():
            depart_name_dict[value['ID']] = value['name']
        jixiao_category_dict = {}
        for key, value in config.jixiao_short_name_dict.items():
            jixiao_category_dict[value['ID']] = value['category']
        depart_name = depart_name_dict[depart]
        series = [0, 0, 0, 0, 0]
        if len(sql_result.values()) > 0:
            for dict in sql_result.values():
                for id in dict.keys():
                    if id in jixiao_category_dict:
                        series[jixiao_category_dict[id] - 1] += dict[id]
        max = 0
        for sum in series:
            if sum > max:
                max = sum
        category = []
        for name in config.jixiao_sum_title:
            category.append({'text': name, 'max': max})
        return_result = {'category': category,
                         'series': series,
                         'depart_name': depart_name}
        return return_result

    def year_salary(self, year=str(time.localtime()[0]), cur_page=1, page_size=10):
        # 因为数据只有两百多条，所以采用全部获取再截取的方式获取分页数据
        start = (cur_page - 1) * page_size
        end = cur_page * page_size
        return_result = self.dao.query_year_salary(year)
        sql_result = DataService.query_yangshi2_result(return_result[0], return_result[1])
        return {'data': sql_result[start:end], 'total_num': len(sql_result)}

    def year_salary_for_download(self, year=str(time.localtime()[0])):
        return_result = self.dao.query_year_salary(year)
        sql_result = DataService.query_yangshi2_result(return_result[0], return_result[1])
        jixiao_dict = {}
        jixiao_name_dict = {}
        for key, value in config.jixiao_short_name_dict.items():
            jixiao_dict[value['ID']] = value['short_name']
            jixiao_name_dict[value['ID']] = value['name']
        jixiao_ID_list = [0]*len(config.jixiao_short_name_dict)
        for id in jixiao_dict:
            jixiao_ID_list[config.jixiao_name_list.index(jixiao_name_dict[id])] = id
        jixiao_short_name_list = []
        jixiao_name_list = []
        for id in jixiao_ID_list:
            jixiao_short_name_list.append(jixiao_dict[id])
            jixiao_name_list.append(jixiao_name_dict[id])
        header_list = ['USER_ID', 'NAME', 'OFFICE_ID']
        header_list.extend(jixiao_short_name_list)
        header_name_list = ['员工编号', '姓名', '部门']
        header_name_list.extend(jixiao_name_list)
        header_list.append('TOTAL')
        header_name_list.append('合计')
        header_dict = {}
        for i in range(len(header_list)):
            header_dict[header_list[i]] = i
        series = []
        for row in sql_result:
            list = [0] * len(header_list)
            for key, value in row.items():
                list[header_dict[key]] = value
            series.append(list)
        return [header_name_list, series]

    # 样式一
    @staticmethod
    def query_yangshi1_result(sql_result, description):
        u"""重组织数据
            """

        result_dict = {}
        keys = [row[0] for row in description]
        depart_dict = {}
        for key, value in config.depart_short_name_dict.items():
            depart_dict[value['ID']] = value['short_name']
        jixiao_dict = {}
        for key, value in config.jixiao_short_name_dict.items():
            jixiao_dict[value['ID']] = value['short_name']
        for row in sql_result:
            if row[0] not in result_dict:
                result_dict[row[0]] = {keys[0]: row[0]}
            if row[1] in depart_dict:
                depart_short_name = depart_dict[row[1]]
                result_dict[row[0]][depart_short_name] = row[2]
            if row[1] in jixiao_dict:
                result_dict[row[0]][row[1]] = row[2]
        return result_dict

    # 样式二
    @staticmethod
    def query_yangshi2_result(sql_result, description):
        u"""重组织数据
            """
        result_dict = {}
        keys = [row[0] for row in description]
        depart_dict = {}
        depart_name_dict = {}
        for key, value in config.depart_short_name_dict.items():
            depart_dict[value['ID']] = value['short_name']
            depart_name_dict[value['ID']] = value['name']
        jixiao_dict = {}
        for key, value in config.jixiao_short_name_dict.items():
            jixiao_dict[value['ID']] = value['short_name']
        for row in sql_result:
            if row[2] in depart_dict and row[3] in jixiao_dict:
                if int(row[0]) not in result_dict:
                    depart_name = depart_name_dict[row[2]]
                    result_dict[int(row[0])] = {keys[0]: row[0], keys[1]: row[1], keys[2]: depart_name, 'TOTAL' : 0}
                jixiao_short_name = jixiao_dict[row[3]]
                result_dict[int(row[0])][jixiao_short_name] = row[4]
                result_dict[int(row[0])]['TOTAL'] += row[4]
        return result_dict.values()