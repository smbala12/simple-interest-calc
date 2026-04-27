principle = 0
rate = 0 
time = 0 

while True:
    principle = float(input("Enter a principle amount: "))
    if principle <0:
        print("The value of principle cant be zero")
    else:
      break

while True:
    rate = float(input("Enter a Rate: "))
    if rate <0:
        print ("The rate cant be zero")
    else:
      break

while True:
    time = int(input("Enter a time in years: "))
    if time <0:
        print ("The time cant be Zero")
    else:
      break

total = principle * (1 + (rate / 100) * time)
print (f"The balance after {time} years is: ₹{total :,.2f}")
