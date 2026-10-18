import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#bot 
computer =[rock, paper, scissors]
chosing = random.choice(computer)


user = input("[Rock, Paper, Scissors]:  ")

#rock for user
if user == "Rock":
  print(f"You choice {rock}")
  print(f"Computer choice {chosing}")
  if chosing == rock:
    print("Draw")
  elif chosing == paper:
    print("Computer win")
  elif chosing == scissors:
    print("user win")


#Paper for user
elif user == "Paper":
  print(f"You choice {paper}")
  print(f"Computer choice {chosing}")
  if chosing == rock:
    print("User win")
  elif chosing == paper:
    print("Draw")
  elif chosing == scissors:
    print("Computer win")


#Scissors for user
elif user == "Scissors":
  print(f"You choice {user}")
  print(f"Computer choice {chosing}")
  if chosing == rock:
    print("Computer win! ")
  elif chosing == paper:
    print("User win!")
  elif chosing == scissors:
    print("DRAW!")
