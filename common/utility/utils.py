
import time
import urllib.request


class TimeUtils(object):
    """Time utils
    Use to handle some operation with time.
    """

    # return preve one hour timestamp and current hour timestamp
    @classmethod
    def prev_an_hour(cls):
        """
        Get an hour before the timestamp and current timestamp.
        :return: an hour before the timestamp and current timestamp.
        """

        # Get string format time without seconds and minutes
        current_hour_time_str = time.strftime('%Y-%m-%d %H:00:00')
        # Turn string format time to time_tuple
        current_hour_time_tp = time.strptime(current_hour_time_str, '%Y-%m-%d %H:%M:%S')
        # Get the timestamp for the string formt time which without seconds and minutes
        current_hour_timestamp = int(time.mktime(current_hour_time_tp) * 1000)
        # Get the prev one hour timestamp
        prev_hour_timestamp = current_hour_timestamp - 60 * 60 * 1000

        # return preve one hour timestamp and current hour timestamp
        return prev_hour_timestamp, current_hour_timestamp


class FileUtils(object):
    """File utils
    Use to handle some operation with file.
    """

    @classmethod
    def save_file(cls, download_url, save_path_name):
        """
        Download image form download_url. And save to save_pathname
        :param download_url:  Image download url
        :param save_path_name: Save path name
        :return: None
        """
        urllib.request.urlretrieve(download_url, save_path_name)
