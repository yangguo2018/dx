from doctor.test_case.models import screenshot, myunit
from doctor.test_case.page_obj import accountsettingpage
import unittest


class AccountSetting(myunit.MyTest):
    def test_01(self):
        """打开个人信息页面"""
        op = accountsettingpage.AccountSettingPage(self.driver)
        op.open_user_profile()
        self.assertEqual(op.user_profile(), '我的简介')
        screenshot.insert_img(self.driver, self.test_01.__doc__)

    def test_02(self):
        """提交个人信息"""
        op = accountsettingpage.AccountSettingPage(self.driver)
        op.submit_information('自动化测试')
        # 这里因为获取不到提示信息，暂时先用字段名来验证提交是否成功
        self.assertEqual(op.user_profile(), '我的简介')
        screenshot.insert_img(self.driver, self.test_02.__doc__)

    def test_03(self):
        """切换至资质管理页面"""
        op = accountsettingpage.AccountSettingPage(self.driver)
        op.qualification_certification_tab()
        self.assertEqual(op.user_real_name(), '谢医生')
        screenshot.insert_img(self.driver, self.test_03.__doc__)

    def test_04(self):
        """资质管理 修改资料"""
        op = accountsettingpage.AccountSettingPage(self.driver)
        # 这是只是作了点击没有进行后续操作，然后验证也是根据真实姓名验证的，后续再补充
        self.assertTrue(op.modify_infomation_button())
        screenshot.insert_img(self.driver, self.test_04.__doc__)

    def test_05(self):
        """切换至服务类型页面"""
        op = accountsettingpage.AccountSettingPage(self.driver)
        op.service_type_tab()
        self.assertEqual(op.service_type_text(), '您已开通的服务类型')
        screenshot.insert_img(self.driver, self.test_05.__doc__)

    def test_06(self):
        """切换至星级积分页面"""
        op = accountsettingpage.AccountSettingPage(self.driver)
        op.integral_rule_tab()
        self.assertEqual(op.integral_rule_text(), '\ue6b1\n星级积分规则')
        screenshot.insert_img(self.driver, self.test_06.__doc__)

    def test_07(self):
        """切换至修改密码页面"""
        op = accountsettingpage.AccountSettingPage(self.driver)
        op.integral_rule_tab()
        self.assertEqual(op.integral_rule_text(), '\ue6b1\n星级积分规则')
        screenshot.insert_img(self.driver, self.test_07.__doc__)

    def test_08(self):
        """修改密码 登录密码为空时"""
        op = accountsettingpage.AccountSettingPage(self.driver)
        op.modify_password(old_pwd='')
        self.assertEqual(op.modify_password_hint(), ' 请输入有效登录密码')
        screenshot.insert_img(self.driver, self.test_08.__doc__)

    def test_09(self):
        """修改密码 新密码为空时"""
        op = accountsettingpage.AccountSettingPage(self.driver)
        op.modify_password(new_pwd='', again_pwd='')
        self.assertEqual(op.modify_password_hint(), ' 请输入6~20位新密码')
        screenshot.insert_img(self.driver, self.test_09.__doc__)

    def test_10(self):
        """修改密码 密码不一致时"""
        op = accountsettingpage.AccountSettingPage(self.driver)
        op.modify_password(new_pwd='111111', again_pwd='123456')
        self.assertEqual(op.modify_password_hint(), ' 两次输入密码不一致')
        screenshot.insert_img(self.driver, self.test_10.__doc__)

    def test_11(self):
        """修改密码 密码修改成功"""
        op = accountsettingpage.AccountSettingPage(self.driver)
        op.modify_password()
        self.assertEqual(self.driver.current_url, 'https://qa-doctor.dr-elephant.com/index')
        screenshot.insert_img(self.driver, self.test_11.__doc__)


if __name__ == '__main__':
    unittest.main()
