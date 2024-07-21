#S(n) = 1 + ½ + ⅓ + ¼ +.....+1/n
n = int(input("n= "))

sum = 0

for i in range(1, n+1):
    sum += 1/i
print("tong la: ", sum)