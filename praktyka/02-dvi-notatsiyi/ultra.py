from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import UltrasonicSensor

# Датчики та мотори
ultra = UltrasonicSensor(INPUT_2)
tank = MoveTank(OUTPUT_A, OUTPUT_B)

# Їхати вперед, поки перешкода далі ніж 15 см
tank.on(30, 30)

while ultra.distance_centimeters > 15:
    pass

# Зупинити робота
tank.off()
