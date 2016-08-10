
import json
import time

from conf import config
from utility.mongo import MongoService
from utility import utility

from aliyunsdkcore import client
from aliyunsdkcms.request.v20160318 import QueryMetricDataRequest


'''
Reference: https://help.aliyun.com/document_detail/28616.html?spm=5176.doc28615.6.137.tRBZjq
'''


def run():
    request = AcsRequest()
    start_timestamp, end_timestamp = utility.prev_an_hour()

    # Start timestamp revise, prevent lose some monitoring data.
    start_timestamp -= 5 * 60 * 1000
    result = request.cpu_utilization_request(start_timestamp, end_timestamp)
    code = result.get('Code')

    if code == '200':
        request_id = result.get('RequestId')
        period = result.get('Period')
        data_points = result.get('Datapoints')
        resolve = AcsResolve()
        resolve.parse_cpu_utilization(
            data_points,
            period=period,
            request_id=request_id
        )


class AcsResolve(object):

    collection_name = 'cmsMonitor'

    def __init__(self, ):
        self.mongo_template = MongoService()
        self.collection = self.mongo_template.collection(self.collection_name)

    def parse_cpu_utilization(self, data_points, period=60, request_id='1'):
        inter_timestamp = int(time.time() * 1000)
        items = []
        for (index, point) in enumerate(data_points):
            item = dict()
            # For mongodb, the primary key must be _id
            # Use timestamp as primary value
            item['_id'] = point['timestamp']
            item['category'] = 'cpu'
            item['interTimestamp'] = inter_timestamp
            item['requestId'] = request_id
            item['period'] = period
            item['userId'] = point['userId']
            item['timestamp'] = point['timestamp']
            item['minimum'] = point['Minimum']
            item['maximum'] = point['Maximum']
            item['average'] = round(point['Average'], 2)
            items.append(item)
        self.save(items)

    def save(self, items):
        # print json.dumps(items, indent=4)
        # Save to MongoDB
        self.collection.insert_many(items)


class AcsRequest(object):

    def __init__(self):
        # RegionId: The required fixed value. Must be cn-hangzhou
        self.client = client.AcsClient(
            config.ALIYUN_ACCESS_KEY_ID,
            config.ALIYUN_ACCESS_KEY_SECRET,
            'cn-hangzhou'
        )

    # CPU percent:	Percent	instanceId	max value, min value, mean value
    def cpu_utilization_request(self, start_timestamp, end_timestamp):
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('CPUUtilization')
        # Date Format: YYYY-MM-DDThh:mm:ssZ
        # request.set_StartTime('2016-07-27T08:00:00Z')
        request.set_StartTime(start_timestamp)
        # request.set_EndTime('2016-07-28T08:00:00Z')
        request.set_EndTime(end_timestamp)
        # request.set_Dimensions("{instanceId:'1527cf43124-cn-ningxiazhongwei'}")
        request.set_Period('60')
        # return request
        return json.loads(self.client.do_action(request))

    # Todo
    # internet in average flow rate: bps instanceId	max value, min value, mean value
    @staticmethod
    def internet_in_rate_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('InternetInRateNew')
        return request

    # Todo
    # Intranet in average flow rate: bps instanceId	max value, min value, mean value
    @staticmethod
    def intranet_in_rate_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('IntranetInRateNew')
        return request

    # Todo
    # internet out average flow rate bps instanceId	max value, min value, mean value
    @staticmethod
    def internet_out_rate_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('InternetOutRateNew')
        return request

    # Todo
    # intranet out average flow rate bps instanceId	max value, min value, mean value
    @staticmethod
    def intranet_out_rate_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('IntranetOutRateNew')
        return request

    # Todo
    # disk read total BPS: bps instanceId max value, min value, mean value
    @staticmethod
    def disk_read_bps_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('DiskReadBPSNew')
        return request

    # Todo
    # disk write total BPS	bps	instanceId	max value, min value, mean value
    @staticmethod
    def disk_write_bps_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('DiskWriteBPSNew')
        return request

    # Todo
    # disk read io ps	Count/Second	instanceId	max value, min value, mean value
    @staticmethod
    def disk_read_iops_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('DiskReadIOPS')
        return request

    # Todo
    # disk write io ps	Count/Second	instanceId	max value, min value, mean value
    @staticmethod
    def disk_write_iops_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('DiskWriteIOPS')
        return request

    # Todo
    # internet in	Bytes	instanceId	max value, min value, mean value, sum value
    @staticmethod
    def internet_in_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('InternetInNew')
        return request

    # Todo
    # intranet Bytes instanceId max value, min value, mean value, sum value
    @staticmethod
    def intranet_in_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('IntranetInNew')
        return request

    # Todo
    # internet out Bytes instanceId	max value, min value, mean value, sum value
    @staticmethod
    def internet_out_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('InternetOutNew')
        return request

    # Todo
    # intranet out Bytes instanceId max value, min value, mean value, sum value
    @staticmethod
    def intranet_out_new_request():
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')
        request.set_Project('acs_ecs')
        request.set_Metric('IntranetOutNew')
        return request
