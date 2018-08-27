import unittest
from doctor.test_case.models import myunit, screenshot
from doctor.test_case.page_obj import reservedpatientpage
import time


class ReservedPatientTest(myunit.MyTest):
    # # 医生未排期用例
    # def test_no_reservedpatient(self):
    #     lo = reservedpatientpage.ReservedPatient(self.driver)
    #     lo.open_page()
    #     self.assertTrue(lo.is_element_exist('loadding'))
    #     filename = '预约患者列表为空' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
    #     screenshot.insert_img(self.driver, filename)

    # 预约患者列表用例
    def test_reservedpatient(self):
        lo = reservedpatientpage.ReservedPatient(self.driver)
        lo.open_page()
        self.assertTrue(lo.is_element_exist('patientDetail'))
        filename = '预约患者列表用例' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
        screenshot.insert_img(self.driver, filename)

    # 点击“查看详情”用例
    def test_viewdetails(self):
        lo = reservedpatientpage.ReservedPatient(self.driver)
        lo.open_page()
        lo.view_details_button()
        print(lo.view_details_success())
        self.assertIn('共预约', lo.view_details_success())
        filename = '点击查看详情用例' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
        screenshot.insert_img(self.driver, filename)


