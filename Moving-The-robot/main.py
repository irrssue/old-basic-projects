# move()
# move()
# turn_left()
# move()

def turn_rigth():
    turn_left()
    turn_left()
    turn_left()

def moving_the_robot():
    move()
    turn_left()
    move()
    turn_rigth()
    move()
    turn_rigth()
    move()
    turn_left()


# turn_rigth()

# move()
# turn_rigth()
# move()
# turn_left()

for steps in range(6):   
    moving_the_robot()

