t1 = int(input("Time Elapsed:"))
t2 = int(input('Half Life:'))
N = int(input('initial quantity:'))

N1 = N*((0.5)**(t1/t2))
print('quantity of the substance remaining:', N1)