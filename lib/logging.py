import logging, time

__all__ = "init_logging",

def init_logging() -> logging.Logger:
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)-8s] %(message)s", datefmt = "%a, %d %b %Y %H:%M:%S")
    logger = logging.getLogger(name = "JusticeLog")
    logger.setLevel(level = logging.DEBUG)

    file_handler = logging.FileHandler(f"logs/JusticeLog-{time.strftime(f'%a-%d-%b-%Y-%H-%M-%S', time.localtime())}.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


