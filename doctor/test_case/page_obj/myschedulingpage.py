from .basepage import Page
from selenium.webdriver.common.by import By
from .loginpage import LoginPage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MySchedulingPage(Page):
    '''
    我的排期页面
    '''

    url = '/slide/schedule'

    # 开始、结束时间
    scheduling_start_loc = (By.ID, 'applyStart')
    scheduling_end_loc = (By.ID, 'applyEnd')
    # 勾选服务类型（全部）
    scheduling_servicetype_loc = (By.XPATH, '//div[@class="serviceType flex"]/div[2]/ul/li[1]/span[1]')
    # 添加排期按钮
    scheduling_add_button_loc = (By.CLASS_NAME, 'addScheduleBtn')

    # # 成功/失败提示信息
    # scheduling_hint_loc = (By.XPATH, '//div[@class="bounceInDown"]')

    # 排期记录元素
    scheduling_record_spread_loc = (By.XPATH, '//div[@class="scheduleTime flex active"]')
    scheduling_record_unspread_loc = (By.XPATH, '//div[@class="scheduleTime flex"]')

    # 输入排期开始时间
    def scheduling_starttime(self, starttime):
        # 日期控件为readonly无法输入，这里通过js去掉readonly属性然后再输入日期
        js = 'document.getElementById("applyStart").removeAttribute("readonly");'
        self.execute_script(js)
        # 先清除输入框的时间再输入
        self.find_element(*self.scheduling_start_loc).clear()
        return self.find_element(*self.scheduling_start_loc).send_keys(starttime)

    # 输入排期结束时间
    def scheduling_endtime(self, endtime):
        # 日期控件为readonly无法输入，这里通过js去掉readonly属性然后再输入日期
        js = 'document.getElementById("applyEnd").removeAttribute("readonly");'
        self.execute_script(js)
        # 先清除输入框的时间再输入
        self.find_element(*self.scheduling_end_loc).clear()
        return self.find_element(*self.scheduling_end_loc).send_keys(endtime)

    # 勾选服务类型为全部
    def scheduling_servicetype(self):
        return self.find_element(*self.scheduling_servicetype_loc).click()

    # 点击添加排期按钮
    # 因为添加排期按钮被时间下拉菜单遮住，直接使用click()方法会报错找不到元素，因此这里使用js模拟点击按钮
    def scheduling_add_button(self):
        element = self.find_element(*self.scheduling_add_button_loc)
        js = ("arguments[0].click()", element)
        self.execute_script(*js)

    # # 登录成功/失败提示
    # def scheduling_hint(self):
    #     try:
    #         ss = WebDriverWait(self.driver, 5, 0.01).until(EC.presence_of_element_located(self.scheduling_hint_loc))
    #         js = ("arguments[0].getAttribute('innerHTML')", ss)
    #         print("....", self.execute_script(*js))     # 打印出来是null，无法作为验证
    #         return True
    #     except TimeoutError:
    #         return False

    # 统计排期记录数量,通过排期前后的排期记录数量对比来判断添加排期是否成功
    def scheduling_record(self):
        spread_record = len(self.find_elements(*self.scheduling_record_spread_loc))
        unspread_record = len(self.find_elements(*self.scheduling_record_unspread_loc))
        all_spread_record = spread_record + unspread_record
        return all_spread_record

    # 统一添加排期操作
    def add_scheduling(self, starttime, endtime):
        # 先登录
        login = LoginPage(self.driver)
        login.user_login()
        # 再打开我的排期页面
        self.open(self.url)
        before_scheduling = self.scheduling_record()
        # 然后执行排期操作
        # 这里先勾选服务类型再填时间，因先填时间的话会出现下拉菜单，下拉菜单会挡住服务类型控件导致勾选服务类型失败
        self.scheduling_servicetype()
        self.scheduling_starttime(starttime)
        self.scheduling_endtime(endtime)
        self.scheduling_add_button()
        time.sleep(5)
        after_scheduling = self.scheduling_record()

        return before_scheduling == after_scheduling - 1


