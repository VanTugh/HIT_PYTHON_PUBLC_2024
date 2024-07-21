# Cho 2 số a, b bất kỳ. Hãy in ra màn hình:
# a.    a cộng b
# b.    a trừ b
# c.    a nhân b
# d.    a chia lấy nguyên b
# e.    a mũ b
# f.     a chia dư b
# g.    so sánh a và b (lớn hơn, nhỏ hơn hay bằng)
# h.    a AND b
# i.     a OR b
# j.     a XOR b
# k.   NOT a == b
# l.    a dịch phải 1 đơn vị
# m.  a dịch trái 1 đơn vị
import math
a = int(input("a= "))
b = int(input("b= "))

print("a + b = ", a+b)
print("a - b = ", a-b)
print("a * b = ", a*b)
print("a // b = ", a//b)
print("a ^ b = ", math.pow(a,b))
print("a % b = ", a%b)
print("a > b", a>b)
print("a < b", a<b)
print("a = b",a == b)
print("a and b", a&b)
print("a or b", a | b)
print("a xor b", a ^ b)
print("not a==b", not(a==b))
print("a >> 1", a>>1)
print("a << 1", a<<1)