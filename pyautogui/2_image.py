import pyautogui
#마우스와 키보드를 자동으로 조작
#좌표를 알려면
#pyautogui.position()
#pyautogui.moveTo(132,245,2)
#pyautogui.click(132,245) #그 자리로 가서 클릭


#화면에서 위치가 바뀌면 좌표를 알아내서 클릭하고싶다...

#pyautogui.locateOnScreen() 
# i =pyautogui.locateOnScreen('1.png')
# q = pyautogui.center(i)
#pyautogui.click(q)
#번거로운작업이다.따라서

#i =pyautogui.locateCenterOnScreen('1.png')
#pyautogui.click(i)


#화면에서 바로인식하려면????

#이미지를 만들때는 가로세로  네모낳게 

print(pyautogui.position())
# pyautogui.screenshot('1.png',region=(268,578,100,100))
