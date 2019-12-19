# 导入selenium的webserver接口
from selenium import webdriver
import time

url = 'https://maoyan.com/board/4'
options = webdriver.ChromeOptions()
options.binary_location = r"D:\Chrome\Application\chrome.exe"
# 1. 创建浏览器对象 - 打开浏览器
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)
# 基准xpath
li_list = browser.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
for li in li_list:
    item = {}
    info_list = li.text.split('\n')
    item['number'] = info_list[0]
    item['name'] = info_list[1]
    item['star'] = info_list[2]
    item['time'] = info_list[3]
    item['score'] = info_list[4]
    print(item)

