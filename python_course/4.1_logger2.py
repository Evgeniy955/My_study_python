import logging
import os

LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", logging.INFO)


class CustomLoggerDecorator:
    def __init__(self,
                 func,
                 name: str = __name__,
                 level: int = LOGGING_LEVEL,
                 log_to_file: bool = True,
                 file_name: str = "logfile.log",
                 formatter_str: str = "%(asctime)s - %(levelname)s - %(message)s",
                 ):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.formatter = logging.Formatter(formatter_str)
        self.log_to_file = log_to_file
        self.file_name = file_name
        self.func = func

        console = logging.StreamHandler()
        console.setFormatter(self.formatter)
        self.logger.addHandler(console)
        if self.log_to_file:
            filehandler = logging.FileHandler(self.file_name)
            filehandler.setFormatter(self.formatter)
            self.logger.addHandler(filehandler)

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        formatter = logging.Formatter(f'%(asctime)s - %(module)s - %(funcName)s - {args} - {result}')
        custom_logger = logging.getLogger(__name__)
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        custom_logger.addHandler(console)
        folder_path = os.path.dirname(*args)
        if folder_path:
            os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist
        filehandler = logging.FileHandler(*args)
        filehandler.setFormatter(formatter)
        custom_logger.addHandler(filehandler)
        custom_logger.info(result)
        return custom_logger


@CustomLoggerDecorator
def custom_logger(*args):
    return 3 + 5


if __name__ == "__main__":
    logger = custom_logger.logger
    logger.info("This is an info message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    logger.debug("This is a debug message")
    print(custom_logger('Logger/logfile.log'))
