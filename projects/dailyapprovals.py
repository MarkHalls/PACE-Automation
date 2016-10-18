# reads ptn's from c:/projects/csv/approvals.csv, accepts only a single column of ptn's
# needs reference images in c:/projects/images
# Author: Mark Halls
# Last Update: 3/18/16

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

pyautogui.PAUSE = 0.50
pyautogui.FAILSAFE = True

coorSearchField = 0
coorSearchButton = 0
coorFilterButton = 0
coorPromoteCheckbox = 0

def jobSearchField():
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('C:/projects/images/jobsearchfield.png')))
    except:
        print("Job Search Field not found, trying again.")
        jobSearchField()
    
def jobSearchButton():
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('C:/projects/images/searchButton.png')))
    except:
        print("Search Button not found, trying again.")
        jobSearchButton()

def selectAllJobs():
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('C:/projects/images/selectalljobs.png')))
    except:
        print("Select All Jobs greyed out, trying again.")
        selectAllJobs()

def clickNext():
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('C:/projects/images/next.png')))
    except:
        print("Next Button greyed out, trying again.")
        clickNext()

def taskFilter():
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('C:/projects/images/taskcodefilter.png')))
    except:
        print("Could not find Task Code Filter, trying again.")
        taskFilter()        

def filterDropDown():
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('C:/projects/images/filterdropdown.png')))
    except:
        print("Could not find Filter Dropdown, trying again.")
        filterDropDown()        

def selectIsNotContainedIn():
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('C:/projects/images/selectisnotcontainedin.png')))
    except:
        print("Could not find Is Not Contained In, trying again.")
        selectIsNotContainedIn()    

def isNotContainedInFilter():
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('C:/projects/images/isnotcontainedinfilter.png')))
    except:
        print("Could not find Is Not Contained In filter field, trying again.")
        isNotContainedInFilter()        
        
def filterButton():
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('C:/projects/images/filterbutton.png')))
    except:
        print("Filter Button not found, trying again.")
        filterButton()

def promoteCheckbox():
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('C:/projects/images/promoteselectall.png')))
    except:
        print("Promote Checkbox not found, trying again.")
        promoteCheckbox()        
        
def submit():
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('C:/projects/images/submitbutton.png')))
    except:
        print("Could not find Submit button, trying again.")
        submit()

def okButton():
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('C:/projects/images/okbutton.png')))
    except:
        print("Could not find OK button, trying again.")
        okButton()
        
def returnToSearch():
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('C:/projects/images/returntohome.png')))
    except:
        print("Could not find Back Button, trying again")
        returnToSearch()
        
        
with open("c:/projects/csv/approvals.csv") as f:
    reader = csv.reader(f)
    i = 0
    promote = []
    newRow = []
    for row in reader:
        if i % 75 == 0:
            promote.append(newRow)
            newRow = row
            #print("1 newlistpromote") 
        else:
            newRow = newRow + row
            #print(len(newRow))
        i = i + 1
    i = 0
    promote.append(newRow)
    promote = list(filter(bool, promote))
    #print(promote)
    #print(len(promote))
    for element in promote:
        if not i == len(promote):
            print("\nPromoting to Approve \nUsing 'Is Not Contained In' \nCI025, CI030, CI031, CI032, CI060, RE020, CI037, CI220\n")
            
            i += 1
            print("Group",i," of ", len(promote), '\n')
            print(', '.join(element), '\n\n')
            
            jobSearchField()
            pyautogui.typewrite(', '.join(element))
            jobSearchButton()
            selectAllJobs()
            clickNext()
            taskFilter()
            filterDropDown()
            selectIsNotContainedIn()
            isNotContainedInFilter()
            pyautogui.typewrite("CI025, CI030, CI031, CI032, CI060, RE020, CI037, CI220")
            filterButton()
            promoteCheckbox()
            submit()
            okButton()
            returnToSearch()
    f.close()
    
    
