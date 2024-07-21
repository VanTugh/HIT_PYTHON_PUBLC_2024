# Viết một chương trình yêu cầu người dùng nhập một số nguyên dương. Tính và in ra tổng các chữ số của số đó.
# Ví dụ: Đối với số 12345, tổng các chữ số là 1 + 2 + 3 + 4 + 5 = 15.
n = int(input("n= "))
sum = 0
while(n>0):
    a = n%10
    sum+= a
    n = n//10
print("tong la: ", sum)