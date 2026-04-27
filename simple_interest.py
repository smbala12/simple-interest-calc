#Python interest calculator
#Formula A = P(1+r/n)^nt
'''
A = amount
P = principal
r = rate of interest
n = number of times interest is compounded per year
t = time (in years)
'''
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the rate of interest%: "))
n = int(input("Enter the number of times interest is compounded(only years): "))
t = int(input("Enter the time (in years): "))
amount = principal*(1+rate/n)**(n*t)
print (f"The amount is {amount}")