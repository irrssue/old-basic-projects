
print("welcome to tip calculator")
money = input("Total amount $?:  ")
percentage = input("what percentage tip would you like to give?:  ")
people = input("How many people to split the bill:  ")

#finding the percentage 

change_to_percentage = float(percentage) / 100 
the_final = float(money) * change_to_percentage

the_percentage_money = float(money) + the_final

# time to split between peoples 

done = the_percentage_money / int(people)

ending = round(done, 2)

print(f"Each person should pay {ending}$")
