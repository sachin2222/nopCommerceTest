import pytest

from Utils.BaseFile import BaseClass


class Testpractice(BaseClass):

    def test_function_demo(self):
        print("Demo Function")
        log = self.get_Logger("practice.log")

        log.info("{},{}".format("sachin", 10))
