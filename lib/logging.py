import time, sys
from logging import Logger, Formatter, getLogger, FileHandler, StreamHandler, DEBUG
from types import TracebackType

__all__ = "init_logging", "logger"

def exception_logging(exc_type: type[BaseException], exc_value: BaseException, exc_traceback: TracebackType | None) -> None:
    logger.critical("Code exception occurred.", exc_info = exc_value)

def init_logging(name: str | None = None, level: str | int | None = None) -> Logger:
    formatter: Formatter = Formatter("[%(asctime)s] [%(levelname)-8s] %(message)s", datefmt = "%a, %d %b %Y %H:%M:%S")
    log_result: Logger = getLogger(name)

    if level is not None:
        log_result.setLevel(level)

    file_handler: FileHandler = FileHandler(f"logs/{name}-{time.strftime(f'%d-%b-%Y-%H-%M-%S', time.localtime())}.log")
    file_handler.setFormatter(formatter)
    log_result.addHandler(file_handler)

    console_handler: StreamHandler = StreamHandler()
    console_handler.setFormatter(formatter)
    log_result.addHandler(console_handler)

    return log_result

logger: Logger = init_logging(name = "JusticeLog", level = DEBUG)
sys.excepthook = exception_logging
