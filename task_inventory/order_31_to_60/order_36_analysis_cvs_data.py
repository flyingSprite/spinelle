
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


class ReadCSV(object):

    @staticmethod
    def read(filename, cb):
        with open(filename, 'r', encoding='gbk') as f:
            if cb:
                cb(csv.reader(f))


class AnalysisBrowserCSV(object):

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
        print('++++++++++++++++++++++++++++++')
        if len(arr) > 0:
            first_row = arr[0]
            if len(first_row) == 1:
                self.analysis_browser_ratio(first_row)
            else:
                self.analysis_browser_total_ratio(first_row)

    def analysis_browser_ratio(self, arr):
        pass

    def analysis_browser_total_ratio(self, arr):
        pass

    def render(self):
        ReadCSV.read(filename=self.filename, cb=self.analysis)

    @staticmethod
    def test():
        filename = '../dependency/csv/baiduData-browser_2017.07-2017.09.csv'
        analysis = AnalysisBrowserCSV(filename)
        analysis.render()


AnalysisBrowserCSV.test()
