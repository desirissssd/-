for count in range(4):
    pen_in5.down()
    tank_drive.on_for_seconds(20, 20, 3)
    tank_drive.on_for_rotations(20, (-20), 0.7)
