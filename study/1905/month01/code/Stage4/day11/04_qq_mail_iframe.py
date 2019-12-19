'''iframe'''
from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = r"D:\Chrome\Application\chrome.exe"

browser = webdriver.Chrome(chrome_options=options)
browser.get('https://mail.qq.com/')
# 1. 切换到iframe子框架
login_frame = browser.find_element_by_id('login_frame')
browser.switch_to.frame(login_frame)
# 2. 找节点:用户名+密码+登录
user = browser.find_element_by_id('u').send_keys('')
pwd = browser.find_element_by_id('p').send_keys('')
login = browser.find_element_by_id('login_button').click()
