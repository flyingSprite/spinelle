# -*- coding: utf-8 -*-

"""Scrapy Pipeline.

SavingPipeline: Normal pipeline, using to save item data to DB.
ImageDownloaderPipeline: Image pipeline, download image by crawl url.
"""

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import hashlib
# from scrapy import Request
# from scrapy.pipelines.images import ImagesPipeline

# from utility.mongo import MongoService


def special_pipeline_wrapper(wrapper_arg):
    """
    For different item use different pipeline.
    Each item must be contained stype. If stype equal wrapper_args or stype in wrapper_args,
    Will be call pipeline process_item func.
    
    :param wrapper_arg: can be str or str array. Witch item can use the pipeline
    :return: wapperfunc
    """
    def wrapper_func(func):
        def wrapper_args(that, item, *args, **kwargs):
            if item['stype'] == wrapper_arg or item['stype'] in wrapper_arg:
                func(that, item, *args, **kwargs)
        return wrapper_args
    return wrapper_func


class SpinellePipeline(object):

    @special_pipeline_wrapper('ltaaa')
    def process_item(self, item, spider):
        return item


class SavingPipeline(object):
    """Class HotNewsPipeline start."""

    collection = None

    def __init__(self):
        """__init__."""
        # self.service = MongoService()
        # self.collection = self.service.collection('hotnews')

    @special_pipeline_wrapper(wrapper_arg=['ltaaa'])
    def process_item(self, item, spider):
        print('ssxxxxxxxx1')
        print(spider)
        """Process hotnews item."""
        # Overlook spider argument
        # _ = spider
        # print item
        # self.save(item)
        return item

    def save(self, item):
        """Save hotnews to db."""
        # self.service.upsert(
        #     self.collection,
        #     item,
        #     {'href': item['href']},
        #     'amendTimestamp'
        # )


# class TestPipeline(ImagesPipeline):
#
#     def get_media_requests(self, item, info):
#         print(item, info.spider.name)
#
#     def item_completed(self, results, item, info):
#         pass
#
#
# class ImageDownloaderPipeline(ImagesPipeline):
#
#     def get_media_requests(self, item, info):
#         # print item
#         name = item.get('name', 'full')
#         urls_filed = 'images'
#         return [Request(url=x, meta={'name': name}) for x in item.get(urls_filed, [])]
#
#     # def process_item(self, item, spider):
#     #     print item
#     #     return item
#
#     def item_completed(self, results, item, info):
#         return item
#
#     # @override file_path
#     def file_path(self, request, response=None, info=None):
#         # start of deprecation warning block (can be removed in the future)
#         def _warn():
#             from scrapy.exceptions import ScrapyDeprecationWarning
#             import warnings
#             warnings.warn('ImagesPipeline.image_key(url) and file_key(url) methods are deprecated, '
#                           'please use file_path(request, response=None, info=None) instead',
#                           category=ScrapyDeprecationWarning, stacklevel=1)
#
#         # check if called from image_key or file_key with url as first argument
#         if not isinstance(request, Request):
#             _warn()
#             url = request
#         else:
#             url = request.url
#
#         # detect if file_key() or image_key() methods have been overridden
#         if not hasattr(self.file_key, '_base'):
#             _warn()
#             return self.file_key(url)
#         elif not hasattr(self.image_key, '_base'):
#             _warn()
#             return self.image_key(url)
#         # end of deprecation warning block
#
#         name = request.meta['name']
#         image_guid = hashlib.sha1(url).hexdigest()  # change to request.url after deprecation
#         path = name + '/%s.jpg' % image_guid
#         return path


