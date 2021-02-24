# 导入selenium包
from selenium import webdriver
import time


def main():
    # 1. 创建chrome浏览器的webdriver实例
    driver = webdriver.Chrome()

    # 浏览器操作
    driver.maximize_window()
    # driver.set_window_size(100, 100)
    # driver.set_window_position(300, 200)

    url = r"file:///Users/liuzhihui/PycharmProjects/seleniumProject/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html"
    # 2. 打开指定url
    driver.get(url)
    try:
        # 3. 调用指定元素定位方式
        # 3.1 id 元素定位方式
        # user = driver.find_element_by_id("userA")
        # pwd = driver.find_element_by_id("passwordA")
        # 3.2 name 元素定位方式
        # user = driver.find_element_by_name("userA")
        # pwd = driver.find_element_by_name("passwordA")
        # 3.3 class_name 元素定位方式
        # phone = driver.find_element_by_class_name("telAHHH")
        # # 3.4 tag_name 元素定位方式及 多目标时选择方式  elements返回的是列表
        # user = driver.find_element_by_tag_name("input")
        # pwd = driver.find_element_by_tag_name("input")
        # res_list = driver.find_elements_by_tag_name("input")
        # user = res_list[0]
        # pwd = res_list[1]
        # 3.5 link_text 超链接文本定位方式
        # baidu = driver.find_element_by_link_text("AA 百度 网站")
        # 3.6 partial_link_text 超链接模糊定位方式
        # baidu = driver.find_element_by_partial_link_text("AA")
        # 3.7 xpath 定位方法  绝对路径, 相对路径:标签+属性，元素属性，层级+属性，层级+逻辑
        user = driver.find_element_by_xpath("/html/body/form/div/fieldset/p/input")
        pwd = driver.find_element_by_xpath("//input[@id='passwordA']")
        phone = driver.find_element_by_xpath("//*[@id='telA']")
        user1 = driver.find_element_by_xpath("//*[@id='p1']/input")
        email = driver.find_element_by_xpath("//*[@name='emailA' and @id='emailA']")
        # baidu = driver.find_element_by_xpath("//*[text()='AA 百度 网站']")
        # 3.8 css 定位方法   "# = id", ". = class", ""
        # user = driver.find_element_by_css_selector("#userA")
        # # pwd = driver.find_element_by_css_selector("fieldset p input#passwordA")
        # pwd = driver.find_element_by_css_selector("[type=password]")
        # phone = driver.find_element_by_css_selector(".telAHHH")
        time.sleep(1)
        # 4. 使用send_keys() 发送数据, 元素操作方法 clear:清除, send_keys:模拟输入, click: 单机
        user.send_keys("admin")
        pwd.send_keys("123456")
        phone.send_keys("11111111111")
        user1.clear()
        user1.send_keys("adminx")
        # email.send_keys("xxx@163.com")
        # baidu.click()
    except Exception as e:
        print(e)
    finally:
        time.sleep(1)
        driver.quit()


if __name__ == "__main__":
    main()
