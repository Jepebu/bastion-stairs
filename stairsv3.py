from PIL import ImageGrab
import time
import pyautogui as pg
import keyboard
import os
import cv2 as cv
import timer
#layer 7 is y190-220
#layer 6 is y300-330
#layer 5 is y400-450
#layer 4 is y520-550
#layer 3 is y630-y660
#layer 2 is y740-y770
#layer 1 is y 850-y900



def screenGrab():
    layer1 = ImageGrab.grab(bbox = (0, 850, 1920, 900))
    layer2 = ImageGrab.grab(bbox = (0, 740, 1920, 770))
    layer3 = ImageGrab.grab(bbox = (0, 630, 1920, 660))
    layer4 = ImageGrab.grab(bbox = (0, 520, 1920, 550))
    layer5 = ImageGrab.grab(bbox = (0, 400, 1920, 450))
    layer6 = ImageGrab.grab(bbox = (0, 300, 1920, 330))
    layer7 = ImageGrab.grab(bbox = (0, 190, 1920, 220))
    layer1.save('layer1' +'.png', 'PNG')
    layer2.save('layer2' +'.png', 'PNG')
    layer3.save('layer3' +'.png', 'PNG')
    layer4.save('layer4' +'.png', 'PNG')
    layer5.save('layer5' +'.png', 'PNG')
    layer6.save('layer6' +'.png', 'PNG')
    layer7.save('layer7' +'.png', 'PNG')


def move():
    pg.press("space")

def switchToRight():
    pg.press("e")
    #pg.press("ctrlleft")


def switchToLeft():
    pg.press("e")
    #pg.press("ctrlleft")


def planMoves(maxloc,moveList,layerNum,previousX,maxval):
    x,y = maxloc
    layerNum = str(layerNum)
    if maxval > .85:
        if x >= (previousX + 75):
            moveList.append('right')
        elif x <= (previousX - 75):
            moveList.append('left')
        else:
            moveList.append(None)
    else:
        moveList.append(None)
    previousX = x
    return moveList, previousX


def main():
    time.sleep(5)
    facing = 'left'
    start = timer.start()
    totalMoves = 0
    while keyboard.is_pressed('q') == False:
        print("\n\n")
        previousX = 960
        screenGrab()
        stair = cv.imread("smallstair.png", cv.IMREAD_COLOR)
        layer1 = cv.imread("layer1.png", cv.IMREAD_COLOR)
        layer2 = cv.imread("layer2.png", cv.IMREAD_COLOR)
        layer3 = cv.imread("layer3.png", cv.IMREAD_COLOR)
        layer4 = cv.imread("layer4.png", cv.IMREAD_COLOR)
        layer5 = cv.imread("layer5.png", cv.IMREAD_COLOR)
        layer6 = cv.imread("layer6.png", cv.IMREAD_COLOR)
        layer7 = cv.imread("layer7.png", cv.IMREAD_COLOR)

        checkLayer1 = cv.matchTemplate(layer1, stair, cv.TM_CCOEFF_NORMED)
        checkLayer2 = cv.matchTemplate(layer2, stair, cv.TM_CCOEFF_NORMED)
        checkLayer3 = cv.matchTemplate(layer3, stair, cv.TM_CCOEFF_NORMED)
        checkLayer4 = cv.matchTemplate(layer4, stair, cv.TM_CCOEFF_NORMED)
        checkLayer5 = cv.matchTemplate(layer5, stair, cv.TM_CCOEFF_NORMED)
        checkLayer6 = cv.matchTemplate(layer6, stair, cv.TM_CCOEFF_NORMED)
        checkLayer7 = cv.matchTemplate(layer7, stair, cv.TM_CCOEFF_NORMED)


        checkList = [checkLayer1,checkLayer2,checkLayer3,checkLayer4,checkLayer5,checkLayer6,checkLayer7]
        layerNum = 1
        moveList = []
        for layer in checkList:
            minval, maxval, minloc, maxloc = cv.minMaxLoc(layer)
            moveList, previousX = planMoves(maxloc,moveList,layerNum,previousX,maxval)
            layerNum += 1
        moveNum = 0
        print(moveList)
        for moves in moveList:
            if moves == None:
                    break
            if moves == 'left' and facing == 'left':
                move()
                moveNum += 1

            elif moves == 'right' and facing == 'right':
                move()
                moveNum += 1

            elif moves == 'left' and facing == 'right':
                switchToLeft()
                facing = 'left'
                moveNum += 1

            elif moves == 'right' and facing == 'left':
                switchToRight()
                facing = 'right'
                moveNum += 1
        tempTotal = totalMoves
        totalMoves += moveNum
        print(totalMoves)
        time.sleep(.30)
    totalTime = timer.stop(start)

    print(totalTime/totalMoves)



if __name__ == '__main__':
    main()
