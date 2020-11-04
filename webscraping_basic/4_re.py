#regular expression

# 주민등록번호
# 990110-1111111
# abcdef-111111
# 올바르지않은주민등록번호
# 이메일주소
# adfaf@gmail. com

# 차량번호
# 11가 1234
#123가 1234
#ip주소
#192.168.0.1


import re
#abcd, book, desk
# 4글자
#3개만기억나
#ab?d
#abad,abbd,abcd,abdd
p= re.compile("ca.e")  #.은 하나의 문자를 의미
# ^: 문자열의 시작을 의미
# ^de  desk , destination
# $ 문자열의 끝
# (se$) case , base

m = p.match("case")

print(m.group())

if m:
    print(m.group())
else:
    print("매칭 안됨")


def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")


#match 는 처음 부터 일치하는지 확인 (주어진 문자열)


#re.compile
#p로받고
#m = p.match("")