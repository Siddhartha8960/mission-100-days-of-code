num1 = int(input("Enter the first number "))
num2 = int(input("Enter he second number "))
choice = int(input("Enter your chioce 1 for sum, 2 for subtract, 3 fro multiply and 4 for divide "))
if choice==1:
 add = (num1) + (num2)
 print(add,"is the addition")
elif choice==2:
 sub = (num1) - (num2)
 print(sub)
elif choice==3:
 mul = (num1) * (num2)
 print(mul)
elif choice==4:
 div = (num1) / (num2)
 print(div)
else:
 print("Enter correct choice")
 