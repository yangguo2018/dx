import unittest
from doctor.test_case.models import myunit, screenshot
from doctor.test_case.page_obj import logoutpage


class LogoutTest(myunit.MyTest):
    def test_01(self):
        """退出登录用例"""
        lo = logoutpage.LogoutPage(self.driver)
        self.assertTrue(lo.logout_button())
        screenshot.insert_img(self.driver, self.test_01.__doc__)
        # 关闭浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
