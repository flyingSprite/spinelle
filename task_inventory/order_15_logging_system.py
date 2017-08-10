import json
import os
import logging
import logging.config


"""Order 15: Use logging with generate log files.

In this sample:
Logging config:     dependency/logging.json
Info logging file： dependency/logs/info.log
Error logging file: dependency/logs/error.log
"""


class LoggingSystem(object):
    logging_config_file = 'dependency/logging.json'

    def __init__(self):
        if os.path.exists(self.logging_config_file):
            with open(self.logging_config_file, 'rt') as f:
                config = json.load(f)
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=logging.INFO)


# LoggingSystem()
# logger = logging.getLogger(__name__)
# logger.info('this is info')
# logger.error('this is error')
