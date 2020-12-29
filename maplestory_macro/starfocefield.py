import pyautogui
import random
import time
A =pyautogui.locateOnScreen('C:\\Users\\hyunjin\Desktop\\studypython\\maplestory_macro\\moveA.png')
D =pyautogui.locateOnScreen('./moveD.png')
AttackImg = pyautogui.locateOnScreen('./Attack.png')
moveToA = pyautogui.center(A)
moveToD = pyautogui.center(D)
Attack = pyautogui.center(AttackImg)
while True:
    
    pyautogui.mouseDown(moveToA)
    time.sleep(random.randint(1,5))
    pyautogui.mouseUp()
    pyautogui.click(Attack)
    pyautogui.click(Attack)
    pyautogui.click(Attack)
    time.sleep(random.randint(1,5))
    

    
    
    # q = pyautogui.center(i)
#pyautogui.click(q)
#번거로운작업이다.따라서