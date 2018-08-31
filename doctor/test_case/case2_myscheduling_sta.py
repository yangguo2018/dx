import unittest
from doctor.test_case.models import myunit, screenshot
from doctor.test_case.page_obj import myschedulingpage


class MyScheduling(myunit.MyTest):
    def test_01(self):
        """成功添加排期用例"""
        lo = myschedulingpage.MySchedulingPage(self.driver)
        ss = lo.add_scheduling('19:30', '20:00')
        self.assertTrue(ss)
        screenshot.insert_img(self.driver, self.test_01.__doc__)

    def test_02(self):
        """排期时间已存在用例"""
        lo = myschedulingpage.MySchedulingPage(self.driver)
        ss = lo.add_scheduling('19:30', '20:00')
        self.assertFalse(ss)
        screenshot.insert_img(self.driver, self.test_02.__doc__)

    def test_03(self):
        """排期时间在当前时间之前用例"""
        lo = myschedulingpage.MySchedulingPage(self.driver)
        ss = lo.add_scheduling('7:30', '8:00')
        self.assertFalse(ss)
        screenshot.insert_img(self.driver, self.test_03.__doc__)

    def test_04(self):
        """排期开始时间大于结束时间用例"""
        lo = myschedulingpage.MySchedulingPage(self.driver)
        ss = lo.add_scheduling('22:30', '22:00')
        self.assertFalse(ss)
        screenshot.insert_img(self.driver, self.test_04.__doc__)

    # def test_add_scheduling_fail4(self):
    #     """排期时间在当前时间14天后用例"""
    #     pass    # 没想好怎么实现


if __name__ == '__main__':
    unittest.main()
