a = int(input()) 
print (a)
#LIST
b=[1,2,3]
print(type(b))
print(b[-2])
#TUPLE
t=(3,)
print(type(t))

""""
nếu để 3 như này thì type = int , 
t=(3,) --> tuple
truy suất trong tuple nhanh hơn list
dic : gồm key(K THAY ĐỔI DC) và value(thay đổi dc)
các key phải khác nhau 


"""
# kiểu dữ liệu dictionary

my_dict ={
    "tên ":"Tùn",
    "giới tính ":"nam", 
    "năm" : 2005
}
print(my_dict)
# hàm print trong python

u=50
v=6
print(f'{u} + {v} = {u+v}')
print(f'{u} - {v} = {u-v}')
print(f'{u} * {v} = {u*v}')
print(f'{u} / {v} = {u/v}')
print(f'{u} % {v} = {u%v}')
print(f'{u} ** {v} = {u**v}')
print(f'{u} // {v} = {u//v}')

#toan tu so sanh
print(u<v or u>v)
print(u<v and u>v)

#
mn=1
y={1,2,3,4}
print(mn in y) # ktra xem mn co trong y ka(not in nguoc lai voi in)
# is: tra ve true neu 2 bien cung tro ve 1 o nho
mm=5
ny=5
print(mm is ny) # true(not is nguoc lai voi is)
# if else
if mn>u :
    print("Tung jjs")
else :
    print("haha")

    # thụt lề trong pyhton(xem slide)
# vd
if(mn<u):
   print("Tung tung")
   print("huhu")
print("haha")   

# nhập vào ba số a,b,c . In ra xem số đó có phải tam giác k
aa = float(input())
bb = float(input())
cc = float(input())
if aa+bb>cc and aa+cc>bb and bb+cc>aa :
  print("tam giác nè")
else :
   print("không phại tam giác nhé")
   # else if= elif
   # toán tử 3 ngôi trong python
res = aa if aa < 10 else aa**2
print(res)
# giá trị truly và falsy
# vòng lặp trong python
for i in range(1,6,2):#start, stop, step
 print(i, end=' ')
 #cách 2
 mu={1,2,3,4}
for i in mu:
 print(i, end=' ')

while u>30 :
  print(u,end=' ')
  u-=10
  if u==40 :
     break
  # pass : bỏ qua vòng lặp
for idx , val in enumerate(mu):
     print(idx, val)
for i in range(9) :
 print(i, end=' ')
else :
   print("Tungdeptrai") 