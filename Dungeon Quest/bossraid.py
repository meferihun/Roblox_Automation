import time
from directkeys import PressKey, ReleaseKey, E, Q
from keyboard import is_pressed

for i in range(0, 4):
    time.sleep(1)

paused = False

while True:
    if is_pressed("k"):
        if paused:
            paused = False
            print("It's running again!")
        else:
            paused = True
            print("It got paused!")

    if not paused:
        PressKey(E)
        ReleaseKey(E)
        PressKey(Q)
        ReleaseKey(Q)
        time.sleep(7)

