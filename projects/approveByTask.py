import csv
import pyautogui

pyautogui.PAUSE = 0.50
pyautogui.FAILSAFE = True


#**************************************
#         Update these values
#**************************************

taskCode = "RE020"
csvPath = "c:\projects\reforecast.csv"

#**************************************



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


def submitDates(taskCode, path):
    allBlocks = parseBlocks(path)

    for index, block in enumerate(allBlocks):
        print("\nApproving Task Code:", taskCode, '\n')
        print(', '.join(block), '\n\n')
        print("Group", index + 1, "of", len(allBlocks), '\n')

        click('C:/projects/images/jobsearchfield.png', "Job Search Field")
        pyautogui.typewrite(', '.join(block))

        click('C:/projects/images/searchButton.png',   "Search Button")
        click('C:/projects/images/selectalljobs.png',  "Select All Jobs")
        click('C:/projects/images/next.png',           "Next Button")
        click('C:/projects/images/taskcodefilter.png', "Task Code Filter")

        click('C:/projects/images/isequalto.png', "Is Equal To")
        pyautogui.typewrite(taskCode)

        click('C:/projects/images/filterbutton.png',     "Filter Button")
        click('C:/projects/images/promoteselectall.png', "Promote Checkbox")
        click('C:/projects/images/submitbutton.png',     "Submit button")
        click('C:/projects/images/okbutton.png',         "OK button")
        click('C:/projects/images/returntohome.png',     "Back Button")


if __name__ == '__main__':
    submitDates(taskCode, csvPath)
