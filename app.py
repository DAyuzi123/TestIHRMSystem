import logging
import os
from logging import handlers
Base_dir = os.path.dirname(os.path.abspath(__file__))
HEADERS = {"Content-Type": "application/json"}
EMPID = ""

def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    sh = logging.StreamHandler()
    fh = logging.handlers.TimedRotatingFileHandler(Base_dir+"/log/IHRM.log",when="S",
                                                   interval=10,backupCount=3,encoding='utf-8')
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(fh)

if __name__ == '__main__':
    init_logging()
    logging.info("测试日志是否正常打印")
