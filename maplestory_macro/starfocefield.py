import pyautogui
import random
import time
# A =pyautogui.locateOnScreen('./img/moveA.png')
# D =pyautogui.locateOnScreen('./img/moveD.png')
# AttackImg = pyautogui.locateOnScreen('./img/Attack.png')
# moveToA = pyautogui.center(A)
# moveToD = pyautogui.center(D)
# Attack = pyautogui.center(AttackImg)

pyautogui.click(1595,239)
# pyautogui.mouseDown(moveToA)

while True:
    pyautogui.keyDown('a')
    time.sleep(random.randint(5,15))
    # pyautogui.mouseUp()
    pyautogui.keyUp('a')
    pyautogui.keyDown('d')
    time.sleep(random.randint(5,15))
    pyautogui.keyUp('d')
    pyautogui.keyDown('f')
    pyautogui.keyUp('f')
    pyautogui.keyDown('f')
    pyautogui.keyUp('f')
    pyautogui.keyDown('f')
    pyautogui.keyUp('f')
    pyautogui.keyDown('f')
    pyautogui.keyUp('f')
   

    time.sleep(random.randint(1,5))
        

    
    
    # q = pyautogui.center(i)
#pyautogui.click(q)
#번거로운작업이다.따라서