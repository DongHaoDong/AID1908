# 导入selenium的webserver接口
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.binary_location = r"D:\Chrome\Application\chrome.exe"
# 1. 创建浏览器对象 - 打开浏览器
browser = webdriver.Chrome(chrome_options=options)
# 2. 地址栏输入百度地址
browser.get('http://www.baidu.com/')
# 1. 在搜索矿中输入赵丽颖 //*[@id="kw"]
kw_input = browser.find_element_by_xpath('//*[@id="kw"]')
kw_input.send_keys('赵丽颖')
# 2. 点击按钮 百度一下 //*[@id="su"]
su_button = browser.find_element_by_xpath('//*[@id="su"]')
su_button.click()
# 3. 停留5秒
time.sleep(5)
# 4. 关闭浏览器
browser.quit()