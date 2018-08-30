import unittest
from doctor.test_case.models import myunit, screenshot
from doctor.test_case.page_obj import myschedulingpage
import time


class MyScheduling(myunit.MyTest):
    def test_add_scheduling_success(self):
        """成功添加排期用例"""
        lo = myschedulingpage.MySchedulingPage(self.driver)
        ss = lo.add_scheduling('19:30', '20:00')
        self.assertTrue(ss)
        filename = '添加排期成功' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
        screenshot.insert_img(self.driver, filename)

    def test_add_scheduling_fail1(self):
        """排期时间已存在用例"""
        lo = myschedulingpage.MySchedulingPage(self.driver)
        ss = lo.add_scheduling('19:30', '20:00')
        self.assertFalse(ss)
        filename = '排期时间已存在' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
        screenshot.insert_img(self.driver, filename)

    def test_add_scheduling_fail2(self):
        """排期时间在当前时间之前用例"""
        lo = myschedulingpage.MySchedulingPage(self.driver)
        ss = lo.add_scheduling('7:30', '8:00')
        self.assertTrue(ss)
        filename = '排期时间在当前时间之前' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
        screenshot.insert_img(self.driver, filename)


if __name__ == '__main__':
    unittest.main()
