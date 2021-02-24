import keyGetter as kg
import Control as ct
from djitellopy import tello

kg.init()

# 初期化
drone = tello.Tello()
drone.connect()

print(drone.get_battery())

drone.streamoff()
drone.streamon()

# 飛行中かどうか
isFlying = 0


while True:
    inputs = ct.getKeyboardInput(isFlying)

    isFlying = inputs[4]
    drone.send_rc_control(inputs[0], inputs[1], inputs[2], inputs[3])
    sleep(0.01)
