
import requests

import urllib.request

default_resource_path = '/Users/Fernando/Develop/downloader'


def get_image(image_hash):
    url_normal = f'http://img.hb.aicdn.com/{image_hash}'
    url_fw236 = f'http://img.hb.aicdn.com/{image_hash}_fw236'
    urllib.request.urlretrieve(url_normal, f'{default_resource_path}/normal/{image_hash}.jpg')
    urllib.request.urlretrieve(url_normal, f'{default_resource_path}/fw236/{image_hash}.jpg')

# get_image('3058ff7398b8b725f436c6c7d56f60447468034d2347b-fGd8hd')
