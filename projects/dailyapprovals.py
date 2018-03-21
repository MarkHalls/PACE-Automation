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


def click(fullPathToImage, name):
    try:
        pyautogui.click(pyautogui.center(
            pyautogui.locateOnScreen(fullPathToImage)))
    except:
        print(name, " not found, trying again")
        click(fullPathToImage, name)


def parseBlocks(path):
    blockList = []
    with open(path, mode='r') as infile:
        reader = csv.reader(infile)
        block = []
        for row in reader:
            block = block.append(row)
            if len(block) >= 40:
                blockList.append(block)
                block = []
        if len(block) > 0:
            blockList.append(block)
    infile.close()
    return blockList


for element in promote:
    if not i == len(promote):
        print("\nPromoting to Approve \nUsing 'Is Not Contained In' \nCI025, CI030, CI031, CI032, CI060, RE020, CI037, CI220\n")

        i += 1
        print("Group", i, " of ", len(promote), '\n')
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
        pyautogui.typewrite(
            "CI025, CI030, CI031, CI032, CI060, RE020, CI037, CI220")
        filterButton()
        promoteCheckbox()
        submit()
        okButton()
        returnToSearch()
f.close()
