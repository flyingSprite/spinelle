
from conf import config

from aliyunsdkcore import client
from aliyunsdkcms.request.v20160318 import QueryMetricDataRequest


'''
Reference: https://help.aliyun.com/document_detail/28616.html?spm=5176.doc28615.6.137.tRBZjq
'''


def run():
    # RegionId: The required fixed value. Must be cn-hangzhou
    clt = client.AcsClient(config.ALIYUN_ACCESS_KEY_ID, config.ALIYUN_ACCESS_KEY_SECRET, 'cn-hangzhou')
    request = QueryMetricDataRequest.QueryMetricDataRequest()
    request.set_accept_format('json')
    request.set_Project('acs_ecs')
    request.set_Metric('CPUUtilization')
    # Date Format: YYYY-MM-DDThh:mm:ssZ
    request.set_StartTime('2016-07-27T08:00:00Z')
    # request.set_Dimensions("{instanceId:'1527cf43124-cn-ningxiazhongwei'}")
    # request.set_Period('60')
    result = clt.do_action(request)

    print result
