from selenium import webdriver
import time
# browser = webdriver.Chrome()
# browser.get("http://www.baidu.com")
# time.sleep(4)
# ele = browser.find_elements_by_xpath('//*[@id="kw"]')[0].send_keys("python")
# print(ele)

br = webdriver.Chrome()
br.get("http://www.mogumiao.com/web")
time.sleep(10)
print(br.page_source)


