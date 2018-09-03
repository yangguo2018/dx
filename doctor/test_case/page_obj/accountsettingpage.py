from .basepage import Page
from selenium.webdriver.common.by import By
import time


class AccountSettingPage(Page):
    url = '/slide/account/user-info'

    # 个人信息页面 我的简介字段和输入框、提交信息按钮
    user_profile_tab_loc = (By.XPATH, '//div[@class="item"]/a[1]')
    user_profile_loc = (By.XPATH, '//div[@class="conten"]/div[4]/span')
    user_profile_text_loc = (By.XPATH, '//div[@class="conten"]/div[4]/div/textarea')
    submit_information_button_loc = (By.CLASS_NAME, 'but')

    # 资质认证页面 真实姓名字段，修改资料按钮
    qualification_certification_tab_loc = (By.XPATH, '//div[@class="item"]/a[2]')
    user_real_name_loc = (By.XPATH, '//div[@class="center"]/div[3]/span[2]')
    modify_infomation_button_loc = (By.XPATH, '//div[@class="but isNext-button"]')

    # 服务类型页面
    service_type_tab_loc = (By.XPATH, '//div[@class="item"]/a[3]')
    service_type_text_loc = (By.XPATH, '//div[@class="service"]/P')

    # 星级积分页面 积分规则按钮
    integral_rule_tab_loc = (By.XPATH, '//div[@class="item"]/a[4]')
    integral_rule_text_loc = (By.CLASS_NAME, 'cursor')

    # 修改密码页面 登录密码、新密码、确认密码输入框，修改密码按钮
    modify_password_tab_loc = (By.XPATH, '//div[@class="item"]/a[5]')
    old_password_loc = (By.XPATH, '//div[@class="Avatar"]/input')
    new_password_loc = (By.XPATH, '//div[@class="conten"]/div[3]/div[1]/input')
    again_password_loc = (By.XPATH, '//div[@class="conten"]/div[3]/div[2]/input')
    modify_password_button_loc = (By.CLASS_NAME, 'but')
    # 修改密码提示信息
    modify_password_hint_loc = (By.XPATH, '//div[@class="tishi"]/span')

    # 个人信息页面
    # 我的简介字段,用于断言
    def user_profile(self):
        return self.find_element(*self.user_profile_loc).text

    # 我的简介输入框
    def user_profile_text(self, text):
        return self.find_element(*self.user_profile_text_loc).send_keys(text)

    # 提交信息
    def submit_information_button(self):
        return self.find_element(*self.submit_information_button_loc).click()

    # 资质认证页面
    # 切换至资质认证Tab
    def qualification_certification_tab(self):
        return self.find_element(*self.qualification_certification_tab_loc).click()

    # 真实姓名字段，用于断言
    def user_real_name(self):
        return self.find_element(*self.user_real_name_loc).text

    # 修改资料按钮
    def modify_infomation_button(self):
        # 这里直接return True，后期补充
        # return self.find_element(*self.modify_infomation_button_loc).click()
        return True

    # 服务类型页面
    # 切换至服务器型Tab
    def service_type_tab(self):
        return self.find_element(*self.service_type_tab_loc).click()

    # 页面文案，用于断言
    def service_type_text(self):
        return self.find_element(*self.service_type_text_loc).text

    # 星级积分页面
    # 切换至星级积分页面
    def integral_rule_tab(self):
        return self.find_element(*self.integral_rule_tab_loc).click()

    # 页面文案，用于断言
    def integral_rule_text(self):
        return self.find_element(*self.integral_rule_text_loc).text

    # 修改密码页面
    # 切换至修改密码页面
    def modify_password_tab(self):
        return self.find_element(*self.modify_password_tab_loc).click()

    # 提示信息
    def modify_password_hint(self):
        return self.find_element(*self.modify_password_hint_loc).text

    # 登录密码
    def old_password(self, old_pwd):
        return self.find_element(*self.old_password_loc).send_keys(old_pwd)

    # 新密码
    def new_password(self, new_pwd):
        return self.find_element(*self.new_password_loc).send_keys(new_pwd)

    # 确认密码
    def again_password(self, again_pwd):
        return self.find_element(*self.again_password_loc).send_keys(again_pwd)

    # 修改密码按钮
    def modify_password_button(self):
        return self.find_element(*self.modify_password_button_loc).click()

    # #######################################################
    # 打开个人信息页面
    def open_user_profile(self):
        return self.open(self.url)

    # 输入我的简介 并提交信息
    def submit_information(self, text):
        self.open_user_profile()
        self.user_profile_text(text)
        self.submit_information_button()

    # 整合修改密码流程
    def modify_password(self, old_pwd='111111', new_pwd='123456', again_pwd='123456'):
        # 打开个人信息页面
        self.open_user_profile()
        # 切换至修改密码Tab
        self.modify_password_tab()
        time.sleep(1)
        # 输入登录密码、新密码、确认密码、点击修改密码按钮
        self.old_password(old_pwd)
        self.new_password(new_pwd)
        self.again_password(again_pwd)
        self.modify_password_button()
        time.sleep(3)
