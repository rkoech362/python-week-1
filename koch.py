print("\n1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
option=int(input("choose an operation to perform: "))
if (option ==1):
  num1=int(input("enter the first number:"))
  num2=int(input("enter the second number: "))
  print (num1+num2)

elif (option==2):
   num1=int(input("enter first number: "))
   num2=int(input("enter second number: "))
   print( num1-num2)
elif (option==3):
   num1=int(input("enter first number: "))
   num2=int(input("enter second number: "))
   print( num1*num2)   
elif (option==4):
 num1=int(input("enter the first number: "))
 num2=int(input("enter second number: "))
 print( num1//num2)
else:
  print("invalid entry")