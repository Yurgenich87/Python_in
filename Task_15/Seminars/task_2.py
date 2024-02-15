from functools import wraps
import logging


logging.basicConfig(level='DEBUG')
logger = logging.getLogger(__name__)

handler_error = logging.FileHandler('log.log', encoding='utf-8')
handler_error.setLevel(logging.ERROR)
logger.addHandler(handler_error)


def func_decorator(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            logger.critical(e)
            raise e
        return result
    return wrap


@func_decorator
def logging_errors(a, b):
    return a / b


if __name__ == '__main__':
    try:
        logging_errors(5, 0)
    except ZeroDivisionError as e:
       print(e)
