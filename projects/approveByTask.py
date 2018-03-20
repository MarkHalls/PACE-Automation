import csv
import pyautogui

pyautogui.PAUSE = 0.50
pyautogui.FAILSAFE = True


def click(fullPathToImage, error):
    try:
        pyautogui.click(pyautogui.center(
            pyautogui.locateOnScreen(fullPathToImage)))
    except:
        print(error, " not found, trying again")
        click(fullPathToImage, error)


def parseBlocks(path):
    blockList = []
    with open(path, mode='r') as infile:
        reader = csv.reader(infile)
        rowIndex = 0
        block = []
        for row in reader:
            if rowIndex % 40 == 0:
                blockList.append(block)
                block = row
            else:
                block = block + row
            rowIndex += 1

        blockList.append(block)
        blockList = list(filter(bool, blockList))
    infile.close()
    return blockList


def start(taskCode, path):
    allBlocks = parseBlocks(path)

    for block in allBlocks:
        if allBlocks.index(block) + 1 != len(allBlocks):
            print("\nApproving Task Code:", taskCode, '\n')
            print(', '.join(block), '\n\n')
            print("Group", allBlocks.index(block) + 1,
                  "of", len(allBlocks), '\n')

            # click Job Search Field
            click('C:/projects/images/jobsearchfield.png', "Job Search Field")

            # type list of jobs to search for
            pyautogui.typewrite(', '.join(block))

            # click Search Button
            click('C:/projects/images/searchButton.png', "Search Button")

            # click Select All Jobs checkbox
            click('C:/projects/images/selectalljobs.png', "Select All Jobs")

            # click Next Button
            click('C:/projects/images/next.png', "Next Button")

            # click Filter Tasks
            click('C:/projects/images/taskcodefilter.png', "Task Code Filter")

            # click Equal to field
            click('C:/projects/images/isequalto.png', "Is Equal To")

            # Type taskcode into field
            pyautogui.typewrite(taskCode)

            # click filter button
            click('C:/projects/images/filterbutton.png', "Filter Button")

            # click Promote to Approve select all checkbox
            click('C:/projects/images/promoteselectall.png',
                  "Promote Checkbox")

            # click submit button
            click('C:/projects/images/submitbutton.png', "Submit button")

            # click Ok button
            click('C:/projects/images/okbutton.png', "OK button")

            # click return button
            click('C:/projects/images/returntohome.png', "Back Button")


if __name__ == '__main__':
    start("RE020", "C:/pathtocsv")
