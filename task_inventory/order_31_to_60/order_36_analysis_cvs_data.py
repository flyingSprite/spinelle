
import csv

""" Order 36: analysis csv data file.
In this sample, we will analysis Baidu Browser Data.
will get two 

"""
document_mapping = {
    u'排序': 'index',
    u'浏览器': 'browser',
    u'浏览量占比': 'browser_ratio',
    u'时间': 'date',
    u'Chrome': 'Chrome',
    u'IE 7.0': 'IE 7.0',
    u'IE 8.0': 'IE 8.0',
    u'IE 9.0': 'IE 9.0',
    u'IE 10.0': 'IE 10.0',
    u'QQ': 'QQ',
    u'2345': '2345',
    u'搜狗': '搜狗',
    u'Firefox': 'Firefox',
    u'其他': '其他'
}


class AnalysisCSV(object):

    @staticmethod
    def read_csv(filename, cb):
        with open(filename, 'r', encoding='gbk') as f:
            if cb:
                cb(csv.reader(f))

    def get_dict_data(self, arr, headers, start, type_name):
        data = list()
        for i in range(start, len(arr)):
            row = arr[i]
            new_dict_row = {'type': type_name}
            for index, header in enumerate(headers):
                new_dict_row[header] = self.analysis_atom_data(row[index])
            data.append(new_dict_row)
        return data

    @staticmethod
    def get_header_dict(headers):
        header_dict = list()
        for header in headers:
            if header:
                header_dict.append(document_mapping[header])
        return header_dict

    def analysis_atom_data(self, str_data):
        if str_data.startswith('='):
            return self.analysis_date_data(str_data)
        elif str_data.endswith('%'):
            return self.analysis_ratio_data(str_data)
        else:
            return str_data

    @staticmethod
    def analysis_date_data(date_str):
        """
        :param date_str: 格式如同="2017.07.01"的字符串
        :return: 格式如同2017.07.01的字符串
        """
        print(date_str)
        return date_str[2: -1]

    @staticmethod
    def analysis_ratio_data(ratio_str):
        """
        :param ratio_str: 格式如同13.90%的字符串
        :return: 返回float数字
        """
        return float(ratio_str[0: -1])

    def render(self):
        pass


class AnalysisBrowserCSV(AnalysisCSV):

    def __init__(self, filename):
        self.filename = filename

    def analysis(self, reader):
        valid_arr = list()
        for row in reader:
            if len(row) == 0:
                self.analysis_valid_data(valid_arr)
                valid_arr = list()
            else:
                valid_arr.append(row)

    def analysis_valid_data(self, arr):
        if len(arr) > 0:
            first_row = arr[0]
            if len(first_row) == 1:
                self.analysis_browser_ratio(arr)
            else:
                self.analysis_browser_total_ratio(arr)

    def analysis_browser_ratio(self, arr):
        name = arr[0][0]
        headers = self.get_header_dict(arr[1])
        data = self.get_dict_data(arr, headers, 2, name)
        print(data)

    def analysis_browser_total_ratio(self, arr):
        headers = self.get_header_dict(arr[0])
        data = self.get_dict_data(arr, headers, 1, 'Total - Last 3 Mouth')
        print(data)

    def render(self):
        self.read_csv(filename=self.filename, cb=self.analysis)

    @staticmethod
    def test():
        filename = '../dependency/csv/baiduData-browser_2017.07-2017.09.csv'
        analysis = AnalysisBrowserCSV(filename)
        analysis.render()


AnalysisBrowserCSV.test()
