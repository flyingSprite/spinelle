import imageio
from imageio.core.format import CannotReadFrameError
import os
import sys
from common.utility.utils import FileUtils


"""Order 39: Download mp4 video by url and convert the mp4 file to gif
"""


class TargetFormat(object):
    GIF = ".gif"
    MP4 = ".mp4"
    AVI = ".avi"


class DownlaodMp4(object):

    mp4_list = list()

    def __init__(self, read_file_name, save_folder):
        self.read_file_name = read_file_name
        self.save_folder = save_folder
        self.get_video_list()

    def get_video_list(self):
        with open(self.read_file_name) as f:
            contents = f.readlines()
            if contents:
                for content in contents:
                    self.mp4_list.append(content.strip())

    def downlaod(self):
        for url in self.mp4_list:
            paths = url.split('/') if url else list()
            if len(paths) > 0:
                print('\n', url, paths[-1])
                save_file_name = os.path.join(self.save_folder, paths[-1])
                FileUtils.save_file(url, save_file_name)
                try:
                    self.convert_to_gif(save_file_name, TargetFormat.GIF)
                except AssertionError or CannotReadFrameError:
                    print('Error:', save_file_name)

    @staticmethod
    def convert_to_gif(inputpath, target_format):
        """Reference: http://imageio.readthedocs.io/en/latest/examples.html#convert-a-movie"""
        outputpath = os.path.splitext(inputpath)[0] + target_format

        reader = imageio.get_reader(inputpath)
        fps = reader.get_meta_data()['fps']

        writer = imageio.get_writer(outputpath, fps=fps)
        for i, im in enumerate(reader):
            sys.stdout.write("\rframe {0}".format(i))
            sys.stdout.flush()
            writer.append_data(im)
        writer.close()


# file_name = '/Users/Fernando/Desktop/videos'
# save_folder = '/Users/Fernando/Desktop/video_gif'
# down = DownlaodMp4(file_name, save_folder)
# down.downlaod()
