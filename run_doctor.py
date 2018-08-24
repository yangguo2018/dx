from package import HTMLTestRunner, send_email
import os
import time
import unittest

case_url = os.path.join(os.path.dirname(__file__), 'doctor/test_case')
discover = unittest.defaultTestLoader.discover(case_url, pattern="*sta.py")

if __name__ == '__main__':
    report_dir = os.path.join(os.path.dirname(__file__), 'doctor/report')
    report_name = os.path.join('result' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.html')
    report_path = os.path.join(report_dir, report_name)
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试用例", description="用例执行情况")
    runner.run(discover)
    fp.close()
    # 发邮件
    send = send_email.SendMail()
    send.send_mail(report_path)
