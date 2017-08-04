import os
import urllib.request

""" Order 3: Download iamge with image url

For internet crawl spider, donwload image is necessary. So Write a function to deel it.
"""


class DownloadImageWithUrl(object):

    @staticmethod
    def donwload(image_url, save_path, save_name):

        urllib.request.urlretrieve(image_url, os.path.join(save_path, save_name))


# Order 3 testing:
# i_image_url = 'http://img.hb.aicdn.com/576fe24099dd9481d52ebeb503b0e17cd95183d5341e6-VUYSZv_fw658'
# i_save_path = 'D:\\test'
# i_save_name = '576fe24099dd9481d52ebeb503b0e17cd95183d5341e6.jpg'
# DownloadImageWithUrl.donwload(i_image_url, i_save_path, i_save_name)
