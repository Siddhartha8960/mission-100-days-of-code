import random
operator = ['+','-','*','/']
num1 = random.randint(0,999)
num2 = random.randint(0,999)
operation = random.choice(operator)
print(num1, operation, num2)
uresult =  int(input('Calculate the answer ? \n'))
result = eval(str(num1) + operation + str(num2))
if (uresult == result):
    print('Great,You have got the right answer')
elif (uresult != result):
    print('Sorry,Work on your maths')
else:
    print("please calculate")
