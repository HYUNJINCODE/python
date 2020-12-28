import pyautogui
pyautogui.screenshot('find.png',region=(619,152, 50,50))
find = pyautogui.locateCenterOnScreen('find.png')
pyautogui.click(find)