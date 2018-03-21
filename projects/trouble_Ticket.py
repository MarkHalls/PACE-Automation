import csv
import pyautogui

pyautogui.PAUSE = 0.50
pyautogui.FAILSAFE = True


def click(fullPathToImage, error):
    try:
        pyautogui.click(pyautogui.center(
            pyautogui.locateOnScreen(fullPathToImage)))
        pyautogui.moveRel(0, -150, duration=0)
        pyautogui.moveRel(50, 0, duration=0)
    except:
        print(error, " not found, trying again")
        click(fullPathToImage, error)


def createTicket():
    click('C:/projects/images/warroom/severity.png', "severity")
    click('C:/projects/images/warroom/majorseverity.png', "major")
    click('C:/projects/images/warroom/assigneddepartment.png', "depart")
    click('C:/projects/images/warroom/constructionandengineering.png', "constr")
    click('C:/projects/images/warroom/problemcategory.png', "category")
    click('C:/projects/images/warroom/3rdparty.png', "3rdparty")
    click('C:/projects/images/warroom/vendorvendor.png', "vendor")
    click('C:/projects/images/warroom/okbutton.png', "ok")
    click('C:/projects/images/warroom/911.png', "911")
    click('C:/projects/images/warroom/911yes.png', "911yes")
    click('C:/projects/images/warroom/vendortype.png', "vendortype")
    click('C:/projects/images/warroom/constructioncontract.png', "contract")
    click('C:/projects/images/warroom/technology.png', "tech")
    click('C:/projects/images/warroom/lte.png', "lte")


if __name__ == '__main__':
    createTicket()
