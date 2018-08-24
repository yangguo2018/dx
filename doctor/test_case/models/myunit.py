from .driver import browser
import unittest
from package import log

"""
定义MyTest类继承unittest.TestCase类，将重复执行的setUp()、tearDown()方法抽象为MyTest类
"""


class MyTest(unittest.TestCase):
    def setUp(self):
        self.logger = log.Log()
        self.logger.info("############################### START ###############################")
        self.driver = browser('Chrome')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
        self.logger.info('###############################  End  ###############################')
