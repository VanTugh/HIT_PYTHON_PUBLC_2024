# Tính tổng các ước số của một số nguyên dương:
# Viết một chương trình yêu cầu người dùng nhập một số nguyên dương n. Tính và in ra tổng của tất cả các ước số của n. Ước số của một số là các số mà chia hết cho số đó mà không dư. Ví dụ: Ước số của 6 là 1, 2, 3, và 6.
n = int(input("n= "))
sum = 0
for i in range(1, n+1):
    if(n%i==0):
        sum += i
print("tong la: ", sum)