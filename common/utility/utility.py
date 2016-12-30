
import time


# return preve one hour timestamp and current hour timestamp
def prev_an_hour():
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
