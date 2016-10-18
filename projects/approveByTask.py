#This program accepts csv files stored
#in c:\projects\approvebytask.csv in the form of "PTN,Date"
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

pyautogui.PAUSE = 0.50
pyautogui.FAILSAFE = True


#click function requires arguments ('fullPathToImage', "Error Identifier")
def click(fullPathToImage, error):
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(fullPathToImage)))
    except:
        print(error, " not found, trying again")
        click(fullPathToImage, error)


def start(taskCode):
    with open('c:/projects/csv/approvebytask.csv', mode='r') as infile:
        reader = csv.reader(infile)
        i = 0
        promote = []
        newRow = []
        for row in reader:
            if i % 40 == 0:
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
            #your code to update forecast here
            if i != len(promote):
                print("\nApproving Task Code:", taskCode, '\n')
                print(', '.join(element), '\n\n')
                i += 1
                print("Group",i,"of", len(promote), '\n')
                
                #click Job Search Field
                click('C:/projects/images/jobsearchfield.png', "Job Search Field")

                #type list of jobs to search for
                pyautogui.typewrite(', '.join(element))

                #click Search Button
                click('C:/projects/images/searchButton.png', "Search Button")

                #click Select All Jobs checkbox
                click('C:/projects/images/selectalljobs.png', "Select All Jobs")

                #click Next Button
                click('C:/projects/images/next.png', "Next Button")

                #click Filter Tasks
                click('C:/projects/images/taskcodefilter.png', "Task Code Filter")
                
                #click Equal to field
                click('C:/projects/images/isequalto.png', "Is Equal To")
                
                #Type taskcode into field
                pyautogui.typewrite(taskCode)

                #click filter button
                click('C:/projects/images/filterbutton.png', "Filter Button")
                                   
                #click Promote to Approve select all checkbox
                click('C:/projects/images/promoteselectall.png', "Promote Checkbox")
                
                #input("Press Enter to continue...")

                #click submit button
                click('C:/projects/images/submitbutton.png', "Submit button")
                
                #click Ok button
                click('C:/projects/images/okbutton.png', "OK button")
                
                #click return button
                click('C:/projects/images/returntohome.png', "Back Button")
                          
    infile.close()

if __name__ == '__main__':
    start("RE020")















    
