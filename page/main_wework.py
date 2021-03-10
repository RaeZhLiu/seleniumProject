from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from page.add_member import AddMember
from page.basePage import BasePage


class MainWework(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()

    def goto_add_member(self):
        # 定位到 添加成员, 使用显示等待
        # self.wait_for_click((By.CSS_SELECTOR, ".ww_operationBar:nth-child(1)>.js_add_member"))
        # 显示等待，使用自己写的条件
        def wait_main_condition(x):
            elements_len = len(self.finds(By.CSS_SELECTOR, '.js_invite_member'))
            if elements_len <= 0:
                self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')

            return elements_len > 0
        self.wait_for_ele(wait_main_condition)
        self.find(By.CSS_SELECTOR, ".ww_operationBar:nth-child(1)>.js_add_member").click()
        return AddMember(self._driver)