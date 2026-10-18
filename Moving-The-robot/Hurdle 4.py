
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#def robot():
#    move()
#   turn_left()
#    move()
#    turn_rigth()
#    move()
#    turn_rigth()
#    move()
#    turn_left()
    
def situation():
    turn_left()
    while wall_on_right():
        move()
        
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
        
    turn_left()
    


while not at_goal():
    if wall_in_front():
        situation()
    else:
        move()
