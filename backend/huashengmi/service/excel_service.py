# encoding: utf-8

import xlwt
from config import conf_of_excel
import StringIO


class XlsCreater(object):
    def __init__(self):
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.worksheet = self.workbook.add_sheet('Sheet1')
        self.start_row = 0
        self.start_col = 0
        self.title_style = self._set_header_style(height=440)
        self.header_style = self._set_header_style()
        self.row_style = self._set_row_style()

    def _set_header_style(self, name="Times New Roman", height=220, bold=True, borders=xlwt.Borders.MEDIUM):
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = name
        font.bold = bold
        font.height = height
        style.font = font
        style.borders.left = borders
        style.borders.right = borders
        style.borders.top = borders
        style.borders.bottom = borders
        style.alignment.horz = 2
        style.alignment.vert = 1
        style.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
        return style

    def _set_row_style(self, name="Times New Roman", height=220, bold=False, borders=xlwt.Borders.THIN):
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = name
        font.bold = bold
        font.height = height
        style.font = font
        style.borders.left = borders
        style.borders.right = borders
        # style.borders.top = borders
        style.borders.bottom = borders
        style.alignment.horz = 2
        style.alignment.vert = 1
        style.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
        return style

    def _write_header(self, headers_dict):
        title = headers_dict['title']
        start_col = self.start_col
        start_row = self.start_row + 1
        headers = headers_dict['header']
        for i in headers:
            count = 0
            if i['children']:
                for child in i['children']:
                    self.worksheet.write(start_row + 1, start_col + count, child, self.header_style)
                    self.worksheet.col(start_col + count).width = len(child)*256
                    count += 1
                self.worksheet.write_merge(start_row, start_row, start_col, start_col + count - 1, i['name'],
                                           self.header_style)
                start_col += count
            else:
                self.worksheet.write_merge(start_row, start_row + 1, start_col, start_col, i['name'], self.header_style)
                start_col += 1
        self.worksheet.write_merge(0, 0, 0, start_col - 1, title['name'], self.title_style)
        self.start_row += 3
        return start_row + 2, 0

    def insert_data(self, header_conf, rows):
        self._write_header(header_conf)
        max_length = self._write_rows(rows)
        self.worksheet.col(1).width = 256 * max_length
        return self.save()

    def _write_rows(self, rows):
        # 初始化最大字符串长度
        max_length = 3
        for row in rows:
            # 写入单元格的起始列
            start_col = self.start_col
            # 初始化每行的单元格列增量
            cell_num = 0
            for cell in row:
                self.worksheet.write(self.start_row, start_col + cell_num, cell, self.row_style)
                cell_num += 1
                max_length = len(str(cell)) if len(str(cell)) > max_length else max_length
            self.start_row += 1
        return max_length

    def save(self):
        str_io = StringIO.StringIO()
        self.workbook.save(str_io)
        return str_io.getvalue()


if __name__ == '__main__':

    a = XlsCreater()
    try:
        a._write_header(conf_of_excel)
    except Exception as e:
        print e
        a.workbook.save('test.xls')
    a.workbook.save('test.xls')
