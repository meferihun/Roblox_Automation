import pyautogui
from PIL import ImageGrab
import pygetwindow as pw
import time


def recognizeBubbleColor(desiredColors, width: int, height: int):
    px = ImageGrab.grab(bbox=(left, top, right, bottom)).load()

    for y in range(int(height * (1 / 4)), int(height * (3 / 4)), 10):
        for x in range(int(width * (1 / 3)), width, 10):
            for desiredColor in desiredColors:
                if px[x, y] == desiredColor:
                    pyautogui.click()
                    return True


for i in range(0, 4):
    time.sleep(1)

window = pw.getWindowsWithTitle('Roblox')[0]

top = window.top + 9 if window.top < 0 else window.top
left = window.left + 9 if window.left < 0 else window.left

bottom = window.bottom - 10 if window.bottom > 1080 else window.bottom
right = window.right - 10 if window.right > 1920 else window.right

width = window.width - 20 if window.width > 1920 else window.width
height = window.height - 20 if window.height > 1080 else window.height

water_bubble = (68, 252, 234)
lava_iced_bubble = (178, 0, 209)
lava_bubble = (253, 95, 10)
alien_bubble = (51, 238, 18)
void_bubble = (129, 109, 192)
bubbles = [water_bubble, lava_bubble, lava_iced_bubble, alien_bubble, void_bubble]

fishing_bar = (251, 98, 76)

fishing_bar_cords = []

while True:
    if pw.getWindowsWithTitle('Roblox')[0].width != width:
        window = pw.getWindowsWithTitle('Roblox')[0]

        top = window.top + 9 if window.top < 0 else window.top
        left = window.left + 9 if window.left < 0 else window.left

        bottom = window.bottom - 10 if window.bottom > 1080 else window.bottom
        right = window.right - 10 if window.right > 1920 else window.right

        width = window.width - 20 if window.width > 1920 else window.width
        height = window.height - 20 if window.height > 1080 else window.height

        fishing_bar_cords = []

    if recognizeBubbleColor(bubbles, width, height):
        if len(fishing_bar_cords) == 0:
            px = ImageGrab.grab(bbox=(left, top, right, bottom)).load()

            class Found(Exception):
                pass

            try:
                for y in range(int(height * 0.7), height):
                    for x in range(int(width * 0.5), int(width * 0.7)):
                        if px[x, y] == fishing_bar:
                            raise Found
            except Found:
                fishing_bar_cords = [x, y+5]

        while pyautogui.pixelMatchesColor(fishing_bar_cords[0], fishing_bar_cords[1], fishing_bar):
            if pyautogui.pixelMatchesColor(fishing_bar_cords[0] - 190, fishing_bar_cords[1] - 10, (255, 255, 255)):
                pyautogui.click(clicks=1, interval=0.1)

            if pyautogui.pixelMatchesColor(fishing_bar_cords[0] - 260, fishing_bar_cords[1] - 10, (255, 255, 255)):
                pyautogui.click(clicks=1, interval=0.1)

        pyautogui.sleep(0.4)
        pyautogui.click()
