import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status
#문제있으면 프로그램 종료시킴


soup = BeautifulSoup(res.text, "lxml")
#우리가 가져온 html문서를 lxml 파서를 통해서 뷰티풀수프 객체로 만듬

# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a["href"])

# print(soup.find("a",attrs={"class":"Nbtn_upload"}))
    