
"""Order 31: simple read and write excel

1. Write simple table data to excel;
2. Read the simple table data from excel;
"""

from faker import Faker
import xlrd
import xlwt


class SimpleReadAndWriteExcel(object):

    @staticmethod
    def read_excel_data(file_name):
        workbook = xlrd.open_workbook(file_name)
        print(workbook.sheet_names())
        # sheet索引从0开始
        # use_sheet = workbook.sheet_by_index(0)
        use_sheet = workbook.sheet_by_name(workbook.sheet_names()[0])

        # 获取整行和整列的值（数组）
        rows = use_sheet.row_values(3)  # 获取第四行内容
        cols = use_sheet.col_values(2)  # 获取第三列内容
        print(type(rows), rows)
        print(type(cols), cols)

        for row in range(10):
            for column in range(3):
                print(use_sheet.cell(row, column).value)

    @staticmethod
    def write_excel_data(file_name):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('sheet 1')

        start_row_num = 0

        need_save_data = SimpleReadAndWriteExcel.gen_data()
        for row_id, row in enumerate(need_save_data):
            for column_id, unit_data in enumerate(row):
                sheet.write(row_id + start_row_num, column_id, unit_data)

        workbook.save(file_name)

    @staticmethod
    def gen_data():
        faker_obj = Faker()
        data = list()
        for i in range(10):
            column = [
                i,
                faker_obj.name_female(),
                faker_obj.phone_number(),
                faker_obj.address()
            ]
            data.append(column)
        return data

    @staticmethod
    def test():
        data = SimpleReadAndWriteExcel.gen_data()
        print(data)

        SimpleReadAndWriteExcel.write_excel_data('test.xls')
        SimpleReadAndWriteExcel.read_excel_data('test.xls')


SimpleReadAndWriteExcel.test()
