p = float(input("Enter the principal=> "))
r = float(input("Enter the rate of interest=> "))
n = float(input("Enter the nujmber of times => "))
a = (p*(1+(r/100))**n)
ci=a-p
print(a,"is the amount")
print(ci,"is the required compound interest")