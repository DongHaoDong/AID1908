# 导入selenium的webserver接口
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.binary_location = r"D:\Chrome\Application\chrome.exe"
# 1. 创建浏览器对象 - 打开浏览器
browser = webdriver.Chrome(chrome_options=options)
# browser = webdriver.PhantomJS()
# 2. 地址栏输入百度地址
browser.get('http://www.baidu.com/')
print(browser.page_source.find('kw'))
# 获取快照
# browser.save_screenshot('baidu.jpg')
# 3. 停留5秒
time.sleep(5)
# 4. 关闭浏览器
browser.quit()