import pyautogui
import time

pyautogui.position() # 내위치어디야?
# pyautogui.moveTo(10,34) # 여기로움직여
# pyautogui.moveTo(0,231,2) # 2초동안여기로움직여
# pyautogui.moveRel(0,300,2) #상대적으로 300내려가 relevant 
# pyautogui.click() # 그위치를 클릭한다.
# pyautogui.click(clicks=2, interval=2) #클릭하고 2초있다가 한번더 클릭
# pyautogui.doubleClick() #두번 클릭
#pyautogui.typewrite("hello") # hello 를 써라
#파일이 열리는 시간을 기다려야한다.

#time.sleep(1) 1초 쉬고 다음 문장실행

#pyautogui.typewrite(["enter"])
# enter 입력 괄호 중요 엔터키를 누른다로 정의

#pyautogui.typewrite(["a","b","c", "enter"])
#pyautogui.typewrite(["abc",'enter'])  #이문장은 abc는 못누르고 엔터는 누르기 가능