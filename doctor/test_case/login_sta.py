import unittest
from doctor.test_case.models import myunit, screenshot
from doctor.test_case.page_obj import loginpage
import time


class LoginTest(myunit.MyTest):
    # 用户名密码均为空用例
    def test_login_allnull(self):
        lo = loginpage.LoginPage(self.driver)
        lo.user_login(username='', password='')
        self.assertEqual(lo.login_error_hint(), ' 请输入手机号')
        filename = '用户名密码均为空用例' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
        screenshot.insert_img(self.driver, filename)

    # 用户名或密码输入错误用例
    def test_login_usererror(self):
        lo = loginpage.LoginPage(self.driver)
        lo.user_login(username='15500000000')
        self.assertEqual(lo.login_error_hint(), ' 用户名或密码错误')
        filename = '用户名或密码错误用例' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
        screenshot.insert_img(self.driver, filename)

    # 用户不存在用例
    def test_login_nousererror(self):
        lo = loginpage.LoginPage(self.driver)
        lo.user_login(username='19999999999')
        self.assertEqual(lo.login_error_hint(), ' 此用户不存在')
        filename = '用户不存在用例' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
        screenshot.insert_img(self.driver, filename)

    # 登录成功用例
    def test_login_success(self):
        lo = loginpage.LoginPage(self.driver)
        lo.user_login()
        self.assertEqual(lo.login_success(), '谢医生')
        filename = '登录成功用例' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
        screenshot.insert_img(self.driver, filename)


if __name__ == '__main__':
    unittest.main()
