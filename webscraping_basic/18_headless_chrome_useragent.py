from selenium import webdriver

options =webdriver.ChromeOptions()
options.headless= True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36")
browser =webdriver.Chrome(options=options)
browser.maximize_window

url ="https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

#헤드리스 크롬을 쓰면 서버에서 막을 수도 있으니까 유저에이전트를 추가해서 쓰면 서버에서 안막음
#셀레늄with python 여기서 셀레늄 공부가능