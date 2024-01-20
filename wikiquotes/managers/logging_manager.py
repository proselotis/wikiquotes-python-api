import logging
import time
import sys
import inspect
from functools import wraps

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')


def error(message):
    logger.error(message)

def info(message):
    logger.info(message)

def debug(message):
    logger.debug(message)

#slack = Slacker(slack_token)

logger = logging.getLogger("wikiquotes")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger.setLevel(logging.DEBUG)
logger.propagate = False

def log_method_call(task):
    @wraps(task)
    def callable(*args, **kwargs):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        function_called = "{}".format(task.__name__)
        logging.info("{} started: ".format(function_called))
        start_detection = time.time()
        task(*args, **kwargs)
        logging.info("{} finished: took {} seconds".format(function_called, time.time() - start_detection))
        return task(*args, **kwargs)
    return callable
