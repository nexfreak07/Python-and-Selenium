import inspect
import logging
class BaseClass:
    def get_logger(self):
        loggerName = inspect.stack()[1][3] # To fix the file name that we get on the log file
        logger = logging.getLogger(loggerName)


        # Different loggers
        fileHandler = logging.FileHandler('logfile.log')  # filehandler knows now where the logfile will be printed
        formatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # Formatting how information to be printed
        fileHandler.setFormatter(formatter)  # setting the formatter applying to fileHandler
        logger.addHandler(fileHandler)  # adding the handler to logger
        logger.setLevel(logging.DEBUG)  # setting the level as from INFO

        logger.debug("A debug statement is executed")
        logger.info("Informtion")
        logger.warning("Something is in warning mode")
        logger.error("A major error")
        logger.critical("Critical Issue")
        return logger