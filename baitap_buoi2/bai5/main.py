# Bài 5: Nhập vào 1 số n. Viết chương trình in ra tất cả các số Armstrong bậc 3 từ 1 đến n. (Số Armstrong bậc 3 là số mà tổng lập phương của các chữ số của nó bằng chính nó)
n = int(input("n= "))

for i in range(1, n+1):
    tong = 0
    m = i
    temp = i
    while(temp>0):
        a = temp%10
        tong += pow(a,3)
        temp = temp//10
    if(tong == m):
        print(m," la so armstrong bac 3 ")
        