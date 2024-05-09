import logging, random, inspect
from logger_method import getlogging

def test_logging():
    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('LoggingFile.log',mode='w')  #file handller for saving the logs
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)

    logger.debug('A debug message')
    logger.info("Information Statement")
    logger.warning('A warning meassage')
    logger.error('Error message')
    logger.critical('Critical Issue')

def test_baseLogger(fixture_pram):
    loge = getlogging()
    loge.info('Here we are calling logger from a fixture')
    loge.debug(fixture_pram)


def test_addition():
    loge = getlogging()
    loge.info('Here we are calling logger from a fixture')
    a = random.randint(1,100)
    b = random.randint(100,200)
    loge.debug(f'The sum of a and b is {a+b}')
    assert a+b >= 300