#S(n) = 1 - 2 + 3 - 4 + 5 + .... + (2*n + 1)
n = int(input("n= "))

sum = 0

for i in range(1,2*n + 2):
    if(i %2 != 0):
        sum += i
    else:
        sum -= i
print("tong la: ", sum)