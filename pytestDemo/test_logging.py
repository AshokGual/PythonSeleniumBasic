import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandler  = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.WARNING)
    logger.debug("debugging executed")
    logger.info("test case information printed")
    logger.warning("warning messages printed")
    logger.error("error created")
    logger.critical("critical message printed")