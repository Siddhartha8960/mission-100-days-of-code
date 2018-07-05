def fact(num):
    if num == 1:
        return 1
    else:
        return(num*fact(num-1))

val = int(input("Enter any number "))
print("The required factorial is ", fact(val))