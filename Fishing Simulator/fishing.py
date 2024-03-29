import keyboard
import pyautogui
import pyscreeze
from PIL import ImageGrab


def recognizeDesiredColor(desiredColor, width: int, height: int):
    px = ImageGrab.grab().load()

    for y in range(int(height * (1 / 3)), int(height * (2 / 3)), 5):
        for x in range(int(width * (1 / 3)), int(width * (2 / 3)), 5):
            if px[x, y] == desiredColor:
                pyautogui.click()
                return True


width = pyautogui.size()[0]
height = pyautogui.size()[1]
water_bubble = (68, 252, 234)
lava_bubble = (178, 0, 209)

while True:
    if keyboard.is_pressed('k'):
        quit()

    if recognizeDesiredColor(water_bubble, width, height) or recognizeDesiredColor(lava_bubble, width, height):
        while pyautogui.pixelMatchesColor(1120, 840, (251, 98, 76)):
            if pyscreeze.pixelMatchesColor(900, 820, (255, 255, 255)):
                pyautogui.click(clicks=2, interval=0.05)

            if pyscreeze.pixelMatchesColor(830, 835, (255, 255, 255)):
                pyautogui.click(clicks=2, interval=0.05)

        pyautogui.sleep(0.5)
        pyautogui.click()
