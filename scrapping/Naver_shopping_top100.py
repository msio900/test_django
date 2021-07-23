from selenium import webdriver

browser = webdriver.Chrome('../../chromedriver.exe')
browser.get('https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000006')

html = browser.page_source

browser.close()
browser.quit()