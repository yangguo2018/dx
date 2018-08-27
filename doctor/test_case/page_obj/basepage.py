import time

class Page(object):
    '''
    页面基类，用于所有页面的继承
    '''

    doctor_url = 'https://qa-doctor.dr-elephant.com'

    def __init__(self, selenium_driver, base_url=doctor_url, parent=None):
        self.driver = selenium_driver
        self.base_url = base_url
        self.parent = parent
        self.timeout = 30

    # 重定义get()方法
    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        time.sleep(3)
        assert self.driver.current_url == url, 'Do not land on %s' % url

    # 重定义find_element()方法
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 重定义find_elements()方法
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 重定义execute_script()方法
    def script(self, src):
        return self.driver.execute_script(src)
