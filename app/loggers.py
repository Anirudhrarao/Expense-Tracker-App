import logging

def setup_logger():
    """
    Set up logger for tracking app activities and errors
    """
    logger = logging.getLogger("BudgetTrackerApp")
    logger.setLevel(logging.INFO)
    # Create a file handler
    file_handler = logging.FileHandler("app.log")
    file_handler.setLevel(logging.INFO)
    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    # Add the handlers to the logger
    logger.addHandler(file_handler)

    return logger
