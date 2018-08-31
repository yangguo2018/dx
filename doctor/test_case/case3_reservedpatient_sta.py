from doctor.test_case.models import myunit, screenshot
from doctor.test_case.page_obj import reservedpatientpage


class ReservedPatientTest(myunit.MyTest):
    # # 医生未排期用例
    # def test_no_reservedpatient(self):
    #     lo = reservedpatientpage.ReservedPatient(self.driver)
    #     lo.open_page()
    #     self.assertTrue(lo.is_element_exist('loadding'))
    #     filename = '预约患者列表为空' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
    #     screenshot.insert_img(self.driver, filename)

    def test_01(self):
        """预约患者列表用例"""
        lo = reservedpatientpage.ReservedPatient(self.driver)
        lo.open_page()
        self.assertTrue(lo.is_element_exist('patientDetail'))
        screenshot.insert_img(self.driver, self.test_01.__doc__)

    def test_02(self):
        """点击查看详情用例"""
        lo = reservedpatientpage.ReservedPatient(self.driver)
        lo.open_page()
        lo.view_details_button()
        self.assertIn('共预约', lo.view_details_success())
        screenshot.insert_img(self.driver, self.test_02.__doc__)


