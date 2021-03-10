import shelve

from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.chrome.options import Options


class TestLogin(object):
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_login_cookie(self):
        # print(self.driver.get_cookies())
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        db = shelve.open("cookies")
        # db["cookie"] = self.driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:
            if "expiry" in cookie:
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_link_text("通讯录").click()
        sleep(3)
        db.close()


if __name__ == '__main__':
    pytest.main(["-v", "-s", "login_wechat_cookies.py"])
