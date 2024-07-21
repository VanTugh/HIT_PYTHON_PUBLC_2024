# Kiểm tra tam giác:
# Viết chương trình yêu cầu người dùng nhập vào 3 số nguyên dương. Kiểm tra xem 3 số đó có tạo thành tam giác hay không? Nếu có thì đó là tam giác gì?(Cân, đều, vuông, nhọn, tù)
import math
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

if a+b>c and b+c>a and c+a>b:
    if(a==b and b==c and c==a):
        print("day la tam giac deu")
    elif(a==b or b==c or c==a):
        print("day la tam giac can")
    elif(a == math.sqrt(math.pow(b,2) + math.pow(c,2)) or b == math.sqrt(math.pow(a,2) + math.pow(c,2)) or c == math.sqrt(math.pow(a,2) + math.pow(b,2))):
        print("day la tam giac vuong")
    elif(math.pow(a,2) > math.sqrt(math.pow(b,2) + math.pow(c,2)) or math.pow(b,2) > math.sqrt(math.pow(a,2) + math.pow(c,2)) or math.pow(c,2) > math.sqrt(math.pow(a,2) + math.pow(b,2))):
        print("day la tam giac tu")
    else:
        print("day la tam giac nhon")
else:
    print("day khong la tam giac")