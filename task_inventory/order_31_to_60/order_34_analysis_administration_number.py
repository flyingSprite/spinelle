import json

"""Order 34: generate administration code json file by text file.
解析中国行政编号
Text文档来源：http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201703/t20170310_1471429.html
查看所有的文字编码：http://graphemica.com/
"""


class AnalysisAdminNumber(object):

    @staticmethod
    def analysis_address_line(line):
        line = line.strip()
        line_arr = line.split(' ')
        code = line_arr[0]
        name = line_arr[len(line_arr) - 1]
        print(line, name)
        return code, name

    @staticmethod
    def read_file():
        file_path = '../dependency/administration_number.txt'
        with open(file_path, encoding='utf-8') as f:
            content = f.readlines()
        print(content)
        return content

    @staticmethod
    def write_file(json_content):
        file_path = '../dependency/administration_number.json'
        with open(file_path, 'w', encoding='utf8') as f:
            f.write(str(json_content))

    @staticmethod
    def analysis():
        content = AnalysisAdminNumber.read_file()

        root_admin_code = list()
        current_city_code_list = None
        current_county_code_list = None
        for line in content:
            if line.startswith('  '):
                code, name = AnalysisAdminNumber.analysis_address_line(line)
                county_code = dict()
                county_code['name'] = name
                county_code['code'] = code
                current_county_code_list.append(county_code)
            elif line.startswith(' '):
                code, name = AnalysisAdminNumber.analysis_address_line(line)
                city_code = dict()
                city_code['name'] = name
                city_code['code'] = code
                city_code['sub'] = list()
                current_city_code_list.append(city_code)
                current_county_code_list = city_code['sub']
            else:
                code, name = AnalysisAdminNumber.analysis_address_line(line)
                state_code = dict()
                state_code['name'] = name
                state_code['code'] = code
                state_code['sub'] = list()
                root_admin_code.append(state_code)
                current_city_code_list = state_code['sub']

        json_content = json.dumps(root_admin_code, indent=4, ensure_ascii=False)
        print(json_content)
        AnalysisAdminNumber.write_file(json_content)

    @staticmethod
    def test():
        AnalysisAdminNumber.analysis()


AnalysisAdminNumber.test()
