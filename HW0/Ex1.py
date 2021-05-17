t = int(input("Number of time periods elapsed:"))
r = int(input('Interest rate:'))
n = int(input('Number of time interest applied per time period:'))
P = int(input('Initial principal balance:'))

A = P*((1+(r/n))**(n*t))
print('quantity of the substance remaining:', A)