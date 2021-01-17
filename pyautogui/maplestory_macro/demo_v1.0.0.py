import pyautogui
import random
import time
import cv2

img = cv2.imread('moveA.png')
moveToA = pyautogui.locateOnScreen(img)
print(moveToA)
# A =pyautogui.locateCenterOnScreen('moveA.png')
# pyautogui.click(A)
# pyautogui.mo