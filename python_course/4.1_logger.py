import logging
import os

LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", logging.DEBUG)


class CustomLoggerDecorator:
    def __init__(self,
                 func,
                 name: str = __name__,
                 level: int = LOGGING_LEVEL,
                 log_to_file: bool = True,
                 file_name = "logfile.log",
                 ):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.log_to_file = log_to_file
        self.file_name = file_name
        self.func = func


    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        formatter = logging.Formatter(f'%(asctime)s - %(module)s - %(funcName)s - {args} - {result}')
        custom_logger = logging.getLogger(__name__)
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        custom_logger.addHandler(console)
        if self.log_to_file:
            folder_path = os.path.dirname(*args)
            if folder_path:
                os.makedirs(folder_path, exist_ok=True)
            filehandler = logging.FileHandler(*args)
            filehandler.setFormatter(formatter)
            custom_logger.addHandler(filehandler)
        custom_logger.info(result)
        return custom_logger


@CustomLoggerDecorator
def custom_logger(*args):
    return "Logger INFO level message"


if __name__ == "__main__":
    print(custom_logger('Logger/logfile.log'))
