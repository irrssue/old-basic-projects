import random

print("""                     
 __     __     ______     __         ______     ______     __    __     ______    
/\ \  _ \ \   /\  ___\   /\ \       /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   
\ \ \/ ".\ \  \ \  __\   \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  __\   
 \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\ 
  \/_/   \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/  \/_/   \/_____/ 
                                                                                  

""")
      
print(f"Ok take a guess I'm think a number between 1 and 100")
GUESS_NUMBER = random.randint(1,100+1)

while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        attempts = 10
        break
    elif difficulty == "hard":
        attempts = 5
        break
    else:
        print("Invalid difficulty level. Please choose 'easy' or 'hard'.")


while attempts > 0:
    print(f"You have {attempts} attamps to guess the number")
    guess = int(input("Enter your guess: "))
    if guess == GUESS_NUMBER:
        print("""
           ┌─┐┬ ┬ 
╚╦╝│ ││ │  ║║║││││
 ╩ └─┘└─┘  ╚╩╝┴┘└┘

        """)
        quit()
    elif guess > GUESS_NUMBER:
        if guess - GUESS_NUMBER > 10:  
          print("Too high")
        elif guess - GUESS_NUMBER < 5:
            print("You are in close range 5")
        else:
            print("You are in clsoe range 10")
          

    elif guess < GUESS_NUMBER:
        if GUESS_NUMBER - guess >10:
          print("Too Low")
        elif GUESS_NUMBER - guess < 5:
            print("You are in close range 5")
        else:
            print("You are in close range 10")

    attempts-=1
print("Game over you run out of attamps")
