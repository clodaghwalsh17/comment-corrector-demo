lives = 10
collide = False
power_up = False
# game loop
while lives > 0:
    # decrease lives
    if collide and not power_up:
        lives -= 1