import logging

# To print test case name in login we pass the __name__ -> It tells what type of error is caused and on which step
# if not given __name__ it will print root
def test_loggingDemo():
    logger = logging.getLogger(__name__)


    # Different loggers
    fileHandler = logging.FileHandler('logfile.log') # filehandler knows now where the logfile will be printed
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s") # Formatting how information to be printed
    fileHandler.setFormatter(formatter) # setting the formatter applying to fileHandler
    logger.addHandler(fileHandler) # adding the handler to logger
    logger.setLevel(logging.INFO) # setting the level as from INFO

    logger.debug("A debug statement is executed")
    logger.info("Informtion")
    logger.warning("Something is in warning mode")
    logger.error("A major error")
    logger.critical("Critical Issue")


# After execution the log file will be created and you can see at what time and everthing you can see
