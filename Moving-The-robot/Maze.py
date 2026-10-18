# this is turn right fun
def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
# definding the robot to move then stick with the right side
def use_when_right_is_clear():
    turn_right()
    move()

def use_when_front_is_clear():
    move()
    
def use_when_left_is_clear():
    turn_left()



while not at_goal():
    if right_is_clear():
        use_when_right_is_clear()
        
    elif front_is_clear():
        use_when_front_is_clear()
    else:
        use_when_left_is_clear()
