import time

import keyboard
import pyautogui
from PIL import ImageGrab
from directkeys import ReleaseKey, PressKey, E


def recognizeDesiredColor(desiredColor, width: int, height: int):
    px = ImageGrab.grab().load()

    for y in range(int(height * (1 / 3)), int(height * (2 / 3)), 5):
        for x in range(int(width * (1 / 3)), int(width * (2 / 3)), 5):
            if px[x, y] == desiredColor:
                pyautogui.click()
                return True


for i in range(0, 4):
    time.sleep(1)

width = pyautogui.size()[0]
height = pyautogui.size()[1]
button = (89, 98, 101)

while True:
    if keyboard.is_pressed('k'):
        quit()

    if recognizeDesiredColor(button, width, height):
        PressKey(E)
        time.sleep(3)
        ReleaseKey(E)

        if pyautogui.pixelMatchesColor(620, 860, (84, 234, 52)):
            pyautogui.click(750, 860, 2)
