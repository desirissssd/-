threshold = 70

tank_drive.on(15, 15)

while color_sensor_in1.reflected_light_intensity >= threshold:
    pass

tank_drive.off()
