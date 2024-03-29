import pyautogui
from PIL import ImageGrab


def recognizeRetryColor(desiredColor, width: int, height: int):
    px = ImageGrab.grab().load()

    for y in range(int(height * (1 / 3)), int(height * (3 / 4))):
        for x in range(0, width):
            if px[x, y] == desiredColor:
                if len(retry_pos) == 0:
                    retry_pos.append([x, y])
                return True


def recognizeBossColor(desiredColor, width: int, height: int):
    px = ImageGrab.grab().load()

    for y in range(int(height * (1 / 3)), int(height * (3 / 4))):
        for x in range(0, width):
            if px[x, y] == desiredColor:
                if len(boss_pos) == 0:
                    boss_pos.append([x, y])
            return True


width = pyautogui.size()[0]
height = pyautogui.size()[1]
retry = (130, 59, 41)
boss = (42, 94, 30)
retry_pos = []
boss_pos = []

while True:

    if recognizeRetryColor(retry, width, height) and recognizeBossColor(boss, width, height):
        pyautogui.moveTo(boss_pos[0][0], boss_pos[0][1], 1)
        pyautogui.click(clicks=2, interval=0.5)

    elif recognizeRetryColor(retry, width, height) and not recognizeBossColor(boss, width, height):
        pyautogui.moveTo(retry_pos[0][0], retry_pos[0][1], 1)
        pyautogui.click(clicks=2, interval=0.5)
