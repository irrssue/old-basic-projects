print("Welcome to the rollercoster")
height = int(input("Please enter your height in feet(only contain int):  "))
legal_height = int(5)
young_age = int(12)
middle_age = int(15) 
older_age = int(180)

if height >= legal_height:
    print("You may enter please choose your age and ticket")
    age = int(input("How old are U?:  "))

    if age <= young_age:
        print(f"Your ticket fee is 8$ due yo your age {age}")
    
    elif age >= middle_age:
        print(f"Your ticket fee is 10$ due to your age {age}")

    elif age >= older_age:
        print(f"Your ticket fee is 12$ due to your age is {age}")
else:
    print(f"You can't due to your height is {height} feet enter please comeback again when you grow up")
 
