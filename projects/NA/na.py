#Author: Mark Halls
#Last update: 3/10/16

# Required Packages:
# pip install send2trash
# pip install requests
# pip install beautifulsoup4
# pip install selenium
# pip install openpyxl
# pip install PyPDF2
# pip install python-docx (install python-docx, not docx)
# pip install imapclient
# pip install pyzmail
# pip install twilio
# pip install pillow
# pip install pyobjc-core (on OS X only)
# pip install pyobjc (on OS X only)
# pip install python3-xlib (on Linux only)
# pip install pyautogui

import csv
import pyautogui
import time

#pyautogui.PAUSE = 0.50
pyautogui.FAILSAFE = True


#click function requires arguments ('fullPathToImage', "Error Identifier")
def click(fullPathToImage, error):
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(fullPathToImage)))
    except:
        print(error, " not found, trying again")
        click(fullPathToImage, error)


def start():
    time.sleep(2)
    #click('C:/projects/NA/images/task.png',"task")
    click('C:/projects/NA/images/workflow.png',"workflow")
    click('C:/projects/NA/images/naButton.png',"Set to NA")
    click('C:/projects/NA/images/execute.png',"execute")
    click('C:/projects/NA/images/returntoregister.png',"return to register")
    #click('C:/projects/NA/images/refresh.png',"refresh")
    start()
    
if __name__ == '__main__':
    start()















    
