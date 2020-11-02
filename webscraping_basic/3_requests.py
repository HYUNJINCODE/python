import requests
res = requests.get("http://google.com")
print("응답코드:", res.status_code)
#403 접근불가 
#status_code로 정상인지 판단

if res.status_code == requests.codes.ok:
    print("정상")
else:
    print("문제가 생겼습니다. [에러코드", res.status_code, "]")


res.raise_for_status()
#문제가 생기면 프로그램 끝냄

print("웹스크래핑을 진행합니다.")

print(len(res.text))
# print(res.text)

with open("mygoogle.html", "w", encoding= "utf8") as f:
    f.write(res.text)