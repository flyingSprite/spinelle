
"""Order 17: show time with give time and current time.

"""


class ShowTimeWithCurrentAndGiven(object):

    @staticmethod
    def show(current_timestamp=0, given_timestamp=0):
        if current_timestamp - given_timestamp < 0:
            return ''
        if current_timestamp - given_timestamp < 120:
            return '1分钟前'
        if current_timestamp - given_timestamp < 60 * 60:
            munite = int((current_timestamp - given_timestamp) / 60)
            return f'{munite}分钟前'
        if current_timestamp - given_timestamp < 24 * 60 * 60:
            hour = int((current_timestamp - given_timestamp) / 60 / 60)
            return f'{hour}小时前'
        day = int((current_timestamp - given_timestamp) / 24 / 60 / 60)
        return f'{day}天前'

# # 1分钟前
# print(ShowTimeWithCurrentAndGiven.show(1502173717, 1502173700))
# # 3分钟前
# print(ShowTimeWithCurrentAndGiven.show(1502173717, 1502173517))
# # 2小时前
# print(ShowTimeWithCurrentAndGiven.show(1502173717, 1502163517))
# # 11天前
# print(ShowTimeWithCurrentAndGiven.show(1502173717, 1501163517))
# # 127天前
# print(ShowTimeWithCurrentAndGiven.show(1502173717, 1491163517))
