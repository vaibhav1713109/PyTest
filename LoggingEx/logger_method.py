import logging, inspect


def getlogging():
    logger_name = inspect.stack()[1][3]
    # print(logger_name)
    logger = logging.getLogger(logger_name)

    filehandler = logging.FileHandler('logfile.log',mode='a')  #file handller for saving the logs
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)
    return logger