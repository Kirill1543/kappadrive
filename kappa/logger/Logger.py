import os
import logging

SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__), os.pardir, os.pardir, os.pardir)))

LOG_DIR: str = os.path.join(SCRIPT_DIR, 'logs')
# LOG_FILE: str = 'log%s.log' % datetime.now().strftime('%Y_%m_%d_%H-%M-%S')
LOG_FILE: str = 'log.log'
LOG_LEVEL = logging.INFO


class Logger:
    def __init__(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(LOG_LEVEL)
        self.log_dir = LOG_DIR
        self.check_folder_exists()
        if not logger.handlers:
            file_name = os.path.join(self.log_dir, LOG_FILE)
            handler = logging.FileHandler(file_name, 'w')
            handler.setLevel(LOG_LEVEL)
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s %(levelname)s:[%(name)s] %(message)s')
            handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.addHandler(console_handler)
        self.__logger = logger

    def get(self):
        return self.__logger

    def check_folder_exists(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
