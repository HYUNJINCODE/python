


from selenium import webdriver
options = webdriver.ChromeOptions()
options.headless =True
options.add_argument("window-size=1920x1080")
browser =webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
#모니터의 해상도높이 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,1080)")
# browser.execute_script("window.scrollTo(0,2080)")

#화면 가장아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

import time
interval =2 #2초에 한번씩 스크롤 내림

#현재 문서 높이를 가져와서 저장
prev_height =  browser.execute_script("return document.body.scrollHeight")

#반복 수행
while True:
    #스크롤 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    #페이지 로딩 대기
    time.sleep(interval)
    #현재문서 높이를 가져와서 저장
    curr_height =  browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height
print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")


import requests
from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies/top"
# headers ={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
#     ,"Accept-Language":"ko-KR,ko"    
# }

res = requests.get(url)
res.raise_for_status
soup = BeautifulSoup(browser.page_source,"lxml")


# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc","Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})

print(len(movies))

# with open("movie.html","w",encoding="utf8") as f:
#     #f.write(res.text) 더럽게나옴
#     f.write(soup.prettify()) # html 문서를 이쁘게 출력

for movie in movies:
    title =movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title)
    #할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title,"  <할인되지 않은 영화 제외>")
        continue
    #할인 된 가격
    price = movie.find("span",attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    #링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    #올바른 링크: https://play.google.com + link

    print(f"제목 :{title}")
    print(f"할인 전 금액: {original_price}")
    print(f"할인 후 금액: {price}")
    print("링크: ","https://play.google.com" + link)
    print("-"*120)

browser.quit()
