# creating BMI calculator 
# Getting infos form users
print("Welcome to BMI calculator")
weight = input("Enter your weight in kg:  ")
height = input("Enteer your height in m:  ")

# calculate with BMI formula wight / height ** 2

calculate = float(weight) / ( float(height) **2 )
final = (round(calculate, 1))

# Chosing BMI levels with the anwer of calculate 

if final < 18.5:
    print(f"Your BMI is {final} and your Underweight")

elif final >= 18.5:
    print(f"Your BMI is {final} and you are Normal weight")

elif final >= 24.9:
    print(f"Your BMI is {final} and you are Over weight")

elif final >= 34.9:
    print(f"Your BMI is {final} and you are Obesity class I")
    
elif final >= 39.9:
    print(f"Your BMI is {final} and you are Obesity class II")

elif final >= 40:
    print(f"Your BMI is {final} and you are Obesity class III")
