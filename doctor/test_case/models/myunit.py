from .drivers import browser
import unittest
from package import log
from doctor.test_case.page_obj.loginpage import LoginPage

"""
定义MyTest类继承unittest.TestCase类，将重复执行的setUp()、tearDown()方法抽象为MyTest类
"""


class MyTest(unittest.TestCase):
    logger = log.Log()
    driver = browser('Chrome')
    login = LoginPage(driver)

    @classmethod
    def setUpClass(cls, logger=logger, driver=driver, login=login):
        cls.logger = logger
        cls.driver = driver
        cls.logger.info("############################### START ###############################")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        # 用户登录
        cls.login.user_login()

    @classmethod
    def tearDownClass(cls):
        cls.logger.info('###############################  End  ###############################')