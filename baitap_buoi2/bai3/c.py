#Biện luận nghiệm của phương trình bậc 2 một ẩn
import math

a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

if(a==0):
    if(b==0):
        if(c==0):
            print("phuong trinh vo so nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        if(c==0):
            print("phuong trinh co nghiem x= 0")
        else:
            print("phuong trinh co nghiem x= ", -c/b)
else:
    denta = math.pow(b,2) - 4*a*c

    if(denta<0):
        print("phuong trinh vo nghiem")
    elif(denta == 0):
        print("phuong trinh co nghiem kep: x= ", -b/(2*a))
    else:
        print("phuong trinh co hai nghiem: x1= ", (-b + math.sqrt(denta))/(2*a), " x2= ", (-b - math.sqrt(denta))/(2*a))