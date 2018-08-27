from .basepage import Page
from selenium.webdriver.common.by import By
from doctor.test_case.page_obj.loginpage import LoginPage


class ReservedPatient(Page):
    '''
    预约患者页面
    '''

    url = '/slide/patientAppointment'

    # 医生无排期时提示信息元素
    no_reservedpatient_loc = (By.CLASS_NAME, 'loadding')

    # 医生有排期时“查看详情”元素
    reservedpatient_loc = (By.CLASS_NAME, 'patientDetail')

    # 详情页的文案信息，用来验证成功打开详情页
    view_details_success_loc = (By.CLASS_NAME, 'p-color')

    # "查看详情"按钮
    def view_details_button(self):
        self.find_elements(*self.reservedpatient_loc)[0].click()
        print(len(self.find_elements(*self.reservedpatient_loc)))

    # 验证打开了详情页
    def view_details_success(self):
        return self.find_element(*self.view_details_success_loc).text


    # 判断元素是否存在
    def is_element_exist(self, element_value):
        if element_value == 'loadding':
            s = self.find_elements(*self.no_reservedpatient_loc)
            if len(s) == 0:
                return False
            elif len(s) == 1:
                return True
        elif element_value == 'patientDetail':
            s = self.find_elements(*self.reservedpatient_loc)
            if len(s) == 0:
                return False
            elif len(s) != 0:
                return True

    # 登录后打开预约患者页面
    def open_page(self):
        login = LoginPage(self.driver)
        login.user_login()
        self.open(self.url)

