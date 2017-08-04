import os
import time

""" Order 1: Generate folder by timestamp

"""


class GenerateFolder(object):
    """
    Reference to http://blog.csdn.net/xiaobing_blog/article/details/12591917
    """

    @staticmethod
    def generate_by_year(root_dir, timestamp):
        lt = time.localtime(timestamp)
        folder_path = os.path.join(root_dir, str(lt.tm_year))
        GenerateFolder.generate_folder(folder_path)
        return folder_path

    @staticmethod
    def generate_by_month(root_dir, timestamp):
        lt = time.localtime(timestamp)
        folder_path = os.path.join(root_dir, str(lt.tm_year), str(lt.tm_mon))
        GenerateFolder.generate_folder(folder_path)
        return folder_path

    @staticmethod
    def generate_by_date(root_dir, timestamp):
        lt = time.localtime(timestamp)
        folder_path = os.path.join(root_dir, str(lt.tm_year), str(lt.tm_mon), str(lt.tm_mday))
        GenerateFolder.generate_folder(folder_path)
        return folder_path

    @staticmethod
    def generate_folder(folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


# Order 1 testing:
# gen_folder_path = GenerateFolder.generate_by_date('D:\\test', 1501221809)
# print(gen_folder_path)
