
from common.utility.utils import FileUtils

default_resource_path = '/Users/Fernando/Develop/downloader'


def get_image(image_hash):
    """
    Download huaban image by image hash code.
    Such as get_image('3058ff7398b8b725f436c6c7d56f60447468034d2347b-fGd8hd')
    :param image_hash: Image hash code. 
    :return: None
    """

    # Download normal auto size iamge.
    url_normal = f'http://img.hb.aicdn.com/{image_hash}'
    FileUtils.save_file(url_normal, f'{default_resource_path}/normal/{image_hash}.jpg')

    # Download 236px width size iamge.
    url_fw236 = f'http://img.hb.aicdn.com/{image_hash}_fw236'
    FileUtils.save_file(url_fw236, f'{default_resource_path}/fw236/{image_hash}.jpg')
