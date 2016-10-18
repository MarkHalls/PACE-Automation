import pyautogui

pyautogui.PAUSE = 0.50
pyautogui.FAILSAFE = True
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("C:/projects/test.png")),clicks=400,interval=0.009)
