import time
from selenium import webdriver

browser = webdriver.Chrome() #"./chromedriver.exe"
browser.get("http://naver.com")
#1.네이버로이동

#2.네이버 로그인버튼클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3.id pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")
#4로그인버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)
# 5 id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6 html 정보 출력
print(browser.page_source)

# 7브라우저 종료
#browser.close() 현재탭만종료
browser.quit()