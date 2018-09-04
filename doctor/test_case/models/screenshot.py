import os
from selenium import webdriver
import time

"""
定义截图函数，图片保存至E:\PycharmProjects\SeleniumDoctor\doctor\\report\image目录
"""


def insert_img(driver, pic_name):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    filename = pic_name + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
    file_path = os.path.join(os.path.join(base_dir, 'report\image'), filename)
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qa-doctor.dr-elephant.com/index")
    time.sleep(2)
    insert_img(driver, 'test.png')
    driver.quit()
