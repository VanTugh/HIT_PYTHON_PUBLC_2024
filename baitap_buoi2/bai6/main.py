#Nhập vào 1 số n. In ra tất cả các số hoàn hảo từ 1 đến n. ( Số hoàn hảo là số mà tổng các ước của nó (không tính chính nó) bằng chính nó ).
n = int(input("n= "))
for j in range(1, n+1):
    tong = 0

    i = 1

    while(i<j):
        if(j%i==0):
            tong += i
        i +=1

    if(tong == j):
        print(j, " la so hoan hao")
    