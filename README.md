# HIT_PYTHON_PUBLC_2024
Bài 1: Python là ngôn ngữ thông dịch vì nó thực thi mã nguồn từng dòng một bằng trình thông dịch, không biên dịch trước thành mã máy, và yêu cầu môi trường thông dịch để chạy mã nguồn.Nếu có lỗi trong mã chương trình, nó sẽ ngừng chạy. Do đó, lập trình viên có thể nhanh chóng tìm ra lỗi trong đoạn mã.
Bài 2:
Các kiểu dữ liệu trong Python:
1. Numeric Types
int: Số nguyên (ví dụ: x=10, 12..)
float: Số thực, số dấu phẩy động (ví dụ: y= -2.5, 3.14)
complex: Số phức (ví dụ: z= 1+2j, -3+4j)
2. Text Type
str: Chuỗi ký tự (ví dụ: s = "Hello Helloo")
3. Sequence Types
list: Một danh sách các mục có thể thay đổi, có thứ tự (ví dụ: fruits = ["apple", "banana", "cherry"])
tuple: Một danh sách các mục không thể thay đổi, có thứ tự (ví dụ:  point =(1,2,3))
range: Đại diện cho một dãy số 
ví dụ:
for i in range(5):
    print(i)
4. Boolean type
bool: Đại diện cho hai giá trị True hoặc False
is_valid = True
is_empty = False
5. Mapping Type
dict: Một tập hợp các cặp khóa-giá trị có thể thay đổi, không có thứ tự
vd:
person = {"name": "Alice", "age": 25}
6. Set Types
set: Một tập hợp các mục không có thứ tự và không trùng lặp 
ví dụ
unique_numbers = {1, 2, 3, 4}
7. Binary Types
bytes: Một chuỗi các byte không thể thay đổi 
ví dụ
data = b"Hello
bytearray: Một chuỗi các byte có thể thay đổi
ví dụ
data = bytearray(b"Hello")
data[0] = 72
memoryview: Cho phép truy cập trực tiếp vào byte dữ liệu 
ví dụ
data = bytearray(b"Hello")
view = memoryview(data)

Các toán tử trong python:
1. Toán tử số học (Arithmetic Operators)
+: Phép cộng
-: Phép trừ
*: Phép nhân
/: Phép chia
%: Phép chia lấy dư
**: Lũy thừa
//: Phép chia lấy nguyên
ví dụ:

a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.3333333333333335
print(a % b)    # 1
print(a ** b)   # 1000
print(a // b)   # 3

2. Toán tử gán (Assignment Operators)
=: Gán
+=: Cộng và gán
-=: Trừ và gán
*=: Nhân và gán
/=: Chia và gán
%=: Chia lấy dư và gán
**=: Lũy thừa và gán
//=: Chia lấy nguyên và gán
ví dụ :

a = 10
a += 5    # a = a + 5
print(a)  # 15

a -= 3    # a = a - 3
print(a)  # 12

a *= 2    # a = a * 2
print(a)  # 24

a /= 4    # a = a / 4
print(a)  # 6.0

a %= 5    # a = a % 5
print(a)  # 1.0

a **= 3   # a = a ** 3
print(a)  # 1.0

a //= 1   # a = a // 1
print(a)  # 1.0  
3. Toán tử so sánh (Comparison Operators)
==: So sánh bằng
!=: So sánh khác
>: Lớn hơn
<: Nhỏ hơn
>=: Lớn hơn hoặc bằng
<=: Nhỏ hơn hoặc bằng
ví dụ :
a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True
4. Toán tử logic (Logical Operators)
and: Phép và
or: Phép hoặc
not: Phép phủ định
ví dụ :
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
5. Toán tử nhị phân (Bitwise Operators)
&: AND
|: OR
^: XOR
~: NOT
<<: Dịch trái
>>: Dịch phải
python
Sao chép mã
a = 10  # 1010 in binary
b = 4   # 0100 in binary

print(a & b)   # 0 (0000 in binary)
print(a | b)   # 14 (1110 in binary)
print(a ^ b)   # 14 (1110 in binary)
print(~a)      # -11 (inverts all bits)
print(a << 1)  # 20 (10100 in binary)
print(a >> 1)  # 5 (0101 in binary)
6. Toán tử xác tực (Identity Operators)
is: Kiểm tra xem hai biến có cùng một đối tượng không
is not: Kiểm tra xem hai biến không phải cùng một đối tượng
ví dụ :
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       # True
print(a is c)       # False
print(a is not c)   # True
7. Toán tử khai thác (Membership Operators)
in: Kiểm tra xem một giá trị có nằm trong một chuỗi, danh sách, tập hợp hoặc từ điển không
not in: Kiểm tra xem một giá trị không nằm trong một chuỗi, danh sách, tập hợp hoặc từ điển
python
Sao chép mã
a = [1, 2, 3]

print(1 in a)       # True
print(4 in a)       # False
print(4 not in a)   # True
8. Toán tử điều kiện (Conditional Operator/Ternary Operator)
Toán tử ba ngôi trong Python được sử dụng để viết các câu lệnh điều kiện trong một dòng.
ví dụ :
a = 5
b = 10

max_value = a if a > b else b
print(max_value)  # 10

Mệnh đề điều kiện:
1. Mệnh đề If else: cho phép kiểm tra nhiều điều kiện khác nhau. Chỉ đoạn mã đầu tiên có điều kiện đúng (True) sẽ được thực hiện
ví dụ :
x = 5
if x > 5:
    print("x lớn hơn 5")
elif x == 5:
    print("x bằng 5")
else:
    print("x nhỏ hơn 5")

Vòng lặp:
1. Vòng lặp for
Vòng lặp for lặp qua một chuỗi các phần tử (như một danh sách, một chuỗi, hoặc một phạm vi).
# Vòng lặp qua một danh sách
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Vòng lặp qua một phạm vi
for i in range(5):
    print(i)
2. Vòng lặp while
Vòng lặp while lặp lại đoạn mã bên trong miễn là điều kiện còn đúng (True).

count = 0
while count < 5:
    print(count)
    count += 1

3. Các câu lệnh điều khiển vòng lặp
break: Kết thúc vòng lặp ngay lập tức.

for i in range(10):
    if i == 5:
        break
    print(i)

continue: Bỏ qua phần còn lại của vòng lặp và tiếp tục với lần lặp tiếp theo.

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

else: Đoạn mã trong else được thực hiện khi vòng lặp kết thúc mà không gặp phải break.
python
Sao chép mã
for i in range(5):
    print(i)
else:
    print("Vòng lặp kết thúc không gặp break")

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Vòng lặp kết thúc không gặp break")

Kiểu dữ liệu true, false:
Trong Python, kiểu dữ liệu đại diện cho các giá trị boolean là bool. Kiểu dữ liệu này chỉ có hai giá trị: True và False.
Sử dụng boolean trong các mệnh đề điều kiện và sử dụng boolean trong các toán tử logic
Các giá trị boolean có thể được kết hợp và thao tác bằng các toán tử logic như and, or, và not.# HIT_WEB_PUBLIC_2024.
# HIT_WEB_PUBLIC_2024.
# HIT_WEB_PUBLIC_2024.
