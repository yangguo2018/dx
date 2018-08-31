import unittest
from doctor.test_case.models import screenshot
from doctor.test_case.page_obj import loginpage
from package import log
from doctor.test_case.models.myunit import MyTest


class LoginTest(unittest.TestCase):
    """
    1、因为封装的myunit.MyTest中加入了登录操作并且默认登录成功，为防止冲突，登录测试类直接继承unittest.TestCase
    2、其他测试类则继承myunit.MyTest，这样只需要每个测试类登录一次而不用每个case都登录一次。
    3、这里的driver调用的myunit.MyTest的driver保证使用同一对象，否则重新创建一个driver对象的话会导致运行时启动两个浏览器
    """

    def setUp(self):
        self.driver = MyTest.driver
        self.logger = log.Log()
        self.logger.info("############################### START ###############################")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.logger.info('###############################  End  ###############################')

    def test_01(self):
        """用户名密码均为空用例"""
        lo = loginpage.LoginPage(self.driver)
        lo.user_login(username='', password='')
        self.assertEqual(lo.login_error_hint(), ' 请输入手机号')
        screenshot.insert_img(self.driver, self.test_01.__doc__)

    def test_02(self):
        """用户名或密码输入错误用例"""
        lo = loginpage.LoginPage(self.driver)
        lo.user_login(username='15500000000')
        self.assertEqual(lo.login_error_hint(), ' 用户名或密码错误')
        screenshot.insert_img(self.driver, self.test_02.__doc__)

    def test_03(self):
        """用户不存在用例"""
        lo = loginpage.LoginPage(self.driver)
        lo.user_login(username='19999999999')
        self.assertEqual(lo.login_error_hint(), ' 此用户不存在')
        screenshot.insert_img(self.driver, self.test_03.__doc__)

    def test_04(self):
        """登录成功用例"""
        lo = loginpage.LoginPage(self.driver)
        lo.user_login()
        self.assertEqual(lo.login_success(), '谢医生')
        screenshot.insert_img(self.driver, self.test_04.__doc__)


# if __name__ == '__main__':
#     unittest.main()
