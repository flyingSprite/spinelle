
from task_inventory.order_1_to_30.order_3_donwload_image_with_url import DownloadImageWithUrl

""" Order 4: Donwload multi images, and get the schedule.
If crawl a website, we can crawl many image url and save them to database.
When download those images, should know the schedule.
"""


class DownloadMultiImages(object):

    @staticmethod
    def download(images, save_path, report_func=None):
        report_message = {
            'success': 0,
            'error': 0,
            'total': len(images)
        }
        for img in images:
            try:
                DownloadImageWithUrl.donwload(img.get('url'), save_path, img.get('name'))
                report_message['success'] = report_message['success'] + 1
            except IOError:
                report_message['error'] = report_message['error'] + 1
            if report_func:
                report_func(report_message)


# base_url = 'http://img.hb.aicdn.com/576fe24099dd9481d52ebeb503b0e17cd95183d5341e6-VUYSZv_fw658'
# image_save_path = '/Users/Fernando/Develop/test'
#
# download_images = list()
# for i in range(0, 1000):
#     download_image = dict()
#     download_image['name'] = f'img_{str(i)}.jpg'
#     download_image['url'] = base_url
#     download_images.append(download_image)
#
#
# def report(report_info):
#     print(report_info)
#
# DownloadMultiImages.download(download_images, image_save_path, report)
