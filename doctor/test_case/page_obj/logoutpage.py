from .basepage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class LogoutPage(Page):
    '''
    用户登录页面
    '''

    url = '/slide/home'

    logout_loc = (By.XPATH, "//p[@class='powerSupply']")

    # 登录按钮
    def logout_button(self):
        # 打开主页
        self.open(self.url)
        try:
            self.find_element(*self.logout_loc).click()
            time.sleep(3)
            return True
        except NoSuchElementException:
            return False
