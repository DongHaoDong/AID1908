# 导入selenium的webserver接口
from selenium import webdriver
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.binary_location = r"D:\Chrome\Application\chrome.exe"

# 1. 打开浏览器+输入百度url+找到设置节点
browser = webdriver.Chrome(chrome_options=options)
browser.get('http://www.baidu.com')
set_node = browser.find_element_by_xpath('//*[@id="u1"]/a[8]')
# 2. 鼠标移动到设置节点
ActionChains(browser).move_to_element(set_node).perform()
# 3. 找高级搜索节点,并点击
browser.find_element_by_link_text('高级搜索').click()