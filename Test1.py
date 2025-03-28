# bai 1
from collections import Counter
my_tuple = tuple(map(int, input(" hay nhap day so vao day : ").split()))
count = Counter(my_tuple)
result = [num for num, dem in count.items() if dem % 5 == 0 and dem % 10 != 0 ]
if result :
    print(*result)
else :
    print(" khong co ")
# bai 2
def kiemtraso():
    while True:
        try:
            x = int(input("Nhập số x (0 < x < 10000):\n ")) 
            if 0<x<10000:  
                return x
            else:
                print(" hay nhap lai ")
        except ValueError:
            print("Lỗi! Vui lòng nhập một số nguyên hợp lệ.")
def dem_so_buoc_toi_thieu(x) :
    return ((x+2)//3)

if __name__ == "__main__":
# t = input(int," nhap cac so di : ")
    x = kiemtraso()  # Kiểm tra giá trị x
    print(dem_so_buoc_toi_thieu(x))  # In kết quả