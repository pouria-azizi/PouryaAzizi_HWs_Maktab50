temp = 0
s = 0
x = 1
for i in range(1, 11):
    temp = temp + i * pow(x, i)
    s = s + pow(-1, i+1)*(1/temp)
    print(s)
print('result : ', s)