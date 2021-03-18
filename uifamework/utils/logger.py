import logging
import logging.handlers


logger = logging.getLogger("MY_LOG")


def init_logger():
    logger.setLevel(logging.INFO)

    log_formatter = logging.Formatter("[%(asctime)s]  %(levelname)s %(filename)s:%(lineno)d:%(funcName)s  %(message)s")

    file_handler = logging.handlers.RotatingFileHandler("../logs/test_log.log", mode="a", backupCount=10,
                                                        encoding="utf-8")
    file_handler.setFormatter(log_formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


