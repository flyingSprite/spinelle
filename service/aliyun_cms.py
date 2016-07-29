
from conf import config

from aliyunsdkcore import client
from aliyunsdkcms.request.v20160318 import QueryMetricDataRequest


'''
Reference: https://help.aliyun.com/document_detail/28616.html?spm=5176.doc28615.6.137.tRBZjq
'''


def run():
    # RegionId: The required fixed value. Must be cn-hangzhou
    clt = client.AcsClient(config.ALIYUN_ACCESS_KEY_ID, config.ALIYUN_ACCESS_KEY_SECRET, 'cn-hangzhou')

    request = AcsRequest()
    cpu_utilization_request = request.cpu_utilization_request()

    result = clt.do_action(cpu_utilization_request)
    print result


class AcsRequest(object):

    # CPU percent:	Percent	instanceId	max value, min value, mean value
    @staticmethod
    def cpu_utilization_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('CPUUtilization')
        # Date Format: YYYY-MM-DDThh:mm:ssZ
        request.set_StartTime('2016-07-27T08:00:00Z')
        # request.set_Dimensions("{instanceId:'1527cf43124-cn-ningxiazhongwei'}")
        # request.set_Period('60')
        return request

    # Todo
    # internet in average flow rate:     bps	instanceId	max value, min value, mean value
    @staticmethod
    def internet_in_rate_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('InternetInRateNew')
        return request

    # Todo
    # Intranet in average flow rate:	bps	instanceId	max value, min value, mean value
    @staticmethod
    def intranet_in_rate_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('IntranetInRateNew')
        return request

    # Todo
    # 公网出流量平均速率	bps	instanceId	max value, min value, mean value
    @staticmethod
    def internet_out_rate_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('InternetOutRateNew')
        return request

    # Todo
    # 私网出流量平均速率	bps	instanceId	max value, min value, mean value
    @staticmethod
    def intranet_out_rate_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('IntranetOutRateNew')
        return request

    # Todo
    # 系统磁盘总读BPS	bps	instanceId	max value, min value, mean value
    @staticmethod
    def disk_read_bps_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('DiskReadBPSNew')
        return request

    # Todo
    # 系统磁盘总写BPS	bps	instanceId	max value, min value, mean value
    @staticmethod
    def disk_write_bps_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('DiskWriteBPSNew')
        return request

    # Todo
    # 系统磁盘读IOPS	Count/Second	instanceId	max value, min value, mean value
    @staticmethod
    def disk_read_iops_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('DiskReadIOPS')
        return request

    # Todo
    # 系统磁盘写IOPS	Count/Second	instanceId	max value, min value, mean value
    @staticmethod
    def disk_write_iops_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('DiskWriteIOPS')
        return request

    # Todo
    # 公网入流量	Bytes	instanceId	max value, min value, mean value, sum value
    @staticmethod
    def internet_in_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('InternetInNew')
        return request

    # Todo
    # 私网入流量	Bytes	instanceId	max value, min value, mean value, sum value
    @staticmethod
    def intranet_in_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('IntranetInNew')
        return request

    # Todo
    # 公网出流量	Bytes	instanceId	max value, min value, mean value, sum value
    @staticmethod
    def internet_out_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('InternetOutNew')
        return request

    # Todo
    # 私网出流量	Bytes	instanceId	max value, min value, mean value, sum value
    @staticmethod
    def intranet_out_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('IntranetOutNew')
        return request
