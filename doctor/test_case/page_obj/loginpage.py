from .basepage import Page
from selenium.webdriver.common.by import By
import time


class LoginPage(Page):
    '''
    用户登录页面
    '''

    url = '/index'

    # username,password,button元素属性
    login_username_loc = (By.NAME, "username")
    login_password_loc = (By.ID, "pass")
    login_button_loc = (By.CLASS_NAME, "but")

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一的登录入口
    def user_login(self, username='13916725407', password='123456'):
        self.open(self.url)
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        time.sleep(5)

    # 错误提示的元素 = (By.XPATH, "//div[@class='error-text']/span")
    login_error_hint_loc = (By.XPATH, "//div[@class='error-text']/span")
    # 成功后用户名称元素属性，依此验证登录成功
    login_success_loc = (By.CLASS_NAME, "userName")

    # 登录报错提示
    def login_error_hint(self):
        return self.find_element(*self.login_error_hint_loc).text

    # 登录成功用户名称
    def login_success(self):
        return self.find_element(*self.login_success_loc).text
