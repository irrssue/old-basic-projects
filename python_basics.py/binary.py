def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = int(input("enter decimal number: "))

convertToBinary(dec)
print()
