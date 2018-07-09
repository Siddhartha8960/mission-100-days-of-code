num1 = int(input("Enter 1st number "))
num2 = int(input("Enter 2nd number "))
num3 = int(input("Enter 3rd number "))
num4 = int(input("Enter 4th number "))
if num1<num2:
    min1=num1
else:
    min1=num2
while(1):
    if (min1%num1==0 and min1%num2==0):
        lcm1=min1
        break
    min1=min1+1        
if num3<num4:
    min2=num3
else:
    min2=num4
while(1):
    if (min2%num3==0 and min2%num4==0):
        lcm2=min2
        break
    min2=min2+1
if lcm1<lcm2:
    min3=lcm1
else:
    min3=lcm2
while(1):
    if (min3%lcm1==0 and min3%lcm2==0):
        print(min3,"is the lcm")
        lcm=min3
        break
    min3=min3+1
    
    #hcf

def hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0)and (y%i==0)):
            hcf=i
    return hcf                  
final1=hcf(num1,num2)
final2=hcf(num3,num4)
final=hcf(final1,final2)
print(final,"is the hcf")











