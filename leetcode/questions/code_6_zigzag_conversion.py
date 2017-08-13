

class ZigZagConversion(object):

    @staticmethod
    def solution(text, row_num):
        zigzag_list = list()
        for ii in range(0, row_num):
            zigzag_list.append(list())

        text_len = len(text)
        repeat_num = row_num * 2 - 2
        if repeat_num == 0:
            return text
        column_index = -1
        for i in range(0, text_len):
            if i % repeat_num == 0:
                column_index += 1
            if i % repeat_num < row_num:
                n = i % repeat_num
            else:
                column_index += 1
                n = row_num * 2 - i % repeat_num - 2
            zigzag_list[n].append(i)

        new_str = ''
        for zigzag in zigzag_list:
            for index in zigzag:
                new_str += text[index]
        return new_str

    @staticmethod
    def test():
        result = ZigZagConversion.solution('a', 1)
        # PPIINAASRGYLHI
        print(result, result == 'PAHNAPLSIIGYIR')


ZigZagConversion.test()
