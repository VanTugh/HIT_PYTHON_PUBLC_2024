
character_name = "TungAnXoi"
character_age= "27"
print("Cứ thế thôi lăn lội phải ra ngoài kia tìm con số lớn")
print(f"{character_name} vẫn bên anh nên chưa {character_age} giây nào anh cô đơn")
print("Em cứ đi nhé nếu em thích ở bên người hơn")
print("Anh đâu trách chi, anh chỉ gửi một lời cảm ơn")
s = input("Nhập chuỗi: ")
print("Chuỗi vừa nhập:", s)
a=3.3
b=2
print(a//b)
print(a == b)
if a>b :
    print("dangrangto")
else :
    print("sai oi")
# toan tu ba ngoi
a=1
kq=a if a % 2 == 0 else a*2
print(kq)
for i in s :
    print(i)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Lặp qua toàn bộ mảng
        swapped = False  # Biến kiểm tra có hoán đổi hay không
        for j in range(n - i - 1):  # Giảm dần phạm vi lặp do phần tử lớn nhất đã được đặt đúng chỗ
            if arr[j] > arr[j + 1]:  # Nếu phần tử trước lớn hơn phần tử sau, hoán đổi
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Đánh dấu có hoán đổi
        if not swapped:  # Nếu không có phần tử nào bị hoán đổi, dừng vòng lặp
            break
    return arr

# Kiểm tra thuật toán
arr = [64, 34, 25, 12, 22, 11, 90]
print("Mảng đã sắp xếp:", bubble_sort(arr))
my_string = """"Hello, im ma wtf king booi """
print(my_string)
# xoa chuoi
del my_string
print(s.split())
sss = input("Nhập chuỗi: ")
print("Chuỗi vừa nhập:", sss.strip())
if sss.isspace() :
    print(" chuoi roan rong")
else :
    word= sss.split()
    print(len(word))

T=("tao", "cam","quyt")
(a,b,c)=T
print(a)
print(b)
print(c)
my_tuple=(12,2,[32,4,5],5)
my_tuple[2][2]=10
print(my_tuple)
 #count()
#Trả về số lượng phần tử trong tuple
#index(item)
#Trả về vị trí đầu tiên xuất hiện item
print(my_tuple.count(5))
print(my_tuple.index(5))
#set
my_set={1,2,3,"hoa"}
my_set.add("hong")
# khong the truyen truc tiep gia tri vao updateupdate
my_set.update(T)

my_set.remove(1)
print(my_set)