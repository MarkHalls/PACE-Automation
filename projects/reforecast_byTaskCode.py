#This program accepts csv files stored
#in c:\projects\forecastdate.csv in the form of "PTN,Date"
#Author: Mark Halls
#Last update: 7/19/16

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


def start():
    #with open('c:/projects/csv/forecastDate.csv', mode='r') as infile:
    with open(r'\\CASNDG1CDFILE02.ITServices.sbc.com\DSW_Mobility_CE\Processes\PACE/forecastDates.csv', mode='r') as infile:
        reader = csv.reader(infile)
        data = list(reader)
        #print(data)
        infile.close()
        taskCodeList = []
        for ptn, taskCode, forecast in data:
            taskCodeList.append(taskCode)
        tList = list(set(filter(bool, taskCodeList)))
        
        print("\nTotal PTNs to update:",len(taskCodeList))
        print("All Task Codes Parsed")
        print(tList, '\n')
        

        #starting counter value for the code group list
        codeGroupValue = 1

        #filter data by task code. runs a loop that takes the first task code, creates a list of all dates assigned to that code and then reforecasts the dates by PTN
        for tcode in tList:            
            l = 1
            #list that stores all date values
            forecastDate = []

            #loop through the data looking for the task code (tcode) in this batch. add all the dates that it finds to the forecastDate list
            for ptn, taskCode, forecast in data:
                if taskCode == tcode:
                    forecastDate.append(forecast)
            #new list that removes duplicates from the forecastDate list
            dateList = list(set(filter(bool, forecastDate)))

            dateCount = 1
            #loop through the dates and add all the ptns that match the task code and date into the ptnList list. 
            for forecastd in dateList:
                ptnList = []
                newPtn = []
                i = 0
                #splits ptns out into batches of 40 to be processed. creates lists of up to 40 items
                for ptn, taskCode, forecast in data:
                    if taskCode == tcode:                        
                        if forecastd == forecast:
                            if i % 75 == 0:
                                ptnList.append(newPtn)
                                newPtn = []                    
                            newPtn.append(ptn)
                            i += 1
                ptnList.append(newPtn)
                #print(ptnList)
                
                #removes any duplicates from the ptnList if they exist
                ptnList = list(filter(bool, ptnList))
                i = 0

                #pyautogui loop that processes job. loops for every value in ptnList, pulls in the task code (tcode) value and the date
                for element in ptnList:
                    #your code to update forecast here
                    if i != len(ptnList):
                        i += 1
                        print("\n\tTask Code",tcode,",Group",codeGroupValue,"of", len(tList))
                        #print("\nReforecasting Taskcode:",tcode)
                        print("\n\tProcessing dates for task code",tcode,dateCount,"finished of", len(dateList))
                        print("\n\tDate",forecastd,",Group",i,"of", len(ptnList), '\n')
                        print(', '.join(element), '\n\n')
                        
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
                        pyautogui.typewrite(tcode)
                        
                        #click filter button
                        click('C:/projects/images/filterbutton.png', "Filter Button")
                        
                        #click Select All checkbox
                        click('C:/projects/images/selectalltasks.png', "Select All Tasks checkbox")
                        
                        #click Update Selected Tasks button
                        click('C:/projects/images/updateselectedtasks.png', "Update Selected Tasks button")
                        
                        #click Forecast date field
                        click('C:/projects/images/updateforecastfield.png', "Update Forecast field")
                        
                        #type date
                        pyautogui.typewrite(forecastd)
                        
                        #input("Press Enter to continue...")

                        #click Apply button
                        click('C:/projects/images/applyforecastbutton.png', "Apply button")
                        
                        #click Promote to Approve select all checkbox
                        click('C:/projects/images/promoteselectall.png', "Promote Checkbox")
                        
                        #input("Press Enter to continue...")

                        #click submit button
                        click('C:/projects/images/submitbutton.png', "Submit button")
                        
                        #click Ok button
                        click('C:/projects/images/okbutton.png', "OK button")
                        
                        #click return button
                        click('C:/projects/images/returntohome.png', "Back Button")
                l += 1
                dateCount += 1
            codeGroupValue += 1
            


if __name__ == '__main__':
    start()















    
