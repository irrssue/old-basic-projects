print("Welcome to the LOVE calculator")
name1 = input("What is your name? \n")
name2 = input("What is your crush name? \n")

lower_case = name1 + name2
lower_case.lower()

# for t
t = lower_case.count("t")

r = lower_case.count("r")

u = lower_case.count("u")

e = lower_case.count("e")
true = (t+r+u+e)
str_true = str(true)

l = lower_case.count("l")

o = lower_case.count("o")

v = lower_case.count("v")

e = lower_case.count("e")
love = (l+o+v+e)
str_love = str(love)

calculate =(str_true+ str_love)
calculate1 = int(calculate)

if calculate1 >= 90 or calculate1 <= 10:
    print(f"Your score is {calculate}, You go together like coke and mentos")

elif calculate1 <= 40 or calculate1 >= 50:
    print(f"Your score is {calculate1}, You are alright together")
