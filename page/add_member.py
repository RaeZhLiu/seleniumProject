from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page.basePage import BasePage
from time import sleep


class AddMember(BasePage):
    def add_member(self, name, passwd, phone):
        self.wait_for_click((By.ID, "username"))
        # 开始输入必填项
        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(passwd)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_member_editor_form>div:nth-child(3)>.js_btn_save").click()

    def update_page(self):
        page_info: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text

        return [int(x) for x in page_info.split('/', 1)]

    def get_member(self, value):
        # 显示等待，使用自带判断条件
        self.wait_for_click((By.CSS_SELECTOR, '.member_colRight_memberTable_th_Checkbox'))
        # 使用自定义显示等待条件
        # def wait_add_condition(x):
        #     elements_len = len(self.finds(By.CSS_SELECTOR, '.js_invite_member'))
        #     if elements_len <= 0:
        #         self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text')
        #
        #     return elements_len > 0
        # self.wait_for_ele(wait_add_condition)
        cur_page, sum_page = self.update_page()
        while True:
            elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            for element in elements:
                attribute = element.get_attribute("title")
                if value == attribute:
                    return True
            if cur_page != sum_page:
                self.find(By.CSS_SELECTOR, '.js_next_page').click()
                cur_page = self.update_page()[0]
                # 需要改进，改为显示等待，自设条件
                sleep(1)
            else:
                return False
