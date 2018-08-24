from selenium import webdriver
# from selenium.webdriver import Remote
import time
from package import log


# 定义浏览器驱动函数，根据传参启动不同的浏览器
def browser(browsername):
    logger = log.Log()
    if browsername == 'Chrome':
        driver = webdriver.Chrome()
    elif browsername == 'FireFox':
        driver = webdriver.Firefox()
    elif browsername == 'IE':
        driver = webdriver.Ie()
    else:
        print("输入有误，目前只支持Chrome,FireFox,IE浏览器！")
    logger.info("{0} Start a new browser: {1}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), browsername))
    return driver

    # # 多线程分布式启动
    # host = '127.0.0.1:4444'     # 运行主机：端口号 （本机默认：127.0.0.1:4444）
    # dc = {'browserName': browsername}      # 指定浏览器
    # driver = Remote(command_executor='http://' + host + '/wd/hub', desired_capabilities=dc)
    # return driver


if __name__ == '__main__':
    dr = browser('Chrome')
    dr.maximize_window()
    dr.get('https://qa-doctor.dr-elephant.com/index')
    dr.quit()

