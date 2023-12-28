import re
import logging

log_file = "C:\\Users\\Yevhen\\Downloads\\Telegram Desktop\\yupdate.log"

logger = logging.getLogger('dev')
logger.setLevel(logging.ERROR)

fileHandler = logging.FileHandler('found_errors.log')
fileHandler.setLevel(logging.ERROR)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.CRITICAL)

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)


class ExceptionCriticalError(Exception):
    pass


def error_line(file_name):
    try:
        with open(file_name, 'r') as log:
            global num_string, errors
            num_string = sum(1 for _ in open(file_name, 'r'))
            errors = [line for line in log.readlines() if re.findall(r'error|Error|ERROR', line)]
    except Exception:
        print("You made a mistake")
    else:
        for line in errors:
            try:
                if not 'CRITICAL ERROR' in line:
                    logger.error(line)
                else:
                    raise ExceptionCriticalError
            except ExceptionCriticalError:
                logger.critical(line)


def result_errors():
    try:
        count = num_string / len(errors)
        return count
    except ZeroDivisionError:
        return "Second argument to a division or modulo operation was zero."
    except Exception:
        return 'You have a mistake in error_line()'


if __name__ == '__main__':
    error_line(log_file)
    print(result_errors())
