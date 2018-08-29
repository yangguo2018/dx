import unittest
from doctor.test_case.models import myunit, screenshot
from doctor.test_case.page_obj import myschedulingpage
import time


class MyScheduling(myunit.MyTest):
    # 添加排期
    def test_add_scheduling_success(self):
        lo = myschedulingpage.MySchedulingPage(self.driver)
        ss = lo.add_scheduling('18:30', '19:00')
        self.assertTrue(ss)
        filename = '添加排期成功' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
        screenshot.insert_img(self.driver, filename)


if __name__ == '__main__':
    unittest.main()
