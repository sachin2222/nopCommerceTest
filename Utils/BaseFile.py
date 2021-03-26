import inspect
import logging

import pytest


@pytest.mark.usefixtures("setup", "login")
class BaseClass:

    def click_element_by_getText(self, values, textvalue, log):
        log.info("{},{}".format("Length of this List:", len(values)))
        for value in values:
            log.info(value.text)
            if value.text == textvalue:
                value.click()
                break

    def verify_customer(self, customer_list, customer, log):
        log.info("{},{}".format("Length of this List:", len(customer_list)))
        for c in customer_list:
            if c.text == customer:
                return True
            else:
                return False

    def get_Logger(self, logFilePath):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        file_handler = logging.FileHandler(logFilePath)

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
