from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    driver = webdriver.Chrome()
    # 实例化ActionChains对象  模拟鼠标操作
    # actions = ActionChains(driver)
    # url = r'file:///Users/liuzhihui/PycharmProjects/seleniumProject/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html'
    # driver.maximize_window()
    # driver.get(url)
    #
    # user = driver.find_element_by_id("userA")
    # user.send_keys("admin")
    # time.sleep(2)
    # # 调用右键方法并执行
    # # actions.context_click(user).perform()
    # actions.double_click().perform()

    # url1 = r'file:///Users/liuzhihui/PycharmProjects/seleniumProject/%E7%B4%A0%E6%9D%90/drag.html'
    # driver.maximize_window()
    # driver.get(url1)
    #
    # pos1 = driver.find_element_by_id("div1")
    # pos2 = driver.find_element_by_id("div2")
    #
    # actions.drag_and_drop(pos1, pos2).perform()

    # url2 = r'https://www.dogedoge.com/'
    # driver.maximize_window()
    # driver.get(url2)
    # time.sleep(3)
    #
    # pos = driver.find_element_by_xpath('//*[@id="search_button_homepage"]')
    # actions.move_to_element(pos).perform()

    # 模拟键盘操作
    url3 = r'http:www.baidu.com'
    driver.get(url3)
    driver.maximize_window()
    time.sleep(2)

    search = driver.find_element_by_id("kw")
    search.send_keys("什么是你好")
    time.sleep(2)
    search.send_keys(Keys.BACK_SPACE)

    time.sleep(1)
    driver.quit()


if __name__ == '__main__':
    main()



