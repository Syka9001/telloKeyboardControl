import keyGetter as kg
from djitellopy import tello
from time import sleep

kg.init()

drone = tello.Tello()
drone.connect()


def getKeyboardInput(isFlying):
    lr, fb, ud, yw = 0, 0, 0, 0
    speed = 50

    # SPACE離陸・着陸
    if kg.getKey("SPACE"):
        if isFlying == 0:
            isFlying = 1
            drone.takeoff()
        else:
            isFlying = 0
            drone.land(); sleep(3)

    # T着陸・L離陸
    if kg.getKey("t"): drone.takeoff(); isFlying = 1
    if kg.getKey("l"): drone.land(); sleep(3); isFlying = 0

    # A左方向 B右方向
    if kg.getKey("a"):
        lr = -speed
    elif kg.getKey("d"):
        lr = speed

    # W前方 s後方
    if kg.getKey("s"):
        fb = -speed
    elif kg.getKey("w"):
        fb = speed

    # ↑上昇 ↓下降
    if kg.getKey("DOWN"):
        ud = -speed
    elif kg.getKey("UP"):
        ud = speed

    # ←左回り →右回り
    if kg.getKey("LEFT"):
        yw = -speed
    elif kg.getKey("RIGHT"):
        yw = speed

    return [lr, fb, ud, yw, isFlying]
