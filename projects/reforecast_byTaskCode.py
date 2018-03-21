import os
import csv
import pyautogui

pyautogui.PAUSE = 0.50
pyautogui.FAILSAFE = True


sourceCSV = '/home/mh/github/PACE-Automation/projects/csv/forecastdate.csv'


def click(fullPathToImage, error):
    tries = 0
    while tries <= 100:
        try:
            pyautogui.click(pyautogui.center(
                pyautogui.locateOnScreen(fullPathToImage)))
        except:
            print(error, " not found, trying again")
            tries += 1


def readFile(path: str):
    with open(path, mode='r') as infile:
        reader = csv.reader(infile)
        data = list(reader)
        infile.close()
    return data


def parseCodes(data: list):
    return list(
        set(
            filter(bool, (
                map(lambda row: row[1], data)))))


def parseDatesByCode(code: str, data: list):
    codeRows = list(filter(lambda row: row[1] == code, data))
    return list(set(map(lambda row: row[2], codeRows)))


def parseBlocks(code: str, dateList: list, data: list):
    allBlocks = []
    for dates in dateList:
        block = []
        for ptn, taskCode, forecast in data:
            if forecast == dates and taskCode == code:
                row = [ptn, taskCode, forecast]
                block.append(row)
                if len(block) >= 40:
                    allBlocks.append(block)
        if len(block) > 0:
            allBlocks.append(block)
    # print(allBlocks, '\n')
    return allBlocks


def submitDates(blocks: list):
    for block in blocks:
        ptns = list(set(map(lambda row: row[0], block)))
        code = list(set(map(lambda row: row[1], block)))
        forecast = list(set(map(lambda row: row[2], block)))

        print("Task code: ".join(code), '\n')
        print("Date: ".join(forecast), '\n')
        print(', '.join(ptns), '\n')

        click(os.path.abspath('images/jobsearchfield.png'), "Job Search Field")
        pyautogui.typewrite(', '.join(ptns))

        click(os.path.abspath('images/searchButton.png'), "Search Button")
        click(os.path.abspath('images/selectalljobs.png'), "Select All Jobs")
        click(os.path.abspath('images/next.png'), "Next Button")
        click(os.path.abspath('images/taskcodefilter.png'), "Task Code Filter")

        click(os.path.abspath('images/isequalto.png'), "Is Equal To")
        pyautogui.typewrite(code)

        click(os.path.abspath('images/filterbutton.png'), "Filter Button")
        click(os.path.abspath('images/selectalltasks.png'),
              "Select All Tasks checkbox")
        click(os.path.abspath('images/updateselectedtasks.png'),
              "Update Selected Tasks button")

        click(os.path.abspath('images/updateforecastfield.png'),
              "Update Forecast field")
        pyautogui.typewrite(forecast)

        click(os.path.abspath('images/applyforecastbutton.png'), "Apply button")
        click(os.path.abspath('images/promoteselectall.png'),
              "Promote Checkbox")
        click(os.path.abspath('images/submitbutton.png'), "Submit button")
        click(os.path.abspath('images/okbutton.png'), "OK button")
        click(os.path.abspath('images/returntohome.png'), "Back Button")


def submitForecast(path: str):
    data = readFile(path)
    codes = parseCodes(data)

    print("\nTotal PTNs to update:", len(data))
    print(codes, '\n')

    for code in codes:
        dates = parseDatesByCode(code, data)
        blocks = parseBlocks(code, dates, data)
        submitDates(blocks)


if __name__ == '__main__':
    submitForecast(
        '/home/mh/github/PACE-Automation/projects/csv/forecastdate.csv')
